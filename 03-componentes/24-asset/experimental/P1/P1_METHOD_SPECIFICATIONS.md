# Asset PRO — P1 Method Specifications

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

# 1. Common Causal Rules

All methods:

- consume closed candles only;
- maintain Candidate Swing separately from Confirmed Structural Swing;
- distinguish extremum timestamp from confirmation timestamp;
- freeze a confirmed swing;
- enforce High/Low alternation;
- preserve causal event time;
- expose ambiguity rather than use future information.

Primary confirmation basis for reversal methods:

> **Close-confirmed reversal against a High/Low candidate extremum.**

Intrabar confirmation is diagnostic-only in DEV and is not eligible for final candidate selection in this experiment.

---

# 2. M1 — Fixed-Window Pivot

A candidate High at bar (i) is confirmed only after (w) subsequent closed bars exist and the candidate is the unique maximum High inside the complete left/right window.

A candidate Low is the symmetric unique minimum.

Exact ties inside the window produce no confirmed M1 pivot for that window.

Confirmation timestamp:

> close time of the (w)-th right-side bar.

This deliberately exposes M1 latency rather than hiding it.

---

# 3. M2 — Fixed-Percentage Reversal

During an UP leg:

- candidate extremum = highest observed High;
- candidate updates causally when a new High is observed;
- confirmation occurs when a later Close satisfies:

[
(H^* - Close_t)/H^* \ge p
]

During a DOWN leg:

[
(Close_t - L^*)/L^* \ge p
]

where (H^*) or (L^*) is the active candidate extremum.

After confirmation, direction changes and the confirmed extremum is frozen.

---

# 4. M3 — Volatility-Normalized Reversal

During an UP leg:

[
H^* - Close_t \ge k \times V^*
]

During a DOWN leg:

[
Close_t - L^* \ge k \times V^*
]

where:

- (H^*/L^*) = active High/Low candidate;
- (V^*) = volatility reference observed causally at the candidate-extremum timestamp;
- candidate update refreshes both the extremum and its associated volatility reference;
- confirmed swing freezes extremum, volatility reference and confirmation timestamp.

Candidate volatility estimators:

- E1 — Wilder ATR using True Range;
- E2 — rolling median True Range.

M3 estimator screening occurs only in DEV.

---

# 5. Structural Comparator Volatility

To avoid giving M3 an exclusive structural-classification advantage, P1 uses a **method-independent comparison volatility** for equality, break-buffer and matching diagnostics:

> Wilder ATR(14), calculated causally on the same analytical timeframe.

This comparison ATR does not alter M1/M2 swing confirmation.

---

# 6. Structural Sequence

For same-type confirmed swings:

High relation:

- HH;
- EH;
- LH.

Low relation:

- HL;
- EL;
- LL.

Equality uses the structural Equality Tolerance profile defined in the Parameter Registry.

---

# 7. Regime

Candidate operational rules:

### Uptrend
Persistent alternating structural sequence without opposing relation, with at least the configured number of directional swing-pair confirmations and at least one strict upward relation.

### Downtrend
Symmetric downward rule.

### Range
At least two confirmed swing highs and two confirmed swing lows defining a bounded structure inside the active equality tolerance, without confirmed boundary break.

### Transition
Previous directional/range structure is lost or materially degraded, while a new qualifying regime is not yet established.

### Indeterminate
Insufficient or contradictory structural evidence.

Direct Uptrend ↔ Downtrend flip without Transition is prohibited and treated as structural inconsistency.

---

# 8. Protected Swing

Primary Protected Swing per timeframe:

- Uptrend → Protected Low;
- Downtrend → Protected High.

Promotion occurs only after a confirmed correction followed by a confirmed continuation structural break.

An internal swing break is not automatically a primary counter-structural break.

---

# 9. P1 Structural Events

- Breach — price excursion through structural reference;
- PCSB — closed-price structural break satisfying the active break-buffer profile;
- Continuation Break — PCSB in direction of current trend structure;
- Counter-Structural Break — PCSB through Primary Protected Swing against current trend;
- Reclaim — closed-price return through the broken reference using the same active buffer logic.

D3 Acceptance/Re-Acceptance is not inferred in P1.
