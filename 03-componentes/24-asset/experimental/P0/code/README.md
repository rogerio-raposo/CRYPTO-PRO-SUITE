# ASSET-P0 Causal Replay Harness

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P0-001  
**Execution status:** NOT STARTED

## Purpose

This directory contains the causal replay implementation used to prepare ASSET-P0-001 for Execution Freeze.

It contains no Asset PRO technical-analysis logic.

## Files

- `replay.py` — causal closed-candle replay, batch visibility, dataset digest, checkpoint/restart.
- `regression.py` — implementation-regression checks against a frozen fixture.

## Causal Rules

- records become visible only at or after `interval_end_us`;
- incomplete derived candles are not replay-eligible;
- records sharing the same close boundary are revealed in one deterministic batch;
- checkpoint restore must match the same dataset digest and replay position;
- future records are never provided to the consumer.

## Regression Invocation

```bash
python regression.py --fixture-root <datafeed-synthetic-fixture-directory>
```

A passing regression validates implementation behavior only. It is not the formal P0 execution and does not authorize P1.
