# Asset PRO — P0 Experiment Manifest

**Status:** DRAFT / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Date:** 2026-10-02  
**Experiment ID:** ASSET-P0-001  
**Freeze status:** PRE-FREEZE — DESIGN COMPLETE, EXECUTION IDENTITY INCOMPLETE

---

## 1. Purpose

Freeze all inputs required to determine whether the Asset PRO historical replay environment is suitable for downstream D1 validation.

## 2. Cross-Repository Baseline

### CRYPTO-PRO-SUITE
- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`
- frozen commit: TBD at Execution Freeze

### Crypto Pro Data Feed
- repository: `rogerio-raposo/crypto-pro-datafeed`
- current design baseline: `8e77307af7e37d472875c4a6435778036e540dfc`
- frozen commit: TBD at Execution Freeze

## 3. Planned Dataset

Canonical Dataset Manifest is owned by the Data Feed and SHALL be referenced rather than duplicated here.

Planned ASSET-P0-001 dataset:

- Dataset ID: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1`
- Data Version: TBD after acquisition/normalization
- Dataset Manifest path/reference: TBD after generation
- checksum: TBD
- source provider: Binance Public Data
- venue: Binance Spot
- market type: Spot
- instrument: BTCUSDT
- data type: klines
- native timeframe: 1h
- start: 2025-01-01 00:00 UTC inclusive
- end: 2025-04-01 00:00 UTC exclusive
- expected native records: 2160
- required derived timeframes: 4h and 1d
- canonical timestamp unit: epoch microseconds
- timezone/boundaries: UTC
- serialization: `asset-p0-canonical-json-v0.1.0`
- checksum algorithm: SHA-256

## 4. Fixture Plan

### Synthetic Golden Fixture
Planned shape:
- 48 expected 1h slots spanning two UTC days;
- one deliberately missing native interval;
- one deliberately extreme but OHLC-valid price observation;
- at least one 4h boundary;
- at least one Daily boundary;
- checkpoint/restart point before the second UTC day;
- frozen expected validation flags and deterministic resampling outputs.

### Real Golden Fixture
Planned period:
- 2024-12-31 00:00 UTC through 2025-01-03 00:00 UTC exclusive;
- BTCUSDT Binance Spot 1h public archive data.

Purpose:
- test real parsing and provenance;
- test UTC 4h/Daily boundaries;
- deliberately cross the Binance Spot public-archive timestamp-unit transition at 2025-01-01;
- verify normalization from source milliseconds/microseconds into canonical epoch microseconds.

Expected complete native slots: 72, subject to acquisition validation.

## 5. Specification References

Suite:
- `P0_REPLAY_SPECIFICATION.md`
- `P0_VALIDATION_CONTROLS.md`
- `P0_FIXTURE_EXPECTATIONS.md`

Data Feed:
- `docs/experimental/asset-p0/DATASET_CONTRACT.md`
- `docs/experimental/asset-p0/HISTORICAL_SOURCE_SPEC.md`
- `docs/experimental/asset-p0/DATA_VALIDATION_SPEC.md`
- `docs/experimental/asset-p0/RESAMPLING_SPEC.md`
- `docs/experimental/asset-p0/PROVENANCE_SPEC.md`
- `docs/experimental/asset-p0/CANDLE_BOUNDARY_POLICY.md`
- `docs/experimental/asset-p0/CANONICAL_SERIALIZATION_SPEC.md`
- `docs/experimental/asset-p0/P0_DATASET_PLAN.md`

## 6. Version Identity

Planned/frozen identities:

- Experiment ID: `ASSET-P0-001`
- Data Version: TBD after dataset generation
- Method/Specification Version: `ASSET-P0-SPEC-0.1.0`
- Parameter Profile: `P0-NONE`
- Code Version: TBD after implementation review
- Manifest hash: TBD at Execution Freeze

## 7. Two-Stage Freeze

### Design Freeze
Locks:
- experiment purpose;
- source selection;
- dataset period and instrument;
- timestamp/boundary semantics;
- serialization;
- fixture design;
- validation controls;
- replay semantics.

### Execution Freeze
Occurs only after:
- producer code exists and is reviewed;
- replay harness exists and is reviewed;
- dataset and fixtures have been generated;
- Dataset Version/checksum exist;
- Suite and Data Feed commit SHAs are pinned;
- Code Version is pinned;
- Manifest hash is computed.

No P0 execution is formal before Execution Freeze.

## 8. Material Change Rule

After Design Freeze, changing source, instrument, period, native timeframe, timestamp semantics, serialization, fixture purpose, validation controls or replay semantics requires explicit unfreeze/revision and review.

After Execution Freeze, a material change requires a new Experiment ID.

## 9. Execution Status

`NOT STARTED`

P1 remains blocked until P0 records PASS.
