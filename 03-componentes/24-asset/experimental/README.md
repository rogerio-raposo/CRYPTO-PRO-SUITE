# Asset PRO — Experimental Workspace

**Status:** WORKING / NON-NORMATIVE  
**Scope:** Asset PRO experimental validation artifacts  
**Date:** 2026-10-03  
**Purpose:** isolate experiment specifications, manifests, validation harness artifacts and decision records from the working methodology.

---

## 1. Governance

Artifacts in this directory do not become Asset PRO methodology merely because they are implemented or tested.

Promotion requires:

`Experiment → Decision Record → Human Gate → methodological update`.

Rejected experiments remain traceable.

## 2. Current Pilots

- `P0/` — Data & Causal Replay Integrity. **Completed with PASS.**
- `P1/` — D1 Structural Engine validation. **Preparation/materialization in progress; execution not started.**

## 3. Repository Boundary

CRYPTO-PRO-SUITE owns the experiment design, causal replay, analytical methods, validation metrics and decision records.

Historical dataset acquisition, producer-side validation, normalization, resampling and provenance are owned by the `crypto-pro-datafeed` repository.

Cross-repository formal experiments must reference immutable commit SHAs and dataset versions.

---
