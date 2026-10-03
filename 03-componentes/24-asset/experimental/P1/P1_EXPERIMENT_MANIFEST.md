# Asset PRO — P1 Experiment Manifest

**Status:** DESIGN FROZEN — REVISION 03 / NON-NORMATIVE  
**Experiment ID:** ASSET-P1-D1-001  
**Pilot:** P1 — D1 Structural Engine Validation  
**P0 dependency:** ASSET-P0-001 = PASS  
**Freeze status:** DESIGN FROZEN — REVISION 03 — IMPLEMENTATION IN PROGRESS

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

> **IN PROGRESS**

P1 Execution Freeze:

> **PENDING**

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
