#!/usr/bin/env python3
"""Metrics, plateau graph and DEV reference bands for ASSET-P1-D1-001."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, Mapping, Sequence

from d1_matching import (
    match_events,
    match_protected_promotions,
    match_swings,
)
from d1_structure import ProtectedSwingSnapshot, StructuralEvent
from d1_swings import Swing, wilder_atr
from p1_profiles import P1Profile, adjacency_edges


class MetricsError(RuntimeError):
    pass


def _d(value) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def type7_quantile(values: Sequence[Decimal | int | str], p: Decimal | str) -> Decimal | None:
    items=sorted(_d(v) for v in values)
    if not items:
        return None
    q=_d(p)
    if q < 0 or q > 1:
        raise MetricsError("Quantile p must be in [0,1].")
    if len(items)==1:
        return items[0]
    h=Decimal(len(items)-1)*q
    lo=int(h)
    hi=lo if h==Decimal(lo) else lo+1
    gamma=h-Decimal(lo)
    return items[lo]+gamma*(items[hi]-items[lo])


def median(values: Sequence[Decimal | int | str]) -> Decimal | None:
    return type7_quantile(values,Decimal("0.50"))


def p90(values: Sequence[Decimal | int | str]) -> Decimal | None:
    return type7_quantile(values,Decimal("0.90"))


def robust_fence(
    values: Sequence[Decimal | int | str],
    *,
    direction: str,
    bounded_rate: bool=False,
    nonnegative: bool=True,
) -> dict:
    items=[_d(v) for v in values]
    if len(items)<4:
        return {
            "status":"INSUFFICIENT_REFERENCE",
            "n":len(items),
            "lower":None,
            "upper":None,
            "q1":None,
            "q3":None,
            "iqr":None,
        }
    q1=type7_quantile(items,Decimal("0.25"))
    q3=type7_quantile(items,Decimal("0.75"))
    assert q1 is not None and q3 is not None
    iqr=q3-q1
    lower=q1-Decimal("1.5")*iqr
    upper=q3+Decimal("1.5")*iqr
    if nonnegative and lower < 0:
        lower=Decimal("0")
    if bounded_rate:
        lower=max(Decimal("0"),lower)
        upper=min(Decimal("1"),upper)
    if direction=="LOWER":
        upper=None
    elif direction=="UPPER":
        lower=None
    elif direction!="TWO_SIDED":
        raise MetricsError(f"Unknown fence direction: {direction}")
    return {
        "status":"VALID",
        "n":len(items),
        "lower":lower,
        "upper":upper,
        "q1":q1,
        "q3":q3,
        "iqr":iqr,
    }


def _regime_episodes(regimes: Sequence[str]) -> list[tuple[str,int,int,bool]]:
    """(regime,start,end_exclusive,completed_inside_island)."""
    if not regimes:
        return []
    out=[]
    start=0
    current=regimes[0]
    for i in range(1,len(regimes)):
        if regimes[i]!=current:
            out.append((current,start,i,True))
            start=i
            current=regimes[i]
    out.append((current,start,len(regimes),False))
    return out


def _single_island_metrics(island: dict) -> dict:
    bars=int(island["bar_count"])
    swings=island.get("swings",[])
    delays=[int(s["confirmation_index"])-int(s["extremum_index"]) for s in swings]
    regimes=list(island.get("regime_by_bar",[]))
    changes=list(island.get("regime_changes",[]))
    cycles=list(island.get("cycles",[]))
    protected=list(island.get("protected_swings",[]))
    events=list(island.get("events",[]))

    if len(regimes)!=bars:
        raise MetricsError("Regime timeline length does not equal island bar count.")

    direct_flips=sum(
        1 for x in changes
        if (x["previous_regime"],x["new_regime"]) in {
            ("TREND_UP","TREND_DOWN"),("TREND_DOWN","TREND_UP")
        }
    )

    episodes=_regime_episodes(regimes)
    completed_non_ind=[e for e in episodes if e[0]!="INDETERMINATE" and e[3]]
    short_lived=0
    for _,start,end,_ in completed_non_ind:
        subsequent_cycles=sum(
            1 for cy in cycles
            if int(cy["confirmation_index"]) > start
            and int(cy["confirmation_index"]) < end
        )
        if subsequent_cycles==0:
            short_lived += 1

    trend_bars=sum(r in {"TREND_UP","TREND_DOWN"} for r in regimes)
    promotions=[x for x in protected if str(x["action"]).startswith("PROMOTE:")]

    missing_protected_num=0
    missing_protected_den=0
    no_promotion_episodes=0
    actions_by_bar: dict[int,list[dict]]={}
    for x in protected:
        actions_by_bar.setdefault(int(x["bar_index"]),[]).append(x)

    for regime,start,end,_ in episodes:
        if regime not in {"TREND_UP","TREND_DOWN"}:
            continue
        first_promotion=next(
            (
                int(x["bar_index"])
                for x in promotions
                if start <= int(x["bar_index"]) < end
            ),
            None,
        )
        if first_promotion is None:
            no_promotion_episodes += 1
            continue
        active=False
        for bar in range(first_promotion,end):
            for action in actions_by_bar.get(bar,[]):
                if str(action["action"]).startswith("PROMOTE:"):
                    active=True
                elif str(action["action"]).startswith("CLEAR:"):
                    active=False
            missing_protected_den += 1
            if not active:
                missing_protected_num += 1

    event_counts=Counter(str(e["event_type"]) for e in events)
    return {
        "bars":bars,
        "swing_count":len(swings),
        "delays":delays,
        "regime_change_count":len(changes),
        "transition_bars":sum(r=="TRANSITION" for r in regimes),
        "indeterminate_bars":sum(r=="INDETERMINATE" for r in regimes),
        "direct_trend_flips":direct_flips,
        "completed_regime_episodes":len(completed_non_ind),
        "short_lived_regime_episodes":short_lived,
        "trend_bars":trend_bars,
        "protected_promotions":len(promotions),
        "missing_protected_num":missing_protected_num,
        "missing_protected_den":missing_protected_den,
        "no_protected_promotion_episodes":no_promotion_episodes,
        "event_counts":event_counts,
    }


def single_profile_cell_metrics(run: dict) -> dict:
    parts=[_single_island_metrics(x) for x in run.get("islands",[])]
    bars=sum(x["bars"] for x in parts)
    if bars<=0:
        raise MetricsError("Profile cell has no evaluable bars.")
    delays=[v for x in parts for v in x["delays"]]
    event_counts=Counter()
    for x in parts:
        event_counts.update(x["event_counts"])
    trend_bars=sum(x["trend_bars"] for x in parts)
    protected_promotions=sum(x["protected_promotions"] for x in parts)
    missing_num=sum(x["missing_protected_num"] for x in parts)
    missing_den=sum(x["missing_protected_den"] for x in parts)
    completed_episodes=sum(x["completed_regime_episodes"] for x in parts)
    short_lived=sum(x["short_lived_regime_episodes"] for x in parts)

    return {
        "EvaluableBars":bars,
        "SwingCount":sum(x["swing_count"] for x in parts),
        "SwingDensity":Decimal(1000)*Decimal(sum(x["swing_count"] for x in parts))/Decimal(bars),
        "ConfirmationDelayMedian":median(delays),
        "ConfirmationDelayP90":p90(delays),
        "RegimeChurn":Decimal(1000)*Decimal(sum(x["regime_change_count"] for x in parts))/Decimal(bars),
        "ShortLivedRegimeRate":(
            None if completed_episodes==0
            else Decimal(short_lived)/Decimal(completed_episodes)
        ),
        "TransitionUtilization":Decimal(sum(x["transition_bars"] for x in parts))/Decimal(bars),
        "IndeterminateRate":Decimal(sum(x["indeterminate_bars"] for x in parts))/Decimal(bars),
        "DirectTrendFlipCount":sum(x["direct_trend_flips"] for x in parts),
        "ProtectedTurnover":(
            None if trend_bars==0
            else Decimal(1000)*Decimal(protected_promotions)/Decimal(trend_bars)
        ),
        "MissingProtectedRate":(
            None if missing_den==0
            else Decimal(missing_num)/Decimal(missing_den)
        ),
        "NoProtectedPromotionEpisodes":sum(x["no_protected_promotion_episodes"] for x in parts),
        "EventDensity":{
            event_type:Decimal(1000)*Decimal(count)/Decimal(bars)
            for event_type,count in sorted(event_counts.items())
        },
    }


def _objects(island: dict):
    swings=tuple(Swing(**x) for x in island.get("swings",[]))
    events=tuple(StructuralEvent(**x) for x in island.get("events",[]))
    protected=tuple(ProtectedSwingSnapshot(**x) for x in island.get("protected_swings",[]))
    return swings,events,protected


def _eligible_event_tokens(events: Sequence[StructuralEvent], candles: Sequence[dict]) -> list[tuple[str,str]]:
    atr14=wilder_atr(candles,14)
    out=[]
    for e in events:
        idx=int(e.bar_index)
        if 0 <= idx < len(atr14) and atr14[idx] is not None and atr14[idx] > 0:
            out.append((e.event_type,e.reference_kind))
    return out


def _lcs_length(a: Sequence[tuple[str,str]],b: Sequence[tuple[str,str]]) -> int:
    prev=[0]*(len(b)+1)
    for x in a:
        cur=[0]
        for j,y in enumerate(b,1):
            cur.append(prev[j-1]+1 if x==y else max(prev[j],cur[-1]))
        prev=cur
    return prev[-1]


def pairwise_cell_metrics(
    run_a: dict,
    run_b: dict,
    analytical_records: Sequence[dict],
    *,
    timeframe: str,
) -> dict:
    records_by_island: dict[str,list[dict]]={}
    for r in analytical_records:
        records_by_island.setdefault(str(r["analysis_island_id"]),[]).append(dict(r))
    islands_a={x["analysis_island_id"]:x for x in run_a.get("islands",[])}
    islands_b={x["analysis_island_id"]:x for x in run_b.get("islands",[])}
    if set(islands_a)!=set(islands_b) or set(islands_a)!=set(records_by_island):
        raise MetricsError("Pairwise cell Analysis Island sets do not match.")

    totals={
        "strict_m":0,"strict_a":0,"strict_b":0,
        "base_m":0,"base_a":0,"base_b":0,
        "wide_m":0,"wide_a":0,"wide_b":0,
        "base_unmatched_a":0,"base_unmatched_b":0,
        "protected_m":0,"protected_a":0,"protected_b":0,
        "event_m":0,"event_a":0,"event_b":0,
        "event_lcs":0,"event_max":0,
    }
    event_delays=[]

    for island_id in sorted(islands_a):
        candles=records_by_island[island_id]
        swings_a,events_a,protected_a=_objects(islands_a[island_id])
        swings_b,events_b,protected_b=_objects(islands_b[island_id])

        match_by_mode={}
        for mode,prefix in (("STRICT","strict"),("BASE","base"),("WIDE","wide")):
            match=match_swings(swings_a,swings_b,candles,timeframe=timeframe,mode=mode)
            match_by_mode[mode]=match
            totals[f"{prefix}_m"] += match.match_count
            totals[f"{prefix}_a"] += match.eligible_count_a
            totals[f"{prefix}_b"] += match.eligible_count_b
        base=match_by_mode["BASE"]
        totals["base_unmatched_a"] += len(base.unmatched_a)
        totals["base_unmatched_b"] += len(base.unmatched_b)

        pm=match_protected_promotions(
            protected_a,protected_b,base,timeframe=timeframe
        )
        totals["protected_m"] += pm.match_count
        totals["protected_a"] += pm.eligible_count_a
        totals["protected_b"] += pm.eligible_count_b

        em=match_events(events_a,events_b,candles,timeframe=timeframe)
        totals["event_m"] += em.match_count
        totals["event_a"] += em.eligible_count_a
        totals["event_b"] += em.eligible_count_b
        event_delays.extend(p.bar_distance for p in em.matched_pairs)

        tokens_a=_eligible_event_tokens(events_a,candles)
        tokens_b=_eligible_event_tokens(events_b,candles)
        totals["event_lcs"] += _lcs_length(tokens_a,tokens_b)
        totals["event_max"] += max(len(tokens_a),len(tokens_b))

    def dice(prefix: str, empty_value):
        den=totals[f"{prefix}_a"]+totals[f"{prefix}_b"]
        return empty_value if den==0 else Decimal(2*totals[f"{prefix}_m"])/Decimal(den)

    strict=dice("strict",Decimal("1"))
    base=dice("base",Decimal("1"))
    wide=dice("wide",Decimal("1"))
    protected=dice("protected",None)
    event=dice("event",None)

    ma=single_profile_cell_metrics(run_a)
    mb=single_profile_cell_metrics(run_b)
    density_a=ma["SwingDensity"]
    density_b=mb["SwingDensity"]
    fragmentation=None
    omission=None
    if density_a > density_b:
        fragmentation=(
            None if totals["base_a"]==0
            else Decimal(totals["base_unmatched_a"])/Decimal(totals["base_a"])
        )
        omission=(
            None if totals["base_b"]==0
            else Decimal(totals["base_unmatched_b"])/Decimal(totals["base_b"])
        )
    elif density_b > density_a:
        fragmentation=(
            None if totals["base_b"]==0
            else Decimal(totals["base_unmatched_b"])/Decimal(totals["base_b"])
        )
        omission=(
            None if totals["base_a"]==0
            else Decimal(totals["base_unmatched_a"])/Decimal(totals["base_a"])
        )

    return {
        "SwingStability_STRICT":strict,
        "SwingStability_BASE":base,
        "SwingStability_WIDE":wide,
        "FragmentationIndicator":fragmentation,
        "OmissionIndicator":omission,
        "ProtectedSwingStability":protected,
        "EventStability":event,
        "EventDelayMedian":median(event_delays),
        "EventDelayP90":p90(event_delays),
        "EventOrderConsistency":(
            None if totals["event_max"]==0
            else Decimal(totals["event_lcs"])/Decimal(totals["event_max"])
        ),
        "eligible_counts":{
            "swing_a":totals["base_a"],
            "swing_b":totals["base_b"],
            "protected_a":totals["protected_a"],
            "protected_b":totals["protected_b"],
            "event_a":totals["event_a"],
            "event_b":totals["event_b"],
        },
    }


PLATEAU_COMPONENTS=(
    "SwingDisagreement",
    "ProtectedDisagreement",
    "EventDisagreement",
    "RegimeChurnDelta",
    "ConfirmationDelayDelta",
)


def plateau_components(
    single_a: Mapping[str,object],
    single_b: Mapping[str,object],
    pair: Mapping[str,object],
) -> dict[str,Decimal | None]:
    swing=pair.get("SwingStability_BASE")
    protected=pair.get("ProtectedSwingStability")
    event=pair.get("EventStability")
    delay_a=single_a.get("ConfirmationDelayMedian")
    delay_b=single_b.get("ConfirmationDelayMedian")
    return {
        "SwingDisagreement":None if swing is None else Decimal("1")-_d(swing),
        "ProtectedDisagreement":None if protected is None else Decimal("1")-_d(protected),
        "EventDisagreement":None if event is None else Decimal("1")-_d(event),
        "RegimeChurnDelta":abs(_d(single_a["RegimeChurn"])-_d(single_b["RegimeChurn"])),
        "ConfirmationDelayDelta":(
            None if delay_a is None or delay_b is None
            else abs(_d(delay_a)-_d(delay_b))
        ),
    }


@dataclass(frozen=True)
class PlateauResult:
    stable_edges: tuple[tuple[str,str], ...]
    plateaus: tuple[tuple[str,...], ...]
    component_fences: dict


def build_plateau_graph(
    profiles: Sequence[P1Profile],
    *,
    single_metrics: Mapping[str,Mapping[str,Mapping[str,object]]],
    pair_metrics: Mapping[tuple[str,str],Mapping[str,Mapping[str,object]]],
    hard_blocked_profiles: set[str] | None=None,
) -> PlateauResult:
    blocked=set() if hard_blocked_profiles is None else set(hard_blocked_profiles)
    edges=adjacency_edges(profiles)
    edge_values: dict[tuple[str,str],dict[str,Decimal | None]]={}
    component_samples={name:[] for name in PLATEAU_COMPONENTS}

    for edge in edges:
        a,b=edge
        cells=sorted(set(single_metrics[a]) & set(single_metrics[b]) & set(pair_metrics[edge]))
        per_component={name:[] for name in PLATEAU_COMPONENTS}
        for cell in cells:
            values=plateau_components(
                single_metrics[a][cell],single_metrics[b][cell],pair_metrics[edge][cell]
            )
            for name,value in values.items():
                if value is not None:
                    per_component[name].append(value)
        medians={name:median(values) for name,values in per_component.items()}
        edge_values[edge]=medians
        for name,value in medians.items():
            if value is not None:
                component_samples[name].append(value)

    fences={}
    for name,values in component_samples.items():
        fences[name]=robust_fence(values,direction="UPPER",nonnegative=True)

    stable=[]
    for edge,values in edge_values.items():
        if edge[0] in blocked or edge[1] in blocked:
            continue
        okay=True
        for name,value in values.items():
            fence=fences[name]
            if value is None or fence["status"]!="VALID":
                continue
            if value > fence["upper"]:
                okay=False
                break
        if okay:
            stable.append(edge)

    graph: dict[str,set[str]]={}
    for a,b in stable:
        graph.setdefault(a,set()).add(b)
        graph.setdefault(b,set()).add(a)
    visited=set()
    components=[]
    for node in sorted(graph):
        if node in visited:
            continue
        stack=[node]
        comp=set()
        while stack:
            x=stack.pop()
            if x in visited:
                continue
            visited.add(x)
            comp.add(x)
            stack.extend(sorted(graph.get(x,set())-visited,reverse=True))
        if len(comp)>=3:
            components.append(tuple(sorted(comp)))

    return PlateauResult(
        stable_edges=tuple(sorted(stable)),
        plateaus=tuple(sorted(components)),
        component_fences=fences,
    )


def select_behavioral_representatives(
    plateau_result: PlateauResult,
    *,
    single_metrics: Mapping[str,Mapping[str,Mapping[str,object]]],
) -> dict[str,dict]:
    eligible=sorted({pid for plateau in plateau_result.plateaus for pid in plateau})
    if not eligible:
        return {}

    densities={}
    memberships={}
    for pid in eligible:
        vals=[
            _d(metrics["SwingDensity"])
            for metrics in single_metrics[pid].values()
            if metrics.get("SwingDensity") is not None
        ]
        density=median(vals)
        if density is None:
            raise MetricsError(f"Missing DEV Swing Density for {pid}")
        densities[pid]=density
        memberships[pid]=[
            i for i,p in enumerate(plateau_result.plateaus,1) if pid in p
        ]

    unique=sorted(set(densities.values()))
    result={}
    if len(unique)==1:
        pid=min(eligible)
        result["Balanced"]={
            "profile_id":pid,
            "pooled_dev_swing_density":densities[pid],
            "plateau_membership":memberships[pid],
        }
        return result

    min_density=min(unique)
    max_density=max(unique)
    conservative=min(pid for pid in eligible if densities[pid]==min_density)
    responsive=min(pid for pid in eligible if densities[pid]==max_density)
    result["Conservative"]={
        "profile_id":conservative,
        "pooled_dev_swing_density":densities[conservative],
        "plateau_membership":memberships[conservative],
    }
    result["Responsive"]={
        "profile_id":responsive,
        "pooled_dev_swing_density":densities[responsive],
        "plateau_membership":memberships[responsive],
    }

    middle=[pid for pid in eligible if min_density < densities[pid] < max_density]
    if middle:
        target=median(list(densities.values()))
        assert target is not None
        balanced=min(
            middle,
            key=lambda pid:(abs(densities[pid]-target),pid),
        )
        result["Balanced"]={
            "profile_id":balanced,
            "pooled_dev_swing_density":densities[balanced],
            "plateau_membership":memberships[balanced],
        }
    return result


SINGLE_REFERENCE_DIRECTIONS={
    "SwingDensity":"TWO_SIDED",
    "ConfirmationDelayMedian":"UPPER",
    "ConfirmationDelayP90":"UPPER",
    "RegimeChurn":"UPPER",
    "ShortLivedRegimeRate":"UPPER",
    "TransitionUtilization":"TWO_SIDED",
    "IndeterminateRate":"UPPER",
    "ProtectedTurnover":"TWO_SIDED",
    "MissingProtectedRate":"UPPER",
}

PAIR_REFERENCE_DIRECTIONS={
    "SwingStability_BASE":"LOWER",
    "ProtectedSwingStability":"LOWER",
    "EventStability":"LOWER",
    "EventOrderConsistency":"LOWER",
    "FragmentationIndicator":"UPPER",
    "OmissionIndicator":"UPPER",
}


def freeze_single_reference_bands(cell_metrics: Mapping[str,Mapping[str,object]]) -> dict:
    bands={}
    for metric,direction in SINGLE_REFERENCE_DIRECTIONS.items():
        values=[
            v[metric] for v in cell_metrics.values()
            if v.get(metric) is not None
        ]
        bounded=metric in {
            "ShortLivedRegimeRate","TransitionUtilization",
            "IndeterminateRate","MissingProtectedRate",
        }
        bands[metric]=robust_fence(
            values,direction=direction,bounded_rate=bounded,nonnegative=True
        )

    event_types=sorted({
        event_type
        for v in cell_metrics.values()
        for event_type in v.get("EventDensity",{})
    })
    bands["EventDensity"]={}
    for event_type in event_types:
        values=[
            v.get("EventDensity",{}).get(event_type,Decimal("0"))
            for v in cell_metrics.values()
        ]
        bands["EventDensity"][event_type]=robust_fence(
            values,direction="TWO_SIDED",nonnegative=True
        )
    return bands


def freeze_pair_reference_bands(cell_metrics: Mapping[str,Mapping[str,object]]) -> dict:
    bands={}
    for metric,direction in PAIR_REFERENCE_DIRECTIONS.items():
        values=[
            v[metric] for v in cell_metrics.values()
            if v.get(metric) is not None
        ]
        bounded=metric in {
            "SwingStability_BASE","ProtectedSwingStability",
            "EventStability","EventOrderConsistency",
            "FragmentationIndicator","OmissionIndicator",
        }
        bands[metric]=robust_fence(
            values,direction=direction,bounded_rate=bounded,nonnegative=True
        )
    return bands
