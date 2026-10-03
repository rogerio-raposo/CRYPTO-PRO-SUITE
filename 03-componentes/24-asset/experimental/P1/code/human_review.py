#!/usr/bin/env python3
"""Deterministic Human Review sampling/blinding for ASSET-P1-D1-001."""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass
from decimal import Decimal
from typing import Mapping, Sequence

from d1_matching import match_events, match_swings
from d1_structure import StructuralEvent
from d1_swings import Swing


class ReviewError(RuntimeError):
    pass


def canonical_bytes(obj: object) -> bytes:
    return (
        json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"),default=str)
        +"\n"
    ).encode("utf-8")


def sha256_obj(obj: object) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def blinded_alias_map(profile_ids: Sequence[str]) -> dict[str,str]:
    ordered=sorted(
        set(profile_ids),
        key=lambda pid:(hashlib.sha256(pid.encode("utf-8")).hexdigest(),pid),
    )
    return {pid:f"R{i:02d}" for i,pid in enumerate(ordered,1)}


@dataclass(frozen=True)
class ReviewWindow:
    analysis_island_id: str
    start_index: int
    end_index: int
    focal_timestamp_us: int
    truncated_context: bool
    disagreement: Decimal | None
    churn_magnitude: Decimal
    event_delay_magnitude: int | None


def _objects(island: dict):
    swings=tuple(Swing(**x) for x in island.get("swings",[]))
    events=tuple(StructuralEvent(**x) for x in island.get("events",[]))
    return swings,events


def _run_island_map(run: dict) -> dict[str,dict]:
    return {str(x["analysis_island_id"]):x for x in run.get("islands",[])}


def _filter_swings(
    swings: Sequence[Swing],
    start: int,
    end: int,
) -> tuple[Swing,...]:
    return tuple(
        x for x in swings
        if start <= int(x.confirmation_index) <= end
    )


def _filter_events(
    events: Sequence[StructuralEvent],
    start: int,
    end: int,
) -> tuple[StructuralEvent,...]:
    return tuple(
        x for x in events
        if start <= int(x.bar_index) <= end
    )


def generate_window_diagnostics(
    *,
    profile_runs: Mapping[str,dict],
    analytical_records: Sequence[dict],
    timeframe: str,
) -> tuple[ReviewWindow,...]:
    if len(profile_runs)<1:
        raise ReviewError("No profile runs supplied.")
    context_bars=120 if timeframe=="4h" else 90 if timeframe=="1d" else None
    if context_bars is None:
        raise ReviewError(f"Unsupported review timeframe: {timeframe}")

    records_by_island: dict[str,list[dict]]={}
    for record in analytical_records:
        records_by_island.setdefault(str(record["analysis_island_id"]),[]).append(dict(record))

    island_maps={pid:_run_island_map(run) for pid,run in profile_runs.items()}
    expected=set(records_by_island)
    for pid,mapping in island_maps.items():
        if set(mapping)!=expected:
            raise ReviewError(f"Profile {pid} Analysis Island set mismatch.")

    pids=sorted(profile_runs)
    windows: list[ReviewWindow]=[]

    for island_id in sorted(records_by_island):
        candles=records_by_island[island_id]
        n=len(candles)
        if n==0:
            continue
        if n<context_bars:
            ranges=[(0,n-1,True)]
        else:
            ranges=[(end-context_bars+1,end,False) for end in range(context_bars-1,n)]

        prepared={}
        for pid in pids:
            prepared[pid]=_objects(island_maps[pid][island_id])

        for start,end,truncated in ranges:
            disagreement_values=[]
            event_delays=[]
            churn_values=[]

            for pid in pids:
                island=island_maps[pid][island_id]
                changes=[
                    x for x in island.get("regime_changes",[])
                    if start <= int(x["bar_index"]) <= end
                ]
                length=end-start+1
                churn_values.append(
                    Decimal(1000)*Decimal(len(changes))/Decimal(length)
                )

            for a,b in itertools.combinations(pids,2):
                swings_a,events_a=prepared[a]
                swings_b,events_b=prepared[b]
                sa=_filter_swings(swings_a,start,end)
                sb=_filter_swings(swings_b,start,end)
                sm=match_swings(sa,sb,candles,timeframe=timeframe,mode="BASE")
                disagreement_values.append(Decimal("1")-Decimal(sm.swing_stability))

                ea=_filter_events(events_a,start,end)
                eb=_filter_events(events_b,start,end)
                em=match_events(ea,eb,candles,timeframe=timeframe)
                event_delays.extend(x.bar_distance for x in em.matched_pairs)

            windows.append(
                ReviewWindow(
                    analysis_island_id=island_id,
                    start_index=start,
                    end_index=end,
                    focal_timestamp_us=int(candles[end]["interval_end_us"]),
                    truncated_context=truncated,
                    disagreement=(
                        max(disagreement_values) if disagreement_values else None
                    ),
                    churn_magnitude=max(churn_values) if churn_values else Decimal("0"),
                    event_delay_magnitude=(
                        max(event_delays) if event_delays else None
                    ),
                )
            )
    return tuple(windows)


def select_review_cases(windows: Sequence[ReviewWindow]) -> tuple[dict,...]:
    remaining=list(windows)
    selected=[]

    def take_best(name: str, key_name: str) -> None:
        nonlocal remaining
        eligible=[
            w for w in remaining
            if getattr(w,key_name) is not None
        ]
        if not eligible:
            selected.append({"criterion":name,"status":"NO_ELIGIBLE_CASE"})
            return
        best=max(
            eligible,
            key=lambda w:(
                getattr(w,key_name),
                -int(w.focal_timestamp_us),
            ),
        )
        selected.append({
            "criterion":name,
            "status":"SELECTED",
            **best.__dict__,
        })
        remaining=[w for w in remaining if w!=best]

    take_best("HIGHEST_DISAGREEMENT","disagreement")
    take_best("HIGHEST_REGIME_CHURN","churn_magnitude")
    take_best("HIGHEST_EVENT_DELAY","event_delay_magnitude")

    eligible=[w for w in remaining if w.disagreement is not None]
    if not eligible:
        selected.append({"criterion":"MEDIAN_DISAGREEMENT","status":"NO_ELIGIBLE_CASE"})
    else:
        ordered=sorted(
            eligible,
            key=lambda w:(w.disagreement,w.focal_timestamp_us),
        )
        median_index=(len(ordered)-1)//2
        median_value=ordered[median_index].disagreement
        same=[w for w in ordered if w.disagreement==median_value]
        chosen=min(same,key=lambda w:w.focal_timestamp_us)
        selected.append({
            "criterion":"MEDIAN_DISAGREEMENT",
            "status":"SELECTED",
            **chosen.__dict__,
        })
    return tuple(selected)


def build_review_package(
    *,
    review_set_id: str,
    profile_runs: Mapping[str,dict],
    analytical_records: Sequence[dict],
    timeframe: str,
    cell_identity: dict,
) -> tuple[dict,dict]:
    aliases=blinded_alias_map(list(profile_runs))
    windows=generate_window_diagnostics(
        profile_runs=profile_runs,
        analytical_records=analytical_records,
        timeframe=timeframe,
    )
    cases=select_review_cases(windows)

    records_by_island: dict[str,list[dict]]={}
    for record in analytical_records:
        records_by_island.setdefault(str(record["analysis_island_id"]),[]).append(dict(record))
    run_maps={pid:_run_island_map(run) for pid,run in profile_runs.items()}

    exported=[]
    for case in cases:
        if case["status"]!="SELECTED":
            exported.append(dict(case))
            continue
        island_id=case["analysis_island_id"]
        start=int(case["start_index"])
        end=int(case["end_index"])
        candles=records_by_island[island_id][start:end+1]
        blinded_profiles={}
        for pid in sorted(profile_runs):
            island=run_maps[pid][island_id]
            alias=aliases[pid]
            blinded_profiles[alias]={
                "swings":[
                    {
                        "kind":x["kind"],
                        "extremum_index":x["extremum_index"],
                        "extremum_open_us":x["extremum_open_us"],
                        "price":x["price"],
                        "confirmation_index":x["confirmation_index"],
                        "confirmation_end_us":x["confirmation_end_us"],
                    }
                    for x in island.get("swings",[])
                    if int(x["confirmation_index"]) <= end
                    and int(x["extremum_index"]) >= start
                ],
                "events":[
                    x for x in island.get("events",[])
                    if start <= int(x["bar_index"]) <= end
                ],
                "protected_swings":[
                    x for x in island.get("protected_swings",[])
                    if start <= int(x["bar_index"]) <= end
                ],
                "regime_timeline":list(island.get("regime_by_bar",[]))[start:end+1],
            }
        exported.append({
            **case,
            "candles":candles,
            "profiles":blinded_profiles,
        })

    package={
        "experiment_id":"ASSET-P1-D1-001",
        "review_set_id":review_set_id,
        "cell_identity":dict(cell_identity),
        "timeframe":timeframe,
        "profile_aliases":sorted(aliases.values()),
        "cases":exported,
        "response_vocabulary":["YES","NO","INDETERMINATE"],
    }
    assert_reviewer_package_blinded(package)
    package["package_sha256"]=sha256_obj(package)

    mapping={
        "experiment_id":"ASSET-P1-D1-001",
        "review_set_id":review_set_id,
        "alias_to_profile":{alias:pid for pid,alias in aliases.items()},
    }
    mapping["mapping_sha256"]=sha256_obj(mapping)
    return package,mapping



def assert_reviewer_package_blinded(package: dict) -> None:
    """Reject reviewer-facing payloads that leak method/profile identity."""
    prohibited={"method","profile_id","volatility_ref","detector","estimator","window","multiplier","percentage"}

    def walk(value,path="$"):
        if isinstance(value,dict):
            for key,item in value.items():
                if str(key) in prohibited:
                    raise ReviewError(f"Reviewer package leaks prohibited key {key!r} at {path}.")
                walk(item,f"{path}.{key}")
        elif isinstance(value,list):
            for i,item in enumerate(value):
                walk(item,f"{path}[{i}]")

    walk(package)


def completed_review_record(
    *,
    review_set_id: str,
    package_sha256: str,
    reviewer_id: str,
    responses: Sequence[dict],
) -> dict:
    allowed={"YES","NO","INDETERMINATE"}
    for response in responses:
        if response.get("response") not in allowed:
            raise ReviewError("Invalid Human Review response.")
    record={
        "experiment_id":"ASSET-P1-D1-001",
        "review_set_id":review_set_id,
        "package_sha256":package_sha256,
        "reviewer_id":reviewer_id,
        "responses":[dict(x) for x in responses],
    }
    record["review_sha256"]=sha256_obj(record)
    return record


def exact_response_agreement(review_records: Sequence[dict]) -> dict:
    if len(review_records)<2:
        return {"status":"INSUFFICIENT_REVIEWERS","overall":None,"per_question":{}}

    maps=[]
    for record in review_records:
        m={}
        for r in record.get("responses",[]):
            key=(r.get("case_id"),r.get("question_id"))
            m[key]=r.get("response")
        maps.append(m)
    common=set(maps[0])
    for m in maps[1:]:
        common &= set(m)

    per_question: dict[str,list[int]]={}
    exact_total=0
    for key in sorted(common):
        values=[m[key] for m in maps]
        exact=int(len(set(values))==1)
        exact_total += exact
        q=str(key[1])
        per_question.setdefault(q,[]).append(exact)

    return {
        "status":"OK",
        "joint_items":len(common),
        "overall":(
            None if not common else Decimal(exact_total)/Decimal(len(common))
        ),
        "per_question":{
            q:Decimal(sum(vals))/Decimal(len(vals))
            for q,vals in sorted(per_question.items())
        },
    }
