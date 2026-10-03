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


---

## 13. Design Freeze Revision 01 — Operational Metric Definitions

The following definitions are frozen for deterministic implementation.

### 13.1 Swing Density

[
SwingDensity = 1000 \times N_{swings}/N_{evaluable\ bars}
]

Reported together with raw Swing Count.

### 13.2 Swing Stability

For one-to-one matched swing sets A and B:

[
SwingStability = \frac{2M}{N_A+N_B}
]

where `M` is the number of matched pairs under the frozen matching specification.

If both sets are empty, stability is defined as 1.0.

### 13.3 Fragmentation and Omission Diagnostics

For a pairwise adjacent-profile comparison:

- the profile with higher Swing Density is the **higher-density** profile;
- `FragmentationIndicator = unmatched_high_density / N_high_density`;
- `OmissionIndicator = unmatched_low_density / N_low_density`.

If densities are equal, both unmatched rates are reported without assigning fragmentation/omission labels.

These are diagnostics, not ground-truth error rates.

### 13.4 Confirmation Delay

Per swing:

[
DelayBars = confirmation\_index - extremum\_index
]

Report median, IQR and p90.

### 13.5 Regime Churn

[
RegimeChurn = 1000 \times N_{regime\ changes}/N_{evaluable\ bars}
]

Analysis-island resets are not counted as regime changes.

### 13.6 Regime Duration

Duration is measured in evaluable bars within an Analysis Island.

No duration may span an island boundary.

### 13.7 Short-Lived Regime Rate

A regime episode is **short-lived** when it terminates before one additional completed structural cycle occurs after the cycle/event that established that regime.

[
ShortLivedRate = N_{short-lived\ episodes}/N_{completed\ regime\ episodes}
]

This is structural rather than based on an arbitrary fixed bar threshold.

### 13.8 Transition Utilization and Indeterminate Rate

[
TransitionUtilization = Bars_{Transition}/Bars_{evaluable}
]

[
IndeterminateRate = Bars_{Indeterminate}/Bars_{evaluable}
]

### 13.9 Direct Trend Flip Rate

Count any `TREND_UP → TREND_DOWN` or `TREND_DOWN → TREND_UP` change without an intervening Transition.

This is a hard invariant; the acceptable count is zero.

### 13.10 Protected Swing Turnover

[
ProtectedTurnover = 1000 \times N_{promotions}/Bars_{Trend}
]

### 13.11 Protected Swing Stability

Protected promotions are pair-matched only when:

- their underlying swings are matched by the BASE swing matcher;
- promotion timestamps are within the BASE timeframe bar-distance window.

Matching is one-to-one and monotonic.

[
ProtectedSwingStability = \frac{2M}{N_A+N_B}
]

If both promotion sets are empty, the value is reported as `NA`, not 1.0.

### 13.12 Time Without Valid Protected Swing

For each Trend episode, measurement begins only after the first valid Protected Swing promotion in that episode.

[
MissingProtectedRate =
Bars_{trend\ after\ first\ promotion\ with\ no\ active\ protected}/
Bars_{trend\ after\ first\ promotion}
]

If no promotion ever occurs in the episode, report `NA` plus the diagnostic `NO_PROTECTED_PROMOTION`.

### 13.13 Structural Event Matching

Two events are match-eligible when:

- event type is identical;
- reference kind is identical;
- event timestamps are within the BASE timeframe bar-distance window;
- normalized reference-price distance is ≤ 1.0 ATR14 at the later event timestamp.

Matching is one-to-one, monotonic and lexicographic using the same priority order as swing matching.

### 13.14 Event Stability and Delay

[
EventStability = \frac{2M}{N_A+N_B}
]

Matched-event delay is absolute occurrence-bar distance; report median, IQR and p90.

If both event sets are empty, Event Stability is reported as `NA`.

### 13.15 Event-Order Consistency

For the event-token sequences `(event_type, reference_kind)`, compute the Longest Common Subsequence length `LCS`.

[
EventOrderConsistency = \frac{LCS}{\max(N_A,N_B)}
]

If both sequences are empty, report `NA`.

### 13.16 Parameter Plateau Width

Plateau Width is the number of connected parameter profiles/cells in the frozen local-stability graph.

### 13.17 Cross-Asset / Cross-Timeframe Stability

No composite score is created.

For each core metric, report across the relevant asset/timeframe cells:

- median;
- IQR;
- minimum;
- maximum;
- flagged cells outside frozen DEV reference bands.

### 13.18 Data-Anomaly Sensitivity

Data-Anomaly Sensitivity is validated using controlled synthetic/reference perturbations, not by treating real missing data as negative evidence.

Report:

- invariant failures;
- swing/event count deltas;
- regime-state deltas;
- determinism status.

### 13.19 Matching-Sensitivity Diagnostic

For every comparison, report Swing Stability under:

- STRICT;
- BASE;
- WIDE.

The BASE result is primary. STRICT/WIDE are diagnostics only.
