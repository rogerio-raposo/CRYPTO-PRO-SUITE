# Asset PRO — Canonical Market Policy

**Status:** WORKING / NON-NORMATIVE  
**Scope:** Asset PRO ↔ Crypto Pro Data Feed / Source Governance  
**Date:** 2026-10-01  
**Purpose:** define the conceptual policy by which a market may be selected, used, validated, replaced or temporarily substituted as the canonical market reference for Asset PRO. This document does not select specific exchanges or define implementation code.

---

## 1. Policy objective

Asset PRO requires a stable and auditable market reference for structural technical analysis.

The Canonical Market Policy exists to ensure that D1–D5 are built from a coherent market series rather than from an arbitrary or silently changing exchange source.

The policy SHALL optimize for:

- analytical representativeness;
- continuity;
- reproducibility;
- data integrity;
- operational reliability;
- provenance;
- controlled source substitution.

The policy SHALL NOT assume that the largest or most familiar exchange is automatically canonical for every asset.

---

## 2. Canonical Market definition

A **Canonical Market** is the explicitly selected market reference used as the authoritative structural series for a defined analytical purpose within Asset PRO.

The canonical object is not merely an exchange. It is the tuple:

- Asset;
- Venue;
- Market Type;
- Instrument / Contract;
- Pair;
- Quote Currency;
- Analytical Purpose;
- Effective Period;
- Policy Version.

Example of analytical purposes may include:

- Structural Price Series;
- Spot Participation;
- Derivatives Context.

The first Asset PRO implementation should prioritize one **Canonical Structural Market** per asset/run for D1, D2 and D5 and for baseline D3/D4 where compatible.

---

## 3. Canonical Structural Market

The **Canonical Structural Market (CSMkt)** is the principal source for:

- OHLC structure;
- swing detection;
- structural breaks;
- support/resistance mapping;
- momentum calculations;
- setup confirmation/invalidation events;
- structural proxies derived from price.

D1, D2 and D5 SHOULD use the same CSMkt unless a documented exception exists.

This policy avoids internal inconsistency caused by deriving structure from one venue and momentum or invalidation from another.

---

## 4. Canonical Market is selected by policy, not preference

A market becomes canonical only after passing:

1. **Eligibility Gates**; and
2. **Comparative Assessment** among eligible candidates.

Historical preferences such as Binance, Bybit, OKX, Bitget or MEXC may inform discovery and operational convenience but SHALL NOT, by themselves, determine canonical status.

---

## 5. Eligibility Gates

A candidate market must satisfy minimum conditions before comparative selection.

### EG1 — Instrument Identity
The traded instrument must map unambiguously to the intended cryptoasset and market type.

### EG2 — Active and Continuous Market
The market must be active and provide sufficient continuity for the requested analytical horizon.

### EG3 — Minimum Data Integrity
Required OHLCV fields must pass semantic and continuity validation.

### EG4 — Historical Sufficiency
The market must provide enough history for the requested CTF/PTF/TTF configuration and admitted analytical calculations.

### EG5 — Operational Accessibility
The source must be retrievable with sufficient reliability for the intended operating cadence.

### EG6 — Provenance
Venue, market type, pair/contract, timestamps and source identity must be preserved.

### EG7 — Governance Eligibility
The source must be permitted under the applicable Source Governance policy, including commercial-use and continuity considerations where relevant.

A market failing a mandatory Eligibility Gate cannot become canonical for that analytical purpose.

---

## 6. Comparative Assessment

Eligible candidates should be compared using evidence families rather than a premature weighted score.

### C1 — Price-Discovery Relevance
How materially does the market contribute to current price formation for the asset?

### C2 — Liquidity and Depth
How robust is the market against isolated trades, local dislocations and execution noise?

### C3 — Volume Quality
How credible and representative is the reported trading activity?

### C4 — Historical Continuity
How stable and complete is the historical series across the required horizon?

### C5 — Data Granularity
Does the source provide the granularity required by the Asset PRO analytical contract?

### C6 — Operational Reliability
How reliable are API access, timestamps, symbol definitions and data publication?

### C7 — Market Stability
How exposed is the instrument to recurrent venue-specific anomalies, contract migrations or discontinuities?

### C8 — Source Continuity
How likely is the source to remain available and methodologically consistent across future runs?

No fixed weights are defined at this stage.

---

## 7. Selection method

The initial selection logic should be hierarchical rather than purely additive:

1. remove candidates failing Eligibility Gates;
2. identify the most analytically representative candidates;
3. compare liquidity, continuity and data integrity;
4. prefer the candidate that best preserves analytical coherence and reproducibility;
5. document the selection and policy version.

A numeric source score MAY be developed later if empirical validation demonstrates value, but it is not required for the initial policy.

---

## 8. Market-type separation

Spot, perpetual futures, dated futures and other market types SHALL remain distinct.

A spot market SHALL NOT be silently substituted by a perpetual market for structural analysis, or vice versa.

Where derivatives data are analytically required, the architecture may define a separate:

- Canonical Structural Market;
- Canonical Derivatives Market.

The methodology must state which market is authoritative for each analytical object.

---

## 9. Quote-currency separation

Markets such as:

- BTCUSDT;
- BTCUSDC;
- BTCUSD;

SHALL NOT be treated as identical data sources.

Quote currency is part of canonical identity.

Any aggregation or substitution across quote currencies requires an explicit transformation policy and provenance.

---

## 10. Validation Venues

A **Validation Venue** is an approved secondary market used to evaluate whether an observed event is likely to be market-wide or venue-specific.

Validation venues do not replace the canonical series during normal operation.

They are used when:

- a critical structural event occurs;
- an invalidation or confirmation may be triggered;
- a candle or wick is anomalously large;
- data quality is flagged;
- the canonical market experiences operational instability;
- cross-venue divergence is unusually high.

The exact number of validation venues and discrepancy thresholds remain open.

---

## 11. Critical-event cross-venue validation

For high-impact methodological transitions, including:

- Confirmed Structural Break;
- Setup Confirmation;
- Setup Invalidation;
- extreme sweep;
- anomalous displacement;

the system SHOULD support cross-venue validation when the event appears abnormal or source-specific.

Possible outcomes include:

### CONFIRMED ACROSS VENUES
The event is broadly consistent across approved secondary markets.

### CANONICAL-ONLY EVENT
The event appears materially isolated to the canonical venue.

### INCONCLUSIVE
Secondary sources are unavailable or materially divergent.

A Canonical-Only Event SHALL be explicitly flagged before it is allowed to drive irreversible analytical state changes under future operational rules.

---

## 12. Venue-Specific Anomaly

A **Venue-Specific Anomaly** is an event materially present in one market but not supported by sufficiently comparable approved venues.

Examples may include:

- isolated wick;
- local flash crash;
- temporary order-book failure;
- exchange outage or matching-engine anomaly;
- contract-specific dislocation.

The exact statistical threshold remains open.

The policy principle is:

> venue-specific anomalies must not be silently interpreted as market-wide structural events.

---

## 13. Fallback Source

A **Fallback Source** is a temporary substitute used when the Canonical Market cannot be accessed or validated.

Fallback use does not transfer canonical status.

Fallback must record:

- reason for activation;
- start time;
- source identity;
- semantic comparability to the canonical market;
- affected dimensions;
- data-sufficiency impact.

---

## 14. Fallback compatibility classes

Fallback sources should be classified conceptually by compatibility.

### F1 — Equivalent Fallback
Same market type and sufficiently comparable instrument/quote structure. Analysis may continue with explicit provenance, subject to validation.

### F2 — Non-equivalent but usable fallback
Different market characteristics but sufficient for limited analytical continuity. Analysis becomes DEGRADED and affected conclusions must be identified.

### F3 — Incompatible fallback
Substitution would materially change the analytical object. Asset PRO should suspend the affected assessment rather than pretend continuity.

The exact mapping rules remain open.

---

## 15. Fallback and irreversible setup transitions

Until empirical rules are defined, a conservative principle should apply:

> an irreversible setup-state transition should not be triggered solely by a non-equivalent fallback source when the canonical market is unavailable.

Examples of irreversible transitions include:

- Confirmed → Invalidated;
- Developing → Confirmed, when the trigger materially depends on venue-specific price behavior.

In such cases the preferred operational state is:

- provisional;
- degraded; or
- assessment suspended,

depending on data availability.

---

## 16. Canonical Market change

A Canonical Market change is a methodological event, not a routine source switch.

A change may be justified by:

- persistent migration of price discovery;
- material deterioration of canonical liquidity;
- delisting;
- discontinuation of the instrument;
- source instability;
- contract migration;
- regulatory or operational constraints;
- material change in data quality;
- revised Source Governance policy.

The change SHALL record:

- previous canonical market;
- new canonical market;
- reason;
- effective date;
- policy version;
- historical comparability assessment.

---

## 17. Historical reconstruction after canonical change

When feasible, a canonical change SHOULD trigger reconstruction of the relevant historical analytical window using the new market.

The purpose is to avoid:

- mixed-venue swing structures;
- artificial support/resistance;
- incompatible momentum series;
- false setup invalidations;
- discontinuous Volume Profile.

If historical reconstruction is not possible, the output must explicitly mark a **Source-Regime Boundary**.

---

## 18. Source-Regime Boundary

A **Source-Regime Boundary** is the timestamp at which the authoritative analytical source changes in a way that may affect comparability.

Analytical calculations that cross this boundary must either:

1. use reconstructed homogeneous history; or
2. declare degraded comparability.

The boundary must be preserved in provenance.

---

## 19. Multi-venue aggregation

Multi-venue aggregation SHALL be used only when the analytical object justifies it.

Potential candidates include:

- total or representative volume;
- derivatives open interest;
- funding context;
- liquidation activity;
- market-wide breadth.

Structural OHLC for D1/D2/D5 SHOULD initially remain based on one coherent Canonical Structural Market rather than a synthetic multi-venue candle.

Synthetic structural series may be considered later only under an explicit methodology.

---

## 20. Relationship with D1–D5

### D1 — Structure and Regime
Uses Canonical Structural Market.

### D2 — Location and Structural Context
Uses the same structural series as D1.

### D3 — Participation and Acceptance
Uses canonical-market participation as baseline and may later consume explicitly defined aggregated participation.

### D4 — Liquidity, Proxies and Displacements
Structural proxies use the canonical market; observed liquidity and derivatives evidence preserve venue-specific provenance.

### D5 — Impulse and Persistence
Uses the same structural series as D1 unless a documented methodological exception exists.

---

## 21. Relationship with Data Sufficiency

Canonical-market status does not guarantee that all data are sufficient.

Data Sufficiency is evaluated independently.

Examples:

- canonical market valid, but volume history incomplete → D3 DEGRADED;
- canonical market valid, but order-book history unavailable → observed-liquidity D4 INSUFFICIENT while proxy D4 remains available;
- canonical market unavailable and only incompatible fallback exists → structural assessment may be SUSPENDED.

---

## 22. Governance outputs

The future operational implementation should be able to expose at least:

- Canonical Market ID;
- Canonical Market effective period;
- selection policy version;
- validation venues;
- fallback status;
- source-regime boundary;
- data-sufficiency status;
- anomaly flags.

These outputs are part of auditability, not optional metadata.

---

## 23. Decisions intentionally deferred

This policy does NOT yet decide:

- which exchanges are Approved Market Sources;
- a fixed Binance/Bybit/OKX/Bitget/MEXC priority;
- exact liquidity thresholds;
- exact data-quality thresholds;
- exact validation-venue count;
- exact cross-venue divergence thresholds;
- exact rules for spot versus derivatives primacy;
- a numeric Canonical Market score;
- synthetic multi-venue OHLC construction;
- DEX inclusion;
- commercial data-vendor selection.

---

## 24. Policy conclusion

Asset PRO should use a **policy-selected Canonical Structural Market**, not an exchange chosen by habit.

Canonical selection requires eligibility, comparative assessment, provenance and lifecycle control.

Validation venues are used to detect source-specific anomalies. Fallback is temporary and does not silently alter canonical status. Canonical changes are methodological events and should preserve historical comparability whenever feasible.

This policy is a working conceptual dependency and does not modify the current stable Crypto Pro Data Feed v1.0.0 implementation.
