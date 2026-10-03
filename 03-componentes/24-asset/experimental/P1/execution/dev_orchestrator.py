#!/usr/bin/env python3
"""Formal DEV orchestration for ASSET-P1-D1-001.

This file is execution orchestration only. Analytical semantics are imported
from the frozen ASSET-P1-D1-CODE-0.1.0 implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import asdict, is_dataclass
from decimal import Decimal
from pathlib import Path
from typing import Mapping, Sequence

from d1_matching import match_swings
from d1_metrics import (
    build_plateau_graph,
    freeze_pair_reference_bands,
    freeze_single_reference_bands,
    pairwise_cell_metrics,
    select_behavioral_representatives,
    single_profile_cell_metrics,
)
from d1_runner import run_profile, split_analysis_islands
from d1_swings import (
    assert_swing_invariants,
    volatility_normalized_reversal,
)
from human_review import build_review_package
from p1_profiles import (
    M3_ESTIMATORS,
    P1Profile,
    adjacency_edges,
    build_profiles,
)


EXPERIMENT_ID = "ASSET-P1-D1-001"
SPEC_ID = "ASSET-P1-D1-SPEC-REV03"
CODE_VERSION = "ASSET-P1-D1-CODE-0.1.0"
DATA_VERSION = "ASSET-P1-DATA-0.2.0"

ASSETS = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT")
DEV_SEGMENTS = ("DEV-01", "DEV-02")
TIMEFRAMES = ("4h", "1d")


class DevExecutionError(RuntimeError):
    pass


def jsonable(value):
    if isinstance(value, Decimal):
        return str(value)
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(v) for v in value]
    return value


def canonical_bytes(obj) -> bytes:
    return (
        json.dumps(
            jsonable(obj),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_obj(obj) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    out=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            value=json.loads(line)
            if not isinstance(value, dict):
                raise DevExecutionError(f"Non-object JSONL record in {path}")
            out.append(value)
    return out


def analytical_path(root: Path, segment: str, asset: str, timeframe: str) -> Path:
    suffix="analytical_4h.jsonl" if timeframe=="4h" else "analytical_1d.jsonl"
    return root/"dev"/segment/asset/suffix


def cell_id(asset: str, segment: str) -> str:
    return f"{asset}|{segment}"


def load_cell(root: Path, asset: str, segment: str, timeframe: str) -> list[dict]:
    path=analytical_path(root,segment,asset,timeframe)
    if not path.exists():
        raise DevExecutionError(f"Missing DEV analytical file: {path}")
    records=read_jsonl(path)
    if not records:
        raise DevExecutionError(f"Empty DEV analytical file: {path}")
    if any(str(r.get("instrument")) != asset for r in records):
        raise DevExecutionError(f"Instrument identity mismatch in {path}")
    return records


def detector_from_profile(profile: P1Profile) -> dict:
    d=profile.detector_dict()
    if profile.method=="M1":
        return {"method":"M1","window":d["window"]}
    if profile.method=="M2":
        return {"method":"M2","percentage":d["percentage"]}
    if profile.method=="M3":
        return {
            "method":"M3",
            "estimator":d["estimator"],
            "window":d["window"],
            "multiplier":d["multiplier"],
        }
    raise DevExecutionError(f"Unsupported method: {profile.method}")


def profile_catalog(
    *,
    timeframe: str,
    m3_estimators: Sequence[str] = M3_ESTIMATORS,
) -> dict[str,P1Profile]:
    out={}
    for method in ("M1","M2"):
        for profile in build_profiles(method,timeframe):
            out[profile.profile_id]=profile
    for profile in build_profiles(
        "M3",timeframe,m3_estimators=tuple(m3_estimators)
    ):
        out[profile.profile_id]=profile
    return out


def command_screen_m3(args) -> int:
    root=Path(args.data_root)
    result={
        "experiment_id":EXPERIMENT_ID,
        "stage":"M3_ESTIMATOR_SCREEN",
        "specification_id":SPEC_ID,
        "code_version":CODE_VERSION,
        "data_package_version":DATA_VERSION,
        "estimators":{},
    }

    survivors=[]
    for estimator in M3_ESTIMATORS:
        est={
            "status":"PASS",
            "hard_blockers":[],
            "cells":{},
        }
        for timeframe in TIMEFRAMES:
            for asset in ASSETS:
                for segment in DEV_SEGMENTS:
                    cid=f"{timeframe}|{asset}|{segment}"
                    records=load_cell(root,asset,segment,timeframe)
                    cell_swings=0
                    island_count=0
                    try:
                        for _,candles in split_analysis_islands(records):
                            island_count += 1
                            a=volatility_normalized_reversal(
                                candles,
                                estimator=estimator,
                                window=14,
                                multiplier="2.0",
                            )
                            b=volatility_normalized_reversal(
                                candles,
                                estimator=estimator,
                                window=14,
                                multiplier="2.0",
                            )
                            assert_swing_invariants(a.swings)
                            assert_swing_invariants(b.swings)
                            if jsonable(a) != jsonable(b):
                                raise DevExecutionError(
                                    f"Nondeterministic M3 screen: {cid}/{estimator}"
                                )
                            cell_swings += len(a.swings)
                        est["cells"][cid]={
                            "status":"PASS",
                            "analysis_islands":island_count,
                            "confirmed_swings":cell_swings,
                        }
                    except Exception as exc:
                        est["status"]="FAIL"
                        est["hard_blockers"].append({
                            "cell":cid,
                            "type":type(exc).__name__,
                            "detail":str(exc),
                        })
        if est["status"]=="PASS":
            survivors.append(estimator)
        result["estimators"][estimator]=est

    result["surviving_estimators"]=sorted(survivors)
    result["status"]="PASS" if survivors else "FAIL"
    result["result_sha256"]=sha256_obj(result)
    Path(args.output).write_bytes(canonical_bytes(result))

    if not survivors:
        raise DevExecutionError("M3 estimator screen left no surviving estimator.")
    print(json.dumps(jsonable(result),indent=2,sort_keys=True))
    return 0


def _pair_key(a: str,b: str) -> str:
    x,y=sorted((a,b))
    return f"{x}|||{y}"


def command_grid(args) -> int:
    root=Path(args.data_root)
    method=args.method
    timeframe=args.timeframe
    estimator=args.estimator

    screen=json.loads(Path(args.m3_screen).read_text(encoding="utf-8"))
    survivors=tuple(screen["surviving_estimators"])

    if method=="M3":
        if estimator not in survivors:
            result={
                "experiment_id":EXPERIMENT_ID,
                "stage":"DEV_GRID",
                "method":method,
                "timeframe":timeframe,
                "estimator":estimator,
                "status":"SKIPPED_ESTIMATOR_NOT_SURVIVING",
                "profiles":[],
                "single_metrics":{},
                "pair_metrics":{},
                "hard_blocked_profiles":[],
            }
            result["result_sha256"]=sha256_obj(result)
            Path(args.output).write_bytes(canonical_bytes(result))
            return 0
        profiles=list(build_profiles(
            "M3",timeframe,m3_estimators=(estimator,)
        ))
    else:
        profiles=list(build_profiles(method,timeframe))

    profile_map={p.profile_id:p for p in profiles}
    edges=adjacency_edges(profiles)
    single_metrics={pid:{} for pid in sorted(profile_map)}
    pair_metrics={_pair_key(a,b):{} for a,b in edges}
    hard_blocked=set()
    run_hashes={pid:{} for pid in sorted(profile_map)}

    for asset in ASSETS:
        for segment in DEV_SEGMENTS:
            cid=cell_id(asset,segment)
            records=load_cell(root,asset,segment,timeframe)
            runs={}
            for profile in profiles:
                try:
                    run=run_profile(
                        records,
                        profile_id=profile.profile_id,
                        detector=detector_from_profile(profile),
                        structural=profile.structural_dict(),
                    )
                    metrics=single_profile_cell_metrics(run)
                    if int(metrics.get("DirectTrendFlipCount",0)) != 0:
                        hard_blocked.add(profile.profile_id)
                    runs[profile.profile_id]=run
                    single_metrics[profile.profile_id][cid]=jsonable(metrics)
                    run_hashes[profile.profile_id][cid]=run["run_sha256"]
                except Exception as exc:
                    hard_blocked.add(profile.profile_id)
                    single_metrics[profile.profile_id][cid]={
                        "HARD_BLOCKER":type(exc).__name__,
                        "detail":str(exc),
                    }

            for a,b in edges:
                if a not in runs or b not in runs:
                    continue
                try:
                    metrics=pairwise_cell_metrics(
                        runs[a],
                        runs[b],
                        records,
                        timeframe=timeframe,
                    )
                    pair_metrics[_pair_key(a,b)][cid]=jsonable(metrics)
                except Exception as exc:
                    hard_blocked.add(a)
                    hard_blocked.add(b)
                    pair_metrics[_pair_key(a,b)][cid]={
                        "HARD_BLOCKER":type(exc).__name__,
                        "detail":str(exc),
                    }

    result={
        "experiment_id":EXPERIMENT_ID,
        "stage":"DEV_GRID",
        "specification_id":SPEC_ID,
        "code_version":CODE_VERSION,
        "data_package_version":DATA_VERSION,
        "method":method,
        "timeframe":timeframe,
        "estimator":estimator,
        "status":"PASS",
        "profiles":[p.profile_id for p in profiles],
        "single_metrics":single_metrics,
        "pair_metrics":pair_metrics,
        "hard_blocked_profiles":sorted(hard_blocked),
        "run_hashes":run_hashes,
    }
    result["result_sha256"]=sha256_obj(result)
    Path(args.output).write_bytes(canonical_bytes(result))
    print(json.dumps({
        "method":method,
        "timeframe":timeframe,
        "estimator":estimator,
        "profile_count":len(profiles),
        "edge_count":len(edges),
        "hard_blocked_profile_count":len(hard_blocked),
        "result_sha256":result["result_sha256"],
    },indent=2,sort_keys=True))
    return 0


def _load_grid_files(root: Path) -> list[dict]:
    files=sorted(root.rglob("grid-*.json"))
    if not files:
        raise DevExecutionError(f"No grid result files under {root}")
    return [json.loads(p.read_text(encoding="utf-8")) for p in files]


def _profiles_for_method_tf(
    method: str,
    timeframe: str,
    survivors: Sequence[str],
) -> list[P1Profile]:
    if method=="M3":
        return list(build_profiles(
            "M3",timeframe,m3_estimators=tuple(survivors)
        ))
    return list(build_profiles(method,timeframe))


def _merge_method_grid(
    grids: Sequence[dict],
    method: str,
    timeframe: str,
) -> tuple[dict,dict,set[str]]:
    selected=[
        g for g in grids
        if g.get("method")==method
        and g.get("timeframe")==timeframe
        and g.get("status")=="PASS"
    ]
    if not selected:
        raise DevExecutionError(f"No successful grid result for {method}/{timeframe}")

    single={}
    pairs={}
    blocked=set()
    for g in selected:
        blocked.update(g.get("hard_blocked_profiles",[]))
        for pid,cells in g["single_metrics"].items():
            single[pid]=cells
        for key,cells in g["pair_metrics"].items():
            pairs[key]=cells
    return single,pairs,blocked


def _tuple_pair_metrics(pair_dict: Mapping[str,dict]) -> dict:
    out={}
    for key,value in pair_dict.items():
        a,b=key.split("|||",1)
        out[(a,b)]=value
    return out


def _candidate_profile_map(
    candidate_records: Sequence[dict],
    *,
    survivors: Sequence[str],
) -> dict[str,P1Profile]:
    catalog={}
    for tf in TIMEFRAMES:
        catalog.update(profile_catalog(
            timeframe=tf,m3_estimators=survivors
        ))
    out={}
    for record in candidate_records:
        pid=record["profile_id"]
        if pid not in catalog:
            raise DevExecutionError(f"Candidate absent from frozen profile catalog: {pid}")
        out[pid]=catalog[pid]
    return out


def _run_candidate_cells(
    root: Path,
    candidate_profiles: Mapping[str,P1Profile],
) -> dict[str,dict[str,dict]]:
    cache={pid:{} for pid in candidate_profiles}
    for pid,profile in candidate_profiles.items():
        tf=profile.timeframe
        for asset in ASSETS:
            for segment in DEV_SEGMENTS:
                cid=cell_id(asset,segment)
                records=load_cell(root,asset,segment,tf)
                cache[pid][cid]=run_profile(
                    records,
                    profile_id=pid,
                    detector=detector_from_profile(profile),
                    structural=profile.structural_dict(),
                )
    return cache


def command_aggregate(args) -> int:
    data_root=Path(args.data_root)
    grids=_load_grid_files(Path(args.grid_root))
    screen=json.loads(Path(args.m3_screen).read_text(encoding="utf-8"))
    survivors=tuple(screen["surviving_estimators"])
    output_root=Path(args.output_root)
    output_root.mkdir(parents=True,exist_ok=True)

    candidate_records=[]
    method_results={}

    for timeframe in TIMEFRAMES:
        for method in ("M1","M2","M3"):
            profiles=_profiles_for_method_tf(method,timeframe,survivors)
            single,pair_raw,blocked=_merge_method_grid(
                grids,method,timeframe
            )
            pair=_tuple_pair_metrics(pair_raw)

            # Remove cell entries that are hard-blocker placeholders from plateau input.
            filtered_single={
                pid:{
                    cid:m for cid,m in cells.items()
                    if "HARD_BLOCKER" not in m
                }
                for pid,cells in single.items()
            }
            filtered_pair={
                edge:{
                    cid:m for cid,m in cells.items()
                    if "HARD_BLOCKER" not in m
                }
                for edge,cells in pair.items()
            }

            plateau=build_plateau_graph(
                profiles,
                single_metrics=filtered_single,
                pair_metrics=filtered_pair,
                hard_blocked_profiles=blocked,
            )
            reps=select_behavioral_representatives(
                plateau,
                single_metrics=filtered_single,
            )

            proposal={}
            for label,record in sorted(reps.items()):
                pid=record["profile_id"]
                enriched={
                    "profile_id":pid,
                    "method":method,
                    "timeframe":timeframe,
                    "behavioral_label":label,
                    "plateau_membership":record["plateau_membership"],
                    "pooled_dev_swing_density":str(
                        record["pooled_dev_swing_density"]
                    ),
                    "single_reference_bands":jsonable(
                        freeze_single_reference_bands(filtered_single[pid])
                    ),
                }
                candidate_records.append(enriched)
                proposal[label]=enriched

            method_results[f"{method}|{timeframe}"]={
                "profile_count":len(profiles),
                "hard_blocked_profiles":sorted(blocked),
                "stable_edge_count":len(plateau.stable_edges),
                "plateaus":[list(x) for x in plateau.plateaus],
                "component_fences":jsonable(plateau.component_fences),
                "candidate_proposal":proposal,
            }

    if not candidate_records:
        raise DevExecutionError("DEV quantitative stage produced no candidates.")

    candidate_profiles=_candidate_profile_map(
        candidate_records,survivors=survivors
    )
    run_cache=_run_candidate_cells(data_root,candidate_profiles)

    # Pair reference bands across all proposed candidates in the same timeframe.
    pair_reference_bands={}
    for timeframe in TIMEFRAMES:
        pids=sorted(
            pid for pid,p in candidate_profiles.items()
            if p.timeframe==timeframe
        )
        for a,b in itertools.combinations(pids,2):
            cells={}
            for asset in ASSETS:
                for segment in DEV_SEGMENTS:
                    cid=cell_id(asset,segment)
                    records=load_cell(data_root,asset,segment,timeframe)
                    cells[cid]=jsonable(pairwise_cell_metrics(
                        run_cache[a][cid],
                        run_cache[b][cid],
                        records,
                        timeframe=timeframe,
                    ))
            pair_reference_bands[_pair_key(a,b)]=jsonable(
                freeze_pair_reference_bands(cells)
            )

    reference={
        "experiment_id":EXPERIMENT_ID,
        "phase":"DEV",
        "candidate_records":sorted(
            candidate_records,key=lambda x:x["profile_id"]
        ),
        "pair_reference_bands":pair_reference_bands,
    }
    reference["metrics_reference_sha256"]=sha256_obj(reference)
    (output_root/"DEV_REFERENCE_BANDS.json").write_bytes(
        canonical_bytes(reference)
    )

    proposal={
        "experiment_id":EXPERIMENT_ID,
        "phase":"DEV",
        "m3_estimator_screen":screen,
        "method_timeframe_results":method_results,
        "candidate_records":reference["candidate_records"],
        "metrics_reference_sha256":reference["metrics_reference_sha256"],
        "status":"QUANTITATIVE_PROPOSAL_READY_FOR_HUMAN_REVIEW",
    }
    proposal["proposal_sha256"]=sha256_obj(proposal)
    (output_root/"DEV_QUANTITATIVE_PROPOSAL.json").write_bytes(
        canonical_bytes(proposal)
    )

    package_dir=output_root/"human_review"/"packages"
    mapping_dir=output_root/"human_review"/"mappings"
    package_dir.mkdir(parents=True,exist_ok=True)
    mapping_dir.mkdir(parents=True,exist_ok=True)
    review_index=[]

    for timeframe in TIMEFRAMES:
        tf_pids=sorted(
            pid for pid,p in candidate_profiles.items()
            if p.timeframe==timeframe
        )
        if not tf_pids:
            continue
        for asset in ASSETS:
            profile_runs={}
            analytical=[]
            for pid in tf_pids:
                combined={
                    "profile_id":pid,
                    "islands":[],
                }
                for segment in DEV_SEGMENTS:
                    cid=cell_id(asset,segment)
                    combined["islands"].extend(
                        run_cache[pid][cid]["islands"]
                    )
                profile_runs[pid]=combined
            for segment in DEV_SEGMENTS:
                analytical.extend(
                    load_cell(data_root,asset,segment,timeframe)
                )

            review_id=f"DEV-{asset}-{timeframe.upper()}"
            package,mapping=build_review_package(
                review_set_id=review_id,
                profile_runs=profile_runs,
                analytical_records=analytical,
                timeframe=timeframe,
                cell_identity={
                    "phase":"DEV",
                    "asset":asset,
                    "timeframe":timeframe,
                    "segments":list(DEV_SEGMENTS),
                },
            )
            (package_dir/f"{review_id}.json").write_bytes(
                canonical_bytes(package)
            )
            (mapping_dir/f"{review_id}.json").write_bytes(
                canonical_bytes(mapping)
            )
            selected=sum(
                1 for case in package.get("cases",[])
                if case.get("status")=="SELECTED"
            )
            review_index.append({
                "review_set_id":review_id,
                "asset":asset,
                "timeframe":timeframe,
                "selected_cases":selected,
                "package_sha256":package["package_sha256"],
                "mapping_sha256":mapping["mapping_sha256"],
            })

    review_manifest={
        "experiment_id":EXPERIMENT_ID,
        "phase":"DEV",
        "review_sets":review_index,
        "review_set_count":len(review_index),
        "selected_case_count":sum(x["selected_cases"] for x in review_index),
    }
    review_manifest["review_manifest_sha256"]=sha256_obj(review_manifest)
    (output_root/"DEV_HUMAN_REVIEW_MANIFEST.json").write_bytes(
        canonical_bytes(review_manifest)
    )

    final={
        "experiment_id":EXPERIMENT_ID,
        "phase":"DEV",
        "status":"AWAITING_HUMAN_REVIEW",
        "m3_surviving_estimators":list(survivors),
        "candidate_count":len(candidate_records),
        "metrics_reference_sha256":reference["metrics_reference_sha256"],
        "proposal_sha256":proposal["proposal_sha256"],
        "review_manifest_sha256":review_manifest["review_manifest_sha256"],
        "review_set_count":review_manifest["review_set_count"],
        "review_case_count":review_manifest["selected_case_count"],
    }
    final["result_sha256"]=sha256_obj(final)
    (output_root/"DEV_QUANTITATIVE_SUMMARY.json").write_bytes(
        canonical_bytes(final)
    )
    print(json.dumps(final,indent=2,sort_keys=True))
    return 0


def main() -> int:
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="command",required=True)

    p=sub.add_parser("screen-m3")
    p.add_argument("--data-root",required=True)
    p.add_argument("--output",required=True)

    p=sub.add_parser("grid")
    p.add_argument("--data-root",required=True)
    p.add_argument("--m3-screen",required=True)
    p.add_argument("--method",choices=("M1","M2","M3"),required=True)
    p.add_argument("--timeframe",choices=TIMEFRAMES,required=True)
    p.add_argument("--estimator")
    p.add_argument("--output",required=True)

    p=sub.add_parser("aggregate")
    p.add_argument("--data-root",required=True)
    p.add_argument("--m3-screen",required=True)
    p.add_argument("--grid-root",required=True)
    p.add_argument("--output-root",required=True)

    args=parser.parse_args()
    if args.command=="screen-m3":
        return command_screen_m3(args)
    if args.command=="grid":
        if args.method=="M3" and not args.estimator:
            raise SystemExit("--estimator is required for M3 grid")
        if args.method!="M3" and args.estimator:
            raise SystemExit("--estimator is only valid for M3 grid")
        return command_grid(args)
    if args.command=="aggregate":
        return command_aggregate(args)
    raise SystemExit("unknown command")


if __name__=="__main__":
    raise SystemExit(main())
