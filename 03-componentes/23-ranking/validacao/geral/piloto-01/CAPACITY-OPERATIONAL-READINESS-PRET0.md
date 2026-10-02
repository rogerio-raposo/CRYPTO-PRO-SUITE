# PCP-01 — Capacity Operational Readiness — PRE-T0

**Status:** IN PROGRESS — controlled two-cycle qualification running  
**Date:** 2026-10-02  
**Scope:** nine Relationship-surviving assets

## Capacity population

Confirmed Relationship complete:
`PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`

Provisional Relationship:
`APT`

Materiality FAIL assets (`ADA, QNT, ONDO`) do not enter Capacity in Run A.

## Frozen QEV mapping

All nine assets have active Binance Spot USDT markets in the captured SMU. QEV status remains UNDECLARED until the two-cycle dry-run qualification is completed and verified.

## Dry-run rule

Pre-registered condition:
> two technically successful cycles in adjacent UTC hour slots.

Repeated individual cycles have returned PASS for 9/9 markets, but prior GitHub scheduler delays produced non-adjacent UTC-hour observations.

The methodology was not relaxed.

## Orchestration correction

The former hourly cron dependency was replaced by a controlled single workflow:
- cycle A;
- wait 3600 seconds;
- cycle B;
- verify PASS;
- verify the exact A/B pair as the qualifying cycles.

Data Feed commit:
`70b9a58bbef3a3be6c4dcf1b7857b4fcfa9ad6e8`

Controlled run:
`37059995273`

Current:
`IN PROGRESS`.

Detailed record:
`DRY-RUN-ORCHESTRATION-CORRECTION.md`

## RSR depth diagnostic

RSRUSDT repeatedly returns valid market data, but standard 1000-level bid depth has been below the ~USD 208.3k child notional.

Treatment remains:
- not a source failure;
- not an Absorption FAIL;
- official capture must escalate depth;
- if still insufficient, apply the frozen source-expansion rule before negative conclusion.

## UFT/T0 status

Not authorized yet.

Remaining readiness items:
1. controlled two-cycle qualification PASS;
2. verify persisted qualified cycle IDs and adjacent slots;
3. declare QEV status;
4. perform final readiness/Freshness gate;
5. human gate;
6. then UFT → Capture Start → T0 may be declared.
