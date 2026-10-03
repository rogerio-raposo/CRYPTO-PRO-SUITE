# Asset PRO — P1 Design Freeze Revision 03

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Date:** 2026-10-03  
**Revision:** Design Freeze Revision 03  
**Active baseline:** Original Design Freeze + Revisions 01, 02 and 03  
**Formal phase execution:** NOT STARTED

---

## 1. Trigger

Final implementation planning identified two process-level ambiguities that could otherwise affect selection:

- the exact timing/population of Human Review relative to DEV/VAL locks;
- the causal-validation contract required to authorize deterministic batch execution.

No formal DEV, VAL or Holdout output had been produced.

## 2. Revision 03 Manifest

Manifest commit:

`0a8ced601788cf89a41e2e62b5b74192a79c74a1`

Manifest blob SHA:

`e88496d3b1dbb10470c0f87c5440b46d229bc2fc`

## 3. Formal DEV Sequence

1. verify Execution Freeze;
2. M3 estimator screen on DEV;
3. full frozen profile grids on DEV;
4. metrics/plateau computation;
5. quantitative candidate proposal;
6. candidate DEV reference bands;
7. blinded DEV Human Review Set;
8. human review/adjudication;
9. final DEV Candidate Lock.

Human Review can remove a candidate only under frozen defect rules.

It cannot replace, retune or create candidates.

## 4. Formal VAL Sequence

1. verify DEV lock;
2. run DEV-locked candidates only;
3. compare against DEV reference bands;
4. blinded VAL review;
5. adjudicate/remove only;
6. VAL Provisional Lock.

## 5. Formal Holdout Sequence

1. verify chained DEV+VAL locks;
2. run VAL-locked candidates only;
3. compare against DEV bands;
4. blinded Holdout review;
5. final P1 Decision.

No Holdout retuning is permitted.

## 6. Review Blinding

Reviewer-facing packages use deterministic aliases:

- hash canonical Profile IDs;
- sort by hash;
- assign R01, R02, ...;
- keep mapping separate;
- hash completed review records.

DEV and VAL locks require the applicable Human Review SHA-256.

## 7. Causal Validation Contract

Before Execution Freeze the implementation must pass:

- prefix invariance;
- future-timestamp audit;
- repeated-run determinism;
- reference checkpoint/restart equivalence;
- Analysis-Island reset validation.

Previously confirmed historical outputs must remain immutable when future candles are added.

The reference checkpoint harness stores only already-revealed candles and frozen profile configuration. Restored state may be deterministically recomputed from that observed prefix.

Formal phase execution may use the batch engine only after these tests pass and because P0 has already validated the underlying historical causal replay environment.

## 8. M3 Intrabar Diagnostic

DEV-only, after estimator screening:

- n=14;
- k={1.5,2.0,3.0};
- surviving estimators only.

It is diagnostic-only and cannot enter final candidate selection.

## 9. Consequence

Implementation and Execution Freeze preparation must use Revision 03.

Formal P1 execution remains prohibited until Execution Freeze.

---

**End of Design Freeze Revision 03**
