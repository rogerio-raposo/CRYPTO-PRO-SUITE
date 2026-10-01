# Asset PRO — Market Data Requirements

**Status:** WORKING / NON-NORMATIVE  
**Scope:** Asset PRO ↔ Crypto Pro Data Feed  
**Date:** 2026-10-01  
**Purpose:** define the minimum market-data contract required by Asset PRO before the methodology is operationalized numerically. This document specifies consumer requirements. It does not define the Data Feed implementation, approved exchanges, API providers, or final source-governance policy.

---

## 1. Architectural principle

Asset PRO SHALL consume normalized market data through the Crypto Pro Data Feed or another formally approved data contract. Asset PRO SHALL NOT depend on direct, ad hoc exchange access as part of its analytical methodology.

The Data Feed is responsible for acquisition, validation, normalization and publication. Asset PRO is responsible for interpretation.

The market-data reference for Asset PRO SHALL be explicit at all times. At minimum, the analytical dataset must identify:

- asset;
- venue;
- market type;
- instrument or pair;
- quote currency;
- data source;
- time range;
- timeframe / granularity;
- data freshness;
- source/provenance status.

No market series may be treated as exchange-independent unless an explicit aggregation methodology has been defined.

---

## 2. Canonical Market concept

Asset PRO requires a **Canonical Market** for the principal structural price series used by D1, D2 and D5 and, when applicable, by D3 and D4.

The Canonical Market is the explicitly selected market reference for a given asset and analytical purpose. It is not automatically synonymous with a preferred exchange.

The final Canonical Market selection policy is not defined in this document. Future source governance should evaluate, at minimum:

- liquidity and market depth;
- reliability of reported volume;
- relevance to price discovery;
- continuity and historical coverage;
- data quality and completeness;
- API reliability and granularity;
- instrument stability;
- commercial-use constraints;
- continuity risk.

A Canonical Market record should preserve at least:

- Asset ID;
- Venue;
- Market Type;
- Instrument / Pair;
- Quote Currency;
- Canonical Status;
- Effective From;
- Effective To, when applicable;
- Selection Method / Policy Version;
- Provenance.

A change of Canonical Market SHALL be auditable and SHALL NOT be performed silently.

---

## 3. Canonical Market, Validation Venue and Fallback are different concepts

### 3.1 Canonical Market
Primary reference used to construct the official analytical series.

### 3.2 Validation Venue
Secondary approved market used to detect venue-specific anomalies, dislocations or data-quality problems.

### 3.3 Fallback Source
Temporary source used because the Canonical Market is unavailable.

Use of a fallback SHALL NOT automatically convert that source into the Canonical Market.

When a source change materially affects historical comparability, the analytical output must record that limitation or rebuild the relevant historical window when feasible.

---

## 4. Spot and derivatives

Spot and derivatives data SHALL remain explicitly distinguished.

Asset PRO may ultimately require separate references such as:

- Canonical Spot Market;
- Canonical Derivatives Market.

The methodology SHALL NOT silently combine spot and perpetual futures into a single market series.

Which market type should be primary for a given analytical object remains an open methodological and data-governance question.

---

## 5. Core OHLCV requirement

Historical OHLCV is the minimum common market-data substrate for the initial Asset PRO methodology.

Each candle record should contain at least:

- open time;
- close time;
- open;
- high;
- low;
- close;
- base volume and/or quote volume, when supported;
- venue;
- market type;
- instrument;
- timeframe;
- source timestamp;
- validation status.

The exact historical-depth requirement SHALL be defined by analytical horizon rather than by one universal number.

The Data Feed must support enough continuous history for the selected Context Timeframe (CTF), Primary Timeframe (PTF) and, when used, Trigger Timeframe (TTF) to permit stable calculation of structural context and any admitted indicators.

---

## 6. D1 — Structure and Regime data requirements

### Required
- continuous OHLC history on the Canonical Market;
- sufficient history to identify structural swings and prior regime;
- explicit timeframe;
- gap/anomaly metadata;
- venue and instrument provenance.

### Potentially useful but not required for initial D1
- cross-venue price confirmation;
- trade-level data;
- derivatives data.

D1 structural events, including breaches and structural breaks, must be attributable to a defined market series.

---

## 7. D2 — Location and Structural Context data requirements

### Required
- the same canonical OHLC series used by D1;
- sufficient historical window to identify relevant structural zones;
- consistent price adjustment and instrument definition.

### Conditional
- Volume Profile-compatible data, where Volume Profile is admitted;
- finer-grained volume-at-price data, if the implementation requires greater precision than candle approximation.

Fibonacci, support/resistance and other derived structural references do not require separate external data sources, but their source price series must be identifiable.

---

## 8. D3 — Participation and Acceptance data requirements

### Required baseline
- volume associated with the same market reference used for the price analysis;
- explicit venue;
- explicit market type;
- baseline history sufficient for relative participation comparisons.

### Strongly preferred
- both base and quote volume when the venue exposes them reliably;
- data-quality flags for abnormal or missing volume.

### Future / optional
- aggregated multi-venue volume;
- spot-versus-derivatives participation separation;
- trade-level buy/sell classification;
- volume delta / CVD;
- open interest;
- funding;
- liquidation data.

No volume measure may be described as "market-wide" unless its aggregation scope is explicit.

---

## 9. D4 — Liquidity, Proxies and Displacements data requirements

D4 uses different evidence classes and must preserve the distinction between them.

### Structural proxies
Require only the canonical OHLC series and explicit derivation rules.

Examples:
- prior highs/lows;
- clustered highs/lows;
- structural sweeps;
- price displacement;
- price-imbalance patterns.

### Observed liquidity
May require:
- bid/ask;
- order-book depth;
- order-book snapshots or history;
- venue-specific execution data.

### Derivatives-related liquidity
May require:
- open interest;
- funding;
- liquidations;
- model-estimated liquidation maps.

Observed, Derived, Proxy and Model-estimated evidence SHALL NOT be silently merged into one class.

Advanced D4 evidence is optional until the Data Feed can support it with sufficient quality and provenance.

---

## 10. D5 — Impulse and Persistence data requirements

### Required
- continuous canonical OHLC history;
- sufficiently stable sampling;
- history adequate for volatility normalization and admitted momentum calculations.

D5 should normally use the same canonical structural price series as D1 to avoid internal inconsistency.

Derived indicators such as RSI, MACD or moving averages do not create additional external data requirements beyond the underlying price series unless future methodology explicitly states otherwise.

---

## 11. Cross-venue anomaly control

For events capable of materially changing a setup state — especially structural break or invalidation — the architecture should support validation against one or more approved secondary venues when:

- the event is unusually large relative to recent volatility;
- the canonical venue shows an isolated wick or price discontinuity;
- data-quality flags are raised;
- the market experienced known venue instability;
- the event would trigger a high-impact methodological transition.

A cross-venue discrepancy SHALL be recorded as a **Venue-Specific Anomaly** or other defined status when applicable.

The exact quantitative discrepancy threshold remains open.

---

## 12. Freshness requirements

Freshness SHALL be defined relative to the analytical horizon.

A single universal freshness threshold is inappropriate.

The data contract should expose:

- observation end time;
- publication time;
- ingestion time when available;
- freshness status;
- last successful update;
- stale-data flag.

The future methodology should define maximum tolerable staleness by timeframe and analytical operation.

---

## 13. Data gaps and continuity

The Data Feed should detect and expose:

- missing candles;
- duplicated candles;
- timestamp discontinuities;
- impossible OHLC relations;
- non-positive or otherwise invalid prices;
- anomalous volume fields;
- symbol/instrument changes;
- market suspensions;
- source interruptions.

Asset PRO SHALL NOT silently interpolate or repair structural price data unless a documented method authorizes it.

Any repair, substitution or reconstruction must preserve provenance.

---

## 14. Data Sufficiency Gate

Asset PRO requires a formal Data Sufficiency Gate before analytical state generation.

Four top-level operational states are proposed:

### SUFFICIENT
Required data are complete and reliable enough for the requested analytical scope.

### DEGRADED
Analysis remains possible, but one or more limitations materially reduce coverage or confidence. The affected dimensions must be identified.

### INSUFFICIENT
Required data are missing, stale, inconsistent or unreliable enough that the requested conclusion cannot be produced defensibly.

### SUSPENDED
A previously active analytical assessment cannot currently be refreshed or validated because critical data availability has been lost.

"Insufficient" and "Suspended" are not negative market evidence. They are analytical availability states.

---

## 15. Dimension-level sufficiency

Overall sufficiency may differ by dimension.

Example:

- D1: Sufficient;
- D2: Sufficient;
- D3: Degraded because volume coverage is partial;
- D4: Insufficient for observed-liquidity analysis but Sufficient for structural proxies;
- D5: Sufficient.

The final output must not convert unavailable evidence into neutral or negative evidence.

---

## 16. Minimum core for an initial Asset PRO implementation

The minimum initial data contract should support:

1. stable asset/instrument identification;
2. one explicit Canonical Market;
3. continuous historical OHLCV;
4. multiple timeframes or deterministic resampling;
5. venue, market-type and pair provenance;
6. timestamps and freshness;
7. data-gap and validation flags;
8. enough history for CTF/PTF/TTF analysis;
9. status sufficient to classify data as SUFFICIENT / DEGRADED / INSUFFICIENT / SUSPENDED where applicable.

This minimum is sufficient to build the first operational versions of D1, D2, baseline D3, proxy-based D4 and D5.

Advanced market-microstructure data SHOULD remain optional until separately specified and validated.

---

## 17. Requirements not decided by this document

This document intentionally does NOT decide:

- the final list of Approved Market Sources;
- a fixed priority order among Binance, Bybit, OKX, Bitget, MEXC or other venues;
- whether spot or perpetual markets are always primary;
- the Canonical Market selection algorithm;
- quantitative cross-venue anomaly thresholds;
- required historical depths by timeframe;
- exact freshness thresholds;
- aggregation methodology for multi-venue volume;
- order-book retention policy;
- commercial data providers;
- licensing and redistribution policy;
- DEX integration;
- exact Data Feed schema or API implementation.

Those items require later Data Feed / Source Governance specification.

---

## 18. Architectural conclusion

Asset PRO should be built against a **market-data contract**, not against a specific exchange.

The initial methodology should use one coherent Canonical Market for structural analysis, preserve explicit provenance, allow secondary venues for anomaly validation, and treat multi-venue aggregation only where the analytical object justifies it.

This document is a working interface specification and does not modify the current stable Crypto Pro Data Feed v1.0.0 contract.
