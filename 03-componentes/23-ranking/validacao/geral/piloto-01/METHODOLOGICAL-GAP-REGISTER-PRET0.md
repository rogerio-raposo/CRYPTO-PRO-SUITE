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
**Status:** OPEN — execution-quality defect identified

**Problem:** the original PRE-T0 Evidence Registry declared an evidence cut of 2026-10-01 but omitted the 2026-09-24 The Clearing House / Quant announcement, a clearly material pre-cut event.

**Impact:** material for QNT Exposure Confidence and potentially for other assets if similar omissions exist.

**Treatment:**
- preserve the original frozen registry;
- use the versioned QNT supplement rather than rewriting history;
- before T0, perform an explicit asset-by-asset Material Event Completeness Check for the full Run A sample;
- search at minimum primary project sources plus direct institutional/issuer counterparties over a defined recent window;
- record both positive and negative search results.

**Relation to BL-RANK-001:** this defect supports testing Critical Event Watch, but the immediate issue is evidence-pack completeness even within a single run.

**requires_method_change:** NO new construct. Operational evidence-control protocol must be strengthened before official T0 freeze.
---

## MGR-008 — AUM / Franchise-Mediated Token Value Thesis Gap

**Stage:** Relationship / Economic Capture / phenomenon alignment
**Status:** OPEN — diagnostic hypothesis registered

**Trigger:** ONDO PRE-T0 Materiality FAIL versus Ondo's observable leadership and institutional scale in tokenized RWAs/Treasuries.

**Problem:** the current Economic Capture construct privileges current explicit token-level transmission. It may under-represent cases where the project's institutional franchise, AUM scale/quality, distribution network and strategic control create market value through expected future monetization or governance option value before explicit token cash-flow rights exist.

**Verified context:** Ondo reported >USD 2.5bn TVL across tokenized products in January 2026, #1 positioning in tokenized Treasuries by TVL/holders/integrations, and subsequently >USD 1bn TVL in tokenized stocks with >70% reported market share. Institutional integrations include Franklin Templeton, Talos/Gate, Broadridge and institutional in-kind conversion infrastructure.

**User-raised thesis to test, not adopted as fact:** ONDO's token value thesis may be linked to the volume and institutional quality of AUM/flows captured by the Ondo franchise, particularly U.S.-Treasury and broader RWA tokenization.

**Distinction from MGR-006:**
- MGR-006: prospective institutional validation before materialization (QNT pattern);
- MGR-008: live institutional franchise/AUM with weakly explicit current token-level value transmission (ONDO pattern).

**Risk:** a Ranking designed to identify assets positioned to capture the next institutional flow may become too restrictive if it equates economically relevant prospective capture only with already-realized mandatory token economics.

**Anti-overfit treatment:** preserve ONDO `Exposure E4/C4`, `Capture E1/C3`, `Materiality CONFIRMED FAIL` in the frozen PRE-T0 result. No ONDO-specific promotion.

**Required test:** design a symmetric diagnostic for franchise/AUM-mediated prospective token capture across the Run A assets before deciding whether Economic Capture anchors need refinement or whether the information belongs in another construct/qualifier.

**requires_method_change:** UNDETERMINED. No methodology change authorized.