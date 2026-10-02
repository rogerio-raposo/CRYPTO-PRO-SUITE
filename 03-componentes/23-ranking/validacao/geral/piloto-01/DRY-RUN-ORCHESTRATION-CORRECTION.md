# PCP-01 — Dry-Run Orchestration Correction

**Status:** IMPLEMENTED / CONTROLLED QUALIFICATION PASS  
**Date:** 2026-10-02  
**Scope:** operational orchestration only  
**Methodology effect:** NONE

## Problem

The pre-registered PCP-01 readiness rule requires:
> two technically successful dry-run cycles in adjacent UTC hour slots.

The first implementation relied on a GitHub Actions hourly cron schedule. Individual market-data cycles repeatedly returned PASS for all 9/9 mapped markets, but scheduler latency placed successful observations in non-adjacent UTC hour slots.

The correct state therefore remained `PENDING` until a qualifying adjacent pair was deliberately produced.

## Decision

The methodological rule was not relaxed or reinterpreted after observing results.

The defect was classified as operational orchestration.

## Corrected dry-run orchestration

Data Feed commit:
`70b9a58bbef3a3be6c4dcf1b7857b4fcfa9ad6e8`

The qualification workflow:
1. ran controlled cycle A;
2. waited 3600 seconds;
3. ran controlled cycle B;
4. required `two_cycle_status = PASS`;
5. required the qualified cycle IDs to equal the current run's A/B IDs.

## Controlled result

GitHub Actions run:
`37059995273`

Qualified pair:
- `gh-37059995273-A` — `2026-10-02T20:00:00Z` — PASS 9/9;
- `gh-37059995273-B` — `2026-10-02T21:00:00Z` — PASS 9/9.

Persisted result:
`two_cycle_status = PASS`.

Workflow conclusion:
`success`.

Therefore the pre-registered adjacent-hour technical qualification is satisfied.

## Follow-on control

The same scheduler-risk lesson applies to the official 24-hour capture window.

Before UFT, a controlled official-capture orchestration was prepared on:
`experiment/pcp01-capacity`

Current implementation commit:
`d439e1b29586cd08b560183654877bf16687337b`

This follow-on correction preserves the original hourly-capture requirement and avoids relying on recurring GitHub cron timing.

## Governance

These corrections:
- do not change PCP-01 configuration;
- do not change the meaning of consecutive hourly cycles;
- do not change QEV requirements;
- do not alter RAS-01;
- do not change PEC/PR formulas or thresholds;
- do not convert prior non-adjacent PASS cycles into qualifying evidence;
- do not authorize UFT/T0 without the human gate.
