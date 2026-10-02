# PCP-01 — Capacity Operational Readiness — PRE-T0

**Status:** HUMAN UFT GATE PASSED / OFFICIAL CAPTURE ACTIVE  
**Date:** 2026-10-02  
**Scope:** nine Relationship-surviving assets

## Capacity population

Confirmed Relationship complete:
`PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`

Provisional Relationship:
`APT`

Materiality FAIL assets (`ADA, QNT, ONDO`) do not enter Capacity in Run A.

## QEV declaration

The frozen Binance Spot USDT mapping for all nine Capacity assets is now:

`QUALIFIED / DECLARED FOR PCP-01`.

Declaration basis:
- controlled workflow run `37059995273`;
- cycle A = `2026-10-02T20:00:00Z`, PASS 9/9;
- cycle B = `2026-10-02T21:00:00Z`, PASS 9/9;
- adjacent UTC hour slots;
- persisted `two_cycle_status = PASS`;
- workflow verification step = success.

Reference:
`QEV-MAPPING-AND-CAPTURE-MANIFEST.md`.

## Dry-run requirement

Pre-registered condition:
> two technically successful cycles in adjacent UTC hour slots.

Result:
> **SATISFIED**.

No prior non-adjacent cycle was retroactively counted.

## Official capture readiness

The official raw capture producer and exact seven-day turnover producer are implemented.

Because GitHub recurring schedule latency proved unreliable during dry-run qualification, official capture orchestration was hardened before UFT.

Isolated Data Feed branch:
`experiment/pcp01-capacity`

Current controlled-capture implementation commit:
`d439e1b29586cd08b560183654877bf16687337b`

Controlled design:
- manual dispatch after activation;
- five bounded sequential capture segments covering events 00–23;
- hourly target waiting inside jobs;
- lateness rejection rather than silent slot substitution;
- segment persistence to the isolated branch;
- exact 7-day turnover collection after T0.

The branch is isolated from concurrent Asset PRO P0 work.

## Conflict / concurrency check

At readiness review:
- Data Feed `main` = `8e77307af7e37d472875c4a6435778036e540dfc`;
- Asset PRO work branch = `experiment/asset-p0`;
- Ranking Capacity work branch = `experiment/pcp01-capacity`;
- no active workflow run was present when branch isolation was established;
- Asset PRO branch changes were confined to `docs/experimental/asset-p0/`;
- PCP-01 controlled-capture changes are confined to PCP-01 workflow/source paths.

Before activation, re-run branch freshness and overlap checks.

## RSR depth diagnostic

RSRUSDT repeatedly returned valid data while standard 1000-level bid depth was below the approximately USD 208.3k child order.

Treatment:
- not a source failure;
- not an Absorption FAIL;
- official capture escalates depth;
- source expansion remains mandatory before a negative Absorption conclusion if E2 cannot be established from qualified Binance evidence.

## Readiness checklist

| Item | State |
|---|---|
| PCP-01 configuration frozen | PASS |
| QPS Capability Matrix completed | PASS |
| SMU-PCP01 built | PASS |
| canonicalization completed | PASS |
| Candidate Discovery completed | PASS |
| candidate sample frozen | PASS |
| QEV mapping frozen | PASS |
| two adjacent dry-run cycles | PASS |
| QEVs declared | PASS |
| raw capture producer implemented | PASS |
| turnover-at-T0 producer implemented | PASS |
| official timing orchestration hardened | PASS |
| Accessibility rubric frozen | PASS |
| Absorption protocol frozen | PASS |
| source-expansion rule frozen | PASS |
| human UFT gate | PASS |

## UFT / Capture Start / T0

Declared after explicit human authorization:

- `UFT = 2026-10-02T23:22:34Z`;
- `Capture Start = 2026-10-03T00:00:00Z`;
- `T0 = 2026-10-04T00:00:00Z`;
- `Horizon End = 2027-01-02T00:00:00Z`.

Execution code freeze:
`468738b56a965c43169afa21bd31452bcc65e8a1`

Activation commit:
`82dd32a341e60201bc1c8c03bf45ad846a56f6a0`

Official GitHub Actions run:
`37077293144`

The workflow validation job completed successfully. The first controlled capture segment is active ahead of Capture Start.

Technical validity remains `PENDING` until the 24-event capture and turnover-at-T0 process completes.

Until T0 completion:
- do not calculate final PEC/PR;
- do not assign final Absorption or Capacity E-states;
- do not calculate Ranking Classes.
