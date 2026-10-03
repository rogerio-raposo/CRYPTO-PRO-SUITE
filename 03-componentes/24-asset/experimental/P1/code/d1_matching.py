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


@dataclass(frozen=True)
class EventMatchedPair:
    a_index: int
    b_index: int
    event_type: str
    reference_kind: str
    bar_distance: int
    normalized_reference_price_distance: str


@dataclass(frozen=True)
class EventMatchingResult:
    matched_pairs: tuple[EventMatchedPair, ...]
    unmatched_a: tuple[int, ...]
    unmatched_b: tuple[int, ...]
    match_count: int
    event_stability: str | None


@dataclass(frozen=True)
class ProtectedMatchedPair:
    a_index: int
    b_index: int
    a_extremum_index: int
    b_extremum_index: int
    promotion_bar_distance: int


@dataclass(frozen=True)
class ProtectedMatchingResult:
    matched_pairs: tuple[ProtectedMatchedPair, ...]
    unmatched_a: tuple[int, ...]
    unmatched_b: tuple[int, ...]
    match_count: int
    protected_stability: str | None


def match_events(
    events_a: Sequence,
    events_b: Sequence,
    candles: Sequence[dict],
    *,
    timeframe: str,
) -> EventMatchingResult:
    """Revision 01 BASE event matching.

    Events match only when type/kind agree, occurrence times are inside the BASE
    bar window, and reference prices are within 1.0 ATR14 at the later event.
    """
    max_bars, _ = _window(timeframe, "BASE")
    atr14 = wilder_atr(candles, 14)

    @dataclass(frozen=True)
    class _EventPath:
        pairs: tuple[EventMatchedPair, ...]
        bar_sum: int
        price_sum: Decimal

        @property
        def matches(self) -> int:
            return len(self.pairs)

        @property
        def signature(self) -> tuple[tuple[int, int], ...]:
            return tuple((p.a_index, p.b_index) for p in self.pairs)

    def better(a: _EventPath, b: _EventPath) -> _EventPath:
        ka=(-a.matches,a.bar_sum,a.price_sum,a.signature)
        kb=(-b.matches,b.bar_sum,b.price_sum,b.signature)
        return a if ka <= kb else b

    def eligible(i: int, j: int) -> EventMatchedPair | None:
        a=events_a[i]
        b=events_b[j]
        if a.event_type != b.event_type or a.reference_kind != b.reference_kind:
            return None
        bar_distance=abs(int(a.bar_index)-int(b.bar_index))
        if bar_distance > max_bars:
            return None
        compare_index=max(int(a.bar_index),int(b.bar_index))
        if compare_index >= len(atr14):
            return None
        atr=atr14[compare_index]
        if atr is None or atr <= 0:
            return None
        distance=abs(_d(a.reference_price)-_d(b.reference_price))/atr
        if distance > Decimal("1.0"):
            return None
        return EventMatchedPair(
            a_index=i,
            b_index=j,
            event_type=a.event_type,
            reference_kind=a.reference_kind,
            bar_distance=bar_distance,
            normalized_reference_price_distance=str(distance),
        )

    @lru_cache(maxsize=None)
    def solve(i: int, j: int) -> _EventPath:
        if i >= len(events_a) or j >= len(events_b):
            return _EventPath((),0,Decimal("0"))
        best=better(solve(i+1,j),solve(i,j+1))
        pair=eligible(i,j)
        if pair is not None:
            tail=solve(i+1,j+1)
            candidate=_EventPath(
                pairs=(pair,)+tail.pairs,
                bar_sum=pair.bar_distance+tail.bar_sum,
                price_sum=_d(pair.normalized_reference_price_distance)+tail.price_sum,
            )
            best=better(best,candidate)
        return best

    path=solve(0,0)
    matched_a={p.a_index for p in path.pairs}
    matched_b={p.b_index for p in path.pairs}
    if not events_a and not events_b:
        stability=None
    else:
        stability=str(
            Decimal(2*path.matches)/Decimal(len(events_a)+len(events_b))
        )
    return EventMatchingResult(
        matched_pairs=path.pairs,
        unmatched_a=tuple(i for i in range(len(events_a)) if i not in matched_a),
        unmatched_b=tuple(i for i in range(len(events_b)) if i not in matched_b),
        match_count=path.matches,
        event_stability=stability,
    )


def match_protected_promotions(
    protected_a: Sequence,
    protected_b: Sequence,
    swing_matching: MatchingResult,
    *,
    timeframe: str,
) -> ProtectedMatchingResult:
    """Match Protected Swing promotions through their already-matched underlying swings."""
    max_bars,_=_window(timeframe,"BASE")
    promotions_a=[
        (i,x) for i,x in enumerate(protected_a)
        if str(x.action).startswith("PROMOTE:")
    ]
    promotions_b=[
        (i,x) for i,x in enumerate(protected_b)
        if str(x.action).startswith("PROMOTE:")
    ]
    matched_underlying={
        (p.a_extremum_index,p.b_extremum_index)
        for p in swing_matching.matched_pairs
    }

    eligible: list[ProtectedMatchedPair]=[]
    used_b: set[int]=set()
    for ai,a in promotions_a:
        choices=[]
        for bi,b in promotions_b:
            if bi in used_b:
                continue
            if (a.extremum_index,b.extremum_index) not in matched_underlying:
                continue
            distance=abs(int(a.bar_index)-int(b.bar_index))
            if distance <= max_bars:
                choices.append((distance,bi,b))
        if not choices:
            continue
        choices.sort(key=lambda x:(x[0],int(x[2].bar_index),x[1]))
        distance,bi,b=choices[0]
        used_b.add(bi)
        eligible.append(
            ProtectedMatchedPair(
                a_index=ai,
                b_index=bi,
                a_extremum_index=int(a.extremum_index),
                b_extremum_index=int(b.extremum_index),
                promotion_bar_distance=distance,
            )
        )

    matched_a={p.a_index for p in eligible}
    matched_b={p.b_index for p in eligible}
    denominator=len(promotions_a)+len(promotions_b)
    stability=None if denominator==0 else str(Decimal(2*len(eligible))/Decimal(denominator))
    return ProtectedMatchingResult(
        matched_pairs=tuple(eligible),
        unmatched_a=tuple(i for i,_ in promotions_a if i not in matched_a),
        unmatched_b=tuple(i for i,_ in promotions_b if i not in matched_b),
        match_count=len(eligible),
        protected_stability=stability,
    )


def event_order_consistency(events_a: Sequence, events_b: Sequence) -> str | None:
    """LCS over (event_type, reference_kind) event tokens."""
    if not events_a and not events_b:
        return None
    a=[(x.event_type,x.reference_kind) for x in events_a]
    b=[(x.event_type,x.reference_kind) for x in events_b]
    previous=[0]*(len(b)+1)
    for token_a in a:
        current=[0]
        for j,token_b in enumerate(b,1):
            if token_a==token_b:
                current.append(previous[j-1]+1)
            else:
                current.append(max(previous[j],current[-1]))
        previous=current
    return str(Decimal(previous[-1])/Decimal(max(len(a),len(b))))
