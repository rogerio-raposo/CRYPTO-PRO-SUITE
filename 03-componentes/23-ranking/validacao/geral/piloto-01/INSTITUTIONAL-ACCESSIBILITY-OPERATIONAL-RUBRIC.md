# PCP-01 — Institutional Accessibility Operational Rubric

**Status:** FROZEN BEFORE CAPACITY ASSESSMENT
**Context:** RIP-01 — Direct Digital-Asset-Capable Professional Allocator (DDAPA)

## Definition

Accessibility is the degree to which RIP-01 has usable channels to acquire, custody, move, administer and settle direct spot exposure to the asset.

## Required propositions

### A1 — Execution Access
A current spot acquisition/disposal route exists on at least one QEV usable under the pilot source configuration.

### A2 — Custody / Holding Path
A professional allocator can hold the economic asset through an institutional-grade or professionally controlled custody/self-custody arrangement consistent with RIP-01.

### A3 — Settlement / Transferability
The asset can be transferred/settled through a current operational path without a present blocker that makes normal acquisition, custody or exit impracticable.

### A4 — Access Resilience
The access path is not demonstrably dependent on a single fragile operational condition whose current failure would make the complete path unusable. Redundancy strengthens higher states but is not universally required for E2.

## Semantic anchors

- `E0` — no current complete institutional access path.
- `E1` — partial, exceptional or materially fragile path; at least one essential leg is not operationally viable.
- `E2` — at least one complete current path satisfies execution + holding + transfer/settlement for RIP-01, with no identified present blocker.
- `E3` — robust institutional accessibility with meaningful redundancy and/or broad institutional infrastructure plus demonstrated operational persistence.
- `E4` — deeply institutionalized and highly redundant access across multiple independent execution/custody/settlement channels with strong persistence.
- `IND` — evidence is insufficient or materially conflicting.

## Gate rule

Capacity confirmation requires Accessibility >= E2 with C3+.

Execution listing alone cannot establish E2. Likewise, a future custody integration cannot be counted as current access.

## Evidence ownership

- current market availability → Accessibility;
- current custody/transfer path → Accessibility;
- prospective delisting/counterparty/regulatory vulnerability beyond current operation → Frictions;
- market depth/slippage/turnover → Absorption, not Accessibility.

## Assessment timing

Accessibility evidence may be prepared PRE-T0 but must pass freshness/event checks at T0 before final Capacity confirmation.