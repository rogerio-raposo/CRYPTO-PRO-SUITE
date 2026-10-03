#!/usr/bin/env python3
"""ASSET-P1-D1-001 Revision 03 causal-validation harness.

Implementation validation only. This is not a formal DEV/VAL/HOLDOUT run.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from d1_runner import (
    assert_no_cross_island_objects,
    run_profile,
)


FOUR_HOURS_US = 14_400_000_000


class CausalValidationError(RuntimeError):
    pass


def canonical_bytes(obj: object) -> bytes:
    return (
        json.dumps(
            obj,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        )
        + "\n"
    ).encode("utf-8")


def sha256_obj(obj: object) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def synthetic_island(
    *,
    island_id: str,
    start_us: int,
    prices: list[float],
) -> list[dict]:
    rows=[]
    for i,close in enumerate(prices):
        rows.append({
            "analysis_island_id":island_id,
            "open_time_us":start_us+i*FOUR_HOURS_US,
            "interval_end_us":start_us+(i+1)*FOUR_HOURS_US,
            "open":f"{close:.4f}",
            "high":f"{close+0.40:.4f}",
            "low":f"{close-0.40:.4f}",
            "close":f"{close:.4f}",
            "timeframe":"4h",
            "instrument":"SYNTHUSDT",
        })
    return rows


def fixture() -> list[dict]:
    anchors_a=[
        100,108,103,112,106,116,109,119,111,121,
        114,118,110,115,105,112,101,109,97,105,
        100,107,102,110,105,114,108,117,
    ]
    anchors_b=[
        80,75,78,72,76,69,74,66,71,64,
        68,62,67,60,65,58,64,61,66,63,
        69,65,72,68,75,70,78,73,
    ]

    def interpolate(anchors):
        values=[]
        for left,right in zip(anchors,anchors[1:]):
            for i in range(3):
                values.append(left+(right-left)*i/3)
        values.append(float(anchors[-1]))
        return values

    first=synthetic_island(
        island_id="ISLAND-001",
        start_us=1_700_000_000_000_000,
        prices=interpolate(anchors_a),
    )
    second=synthetic_island(
        island_id="ISLAND-002",
        start_us=first[-1]["interval_end_us"] + 12*FOUR_HOURS_US,
        prices=interpolate(anchors_b),
    )
    return first+second


PROFILE_ID="M2-TF4H-p0.04-q0.50-b0.25-m2"
DETECTOR={"method":"M2","percentage":"0.04"}
STRUCTURAL={"q":"0.50","b":"0.25","m":"2"}


def _strip_hashes(run: dict) -> dict:
    value=copy.deepcopy(run)
    value.pop("run_sha256",None)
    for island in value.get("islands",[]):
        island.pop("result_sha256",None)
    return value


def _objects_visible_through(island: dict, max_bar: int) -> dict:
    """Return only outputs that were knowable by max_bar in one island."""
    return {
        "swings":[
            x for x in island.get("swings",[])
            if int(x["confirmation_index"]) <= max_bar
        ],
        "relations":[
            x for x in island.get("relations",[])
            if int(x["confirmation_index"]) <= max_bar
        ],
        "cycles":[
            x for x in island.get("cycles",[])
            if int(x["confirmation_index"]) <= max_bar
        ],
        "regime_changes":[
            x for x in island.get("regime_changes",[])
            if int(x["bar_index"]) <= max_bar
        ],
        "events":[
            x for x in island.get("events",[])
            if int(x["bar_index"]) <= max_bar
        ],
        "protected_swings":[
            x for x in island.get("protected_swings",[])
            if int(x["bar_index"]) <= max_bar
        ],
        "regime_by_bar":list(island.get("regime_by_bar",[]))[:max_bar+1],
        "integrity_by_bar":list(island.get("integrity_by_bar",[]))[:max_bar+1],
    }


def assert_future_timestamp_audit(run: dict, records: list[dict]) -> None:
    records_by_island={}
    for r in records:
        records_by_island.setdefault(r["analysis_island_id"],[]).append(r)

    for island in run.get("islands",[]):
        candles=records_by_island[island["analysis_island_id"]]
        final_ts=int(candles[-1]["interval_end_us"])
        n=len(candles)
        for swing in island.get("swings",[]):
            if int(swing["confirmation_index"]) >= n:
                raise CausalValidationError("Swing confirmation index exceeds visible prefix.")
            if int(swing["confirmation_end_us"]) > final_ts:
                raise CausalValidationError("Swing confirmation timestamp is in future.")
        for relation in island.get("relations",[]):
            if int(relation["confirmation_end_us"]) > final_ts:
                raise CausalValidationError("Relation timestamp is in future.")
        for event in island.get("events",[]):
            if int(event["timestamp_us"]) > final_ts:
                raise CausalValidationError("Event timestamp is in future.")
        for change in island.get("regime_changes",[]):
            if int(change["timestamp_us"]) > final_ts:
                raise CausalValidationError("Regime timestamp is in future.")
        for protected in island.get("protected_swings",[]):
            if int(protected["timestamp_us"]) > final_ts:
                raise CausalValidationError("Protected Swing timestamp is in future.")


def prefix_invariance(records: list[dict]) -> dict:
    full=run_profile(
        records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    assert_no_cross_island_objects(full)
    full_map={x["analysis_island_id"]:x for x in full["islands"]}

    checkpoints=[]
    # Test multiple prefixes inside each island, always respecting island split.
    by_island={}
    for r in records:
        by_island.setdefault(r["analysis_island_id"],[]).append(r)

    accumulated=[]
    for island_id in sorted(by_island):
        current=by_island[island_id]
        prior=list(accumulated)
        for size in sorted(set([
            min(len(current),24),
            max(1,len(current)//2),
            max(1,len(current)-5),
            len(current),
        ])):
            prefix=prior+current[:size]
            run=run_profile(
                prefix,
                profile_id=PROFILE_ID,
                detector=DETECTOR,
                structural=STRUCTURAL,
            )
            assert_no_cross_island_objects(run)
            assert_future_timestamp_audit(run,prefix)
            prefix_map={x["analysis_island_id"]:x for x in run["islands"]}

            for pid,pisland in prefix_map.items():
                max_bar=len(
                    [x for x in prefix if x["analysis_island_id"]==pid]
                )-1
                expected=_objects_visible_through(full_map[pid],max_bar)
                actual=_objects_visible_through(pisland,max_bar)
                if actual != expected:
                    raise CausalValidationError(
                        f"Prefix invariance failed for {pid} at size {size}"
                    )
            checkpoints.append({
                "island_id":island_id,
                "size":size,
                "run_sha256":run["run_sha256"],
            })
        accumulated += current
    return {
        "status":"PASS",
        "checkpoint_count":len(checkpoints),
        "checkpoints":checkpoints,
    }


def checkpoint_restart(records: list[dict]) -> dict:
    """Reference checkpoint stores revealed candles + frozen profile config only."""
    cut=len(records)//3
    revealed=copy.deepcopy(records[:cut])
    checkpoint={
        "experiment_id":"ASSET-P1-D1-001",
        "profile_id":PROFILE_ID,
        "detector":copy.deepcopy(DETECTOR),
        "structural":copy.deepcopy(STRUCTURAL),
        "revealed_records":revealed,
    }
    checkpoint["checkpoint_sha256"]=sha256_obj(checkpoint)

    restored_payload={
        k:copy.deepcopy(v)
        for k,v in checkpoint.items()
        if k!="checkpoint_sha256"
    }
    if sha256_obj(restored_payload) != checkpoint["checkpoint_sha256"]:
        raise CausalValidationError("Checkpoint integrity mismatch.")

    before=run_profile(
        revealed,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    restored=run_profile(
        restored_payload["revealed_records"],
        profile_id=restored_payload["profile_id"],
        detector=restored_payload["detector"],
        structural=restored_payload["structural"],
    )
    if _strip_hashes(before) != _strip_hashes(restored):
        raise CausalValidationError("Checkpoint recomputation mismatch.")

    resumed_records=restored_payload["revealed_records"]+copy.deepcopy(records[cut:])
    resumed=run_profile(
        resumed_records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    direct=run_profile(
        records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    if _strip_hashes(resumed) != _strip_hashes(direct):
        raise CausalValidationError("Checkpoint/restart full-run mismatch.")

    return {
        "status":"PASS",
        "checkpoint_sha256":checkpoint["checkpoint_sha256"],
        "final_run_sha256":direct["run_sha256"],
    }


def island_reset(records: list[dict]) -> dict:
    by_island={}
    for r in records:
        by_island.setdefault(r["analysis_island_id"],[]).append(r)

    combined=run_profile(
        records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    combined_map={x["analysis_island_id"]:x for x in combined["islands"]}

    hashes={}
    for island_id,candles in sorted(by_island.items()):
        standalone=run_profile(
            candles,
            profile_id=PROFILE_ID,
            detector=DETECTOR,
            structural=STRUCTURAL,
        )
        if len(standalone["islands"]) != 1:
            raise CausalValidationError("Standalone island produced invalid island count.")
        a=copy.deepcopy(standalone["islands"][0])
        b=copy.deepcopy(combined_map[island_id])
        a.pop("result_sha256",None)
        b.pop("result_sha256",None)
        if a != b:
            raise CausalValidationError(
                f"Analysis Island state leaked across boundary: {island_id}"
            )
        hashes[island_id]=combined_map[island_id]["result_sha256"]

    assert_no_cross_island_objects(combined)
    return {
        "status":"PASS",
        "island_count":len(by_island),
        "island_hashes":hashes,
    }


def main() -> int:
    records=fixture()

    run_a=run_profile(
        records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    run_b=run_profile(
        records,
        profile_id=PROFILE_ID,
        detector=DETECTOR,
        structural=STRUCTURAL,
    )
    if run_a["run_sha256"] != run_b["run_sha256"]:
        raise CausalValidationError("Repeated-run determinism failed.")

    result={
        "experiment_id":"ASSET-P1-D1-001",
        "status":"PASS",
        "repeated_run":{
            "status":"PASS",
            "hash_a":run_a["run_sha256"],
            "hash_b":run_b["run_sha256"],
        },
        "prefix_invariance":prefix_invariance(records),
        "future_timestamp_audit":{"status":"PASS"},
        "checkpoint_restart":checkpoint_restart(records),
        "analysis_island_reset":island_reset(records),
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
