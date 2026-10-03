#!/usr/bin/env python3
"""Canonical profile registry and adjacency for ASSET-P1-D1-001."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


M1_WINDOWS={
    "4h":("2","3","4","6","8","12"),
    "1d":("2","3","4","5","7","10"),
}
M2_PERCENTAGES={
    "4h":("0.01","0.015","0.025","0.04","0.06","0.09"),
    "1d":("0.02","0.03","0.05","0.08","0.12","0.18"),
}
M3_WINDOWS=("10","14","21","34")
M3_MULTIPLIERS=("1.0","1.5","2.0","2.5","3.0","4.0")
M3_ESTIMATORS=("WILDER_ATR","MEDIAN_TR")
Q_VALUES=("0.25","0.50","0.75")
B_VALUES=("0","0.25","0.50")
M_VALUES=("2","3")


class ProfileError(RuntimeError):
    pass


@dataclass(frozen=True)
class P1Profile:
    method: str
    timeframe: str
    detector: tuple[tuple[str,str], ...]
    structural: tuple[tuple[str,str], ...]
    profile_id: str

    def detector_dict(self) -> dict[str,str]:
        return dict(self.detector)

    def structural_dict(self) -> dict[str,str]:
        return dict(self.structural)

    def axis_values(self) -> tuple[str, ...]:
        d=self.detector_dict()
        s=self.structural_dict()
        if self.method=="M1":
            return (d["window"],s["q"],s["b"],s["m"])
        if self.method=="M2":
            return (d["percentage"],s["q"],s["b"],s["m"])
        if self.method=="M3":
            return (
                d["estimator"],d["window"],d["multiplier"],
                s["q"],s["b"],s["m"],
            )
        raise ProfileError(f"Unsupported method: {self.method}")


def _tf_id(timeframe: str) -> str:
    if timeframe=="4h":
        return "TF4H"
    if timeframe=="1d":
        return "TF1D"
    raise ProfileError(f"Unsupported timeframe: {timeframe}")


def _structural_combinations() -> Iterable[tuple[str,str,str]]:
    for q in Q_VALUES:
        for b in B_VALUES:
            for m in M_VALUES:
                yield q,b,m


def canonical_profile_id(
    method: str,
    timeframe: str,
    detector: dict[str,str],
    structural: dict[str,str],
) -> str:
    tf=_tf_id(timeframe)
    q,b,m=structural["q"],structural["b"],structural["m"]
    if method=="M1":
        return f"M1-{tf}-w{detector['window']}-q{q}-b{b}-m{m}"
    if method=="M2":
        return f"M2-{tf}-p{detector['percentage']}-q{q}-b{b}-m{m}"
    if method=="M3":
        return (
            f"M3-{tf}-{detector['estimator']}-n{detector['window']}-"
            f"k{detector['multiplier']}-q{q}-b{b}-m{m}"
        )
    raise ProfileError(f"Unsupported method: {method}")


def build_profiles(
    method: str,
    timeframe: str,
    *,
    m3_estimators: tuple[str,...]=M3_ESTIMATORS,
) -> tuple[P1Profile,...]:
    profiles: list[P1Profile]=[]
    if method=="M1":
        detector_rows=({"window":w} for w in M1_WINDOWS[timeframe])
    elif method=="M2":
        detector_rows=({"percentage":p} for p in M2_PERCENTAGES[timeframe])
    elif method=="M3":
        detector_rows=(
            {"estimator":est,"window":n,"multiplier":k}
            for est in m3_estimators
            for n in M3_WINDOWS
            for k in M3_MULTIPLIERS
        )
    else:
        raise ProfileError(f"Unsupported method: {method}")

    detector_rows=list(detector_rows)
    for detector in detector_rows:
        for q,b,m in _structural_combinations():
            structural={"q":q,"b":b,"m":m}
            pid=canonical_profile_id(method,timeframe,detector,structural)
            profiles.append(P1Profile(
                method=method,
                timeframe=timeframe,
                detector=tuple(detector.items()),
                structural=tuple(structural.items()),
                profile_id=pid,
            ))
    return tuple(sorted(profiles,key=lambda x:x.profile_id))


def _axis_orders(profile: P1Profile) -> tuple[tuple[str,...], ...]:
    if profile.method=="M1":
        return (M1_WINDOWS[profile.timeframe],Q_VALUES,B_VALUES,M_VALUES)
    if profile.method=="M2":
        return (M2_PERCENTAGES[profile.timeframe],Q_VALUES,B_VALUES,M_VALUES)
    if profile.method=="M3":
        # Estimator is identity, never an adjacency axis.
        return (
            (profile.detector_dict()["estimator"],),
            M3_WINDOWS,M3_MULTIPLIERS,Q_VALUES,B_VALUES,M_VALUES,
        )
    raise ProfileError(f"Unsupported method: {profile.method}")


def are_adjacent(a: P1Profile,b: P1Profile) -> bool:
    if a.method!=b.method or a.timeframe!=b.timeframe:
        return False
    av=a.axis_values()
    bv=b.axis_values()
    if a.method=="M3" and av[0]!=bv[0]:
        return False
    orders=_axis_orders(a)
    changed=0
    for index,(x,y,order) in enumerate(zip(av,bv,orders)):
        if x==y:
            continue
        if a.method=="M3" and index==0:
            return False
        try:
            xi=order.index(x)
            yi=order.index(y)
        except ValueError as exc:
            raise ProfileError("Profile value outside frozen grid.") from exc
        if abs(xi-yi)!=1:
            return False
        changed += 1
        if changed>1:
            return False
    return changed==1


def adjacency_edges(profiles: Iterable[P1Profile]) -> tuple[tuple[str,str], ...]:
    items=sorted(profiles,key=lambda x:x.profile_id)
    edges=[]
    for i,a in enumerate(items):
        for b in items[i+1:]:
            if are_adjacent(a,b):
                edges.append((a.profile_id,b.profile_id))
    return tuple(edges)


def m3_screen_profiles(timeframe: str) -> tuple[dict,...]:
    return tuple(
        {
            "method":"M3",
            "timeframe":timeframe,
            "estimator":est,
            "window":"14",
            "multiplier":"2.0",
            "screen_id":f"M3-SCREEN-{_tf_id(timeframe)}-{est}-n14-k2.0",
        }
        for est in M3_ESTIMATORS
    )
