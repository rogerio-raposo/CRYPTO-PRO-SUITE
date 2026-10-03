#!/usr/bin/env python3
"""ASSET-P1-D1-001 volatility and swing detectors.

Experimental / non-normative. Uses closed candles only.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
from statistics import median
from typing import Sequence


class D1Error(RuntimeError):
    pass


@dataclass(frozen=True)
class Swing:
    kind: str
    extremum_index: int
    extremum_open_us: int
    price: str
    confirmation_index: int
    confirmation_end_us: int
    method: str
    profile_id: str
    volatility_ref: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class DetectionResult:
    swings: tuple[Swing, ...]
    anomalies: tuple[dict, ...]


def _d(value) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def true_range(candles: Sequence[dict]) -> list[Decimal]:
    out: list[Decimal] = []
    previous_close: Decimal | None = None
    for candle in candles:
        high = _d(candle["high"])
        low = _d(candle["low"])
        close = _d(candle["close"])
        tr = high - low
        if previous_close is not None:
            tr = max(tr, abs(high - previous_close), abs(low - previous_close))
        out.append(tr)
        previous_close = close
    return out


def wilder_atr(candles: Sequence[dict], n: int) -> list[Decimal | None]:
    if n < 1:
        raise D1Error("ATR window must be positive.")
    tr = true_range(candles)
    out: list[Decimal | None] = [None] * len(tr)
    if len(tr) < n:
        return out
    current = sum(tr[:n], Decimal("0")) / Decimal(n)
    out[n - 1] = current
    for i in range(n, len(tr)):
        current = (current * Decimal(n - 1) + tr[i]) / Decimal(n)
        out[i] = current
    return out


def median_true_range(candles: Sequence[dict], n: int) -> list[Decimal | None]:
    if n < 1:
        raise D1Error("Median TR window must be positive.")
    tr = true_range(candles)
    out: list[Decimal | None] = [None] * len(tr)
    for i in range(n - 1, len(tr)):
        out[i] = Decimal(str(median(tr[i - n + 1 : i + 1])))
    return out


def _swing(
    kind: str,
    extremum_index: int,
    confirmation_index: int,
    price: Decimal,
    candles: Sequence[dict],
    method: str,
    profile_id: str,
    volatility_ref: Decimal | None = None,
) -> Swing:
    return Swing(
        kind=kind,
        extremum_index=extremum_index,
        extremum_open_us=int(candles[extremum_index]["open_time_us"]),
        price=str(price),
        confirmation_index=confirmation_index,
        confirmation_end_us=int(candles[confirmation_index]["interval_end_us"]),
        method=method,
        profile_id=profile_id,
        volatility_ref=None if volatility_ref is None else str(volatility_ref),
    )


def fixed_window_pivots(candles: Sequence[dict], window: int) -> DetectionResult:
    """M1 — causal fixed-window pivot.

    A pivot extremum is recognized only when all right-side bars exist.
    Once a swing is confirmed it is immutable. A later same-type pivot
    before an opposite confirmed swing is diagnostically ignored rather
    than retroactively replacing history.
    """
    if window < 1:
        raise D1Error("M1 window must be positive.")
    candidates: list[Swing] = []
    anomalies: list[dict] = []
    for i in range(window, len(candles) - window):
        bars = candles[i - window : i + window + 1]
        highs = [_d(x["high"]) for x in bars]
        lows = [_d(x["low"]) for x in bars]
        high = _d(candles[i]["high"])
        low = _d(candles[i]["low"])
        confirmation = i + window
        is_high = high == max(highs) and highs.count(high) == 1
        is_low = low == min(lows) and lows.count(low) == 1
        if is_high and is_low:
            anomalies.append(
                {
                    "type": "AMBIGUOUS_DUAL_PIVOT",
                    "extremum_index": i,
                    "confirmation_index": confirmation,
                    "action": "NO_CONFIRMATION",
                }
            )
            continue
        if is_high:
            candidates.append(
                _swing(
                    "HIGH",
                    i,
                    confirmation,
                    high,
                    candles,
                    "M1",
                    f"M1-w{window}",
                )
            )
        if is_low:
            candidates.append(
                _swing(
                    "LOW",
                    i,
                    confirmation,
                    low,
                    candles,
                    "M1",
                    f"M1-w{window}",
                )
            )

    candidates.sort(
        key=lambda x: (
            x.confirmation_index,
            x.extremum_index,
            0 if x.kind == "HIGH" else 1,
        )
    )
    confirmed: list[Swing] = []
    for candidate in candidates:
        if not confirmed or candidate.kind != confirmed[-1].kind:
            confirmed.append(candidate)
        else:
            anomalies.append(
                {
                    "type": "SAME_TYPE_CONFIRMED_PIVOT_IGNORED",
                    "kind": candidate.kind,
                    "extremum_index": candidate.extremum_index,
                    "confirmation_index": candidate.confirmation_index,
                }
            )
    return DetectionResult(tuple(confirmed), tuple(anomalies))


def _threshold_detector(
    candles: Sequence[dict],
    *,
    method: str,
    threshold: Decimal,
    profile_id: str,
    volatility: Sequence[Decimal | None] | None = None,
) -> DetectionResult:
    if not candles:
        return DetectionResult((), ())
    if threshold <= 0:
        raise D1Error("Reversal threshold must be positive.")
    if method not in {"M2", "M3"}:
        raise D1Error(f"Unsupported threshold detector: {method}")
    if method == "M3" and volatility is None:
        raise D1Error("M3 requires a volatility series.")

    confirmed: list[Swing] = []
    anomalies: list[dict] = []
    state = "UNINITIALIZED"

    start_index = 0
    if method == "M3":
        start_index = next(
            (i for i, value in enumerate(volatility or ()) if value is not None),
            -1,
        )
        if start_index < 0:
            return DetectionResult((), ())
        anomalies.append(
            {
                "type": "VOLATILITY_INITIALIZED",
                "bar_index": start_index,
            }
        )

    high = _d(candles[start_index]["high"])
    high_i = start_index
    high_v = None if volatility is None else volatility[start_index]
    low = _d(candles[start_index]["low"])
    low_i = start_index
    low_v = None if volatility is None else volatility[start_index]

    def high_trigger(close: Decimal) -> bool:
        if method == "M2":
            return (high - close) / high >= threshold
        return high_v is not None and high - close >= threshold * high_v

    def low_trigger(close: Decimal) -> bool:
        if method == "M2":
            return (close - low) / low >= threshold
        return low_v is not None and close - low >= threshold * low_v

    for i in range(start_index, len(candles)):
        candle = candles[i]
        candle_high = _d(candle["high"])
        candle_low = _d(candle["low"])
        close = _d(candle["close"])
        current_v = None if volatility is None else volatility[i]

        if state == "UNINITIALIZED":
            if candle_high > high:
                high, high_i, high_v = candle_high, i, current_v
            if candle_low < low:
                low, low_i, low_v = candle_low, i, current_v

            high_hit = high_trigger(close)
            low_hit = low_trigger(close)
            if high_hit and low_hit:
                anomalies.append(
                    {
                        "type": "AMBIGUOUS_BOOTSTRAP",
                        "bar_index": i,
                        "action": "NO_CONFIRMATION",
                    }
                )
                continue
            if high_hit:
                confirmed.append(
                    _swing(
                        "HIGH", high_i, i, high, candles, method, profile_id, high_v
                    )
                )
                state = "DOWN_LEG"
                low, low_i, low_v = candle_low, i, current_v
            elif low_hit:
                confirmed.append(
                    _swing(
                        "LOW", low_i, i, low, candles, method, profile_id, low_v
                    )
                )
                state = "UP_LEG"
                high, high_i, high_v = candle_high, i, current_v
            continue

        if state == "UP_LEG":
            if candle_high > high:
                high, high_i, high_v = candle_high, i, current_v
            if high_trigger(close):
                confirmed.append(
                    _swing(
                        "HIGH", high_i, i, high, candles, method, profile_id, high_v
                    )
                )
                state = "DOWN_LEG"
                low, low_i, low_v = candle_low, i, current_v
        elif state == "DOWN_LEG":
            if candle_low < low:
                low, low_i, low_v = candle_low, i, current_v
            if low_trigger(close):
                confirmed.append(
                    _swing(
                        "LOW", low_i, i, low, candles, method, profile_id, low_v
                    )
                )
                state = "UP_LEG"
                high, high_i, high_v = candle_high, i, current_v
        else:
            raise D1Error(f"Unexpected detector state: {state}")

    return DetectionResult(tuple(confirmed), tuple(anomalies))


def fixed_percentage_reversal(
    candles: Sequence[dict],
    percentage: str | Decimal,
) -> DetectionResult:
    p = _d(percentage)
    return _threshold_detector(
        candles,
        method="M2",
        threshold=p,
        profile_id=f"M2-p{p}",
    )


def volatility_normalized_reversal(
    candles: Sequence[dict],
    *,
    estimator: str,
    window: int,
    multiplier: str | Decimal,
) -> DetectionResult:
    k = _d(multiplier)
    if estimator == "WILDER_ATR":
        volatility = wilder_atr(candles, window)
    elif estimator == "MEDIAN_TR":
        volatility = median_true_range(candles, window)
    else:
        raise D1Error(f"Unknown M3 estimator: {estimator}")
    return _threshold_detector(
        candles,
        method="M3",
        threshold=k,
        profile_id=f"M3-{estimator}-n{window}-k{k}",
        volatility=volatility,
    )


def assert_swing_invariants(swings: Sequence[Swing]) -> None:
    previous_confirmation = -1
    previous_kind: str | None = None
    for swing in swings:
        if swing.confirmation_index < swing.extremum_index:
            raise D1Error("Swing confirmed before its extremum.")
        if swing.confirmation_index <= previous_confirmation:
            raise D1Error("Swing confirmations are not strictly chronological.")
        if previous_kind == swing.kind:
            raise D1Error("Confirmed swings do not alternate.")
        previous_confirmation = swing.confirmation_index
        previous_kind = swing.kind


def volatility_normalized_reversal_intrabar(
    candles: Sequence[dict],
    *,
    estimator: str,
    window: int,
    multiplier: str | Decimal,
) -> DetectionResult:
    """M3 diagnostic-only closed-candle intrabar-range variant.

    This variant cannot become a final ASSET-P1-D1-001 candidate.
    """
    if not candles:
        return DetectionResult((), ())
    k=_d(multiplier)
    if k <= 0:
        raise D1Error("M3 intrabar multiplier must be positive.")
    if estimator == "WILDER_ATR":
        volatility=wilder_atr(candles,window)
    elif estimator == "MEDIAN_TR":
        volatility=median_true_range(candles,window)
    else:
        raise D1Error(f"Unknown M3 estimator: {estimator}")

    start_index=next((i for i,v in enumerate(volatility) if v is not None),-1)
    if start_index < 0:
        return DetectionResult((), ())

    profile_id=f"M3-INTRABAR-{estimator}-n{window}-k{k}"
    anomalies=[{"type":"VOLATILITY_INITIALIZED","bar_index":start_index}]
    confirmed: list[Swing]=[]
    state="UNINITIALIZED"

    high=_d(candles[start_index]["high"])
    high_i=start_index
    high_v=volatility[start_index]
    low=_d(candles[start_index]["low"])
    low_i=start_index
    low_v=volatility[start_index]

    for i in range(start_index,len(candles)):
        candle=candles[i]
        candle_high=_d(candle["high"])
        candle_low=_d(candle["low"])
        current_v=volatility[i]

        if state=="UNINITIALIZED":
            if candle_high > high:
                high,high_i,high_v=candle_high,i,current_v
            if candle_low < low:
                low,low_i,low_v=candle_low,i,current_v
            high_hit=high_v is not None and candle_low <= high-k*high_v
            low_hit=low_v is not None and candle_high >= low+k*low_v
            if high_hit and low_hit:
                anomalies.append({
                    "type":"AMBIGUOUS_BOOTSTRAP",
                    "bar_index":i,
                    "action":"NO_CONFIRMATION",
                })
                continue
            if high_hit:
                confirmed.append(_swing(
                    "HIGH",high_i,i,high,candles,"M3_INTRABAR",profile_id,high_v
                ))
                state="DOWN_LEG"
                low,low_i,low_v=candle_low,i,current_v
            elif low_hit:
                confirmed.append(_swing(
                    "LOW",low_i,i,low,candles,"M3_INTRABAR",profile_id,low_v
                ))
                state="UP_LEG"
                high,high_i,high_v=candle_high,i,current_v
            continue

        if state=="UP_LEG":
            updated=candle_high > high
            if updated:
                high,high_i,high_v=candle_high,i,current_v
            hit=high_v is not None and candle_low <= high-k*high_v
            if updated and hit:
                anomalies.append({
                    "type":"AMBIGUOUS_INTRABAR_SEQUENCE",
                    "bar_index":i,
                    "leg":"UP_LEG",
                    "action":"NO_CONFIRMATION",
                })
                continue
            if hit:
                confirmed.append(_swing(
                    "HIGH",high_i,i,high,candles,"M3_INTRABAR",profile_id,high_v
                ))
                state="DOWN_LEG"
                low,low_i,low_v=candle_low,i,current_v
        elif state=="DOWN_LEG":
            updated=candle_low < low
            if updated:
                low,low_i,low_v=candle_low,i,current_v
            hit=low_v is not None and candle_high >= low+k*low_v
            if updated and hit:
                anomalies.append({
                    "type":"AMBIGUOUS_INTRABAR_SEQUENCE",
                    "bar_index":i,
                    "leg":"DOWN_LEG",
                    "action":"NO_CONFIRMATION",
                })
                continue
            if hit:
                confirmed.append(_swing(
                    "LOW",low_i,i,low,candles,"M3_INTRABAR",profile_id,low_v
                ))
                state="UP_LEG"
                high,high_i,high_v=candle_high,i,current_v
        else:
            raise D1Error(f"Unexpected intrabar detector state: {state}")

    return DetectionResult(tuple(confirmed),tuple(anomalies))
