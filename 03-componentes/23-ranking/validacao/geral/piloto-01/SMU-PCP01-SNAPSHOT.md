# PCP-01 — Supported Market Universe Snapshot

**Status:** CAPTURED — provisional identity layer  
**Source venue:** Binance Spot  
**Observed at:** 2026-10-01T03:19:25Z approximately  
**Data Feed commit containing snapshot:** `7cb176a9dbe294d3e256095cbcfdca79f710c463`

## Result

The experimental Data Feed generated and persisted:

`data/experimental/pcp-01/universe/binance-supported-market-universe.json`

Observed counts:
- active spot markets: **1374**;
- provisional unique base-asset symbols: **504**.

## Identity status

This is a **provisional market-derived universe**.

`baseAsset` / ticker is not sufficient canonical identity for formal Ranking assessment. Full identity resolution is required only for assets that survive Flow Vector discovery and become candidates for Current Admission.

Operational sequence:

```text
venue-native market universe
        ↓
provisional base-asset identity
        ↓
FV-01 discovery
        ↓
full canonicalization of discovered candidates
        ↓
Current Admission
```

Unresolved identity produces `CA-IND` or Eligibility `IND`; it must never be silently guessed.

## Coverage limitation

PCP-01 Run A currently uses Binance as the first technical source. The snapshot therefore represents **pilot product coverage**, not the complete economic universe of cryptoassets.
