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

---

## MGR-006 — Prospective Institutional Validation / Future-Capture Gap

**Stage:** Relationship / Materiality
**Status:** OPEN — shadow diagnostic executed; integration decision deferred

**Trigger:** QNT exception review.

**Problem:** the current Economic Capture construct is anchored to demonstrable current token-level transmission. A systemically significant institutional selection can materially increase expected future adoption and market expectations before a current mandatory token-capture mechanism is observable.

**Controlled QNT result under unchanged rules:**
- Exposure = E3 / C4;
- Capture = E1 / C4;
- Materiality = Confirmed FAIL.

**Risk:** the Ranking may deliberately miss assets where institutional validation precedes realized token capture, even when that validation may be informative about the next institutional-flow regime.

**Anti-overfit treatment:** no QNT-specific rule change.

**Diagnostic:** apply `PROSPECTIVE-INSTITUTIONAL-VALIDATION-SHADOW-TEST.md` symmetrically to all Run A assets.

**Shadow-test result:** IV/PM/PTC appears to capture a distinct prospective-validation pattern for QNT (IV3 / PM2 / PTC1) that is not represented by Materiality alone. This is descriptive evidence, not proof of predictive value.

**Decision:** keep the diagnostic outside Ranking merit and Materiality. Revisit only after broader/outcome-oriented validation and Critical Event Watch testing.

**requires_method_change:** UNDETERMINED. No methodology change authorized.

---

## MGR-007 — Evidence Completeness / Material Event Retrieval Failure

**Stage:** Evidence Registry / Freshness control
**Status:** RESOLVED FOR PRE-T0 BASELINE — permanent control required at T0

**Problem:** the original PRE-T0 Evidence Registry declared an evidence cut of 2026-10-01 but omitted the 2026-09-24 The Clearing House / Quant announcement, a clearly material pre-cut event.

**Impact:** material for QNT Exposure Confidence and potentially for other assets if similar omissions exist.

**Treatment:**
- preserve the original frozen registry;
- use the versioned QNT supplement rather than rewriting history;
- before T0, perform an explicit asset-by-asset Material Event Completeness Check for the full Run A sample;
- search at minimum primary project sources plus direct institutional/issuer counterparties over a defined recent window;
- record both positive and negative search results.

**Relation to BL-RANK-001:** this defect supports testing Critical Event Watch, but the immediate issue is evidence-pack completeness even within a single run.

**Resolution:** the 12-asset Material Event Completeness Audit was executed under a separately frozen protocol. It found additional omitted evidence for PLUME, OP, ADA, LINK, ONDO, RSR, INJ and SYRUP, in addition to the previously corrected QNT case. APT, SUI and HYPE received no material-omission finding under the defined audit process.

Relationship decision changes from the audit:
- QNT: Exposure/Confidence correction already handled; Materiality unchanged FAIL;
- INJ: Capture Confidence C3 → C4; Materiality unchanged PASS;
- no other Relationship E-state or Materiality result changed.

Other material evidence was routed to the correct owner (notably ADA → future Accessibility/prospective validation; RSR → Frictions).

**T0 control:** the same completeness discipline must be repeated before the official T0 Evidence Pack freeze; PRE-T0 resolution does not waive that requirement.

**requires_method_change:** NO new construct. Operational evidence-control protocol adopted.
---

## MGR-008 — AUM / Franchise-Mediated Token Value Thesis Gap

**Stage:** Relationship / Economic Capture / phenomenon alignment
**Status:** RESOLVED — no methodology defect established for PCP-01

**Trigger:** ONDO PRE-T0 Materiality FAIL versus Ondo's observable leadership and institutional scale in tokenized RWAs/Treasuries.

**Resolution:** platform/franchise scale, institutional AUM and market leadership strengthen Exposure and may inform Structural Position, but they do not themselves demonstrate token-level Economic Capture.

Ondo Foundation currently identifies ONDO as a governance token. A June 2026 community fee-switch temperature check explicitly states that it is non-binding. A binding/executed fee switch was not verified at the PRE-T0 cut.

Therefore the frozen ONDO result remains:
- Exposure E4/C4;
- Capture E1/C3;
- Materiality CONFIRMED FAIL.

Future fee-switch approval/activation would constitute new evidence and could trigger a later reassessment prospectively. It is not back-projected into PCP-01.

**Implementation:** `ONDO-DIAGNOSTIC-RESOLUTION-PRET0.md`.

**requires_method_change:** NO.