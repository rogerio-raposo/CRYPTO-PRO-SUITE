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


---

## 14. Design Freeze Revision 02 — Statistical Convention

All experiment quantiles use deterministic linear interpolation equivalent to the R/NumPy Type-7 convention.

For sorted observations (x_0,\dots,x_{N-1}) and percentile (p\in[0,1]):

[
h=(N-1)p
]

[
Q_p=x_{\lfloor h\rfloor}+(h-\lfloor h\rfloor)
(x_{\lceil h\rceil}-x_{\lfloor h\rfloor})
]

For (N=1), (Q_p=x_0).

Definitions:

- Median = (Q_{0.50});
- Q1 = (Q_{0.25});
- Q3 = (Q_{0.75});
- IQR = Q3 − Q1;
- p90 = (Q_{0.90}).

A DEV reference fence requires at least four valid observations after NA exclusion. Otherwise its status is `INSUFFICIENT_REFERENCE` and it cannot be used to establish material degradation.

Bounded-rate fences are clipped to their natural domain ([0,1]). Non-negative unbounded metric lower fences are clipped at zero.

## 15. Full Parameter-Profile Adjacency Graph

Plateau detection operates on **complete detector+structural profiles**.

For each method/timeframe, two profiles are adjacent only when exactly one ordered parameter coordinate moves by one grid step and every other coordinate is identical.

Axes:

### M1
((w,q,b,m))

### M2
((p,q,b,m))

### M3
((estimator,n,k,q,b,m))

M3 adjacency never crosses estimator identity. Estimator screening precedes the full-grid graph.

## 16. DEV Cell Definition and Neighbor Statistics

For a fixed timeframe, the DEV cell set is:

[
4\ assets \times 2\ DEV\ segments = 8\ cells
]

Each cell may contain multiple Analysis Islands; island-level numerators/denominators are aggregated according to the metric definition before producing one cell value.

For every adjacent profile pair and every plateau component:

1. compute the component separately in each of the 8 DEV cells;
2. exclude NA cells only where the component is genuinely not applicable;
3. compute the pair's component value as the Type-7 median across valid DEV cells.

Across all adjacent profile pairs in the same method/timeframe family, compute the component robust upper fence:

[
Q3 + 1.5\times IQR
]

A neighbor edge is locally stable when:

- both profiles pass all hard blockers; and
- every applicable component with a valid fence is at or below that fence.

A candidate plateau is a connected component of at least three profiles in this locally-stable graph.

## 17. Deterministic Behavioral Representatives

Candidate labels describe behavior only and are not quality grades.

For every method/timeframe:

1. take the union of profiles belonging to qualifying plateaus;
2. compute each profile's pooled DEV Swing Density as the Type-7 median of its 8 DEV cell Swing Densities;
3. if all eligible profiles have identical pooled density, retain one `Balanced` representative using lexicographically smallest canonical Profile ID;
4. otherwise:
   - `Conservative` = lowest pooled Swing Density;
   - `Responsive` = highest pooled Swing Density;
   - `Balanced` = eligible profile with density closest to the Type-7 median pooled density, but only when a profile exists strictly between Conservative and Responsive densities.
5. all ties are resolved by lexicographically smallest canonical Profile ID.

Thus no candidate is chosen by return, outcome success or composite score.

## 18. Canonical Profile ID

Profile IDs are deterministic and include all active coordinates in fixed order.

Examples:

- `M1-TF4H-w3-q0.50-b0.25-m2`;
- `M2-TF1D-p0.05-q0.25-b0-m3`;
- `M3-TF4H-WILDER_ATR-n14-k2.0-q0.50-b0.25-m2`.

Equivalent numeric values must serialize identically.

## 19. Frozen DEV Reference-Band Set

Reference bands are computed after DEV candidate lock.

### Single-profile metrics

Two-sided robust fences:
- Swing Density;
- Transition Utilization;
- Protected Swing Turnover, when applicable;
- Event Density by event type.

Upper-fence-only:
- Confirmation Delay median;
- Confirmation Delay p90;
- Regime Churn;
- Short-Lived Regime Rate;
- Indeterminate Rate;
- Missing Protected Swing Rate, when applicable.

### Pairwise candidate metrics

Lower-fence-only:
- Swing Stability;
- Protected Swing Stability, when applicable;
- Event Stability, when applicable;
- Event Order Consistency, when applicable.

Upper-fence-only:
- Fragmentation Indicator;
- Omission Indicator.

STRICT/WIDE matching-sensitivity results remain diagnostic and do not create independent acceptance fences.

## 20. Candidate and Candidate-Pair Reference Bands

Single-profile bands are frozen per:

- candidate;
- timeframe;
- metric.

Pairwise bands are frozen per:

- ordered canonical candidate pair;
- timeframe;
- metric.

The 8 DEV asset×segment cell values form the reference distribution.

If fewer than four valid cell values exist, the reference status is `INSUFFICIENT_REFERENCE`.

## 21. VAL/Holdout Flag Semantics

VAL/Holdout is evaluated at the asset×segment×timeframe cell level.

A cell flag occurs when a metric crosses its applicable frozen DEV fence.

For the existing material-degradation rule:

- "at least two assets within the same timeframe" means at least two distinct assets each have one or more flagged segments for that same metric/timeframe;
- "both timeframes for the same asset" means that asset has at least one flagged segment in 4h and at least one flagged segment in Daily for the same metric;
- "multiple structural layers in the same cell" means two or more independent metric families flag in the same asset×segment×timeframe cell.

No VAL/Holdout observation may alter a DEV fence.

## 22. Event Density

For each structural event type:

[
EventDensity = 1000\times N_{events}/N_{evaluable\ bars}
]

Analysis-Island resets are not events.
