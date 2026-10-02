#!/usr/bin/env python3
"""Regression checks for the ASSET-P0-001 causal replay harness.

These checks validate implementation behavior against frozen fixtures.
They are not the formal P0 execution.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from replay import (
    CausalReplay,
    ReplayError,
    canonical_json_bytes,
    combine_streams,
    read_jsonl,
    sha256_bytes,
)


def apply_batch(state: dict, batch) -> dict:
    state = copy.deepcopy(state)
    state.setdefault("counts", {})
    state.setdefault("last_close", {})
    state.setdefault("seen_timestamps", [])
    state["seen_timestamps"].append(batch.replay_timestamp_us)
    for record in batch.records:
        tf = record["timeframe"]
        state["counts"][tf] = state["counts"].get(tf, 0) + 1
        state["last_close"][tf] = record["close"]
        if int(record["interval_end_us"]) > batch.replay_timestamp_us:
            raise ReplayError("Future candle access detected.")
    return state


def run_continuous(records: list[dict]) -> tuple[str, dict, list[dict]]:
    replay = CausalReplay(records)
    state: dict = {}
    trace: list[dict] = []
    while True:
        batch = replay.next_batch()
        if batch is None:
            break
        state = apply_batch(state, batch)
        trace.append(
            {
                "records": list(batch.records),
                "replay_timestamp_us": batch.replay_timestamp_us,
                "state": copy.deepcopy(state),
            }
        )
    return (
        sha256_bytes(b"".join(canonical_json_bytes(x) for x in trace)),
        state,
        trace,
    )


def run_restart(
    records: list[dict],
    checkpoint_ts: int,
) -> tuple[str, dict, list[dict]]:
    replay = CausalReplay(records)
    state: dict = {}
    trace: list[dict] = []
    checkpoint = None

    while True:
        batch = replay.next_batch()
        if batch is None:
            break
        state = apply_batch(state, batch)
        trace.append(
            {
                "records": list(batch.records),
                "replay_timestamp_us": batch.replay_timestamp_us,
                "state": copy.deepcopy(state),
            }
        )
        if batch.replay_timestamp_us == checkpoint_ts:
            checkpoint = replay.checkpoint(state)
            break

    if checkpoint is None:
        raise ReplayError("Requested checkpoint timestamp was not reached.")

    restarted = CausalReplay(records)
    state = restarted.restore(checkpoint)

    while True:
        batch = restarted.next_batch()
        if batch is None:
            break
        state = apply_batch(state, batch)
        trace.append(
            {
                "records": list(batch.records),
                "replay_timestamp_us": batch.replay_timestamp_us,
                "state": copy.deepcopy(state),
            }
        )

    return (
        sha256_bytes(b"".join(canonical_json_bytes(x) for x in trace)),
        state,
        trace,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture-root", type=Path, required=True)
    args = parser.parse_args()

    native = read_jsonl(args.fixture_root / "native.jsonl")
    d4 = read_jsonl(args.fixture_root / "derived_4h.jsonl")
    d1 = read_jsonl(args.fixture_root / "derived_1d.jsonl")
    expected = json.loads(
        (args.fixture_root / "expected.json").read_text(encoding="utf-8")
    )

    records = combine_streams(native, d4, d1)

    hash_a, state_a, trace_a = run_continuous(records)
    hash_b, state_b, _ = run_continuous(records)
    hash_c, state_c, _ = run_restart(
        records,
        int(expected["checkpoint_after_batch_timestamp_us"]),
    )

    if not (hash_a == hash_b == hash_c):
        raise ReplayError(
            f"Determinism mismatch: A={hash_a}, B={hash_b}, C={hash_c}"
        )
    if not (state_a == state_b == state_c):
        raise ReplayError("Final replay state mismatch.")

    incomplete_keys = {
        ("4h", int(x)) for x in expected["incomplete_4h_open_times_us"]
    } | {
        ("1d", int(x)) for x in expected["incomplete_1d_open_times_us"]
    }
    for item in trace_a:
        for record in item["records"]:
            key = (record["timeframe"], int(record["open_time_us"]))
            if key in incomplete_keys:
                raise ReplayError(
                    f"Incomplete derived candle leaked into replay: {key}"
                )

    result = {
        "continuous_hash_a": hash_a,
        "continuous_hash_b": hash_b,
        "dataset_records_input": len(records),
        "final_counts": state_a["counts"],
        "last_replay_timestamp_us": state_a["seen_timestamps"][-1],
        "restart_hash_c": hash_c,
        "status": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
