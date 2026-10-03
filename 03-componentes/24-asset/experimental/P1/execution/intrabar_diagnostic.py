#!/usr/bin/env python3
"""Formal DEV diagnostic-only M3 intrabar comparison for ASSET-P1-D1-001."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from d1_runner import split_analysis_islands
from d1_swings import (
    assert_swing_invariants,
    volatility_normalized_reversal,
    volatility_normalized_reversal_intrabar,
)

ASSETS=("BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT")
SEGMENTS=("DEV-01","DEV-02")
TIMEFRAMES=("4h","1d")
ESTIMATORS=("WILDER_ATR","MEDIAN_TR")
MULTIPLIERS=("1.5","2.0","3.0")


def canonical_bytes(obj):
    return (
        json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"))
        +"\n"
    ).encode("utf-8")


def sha256_obj(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def read_jsonl(path: Path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def analytical_path(root: Path, segment: str, asset: str, timeframe: str) -> Path:
    suffix="analytical_4h.jsonl" if timeframe=="4h" else "analytical_1d.jsonl"
    return root/"dev"/segment/asset/suffix


def main() -> int:
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--data-root",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()

    root=Path(args.data_root)
    results=[]

    for timeframe in TIMEFRAMES:
        for estimator in ESTIMATORS:
            for k in MULTIPLIERS:
                summary={
                    "timeframe":timeframe,
                    "estimator":estimator,
                    "window":14,
                    "multiplier":k,
                    "cells":[],
                    "close_swings_total":0,
                    "intrabar_swings_total":0,
                    "ambiguous_bootstrap_total":0,
                    "ambiguous_intrabar_sequence_total":0,
                }

                for asset in ASSETS:
                    for segment in SEGMENTS:
                        records=read_jsonl(analytical_path(root,segment,asset,timeframe))
                        cell={
                            "asset":asset,
                            "segment":segment,
                            "analysis_islands":0,
                            "close_swings":0,
                            "intrabar_swings":0,
                            "ambiguous_bootstrap":0,
                            "ambiguous_intrabar_sequence":0,
                        }
                        for _,candles in split_analysis_islands(records):
                            cell["analysis_islands"] += 1
                            close=volatility_normalized_reversal(
                                candles,
                                estimator=estimator,
                                window=14,
                                multiplier=k,
                            )
                            intra=volatility_normalized_reversal_intrabar(
                                candles,
                                estimator=estimator,
                                window=14,
                                multiplier=k,
                            )
                            assert_swing_invariants(close.swings)
                            assert_swing_invariants(intra.swings)
                            cell["close_swings"] += len(close.swings)
                            cell["intrabar_swings"] += len(intra.swings)
                            for anomaly in intra.anomalies:
                                t=str(anomaly.get("type"))
                                if t=="AMBIGUOUS_BOOTSTRAP":
                                    cell["ambiguous_bootstrap"] += 1
                                elif t=="AMBIGUOUS_INTRABAR_SEQUENCE":
                                    cell["ambiguous_intrabar_sequence"] += 1

                        for key in (
                            "close_swings",
                            "intrabar_swings",
                            "ambiguous_bootstrap",
                            "ambiguous_intrabar_sequence",
                        ):
                            total_key = key + "_total"
                            summary[total_key] += cell[key]
                        summary["cells"].append(cell)

                close_total=summary["close_swings_total"]
                intra_total=summary["intrabar_swings_total"]
                summary["intrabar_to_close_ratio"]=(
                    None if close_total==0 else str(intra_total/close_total)
                )
                results.append(summary)

    result={
        "experiment_id":"ASSET-P1-D1-001",
        "phase":"DEV",
        "diagnostic":"M3_INTRABAR",
        "candidate_eligibility":"DIAGNOSTIC_ONLY",
        "results":results,
    }
    result["result_sha256"]=sha256_obj(result)
    Path(args.output).write_bytes(canonical_bytes(result))
    print(json.dumps({
        "result_sha256":result["result_sha256"],
        "rows":[
            {
                "timeframe":r["timeframe"],
                "estimator":r["estimator"],
                "k":r["multiplier"],
                "close_swings":r["close_swings_total"],
                "intrabar_swings":r["intrabar_swings_total"],
                "ratio":r["intrabar_to_close_ratio"],
                "ambiguous_bootstrap":r["ambiguous_bootstrap_total"],
                "ambiguous_intrabar_sequence":r["ambiguous_intrabar_sequence_total"],
            }
            for r in results
        ],
    },indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
