#!/usr/bin/env python3
"""Synthetic implementation regression for ASSET-P1-D1-001.

This is not a formal DEV/VAL/HOLDOUT execution.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from d1_matching import match_swings
from d1_structure import build_structure
from d1_swings import (
    assert_swing_invariants,
    fixed_percentage_reversal,
    fixed_window_pivots,
    volatility_normalized_reversal,
)
from phase_gate import (
    PhaseAccessError,
    authorize_phase,
    build_lock,
)


FOUR_HOURS_US = 14_400_000_000


def synthetic_candles() -> list[dict]:
    anchors = [
        100, 110, 104, 115, 108, 121, 113, 124,
        116, 126, 118, 120, 118, 121, 119, 120,
        110, 115, 105, 112, 100, 108, 96, 104,
        98, 103, 99, 102, 98, 101, 99, 100,
        105, 102, 109, 105, 113, 108, 117, 111,
    ]
    prices: list[int] = []
    for left, right in zip(anchors, anchors[1:]):
        steps = 4
        for i in range(steps):
            value = left + (right - left) * i / steps
            prices.append(round(value * 100))
    prices.append(anchors[-1] * 100)

    start = 1_700_000_000_000_000
    candles = []
    for i, cents in enumerate(prices):
        close = cents / 100
        # Synthetic bars are deliberately point-centered so local extrema are unique.
        # This fixture tests detector semantics, not realistic intrabar paths.
        open_ = close
        high = close + 0.35
        low = close - 0.35
        candles.append(
            {
                "open_time_us": start + i * FOUR_HOURS_US,
                "interval_end_us": start + (i + 1) * FOUR_HOURS_US,
                "open": f"{open_:.2f}",
                "high": f"{high:.2f}",
                "low": f"{low:.2f}",
                "close": f"{close:.2f}",
                "timeframe": "4h",
                "instrument": "SYNTHUSDT",
            }
        )
    return candles


def canonical_hash(obj: object) -> str:
    raw=(json.dumps(obj,sort_keys=True,separators=(",",":"),default=str)+"\n").encode()
    return hashlib.sha256(raw).hexdigest()


def run_once() -> dict:
    candles=synthetic_candles()

    m1=fixed_window_pivots(candles,3)
    m2=fixed_percentage_reversal(candles,"0.035")
    m3=volatility_normalized_reversal(
        candles,
        estimator="WILDER_ATR",
        window=14,
        multiplier="2.0",
    )

    for result in (m1,m2,m3):
        assert_swing_invariants(result.swings)
        for swing in result.swings:
            assert swing.confirmation_index >= swing.extremum_index
            assert swing.confirmation_end_us <= candles[swing.confirmation_index]["interval_end_us"]

    counts=(len(m1.swings),len(m2.swings),len(m3.swings))
    print(f"synthetic_swing_counts={counts}")
    if min(counts) < 4:
        raise AssertionError(f"Synthetic series did not exercise enough swings: {counts}")

    structure=build_structure(
        candles,
        m2.swings,
        equality_q="0.50",
        break_b="0.25",
        trend_m=2,
    )

    for prev,current in zip(structure.regime_changes,structure.regime_changes[1:]):
        direct={
            (prev.new_regime,current.new_regime)
        } & {
            ("TREND_UP","TREND_DOWN"),
            ("TREND_DOWN","TREND_UP"),
        }
        if direct:
            raise AssertionError("Direct trend flip detected.")

    self_match=match_swings(
        m2.swings,
        m2.swings,
        candles,
        timeframe="4h",
        mode="BASE",
    )
    if self_match.match_count != len(m2.swings) or self_match.swing_stability != "1":
        raise AssertionError("Self matching is not identity.")

    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp)
        denied_val=False
        try:
            authorize_phase("VAL")
        except PhaseAccessError:
            denied_val=True
        if not denied_val:
            raise AssertionError("VAL was not blocked without DEV lock.")

        dev_doc=build_lock(
            lock_type="DEV_CANDIDATE_LOCK",
            candidates=["CANDIDATE-A","CANDIDATE-B"],
            metrics_reference_sha256="1"*64,
        )
        dev_path=root/"dev.json"
        dev_path.write_text(json.dumps(dev_doc),encoding="utf-8")

        val_candidates=authorize_phase("VAL",dev_lock_path=dev_path)
        if val_candidates != ("CANDIDATE-A","CANDIDATE-B"):
            raise AssertionError("DEV lock candidate set changed.")

        denied_holdout=False
        try:
            authorize_phase("HOLDOUT",dev_lock_path=dev_path)
        except PhaseAccessError:
            denied_holdout=True
        if not denied_holdout:
            raise AssertionError("HOLDOUT was not blocked without VAL lock.")

        val_doc=build_lock(
            lock_type="VAL_PROVISIONAL_LOCK",
            candidates=["CANDIDATE-A"],
            metrics_reference_sha256="2"*64,
            prior_lock_sha256=dev_doc["payload_sha256"],
        )
        val_path=root/"val.json"
        val_path.write_text(json.dumps(val_doc),encoding="utf-8")
        holdout_candidates=authorize_phase(
            "HOLDOUT",
            dev_lock_path=dev_path,
            val_lock_path=val_path,
        )
        if holdout_candidates != ("CANDIDATE-A",):
            raise AssertionError("Holdout candidate gate mismatch.")

    return {
        "candles":len(candles),
        "m1_swings":len(m1.swings),
        "m2_swings":len(m2.swings),
        "m3_swings":len(m3.swings),
        "relations":len(structure.relations),
        "cycles":len(structure.cycles),
        "regime_changes":[r.__dict__ for r in structure.regime_changes],
        "events":len(structure.events),
        "protected_snapshots":len(structure.protected_swings),
        "self_match_count":self_match.match_count,
        "phase_gate":"PASS",
    }


def main() -> int:
    a=run_once()
    b=run_once()
    hash_a=canonical_hash(a)
    hash_b=canonical_hash(b)
    if hash_a != hash_b:
        raise AssertionError("Synthetic implementation regression is nondeterministic.")
    result={
        "status":"PASS",
        "hash_a":hash_a,
        "hash_b":hash_b,
        "summary":a,
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
