# PCP-01 — QEV Mapping and Capture Manifest

**Status:** QEV MAPPING FROZEN / QEVs DECLARED FOR PCP-01  
**As-of:** 2026-10-02

## QEV — Qualified Execution Venue

Qualification is performed by `Asset × Venue × Market × T0`, not merely by exchange.

The declaration below is specific to PCP-01. It does not constitute permanent commercial approval of Binance as a Suite-wide source.

## Frozen Run A Capacity mapping

| canonical_asset_id | venue | symbol | base | quote | market_type | quote_usd_equivalent | controlled dry-run | qev_status |
|---|---|---|---|---|---|---|---|---|
| CPS-PLUME | Binance | PLUMEUSDT | PLUME | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-OP | Binance | OPUSDT | OP | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-APT | Binance | APTUSDT | APT | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-SUI | Binance | SUIUSDT | SUI | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-LINK | Binance | LINKUSDT | LINK | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-RSR | Binance | RSRUSDT | RSR | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-INJ | Binance | INJUSDT | INJ | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-HYPE | Binance | HYPEUSDT | HYPE | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |
| CPS-SYRUP | Binance | SYRUPUSDT | SYRUP | USDT | spot | yes — USDT_PARITY_PROXY | PASS | QUALIFIED / DECLARED |

## Controlled two-cycle qualification basis

Data Feed workflow run:
`37059995273`

Qualified cycles:
- `gh-37059995273-A` — UTC hour slot `2026-10-02T20:00:00Z` — PASS 9/9;
- `gh-37059995273-B` — UTC hour slot `2026-10-02T21:00:00Z` — PASS 9/9.

Persisted Data Feed result:
`two_cycle_status = PASS`

The two hour slots are adjacent and the workflow verification step completed successfully.

This satisfies the pre-registered technical dry-run prerequisite for QEV declaration.

## What the dry-run validates

- active market identity;
- order-book acquisition;
- best bid/ask and ordered levels;
- seven-day turnover availability;
- UTC timestamps;
- provenance;
- failure semantics;
- repeated technical collection across all nine mapped markets.

It does not calculate PEC, PR or Capacity states.

## Diagnostic depth observation

RSRUSDT repeatedly returned valid market data but standard 1000-level visible bid notional below the approximately USD 208.3k child order.

This is:
- not a technical collection failure;
- not an Absorption FAIL;
- a trigger for the frozen depth-escalation rule during official capture.

If deeper Binance coverage still cannot establish E2, the source-expansion rule applies before any negative Absorption conclusion.

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

## Official capture orchestration

The original recurring-cron design is not considered sufficiently reliable for the official 24-hour window after the scheduler behavior observed during the dry-run phase.

A controlled official-capture implementation is prepared on the isolated Data Feed branch:

`experiment/pcp01-capacity`

Current implementation commit:

`d439e1b29586cd08b560183654877bf16687337b`

The controlled workflow:
1. is manually dispatched after activation;
2. executes events in bounded sequential segments;
3. waits for frozen hourly targets inside each segment;
4. rejects materially late intended slots instead of silently relabeling them;
5. persists each completed segment;
6. captures the exact seven-day turnover after T0.

This is an operational correction only; no PCP-01 methodological threshold or gate is changed.

## Depth policy

Standard snapshot request:
`1000 levels`.

If the RAS child order cannot be observed in either direction:
1. retry the same Binance market with target depth of 5000 levels where supported;
2. never interpolate missing depth;
3. preserve whether depth escalation occurred;
4. if the child order still cannot be filled, route to the Capacity source-expansion rule before any negative Absorption conclusion.

## Deposit / withdrawal state

The public Binance market-data path does not establish a complete institutional execution/custody/transfer path.

Therefore:
- deposit/withdraw status is not silently inferred from market availability;
- QEV qualification is not equivalent to Institutional Accessibility PASS;
- transferability/custody evidence remains separately assessed under the Institutional Accessibility rubric.

## Activation status

`UFT`: `2026-10-02T23:22:34Z`  
`Capture Start`: `2026-10-03T00:00:00Z`  
`T0`: `2026-10-04T00:00:00Z`  
`Horizon End`: `2027-01-02T00:00:00Z`  
Official capture activation: `active=true`  
Data Feed activation commit: `82dd32a341e60201bc1c8c03bf45ad846a56f6a0`  
GitHub Actions run: `37077293144`

The human UFT gate was explicitly authorized. Official capture is active on `experiment/pcp01-capacity`; technical validity remains pending until the 24-event capture and turnover-at-T0 process completes.
