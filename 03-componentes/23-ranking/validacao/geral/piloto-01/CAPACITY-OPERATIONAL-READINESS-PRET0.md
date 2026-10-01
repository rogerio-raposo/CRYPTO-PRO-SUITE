# PCP-01 — Capacity Operational Readiness — PRE-T0

**Status:** IN PROGRESS — first dry-run cycle PASS; second adjacent UTC-hour cycle pending
**Date:** 2026-10-01
**Scope:** nine Relationship-surviving assets

## Capacity population

Confirmed Relationship complete:
`PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`

Provisional Relationship:
`APT`

Materiality FAIL assets (`ADA, QNT, ONDO`) do not enter Capacity in Run A.

## Frozen QEV mapping

All nine assets have an active Binance Spot USDT market in the captured SMU.

| Asset | Canonical ID | Venue | Market | Quote | QEV status |
|---|---|---|---|---|---|
| PLUME | CPS-PLUME | Binance | PLUMEUSDT | USDT | UNDECLARED — dry-run pending completion |
| OP | CPS-OP | Binance | OPUSDT | USDT | UNDECLARED — dry-run pending completion |
| APT | CPS-APT | Binance | APTUSDT | USDT | UNDECLARED — dry-run pending completion |
| SUI | CPS-SUI | Binance | SUIUSDT | USDT | UNDECLARED — dry-run pending completion |
| LINK | CPS-LINK | Binance | LINKUSDT | USDT | UNDECLARED — dry-run pending completion |
| RSR | CPS-RSR | Binance | RSRUSDT | USDT | UNDECLARED — dry-run pending completion |
| INJ | CPS-INJ | Binance | INJUSDT | USDT | UNDECLARED — dry-run pending completion |
| HYPE | CPS-HYPE | Binance | HYPEUSDT | USDT | UNDECLARED — dry-run pending completion |
| SYRUP | CPS-SYRUP | Binance | SYRUPUSDT | USDT | UNDECLARED — dry-run pending completion |

USDT is treated as USD-equivalent for PCP-01 notional normalization under `USDT_PARITY_PROXY`. A material stablecoin dislocation invalidates silent 1:1 normalization and requires explicit handling.

## First multi-asset operational cycle

Data Feed workflow run:
`36820324581`

UTC hour slot:
`2026-10-01T05:00:00Z`

Result:
`PASS — 9/9 assets technically collected`.

Observed visible depth at 1000-level request is diagnostic only and does not determine dry-run technical success.

Notable diagnostic:
- RSRUSDT returned valid book/turnover data but visible bid notional was ~USD 125.9k, below the ~USD 208.3k child order;
- this is **not** a source failure and is **not** yet an Absorption FAIL;
- the official pipeline must escalate depth before any economic conclusion.

## Dry-run completion rule

The pre-registered requirement of two consecutive hourly cycles is operationalized as:
> two technically successful cycles in adjacent UTC hour slots.

Same-hour reruns replace the hour-slot observation and do not count as a second cycle.

Data Feed status:
`data/experimental/pcp-01/dry-run/capacity-status.json`

Current two-cycle status:
`PENDING`.

## Source-coverage rule

Binance is sufficient to establish an Absorption lower-bound PASS if the asset independently meets the PCP-01 E2 thresholds on this QEV.

A Binance-only failure must **not** be converted automatically into Absorption E1/E0. Before a negative Capacity conclusion caused by depth, PEC or PR, the pilot must execute the frozen source-expansion rule in `CAPACITY-SOURCE-EXPANSION-RULE.md`.

## UFT/T0 status

Not authorized yet.

Remaining readiness items:
1. second adjacent UTC-hour dry-run PASS;
2. official capture pipeline implemented and validated;
3. QEV status declaration;
4. Accessibility evidence plan ready;
5. then UFT → Capture Start → T0 may be declared.