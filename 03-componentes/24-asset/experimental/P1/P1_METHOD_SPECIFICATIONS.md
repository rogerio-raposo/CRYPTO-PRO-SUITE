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

Dataset-edge rule:

> if a method lacks the required past or future-confirmation bars inside the currently visible segment, no swing is confirmed from unavailable information.

---

# 2. M1 — Fixed-Window Pivot

A candidate High at bar (i) is confirmed only after (w) subsequent closed bars exist and the candidate is the unique maximum High inside the complete ((2w+1))-bar left/right window.

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

### E1 — Wilder ATR
- True Range uses the standard maximum of High-Low, |High-prevClose| and |Low-prevClose|;
- initialization = arithmetic mean of the first (n) valid True Range observations;
- subsequent values use Wilder recursive smoothing;
- no ATR value exists before initialization is complete.

### E2 — Median True Range
- same causal True Range definition;
- rolling median of the last (n) valid True Range observations;
- no value exists before the complete window is available.

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

## Equality reference

When a newly confirmed same-type swing (S_2) is compared with prior swing (S_1):

[
Tolerance = q \times ATR14_{confirm(S_2)}
]

The ATR value is sampled at (S_2)'s confirmation timestamp and is frozen for that relation classification.

Thus equality is causal and cannot be recomputed later using future volatility.

---

# 7. Directional Structural Cycles

A **completed structural cycle** contains one newly classified High relation and one newly classified Low relation since the previous completed cycle.

### Up-qualifying cycle
- High relation ∈ {HH, EH};
- Low relation ∈ {HL, EL};
- at least one of the two relations is strict directional evidence: HH or HL.

### Down-qualifying cycle
- High relation ∈ {LH, EH};
- Low relation ∈ {LL, EL};
- at least one is strict directional evidence: LH or LL.

Any opposing strict relation prevents that cycle from qualifying in the candidate direction.

The active directional-cycle count resets when an opposing structural relation invalidates continuity.

---

# 8. Regime

### Uptrend
Established after (m) consecutive Up-qualifying completed structural cycles with no intervening opposing strict relation.

### Downtrend
Established after (m) consecutive Down-qualifying completed structural cycles with no intervening opposing strict relation.

### Range
Requires:

- at least two confirmed structural Highs;
- at least two confirmed structural Lows;
- alternating High/Low swing sequence;
- High references mutually contained by the active equality tolerance;
- Low references mutually contained by the active equality tolerance;
- no active directional regime;
- no confirmed PCSB outside the active range boundary.

### Transition
Used when:

- a prior Trend loses Protected Swing integrity;
- a Range suffers PCSB outside its boundary;
- or previous regime requirements are materially lost while a new regime is not established.

### Indeterminate
Used when:

- structural history is insufficient;
- comparator volatility is unavailable;
- or relations are contradictory without a defensible Transition state.

Direct Uptrend ↔ Downtrend flip without Transition is prohibited and treated as structural inconsistency.

---

# 9. Structural Reference and Break Buffer

When a structural swing/range boundary becomes an active break reference:

- reference price is frozen;
- comparator `ATR14_ref` is sampled at activation and frozen;
- break buffer is:

[
Buffer = b \times ATR14_{ref}
]

The buffer does not drift with future volatility.

### Breach
Intrabar High/Low crosses the raw structural reference but the applicable PCSB Close rule is not satisfied.

### PCSB
For resistance/high reference:

[
Close_t > Reference + Buffer
]

For support/low reference:

[
Close_t < Reference - Buffer
]

Equality at the buffered boundary is not a PCSB.

### Reclaim
After PCSB, price closes back through the same frozen reference to the prior side by the same frozen buffer.

No D3 Acceptance/Re-Acceptance is inferred from this event.

---

# 10. Protected Swing

Primary Protected Swing per timeframe:

- Uptrend → Protected Low;
- Downtrend → Protected High.

### Promotion in Uptrend
1. a confirmed structural High exists;
2. a subsequent confirmed correction Low forms;
3. a later PCSB confirms continuation above the relevant prior structural High;
4. the intervening correction Low is promoted to Primary Protected Low at the PCSB confirmation timestamp.

### Promotion in Downtrend
Symmetric logic promotes the intervening correction High after confirmed continuation below the relevant prior structural Low.

Promotion is causal and timestamped at the continuation PCSB, not retrospectively at the correction extremum.

An internal swing break is not automatically a primary counter-structural break.

A PCSB through the Primary Protected Swing against the trend changes trend integrity to Broken and moves the regime to Transition.

---

# 11. P1 Structural Events

P1 includes:

- Breach;
- PCSB;
- Continuation Break;
- Counter-Structural Break;
- price-based Reclaim.

Range boundary PCSB moves the regime to Transition.

D3 Acceptance/Re-Acceptance and final Failed Break classification are excluded from P1.


---

# 12. Design Freeze Revision 01 — Operational Clarifications

These rules are part of the frozen P1 design and remove implementation ambiguity.

## 12.1 Analysis Islands and Data Gaps

P1 does not interpolate missing market candles.

A frozen phase segment may contain a documented `SYNCHRONIZED_VENUE_GAP` only when:

- the missing native timestamps are identical across all four pilot instruments;
- official source archives/checksums are valid;
- external venue evidence supports a common trading interruption;
- the gap is registered before Execution Freeze.

For each analytical timeframe:

- any derived candle containing a registered native gap is `INCOMPLETE`;
- incomplete derived candles are excluded from D1 analytical input;
- the analytical stream is split into contiguous **Analysis Islands**;
- all swing, volatility, regime, Protected Swing and structural-event state resets at the first candle of every new Analysis Island;
- no structural object may span an island boundary.

An unregistered or non-synchronized gap is an Execution-Freeze blocker.

## 12.2 M1 Same-Type Pivot Handling

M1 preserves the first causally confirmed pivot.

If another same-type fixed-window pivot confirms before an opposite structural swing confirms:

- the later pivot is not allowed to mutate the already confirmed swing;
- it is ignored for the confirmed-swing sequence;
- the occurrence is logged as a diagnostic anomaly.

This rule enforces both swing immutability and High/Low alternation.

## 12.3 M2 Bootstrap

M2 begins with simultaneous causal High and Low candidates from the first evaluable candle.

If the same closed candle satisfies both initial reversal directions:

- no swing is confirmed;
- state remains `UNINITIALIZED`;
- an `AMBIGUOUS_BOOTSTRAP` diagnostic is emitted.

Candidate extrema update only on a **strict** new High or Low; equal extrema preserve the earlier timestamp.

## 12.4 M3 Bootstrap

M3 begins only at the first candle where the selected volatility estimator is valid.

The first valid-volatility candle initializes simultaneous High and Low candidates and their corresponding volatility references.

The same ambiguous-bootstrap and strict-extremum-update rules used by M2 apply.

No pre-initialization extremum may later receive a volatility value retroactively.

## 12.5 Same-Bar Processing Order

For every closed candle:

1. evaluate already active structural references and Protected Swing conditions;
2. emit any resulting structural events/regime consequences;
3. process swing confirmations that occur at this candle close;
4. classify new structural relations/cycles;
5. activate new references.

A newly activated reference is first break-eligible on a **later** closed candle.

## 12.6 Generic Structural Reference Lifecycle

At most one generic active Swing reference per type is maintained:

- latest confirmed structural High;
- latest confirmed structural Low.

When a new same-type confirmed swing activates:

- the previous unbroken generic same-type reference is `RETIRED`;
- a previously broken reference may remain only for its pending Reclaim lifecycle;
- a Primary Protected Swing is managed separately and is not retired by this rule.

This prevents one candle from generating duplicate PCSB/Continuation events through stacked obsolete swing references.

## 12.7 Range Boundary Construction

When Range is established from the latest two equal Highs and latest two equal Lows:

- Range High = maximum price of those two Highs;
- Range Low = minimum price of those two Lows.

The range-boundary ATR/buffer is frozen at Range activation.

## 12.8 Opposing Cycle Resolution

While a directional Trend is active:

- one opposing completed directional cycle sets integrity to `WEAKENING`;
- if opposing completed cycles reach the active `m` requirement before a Protected Swing break has already transitioned the regime, the current Trend moves to `TRANSITION / BROKEN`;
- the opposite Trend cannot be established on the same cycle that caused the transition.

This preserves the prohibition on direct Uptrend↔Downtrend flips.


---

# 13. Design Freeze Revision 02 — Detector Edge Cases

Revision 02 closes the remaining detector ambiguities discovered by implementation regression.

## 13.1 M1 Dual-Pivot Ambiguity

If the same fixed-window center candle is simultaneously:

- the unique maximum High; and
- the unique minimum Low

inside the same complete ((2w+1))-bar window, intrabar direction cannot be inferred.

Result:

- neither pivot is confirmed;
- diagnostic `AMBIGUOUS_DUAL_PIVOT` is emitted;
- no same-timestamp pair of opposite swings is created.

## 13.2 M3 Intrabar Diagnostic Variant

The diagnostic-only intrabar M3 subset remains excluded from final candidate eligibility.

It uses the same causal volatility estimator and candidate-extremum state as primary M3, but the trigger is evaluated from the full closed candle range:

During an UP leg:

[
Low_t \le H^* - kV^*
]

During a DOWN leg:

[
High_t \ge L^* + kV^*
]

Processing occurs only after the candle closes.

If the same candle both:

- establishes a strict new candidate extremum; and
- satisfies the opposite intrabar reversal condition,

the chronological intrabar order is unknowable.

Result:

- no swing confirmation;
- diagnostic `AMBIGUOUS_INTRABAR_SEQUENCE`;
- the updated candidate remains active.

The diagnostic variant cannot be promoted to a final ASSET-P1-D1-001 candidate regardless of its observed behavior.
