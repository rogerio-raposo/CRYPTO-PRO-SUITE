# Asset PRO — P0 Experiment Manifest

**Status:** DESIGN FROZEN / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Date:** 2026-10-02  
**Experiment ID:** ASSET-P0-001  
**Freeze status:** DESIGN FROZEN — EXECUTION FREEZE PENDING

---

## 1. Purpose

Freeze the design inputs required to determine whether the Asset PRO historical replay environment is suitable for downstream D1 validation.

P0 validates infrastructure and data/replay integrity. It does not validate D1, select swing parameters, or evaluate predictive outcomes.

## 2. Cross-Repository Design Baseline

### CRYPTO-PRO-SUITE
- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`
- Design Freeze manifest commit: recorded in `P0_DESIGN_FREEZE_RECORD.md`
- Execution Freeze commit: TBD

### Crypto Pro Data Feed
- repository: `rogerio-raposo/crypto-pro-datafeed`
- isolated branch: `experiment/asset-p0`
- Design Freeze producer-side commit: `35e8c1120c6d13acb16617507d770aa2b0ea0b7e`
- Execution Freeze commit: TBD

The Data Feed design commit is immutable evidence for the frozen producer-side specifications. Future branch movement does not alter this reference.

## 3. Frozen Dataset Design

Canonical Dataset Manifest is owned by the Data Feed and SHALL be referenced rather than duplicated here.

ASSET-P0-001 main validation dataset:

- planned Dataset ID: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1`
- Data Version: TBD after acquisition/normalization
- Dataset Manifest path/reference: TBD after generation
- final normalized checksum: TBD
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
- expected 4h records: 540
- expected 1d records: 90
- canonical timestamp unit: Unix epoch microseconds
- timezone/boundaries: UTC
- interval semantics: half-open `[start,end)`
- serialization policy: `asset-p0-canonical-json-v0.1.0`
- checksum algorithm: SHA-256.

Any missing native 1h interval inside the formal main dataset is a blocking integrity failure for ASSET-P0-001.

## 4. Frozen Source Acquisition Design

Main validation dataset:

- official Binance Public Data monthly Spot kline archives;
- BTCUSDT 1h;
- January 2025;
- February 2025;
- March 2025.

Each archive must be verified against its associated official `.CHECKSUM` before extraction.

## 5. Frozen Fixture Design

### Synthetic Golden Fixture
Design:

- 48 expected hourly slots spanning two complete UTC days;
- one deliberately missing native interval;
- one deliberately extreme but OHLC-valid observation;
- multiple 4h boundaries;
- one Daily boundary transition;
- checkpoint/restart point before the second UTC day;
- frozen expected validation flags, resampling states and canonical hashes before Execution Freeze.

The fixture intentionally tests gap behavior and is not required to be a complete market series.

### Real Golden Fixture
Source:

- Binance Public Data;
- Binance Spot;
- BTCUSDT;
- 1h daily kline archives.

Period:

- 2024-12-31 00:00 UTC inclusive;
- 2025-01-03 00:00 UTC exclusive.

Planned source objects:

- 2024-12-31;
- 2025-01-01;
- 2025-01-02;

with official checksum verification.

Purpose:

- real archive parsing;
- provenance;
- UTC 4h/Daily boundaries;
- normalization across the Binance Spot public-data source timestamp-unit transition at 2025-01-01.

Expected complete native slots: 72, subject to acquisition validation.

## 6. Frozen Replay Semantics

The P0 replay design SHALL preserve:

- one logical `replay_timestamp`;
- closed-candle visibility only;
- no future-row access;
- no incomplete higher-timeframe leakage;
- canonical availability at `interval_end_us`;
- append-only event log;
- deterministic snapshot envelope;
- checkpoint/restart equivalence;
- canonical serialization prior to deterministic hash comparison.

## 7. Frozen Validation Semantics

P0 decision remains binary:

- `PASS`;
- `FAIL`.

Critical controls include:

- dataset/schema integrity;
- timestamp integrity;
- official archive checksum verification;
- no unresolved duplicates/missing intervals in the main dataset;
- deterministic resampling;
- causal visibility;
- repeated-run determinism;
- checkpoint/restart equivalence.

Warnings do not create a third formal decision state.

## 8. Specification References

Suite:

- `P0_REPLAY_SPECIFICATION.md`
- `P0_VALIDATION_CONTROLS.md`
- `P0_FIXTURE_EXPECTATIONS.md`
- `P0_DESIGN_FREEZE_RECORD.md`

Data Feed at commit `35e8c1120c6d13acb16617507d770aa2b0ea0b7e`:

- `docs/experimental/asset-p0/DATASET_CONTRACT.md`
- `docs/experimental/asset-p0/HISTORICAL_SOURCE_SPEC.md`
- `docs/experimental/asset-p0/DATA_VALIDATION_SPEC.md`
- `docs/experimental/asset-p0/RESAMPLING_SPEC.md`
- `docs/experimental/asset-p0/PROVENANCE_SPEC.md`
- `docs/experimental/asset-p0/CANDLE_BOUNDARY_POLICY.md`
- `docs/experimental/asset-p0/CANONICAL_SERIALIZATION_SPEC.md`
- `docs/experimental/asset-p0/P0_DATASET_PLAN.md`

## 9. Version Identity

Frozen design identity:

- Experiment ID: `ASSET-P0-001`
- Method/Specification Version: `ASSET-P0-SPEC-0.1.0`
- Parameter Profile: `P0-NONE`

Pending for Execution Freeze:

- Data Version;
- canonical Dataset Manifest;
- dataset checksum;
- Suite execution commit;
- Data Feed execution commit;
- Code Version;
- fixture hashes;
- Manifest hash.

## 10. Freeze Model

### Design Freeze — COMPLETE
Locks:

- experiment purpose;
- source selection;
- instrument;
- period;
- native/derived timeframes;
- timestamp and boundary semantics;
- canonical serialization;
- fixture purposes/design;
- validation controls;
- replay semantics.

Changing any of those items requires an explicit Design Unfreeze/Revision Record before implementation continues under ASSET-P0-001.

### Execution Freeze — PENDING
Requires:

- producer code implemented and reviewed;
- replay harness implemented and reviewed;
- fixtures produced and reviewed;
- main dataset produced and validated;
- Data Version/checksum generated;
- Suite and Data Feed execution SHAs pinned;
- Code Version pinned;
- Manifest hash generated.

No formal P0 execution may occur before Execution Freeze.

## 11. Execution Status

`NOT STARTED`

P1 remains blocked until P0 records `PASS`.
