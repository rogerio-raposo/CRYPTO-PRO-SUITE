# PCP-01 — Deterministic Sampling Protocol

**Status:** FROZEN BEFORE SAMPLE DRAW  
**As-of:** 2026-10-01  
**Input population:** 22 CA-PASS assets  
**Target sample size:** 12  
**Seed:** `PCP01-FV01`

## Objective

Pilot 01 is a methodological stress test, not a population-estimation exercise.

Accordingly, sampling is designed to preserve **functional heterogeneity** rather than reproduce the exact population proportions of the 22 admitted candidates.

## Allocation rule

1. Use the frozen Functional Reference Classes.
2. Target the maximum pre-registered sample size: **12 assets**.
3. Include all members of any class whose size is **3 or fewer**.
4. Allocate all remaining sample slots to classes larger than 3.
5. If more than one class larger than 3 exists, distribute remaining slots proportionally using largest remainder.
6. Within any class requiring subsampling, select candidates by deterministic SHA-256 ordering.

For the current population this yields, before any draw:

| Class | Population | Rule | Sample allocation |
|---|---:|---|---:|
| FR-SET | 15 | subsample | 5 |
| FR-MID | 2 | include all | 2 |
| FR-ISS | 2 | include all | 2 |
| FR-MKT | 3 | include all | 3 |
| **Total** | **22** |  | **12** |

## Deterministic selection function

For each candidate that must be sampled inside a class:

```text
key = SHA256(
  "PCP01-FV01" + "|" +
  functional_class_code + "|" +
  canonical_asset_id
)
```

Sort candidates in ascending hexadecimal order of `key`.

Take the first `n` records required by the class allocation.

This construction is preferred to runtime-specific pseudo-random generators because SHA-256 ordering is reproducible across implementations.

## Anti-bias rules

The draw must not use:
- market capitalization;
- price return;
- project popularity;
- analyst preference;
- expected Ranking result;
- later E-state/Confidence;
- later liquidity result.

No manually selected “must-have” token may be inserted after the draw.

## Sample-lock rule

Once the deterministic draw is recorded:
- selected assets form the Run A candidate sample;
- non-selected CA-PASS assets remain part of the admitted population but not Run A;
- no replacement is allowed for convenience;
- later hard invalidation is recorded as a sample event, not silently replaced.

## Rationale for sample size 12

The protocol previously allowed 8–12 assets with an operational target around 10.

Twelve is chosen **before the draw** because:
- it preserves every member of the three small functional classes;
- it still limits the pairwise maximum to 66 pairs;
- it creates a more adversarial and heterogeneous methodological test than proportional sampling dominated by settlement networks.

This choice is pilot-specific and does not define future production-universe sizing.
