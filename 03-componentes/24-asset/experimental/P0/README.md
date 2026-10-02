# Asset PRO — P0 Data & Causal Replay Integrity

**Status:** DESIGN FROZEN / IMPLEMENTATION IN PROGRESS / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02  
**Execution status:** NOT STARTED

---

## Purpose

P0 verifies that the historical validation environment is causal, deterministic, auditable and reproducible before any D1/P1 experiment is authorized.

## Package

- `P0_EXPERIMENT_MANIFEST.md`
- `P0_REPLAY_SPECIFICATION.md`
- `P0_VALIDATION_CONTROLS.md`
- `P0_FIXTURE_EXPECTATIONS.md`
- `P0_DESIGN_FREEZE_RECORD.md`
- `P0_IMPLEMENTATION_VALIDATION.md`
- `P0_EXECUTION_FREEZE_CHECKLIST.md`
- `P0_DECISION_RECORD.md`
- `code/` — causal replay implementation and regression checks.

## Design Freeze

Experiment:

`ASSET-P0-001`

Suite manifest freeze commit:

`915d3ef01c5c273348a84078ca1dfc81fe701781`

Data Feed producer-side design commit:

`35e8c1120c6d13acb16617507d770aa2b0ea0b7e`

Data Feed development branch:

`experiment/asset-p0`

The branch name is operational; the commit SHA is the immutable Design Freeze reference.

## Implementation State

Implemented:

- producer-side normalization / validation / resampling / checksum utilities;
- deterministic synthetic golden fixture;
- causal replay harness;
- checkpoint/restart;
- implementation-level synthetic determinism regression.

Still pending:

- Python 3.12 runtime regression;
- Real Golden Fixture acquisition and freeze;
- main Q1-2025 validation dataset acquisition and freeze;
- final code review and cross-repository pinning;
- final Experiment Manifest hash.

## Execution Freeze

`PENDING`

No formal P0 execution is authorized before Execution Freeze.

## Gate

P1 remains blocked until the P0 Decision Record records `PASS`.
