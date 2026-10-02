#!/usr/bin/env python3
"""ASSET-P0-001 causal replay harness.

Experimental / non-normative. Contains no technical-analysis logic.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

TIMEFRAME_ORDER = {"1h": 0, "4h": 1, "1d": 2}


class ReplayError(RuntimeError):
    """Raised when causal replay invariants are violated."""


def canonical_json_bytes(obj: object) -> bytes:
    return (
        json.dumps(
            obj,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ReplayError(f"{path}:{line_number} is not a JSON object.")
        records.append(value)
    return records


def record_sort_key(record: dict) -> tuple:
    timeframe = str(record.get("timeframe", ""))
    return (
        int(record["interval_end_us"]),
        TIMEFRAME_ORDER.get(timeframe, 99),
        str(record.get("instrument", "")),
        int(record["open_time_us"]),
    )


def is_replay_eligible(record: dict) -> bool:
    if record.get("data_origin") == "DERIVED" and record.get("complete") is not True:
        return False
    return True


def dataset_digest(records: Sequence[dict]) -> str:
    ordered = sorted((r for r in records if is_replay_eligible(r)), key=record_sort_key)
    return sha256_bytes(b"".join(canonical_json_bytes(r) for r in ordered))


@dataclass(frozen=True)
class ReplayBatch:
    replay_timestamp_us: int
    records: tuple[dict, ...]


class CausalReplay:
    def __init__(self, records: Sequence[dict]):
        eligible = sorted(
            (copy.deepcopy(r) for r in records if is_replay_eligible(r)),
            key=record_sort_key,
        )
        self.dataset_digest = dataset_digest(eligible)
        self._batches: list[ReplayBatch] = []
        self._next_batch_index = 0
        self.replay_timestamp_us: int | None = None

        current_ts: int | None = None
        bucket: list[dict] = []
        for record in eligible:
            end_us = int(record["interval_end_us"])
            open_us = int(record["open_time_us"])
            if end_us <= open_us:
                raise ReplayError("Record interval_end_us must be after open_time_us.")
            if current_ts is None:
                current_ts = end_us
            if end_us != current_ts:
                self._batches.append(
                    ReplayBatch(current_ts, tuple(copy.deepcopy(bucket)))
                )
                current_ts = end_us
                bucket = []
            bucket.append(record)
        if current_ts is not None:
            self._batches.append(ReplayBatch(current_ts, tuple(copy.deepcopy(bucket))))

    @property
    def exhausted(self) -> bool:
        return self._next_batch_index >= len(self._batches)

    @property
    def next_batch_index(self) -> int:
        return self._next_batch_index

    def next_batch(self) -> ReplayBatch | None:
        if self.exhausted:
            return None
        batch = self._batches[self._next_batch_index]
        if self.replay_timestamp_us is not None:
            if batch.replay_timestamp_us <= self.replay_timestamp_us:
                raise ReplayError("Replay timestamp must advance strictly.")
        for record in batch.records:
            if int(record["interval_end_us"]) > batch.replay_timestamp_us:
                raise ReplayError("Future record leaked into current replay batch.")
        self.replay_timestamp_us = batch.replay_timestamp_us
        self._next_batch_index += 1
        return ReplayBatch(
            batch.replay_timestamp_us,
            tuple(copy.deepcopy(r) for r in batch.records),
        )

    def checkpoint(self, module_state: dict | None = None) -> dict:
        return {
            "dataset_digest": self.dataset_digest,
            "module_state": copy.deepcopy(module_state or {}),
            "next_batch_index": self._next_batch_index,
            "replay_timestamp_us": self.replay_timestamp_us,
            "schema_version": "ASSET-P0-REPLAY-CHECKPOINT-0.1.0",
        }

    def restore(self, checkpoint: dict) -> dict:
        if checkpoint.get("dataset_digest") != self.dataset_digest:
            raise ReplayError("Checkpoint dataset digest mismatch.")
        index = int(checkpoint["next_batch_index"])
        if not 0 <= index <= len(self._batches):
            raise ReplayError("Checkpoint next_batch_index out of range.")
        timestamp = checkpoint.get("replay_timestamp_us")
        if index == 0 and timestamp is not None:
            raise ReplayError("Zero-index checkpoint cannot have a replay timestamp.")
        if index > 0:
            expected_ts = self._batches[index - 1].replay_timestamp_us
            if timestamp != expected_ts:
                raise ReplayError("Checkpoint timestamp does not match replay position.")
        self._next_batch_index = index
        self.replay_timestamp_us = timestamp
        return copy.deepcopy(checkpoint.get("module_state", {}))


def combine_streams(*streams: Iterable[dict]) -> list[dict]:
    combined: list[dict] = []
    for stream in streams:
        combined.extend(copy.deepcopy(list(stream)))
    return combined
