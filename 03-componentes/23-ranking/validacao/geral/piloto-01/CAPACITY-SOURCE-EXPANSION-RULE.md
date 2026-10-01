# PCP-01 — Capacity Source Expansion Rule

**Status:** FROZEN BEFORE OFFICIAL CAPTURE RESULTS

## Purpose

Prevent a single-venue pilot boundary from creating false negative Absorption conclusions while avoiding pre-emptive implementation of five exchange adapters.

## Rule

### Case A — Binance alone satisfies E2

If validated Binance QEV data alone satisfies the E2 Absorption thresholds with sufficient Confidence:
> no second venue is required to establish minimum Capacity viability.

Additional venues could only add execution capacity; they are not necessary to prove the lower bound.

### Case B — Binance does not satisfy E2

If an asset fails the E2 threshold on Binance because of:
- insufficient observable depth;
- median PEC > 2%;
- PR > 10%;

then a negative Absorption state is **coverage-pending**.

Before E1/E0 or CAP-FAIL can be confirmed:
1. perform deeper Binance snapshot escalation where applicable;
2. if still below E2, implement/qualify the next approved experimental source with current spot coverage for that asset;
3. freeze the multi-venue aggregation/execution rule before using second-venue results.

## Source order

No permanent commercial source ranking is created here.

For PCP-01 engineering, the next venue is selected using already documented technical capability, asset coverage and implementation cost. Commercial approval remains deferred for the methodological pilot.

## If expansion is not feasible

If no additional technically qualified source can be added within the pilot constraints, do not claim global low Absorption.

Use `IND / bounded source coverage` and record the limitation.

## Anti-outcome rule

The trigger applies symmetrically to every asset that fails E2 on the first qualified venue. It cannot be invoked selectively to rescue a preferred asset.