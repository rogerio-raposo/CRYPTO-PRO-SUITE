# Asset PRO — P1 Execution Freeze Record

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Date:** 2026-10-03  
**Freeze type:** EXECUTION FREEZE  
**Formal DEV execution:** NOT STARTED

---

## 1. Decision

ASSET-P1-D1-001 is **EXECUTION FROZEN**.

This record authorizes only the formal DEV sequence defined by Design Freeze Revision 03.

It does not authorize VAL or HOLDOUT independently of their required locks.

## 2. Active Design Baseline

The frozen methodological baseline is:

> **Original Design Freeze + Revision 01 + Revision 02 + Revision 03**

Immutable revision records:

- `P1_DESIGN_FREEZE_RECORD.md`;
- `P1_DESIGN_FREEZE_REVISION_01.md`;
- `P1_DESIGN_FREEZE_REVISION_02.md`;
- `P1_DESIGN_FREEZE_REVISION_03.md`.

No formal DEV, VAL or HOLDOUT method output existed when these revisions were approved.

## 3. Frozen Experiment Manifest

Path:

`03-componentes/24-asset/experimental/P1/P1_EXPERIMENT_MANIFEST.md`

Frozen commit:

`bb75048c8a1d28859247a420093f8131028c4639`

Git blob SHA:

`6bb6494b66b290ad1204c4039892c8a63fe80599`

Exact UTF-8 file SHA-256:

`967f3e59772fca9d45aefa7679c4ba4abd091b3ba06f627a7ae0e7b97713e1f1`

Hash evidence:

- workflow: `Asset P1 frozen manifest hash`;
- run ID: `37120394300`;
- conclusion: `success`;
- evidence artifact ID: `11272967870`;
- artifact digest:
  `sha256:c0cba2ec8497c14448eaf36f55a42e26b333e01c31abe9bb795bef3b475154b5`.

## 4. Frozen Specification Identity

Experiment ID:

`ASSET-P1-D1-001`

Specification identity:

`ASSET-P1-D1-SPEC-REV03`

Frozen methods:

- M1 Fixed-Window Pivot;
- M2 Fixed-Percentage Reversal;
- M3 Volatility-Normalized Reversal.

Frozen analytical timeframes:

- 4h;
- Daily.

Frozen universe:

- BTCUSDT;
- ETHUSDT;
- SOLUSDT;
- XRPUSDT;
- Binance Spot.

## 5. Frozen Code Identity

Code Version:

`ASSET-P1-D1-CODE-0.1.0`

Repository:

`rogerio-raposo/CRYPTO-PRO-SUITE`

Implementation branch:

`experiment/asset-p1-d1`

Frozen implementation commit:

`cbd80134aed0cf0f0796a9ecd870dc2201ef38c3`

Implementation review:

- file: `P1_IMPLEMENTATION_REVIEW.md`;
- commit: `6077e60bade10d300ac788a614a089b999486abe`;
- result: **PROVISIONALLY READY FOR EXECUTION FREEZE** with no unresolved implementation blocker.

## 6. Code Validation Evidence

Final implementation-regression workflow:

- run ID: `37119958661`;
- conclusion: `success`;
- Python runtime: 3.12;
- artifact ID: `11273086813`;
- artifact digest:
  `sha256:f2d38ba0db16323750f5e64456ca3f18edfd57d8ce1c4d365c33a73c0abd8e73`.

Deterministic implementation hash A/B:

`6db044c41297d0e9af3c526195cc314c8883ff38244541491ae3eef8662ac63d`

Revision 03 causal repeated-run hash A/B:

`877c157331dd09501c93291c5e427bf8ce4f3798db55a340adcc2ea30d609f6b`

Validated controls:

- M1/M2/M3 implementation: PASS;
- structural sequence/regime: PASS;
- Protected Swing lifecycle: PASS;
- structural-event lifecycle: PASS;
- matching: PASS;
- comparator warm-up handling: PASS;
- Type-7/IQR primitives: PASS;
- full-profile adjacency: PASS;
- plateau/candidate-representative tooling: PASS;
- reference-band tooling: PASS;
- Human Review sampling/blinding: PASS;
- DEV/VAL/HOLDOUT phase locks: PASS;
- Prefix Invariance: PASS;
- Future-Timestamp Audit: PASS;
- Repeated-Run Determinism: PASS;
- Reference Checkpoint/Restart: PASS;
- Analysis-Island Reset: PASS.

Human Review synthetic evidence:

- review package SHA-256:
  `760f41b4c221b48941bbeffaea8c589251cc8a9119625c245eece0555317c54e`;
- alias mapping SHA-256:
  `4b6d57592a46fa4b824232a3940bcabf1e854210543f8216062bc2a91d7f44b9`.

## 7. Frozen Data Identity

Data Package Version:

`ASSET-P1-DATA-0.2.0`

Repository:

`rogerio-raposo/crypto-pro-datafeed`

Producer branch:

`experiment/asset-p1`

Dataset-build code/run head:

`f8d85435516d1eeb42085f7622296abfa4ea2ee2`

Generated-manifest commit:

`64b6489eda3b6a4e706f46dd18ed5d65d8991810`

Frozen package/documentation head:

`cd461d999d56df6b441a3a571aa118a0b6d25d32`

Dataset Index:

- path: `data/experimental/asset-p1/manifests/DATASET_INDEX.json`;
- blob SHA: `e1cf500310af3dfe1d9e3fc113353fca400c7764`.

Gap Registry blob SHA:

`f8dc5c4244df931988487d24071253a1d3f51887`

Dataset cells:

`24`

Every asset×segment Dataset Version:

`v0.2.0`

## 8. Frozen Dataset Packages

Dataset-preparation workflow:

- run ID: `37097201212`;
- conclusion: `success`.

### DEV
- 8 datasets;
- artifact ID: `11263914965`;
- digest:
  `sha256:ba0a89be052d2e765d98f6941f5689f347fda144e31ddde37ae21890ce394b09`.

### VAL
- 8 datasets;
- artifact ID: `11264144472`;
- digest:
  `sha256:adfb3bd046d45e3ad450fb2dc00c7e7c578bb92ce231f21814ee025775cd6d71`.

### HOLDOUT
- 8 datasets;
- artifact ID: `11264369151`;
- digest:
  `sha256:fb12740f8c1b4485d34e8d5033fb489d5f88ca224ec7a0243b574d6064ebae05`;
- manifests retain `analytical_access = LOCKED`.

HOLDOUT may not be analytically opened before a valid chained DEV Candidate Lock and VAL Provisional Lock.

## 9. Synchronized Venue-Gap / Analysis-Island Identity

Continuity diagnostic:

- run ID: `37096651289`;
- artifact ID: `11264686520`;
- digest:
  `sha256:bc6d5305382340ff9cf7c8a93e967eaf8ef5eeae0481bd1264cfee90bf9bbd5c`.

Frozen registered gaps:

### DEV-01
- 2021-02-11 04:00 UTC;
- 2021-03-06 02:00 UTC;
- 2021-04-20 02:00 UTC;
- 2021-04-20 03:00 UTC;
- 2021-04-25 05:00 UTC;
- 2021-04-25 06:00 UTC;
- 2021-04-25 07:00 UTC.

### VAL-01
- 2023-03-24 13:00 UTC.

Rules:

- no interpolation;
- incomplete derived candles remain audit-only;
- analytical input uses complete candles only;
- D1 state resets across Analysis Islands;
- no structural object or metric may bridge an island boundary.

Any unregistered/asymmetric gap invalidates this Execution Freeze.

## 10. Frozen Formal Phase Sequence

### DEV
1. verify this Execution Freeze;
2. M3 estimator screen;
3. execute frozen full profile grids;
4. compute metrics and plateau graph;
5. produce quantitative candidate proposal;
6. freeze DEV reference bands;
7. generate blinded DEV Human Review Set;
8. complete review/adjudication;
9. create final DEV Candidate Lock.

### VAL
Requires valid DEV Candidate Lock.

VAL may only remove/adjudicate DEV-locked candidates and may not retune parameters.

### HOLDOUT
Requires chained DEV Candidate Lock + VAL Provisional Lock.

HOLDOUT may not retune, replace, or mutate candidate identities.

## 11. Concurrency / Freshness Check at Freeze

### Data Feed
At final check:

- Data Feed `main`: `8e77307af7e37d472875c4a6435778036e540dfc`;
- P1 branch: `cd461d999d56df6b441a3a571aa118a0b6d25d32`;
- relation: ahead of main / 0 behind;
- no P1 modification to `pcp-01` paths.

### Suite
At final check:

- Suite documentation/main baseline:
  `bb75048c8a1d28859247a420093f8131028c4639`;
- frozen code baseline:
  `cbd80134aed0cf0f0796a9ecd870dc2201ef38c3`.

The code branch intentionally diverges from `main` because documentation Revisions 01–03 live in `main` and implementation lives in a dedicated branch.

The compare set contains only:

- P1 code files;
- the P1 implementation-regression workflow.

Therefore documentation and code are pinned separately rather than merged implicitly.

## 12. Freeze Rule

During formal phase execution:

- specification identity cannot change;
- Code Version cannot change;
- Data Package Version cannot change;
- Dataset Manifests/hashes cannot change;
- registered-gap policy cannot change;
- DEV reference-band methodology cannot change;
- Human Review protocol cannot change;
- phase-lock semantics cannot change.

Any material change invalidates this Execution Freeze and requires an explicit revision/new execution identity.

## 13. Consequence

P1 Execution Freeze status:

> **COMPLETE**

Formal P1 status:

> **DEV AUTHORIZED — NOT STARTED**

VAL status:

> **LOCKED — requires final DEV Candidate Lock**

HOLDOUT status:

> **LOCKED — requires valid chained DEV + VAL locks**

The only authorized next step is formal DEV execution under Revision 03.

---

**End of P1 Execution Freeze Record**
