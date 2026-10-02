# PCP-01 — UFT / T0 Run Declaration

**Status:** ACTIVE — OFFICIAL CAPACITY CAPTURE IN PROGRESS  
**Declared:** 2026-10-02  
**Run ID:** `PCP01-CAP-20261003T0000Z`

## Human gate
Explicit project-owner authorization received after two-cycle PASS, QEV declaration, freshness review and branch-overlap review.

## Temporal declaration
- UFT: `2026-10-02T23:22:34Z`
- Capture Start: `2026-10-03T00:00:00Z`
- T0: `2026-10-04T00:00:00Z`
- Horizon End: `2027-01-02T00:00:00Z`

## Execution provenance
- Data Feed: `rogerio-raposo/crypto-pro-datafeed`
- Branch: `experiment/pcp01-capacity`
- Frozen execution-code commit: `468738b56a965c43169afa21bd31452bcc65e8a1`
- Activation commit: `82dd32a341e60201bc1c8c03bf45ad846a56f6a0`
- Official workflow run: `37077293144`
- Validation job: PASS

## Dry-run qualification
- workflow run: `37059995273`
- cycle A: `2026-10-02T20:00:00Z` — PASS 9/9
- cycle B: `2026-10-02T21:00:00Z` — PASS 9/9
- `two_cycle_status = PASS`

## QPS / QEV
Pilot source: **Binance Spot — PILOT QUALIFIED for PCP-01**.  
Commercial approval remains **DEFERRED**.

Declared QEVs:
`PLUMEUSDT, OPUSDT, APTUSDT, SUIUSDT, LINKUSDT, RSRUSDT, INJUSDT, HYPEUSDT, SYRUPUSDT`.

## Candidate sample freeze
Reference: `RUN-A-SAMPLE.json`  
Git blob SHA: `98cd3f4753c0925c8779537995e753968216cd37`

Frozen sample:
`PLUME, OP, APT, ADA, SUI, LINK, QNT, ONDO, RSR, INJ, HYPE, SYRUP`.

Capacity population:
`PLUME, OP, APT, SUI, LINK, RSR, INJ, HYPE, SYRUP`.

## Parallel-work isolation
At the final gate:
- Data Feed main: `8e77307af7e37d472875c4a6435778036e540dfc`
- Ranking branch: `experiment/pcp01-capacity`
- Asset PRO branch: `experiment/asset-p0`
- both experiment branches were 0 behind main
- changed-file overlap: none
- pre-activation in-progress workflows: none

## Technical validity
Current state: `PENDING`.

Final technical validity requires post-T0 verification of:
- events 00–23 and capture-manifest;
- per-asset valid-event coverage;
- >25% systemic acquisition-failure rule;
- turnover-at-T0;
- provenance and depth-escalation evidence.

No final PEC/PR or Capacity classification is authorized before that review.
