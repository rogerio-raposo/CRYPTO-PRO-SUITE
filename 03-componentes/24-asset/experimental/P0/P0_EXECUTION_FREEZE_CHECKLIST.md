# Asset PRO — P0 Execution Freeze Checklist

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P0-001  
**Date:** 2026-10-02  
**Execution Freeze:** PENDING

---

## 1. Design and Governance

- [x] P0 design frozen.
- [x] Experiment ID fixed as `ASSET-P0-001`.
- [x] Data Feed work isolated on `experiment/asset-p0`.
- [x] Current Data Feed branch has no overlap with PCP-01 paths.
- [x] P1 remains blocked until P0 PASS.

## 2. Producer-Side Implementation

- [x] canonical decimal normalization implemented.
- [x] explicit source timestamp-unit normalization implemented.
- [x] Binance ZIP parser implemented.
- [x] official SHA-256 checksum verification implemented.
- [x] OHLC/timestamp/duplicate/gap validation implemented.
- [x] deterministic 1h → 4h / 1d resampling implemented.
- [x] canonical JSON/JSONL serialization implemented.
- [x] dataset/fixture builder implemented.

## 3. Synthetic Golden Fixture

- [x] fixture bytes generated.
- [x] deliberate missing interval present.
- [x] deliberate extreme OHLC-valid observation present.
- [x] expected 4h / 1d outputs generated.
- [x] producer hashes frozen.
- [x] fixture committed to isolated Data Feed branch.

## 4. Causal Replay Harness

- [x] closed-candle replay implemented.
- [x] incomplete derived candles excluded from replay eligibility.
- [x] deterministic batch ordering implemented.
- [x] checkpoint/restart implemented.
- [x] dataset-digest validation implemented.
- [x] future-record visibility guard implemented.
- [x] synthetic continuous/repeat/restart regression hashes equal.

## 5. Runtime Validation

- [x] local regression executed successfully on Python 3.13.5.
- [x] source parses under Python 3.12 grammar.
- [ ] runtime regression executed on Python 3.12.

Python 3.12 runtime validation remains mandatory because it is the stable Data Feed engineering baseline.

## 6. Real Golden Fixture

- [ ] official daily archives acquired.
- [ ] official archive checksums verified.
- [ ] 72 expected native intervals validated.
- [ ] millisecond → microsecond source transition verified.
- [ ] normalized fixture generated.
- [ ] 4h / 1d expected outputs generated.
- [ ] fixture hashes frozen.
- [ ] fixture committed/referenced.

## 7. Main Validation Dataset

- [ ] January 2025 monthly archive acquired/verified.
- [ ] February 2025 monthly archive acquired/verified.
- [ ] March 2025 monthly archive acquired/verified.
- [ ] 2160 contiguous 1h intervals validated.
- [ ] 540 complete 4h records validated.
- [ ] 90 complete Daily records validated.
- [ ] canonical normalized dataset generated.
- [ ] Dataset Version finalized.
- [ ] canonical Dataset Manifest generated.
- [ ] final dataset SHA-256 frozen.

## 8. Code and Cross-Repository Freeze

- [x] producer code review complete.
- [x] replay code review complete.
- [ ] final Data Feed implementation commit pinned.
- [ ] final Suite implementation commit pinned.
- [ ] final Code Version declared.
- [ ] P0 Experiment Manifest updated with execution identities.
- [ ] final Manifest hash computed.
- [ ] final freshness/conflict check against Data Feed `main`.

## 9. Execution Freeze Decision

Execution Freeze may be declared only when every required item above is complete or explicitly adjudicated through a documented revision.

Current decision:

> **NOT READY FOR EXECUTION FREEZE**

Formal P0 execution remains prohibited.

---

**End of Execution Freeze Checklist**
