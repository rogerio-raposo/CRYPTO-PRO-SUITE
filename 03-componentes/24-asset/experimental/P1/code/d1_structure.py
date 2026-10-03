#!/usr/bin/env python3
"""ASSET-P1-D1-001 structural sequence, regime and event engine.

Experimental / non-normative. The engine consumes already-confirmed causal swings.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
from typing import Sequence

from d1_swings import D1Error, Swing, wilder_atr


@dataclass(frozen=True)
class SwingRelation:
    relation_id: str
    kind: str
    relation: str
    previous_extremum_index: int
    current_extremum_index: int
    confirmation_index: int
    confirmation_end_us: int
    tolerance: str | None


@dataclass(frozen=True)
class StructuralCycle:
    cycle_id: str
    confirmation_index: int
    high_relation: str
    low_relation: str
    classification: str


@dataclass(frozen=True)
class RegimeChange:
    change_id: str
    bar_index: int
    timestamp_us: int
    previous_regime: str
    new_regime: str
    integrity: str
    reason: str


@dataclass(frozen=True)
class StructuralEvent:
    event_id: str
    event_type: str
    bar_index: int
    timestamp_us: int
    reference_id: str
    reference_kind: str
    reference_price: str
    buffer: str
    regime_before: str
    detail: str


@dataclass(frozen=True)
class ProtectedSwingSnapshot:
    snapshot_id: str
    bar_index: int
    timestamp_us: int
    action: str
    kind: str | None
    extremum_index: int | None
    price: str | None
    buffer: str | None


@dataclass(frozen=True)
class StructureResult:
    relations: tuple[SwingRelation, ...]
    cycles: tuple[StructuralCycle, ...]
    regime_changes: tuple[RegimeChange, ...]
    events: tuple[StructuralEvent, ...]
    protected_swings: tuple[ProtectedSwingSnapshot, ...]
    regime_by_bar: tuple[str, ...]
    integrity_by_bar: tuple[str, ...]
    anomalies: tuple[dict, ...]


@dataclass
class _Reference:
    reference_id: str
    kind: str
    price: Decimal
    buffer: Decimal
    activated_index: int
    swing: Swing | None
    reference_class: str
    active: bool = True
    breached: bool = False
    broken_index: int | None = None
    break_direction: str | None = None
    reclaimed: bool = False


@dataclass
class _Protected:
    kind: str
    swing: Swing
    buffer: Decimal
    activated_index: int


def _d(value) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def _relation_for(
    previous: Swing,
    current: Swing,
    *,
    atr: Decimal | None,
    equality_q: Decimal,
) -> tuple[str, Decimal | None]:
    if atr is None:
        return "INDETERMINATE", None
    tolerance = equality_q * atr
    p0 = _d(previous.price)
    p1 = _d(current.price)
    if abs(p1 - p0) <= tolerance:
        return ("EH" if current.kind == "HIGH" else "EL"), tolerance
    if current.kind == "HIGH":
        return ("HH" if p1 > p0 else "LH"), tolerance
    return ("HL" if p1 > p0 else "LL"), tolerance


def _cycle_class(high_relation: str, low_relation: str) -> str:
    up = (
        high_relation in {"HH", "EH"}
        and low_relation in {"HL", "EL"}
        and (high_relation == "HH" or low_relation == "HL")
    )
    down = (
        high_relation in {"LH", "EH"}
        and low_relation in {"LL", "EL"}
        and (high_relation == "LH" or low_relation == "LL")
    )
    if up:
        return "UP"
    if down:
        return "DOWN"
    return "NEUTRAL"


def _same_swing(a: Swing | None, b: Swing | None) -> bool:
    if a is None or b is None:
        return False
    return (
        a.kind == b.kind
        and a.extremum_index == b.extremum_index
        and a.confirmation_index == b.confirmation_index
    )


def build_structure(
    candles: Sequence[dict],
    swings: Sequence[Swing],
    *,
    equality_q: str | Decimal,
    break_b: str | Decimal,
    trend_m: int,
) -> StructureResult:
    if trend_m not in {2, 3}:
        raise D1Error("P1 trend_m must be 2 or 3.")
    q = _d(equality_q)
    b = _d(break_b)
    if q < 0 or b < 0:
        raise D1Error("Structural q/b parameters cannot be negative.")

    atr14 = wilder_atr(candles, 14)
    swings_by_confirmation: dict[int, list[Swing]] = {}
    for swing in swings:
        swings_by_confirmation.setdefault(swing.confirmation_index, []).append(swing)
    for values in swings_by_confirmation.values():
        values.sort(key=lambda x: (x.extremum_index, x.kind))

    relations: list[SwingRelation] = []
    cycles: list[StructuralCycle] = []
    regime_changes: list[RegimeChange] = []
    events: list[StructuralEvent] = []
    protected_log: list[ProtectedSwingSnapshot] = []
    anomalies: list[dict] = []

    previous_same: dict[str, Swing] = {}
    latest_relation: dict[str, SwingRelation] = {}
    pending_relations: dict[str, SwingRelation] = {}
    confirmed_by_kind: dict[str, list[Swing]] = {"HIGH": [], "LOW": []}

    up_count = 0
    down_count = 0
    regime = "INDETERMINATE"
    integrity = "INDETERMINATE"
    protected: _Protected | None = None
    references: list[_Reference] = []
    range_references: list[_Reference] = []

    regime_by_bar: list[str] = []
    integrity_by_bar: list[str] = []

    def log_regime(bar_index: int, new: str, new_integrity: str, reason: str) -> None:
        nonlocal regime, integrity, range_references
        if new == regime and new_integrity == integrity:
            return
        previous = regime
        regime = new
        integrity = new_integrity
        regime_changes.append(
            RegimeChange(
                change_id=f"RG{len(regime_changes)+1:05d}",
                bar_index=bar_index,
                timestamp_us=int(candles[bar_index]["interval_end_us"]),
                previous_regime=previous,
                new_regime=new,
                integrity=new_integrity,
                reason=reason,
            )
        )
        if new != "RANGE":
            for ref in range_references:
                ref.active = False
            range_references = []

    def make_buffer(bar_index: int) -> Decimal | None:
        atr = atr14[bar_index]
        if b == 0:
            return Decimal("0")
        return None if atr is None else b * atr

    def activate_swing_reference(swing: Swing) -> None:
        # Revision 01: only the latest unbroken generic reference of each type
        # remains active. Broken references stay in history for a possible Reclaim.
        for prior in references:
            if (
                prior.reference_class == "SWING"
                and prior.kind == swing.kind
                and prior.active
                and prior.broken_index is None
            ):
                prior.active = False
                anomalies.append(
                    {
                        "type": "GENERIC_REFERENCE_RETIRED",
                        "reference_id": prior.reference_id,
                        "retired_at_confirmation_index": swing.confirmation_index,
                    }
                )

        buffer = make_buffer(swing.confirmation_index)
        if buffer is None:
            anomalies.append(
                {
                    "type": "REFERENCE_NOT_EVALUABLE_NO_ATR",
                    "kind": swing.kind,
                    "confirmation_index": swing.confirmation_index,
                }
            )
            return
        references.append(
            _Reference(
                reference_id=(
                    f"SW-{swing.kind}-{swing.extremum_index}-"
                    f"{swing.confirmation_index}"
                ),
                kind=swing.kind,
                price=_d(swing.price),
                buffer=buffer,
                activated_index=swing.confirmation_index,
                swing=swing,
                reference_class="SWING",
            )
        )

    def activate_range(bar_index: int) -> None:
        nonlocal range_references
        if len(confirmed_by_kind["HIGH"]) < 2 or len(confirmed_by_kind["LOW"]) < 2:
            return
        buffer = make_buffer(bar_index)
        if buffer is None:
            anomalies.append(
                {"type": "RANGE_REFERENCE_NOT_EVALUABLE_NO_ATR", "bar_index": bar_index}
            )
            return
        highs = confirmed_by_kind["HIGH"][-2:]
        lows = confirmed_by_kind["LOW"][-2:]
        range_references = [
            _Reference(
                reference_id=f"RANGE-HIGH-{bar_index}",
                kind="HIGH",
                price=max(_d(x.price) for x in highs),
                buffer=buffer,
                activated_index=bar_index,
                swing=None,
                reference_class="RANGE",
            ),
            _Reference(
                reference_id=f"RANGE-LOW-{bar_index}",
                kind="LOW",
                price=min(_d(x.price) for x in lows),
                buffer=buffer,
                activated_index=bar_index,
                swing=None,
                reference_class="RANGE",
            ),
        ]

    def set_protected(
        bar_index: int,
        candidate: Swing,
        reason: str,
    ) -> None:
        nonlocal protected
        buffer = make_buffer(bar_index)
        if buffer is None:
            anomalies.append(
                {"type": "PROTECTED_NOT_EVALUABLE_NO_ATR", "bar_index": bar_index}
            )
            return
        if protected is not None and _same_swing(protected.swing, candidate):
            return
        protected = _Protected(candidate.kind, candidate, buffer, bar_index)
        protected_log.append(
            ProtectedSwingSnapshot(
                snapshot_id=f"PS{len(protected_log)+1:05d}",
                bar_index=bar_index,
                timestamp_us=int(candles[bar_index]["interval_end_us"]),
                action=f"PROMOTE:{reason}",
                kind=candidate.kind,
                extremum_index=candidate.extremum_index,
                price=candidate.price,
                buffer=str(buffer),
            )
        )

    def clear_protected(bar_index: int, reason: str) -> None:
        nonlocal protected
        if protected is None:
            return
        protected_log.append(
            ProtectedSwingSnapshot(
                snapshot_id=f"PS{len(protected_log)+1:05d}",
                bar_index=bar_index,
                timestamp_us=int(candles[bar_index]["interval_end_us"]),
                action=f"CLEAR:{reason}",
                kind=protected.kind,
                extremum_index=protected.swing.extremum_index,
                price=protected.swing.price,
                buffer=str(protected.buffer),
            )
        )
        protected = None

    def emit_event(
        bar_index: int,
        event_type: str,
        ref: _Reference,
        detail: str,
    ) -> None:
        events.append(
            StructuralEvent(
                event_id=f"EV{len(events)+1:06d}",
                event_type=event_type,
                bar_index=bar_index,
                timestamp_us=int(candles[bar_index]["interval_end_us"]),
                reference_id=ref.reference_id,
                reference_kind=ref.kind,
                reference_price=str(ref.price),
                buffer=str(ref.buffer),
                regime_before=regime,
                detail=detail,
            )
        )

    def check_protected_break(bar_index: int, close: Decimal) -> bool:
        nonlocal protected
        if protected is None or bar_index <= protected.activated_index:
            return False
        price = _d(protected.swing.price)
        broken = (
            protected.kind == "LOW" and close < price - protected.buffer
        ) or (
            protected.kind == "HIGH" and close > price + protected.buffer
        )
        if not broken:
            return False
        ref = _Reference(
            reference_id=(
                f"PROTECTED-{protected.kind}-"
                f"{protected.swing.extremum_index}-{protected.activated_index}"
            ),
            kind=protected.kind,
            price=price,
            buffer=protected.buffer,
            activated_index=protected.activated_index,
            swing=protected.swing,
            reference_class="PROTECTED",
        )
        emit_event(bar_index, "COUNTER_STRUCTURAL_BREAK", ref, "Primary Protected Swing")
        clear_protected(bar_index, "COUNTER_STRUCTURAL_BREAK")
        log_regime(bar_index, "TRANSITION", "BROKEN", "Protected Swing broken")
        for generic in references:
            if _same_swing(generic.swing, ref.swing):
                generic.active = False
                generic.broken_index = bar_index
        return True

    def check_reclaims(bar_index: int, close: Decimal) -> None:
        for ref in references + range_references:
            if ref.broken_index is None or ref.reclaimed or bar_index <= ref.broken_index:
                continue
            reclaimed = (
                ref.break_direction == "UP" and close < ref.price - ref.buffer
            ) or (
                ref.break_direction == "DOWN" and close > ref.price + ref.buffer
            )
            if reclaimed:
                emit_event(bar_index, "RECLAIM", ref, "Return to prior side")
                ref.reclaimed = True

    def check_active_references(bar_index: int, candle: dict) -> None:
        nonlocal protected
        high = _d(candle["high"])
        low = _d(candle["low"])
        close = _d(candle["close"])

        counter_broken = check_protected_break(bar_index, close)
        check_reclaims(bar_index, close)

        for ref in references + range_references:
            if not ref.active or bar_index <= ref.activated_index:
                continue
            if protected is not None and _same_swing(ref.swing, protected.swing):
                continue

            raw_cross = high > ref.price if ref.kind == "HIGH" else low < ref.price
            pcsb = (
                ref.kind == "HIGH" and close > ref.price + ref.buffer
            ) or (
                ref.kind == "LOW" and close < ref.price - ref.buffer
            )

            if raw_cross and not pcsb and not ref.breached:
                emit_event(bar_index, "BREACH", ref, "Raw reference crossed intrabar")
                ref.breached = True

            if not pcsb:
                continue

            event_type = "PCSB"
            if ref.reference_class == "RANGE":
                event_type = "PCSB"
            elif regime == "TREND_UP" and ref.kind == "HIGH":
                event_type = "CONTINUATION_BREAK"
            elif regime == "TREND_DOWN" and ref.kind == "LOW":
                event_type = "CONTINUATION_BREAK"

            emit_event(bar_index, event_type, ref, ref.reference_class)
            ref.active = False
            ref.broken_index = bar_index
            ref.break_direction = "UP" if ref.kind == "HIGH" else "DOWN"

            if ref.reference_class == "RANGE" and regime == "RANGE":
                log_regime(bar_index, "TRANSITION", "BROKEN", "Range boundary PCSB")

            if event_type == "CONTINUATION_BREAK" and not counter_broken:
                if regime == "TREND_UP" and ref.kind == "HIGH":
                    candidates = [
                        s
                        for s in confirmed_by_kind["LOW"]
                        if s.confirmation_index > (
                            ref.swing.confirmation_index if ref.swing else -1
                        )
                        and s.confirmation_index < bar_index
                    ]
                    if candidates:
                        set_protected(bar_index, candidates[-1], "UP_CONTINUATION")
                elif regime == "TREND_DOWN" and ref.kind == "LOW":
                    candidates = [
                        s
                        for s in confirmed_by_kind["HIGH"]
                        if s.confirmation_index > (
                            ref.swing.confirmation_index if ref.swing else -1
                        )
                        and s.confirmation_index < bar_index
                    ]
                    if candidates:
                        set_protected(bar_index, candidates[-1], "DOWN_CONTINUATION")

    def current_range_candidate() -> bool:
        return (
            latest_relation.get("HIGH") is not None
            and latest_relation.get("LOW") is not None
            and latest_relation["HIGH"].relation == "EH"
            and latest_relation["LOW"].relation == "EL"
            and len(confirmed_by_kind["HIGH"]) >= 2
            and len(confirmed_by_kind["LOW"]) >= 2
        )

    def handle_cycle(bar_index: int, cycle_class: str) -> None:
        nonlocal up_count, down_count, integrity
        if cycle_class == "UP":
            up_count += 1
            down_count = 0
        elif cycle_class == "DOWN":
            down_count += 1
            up_count = 0
        else:
            up_count = 0
            down_count = 0

        if regime == "TREND_UP":
            if cycle_class == "UP":
                integrity = "INTACT"
            elif cycle_class == "DOWN":
                integrity = "WEAKENING"
                if down_count >= trend_m:
                    clear_protected(bar_index, "OPPOSING_CYCLE_SEQUENCE")
                    log_regime(
                        bar_index,
                        "TRANSITION",
                        "BROKEN",
                        "Opposing down cycles against Uptrend",
                    )
            return

        if regime == "TREND_DOWN":
            if cycle_class == "DOWN":
                integrity = "INTACT"
            elif cycle_class == "UP":
                integrity = "WEAKENING"
                if up_count >= trend_m:
                    clear_protected(bar_index, "OPPOSING_CYCLE_SEQUENCE")
                    log_regime(
                        bar_index,
                        "TRANSITION",
                        "BROKEN",
                        "Opposing up cycles against Downtrend",
                    )
            return

        if regime == "RANGE":
            return

        if up_count >= trend_m:
            log_regime(bar_index, "TREND_UP", "INTACT", "Directional cycles established")
        elif down_count >= trend_m:
            log_regime(
                bar_index, "TREND_DOWN", "INTACT", "Directional cycles established"
            )
        elif current_range_candidate():
            log_regime(bar_index, "RANGE", "INTACT", "Equal high/low containment")
            activate_range(bar_index)

    for bar_index, candle in enumerate(candles):
        check_active_references(bar_index, candle)

        for swing in swings_by_confirmation.get(bar_index, []):
            previous = previous_same.get(swing.kind)
            confirmed_by_kind[swing.kind].append(swing)

            if previous is not None:
                relation_name, tolerance = _relation_for(
                    previous,
                    swing,
                    atr=atr14[bar_index],
                    equality_q=q,
                )
                relation = SwingRelation(
                    relation_id=f"RL{len(relations)+1:05d}",
                    kind=swing.kind,
                    relation=relation_name,
                    previous_extremum_index=previous.extremum_index,
                    current_extremum_index=swing.extremum_index,
                    confirmation_index=bar_index,
                    confirmation_end_us=int(candle["interval_end_us"]),
                    tolerance=None if tolerance is None else str(tolerance),
                )
                relations.append(relation)
                latest_relation[swing.kind] = relation
                pending_relations[swing.kind] = relation

                if "HIGH" in pending_relations and "LOW" in pending_relations:
                    high_rel = pending_relations.pop("HIGH")
                    low_rel = pending_relations.pop("LOW")
                    cycle_class = _cycle_class(
                        high_rel.relation, low_rel.relation
                    )
                    cycle = StructuralCycle(
                        cycle_id=f"CY{len(cycles)+1:05d}",
                        confirmation_index=bar_index,
                        high_relation=high_rel.relation,
                        low_relation=low_rel.relation,
                        classification=cycle_class,
                    )
                    cycles.append(cycle)
                    handle_cycle(bar_index, cycle_class)

            previous_same[swing.kind] = swing
            activate_swing_reference(swing)

        regime_by_bar.append(regime)
        integrity_by_bar.append(integrity)

    return StructureResult(
        relations=tuple(relations),
        cycles=tuple(cycles),
        regime_changes=tuple(regime_changes),
        events=tuple(events),
        protected_swings=tuple(protected_log),
        regime_by_bar=tuple(regime_by_bar),
        integrity_by_bar=tuple(integrity_by_bar),
        anomalies=tuple(anomalies),
    )
