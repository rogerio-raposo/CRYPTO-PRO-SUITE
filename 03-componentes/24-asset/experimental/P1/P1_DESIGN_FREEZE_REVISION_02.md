# Asset PRO — P1 Design Freeze Revision 02

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Date:** 2026-10-03  
**Revision:** Design Freeze Revision 02  
**Active baseline:** Original Design Freeze + Revision 01 + Revision 02  
**Formal phase execution:** NOT STARTED

---

## 1. Trigger

Implementation regression after Revision 01 exposed remaining design ambiguities that could materially affect candidate selection or stability measurement:

- comparator ATR14 is unavailable for some early confirmed swings/events;
- quantile/IQR interpolation had not been fixed;
- adjacency of complete detector+structural profiles had not been fully specified;
- Responsive/Balanced/Conservative representative selection was not deterministic;
- DEV reference-band metric sets and cell aggregation required exact definitions;
- Human Review case magnitudes/ties required deterministic rules;
- M1 simultaneous dual pivot and M3 intrabar diagnostic ordering required explicit treatment.

These were discovered before any formal DEV, VAL or Holdout method execution.

## 2. Prior Freeze References

Original Design Freeze Manifest:

`9e234e1d5d5975ffc111309a7eafaf345e670cc7`

Revision 01 Manifest:

`dd36c1f2e5dbf080efab5230d5e9edeadb638b4e`

Revision 01 Record:

`a4b7dd619d8298059f0ec73f2fd950b37c8331f0`

All remain immutable historical evidence.

## 3. Revision 02 Manifest

Revised Manifest commit:

`a3d532988d37f796c81c183d8707ecb17be5a67a`

Manifest blob SHA:

`f8338f5d828693a7983f2d6cba68158586f97142`

Revision 02 becomes the active design baseline together with Revision 01.

## 4. Comparator Warm-Up

ATR14-normalized comparison excludes:

- swings whose own confirmation timestamp precedes ATR14 initialization;
- events whose own event timestamp precedes ATR14 initialization;
- Protected Swing promotions whose underlying swing is comparison-ineligible.

These objects remain valid D1 outputs. They are excluded only from comparison universes and stability denominators.

Matching remains island-local.

## 5. Quantile Convention

All experiment quantiles use deterministic Type-7 linear interpolation.

Frozen statistics:

- Median = Q0.50;
- Q1 = Q0.25;
- Q3 = Q0.75;
- IQR = Q3-Q1;
- p90 = Q0.90.

A DEV fence requires at least four valid observations after NA exclusion.

## 6. Full-Profile Adjacency

Plateau graphs use complete profile coordinates:

- M1: (w,q,b,m);
- M2: (p,q,b,m);
- M3: (estimator,n,k,q,b,m).

Profiles are neighbors only if exactly one ordered coordinate moves by one grid step.

M3 estimator identity is not an adjacency axis.

## 7. DEV Plateau Statistics

For one method/timeframe:

- DEV cells = 4 assets × 2 DEV segments = 8;
- each neighbor-pair component is calculated in each cell;
- Analysis-Island numerators/denominators are aggregated inside the cell without cross-island objects;
- neighbor component = Type-7 median across valid DEV cells;
- robust upper fence = Q3 + 1.5×IQR across neighbor-pair component values;
- a local-stability edge requires all applicable component values within their valid fences and no hard blocker;
- a plateau requires at least three connected profiles.

No composite distance is used.

## 8. Behavioral Candidate Selection

Candidates are selected only from profiles inside qualifying plateaus.

Pooled DEV Swing Density = Type-7 median across the eight DEV cells.

Rules:

- if all eligible densities are identical: one Balanced candidate, lexicographically smallest Profile ID;
- otherwise: Conservative = minimum density; Responsive = maximum density;
- Balanced exists only if a density strictly between the two extremes exists and is selected nearest to the pooled-density median;
- ties use lexicographically smallest canonical Profile ID.

Labels are behavioral, not evaluative.

## 9. DEV Reference Bands

Revision 02 freezes:

- exact single-profile metrics;
- exact pairwise candidate metrics;
- lower/upper/two-sided fence direction;
- candidate/candidate-pair identity of the reference distribution;
- minimum four valid observations;
- VAL/Holdout cell-flag semantics.

No VAL/Holdout result may alter a DEV fence.

## 10. Human Review

Revision 02 freezes:

- disagreement magnitude = maximum pairwise 1-SwingStability;
- churn magnitude = maximum profile Regime Churn;
- event-delay magnitude = maximum absolute matched-event delay;
- fixed case-selection order;
- unique-window constraint;
- earliest-time tie-break;
- YES/NO/INDETERMINATE response vocabulary;
- exact-response inter-rater agreement.

Review remains diagnostic and cannot override hard blockers.

## 11. Detector Edge Cases

### M1
A center candle that is simultaneously unique maximum High and unique minimum Low in its window is:

`AMBIGUOUS_DUAL_PIVOT`

No pivot is confirmed.

### M3 intrabar diagnostic
Uses closed-candle High/Low range against the frozen candidate extremum/volatility threshold.

If the same candle creates a strict new candidate extremum and would also satisfy opposite intrabar reversal:

`AMBIGUOUS_INTRABAR_SEQUENCE`

No swing confirms on that candle.

The intrabar variant remains diagnostic-only and final-candidate ineligible.

## 12. Consequence

Implementation and Execution Freeze preparation must use Revision 02.

Formal P1 DEV/VAL/HOLDOUT execution remains prohibited until Execution Freeze.

---

**End of Design Freeze Revision 02**
