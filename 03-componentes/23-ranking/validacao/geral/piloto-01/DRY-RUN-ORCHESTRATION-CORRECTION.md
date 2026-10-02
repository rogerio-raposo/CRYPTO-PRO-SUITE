# PCP-01 — Dry-Run Orchestration Correction

**Status:** IMPLEMENTED / CONTROLLED QUALIFICATION IN PROGRESS  
**Date:** 2026-10-02  
**Scope:** operational orchestration only  
**Methodology effect:** NONE

## Problem

The pre-registered PCP-01 readiness rule requires:
> two technically successful dry-run cycles in adjacent UTC hour slots.

The first implementation relied on a GitHub Actions hourly cron schedule. Although individual market-data cycles repeatedly returned PASS for all 9/9 mapped markets, GitHub scheduler start delays placed successful observations in non-adjacent UTC hour slots.

Observed persisted PASS slots included:
`05:00, 13:00, 18:00, 23:00, 02:00, 08:00, 15:00 UTC`.

Therefore the correct state remained:
`two_cycle_status = PENDING`.

## Decision

Do not relax or reinterpret the methodological rule after observing results.

The defect is operational:
> the scheduler was not a reliable mechanism for generating the required temporal pair.

## Corrected orchestration

Data Feed commit:
`70b9a58bbef3a3be6c4dcf1b7857b4fcfa9ad6e8`

The qualification workflow now executes a single controlled pair:
1. cycle A;
2. wait 3600 seconds;
3. cycle B;
4. validate the persisted status;
5. require `two_cycle_status = PASS`;
6. require the qualified cycle IDs to equal the current run's A/B IDs.

The recurring cron was removed from this qualification workflow.

## Controlled run

GitHub Actions run:
`37059995273`

State when this record was written:
`IN PROGRESS`.

## Governance

This correction:
- does not change PCP-01 configuration;
- does not change the meaning of “two consecutive hourly cycles”;
- does not change QEV requirements;
- does not alter RAS-01;
- does not change PEC/PR formulas or thresholds;
- does not convert prior non-adjacent PASS cycles into qualifying evidence;
- does not authorize UFT/T0 before controlled-pair verification.

After the controlled run completes, the persisted Data Feed status remains the authoritative operational result for this gate.
