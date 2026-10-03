#!/usr/bin/env python3
"""ASSET-P1-D1-001 deterministic monotonic swing matching."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from functools import lru_cache
from typing import Sequence

from d1_swings import D1Error, Swing, wilder_atr


@dataclass(frozen=True)
class MatchedPair:
    a_index: int
    b_index: int
    a_extremum_index: int
    b_extremum_index: int
    bar_distance: int
    normalized_price_distance: str


@dataclass(frozen=True)
class MatchingResult:
    matched_pairs: tuple[MatchedPair, ...]
    unmatched_a: tuple[int, ...]
    unmatched_b: tuple[int, ...]
    match_count: int
    swing_stability: str


def _d(value) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def _window(timeframe: str, mode: str) -> tuple[int, Decimal]:
    table = {
        ("4h", "STRICT"): (2, Decimal("0.5")),
        ("4h", "BASE"): (3, Decimal("1.0")),
        ("4h", "WIDE"): (6, Decimal("1.5")),
        ("1d", "STRICT"): (1, Decimal("0.5")),
        ("1d", "BASE"): (2, Decimal("1.0")),
        ("1d", "WIDE"): (3, Decimal("1.5")),
    }
    try:
        return table[(timeframe, mode)]
    except KeyError as exc:
        raise D1Error(f"Unsupported matching configuration: {timeframe}/{mode}") from exc


@dataclass(frozen=True)
class _Path:
    pairs: tuple[MatchedPair, ...]
    bar_sum: int
    price_sum: Decimal

    @property
    def matches(self) -> int:
        return len(self.pairs)

    @property
    def signature(self) -> tuple[tuple[int, int], ...]:
        return tuple((p.a_extremum_index, p.b_extremum_index) for p in self.pairs)


def _better(a: _Path, b: _Path) -> _Path:
    ka = (-a.matches, a.bar_sum, a.price_sum, a.signature)
    kb = (-b.matches, b.bar_sum, b.price_sum, b.signature)
    return a if ka <= kb else b


def match_swings(
    swings_a: Sequence[Swing],
    swings_b: Sequence[Swing],
    candles: Sequence[dict],
    *,
    timeframe: str,
    mode: str = "BASE",
) -> MatchingResult:
    max_bars, max_price_atr = _window(timeframe, mode)
    atr14 = wilder_atr(candles, 14)

    def eligible(i: int, j: int) -> MatchedPair | None:
        a = swings_a[i]
        b = swings_b[j]
        if a.kind != b.kind:
            return None
        bar_distance = abs(a.extremum_index - b.extremum_index)
        if bar_distance > max_bars:
            return None
        compare_index = max(a.confirmation_index, b.confirmation_index)
        if compare_index >= len(atr14):
            return None
        atr = atr14[compare_index]
        if atr is None or atr <= 0:
            return None
        distance = abs(_d(a.price) - _d(b.price)) / atr
        if distance > max_price_atr:
            return None
        return MatchedPair(
            a_index=i,
            b_index=j,
            a_extremum_index=a.extremum_index,
            b_extremum_index=b.extremum_index,
            bar_distance=bar_distance,
            normalized_price_distance=str(distance),
        )

    @lru_cache(maxsize=None)
    def solve(i: int, j: int) -> _Path:
        if i >= len(swings_a) or j >= len(swings_b):
            return _Path((), 0, Decimal("0"))

        best = solve(i + 1, j)
        best = _better(best, solve(i, j + 1))

        pair = eligible(i, j)
        if pair is not None:
            tail = solve(i + 1, j + 1)
            matched = _Path(
                pairs=(pair,) + tail.pairs,
                bar_sum=pair.bar_distance + tail.bar_sum,
                price_sum=_d(pair.normalized_price_distance) + tail.price_sum,
            )
            best = _better(best, matched)
        return best

    path = solve(0, 0)
    matched_a = {p.a_index for p in path.pairs}
    matched_b = {p.b_index for p in path.pairs}
    denominator = len(swings_a) + len(swings_b)
    stability = (
        Decimal("1")
        if denominator == 0
        else Decimal(2 * path.matches) / Decimal(denominator)
    )

    return MatchingResult(
        matched_pairs=path.pairs,
        unmatched_a=tuple(i for i in range(len(swings_a)) if i not in matched_a),
        unmatched_b=tuple(i for i in range(len(swings_b)) if i not in matched_b),
        match_count=path.matches,
        swing_stability=str(stability),
    )
