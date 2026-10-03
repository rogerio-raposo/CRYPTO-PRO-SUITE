# Asset PRO — P1 Historical Segment Registry

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

## 1. Principle

Segments are selected before method execution and are identical across assets to reduce discretionary chart selection.

Descriptive regime labels are sampling descriptors only. They are not algorithmic ground truth.

## 2. Segments

| ID | Phase | Start UTC inclusive | End UTC exclusive | Sampling purpose |
|---|---|---|---|---|
| DEV-01 | DEV | 2021-01-01 | 2021-07-01 | expansion, correction, elevated volatility |
| DEV-02 | DEV | 2022-06-01 | 2022-12-01 | persistent decline, transition, volatility shock |
| VAL-01 | VAL | 2023-01-01 | 2023-07-01 | recovery/transition and mixed directional structure |
| VAL-02 | VAL | 2023-07-01 | 2024-01-01 | range/mixed structure followed by expansion |
| HOLD-01 | HOLDOUT | 2024-01-01 | 2024-07-01 | unseen-to-tuning structural validation |
| HOLD-02 | HOLDOUT | 2024-07-01 | 2025-01-01 | unseen-to-tuning structural validation |

## 3. Holdout Discipline

Holdout is **operationally blind**, not historically unknowable.

Before Holdout is opened:

- candidate profiles must be locked;
- blocker rules must be locked;
- metrics must be locked;
- no tuning based on Holdout outputs is allowed.

If Holdout reveals a material failure requiring parameter change:

> ASSET-P1-D1-001 does not retune in place; it moves to P1-REVISE and a revised experiment identity is required.

## 4. Source Eligibility

Every asset must demonstrate continuous eligible Binance Spot historical data for every segment before Design Freeze.

If one instrument lacks a required segment:

- do not silently shorten that asset;
- either revise the common segment before freeze or replace the asset through an explicit design revision.
