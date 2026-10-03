# Asset PRO — P1 Human Review Protocol

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

## 1. Role

Human review evaluates interpretability and diagnoses pathological structural behavior.

Human review does not override causal-integrity failures and does not select a winner by visual preference.

## 2. Blinding

Where operationally possible:

- method/profile identifiers are masked;
- reviewers receive identical chart scale and context;
- future bars outside the defined review window are hidden.

## 3. DEV and VAL Sampling

For every asset × timeframe × phase, select four review cases deterministically:

1. highest method/profile disagreement window;
2. highest regime-churn window;
3. highest structural-event-delay window;
4. a median diagnostic window selected chronologically from non-extreme cases.

With four assets, two timeframes and two reviewed phases (DEV and VAL), target review set:

> 64 cases.

## 4. Holdout Sampling

After provisional candidate lock, select two cases per asset×timeframe:

1. highest candidate disagreement;
2. chronological median non-extreme case.

Target:

> 16 Holdout review cases.

Holdout review cannot trigger retuning inside ASSET-P1-D1-001.

## 5. Review Questions

- Is the swing sequence interpretable under the stated rules?
- Is there clear microfragmentation?
- Are material legs omitted?
- Is Transition being used coherently?
- Is Protected Swing promotion defensible under its rule?
- Are structural events consistent with the documented reference?
- Is any apparent improvement dependent on future visual knowledge?

## 6. Reviewers

Preferred:

- at least two independent reviewers for a stratified subset.

If only one reviewer is available:

- findings remain diagnostic;
- subjective review cannot be used as a sole blocker or sole acceptance basis.

Inter-rater agreement is reported when two or more reviewers evaluate the same cases.


---

## 7. Design Freeze Revision 01 — Deterministic Review Windows

Human-review windows are presentation/sampling controls, not trading horizons.

### 7.1 Causal Review Context

Every review chart ends at the focal diagnostic timestamp. No future bars are displayed.

Trailing context:

- 4h: 120 evaluable bars;
- Daily: 90 evaluable bars.

A review window never crosses an Analysis-Island boundary.

If fewer bars exist in the current island, all available preceding bars are shown and the case is flagged `TRUNCATED_CONTEXT`.

### 7.2 Diagnostic Rolling Windows

The same trailing lengths are used when locating:

- highest method/profile disagreement;
- highest Regime Churn;
- highest structural-event delay.

Windows are evaluated only on complete analytical bars inside one Analysis Island.

### 7.3 Median Diagnostic Case

After excluding the three selected extreme cases in a DEV/VAL cell:

- rank remaining eligible windows by the primary diagnostic magnitude;
- choose the chronological earliest window at the median rank.

Ties at any selection stage are resolved by earliest focal timestamp.

### 7.4 Holdout Review

The Holdout review uses the same causal window lengths and tie rules.

No chart may expose bars after the focal timestamp.


---

## 8. Design Freeze Revision 02 — Review-Case Scoring

Review cases are selected from causal trailing windows only.

For DEV, eligible comparisons include the profiles permitted by the DEV analysis stage.

For VAL, only DEV-locked candidates are eligible.

For Holdout, only VAL-locked provisional candidates are eligible.

### 8.1 Disagreement Magnitude

For one review window:

[
Disagreement = \max(1-SwingStability_{pair})
]

across all eligible candidate/profile pairs with a valid BASE comparison in that window.

If no valid pair exists, the window is ineligible for the disagreement criterion.

### 8.2 Regime-Churn Magnitude

For one review window:

[
ChurnMagnitude = \max(RegimeChurn_{profile})
]

across eligible profiles.

### 8.3 Structural-Event-Delay Magnitude

For one review window, use the maximum absolute matched-event bar delay observed across eligible profile pairs under BASE event matching.

If no matched event exists, the window is ineligible for this criterion.

### 8.4 Selection Order and Uniqueness

Per asset×timeframe×phase cell, cases are selected in this fixed order:

1. highest Disagreement;
2. highest ChurnMagnitude among windows not already selected;
3. highest Structural-Event-Delay among windows not already selected;
4. median Disagreement window among remaining eligible windows.

Every tie is resolved by earliest focal timestamp.

If a criterion has no eligible remaining window, the case is omitted and explicitly labeled `NO_ELIGIBLE_CASE`; another criterion is not duplicated to preserve the target count.

## 9. Review Response Schema and Agreement

Each review question is answered using exactly:

- `YES`;
- `NO`;
- `INDETERMINATE`.

Free-text diagnostic notes are allowed but are not converted into scores.

With two or more reviewers, inter-rater agreement is reported as:

- exact-response agreement proportion per question;
- overall exact-response agreement proportion across all jointly reviewed question-items.

No agreement score can override a hard quantitative blocker.


---

## 10. Design Freeze Revision 03 — Review Timing and Blinding

### 10.1 DEV Review Population

DEV Human Review is generated **after** the quantitative candidate proposal and uses only the proposed candidate set.

It does not review the entire full-grid universe.

### 10.2 VAL/Holdout Review Population

- VAL: DEV-locked candidates only.
- Holdout: VAL-locked candidates only.

### 10.3 Blinded Aliases

For each review package:

1. compute SHA-256 of each canonical Profile ID;
2. sort candidates by that hash;
3. assign aliases `R01`, `R02`, ... in sorted order;
4. expose only aliases in reviewer-facing artifacts;
5. store the alias mapping separately and record its SHA-256.

Reviewers are not shown the detector method/profile identity in the review package.

### 10.4 Review Integrity Hash

Every completed review record receives a canonical SHA-256.

The applicable Human Review SHA-256 is recorded in the DEV or VAL lock.

A lock without the required review hash is invalid.
