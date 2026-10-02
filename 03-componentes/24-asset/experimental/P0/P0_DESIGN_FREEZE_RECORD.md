# Asset PRO — P0 Design Freeze Record

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0 — Data & Causal Replay Integrity  
**Experiment ID:** ASSET-P0-001  
**Date:** 2026-10-02  
**Freeze type:** DESIGN FREEZE  
**Execution status:** NOT STARTED

---

## 1. Decision

The design of `ASSET-P0-001` is frozen for implementation.

This freeze does **not** authorize experiment execution. It authorizes implementation against the frozen design only.

## 2. Frozen Suite Manifest

- repository: `rogerio-raposo/CRYPTO-PRO-SUITE`
- manifest path: `03-componentes/24-asset/experimental/P0/P0_EXPERIMENT_MANIFEST.md`
- manifest commit: `915d3ef01c5c273348a84078ca1dfc81fe701781`

## 3. Frozen Producer-Side Design

- repository: `rogerio-raposo/crypto-pro-datafeed`
- isolated branch used during development: `experiment/asset-p0`
- frozen producer-side design commit: `35e8c1120c6d13acb16617507d770aa2b0ea0b7e`

This SHA, not the moving branch name, is the authoritative producer-side design reference for this freeze.

## 4. Frozen Design Scope

The Design Freeze covers:

- Binance Public Data as historical source;
- Binance Spot / BTCUSDT;
- native 1h klines;
- main period 2025-01-01 through 2025-04-01 UTC exclusive;
- derived 4h and Daily series;
- UTC half-open candle boundaries;
- canonical epoch-microsecond timestamps;
- canonical deterministic JSON/JSONL serialization;
- SHA-256 archive/dataset integrity model;
- strict contiguous native-data requirement for the main P0 dataset;
- Synthetic Golden Fixture design;
- Real Golden Fixture design crossing 2025-01-01;
- causal replay semantics;
- binary P0 PASS/FAIL gate;
- deterministic repeated-run and checkpoint/restart controls.

## 5. Items Explicitly Not Frozen Yet

These belong to Execution Freeze:

- producer implementation;
- replay-harness implementation;
- generated fixture bytes;
- fixture expected hashes;
- acquired main dataset bytes;
- Dataset Version;
- canonical Dataset Manifest;
- normalized dataset checksum;
- execution commit SHAs;
- Code Version;
- final Manifest hash.

## 6. Change Control

After this record, any material change to frozen design scope requires:

1. explicit identification of the proposed change;
2. rationale;
3. impact assessment;
4. Design Unfreeze/Revision Record;
5. updated specification references before implementation continues.

Editorial corrections that do not alter semantics do not require unfreeze, but remain versioned normally.

## 7. Concurrency Rule

Producer-side implementation SHALL remain isolated from parallel Data Feed work.

Before every integration with Data Feed `main`:

- compare `experiment/asset-p0` against current `main`;
- inspect overlapping paths;
- reconcile any shared-file changes explicitly;
- do not overwrite PCP-01 or unrelated experimental artifacts.

## 8. Consequence

The next authorized phase is:

> **implementation toward Execution Freeze**, not experiment execution.

P1 remains blocked until:

> P0 Execution Freeze → P0 execution → P0 Decision Record = PASS.

---

**End of Design Freeze Record**
