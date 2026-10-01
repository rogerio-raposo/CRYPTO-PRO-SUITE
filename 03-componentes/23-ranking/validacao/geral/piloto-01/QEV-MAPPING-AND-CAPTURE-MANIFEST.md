# PCP-01 — QEV Mapping and Capture Manifest

**Status:** MAPPING FROZEN / QEV DECLARATION PENDING SECOND DRY-RUN CYCLE  
**As-of:** 2026-10-01

## QEV — Qualified Execution Venue

Qualification is performed by `Asset × Venue × Market × T0`, not merely by exchange.

## Frozen Run A Capacity mapping

| canonical_asset_id | venue | symbol | base | quote | market_type | quote_usd_equivalent | first dry-run | qev_status |
|---|---|---|---|---|---|---|---|---|
| CPS-PLUME | Binance | PLUMEUSDT | PLUME | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-OP | Binance | OPUSDT | OP | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-APT | Binance | APTUSDT | APT | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-SUI | Binance | SUIUSDT | SUI | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-LINK | Binance | LINKUSDT | LINK | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-RSR | Binance | RSRUSDT | RSR | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-INJ | Binance | INJUSDT | INJ | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-HYPE | Binance | HYPEUSDT | HYPE | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |
| CPS-SYRUP | Binance | SYRUPUSDT | SYRUP | USDT | spot | yes — USDT_PARITY_PROXY | PASS | UNDECLARED |

QEV status remains undeclared until the required two adjacent UTC-hour dry-run cycles pass.

## First operational dry-run cycle

Workflow run: `36820324581`  
UTC hour slot: `2026-10-01T05:00:00Z`  
Technical result: **PASS — 9/9 markets**.

The dry-run validates:
- active market identity;
- order-book acquisition;
- best bid/ask and ordered levels;
- seven-day turnover availability;
- timestamps;
- provenance;
- failure semantics.

It does not calculate PEC, PR or Capacity states.

### Diagnostic depth observation

The first cycle showed that RSRUSDT had valid market data but only about USD 125.9k of visible bid notional in the standard 1000-level snapshot, below the ~USD 208.3k child order.

This is not a technical failure. Official capture will escalate depth to the deepest supported pilot REST snapshot before any economic conclusion.

## Capture Manifest — official run

For each declared QEV:
- 24 hourly capture events;
- UTC;
- best bid/ask;
- ordered order-book levels/depth;
- market status;
- venue/source timestamp when available;
- observed_at;
- collection status;
- provenance;
- depth-limit/escalation metadata;
- retry/error metadata.

Official Data Feed namespace:

`data/experimental/pcp-01/capture/<run_id>/`

Expected artifacts:
- `event-00.json.gz` … `event-23.json.gz`;
- `capture-manifest.json`;
- `turnover-7d-at-t0.json`.

## Depth policy

Standard snapshot request:
`1000 levels`.

If the RAS child order cannot be observed in either direction:
1. retry same Binance market with target depth of 5000 levels where supported;
2. never interpolate missing depth;
3. preserve whether depth escalation occurred;
4. if the child order still cannot be filled, route to the Capacity source-expansion rule before any negative Absorption conclusion.

## Synchronization

For a future multi-venue extension:
- target cross-venue alignment <= 60 seconds;
- maximum consolidation tolerance = 180 seconds;
- above 180 seconds, preserve venue-specific observations without treating them as simultaneous consolidated liquidity.

Run A currently has one venue per mapped asset, so cross-venue aggregation is not active.

## Deposit / withdrawal state

The public Binance market-data path used by the Data Feed does not provide the authenticated account/network deposit-withdrawal status required for a complete institutional-access conclusion.

Therefore:
- deposit/withdraw status is **not silently inferred** from market availability;
- this field remains outside the Data Feed market-data qualification in the current step;
- transferability/custody evidence is assessed separately under the Institutional Accessibility rubric.

## Activation status

`UFT`: NOT DECLARED  
`Capture Start`: NOT DECLARED  
`T0`: NOT DECLARED

The official capture activation file exists in the Data Feed but remains `active=false` until two-cycle dry-run qualification and formal UFT declaration.
