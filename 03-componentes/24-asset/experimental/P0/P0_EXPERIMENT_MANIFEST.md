# Asset PRO — P0 Experiment Manifest

**Status:** DRAFT / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Date:** 2026-10-02  
**Experiment ID:** TBD  
**Freeze status:** NOT FROZEN

---

## 1. Purpose

Freeze all inputs required to determine whether the Asset PRO historical replay environment is suitable for downstream D1 validation.

## 2. Cross-Repository Baseline

### CRYPTO-PRO-SUITE
- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`
- frozen commit: TBD at Experiment Freeze

### Crypto Pro Data Feed
- repository: `rogerio-raposo/crypto-pro-datafeed`
- initial materialization baseline: `e690c2cee254a053d309cde82b4cb784ace35503`
- frozen commit: TBD at Experiment Freeze

## 3. Dataset References

The canonical Dataset Manifest is owned by the Data Feed and SHALL be referenced rather than duplicated here.

Required before freeze:

- Dataset ID: TBD
- Data Version: TBD
- Dataset Manifest path/reference: TBD
- Dataset checksum: TBD
- source provider: TBD
- venue: TBD
- market type: TBD
- instrument(s): TBD
- native timeframe: TBD
- date range: TBD

## 4. Specification References

Suite:
- `P0_REPLAY_SPECIFICATION.md`
- `P0_VALIDATION_CONTROLS.md`
- `P0_FIXTURE_EXPECTATIONS.md`

Data Feed baseline:
- `docs/experimental/asset-p0/DATASET_CONTRACT.md`
- `docs/experimental/asset-p0/HISTORICAL_SOURCE_SPEC.md`
- `docs/experimental/asset-p0/DATA_VALIDATION_SPEC.md`
- `docs/experimental/asset-p0/RESAMPLING_SPEC.md`
- `docs/experimental/asset-p0/PROVENANCE_SPEC.md`

## 5. Version Identity

Required before execution:

- Data Version: TBD
- Method Version: TBD
- Parameter Profile: `P0-NONE` unless a technical harness parameter set is explicitly introduced
- Code Version: TBD
- Manifest hash: TBD

## 6. Freeze Rule

After freeze, a material change to dataset, source, replay semantics, validation controls, fixture expectations or code baseline requires a new Experiment ID.

## 7. Execution Status

`NOT STARTED`

P1 is blocked until P0 records PASS.
