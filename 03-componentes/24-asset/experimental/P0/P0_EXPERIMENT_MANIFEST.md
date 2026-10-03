# Asset PRO — P0 Experiment Manifest

**Status:** EXECUTION FROZEN / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Date:** 2026-10-03  
**Experiment ID:** ASSET-P0-001  
**Freeze status:** EXECUTION FROZEN — FORMAL EXECUTION NOT STARTED

---

## 1. Purpose

Freeze all inputs, implementations, datasets and identities required for the formal execution of ASSET-P0-001.

P0 validates infrastructure and data/replay integrity. It does not validate D1, select swing parameters, or evaluate predictive outcomes.

## 2. Cross-Repository Execution Baseline

### CRYPTO-PRO-SUITE
- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`;
- frozen implementation commit used by Python 3.12 regression: `2bc3ac84397f678cdd9d202dbc8fd484928d8911`;
- replay implementation path: `03-componentes/24-asset/experimental/P0/code/`.

### Crypto Pro Data Feed
- repository: `rogerio-raposo/crypto-pro-datafeed`;
- isolated branch: `experiment/asset-p0`;
- source-validation workflow/code commit: `d74bf09879b0d41d4129e3a3bd60c6c764e88ecf`;
- frozen artifact commit: `fd6dda3f4b44b5e2109779dd5e8d95a021bead7e`;
- main branch observed during final conflict check: `8e77307af7e37d472875c4a6435778036e540dfc`;
- branch status at freeze: 16 commits ahead / 0 behind;
- divergent paths: Asset P0 only; no PCP-01 overlap.

## 3. Dataset Identity

- Dataset ID: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1`;
- Data Version: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1-v0.1.0`;
- canonical Dataset Manifest: `data/experimental/asset-p0/manifests/ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1.json`;
- manifest blob SHA: `55c42a448e08ec8a9d4b6ffa3045aaadbc2c04e4`;
- normalized native dataset SHA-256: `a3032c26b6c6cb87327a0148369e6977cb3c8fc57a55779117d5c7b7e6053d24`;
- derived 4h SHA-256: `f9e943ea5c04c48341355f3878e8c90e1c51d4c75c996890213b3526d922a3b5`;
- derived 1d SHA-256: `693c263ef8cfb9c8c670377bdb1091c19bdc066f69b4c16a090189b21af68155`;
- records: 2160 native / 540 4h / 90 1d;
- source provider: Binance Public Data;
- venue: Binance Spot;
- instrument: BTCUSDT;
- native timeframe: 1h;
- period: 2025-01-01 00:00 UTC inclusive through 2025-04-01 00:00 UTC exclusive;
- canonical timestamp unit: Unix epoch microseconds;
- timezone/boundaries: UTC;
- serialization policy: `asset-p0-canonical-json-v0.1.0`;
- checksum algorithm: SHA-256.

## 4. Official Source Archives

Monthly source archives and verified official SHA-256 values:

- January 2025: `e7f2aaa5396a8062a57ab29ce9fab2d76b2c84ec58815d4ab7b3fe16f78c7118`;
- February 2025: `7420f55c93f61d7e734fc9d2507c7f2fcb5eaf48112277cecd241d4e1dbf3bd5`;
- March 2025: `b5ae8bb57e5e526c2050c9f8229b723871a5af47d80c53453abf61847a5f3aa6`.

Every archive was verified against its official `.CHECKSUM` before extraction.

## 5. Golden Fixtures

### Synthetic Golden Fixture
- version: `ASSET-P0-SYNTHETIC-v0.1.0`;
- native SHA-256: `09ca24c7bc6c7c08ec678b10e5c93817ba64d5cd3aef08e6fc122b6c9a838575`;
- 4h SHA-256: `53c2e1a6166464df63ead361042399edf6bfbac956bf2b5a8cef4d4fd2370b7c`;
- 1d SHA-256: `0bbb526838b76d1ab58ee17286d2067030861c3c9ff223dee6ce8570ecb54f18`.

### Real Golden Fixture
- Dataset ID: `ASSET-P0-REAL-GOLDEN-BTCUSDT-1H-2024-12-31_2025-01-02`;
- version: `ASSET-P0-REAL-FIXTURE-v0.1.0`;
- records: 72 native / 18 4h / 3 1d;
- native SHA-256: `3516bfbc38463d65e06cb9c83d4f05b906c01ab628dfaf5a9b767a54ee4e3a39`;
- 4h SHA-256: `8966ee447596fc654eb38e68b146d20034fb36deaba610f9e26e593e53848452`;
- 1d SHA-256: `dce12a94a6944227dcd058b92196e649350d46e4e7442b747986f569d0d9c2ab`;
- 2024-12-31 source archive unit: milliseconds;
- 2025-01-01 and 2025-01-02 source archive unit: microseconds;
- canonical normalized unit: microseconds.

Verified daily archive SHA-256 values:

- 2024-12-31: `4a6836ceae18ee150f54de0d8d33d60864b0f4c18457e025d56711e61dfdd343`;
- 2025-01-01: `8077644eb5088200969b135d7046ba777281be303fa32aceff28fe3baeaa5873`;
- 2025-01-02: `7615431267eec61ab67add2206f2efdfd53c38cb0db21322aec013c12203a084`.

## 6. Code Version

- Code Version: `ASSET-P0-CODE-0.1.0`;
- Data Feed code/workflow commit: `d74bf09879b0d41d4129e3a3bd60c6c764e88ecf`;
- Suite replay commit: `2bc3ac84397f678cdd9d202dbc8fd484928d8911`;
- Method/Specification Version: `ASSET-P0-SPEC-0.1.0`;
- Parameter Profile: `P0-NONE`.

## 7. Python 3.12 Regression

GitHub Actions workflow:

- run ID: `37094587777`;
- conclusion: `success`;
- Python runtime: 3.12;
- regression artifact path: `data/experimental/asset-p0/manifests/PYTHON312_REPLAY_REGRESSION.json`;
- regression blob SHA: `e8669252562042ab135600553fd824a7a8ff2151`.

Replay trace hashes:

- Run A continuous: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`;
- Run B independent continuous: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`;
- Run C checkpoint/restart: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`.

Result:

> implementation-level deterministic replay PASS on Python 3.12.

## 8. Large Dataset Artifact

GitHub Actions artifact:

- artifact ID: `11263860573`;
- name: `asset-p0-main-dataset`;
- artifact digest: `sha256:91d076d55c872021092ba993312cb55ea8b29479b8dcd9038ba33f3dcdff7277`;
- workflow run: `37094587777`;
- retention at creation: 30 days.

The artifact is a convenience copy only. Reproducibility is governed by source archive checksums, frozen code, dataset version and canonical normalized hashes.

## 9. Frozen Replay and Validation Semantics

The formal execution SHALL use the already-frozen rules for:

- closed-candle causal visibility;
- canonical `interval_end_us`;
- no future-row access;
- no incomplete higher-timeframe leakage;
- append-only events;
- deterministic snapshots;
- checkpoint/restart equivalence;
- deterministic resampling;
- archive checksum verification;
- no missing/duplicate native interval in the main dataset;
- binary P0 decision: PASS or FAIL.

## 10. Execution Freeze

### Design Freeze
`COMPLETE`

### Execution Freeze
`COMPLETE`

No inputs, code identities, data identities, fixture identities, validation controls or replay semantics may change during formal ASSET-P0-001 execution.

Any material change requires a new formal experiment identity or explicit freeze revision before execution.

## 11. Manifest Integrity

The SHA-256 of this exact frozen manifest file is calculated after commit and recorded in:

`P0_EXECUTION_FREEZE_RECORD.md`.

The hash is intentionally external to avoid a self-referential manifest hash.

## 12. Execution Status

`NOT STARTED`

Execution Freeze authorizes the next phase but does not itself execute P0.

P1 remains blocked until the P0 Decision Record records `PASS`.
