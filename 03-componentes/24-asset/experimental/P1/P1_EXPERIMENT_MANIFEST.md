# Asset PRO — P1 Experiment Manifest

**Status:** EXECUTION FROZEN / NON-NORMATIVE  
**Experiment ID:** ASSET-P1-D1-001  
**Pilot:** P1 — D1 Structural Engine Validation  
**P0 dependency:** ASSET-P0-001 = PASS  
**Freeze status:** EXECUTION FROZEN — FORMAL DEV NOT STARTED

---

## 1. Question

Which candidate swing-detection architecture(s) provide a causal, deterministic, stable, interpretable and sufficiently responsive basis for D1 structural sequence, regime, Protected Swing and structural-event classification?

P1 does not evaluate trading returns or predictive profitability.

## 2. Frozen Universe

| Role | Instrument | Function |
|---|---|---|
| A1 | BTCUSDT | high-liquidity market reference |
| A2 | ETHUSDT | second large-cap, distinct structural behavior |
| A3 | SOLUSDT | liquid high-beta large-cap |
| A4 | XRPUSDT | liquid large-cap alt with distinct episodic structure |

Frozen pilot market:

`Binance Spot`

## 3. Frozen Data Design

Producer repository:

`rogerio-raposo/crypto-pro-datafeed`

P1 producer branch:

`experiment/asset-p1`

Frozen producer-side design/evidence commit:

`199c301b5ee14a1b322b86d4b992d4de9d2157cf`

Source:

`Binance Public Data monthly Spot kline archives`

Native timeframe:

`1h`

Analytical timeframes:

- 4h;
- 1d.

Canonical temporal contract:

- UTC boundaries;
- canonical epoch microseconds after normalization;
- deterministic resampling semantics inherited from the P0-approved contract.

Large historical datasets remain outside Git. Dataset manifests, checksums and audit metadata remain versioned.

## 4. Source Eligibility Evidence

Eligibility workflow:

- run ID: `37095698535`;
- conclusion: `success`.

Evidence:

`data/experimental/asset-p1/SOURCE_ELIGIBILITY.md`

Result:

- BTCUSDT: 36/36 months eligible;
- ETHUSDT: 36/36 months eligible;
- SOLUSDT: 36/36 months eligible;
- XRPUSDT: 36/36 months eligible.

Overall:

> **PASS**

Source existence verification does not replace archive checksum, record-continuity or dataset validation required before Execution Freeze.

## 5. Frozen Phase Split

### DEV
- `DEV-01`: 2021-01-01 through 2021-07-01 UTC exclusive.
- `DEV-02`: 2022-06-01 through 2022-12-01 UTC exclusive.

### VAL
- `VAL-01`: 2023-01-01 through 2023-07-01 UTC exclusive.
- `VAL-02`: 2023-07-01 through 2024-01-01 UTC exclusive.

### Structural Holdout
- `HOLD-01`: 2024-01-01 through 2024-07-01 UTC exclusive.
- `HOLD-02`: 2024-07-01 through 2025-01-01 UTC exclusive.

The same calendar segments apply to all assets.

Holdout analytical outputs may not be used for parameter tuning.

## 6. Frozen Methods

- M1 — Fixed-Window Pivot;
- M2 — Fixed-Percentage Reversal;
- M3 — Volatility-Normalized Reversal.

No hybrid M4 is permitted in ASSET-P1-D1-001.

Primary reversal confirmation basis:

> Close-confirmed reversal against a High/Low candidate extremum.

Intrabar variants remain DEV diagnostic-only and are not eligible for final candidate selection.

## 7. Frozen Structural Pipeline

`Swing Detector → Confirmed Structural Swings → HH/EH/LH/HL/EL/LL → Regime → Protected Swing → Structural Events`

P1 structural events:

- Breach;
- PCSB;
- Continuation Break;
- Counter-Structural Break;
- price-based Reclaim.

D3 Acceptance/Re-Acceptance and final Failed Break classification are excluded.

## 8. Frozen Parameter Design

### M1
4h:

`w ∈ {2,3,4,6,8,12}`

Daily:

`w ∈ {2,3,4,5,7,10}`

### M2
4h:

`p ∈ {1.0%,1.5%,2.5%,4.0%,6.0%,9.0%}`

Daily:

`p ∈ {2.0%,3.0%,5.0%,8.0%,12.0%,18.0%}`

### M3 estimator screen
- Wilder ATR;
- rolling Median True Range;
- screening profile (n=14, k=2.0).

Full grid for surviving estimators:

[
n \in \{10,14,21,34\}
]

[
k \in \{1.0,1.5,2.0,2.5,3.0,4.0\}
]

### Structural grid
Equality:

[
q \in \{0.25,0.50,0.75\}
]

Break/reclaim buffer:

[
b \in \{0,0.25,0.50\}
]

Trend persistence:

[
m \in \{2,3\}
]

Temporal ATR-reference semantics are frozen in `P1_METHOD_SPECIFICATIONS.md` and `P1_PARAMETER_PROFILE_REGISTRY.md`.

## 9. Frozen Plateau / Reference-Band Methodology

P1 does not use arbitrary universal stability thresholds.

DEV identifies local parameter plateaus using componentwise adjacent-profile discontinuities and robust fences:

[
Q3 + 1.5 \times IQR
]

A candidate plateau requires at least three connected profiles/cells and no hard blocker.

DEV also freezes candidate-specific reference bands.

VAL and Holdout test those frozen bands and cannot redefine them.

No weighted composite score is used.

## 10. Frozen Matching Design

Matching is:

- same swing type only;
- one-to-one;
- chronological/monotonic;
- lexicographic, not weighted.

Primary window:

- 4h: 3 bars and 1.0 ATR14;
- Daily: 2 bars and 1.0 ATR14.

Strict and wide diagnostics are frozen in `P1_MATCHING_SPECIFICATION.md`.

## 11. Frozen Anti-Leakage Rules

P1 shall not use:

- P&L;
- future return;
- trade outcome;
- post-event success;
- Holdout results for tuning;
- visual preference as sole selection basis;
- composite weighted scores.

At DEV end, candidates are locked before VAL.

At VAL end, provisional candidates are locked before Holdout.

Any required retuning after VAL/Holdout results in `P1-REVISE`, not in-place parameter modification.

## 12. Frozen Human Review Design

Human review is diagnostic.

DEV/VAL target set:

> 64 cases.

Holdout target set:

> 16 cases.

Method/profile identifiers are masked where operationally possible.

If only one reviewer is available, subjective findings cannot be the sole acceptance/rejection basis.

## 13. Frozen Decision States

- `P1-PASS — Single Candidate`;
- `P1-PASS — Multiple Candidates`;
- `P1-REVISE`;
- `P1-FAIL`.

## 14. Freeze Model

### Design Freeze — COMPLETE

This Design Freeze locks:

- universe;
- source/market contract;
- phase/segment design;
- Holdout discipline;
- M1/M2/M3 semantics;
- parameter grids;
- structural semantics;
- matching;
- metrics/plateau methodology;
- Human Review;
- blockers/decision states.

Any material change requires an explicit Design Freeze revision before implementation continues.

### Execution Freeze — PENDING

Execution Freeze requires:

- multi-asset producer implementation and review;
- generated datasets/manifests/checksums;
- D1 Structural Engine implementation and review;
- deterministic regression tests;
- Holdout access segregation;
- Code/Data Versions;
- pinned implementation commits;
- frozen Manifest hash.

## 15. Current Status

P1 Design Freeze:

> **COMPLETE — REVISION 03**

P1 implementation:

> **VALIDATED**

P1 Execution Freeze:

> **COMPLETE**

P1 formal execution:

> **NOT STARTED**


---

## 16. Design Freeze Revision 01

Revision 01 preserves the original universe, market, phase calendar, methods and parameter grids, but closes implementation-readiness gaps discovered after the original Design Freeze.

### 16.1 Synchronized Venue Gap Registry

The following native 1h intervals are missing identically in BTCUSDT, ETHUSDT, SOLUSDT and XRPUSDT Binance Spot archives:

#### DEV-01
- 2021-02-11 04:00 UTC
- 2021-03-06 02:00 UTC
- 2021-04-20 02:00 UTC
- 2021-04-20 03:00 UTC
- 2021-04-25 05:00 UTC
- 2021-04-25 06:00 UTC
- 2021-04-25 07:00 UTC

#### VAL-01
- 2023-03-24 13:00 UTC

No duplicates were detected in the 24 frozen asset×segment source cells.

These timestamps are classified as `SYNCHRONIZED_VENUE_GAP` because:

- the missing timestamps are identical across all four pilot instruments;
- official archive checksums remain valid;
- Binance published maintenance/interruption notices covering the corresponding periods.

### 16.2 Gap Handling

Frozen segment dates do not change.

P1 does not interpolate missing candles.

For 4h and Daily:

- any derived candle containing a registered gap is incomplete and excluded from analytical input;
- the analytical stream is split into contiguous Analysis Islands;
- D1 state resets at every island boundary;
- metrics do not span an island boundary.

An unregistered or non-synchronized gap remains a blocker.

### 16.3 Operational Clarifications

Revision 01 additionally freezes:

- M1 same-type confirmed-pivot handling;
- M2/M3 bootstrap and ambiguity rules;
- M3 start only after volatility initialization;
- same-bar processing order;
- latest-only generic swing-reference lifecycle;
- range outer-boundary construction;
- opposing-cycle Transition logic;
- exact metric formulas;
- event/protected-swing matching;
- deterministic causal Human Review windows.

Canonical details are contained in:

- `P1_METHOD_SPECIFICATIONS.md`;
- `P1_METRICS_SPECIFICATION.md`;
- `P1_HUMAN_REVIEW_PROTOCOL.md`.

### 16.4 Change-Control Consequence

The original Design Freeze Record remains historical evidence.

Revision 01 supersedes only the affected design clauses and must be the design baseline used for implementation and Execution Freeze.


---

## 17. Design Freeze Revision 02

Revision 02 preserves:

- the complete Revision 01 synchronized-venue-gap policy;
- the original universe and phase calendar;
- M1/M2/M3 primary method semantics;
- detector and structural parameter grids.

Revision 02 closes the remaining implementation ambiguities affecting matching, statistical fences, candidate selection and review sampling.

### 17.1 Comparator Warm-Up

ATR14-normalized matching excludes objects whose own causal timestamp precedes ATR14 initialization.

Such objects remain valid structural outputs but are marked comparison-ineligible and are excluded from matching denominators.

### 17.2 Statistical Convention

All quantiles use deterministic Type-7 linear interpolation.

DEV fences require at least four valid observations after NA exclusion.

### 17.3 Full-Profile Plateau Graph

Plateau adjacency uses complete detector+structural profile coordinates and exactly one one-step coordinate change.

M3 adjacency never crosses estimator identity.

### 17.4 Deterministic Candidate Representatives

Responsive, Balanced and Conservative representatives are selected only from qualifying plateau profiles using pooled DEV Swing Density and deterministic tie-breaking.

The labels describe output density, not quality.

### 17.5 Frozen DEV Reference Bands

Single-profile and candidate-pair reference-band metrics, directionality and NA requirements are frozen in `P1_METRICS_SPECIFICATION.md`.

VAL/Holdout may test but never redefine those bands.

### 17.6 Human Review Determinism

Revision 02 freezes:

- exact disagreement/churn/event-delay window magnitudes;
- fixed case-selection order;
- unique-window rule;
- response vocabulary;
- exact-response inter-rater agreement.

### 17.7 Detector Edge Cases

Revision 02 freezes:

- M1 simultaneous unique High+Low pivot as `AMBIGUOUS_DUAL_PIVOT` with no confirmation;
- M3 diagnostic intrabar trigger semantics;
- `AMBIGUOUS_INTRABAR_SEQUENCE` handling.

### 17.8 Active Design Baseline

Revision 02 supersedes only clauses explicitly revised by Revision 01/02.

The active implementation baseline is:

> **Original Design Freeze + Revision 01 + Revision 02**

No formal P1 phase execution has occurred.


---

## 18. Design Freeze Revision 03

Revision 03 freezes formal phase orchestration and causal-validation preconditions.

### 18.1 Formal Phase Stop Points

DEV, VAL and HOLDOUT follow the explicit compute → review → lock/decision sequence defined in `P1_DECISION_RULES.md`.

Human Review may remove a candidate under frozen defect rules but may never trigger in-place parameter substitution.

### 18.2 Review Population

- DEV review: quantitative proposed candidates only;
- VAL review: DEV-locked candidates only;
- Holdout review: VAL-locked candidates only.

### 18.3 Review Integrity

Reviewer-facing profile identities are blinded by deterministic aliases.

Completed review records are hashed and their SHA-256 is required by the applicable lock.

### 18.4 Causal Validation Before Execution Freeze

The D1 implementation must pass:

- prefix-invariance regression;
- no future-timestamp output audit;
- repeated-run determinism;
- reference checkpoint/restart equivalence;
- Analysis-Island reset regression.

Prefix invariance means every previously confirmed swing, structural relation, regime-change event, Protected Swing lifecycle record and structural event remains byte-equivalent when additional future candles are revealed.

The reference checkpoint harness may persist the already-revealed candle prefix plus frozen profile configuration and recompute state after restore. It must never persist or access future candles.

After these regressions pass, formal P1 phase execution may use the deterministic batch engine because P0 has already validated the underlying causal replay environment.

### 18.5 M3 Intrabar Diagnostic

The frozen diagnostic-only M3 intrabar subset is executed in DEV after estimator screening and reported separately.

It cannot become a candidate in ASSET-P1-D1-001.

### 18.6 Active Baseline

The active design baseline is:

> **Original Design Freeze + Revision 01 + Revision 02 + Revision 03**

No formal P1 phase execution has occurred.


---

## 19. Execution Freeze Identity

The P1 Execution Freeze uses the active design baseline:

> **Original Design Freeze + Revision 01 + Revision 02 + Revision 03**

### 19.1 Specification Identity

- Experiment ID: `ASSET-P1-D1-001`;
- Specification identity: `ASSET-P1-D1-SPEC-REV03`;
- parameter registry: frozen grids and rules defined by the active design baseline.

### 19.2 Code Identity

Code Version:

`ASSET-P1-D1-CODE-0.1.0`

Frozen Suite implementation:

- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`;
- implementation branch: `experiment/asset-p1-d1`;
- frozen code commit: `cbd80134aed0cf0f0796a9ecd870dc2201ef38c3`;
- implementation review commit: `6077e60bade10d300ac788a614a089b999486abe`.

Implementation regression:

- workflow run: `37119958661`;
- conclusion: `success`;
- Python runtime: 3.12;
- artifact ID: `11273086813`;
- artifact digest: `sha256:f2d38ba0db16323750f5e64456ca3f18edfd57d8ce1c4d365c33a73c0abd8e73`;
- deterministic implementation hash:
  `6db044c41297d0e9af3c526195cc314c8883ff38244541491ae3eef8662ac63d`;
- Revision 03 repeated-run causal hash:
  `877c157331dd09501c93291c5e427bf8ce4f3798db55a340adcc2ea30d609f6b`.

Validated causal controls:

- Prefix Invariance: PASS;
- Future-Timestamp Audit: PASS;
- Repeated-Run Determinism: PASS;
- Reference Checkpoint/Restart: PASS;
- Analysis-Island Reset: PASS.

### 19.3 Data Identity

Data Package Version:

`ASSET-P1-DATA-0.2.0`

Frozen Data Feed identities:

- repository: `rogerio-raposo/crypto-pro-datafeed`;
- producer branch: `experiment/asset-p1`;
- dataset-build code/run head: `f8d85435516d1eeb42085f7622296abfa4ea2ee2`;
- generated-manifest commit: `64b6489eda3b6a4e706f46dd18ed5d65d8991810`;
- package/documentation head: `cd461d999d56df6b441a3a571aa118a0b6d25d32`;
- Dataset Index blob SHA: `e1cf500310af3dfe1d9e3fc113353fca400c7764`;
- synchronized-gap registry blob SHA: `f8dc5c4244df931988487d24071253a1d3f51887`.

Dataset package:

- 24 asset×segment datasets;
- all dataset cell versions: `v0.2.0`;
- DEV, VAL and HOLDOUT packaged separately;
- Holdout manifests preserve `analytical_access = LOCKED`.

Dataset preparation workflow:

- run: `37097201212`;
- conclusion: `success`.

Artifacts:

- DEV ID `11263914965`, digest
  `sha256:ba0a89be052d2e765d98f6941f5689f347fda144e31ddde37ae21890ce394b09`;
- VAL ID `11264144472`, digest
  `sha256:adfb3bd046d45e3ad450fb2dc00c7e7c578bb92ce231f21814ee025775cd6d71`;
- HOLDOUT ID `11264369151`, digest
  `sha256:fb12740f8c1b4485d34e8d5033fb489d5f88ca224ec7a0243b574d6064ebae05`.

### 19.4 Gap / Analysis-Island Identity

Continuity diagnostic:

- run: `37096651289`;
- artifact ID: `11264686520`;
- digest:
  `sha256:bc6d5305382340ff9cf7c8a93e967eaf8ef5eeae0481bd1264cfee90bf9bbd5c`.

Only the synchronized venue gaps registered by Revision 01 are admissible.

No interpolation is permitted.

### 19.5 Human Review / Phase-Lock Identity

The frozen implementation includes:

- deterministic reviewer aliases;
- hashed review packages and completed review records;
- DEV Candidate Lock requiring Human Review SHA-256;
- VAL Provisional Lock chained to the DEV lock;
- HOLDOUT authorization only after valid DEV+VAL lock chain;
- prohibition on candidate mutation between locks.

Human Review tooling regression:

- package SHA-256:
  `760f41b4c221b48941bbeffaea8c589251cc8a9119625c245eece0555317c54e`;
- alias mapping SHA-256:
  `4b6d57592a46fa4b824232a3940bcabf1e854210543f8216062bc2a91d7f44b9`.

### 19.6 Freeze Rule

During formal P1 execution:

- code identity cannot change;
- Data Package identity cannot change;
- design rules cannot change;
- DEV reference-band rules cannot change;
- Holdout cannot be opened before valid DEV+VAL locks;
- a required retune produces `P1-REVISE`, not an in-place modification.

A material change invalidates this Execution Freeze and requires an explicit new freeze identity or experiment revision.

### 19.7 Manifest Integrity

The SHA-256 of this exact Execution-Frozen Manifest is calculated after commit and recorded externally in:

`P1_EXECUTION_FREEZE_RECORD.md`

This avoids a self-referential hash.

### 19.8 Formal Execution Status

`NOT STARTED`

The next authorized stage is formal DEV execution under the frozen phase sequence.
