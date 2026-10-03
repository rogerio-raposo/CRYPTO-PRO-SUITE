# Asset PRO — P1 Decision Rules

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

# 1. Hard Blockers

A method/profile is rejected or the run is invalid when any applicable condition occurs:

- look-ahead;
- nondeterministic replay/output;
- mutation of a confirmed historical swing/event;
- structural invariant violation;
- direct Uptrend↔Downtrend flip without Transition;
- unresolved source/data-integrity failure;
- inability to reproduce the frozen run identity.

Hard blockers cannot be compensated by soft metrics.

---

# 2. DEV Gate

A profile may continue from DEV only if:

- all hard blockers pass;
- it belongs to a connected local plateau under the frozen componentwise IQR rule;
- cross-asset behavior shows no recurrent structural-invariant defect;
- its latency/churn/Indeterminate behavior is documented;
- structural outputs are interpretable enough to proceed.

DEV freezes:

- selected candidate identities;
- DEV reference bands for stability, delay, churn and Indeterminate behavior;
- at most one Responsive, one Balanced and one Conservative candidate per method/timeframe when defensible.

These behavioral labels do not imply ranking.

---

# 3. VAL Gate

VAL uses only DEV-locked candidates and the DEV-frozen reference bands.

A candidate may proceed to Holdout when:

- all hard blockers remain passed;
- parameter/profile identity is unchanged;
- no recurrent material stability degradation appears across multiple assets or both timeframes;
- no rule-level defect is identified;
- human review does not reveal a reproducible structural inconsistency.

A VAL result that requires parameter change causes:

> `P1-REVISE`

rather than in-place retuning.

---

# 4. Holdout Gate

Holdout uses only VAL-locked provisional candidates.

Possible candidate outcomes:

### Survives
No hard blocker and no material pattern of out-of-band structural degradation requiring rule change.

### Rejected
A reproducible structural failure appears under the frozen rules.

### Revision Required
Observed failure exposes a methodological issue that cannot be resolved without changing frozen rules or parameters.

Holdout never changes DEV reference bands and never tunes parameters.

---

# 5. Adjudicating Material Degradation

A single out-of-band diagnostic does not automatically reject a candidate.

Material degradation is established when at least one of the following occurs:

- a hard blocker;
- the same structural metric degrades beyond its frozen DEV fence in at least two assets within the same timeframe;
- the same structural metric degrades beyond its frozen DEV fence in both timeframes for the same asset;
- multiple independent structural layers degrade concurrently in the same asset×timeframe cell;
- blinded human review identifies a reproducible rule-level defect consistent with quantitative diagnostics.

The adjudication must name the affected metric(s), cells and evidence. No aggregate score is used.

---

# 6. Final P1 Decisions

### P1-PASS — Single Candidate
Exactly one architecture/profile remains defensible after Holdout.

### P1-PASS — Multiple Candidates
More than one candidate remains defensible and evidence does not justify collapsing them into one.

### P1-REVISE
No candidate can be accepted without a methodological or parameter-design revision.

### P1-FAIL
The current D1 swing/structural architecture is not adequate for continuation.

P1 never reports an overall score or a “best return” winner.
