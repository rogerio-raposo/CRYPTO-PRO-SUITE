# Asset PRO — P1 / D1 Structural Validation

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**P0 dependency:** SATISFIED — ASSET-P0-001 PASS  
**Execution status:** NOT STARTED

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

No P1 analytical code is implemented before Design Freeze.

After Design Freeze, implementation proceeds toward a separate Execution Freeze. No formal P1 run is authorized before Execution Freeze.
