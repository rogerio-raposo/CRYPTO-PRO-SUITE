# PCP-01 — Absorption Calculation Protocol

**Status:** FROZEN BEFORE OFFICIAL CAPTURE
**RAS-01:** USD 5,000,000 executed within 24h
**Child order:** USD 5,000,000 / 24 = USD 208,333.333333...

## 1. Snapshot execution model

For each valid QEV order-book snapshot:

`mid = (best_bid + best_ask) / 2`

### Buy simulation
Walk asks from best to worse until exactly the child-order quote notional is filled.

`avg_buy = quote_spent / base_acquired`

`PEC_buy = (avg_buy - mid) / mid`

### Sell simulation
Define target base quantity as:

`base_to_sell = child_notional_usd / mid`

Walk bids from best to worse until that base quantity is filled.

`avg_sell = quote_received / base_sold`

`PEC_sell = (mid - avg_sell) / mid`

### Snapshot PEC_core

`PEC_core_snapshot = max(PEC_buy, PEC_sell)`

This conservative one-way metric includes half-spread plus book slippage/observable impact relative to mid. Account-specific fees are excluded.

## 2. Depth escalation

Standard capture requests 1000 book levels.

If either direction cannot fill the child order at 1000 levels:
1. retry the same venue with the deepest supported REST snapshot used by the pilot (target 5000 levels where supported);
2. do not extrapolate unobserved depth;
3. if still unfilled, mark `VENUE_DEPTH_INSUFFICIENT` for that direction.

Depth insufficiency is an economic observation, not an API failure.

## 3. Snapshot aggregation

Requirements:
- 24 hourly events planned;
- at least 18 valid snapshots required;
- median `PEC_core_snapshot` is the threshold statistic;
- P90 PEC is retained diagnostically.

Insufficient valid coverage produces `IND`, not poor-liquidity evidence.

## 4. Participation Ratio

`PR = RAS-01 / median_daily_qualified_spot_turnover_7d`

For Binance/USDT, turnover uses exact 7×24 one-hour records ending at T0, grouped into seven consecutive 24-hour bins relative to T0.

USDT quote turnover is treated as USD-equivalent under `USDT_PARITY_PROXY` unless a material parity disruption requires explicit normalization review.

## 5. E-state thresholds

Choose the highest fully satisfied state:

- `E4`: median PEC <= 0.50% AND PR <= 2%;
- `E3`: median PEC <= 1.00% AND PR <= 5%;
- `E2`: median PEC <= 2.00% AND PR <= 10%;
- `E1`: market is executable with sufficient evidence but does not satisfy E2 viability thresholds after required source-coverage review;
- `E0`: RAS child execution is not practically observable/achievable in the qualified execution set with robust sufficient evidence;
- `IND`: insufficient/conflicting data or unresolved source-coverage ambiguity.

Confidence is assigned separately.

## 6. Source coverage before negative conclusion

A single Binance QEV can prove minimum sufficiency when it alone passes E2.

If Binance does not meet E2 because of depth, PEC or PR, no E1/E0 conclusion is allowed until the source-expansion rule has been executed or explicitly shown infeasible. Until then the state is coverage-pending/IND.

## 7. Architecture

Data Feed captures and publishes raw books/turnover/provenance.

The Ranking validation layer computes PEC, PR and Absorption state. The Data Feed must not assign methodology E-states.