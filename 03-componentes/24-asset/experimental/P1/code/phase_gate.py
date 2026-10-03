#!/usr/bin/env python3
"""ASSET-P1-D1-001 DEV/VAL/Holdout phase-lock enforcement."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


EXPERIMENT_ID="ASSET-P1-D1-001"
ALLOWED_LABELS={"Responsive","Balanced","Conservative"}


class PhaseAccessError(RuntimeError):
    pass


def canonical_bytes(obj: dict) -> bytes:
    return (
        json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"))
        +"\n"
    ).encode("utf-8")


def payload_sha256(obj: dict) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def _validate_candidate_record(record: dict) -> None:
    required={
        "profile_id","behavioral_label","plateau_membership",
        "pooled_dev_swing_density","single_reference_bands",
    }
    if not required <= set(record):
        raise PhaseAccessError(
            f"Candidate record missing fields: {sorted(required-set(record))}"
        )
    if not isinstance(record["profile_id"],str) or not record["profile_id"]:
        raise PhaseAccessError("Invalid candidate profile_id.")
    if record["behavioral_label"] not in ALLOWED_LABELS:
        raise PhaseAccessError("Invalid behavioral label.")
    if not isinstance(record["plateau_membership"],list) or not record["plateau_membership"]:
        raise PhaseAccessError("Candidate has no qualifying plateau membership.")
    if not isinstance(record["single_reference_bands"],dict):
        raise PhaseAccessError("Candidate single-reference bands must be an object.")


@dataclass(frozen=True)
class PhaseLock:
    experiment_id: str
    lock_type: str
    candidate_ids: tuple[str,...]
    candidate_records: tuple[dict,...]
    pair_reference_bands: dict
    prior_lock_sha256: str | None
    metrics_reference_sha256: str
    human_review_sha256: str
    created_from_phase: str
    payload_sha256: str


def build_lock(
    *,
    lock_type: str,
    candidate_records: Sequence[dict],
    metrics_reference_sha256: str,
    human_review_sha256: str,
    pair_reference_bands: dict | None=None,
    prior_lock_sha256: str | None=None,
) -> dict:
    if lock_type not in {"DEV_CANDIDATE_LOCK","VAL_PROVISIONAL_LOCK"}:
        raise PhaseAccessError(f"Unsupported lock_type: {lock_type}")
    records=[dict(x) for x in candidate_records]
    if not records:
        raise PhaseAccessError("Candidate lock cannot be empty.")
    for record in records:
        _validate_candidate_record(record)

    records=sorted(records,key=lambda x:x["profile_id"])
    ids=[x["profile_id"] for x in records]
    if len(ids)!=len(set(ids)):
        raise PhaseAccessError("Duplicate profile_id in candidate lock.")

    metrics_sha=str(metrics_reference_sha256)
    if len(metrics_sha)!=64:
        raise PhaseAccessError("Invalid metrics reference hash.")
    review_sha=str(human_review_sha256)
    if len(review_sha)!=64:
        raise PhaseAccessError("Invalid Human Review hash.")

    created_from="DEV" if lock_type=="DEV_CANDIDATE_LOCK" else "VAL"
    body={
        "experiment_id":EXPERIMENT_ID,
        "lock_type":lock_type,
        "candidate_records":records,
        "candidate_ids":ids,
        "pair_reference_bands":{} if pair_reference_bands is None else pair_reference_bands,
        "prior_lock_sha256":prior_lock_sha256,
        "metrics_reference_sha256":metrics_sha,
        "human_review_sha256":review_sha,
        "created_from_phase":created_from,
    }
    body["payload_sha256"]=payload_sha256(body)
    return body


def validate_lock(lock: dict,expected_type: str) -> PhaseLock:
    if lock.get("experiment_id")!=EXPERIMENT_ID:
        raise PhaseAccessError("Lock experiment identity mismatch.")
    if lock.get("lock_type")!=expected_type:
        raise PhaseAccessError(
            f"Expected {expected_type}, got {lock.get('lock_type')}"
        )

    supplied=lock.get("payload_sha256")
    body={k:v for k,v in lock.items() if k!="payload_sha256"}
    if supplied!=payload_sha256(body):
        raise PhaseAccessError("Lock payload hash mismatch.")

    records=tuple(lock.get("candidate_records") or ())
    if not records:
        raise PhaseAccessError("Lock has no candidate records.")
    for record in records:
        _validate_candidate_record(record)

    ids=tuple(str(x) for x in (lock.get("candidate_ids") or ()))
    expected_ids=tuple(sorted(str(x["profile_id"]) for x in records))
    if ids!=expected_ids:
        raise PhaseAccessError("candidate_ids do not match candidate_records.")

    metrics_sha=str(lock.get("metrics_reference_sha256") or "")
    if len(metrics_sha)!=64:
        raise PhaseAccessError("Invalid metrics reference hash.")
    pair_bands=lock.get("pair_reference_bands")
    if not isinstance(pair_bands,dict):
        raise PhaseAccessError("pair_reference_bands must be an object.")
    review_sha=str(lock.get("human_review_sha256") or "")
    if len(review_sha)!=64:
        raise PhaseAccessError("Invalid Human Review hash.")

    if expected_type=="VAL_PROVISIONAL_LOCK":
        prior=lock.get("prior_lock_sha256")
        if not isinstance(prior,str) or len(prior)!=64:
            raise PhaseAccessError("VAL lock must reference DEV lock hash.")

    return PhaseLock(
        experiment_id=EXPERIMENT_ID,
        lock_type=expected_type,
        candidate_ids=ids,
        candidate_records=records,
        pair_reference_bands=pair_bands,
        prior_lock_sha256=lock.get("prior_lock_sha256"),
        metrics_reference_sha256=metrics_sha,
        human_review_sha256=review_sha,
        created_from_phase=str(lock.get("created_from_phase")),
        payload_sha256=str(supplied),
    )


def read_lock(path: Path,expected_type: str) -> PhaseLock:
    if not path.exists():
        raise PhaseAccessError(f"Required lock missing: {path}")
    value=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value,dict):
        raise PhaseAccessError("Lock document must be a JSON object.")
    return validate_lock(value,expected_type)


def _records_by_id(lock: PhaseLock) -> dict[str,dict]:
    return {str(x["profile_id"]):dict(x) for x in lock.candidate_records}


def authorize_phase(
    phase: str,
    *,
    dev_lock_path: Path | None=None,
    val_lock_path: Path | None=None,
) -> tuple[str,...] | None:
    phase=phase.upper()
    if phase=="DEV":
        return None
    if phase=="VAL":
        if dev_lock_path is None:
            raise PhaseAccessError("VAL requires DEV candidate lock.")
        return read_lock(dev_lock_path,"DEV_CANDIDATE_LOCK").candidate_ids
    if phase=="HOLDOUT":
        if dev_lock_path is None or val_lock_path is None:
            raise PhaseAccessError("HOLDOUT requires DEV and VAL locks.")
        dev=read_lock(dev_lock_path,"DEV_CANDIDATE_LOCK")
        val=read_lock(val_lock_path,"VAL_PROVISIONAL_LOCK")
        if val.prior_lock_sha256!=dev.payload_sha256:
            raise PhaseAccessError("VAL lock does not chain to supplied DEV lock.")
        if not set(val.candidate_ids).issubset(set(dev.candidate_ids)):
            raise PhaseAccessError("VAL lock introduces candidate absent from DEV lock.")

        dev_records=_records_by_id(dev)
        for record in val.candidate_records:
            pid=str(record["profile_id"])
            if record!=dev_records[pid]:
                raise PhaseAccessError(
                    f"VAL lock mutated frozen DEV candidate record: {pid}"
                )
        return val.candidate_ids
    raise PhaseAccessError(f"Unsupported phase: {phase}")
