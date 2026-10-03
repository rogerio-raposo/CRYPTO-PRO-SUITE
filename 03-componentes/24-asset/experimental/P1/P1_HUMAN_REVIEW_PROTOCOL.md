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
