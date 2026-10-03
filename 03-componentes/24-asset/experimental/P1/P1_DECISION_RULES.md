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
- it belongs to, or is necessary to characterize, a defensible local parameter plateau;
- cross-asset behavior is not pathologically unstable;
- confirmation delay is not disqualifying or is explicitly adjudicated;
- structural outputs are interpretable enough to proceed.

At most one Responsive, one Balanced and one Conservative profile per method/timeframe continue when available.

---

# 3. VAL Gate

VAL uses only DEV-locked candidates.

A candidate may proceed to Holdout when:

- all hard blockers remain passed;
- parameter/profile identity is unchanged;
- stability does not materially collapse outside DEV;
- no asset×timeframe cell shows recurrent structural inconsistency;
- human review does not reveal a rule-level defect.

VAL cannot retune parameters. A required retune causes P1-REVISE.

---

# 4. Holdout Gate

Holdout uses only VAL-locked provisional candidates.

Possible outcomes:

### Survives
Behavior remains within pre-registered stability/latency/structural guardrails.

### Rejected
Material failure appears without requiring ambiguity about implementation.

### Revision Required
Failure reveals a methodological issue that cannot be fixed without changing frozen rules.

No Holdout-driven parameter optimization is allowed.

---

# 5. Final P1 Decisions

### P1-PASS — Single Candidate
Exactly one architecture/profile remains defensible after Holdout.

### P1-PASS — Multiple Candidates
More than one candidate remains defensible and the evidence does not justify collapsing them into one.

### P1-REVISE
No candidate can be accepted without a methodological or parameter-design revision.

### P1-FAIL
The current D1 swing/structural architecture is not adequate for continuation.

P1 never reports an overall score or a “best return” winner.
