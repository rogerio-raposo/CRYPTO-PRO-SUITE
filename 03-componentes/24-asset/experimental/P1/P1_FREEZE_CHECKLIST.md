# Asset PRO — P1 Design Freeze Checklist

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Design Freeze:** PENDING

---

## Dependency

- [x] ASSET-P0-001 Decision Record = PASS.

## Universe and Data

- [x] A1 BTCUSDT selected.
- [x] A2 ETHUSDT selected.
- [x] A3 SOLUSDT selected.
- [x] A4 XRPUSDT selected.
- [x] native timeframe planned as 1h.
- [x] analytical timeframes planned as 4h / Daily.
- [ ] source archive availability verified for all assets and all frozen segments.
- [ ] canonical dataset manifests/checksum plan materialized in Data Feed P1 package.
- [ ] P1 Data Feed implementation branch freshness/conflict check complete.

## Sampling

- [x] DEV segments defined.
- [x] VAL segments defined.
- [x] Structural Holdout segments defined.
- [x] Holdout anti-retuning rule defined.

## Methods

- [x] M1 operational specification drafted.
- [x] M2 operational specification drafted.
- [x] M3 operational specification drafted.
- [x] primary Close-confirmation basis defined.
- [x] M3 estimator screen defined.
- [x] diagnostic intrabar subset isolated from final candidate eligibility.

## Parameters and Structure

- [x] M1 grid drafted.
- [x] M2 grid drafted.
- [x] M3 grid drafted.
- [x] equality-tolerance grid drafted.
- [x] break-buffer grid drafted.
- [x] trend-persistence grid drafted.
- [ ] candidate thresholds reviewed and frozen.

## Comparison and Review

- [x] monotonic one-to-one swing matching drafted.
- [x] strict/base/wide matching diagnostics defined.
- [x] metrics vector defined.
- [x] hard blockers defined.
- [x] Human Review sampling protocol defined.
- [x] final P1 decision states defined.

## Implementation / Freeze

- [ ] D1 code architecture reviewed.
- [ ] experiment Code Version assigned.
- [ ] Data Version(s) assigned.
- [ ] Suite commit pinned.
- [ ] Data Feed commit pinned.
- [ ] P1 Experiment Manifest hash generated.
- [ ] P1 Design Freeze Record created.

Current state:

> **NOT READY FOR P1 DESIGN FREEZE**

No P1 execution is authorized.
