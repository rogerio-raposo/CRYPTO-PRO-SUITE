#!/usr/bin/env python3
"""ASSET-P1-D1-001 phase-lock and Holdout access control."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


EXPERIMENT_ID = "ASSET-P1-D1-001"


class PhaseAccessError(RuntimeError):
    pass


def canonical_bytes(obj: dict) -> bytes:
    return (
        json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def payload_sha256(obj: dict) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


@dataclass(frozen=True)
class PhaseLock:
    experiment_id: str
    lock_type: str
    candidates: tuple[str, ...]
    prior_lock_sha256: str | None
    metrics_reference_sha256: str
    created_from_phase: str
    payload_sha256: str


def build_lock(
    *,
    lock_type: str,
    candidates: list[str],
    metrics_reference_sha256: str,
    prior_lock_sha256: str | None = None,
) -> dict:
    if lock_type not in {"DEV_CANDIDATE_LOCK", "VAL_PROVISIONAL_LOCK"}:
        raise PhaseAccessError(f"Unsupported lock_type: {lock_type}")
    if not candidates:
        raise PhaseAccessError("Candidate lock cannot be empty.")
    created_from = "DEV" if lock_type == "DEV_CANDIDATE_LOCK" else "VAL"
    body = {
        "experiment_id": EXPERIMENT_ID,
        "lock_type": lock_type,
        "candidates": sorted(set(candidates)),
        "prior_lock_sha256": prior_lock_sha256,
        "metrics_reference_sha256": metrics_reference_sha256,
        "created_from_phase": created_from,
    }
    body["payload_sha256"] = payload_sha256(body)
    return body


def validate_lock(lock: dict, expected_type: str) -> PhaseLock:
    if lock.get("experiment_id") != EXPERIMENT_ID:
        raise PhaseAccessError("Lock experiment identity mismatch.")
    if lock.get("lock_type") != expected_type:
        raise PhaseAccessError(
            f"Expected {expected_type}, got {lock.get('lock_type')}"
        )
    supplied = lock.get("payload_sha256")
    body = {k: v for k, v in lock.items() if k != "payload_sha256"}
    actual = payload_sha256(body)
    if supplied != actual:
        raise PhaseAccessError("Lock payload hash mismatch.")
    candidates = tuple(lock.get("candidates") or ())
    if not candidates:
        raise PhaseAccessError("Lock has no candidates.")
    metrics_sha = str(lock.get("metrics_reference_sha256") or "")
    if len(metrics_sha) != 64:
        raise PhaseAccessError("Invalid metrics reference hash.")
    if expected_type == "VAL_PROVISIONAL_LOCK":
        prior = lock.get("prior_lock_sha256")
        if not isinstance(prior, str) or len(prior) != 64:
            raise PhaseAccessError("VAL lock must reference DEV lock hash.")
    return PhaseLock(
        experiment_id=EXPERIMENT_ID,
        lock_type=expected_type,
        candidates=candidates,
        prior_lock_sha256=lock.get("prior_lock_sha256"),
        metrics_reference_sha256=metrics_sha,
        created_from_phase=str(lock.get("created_from_phase")),
        payload_sha256=supplied,
    )


def read_lock(path: Path, expected_type: str) -> PhaseLock:
    if not path.exists():
        raise PhaseAccessError(f"Required lock missing: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise PhaseAccessError("Lock document must be a JSON object.")
    return validate_lock(value, expected_type)


def authorize_phase(
    phase: str,
    *,
    dev_lock_path: Path | None = None,
    val_lock_path: Path | None = None,
) -> tuple[str, ...] | None:
    phase = phase.upper()
    if phase == "DEV":
        return None
    if phase == "VAL":
        if dev_lock_path is None:
            raise PhaseAccessError("VAL requires DEV candidate lock.")
        return read_lock(dev_lock_path, "DEV_CANDIDATE_LOCK").candidates
    if phase == "HOLDOUT":
        if dev_lock_path is None or val_lock_path is None:
            raise PhaseAccessError("HOLDOUT requires DEV and VAL locks.")
        dev = read_lock(dev_lock_path, "DEV_CANDIDATE_LOCK")
        val = read_lock(val_lock_path, "VAL_PROVISIONAL_LOCK")
        if val.prior_lock_sha256 != dev.payload_sha256:
            raise PhaseAccessError("VAL lock does not chain to supplied DEV lock.")
        if not set(val.candidates).issubset(set(dev.candidates)):
            raise PhaseAccessError("VAL lock introduces candidates absent from DEV lock.")
        return val.candidates
    raise PhaseAccessError(f"Unsupported phase: {phase}")
