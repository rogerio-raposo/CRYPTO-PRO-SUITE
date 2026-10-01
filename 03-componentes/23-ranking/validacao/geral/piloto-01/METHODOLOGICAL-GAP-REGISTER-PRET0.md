# PCP-01 — Methodological Gap Register — PRE-T0

**Status:** OPEN  
**As-of:** 2026-10-01

## MGR-001 — Structural Position reference-universe ambiguity

**Status:** RESOLVED — 2026-10-01

**Decision:**
Structural Position uses the full **CA-PASS Functional Reference Class within SMU-PCP01**, not the deterministic Run A sample and not a Materiality-PASS-only subset.

**Rationale:**
- sampling must not alter an economic relative-position construct;
- Economic Capture must not determine who exists in the Position comparator landscape;
- CA-IND/FAIL lack validated relation to FV-01;
- external comparators outside the governed SMU cannot be introduced ad hoc.

**Implementation:**
- `STRUCTURAL-POSITION-REFERENCE-RULE.md`
- `REFERENCE-COMPARATOR-PROFILE-SCHEMA.md`
- `POSITION-REFERENCE-CENSUS.md`

**requires_method_change:** RESOLVED by operational clarification; no new construct introduced.

---

## MGR-002 — Independent inter-rater assessment not yet available

**Stage:** Relationship reproducibility validation  
**Problem:** Evaluator A assessment is complete, but no independent Evaluator B has yet assessed the same frozen evidence pack without seeing A's states.

**Impact:** reproducibility metrics cannot yet be calculated.

**Temporary treatment:** preserve Evaluator A as immutable first pass. Do not manufacture a second "independent" rating inside the same informed analytical pass.

**requires_method_change:** NO. Requires a genuinely independent reviewer/session.

---

## MGR-003 — T0 not yet declared

**Stage:** Evidence freeze / official Run A  
**Problem:** the current Relationship pack precedes the official T0 because the Capacity capture pipeline has not completed the temporal dry-run/UFT process.

**Impact:** current states are PRE-T0 baseline states, not final Run A states.

**Temporary treatment:** freeze this baseline; at T0 run a Freshness/Event Gate and append only evidence with effective/published time <= T0. Preserve both baseline and final states.

**requires_method_change:** NO. This is a sequencing/governance issue.

---

## MGR-004 — Gas-token materiality calibration

**Stage:** Economic Capture  
**Problem:** APT, ADA, SUI and PLUME expose a recurring methodological question: required gas establishes a causal pathway but does not itself prove economically material capture.

**Impact:** material; can change Materiality PASS/FAIL.

**Current treatment:** apply the existing E1→E2 boundary:
- required gas only = insufficient for E2;
- E2 needs evidence that vector-related activity has an economically relevant transmission through gas/security/storage/burn;
- uncertainty is expressed through Confidence/Provisional status, not automatic promotion.

**requires_method_change:** NO at this stage. Retain as a pilot diagnostic and test whether later empirical data requires tighter anchors.

---

## MGR-005 — Position is bounded by Supported Market Universe coverage

**Stage:** Structural Position

**Problem:** SMU-PCP01 currently begins from Binance-supported spot assets. A globally important FV-01 comparator outside the supported universe would not enter the PCP-01 Position Reference Universe.

**Impact:** potentially material for claims of global leadership.

**Treatment:**
- Position is explicitly labeled as relative to the `PCP-01 PRU`;
- no global-leadership claim is permitted;
- no external comparator is added ad hoc after freeze;
- later Data Feed/source expansion can test coverage sensitivity in a separate run.

**requires_method_change:** NO for PCP-01. This is a coverage limitation and future sensitivity-test requirement.
