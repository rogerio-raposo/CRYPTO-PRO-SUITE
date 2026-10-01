# PCP-01 — Material Event Completeness Audit Protocol — PRE-T0

**Status:** FROZEN BEFORE AUDIT RESULTS
**Date frozen:** 2026-10-01
**Scope:** all 12 Run A assets
**Purpose:** resolve MGR-007 before Structural Position

## 1. Audit window

Recent-material-event window:
`2026-08-02 through the PRE-T0 evidence cut on 2026-10-01`.

The 60-day window is a minimum completeness screen. Older evidence already present in the frozen Evidence Registry remains valid subject to its existing freshness rules.

## 2. Assets

`PLUME, OP, APT, ADA, SUI, LINK, QNT, ONDO, RSR, INJ, HYPE, SYRUP`

## 3. Mandatory search lanes per asset

At minimum:
1. official project/foundation newsroom/blog/docs;
2. official governance or token-economics source where relevant;
3. direct institutional/issuer/counterparty source for material announced partnerships or deployments when identifiable;
4. evidence of launches, committed deployments, regulatory/market-infrastructure integrations, token-economic changes, material security/governance events, or other developments plausibly able to change a frozen construct state or Confidence.

## 4. Material-event test

An event is material for this audit if, had it been included in the original pack, it could plausibly:
- change Exposure, Capture or Confidence;
- change a Materiality decision;
- require routing to Structural Position, Capacity, Frictions or Trajectory;
- change a shadow diagnostic such as IV/PM/PTC;
- reveal that the declared evidence cut was incomplete in a decision-relevant way.

Price appreciation, returns, market capitalization changes and trading-volume spikes are excluded from event qualification.

## 5. Outcome codes

- `NO_MATERIAL_OMISSION` — no relevant omitted event identified in the audit window.
- `SUPPLEMENT_NO_STATE_CHANGE` — omitted evidence should be added, but does not change the frozen Relationship state.
- `REASSESS_RELATIONSHIP` — omitted evidence can plausibly change Exposure/Capture state or Confidence.
- `ROUTE_OTHER_CONSTRUCT` — evidence is material but its primary owner is Capacity, Frictions, Position, Trajectory or another governed layer.
- `SHADOW_UPDATE` — evidence changes a non-decisional diagnostic but not current Ranking merit.

More than one code may apply.

## 6. Audit immutability

The original PRE-T0 Relationship Evidence Registry and Evaluator A file are not rewritten.

Any correction must be versioned as:
- asset supplement;
- controlled reassessment;
- routing note;
- shadow diagnostic correction.

## 7. Search-result discipline

Absence of a search hit is not evidence that no event exists. `NO_MATERIAL_OMISSION` means only that the defined audit process did not identify a material omitted event in the specified sources/window.

## 8. Completion gate

Structural Position may resume only after:
- all 12 assets receive an audit outcome;
- every `REASSESS_RELATIONSHIP` item is resolved;
- material evidence owned by another construct is routed and preserved;
- shadow diagnostics affected by omitted evidence are corrected in a versioned result.