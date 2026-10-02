# Asset PRO — P0 Data & Causal Replay Integrity

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02  
**Execution status:** NOT STARTED

---

## Purpose

P0 verifies that the historical validation environment is causal, deterministic, auditable and reproducible before any D1/P1 experiment is authorized.

## Package

- `P0_EXPERIMENT_MANIFEST.md`
- `P0_REPLAY_SPECIFICATION.md`
- `P0_VALIDATION_CONTROLS.md`
- `P0_FIXTURE_EXPECTATIONS.md`
- `P0_DECISION_RECORD.md`

## Current Data Feed Baseline

Initial materialization reference:

- repository: `rogerio-raposo/crypto-pro-datafeed`
- commit: `073fe17d969655c46780261663c6d86f6804216d`
- experimental package: `docs/experimental/asset-p0/`

This is a materialization baseline, **not yet an Experiment Freeze**.

## Gate

P1 remains blocked until the P0 Decision Record records `PASS`.
