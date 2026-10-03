# Asset PRO — P0 Decision Record

**Status:** FINAL / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Date:** 2026-10-03  
**Experiment ID:** ASSET-P0-001

---

## 1. Experiment Identity

- Experiment ID: `ASSET-P0-001`
- Method/Specification Version: `ASSET-P0-SPEC-0.1.0`
- Code Version: `ASSET-P0-CODE-0.1.0`
- Frozen Suite replay commit: `2bc3ac84397f678cdd9d202dbc8fd484928d8911`
- Frozen Data Feed code/workflow commit: `d74bf09879b0d41d4129e3a3bd60c6c764e88ecf`
- Frozen Data Feed artifact commit: `fd6dda3f4b44b5e2109779dd5e8d95a021bead7e`
- Dataset ID: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1`
- Data Version: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1-v0.1.0`
- Dataset native SHA-256: `a3032c26b6c6cb87327a0148369e6977cb3c8fc57a55779117d5c7b7e6053d24`
- Frozen Manifest commit: `1d8750b0279d70e7833af8324b036562390fb507`
- Frozen Manifest SHA-256: `5248eca0106f018d34919417f1f289239698900e92108eca6f43dd1745cb89eb`
- Parameter Profile: `P0-NONE`

## 2. Formal Execution

Formal runner:

- workflow: `ASSET-P0-001 formal execution`
- workflow run ID: `37094998832`
- orchestration branch: `execution/asset-p0-001`
- orchestration commit: `da00612fe74f6f6bb2db19c5546fe369e6a7d1bf`
- execution timestamp: `2026-10-03T03:59:14.862528+00:00`
- Python runtime: `3.12.14`

The orchestration runner is not part of the frozen analytical Code Version. Its function was limited to checking out immutable frozen identities, executing the pre-frozen controls, and publishing evidence.

Formal execution evidence artifact:

- artifact ID: `11262704648`
- artifact name: `asset-p0-001-formal-execution`
- artifact SHA-256 digest: `ead0b4a5c8748f1e8f10836f8f28f356765f7a6dc392d4581278e041d2372e7d`
- retention at creation: 90 days

## 3. Dataset and Source Controls

| Control | Result |
|---|---|
| Frozen Experiment Manifest integrity | PASS |
| Dataset schema valid | PASS |
| Required OHLC invariants valid | PASS |
| Timestamps ordered and unambiguous | PASS |
| Unresolved duplicates absent | PASS |
| Missing native intervals absent in main dataset | PASS |
| Dataset checksum/provenance recorded | PASS |
| Official archive checksums verified | PASS |
| Main native record count = 2160 | PASS |
| Derived 4h record count = 540 | PASS |
| Derived Daily record count = 90 | PASS |
| Deterministic resampling | PASS |
| Synthetic Golden Fixture reproduced | PASS |
| Real Golden Fixture reproduced | PASS |
| Source timestamp transition ms → µs normalized correctly | PASS |

Main normalized dataset hashes reproduced:

- native: `a3032c26b6c6cb87327a0148369e6977cb3c8fc57a55779117d5c7b7e6053d24`
- 4h: `f9e943ea5c04c48341355f3878e8c90e1c51d4c75c996890213b3526d922a3b5`
- 1d: `693c263ef8cfb9c8c670377bdb1091c19bdc066f69b4c16a090189b21af68155`

## 4. Synthetic Determinism Control

Frozen Synthetic Golden Fixture replay:

- Run A continuous:
  `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`
- Run B independent continuous:
  `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`
- Run C checkpoint/restart:
  `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`

Equivalence:

> PASS

## 5. Main Dataset Determinism

Formal replay of the frozen main dataset:

- Run A continuous:
  `e3b1822653067136c5f833b45cff4258645ef378fba45a00d510c125d20552ad`
- Run B independent continuous:
  `e3b1822653067136c5f833b45cff4258645ef378fba45a00d510c125d20552ad`
- Run C checkpoint/restart:
  `e3b1822653067136c5f833b45cff4258645ef378fba45a00d510c125d20552ad`

Checkpoint timestamp used by the formal runner:

`1739581200000000` epoch microseconds.

Equivalence:

> PASS

Final replay-visible counts:

- 1h: 2160
- 4h: 540
- 1d: 90

## 6. Look-Ahead Audit

| Test | Result |
|---|---|
| Future Candle Access Test | PASS |
| Incomplete Higher-Timeframe Test | PASS |
| Derived Calculation Visibility Test | PASS |
| Restart State Isolation Test | PASS |

No confirmed look-ahead violation was observed.

## 7. Critical Failures and Warnings

Critical failures:

> **NONE**

Warnings:

> **NONE**

Anomaly notes:

> No anomaly requiring escalation, freeze revision, or experiment invalidation was observed during the formal execution.

## 8. Final Decision

**Final Decision: `PASS`**

Rationale:

ASSET-P0-001 satisfied every frozen critical control. The frozen dataset and Golden Fixtures were reproduced from the approved source contract, official archive integrity checks passed, canonical dataset identities matched the Execution Freeze, deterministic resampling was reproduced, causal replay showed no future-data leakage, incomplete higher-timeframe leakage was blocked, and continuous/repeated/checkpoint-restart runs were equivalent on both the synthetic fixture and the main validation dataset.

Therefore:

> the historical validation environment is sufficiently causal, deterministic, auditable and reproducible to authorize downstream P1/D1 validation under the explicitly frozen P0 baseline.

## 9. Consequence

P0 status:

> **PASS**

P1 status:

> **UNBLOCKED**

The next authorized phase is P1 preparation/execution under the previously defined D1 validation protocol.

This PASS does not:

- validate D1 itself;
- select a swing method;
- select D1 parameter profiles;
- validate predictive usefulness;
- promote experimental artifacts automatically to normative methodology.

---

**End of Decision Record**
