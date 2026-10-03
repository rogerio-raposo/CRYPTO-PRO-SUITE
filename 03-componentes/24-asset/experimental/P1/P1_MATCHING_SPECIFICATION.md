# Asset PRO — P1 Swing Matching Specification

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

## 1. Purpose

Compare whether two methods/profiles identify approximately the same structural swing without requiring identical timestamps or prices.

Matching is an experimental comparison tool. It is not part of final D1 market semantics.

## 2. Eligibility

A pair may match only when:

- both swings have the same type: High↔High or Low↔Low;
- their extremum timestamps are within the active time window;
- normalized price distance is within the active price window.

Normalized price distance:

[
D_p = |P_a-P_b|/ATR14
]

ATR14 is the method-independent structural comparator volatility at the later of the two causal comparison timestamps.

## 3. Primary Matching Window

### 4h
- maximum extremum distance: 3 bars;
- maximum price distance: 1.0 ATR14.

### Daily
- maximum extremum distance: 2 bars;
- maximum price distance: 1.0 ATR14.

## 4. Matching Sensitivity Diagnostics

Strict:
- 4h: 2 bars / 0.5 ATR;
- Daily: 1 bar / 0.5 ATR.

Wide:
- 4h: 6 bars / 1.5 ATR;
- Daily: 3 bars / 1.5 ATR.

Matching-sensitivity results are diagnostic and cannot be selectively substituted after results are known.

## 5. One-to-One Monotonic Alignment

Matching must preserve chronological order and be one-to-one.

Optimization is lexicographic:

1. maximize number of eligible matched pairs;
2. minimize total absolute bar-distance;
3. minimize total normalized price-distance;
4. deterministic earliest-timestamp tie break.

No weighted matching score is used.

## 6. Outputs

For every comparison:

- matched pairs;
- unmatched swings from A;
- unmatched swings from B;
- temporal displacement;
- normalized price displacement;
- fragmentation indicators;
- omission indicators.
