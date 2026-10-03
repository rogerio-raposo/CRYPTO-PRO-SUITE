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
from d1_metrics import (
    build_plateau_graph,
    freeze_pair_reference_bands,
    freeze_single_reference_bands,
    pairwise_cell_metrics,
    select_behavioral_representatives,
    single_profile_cell_metrics,
    type7_quantile,
)
from d1_runner import run_profile
from d1_structure import build_structure
from d1_swings import (
    assert_swing_invariants,
    fixed_percentage_reversal,
    fixed_window_pivots,
    volatility_normalized_reversal,
    volatility_normalized_reversal_intrabar,
)
from human_review import build_review_package
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



def revision02_metrics_and_review(candles: list[dict]) -> dict:
    analytical=[dict(x,analysis_island_id="REGRESSION-ISLAND") for x in candles]
    profiles=build_profiles("M1","4h")
    selected=[
        next(p for p in profiles if p.profile_id==pid)
        for pid in (
            "M1-TF4H-w2-q0.50-b0.25-m2",
            "M1-TF4H-w3-q0.50-b0.25-m2",
            "M1-TF4H-w4-q0.50-b0.25-m2",
        )
    ]

    runs={}
    singles={}
    for p in selected:
        d=p.detector_dict()
        s=p.structural_dict()
        run=run_profile(
            analytical,
            profile_id=p.profile_id,
            detector={"method":"M1","window":d["window"]},
            structural=s,
        )
        runs[p.profile_id]=run
        metric=single_profile_cell_metrics(run)
        # Eight deterministic DEV-like cells exercise Type-7/reference-band logic.
        singles[p.profile_id]={f"CELL-{i:02d}":metric for i in range(8)}

    pairs={}
    for a,b in zip(selected,selected[1:]):
        edge=(a.profile_id,b.profile_id)
        metric=pairwise_cell_metrics(
            runs[a.profile_id],
            runs[b.profile_id],
            analytical,
            timeframe="4h",
        )
        pairs[edge]={f"CELL-{i:02d}":metric for i in range(8)}

    plateau=build_plateau_graph(
        selected,
        single_metrics=singles,
        pair_metrics=pairs,
    )
    if not plateau.plateaus:
        raise AssertionError("Synthetic plateau graph produced no qualifying plateau.")

    representatives=select_behavioral_representatives(
        plateau,
        single_metrics=singles,
    )
    if not representatives:
        raise AssertionError("Behavioral representative selection returned empty.")

    for label,record in representatives.items():
        bands=freeze_single_reference_bands(singles[record["profile_id"]])
        if not bands or any(
            v.get("status") not in {"VALID","INSUFFICIENT_REFERENCE"}
            for k,v in bands.items() if k!="EventDensity"
        ):
            raise AssertionError("Single-profile DEV reference bands invalid.")

    first_edge=next(iter(pairs))
    pair_bands=freeze_pair_reference_bands(pairs[first_edge])
    if not pair_bands:
        raise AssertionError("Pair reference bands were not generated.")

    package,mapping=build_review_package(
        review_set_id="SYNTHETIC-DEV-REVIEW",
        profile_runs=runs,
        analytical_records=analytical,
        timeframe="4h",
        cell_identity={
            "asset":"SYNTH",
            "segment":"DEV-SYNTH",
            "phase":"DEV",
        },
    )
    aliases=package.get("profile_aliases",[])
    if not aliases or any(not str(x).startswith("R") for x in aliases):
        raise AssertionError("Human Review aliases were not blinded.")
    raw_ids=set(runs)
    serialized=json.dumps(package,sort_keys=True,default=str)
    if any(pid in serialized for pid in raw_ids):
        raise AssertionError("Reviewer-facing package leaked raw Profile ID.")
    if len(mapping.get("alias_to_profile",{})) != len(runs):
        raise AssertionError("Human Review alias mapping is incomplete.")

    return {
        "plateau_count":len(plateau.plateaus),
        "stable_edge_count":len(plateau.stable_edges),
        "representative_labels":sorted(representatives),
        "review_case_count":len(package.get("cases",[])),
        "review_package_sha256":package["package_sha256"],
        "review_mapping_sha256":mapping["mapping_sha256"],
        "status":"PASS",
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

    metrics_review=revision02_metrics_and_review(candles)

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
        "metrics_and_human_review":metrics_review,
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
