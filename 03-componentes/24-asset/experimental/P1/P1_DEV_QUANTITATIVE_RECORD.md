# Asset PRO — P1 DEV Quantitative Record

**Status:** AWAITING HUMAN REVIEW / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Phase:** DEV  
**Date:** 2026-10-03  
**DEV Candidate Lock:** NOT CREATED  
**VAL:** LOCKED  
**HOLDOUT:** LOCKED

---

## 1. Execution Baseline

Formal DEV used the frozen identities recorded by:

- `P1_EXECUTION_FREEZE_RECORD.md`;
- Specification: `ASSET-P1-D1-SPEC-REV03`;
- Code Version: `ASSET-P1-D1-CODE-0.1.0`;
- Data Package Version: `ASSET-P1-DATA-0.2.0`.

Frozen Manifest SHA-256:

`967f3e59772fca9d45aefa7679c4ba4abd091b3ba06f627a7ae0e7b97713e1f1`

## 2. Formal DEV Runs

Initial formal run:

- run ID: `37120970557`;
- Manifest verification: PASS;
- frozen DEV dataset reconstruction/verification: PASS;
- M3 estimator screen: PASS;
- six grid jobs completed successfully;
- M2/4h and M3-MEDIAN_TR/4h exceeded the 90-minute orchestration limit and were cancelled;
- cancellation was operational timeout, not methodological failure.

Recovery run:

- run ID: `37131101083`;
- conclusion: `success`;
- timed-out grids were partitioned by asset;
- all eight recovery partitions: PASS;
- final quantitative aggregation: PASS.

## 3. M3 Estimator Screen

Both frozen candidate estimators survived:

- `WILDER_ATR`;
- `MEDIAN_TR`.

No estimator was removed.

## 4. Grid / Hard-Blocker Outcome

All six method×timeframe families produced valid plateau/candidate output.

Notable hard-blocker finding:

- M2/4h: 36 profiles were hard-blocked;
- all 36 belonged to `p=1.0%` or `p=1.5%` detector families across structural-grid combinations;
- none of the three proposed M2/4h representatives is hard-blocked.

No proposed candidate carries a recorded hard blocker.

## 5. Quantitative Candidate Proposal

Proposed candidates:

`18`

The proposal contains one Responsive, Balanced and Conservative representative for each method×timeframe family:

- M1 / 4h;
- M1 / Daily;
- M2 / 4h;
- M2 / Daily;
- M3 / 4h;
- M3 / Daily.

Quantitative proposal SHA-256:

`cec4979663e9c1030a17472805894602f18dfd99a7a4248837032bd25cfd7195`

Metrics-reference SHA-256:

`280dd3554cf567c14dc305c4d6b37be63af4489f168b3763693d2cc3b97cd494`

Quantitative summary SHA-256:

`f4a414b313ea816609d2c6d77b08578691e071f2112586347bfca20ea4b05497`

Quantitative artifact:

- ID: `11278470145`;
- digest:
  `sha256:4be2191194cac19168ff243b851ad586b32f19c34763240b4cdbe8deb794febf`.

## 6. Blinded DEV Human Review Set

Generated review sets:

`8`

Selected cases:

`32`

Review-manifest SHA-256:

`65c0a17ea60b64404d2eaf9861367b194599564868a39b30c6a7143ce603ca46`

Reviewer-facing package artifact:

- ID: `11277727121`;
- digest:
  `sha256:fdc47ac69de3d0c542684fa17deebe93366b0d242e3478855c086084ee2b4138`.

Separate blinded-alias mapping artifact:

- ID: `11278155725`;
- digest:
  `sha256:a1234f3dea5fb03ccc545279b28cfc96c7c87c365361c3ab6a675ae2b8992145`.

## 7. AI-Assisted Diagnostic Pre-Review

An AI-assisted diagnostic inspection was performed only to identify implementation/rule anomalies before requesting the mandatory Human Review.

It does **not** satisfy the frozen Human Review requirement and is not the Human Review SHA used by a candidate lock.

Findings:

- no swing-alternation defect observed in the 32 cases;
- no future-context exposure observed;
- observed structural events were price/reference consistent;
- observed Protected Swing promotions matched their continuation-break trigger;
- responsive representatives visibly produce denser swing sequences;
- conservative representatives visibly omit more minor/intermediate legs, consistent with their behavioral label;
- an apparent BTC 4h direct trend flip was investigated and found to contain a same-timestamp intermediate `TRANSITION` after Counter-Structural Break; therefore it is not a direct flip *without* Transition.

No confirmed rule-level defect was established by this diagnostic.

## 8. M3 Intrabar Diagnostic

Revision 03 diagnostic run:

- run ID: `37161629487`;
- conclusion: `success`;
- artifact ID: `11287488440`;
- artifact digest:
  `sha256:5c329829df0c3918ae8568ec58cec616ba43e1c41246caf48b447bcf96de4288`;
- result SHA-256:
  `021fa592d0da274e6fe05ae1e16ded91f3c613f89b1c790171d83ffb86ee036b`.

Observed behavior:

- intrabar detection produced materially more swings than Close-confirmation across all frozen diagnostic combinations;
- intrabar processing also produced substantial `AMBIGUOUS_INTRABAR_SEQUENCE` observations;
- this does not promote an intrabar profile;
- no evidence requires changing the frozen primary Close-confirmation architecture.

Current adjudication:

> **NO P1-REVISE trigger from the intrabar diagnostic.**

## 9. Mandatory Stop Point

Revision 03 requires:

> quantitative proposal → frozen DEV reference bands → blinded DEV Human Review → adjudication → final DEV Candidate Lock.

The quantitative proposal and DEV reference bands are complete.

The blinded packages are complete.

The mandatory **Human Review has not yet been completed by a human reviewer**.

Therefore:

> **DEV Candidate Lock cannot yet be created.**

VAL and HOLDOUT remain locked.

---

**End of P1 DEV Quantitative Record**
