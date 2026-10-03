# Asset PRO — P0 Execution Freeze Record

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Experiment ID:** ASSET-P0-001  
**Date:** 2026-10-03  
**Freeze type:** EXECUTION FREEZE  
**Formal execution status:** NOT STARTED

---

## 1. Decision

ASSET-P0-001 is **EXECUTION FROZEN**.

This record authorizes formal P0 execution using only the identities and artifacts listed below.

It does not itself execute P0 and does not authorize P1.

## 2. Frozen Experiment Manifest

- path: `03-componentes/24-asset/experimental/P0/P0_EXPERIMENT_MANIFEST.md`;
- manifest commit: `1d8750b0279d70e7833af8324b036562390fb507`;
- manifest blob SHA: `29ea5beb2f6a40a7e5ea2843b84cf96058e31662`;
- manifest SHA-256: `5248eca0106f018d34919417f1f289239698900e92108eca6f43dd1745cb89eb`.

The SHA-256 is computed over the exact UTF-8 content of the frozen manifest file.

## 3. Frozen Code Identity

Code Version:

`ASSET-P0-CODE-0.1.0`

Suite replay implementation:

`2bc3ac84397f678cdd9d202dbc8fd484928d8911`

Data Feed source-validation workflow/code:

`d74bf09879b0d41d4129e3a3bd60c6c764e88ecf`

Data Feed artifact commit:

`fd6dda3f4b44b5e2109779dd5e8d95a021bead7e`

## 4. Frozen Dataset Identity

- Dataset ID: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1`;
- Data Version: `ASSET-P0-001-BTCUSDT-SPOT-1H-2025Q1-v0.1.0`;
- native checksum: `a3032c26b6c6cb87327a0148369e6977cb3c8fc57a55779117d5c7b7e6053d24`;
- 4h checksum: `f9e943ea5c04c48341355f3878e8c90e1c51d4c75c996890213b3526d922a3b5`;
- 1d checksum: `693c263ef8cfb9c8c670377bdb1091c19bdc066f69b4c16a090189b21af68155`;
- records: 2160 native / 540 4h / 90 1d.

## 5. Source Verification

Official Binance archive checksum verification passed for:

### Main dataset
- 2025-01: `e7f2aaa5396a8062a57ab29ce9fab2d76b2c84ec58815d4ab7b3fe16f78c7118`;
- 2025-02: `7420f55c93f61d7e734fc9d2507c7f2fcb5eaf48112277cecd241d4e1dbf3bd5`;
- 2025-03: `b5ae8bb57e5e526c2050c9f8229b723871a5af47d80c53453abf61847a5f3aa6`.

### Real Golden Fixture
- 2024-12-31: `4a6836ceae18ee150f54de0d8d33d60864b0f4c18457e025d56711e61dfdd343`;
- 2025-01-01: `8077644eb5088200969b135d7046ba777281be303fa32aceff28fe3baeaa5873`;
- 2025-01-02: `7615431267eec61ab67add2206f2efdfd53c38cb0db21322aec013c12203a084`.

## 6. Fixture Validation

Synthetic Golden Fixture:

- 47 native records across 48 expected slots;
- deliberate gap and extreme observation preserved;
- frozen expected hashes reproduced.

Real Golden Fixture:

- 72 native records;
- 18 complete 4h records;
- 3 complete Daily records;
- millisecond source timestamps confirmed on 2024-12-31;
- microsecond source timestamps confirmed from 2025-01-01;
- canonical microsecond timeline remained continuous.

## 7. Python 3.12 Validation

GitHub Actions run:

`37094587777`

Conclusion:

`success`

Replay regression:

- continuous A: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`;
- continuous B: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`;
- checkpoint/restart C: `0a4d6e1a401081f94b0f8397142a6395103c1863a5fd438125cf180c551b6dc3`.

Result:

> deterministic replay regression PASS on Python 3.12.

## 8. Concurrency Check

At freeze:

- Data Feed `main`: `8e77307af7e37d472875c4a6435778036e540dfc`;
- Asset P0 branch artifact head: `fd6dda3f4b44b5e2109779dd5e8d95a021bead7e`;
- branch relation: 16 commits ahead / 0 behind;
- divergent files belong only to Asset P0 paths and its dedicated workflow;
- no PCP-01 path overlap was detected.

No merge into Data Feed `main` is required for formal P0 execution because the experiment is pinned to immutable branch commits.

## 9. Large Dataset Artifact

GitHub Actions artifact:

- ID: `11263860573`;
- digest: `sha256:91d076d55c872021092ba993312cb55ea8b29479b8dcd9038ba33f3dcdff7277`.

This artifact is convenience storage only. The experiment identity remains reproducible from frozen source checksums, code SHAs and canonical dataset hashes.

## 10. Freeze Consequence

The only authorized next phase is:

> **formal execution of ASSET-P0-001**.

During formal execution:

- no frozen input may change;
- no code may change;
- no dataset may change;
- no validation rule may change;
- no fixture may change.

Any material change invalidates this Execution Freeze and requires a new formal identity or revision.

P1 remains blocked until:

> `P0_DECISION_RECORD.md = PASS`.

---

**End of Execution Freeze Record**
