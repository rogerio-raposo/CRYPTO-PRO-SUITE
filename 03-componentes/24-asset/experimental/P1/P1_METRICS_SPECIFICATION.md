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

## 8. Candidate Plateau Diagnostics

A detector/structural region is a candidate plateau when:

- at least three adjacent parameter profiles survive hard blockers;
- median adjacent-profile swing stability across asset×timeframe cells is at least 0.70;
- median Protected Swing stability is at least 0.60;
- median structural-event stability is at least 0.60;
- no asset×timeframe cell has swing stability below 0.50.

These are pre-freeze candidate thresholds and must be reviewed before Design Freeze. They are not outcome-optimized.

## 9. Responsiveness Guardrail

A candidate is flagged as pathologically delayed when confirmation-delay p90 exceeds:

- 20 bars on 4h; or
- 12 bars on Daily.

A flagged candidate may proceed only through an explicit pre-Holdout adjudication explaining why its structural stability justifies the latency.

## 10. Indeterminate Guardrail

If a candidate spends more than 60% of evaluable bars in Indeterminate state on the median asset×timeframe cell, it is flagged for P1-REVISE unless the behavior is shown to arise from intentional data sufficiency restrictions rather than structural incapacity.
