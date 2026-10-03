# Asset PRO — P1 Freeze Checklist

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

# A. Design Freeze Checklist

## Dependency

- [x] ASSET-P0-001 Decision Record = PASS.

## Universe and Data Design

- [x] A1 BTCUSDT selected.
- [x] A2 ETHUSDT selected.
- [x] A3 SOLUSDT selected.
- [x] A4 XRPUSDT selected.
- [x] Binance Spot planned as common pilot market.
- [x] native timeframe planned as 1h.
- [x] analytical timeframes planned as 4h / Daily.
- [x] source archive availability verified for all assets and all frozen segments — 36/36 months each.
- [x] canonical dataset-manifest/checksum plan materialized in Data Feed P1 package.
- [x] P1 Data Feed branch freshness/conflict check completed for Design Freeze — branch 0 behind main; no PCP-01 path modified by P1 work.

## Sampling

- [x] DEV segments defined.
- [x] VAL segments defined.
- [x] Structural Holdout segments defined.
- [x] common-calendar rule defined.
- [x] Holdout anti-retuning rule defined.

## Methods

- [x] M1 operational specification drafted.
- [x] M2 operational specification drafted.
- [x] M3 operational specification drafted.
- [x] primary Close-confirmation basis defined.
- [x] M3 estimator screen defined.
- [x] diagnostic intrabar subset isolated from final-candidate eligibility.

## Parameters and Structure

- [x] M1 grid drafted.
- [x] M2 grid drafted.
- [x] M3 grid drafted.
- [x] equality-tolerance grid drafted.
- [x] break-buffer grid drafted.
- [x] trend-persistence grid drafted.
- [x] arbitrary fixed stability thresholds reviewed and removed.
- [x] DEV IQR plateau/reference-band methodology drafted.
- [x] DEV IQR plateau/reference-band methodology formally accepted for Design Freeze.

## Comparison and Review

- [x] monotonic one-to-one swing matching drafted.
- [x] strict/base/wide matching diagnostics defined.
- [x] metrics vector defined.
- [x] hard blockers defined.
- [x] Human Review sampling protocol defined.
- [x] final P1 decision states defined.

## Design Freeze Record

- [x] all design documents reviewed for internal consistency.
- [x] Design Freeze baseline commit pinned — manifest commit `9e234e1d5d5975ffc111309a7eafaf345e670cc7`.
- [x] P1 Design Freeze Record created.

Current Design Freeze state:

> **COMPLETE — REVISION 03**

---

# B. Execution Freeze Checklist

Execution Freeze is intentionally separate and is not required to close the current design stage.

## Producer / Data

- [x] multi-asset P1 producer core implemented.
- [ ] synchronized venue-gap/island policy implemented and validated.
- [ ] source archives acquired and checksums verified.
- [ ] per-asset/per-segment Dataset Manifests generated.
- [ ] Data Versions pinned.
- [x] Holdout analytical-access segregation core implemented; regression pending.

## D1 Structural Engine

- [x] M1 implemented.
- [x] M2 implemented.
- [x] M3 implemented.
- [x] structural sequence implemented.
- [x] regime classifier implemented.
- [x] Protected Swing implemented.
- [x] P1 structural-event taxonomy implemented.
- [x] matching engine implemented.
- [ ] metrics/plateau/reference-band engine implemented against Revision 02.
- [ ] Human Review deterministic sampling/export implemented against Revision 03.

## Validation

- [ ] causal replay regression passes.
- [ ] deterministic repeated-run regression passes.
- [ ] checkpoint/restart regression passes.
- [ ] synthetic/reference tests pass.
- [ ] Code Version assigned.
- [ ] Suite implementation commit pinned.
- [ ] Data Feed implementation commit pinned.
- [ ] P1 frozen Manifest hash generated.
- [ ] Execution Freeze Record created.

Current Execution Freeze state:

> **NOT STARTED**

No P1 method execution is authorized.
