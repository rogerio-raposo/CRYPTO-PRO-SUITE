# Asset PRO — P0 Validation Controls

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02

---

## 1. Gate Semantics

P0 final decision is binary:

- `PASS`;
- `FAIL`.

Warnings are recorded separately and do not create a third formal decision state.

## 2. Critical Controls

The following classes are blocking when applicable to the frozen experiment:

| Control | Class | P1 blocked on failure |
|---|---|---|
| Dataset schema valid | CRITICAL | Yes |
| Required OHLC invariants valid | CRITICAL | Yes |
| Timestamps ordered and unambiguous | CRITICAL | Yes |
| Unresolved duplicates absent | CRITICAL | Yes |
| Dataset checksum/provenance recorded | CRITICAL | Yes |
| Resampling deterministic | CRITICAL | Yes |
| Future candle access impossible | CRITICAL | Yes |
| Incomplete higher-TF leakage impossible | CRITICAL | Yes |
| Derived calculations consume only visible history | CRITICAL | Yes |
| Independent repeated run deterministic | CRITICAL | Yes |
| Checkpoint/restart equivalent to continuous run | CRITICAL | Yes |

## 3. Conditional Warnings

Examples:

- isolated zero volume;
- flagged extreme price move;
- flagged extreme volume;
- Non-Material gap;
- source note not affecting the frozen segment.

A warning can be escalated to a critical failure when it affects required evidence or reproducibility.

## 4. Required Determinism Runs

At minimum:

- Run A — continuous;
- Run B — independent continuous repetition;
- Run C — checkpoint/restart.

Canonical deterministic outputs SHALL satisfy equivalent hashes under the frozen serialization specification.

## 5. Look-Ahead Tests

Required test classes:

- Future Candle Access Test;
- Incomplete Higher-Timeframe Test;
- Derived Calculation Visibility Test;
- Restart State Isolation Test.

Any confirmed look-ahead violation is a critical failure.

## 6. Decision Rule

P0 PASS requires:

- no unresolved critical control failure;
- deterministic/reproducible outputs;
- provenance sufficient to reproduce the frozen dataset and harness identity.

P0 FAIL preserves its Experiment ID and Decision Record. Corrections require a formally separate execution identity.
