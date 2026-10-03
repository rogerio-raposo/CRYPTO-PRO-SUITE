#!/usr/bin/env python3
"""Island-aware single-profile runner for ASSET-P1-D1-001.

This module is implementation infrastructure only. It does not select profiles,
open Holdout, or execute the formal P1 phase protocol.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from decimal import Decimal
from typing import Sequence

from d1_structure import build_structure
from d1_swings import (
    D1Error,
    assert_swing_invariants,
    fixed_percentage_reversal,
    fixed_window_pivots,
    volatility_normalized_reversal,
    volatility_normalized_reversal_intrabar,
)


class RunnerError(RuntimeError):
    pass


def _canonical_bytes(obj: object) -> bytes:
    return (
        json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
        + "\n"
    ).encode("utf-8")


def _sha256(obj: object) -> str:
    return hashlib.sha256(_canonical_bytes(obj)).hexdigest()


def split_analysis_islands(records: Sequence[dict]) -> list[tuple[str, list[dict]]]:
    if not records:
        return []
    grouped: list[tuple[str, list[dict]]] = []
    current_id: str | None = None
    current: list[dict] = []

    for record in records:
        island_id = record.get("analysis_island_id")
        if not isinstance(island_id, str) or not island_id:
            raise RunnerError("Analytical record is missing analysis_island_id.")
        if current_id is None:
            current_id = island_id
        if island_id != current_id:
            grouped.append((current_id, current))
            current_id = island_id
            current = []
        current.append(dict(record))
    if current_id is not None:
        grouped.append((current_id, current))

    seen: set[str] = set()
    for island_id, candles in grouped:
        if island_id in seen:
            raise RunnerError(f"Analysis Island is non-contiguous: {island_id}")
        seen.add(island_id)
        opens=[int(x["open_time_us"]) for x in candles]
        if opens != sorted(opens):
            raise RunnerError(f"Analysis Island is not chronological: {island_id}")
    return grouped


def _detect(candles: Sequence[dict], detector: dict):
    method = detector.get("method")
    if method == "M1":
        return fixed_window_pivots(candles, int(detector["window"]))
    if method == "M2":
        return fixed_percentage_reversal(candles, Decimal(str(detector["percentage"])))
    if method == "M3":
        return volatility_normalized_reversal(
            candles,
            estimator=str(detector["estimator"]),
            window=int(detector["window"]),
            multiplier=Decimal(str(detector["multiplier"])),
        )
    if method == "M3_INTRABAR":
        return volatility_normalized_reversal_intrabar(
            candles,
            estimator=str(detector["estimator"]),
            window=int(detector["window"]),
            multiplier=Decimal(str(detector["multiplier"])),
        )
    raise RunnerError(f"Unsupported detector method: {method}")


def run_profile(
    analytical_records: Sequence[dict],
    *,
    profile_id: str,
    detector: dict,
    structural: dict,
) -> dict:
    """Run one predeclared profile independently on each Analysis Island."""
    islands=split_analysis_islands(analytical_records)
    outputs: list[dict] = []

    for island_id, candles in islands:
        detection=_detect(candles,detector)
        assert_swing_invariants(detection.swings)
        structure=build_structure(
            candles,
            detection.swings,
            equality_q=Decimal(str(structural["q"])),
            break_b=Decimal(str(structural["b"])),
            trend_m=int(structural["m"]),
        )
        result={
            "analysis_island_id":island_id,
            "bar_count":len(candles),
            "start_open_time_us":int(candles[0]["open_time_us"]),
            "end_interval_end_us":int(candles[-1]["interval_end_us"]),
            "swings":[s.to_dict() for s in detection.swings],
            "detector_anomalies":list(detection.anomalies),
            "relations":[asdict(x) for x in structure.relations],
            "cycles":[asdict(x) for x in structure.cycles],
            "regime_changes":[asdict(x) for x in structure.regime_changes],
            "events":[asdict(x) for x in structure.events],
            "protected_swings":[asdict(x) for x in structure.protected_swings],
            "regime_by_bar":list(structure.regime_by_bar),
            "integrity_by_bar":list(structure.integrity_by_bar),
            "structural_anomalies":list(structure.anomalies),
        }
        result["result_sha256"]=_sha256(result)
        outputs.append(result)

    summary={
        "profile_id":profile_id,
        "detector":dict(detector),
        "structural":dict(structural),
        "analysis_island_count":len(outputs),
        "evaluable_bars":sum(x["bar_count"] for x in outputs),
        "islands":outputs,
    }
    summary["run_sha256"]=_sha256(summary)
    return summary


def assert_no_cross_island_objects(run: dict) -> None:
    for island in run.get("islands", []):
        n=int(island["bar_count"])
        for swing in island.get("swings", []):
            if not (0 <= int(swing["extremum_index"]) < n):
                raise RunnerError("Swing extremum escaped Analysis Island.")
            if not (0 <= int(swing["confirmation_index"]) < n):
                raise RunnerError("Swing confirmation escaped Analysis Island.")
        for event in island.get("events", []):
            if not (0 <= int(event["bar_index"]) < n):
                raise RunnerError("Structural event escaped Analysis Island.")
        for change in island.get("regime_changes", []):
            if not (0 <= int(change["bar_index"]) < n):
                raise RunnerError("Regime change escaped Analysis Island.")
