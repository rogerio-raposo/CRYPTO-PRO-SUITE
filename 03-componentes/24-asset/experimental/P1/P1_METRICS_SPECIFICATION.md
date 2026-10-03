# Asset PRO — P1 Metrics Specification

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

## 1. Principle

Metrics are reported as a vector. No weighted composite score is permitted.

Metrics are stratified by:

- method/profile;
- asset;
- timeframe;
- phase/segment.

DEV is allowed to define empirical stability bands. VAL and Holdout may test those frozen bands but may not redefine them.

## 2. Swing Metrics

- Swing Count;
- Swing Density;
- Confirmation Delay;
- Normalized Confirmation Delay in bars;
- Swing Stability versus adjacent parameter profiles;
- Swing Fragmentation;
- Swing Omission.

## 3. Regime Metrics

- Regime Churn;
- Regime Duration distribution;
- Short-Lived Regime Rate;
- Transition Utilization;
- Direct Trend Flip Rate;
- Indeterminate Rate.

## 4. Protected Swing Metrics

- Protected Swing Turnover;
- Protected Swing Stability across adjacent profiles;
- time spent without valid Protected Swing when regime requires one.

## 5. Structural Event Metrics

For Breach, PCSB, Continuation Break, Counter-Structural Break and Reclaim:

- Event Count;
- Event Stability;
- Event Delay;
- event-order consistency.

D3-dependent Failed Break is excluded.

## 6. Robustness Metrics

- Parameter Plateau Width;
- Cross-Asset Stability;
- Cross-Timeframe Stability;
- Data-Anomaly Sensitivity;
- matching-sensitivity diagnostic stability.

## 7. Causal/Implementation Metrics

Hard binary checks:

- Causal Integrity;
- Determinism;
- Structural Invariant Integrity;
- no direct trend flip without Transition;
- no mutation of confirmed historical swing/event records.

Any failure of a hard binary check is a blocker.

## 8. DEV Plateau Detection

P1 deliberately avoids universal preselected stability thresholds such as 0.70 or 0.60.

For each method/timeframe, adjacent parameter profiles are compared component-by-component.

Primary plateau components:

- swing disagreement = `1 - Swing Stability`;
- Protected Swing disagreement = `1 - Protected Swing Stability`;
- structural-event disagreement = `1 - Event Stability`;
- absolute change in Regime Churn;
- absolute change in normalized Confirmation Delay.

For each component, DEV computes the distribution of adjacent-profile discontinuities.

A neighbor relation is considered **locally stable** when every applicable component is at or below its DEV robust upper fence:

[
Q3 + 1.5 \times IQR
]

computed within the same method/timeframe comparison family.

A candidate plateau requires:

- at least three connected profiles/cells;
- no hard blocker inside the candidate region;
- local-stability relations connecting the region;
- no single asset×timeframe cell with a structural invariant failure.

For one-dimensional grids (M1/M2), connectivity is adjacency in parameter order.

For M3, connectivity uses horizontal/vertical neighbors in the ((n,k)) grid for the same estimator.

No composite distance is calculated.

## 9. DEV Reference Bands

When a candidate is locked after DEV, the experiment freezes DEV reference bands for key metrics.

For metrics where **higher is more stable** (for example Swing Stability or Event Stability), the reference lower fence is:

[
Q1 - 1.5 \times IQR
]

For metrics where **lower is preferable as a diagnostic burden** (for example Regime Churn or Confirmation Delay), the reference upper fence is:

[
Q3 + 1.5 \times IQR
]

These fences are not claims of universal market truth. They are experiment-specific robustness expectations derived without using VAL or Holdout.

## 10. VAL / Holdout Stability Test

VAL and Holdout compare each frozen candidate against its DEV reference bands.

A metric outside a DEV reference fence is flagged as **material stability degradation**.

A single flagged metric is not automatically a rejection unless it represents a hard structural defect.

Repeated degradation across:

- multiple assets;
- both timeframes;
- or multiple structural layers

requires explicit adjudication and may lead to P1-REVISE or rejection.

No VAL/Holdout result may modify the DEV reference bands inside ASSET-P1-D1-001.

## 11. Responsiveness

Confirmation Delay is reported by median, IQR and p90.

No universal bar-count cutoff is imposed before DEV.

A candidate with delay above its DEV upper reference fence in VAL/Holdout is flagged for material responsiveness degradation.

This prevents choosing an arbitrary global latency threshold while still requiring out-of-sample stability.

## 12. Indeterminate State

Indeterminate Rate is treated as an epistemic diagnostic, not something to minimize mechanically.

Its DEV distribution is frozen per candidate.

Material VAL/Holdout expansion beyond the DEV upper reference fence is flagged and must be interpreted together with:

- data sufficiency;
- Transition behavior;
- structural ambiguity.

Missing data is never coded as neutral or negative evidence.
