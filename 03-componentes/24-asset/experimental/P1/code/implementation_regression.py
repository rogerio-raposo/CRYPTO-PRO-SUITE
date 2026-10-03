#!/usr/bin/env python3
"""Synthetic implementation regression for ASSET-P1-D1-001.

This is implementation validation only; it is not a formal DEV/VAL/HOLDOUT run.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
from decimal import Decimal
from pathlib import Path

from d1_matching import match_swings
from d1_metrics import type7_quantile
from d1_structure import build_structure
from d1_swings import (
    assert_swing_invariants,
    fixed_percentage_reversal,
    fixed_window_pivots,
    volatility_normalized_reversal,
    volatility_normalized_reversal_intrabar,
)
from p1_profiles import are_adjacent, build_profiles
from phase_gate import PhaseAccessError, authorize_phase, build_lock


FOUR_HOURS_US=14_400_000_000


def synthetic_candles() -> list[dict]:
    anchors=[
        100,110,104,115,108,121,113,124,
        116,126,118,120,118,121,119,120,
        110,115,105,112,100,108,96,104,
        98,103,99,102,98,101,99,100,
        105,102,109,105,113,108,117,111,
    ]
    prices=[]
    for left,right in zip(anchors,anchors[1:]):
        for i in range(4):
            value=left+(right-left)*i/4
            prices.append(round(value*100))
    prices.append(anchors[-1]*100)

    start=1_700_000_000_000_000
    candles=[]
    for i,cents in enumerate(prices):
        close=cents/100
        candles.append({
            "open_time_us":start+i*FOUR_HOURS_US,
            "interval_end_us":start+(i+1)*FOUR_HOURS_US,
            "open":f"{close:.2f}",
            "high":f"{close+0.35:.2f}",
            "low":f"{close-0.35:.2f}",
            "close":f"{close:.2f}",
            "timeframe":"4h",
            "instrument":"SYNTHUSDT",
        })
    return candles


def dual_pivot_fixture() -> list[dict]:
    start=1_600_000_000_000_000
    rows=[
        (7,9,6,8),
        (8,10,7,9),
        (9,20,0,10),
        (10,11,8,9),
        (9,10,7,8),
    ]
    return [
        {
            "open_time_us":start+i*FOUR_HOURS_US,
            "interval_end_us":start+(i+1)*FOUR_HOURS_US,
            "open":str(o),"high":str(h),"low":str(l),"close":str(c),
            "timeframe":"4h","instrument":"DUALUSDT",
        }
        for i,(o,h,l,c) in enumerate(rows)
    ]


def canonical_hash(obj: object) -> str:
    raw=(json.dumps(obj,sort_keys=True,separators=(",",":"),default=str)+"\n").encode()
    return hashlib.sha256(raw).hexdigest()


def dummy_candidate(profile_id: str,label: str,density: str) -> dict:
    return {
        "profile_id":profile_id,
        "behavioral_label":label,
        "plateau_membership":[1],
        "pooled_dev_swing_density":density,
        "single_reference_bands":{
            "SwingDensity":{"status":"VALID","lower":"1","upper":"100"}
        },
    }


def run_once() -> dict:
    candles=synthetic_candles()

    m1=fixed_window_pivots(candles,3)
    m2=fixed_percentage_reversal(candles,"0.035")
    m3=volatility_normalized_reversal(
        candles,estimator="WILDER_ATR",window=14,multiplier="2.0"
    )
    m3i=volatility_normalized_reversal_intrabar(
        candles,estimator="WILDER_ATR",window=14,multiplier="2.0"
    )

    for result in (m1,m2,m3,m3i):
        assert_swing_invariants(result.swings)
        for swing in result.swings:
            assert swing.confirmation_index >= swing.extremum_index

    counts=(len(m1.swings),len(m2.swings),len(m3.swings),len(m3i.swings))
    print(f"synthetic_swing_counts={counts}")
    if min(counts[:3]) < 4:
        raise AssertionError(f"Synthetic primary methods under-exercised: {counts}")
    if any(s.extremum_index < 13 for s in m3.swings):
        raise AssertionError("M3 used pre-volatility-init extremum.")

    dual=fixed_window_pivots(dual_pivot_fixture(),2)
    if dual.swings:
        raise AssertionError("M1 confirmed an ambiguous dual pivot.")
    if not any(x.get("type")=="AMBIGUOUS_DUAL_PIVOT" for x in dual.anomalies):
        raise AssertionError("M1 dual-pivot diagnostic missing.")

    structure=build_structure(
        candles,m2.swings,equality_q="0.50",break_b="0.25",trend_m=2
    )
    if any(
        (x.previous_regime,x.new_regime) in {
            ("TREND_UP","TREND_DOWN"),("TREND_DOWN","TREND_UP")
        }
        for x in structure.regime_changes
    ):
        raise AssertionError("Direct trend flip detected.")

    self_match=match_swings(
        m2.swings,m2.swings,candles,timeframe="4h",mode="BASE"
    )
    if (
        self_match.match_count != self_match.eligible_count_a
        or self_match.eligible_count_a != self_match.eligible_count_b
        or self_match.swing_stability != "1"
    ):
        raise AssertionError("Comparator-eligible self matching is not identity.")
    if not self_match.comparison_ineligible_a:
        raise AssertionError("Comparator warm-up exclusion was not exercised.")

    if type7_quantile([0,10,20,30],Decimal("0.25")) != Decimal("7.50"):
        raise AssertionError("Type-7 Q1 convention mismatch.")
    if type7_quantile([0,10,20,30],Decimal("0.75")) != Decimal("22.50"):
        raise AssertionError("Type-7 Q3 convention mismatch.")

    profiles=build_profiles("M1","4h")
    base=next(p for p in profiles if p.profile_id=="M1-TF4H-w2-q0.50-b0.25-m2")
    adjacent=next(p for p in profiles if p.profile_id=="M1-TF4H-w3-q0.50-b0.25-m2")
    distant=next(p for p in profiles if p.profile_id=="M1-TF4H-w6-q0.50-b0.25-m2")
    if not are_adjacent(base,adjacent) or are_adjacent(base,distant):
        raise AssertionError("Full-profile adjacency rule mismatch.")

    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp)
        try:
            authorize_phase("VAL")
        except PhaseAccessError:
            pass
        else:
            raise AssertionError("VAL was not blocked without DEV lock.")

        records=[
            dummy_candidate("CANDIDATE-A","Responsive","20"),
            dummy_candidate("CANDIDATE-B","Conservative","5"),
        ]
        dev_doc=build_lock(
            lock_type="DEV_CANDIDATE_LOCK",
            candidate_records=records,
            metrics_reference_sha256="1"*64,
            human_review_sha256="3"*64,
            pair_reference_bands={
                "CANDIDATE-A|CANDIDATE-B":{
                    "SwingStability_BASE":{"status":"VALID","lower":"0.5","upper":None}
                }
            },
        )
        dev_path=root/"dev.json"
        dev_path.write_text(json.dumps(dev_doc),encoding="utf-8")

        val_candidates=authorize_phase("VAL",dev_lock_path=dev_path)
        if val_candidates != ("CANDIDATE-A","CANDIDATE-B"):
            raise AssertionError("DEV lock candidate identity changed.")

        try:
            authorize_phase("HOLDOUT",dev_lock_path=dev_path)
        except PhaseAccessError:
            pass
        else:
            raise AssertionError("HOLDOUT was not blocked without VAL lock.")

        val_doc=build_lock(
            lock_type="VAL_PROVISIONAL_LOCK",
            candidate_records=[records[0]],
            metrics_reference_sha256="2"*64,
            human_review_sha256="4"*64,
            pair_reference_bands={},
            prior_lock_sha256=dev_doc["payload_sha256"],
        )
        val_path=root/"val.json"
        val_path.write_text(json.dumps(val_doc),encoding="utf-8")
        holdout_candidates=authorize_phase(
            "HOLDOUT",dev_lock_path=dev_path,val_lock_path=val_path
        )
        if holdout_candidates != ("CANDIDATE-A",):
            raise AssertionError("Holdout candidate gate mismatch.")

        mutated=dict(records[0])
        mutated["behavioral_label"]="Balanced"
        bad_val=build_lock(
            lock_type="VAL_PROVISIONAL_LOCK",
            candidate_records=[mutated],
            metrics_reference_sha256="2"*64,
            human_review_sha256="4"*64,
            prior_lock_sha256=dev_doc["payload_sha256"],
        )
        bad_path=root/"bad-val.json"
        bad_path.write_text(json.dumps(bad_val),encoding="utf-8")
        try:
            authorize_phase(
                "HOLDOUT",dev_lock_path=dev_path,val_lock_path=bad_path
            )
        except PhaseAccessError:
            pass
        else:
            raise AssertionError("VAL mutation of DEV candidate was not blocked.")

    return {
        "candles":len(candles),
        "m1_swings":len(m1.swings),
        "m2_swings":len(m2.swings),
        "m3_swings":len(m3.swings),
        "m3_intrabar_swings":len(m3i.swings),
        "m2_comparison_eligible":self_match.eligible_count_a,
        "m2_comparison_warmup_excluded":len(self_match.comparison_ineligible_a),
        "relations":len(structure.relations),
        "cycles":len(structure.cycles),
        "regime_changes":[x.__dict__ for x in structure.regime_changes],
        "events":len(structure.events),
        "protected_snapshots":len(structure.protected_swings),
        "profile_count_m1_4h":len(profiles),
        "phase_gate":"PASS",
        "revision02_primitives":"PASS",
    }


def main() -> int:
    a=run_once()
    b=run_once()
    hash_a=canonical_hash(a)
    hash_b=canonical_hash(b)
    if hash_a!=hash_b:
        raise AssertionError("Synthetic implementation regression is nondeterministic.")
    print(json.dumps({
        "status":"PASS",
        "hash_a":hash_a,
        "hash_b":hash_b,
        "summary":a,
    },indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
