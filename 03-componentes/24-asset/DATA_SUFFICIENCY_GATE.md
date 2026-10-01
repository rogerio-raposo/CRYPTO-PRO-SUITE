# Asset PRO — Data Sufficiency Gate

**Status:** WORKING / NON-NORMATIVE  
**Scope:** Asset PRO ↔ Crypto Pro Data Feed  
**Date:** 2026-10-01  
**Purpose:** define the conceptual gate that determines whether Asset PRO has enough reliable market data to generate, qualify or suspend analytical conclusions.

---

## 1. Objective

The Data Sufficiency Gate prevents missing, stale, inconsistent or source-ambiguous data from being interpreted as neutral or negative market evidence.

Data availability is a property of the analytical process, not of the market.

The gate SHALL be evaluated before analytical synthesis and SHALL be preserved at dimension level.

---

## 2. Top-level states

### SUFFICIENT
Required data are available, valid and coherent enough for the requested analytical scope.

### DEGRADED
Analysis remains possible, but one or more material limitations reduce coverage, comparability or confidence.

### INSUFFICIENT
Required data are unavailable, stale, inconsistent or unreliable enough that the requested analytical conclusion cannot be defensibly produced.

### SUSPENDED
A previously active analytical assessment cannot currently be refreshed or validated because critical data availability has been lost.

SUSPENDED is operationally distinct from INSUFFICIENT:
- INSUFFICIENT may prevent an analysis from being initiated;
- SUSPENDED applies when an existing live assessment can no longer be safely updated.

---

## 3. Gate dimensions

Data sufficiency SHALL consider at least:

- source identity;
- canonical-market status;
- historical depth;
- continuity;
- freshness;
- timestamp integrity;
- OHLC semantic validity;
- volume validity where required;
- market-type consistency;
- instrument identity;
- cross-venue anomaly status when applicable;
- source-regime boundaries;
- fallback compatibility.

---

## 4. Global versus dimension-level sufficiency

Asset PRO SHALL expose both:

1. **Global Sufficiency Status**; and
2. **Dimension-Level Sufficiency Status**.

Example:

- Global: DEGRADED
- D1: SUFFICIENT
- D2: SUFFICIENT
- D3: DEGRADED
- D4 Structural Proxies: SUFFICIENT
- D4 Observed Liquidity: INSUFFICIENT
- D5: SUFFICIENT

A dimension marked INSUFFICIENT must not be silently converted into a neutral analytical reading.

---

## 5. D1 — Structure and Regime

D1 requires at minimum:

- valid canonical OHLC series;
- sufficient historical depth for swing/regime identification;
- continuous timestamps or explicitly handled gaps;
- consistent market identity;
- acceptable freshness for the requested horizon.

D1 becomes DEGRADED when:
- minor recoverable gaps exist;
- a source-regime boundary reduces comparability;
- fallback use is compatible but not fully equivalent.

D1 becomes INSUFFICIENT or SUSPENDED when:
- structural history is too short;
- market identity is ambiguous;
- OHLC integrity is materially compromised;
- only incompatible fallback data are available.

---

## 6. D2 — Location and Structural Context

D2 inherits the structural-series requirements of D1.

D2 additionally requires enough history to identify relevant structural references.

Volume Profile-related outputs require their own sufficiency status and SHALL NOT block baseline D2 if structural price data remain valid.

Example:
- D2 Structural Location: SUFFICIENT
- D2 Volume Profile Context: INSUFFICIENT

---

## 7. D3 — Participation and Acceptance

Baseline D3 requires:

- volume tied to the same market identity as the analyzed price series;
- enough history for relative participation comparison;
- volume continuity and validity;
- explicit market type.

D3 may remain DEGRADED when:
- volume is canonical-venue only and broader market aggregation is unavailable;
- partial but usable volume history exists;
- spot/derivatives separation is incomplete.

D3 becomes INSUFFICIENT when participation conclusions would rely on missing or materially unreliable volume data.

Acceptance inferred primarily from price behavior may remain available even when advanced participation evidence is unavailable, provided the output clearly distinguishes the evidence type.

---

## 8. D4 — Liquidity, Proxies and Displacements

D4 SHALL maintain sufficiency separately by evidence class.

### Structural Proxy Sufficiency
May rely on canonical OHLC and deterministic derivation rules.

### Observed Liquidity Sufficiency
Requires relevant bid/ask, depth or execution data.

### Derivatives-Liquidity Sufficiency
Requires reliable open interest, funding, liquidations or other specified derivatives data.

### Model-Estimated Sufficiency
Requires source methodology, timestamp, provider and model provenance.

Absence of advanced D4 data SHALL NOT force structural-proxy D4 to zero.

---

## 9. D5 — Impulse and Persistence

D5 requires:

- continuous canonical OHLC;
- sufficient history for admitted calculations;
- stable sampling;
- volatility reference availability when normalization is required.

Derived indicators cannot be treated as valid when their initialization history is insufficient.

---

## 10. Freshness

Freshness thresholds SHALL be horizon-specific.

The gate must preserve:

- observation end time;
- ingestion/publication time where available;
- last successful update;
- current staleness;
- timeframe-specific freshness status.

A stale dataset may be:
- acceptable for higher-timeframe historical structure;
- unacceptable for tactical confirmation or invalidation.

Therefore freshness must be assessed against the analytical operation, not only the dataset.

---

## 11. Historical depth

Historical sufficiency SHALL be defined relative to:

- CTF;
- PTF;
- TTF when used;
- swing-identification method;
- volatility normalization;
- admitted indicators;
- profile calculations where applicable.

No universal candle-count requirement is fixed by this document.

Future operational rules should define minimum usable history plus initialization buffer.

---

## 12. Gaps and repairs

Detected gaps SHALL be classified.

### Non-material Gap
Does not materially alter the analytical object under the applicable rule.

### Material Gap
May alter swings, indicators, volume baselines or structural events.

### Critical Gap
Prevents defensible continuation of the affected analysis.

Asset PRO SHALL NOT silently fill a material or critical gap.

Any approved reconstruction method must preserve:
- original source;
- repaired interval;
- repair method;
- confidence impact.

---

## 13. Canonical-source loss

If the Canonical Structural Market becomes unavailable:

### Equivalent fallback available
Analysis may continue with explicit fallback provenance and possible DEGRADED status.

### Non-equivalent but usable fallback
Affected conclusions become DEGRADED; irreversible setup transitions should remain provisional unless validated.

### Only incompatible fallback available
Affected analysis becomes SUSPENDED.

---

## 14. Cross-venue anomalies

When a critical event appears venue-specific:

- the event SHALL be flagged;
- relevant state transitions may remain provisional;
- validation status SHALL be propagated into sufficiency/confidence.

A canonical-only anomaly must not be interpreted as broad confirmation without the future validation rule being satisfied.

---

## 15. Interaction with setup lifecycle

Data status and setup status are separate.

Examples:

- Setup CONFIRMED + Data SUFFICIENT
- Setup CONFIRMED + Data DEGRADED
- Setup CONFIRMED + Assessment SUSPENDED

Data deterioration does not automatically invalidate the setup.

Market invalidation requires a market event. Data failure only limits the ability to observe or update that event.

---

## 16. Interaction with Confidence

Data Sufficiency and Confidence are related but not interchangeable.

### Sufficiency
Can the analytical statement be defensibly produced at all?

### Confidence
How robust is the resulting inference given data quality, methodological clarity and evidence consistency?

A conclusion may be:
- SUFFICIENT with Medium Confidence;
- DEGRADED with Low Confidence;
- INSUFFICIENT with no analytical conclusion.

---

## 17. Minimum initial implementation gate

For the first operational Asset PRO version, an analysis should not receive global SUFFICIENT status unless at minimum:

1. asset/instrument identity is resolved;
2. Canonical Structural Market is known;
3. OHLC history is valid and sufficiently deep;
4. timestamps are continuous enough for the requested horizon;
5. freshness is acceptable for the requested operation;
6. venue, market type and pair are preserved;
7. D1, D2 and D5 are individually SUFFICIENT;
8. D3 has at least a valid baseline participation/acceptance source or is explicitly scoped as DEGRADED;
9. D4 evidence classes are individually declared rather than assumed;
10. no unresolved critical source anomaly makes the requested conclusion non-defensible.

---

## 18. Output contract

The future operational output should expose:

- Global Sufficiency Status;
- status by D1–D5;
- status by D4 evidence class;
- freshness status;
- canonical/fallback status;
- gap flags;
- source-regime-boundary flags;
- cross-venue anomaly flags;
- limitations text;
- timestamp of assessment.

---

## 19. Deferred quantitative rules

This document does NOT yet define:

- maximum stale intervals;
- minimum historical candle counts;
- acceptable missing-candle percentages;
- anomaly z-scores or volatility thresholds;
- fallback equivalence thresholds;
- cross-venue divergence thresholds;
- minimum volume history;
- minimum order-book coverage;
- dimension-specific numeric quality scores.

These require implementation and empirical validation.

---

## 20. Conclusion

The Data Sufficiency Gate is a precondition for defensible Asset PRO output.

Missing evidence is not negative evidence. Source failure is not market invalidation. Advanced-data absence should degrade only the dimensions that depend on those data.

The initial Asset PRO methodology should remain operational on high-quality canonical OHLCV while exposing clearly where participation, liquidity or cross-venue evidence is incomplete.
