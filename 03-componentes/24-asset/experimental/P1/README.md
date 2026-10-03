# Asset PRO — P1 / D1 Structural Validation

**Status:** EXECUTION FROZEN / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**P0 dependency:** SATISFIED — ASSET-P0-001 PASS  
**Implementation status:** VALIDATED  
**Execution Freeze:** COMPLETE  
**Formal DEV execution:** NOT STARTED

---

## Purpose

P1 evaluates candidate causal swing-detection architectures and their ability to support a stable, interpretable D1 structural state.

P1 does not evaluate trading returns or predictive profitability.

## Phase Model

`DEV → candidate lock → VAL → provisional candidate lock → Structural Holdout → P1 Decision`

Holdout results may not be used for parameter retuning.

## Package

- `P1_EXPERIMENT_MANIFEST.md`
- `P1_SEGMENT_REGISTRY.md`
- `P1_METHOD_SPECIFICATIONS.md`
- `P1_PARAMETER_PROFILE_REGISTRY.md`
- `P1_MATCHING_SPECIFICATION.md`
- `P1_METRICS_SPECIFICATION.md`
- `P1_HUMAN_REVIEW_PROTOCOL.md`
- `P1_DECISION_RULES.md`
- `P1_FREEZE_CHECKLIST.md`
- `P1_DESIGN_FREEZE_RECORD.md`
- `P1_DESIGN_FREEZE_REVISION_01.md`
- `P1_DESIGN_FREEZE_REVISION_02.md`
- `P1_DESIGN_FREEZE_REVISION_03.md`
- `P1_IMPLEMENTATION_REVIEW.md`
- `P1_EXECUTION_FREEZE_RECORD.md`

Design Freeze is complete.

The next phase is implementation toward a separate Execution Freeze. No formal P1 run is authorized before Execution Freeze.


## Active Design Baseline

The original Design Freeze remains historical evidence.

Active implementation baseline:

> **Original Design Freeze + Revision 01 + Revision 02 + Revision 03**

Revision 01 adds synchronized-venue-gap Analysis Islands. Revision 02 fixes comparator warm-up, statistical conventions, plateau/candidate-lock and deterministic sampling. Revision 03 fixes formal DEV/VAL/HOLDOUT stop points, review-lock integrity and causal-validation preconditions.


## Implementation Validation

Producer/data preparation and the D1 implementation have completed pre-freeze validation.

Execution Freeze is complete. Formal DEV is authorized under Revision 03. VAL and HOLDOUT remain locked behind their required phase locks.
