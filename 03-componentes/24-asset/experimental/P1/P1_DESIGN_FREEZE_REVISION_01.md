# Asset PRO — P1 Design Freeze Revision 01

**Status:** WORKING / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001  
**Date:** 2026-10-03  
**Revision:** Design Freeze Revision 01  
**Original Design Freeze:** preserved and superseded only where explicitly stated

---

## 1. Trigger

Implementation-readiness work identified two material gaps after the original Design Freeze:

1. source archives existed for all 144 required months, but continuity diagnostics detected synchronized missing 1h intervals in DEV-01 and VAL-01;
2. several frozen diagnostic metrics and implementation-edge behaviors were not operationally specified enough for deterministic code.

No formal DEV, VAL or Holdout method result had been generated.

## 2. Original Freeze Reference

Original Manifest freeze commit:

`9e234e1d5d5975ffc111309a7eafaf345e670cc7`

Original Design Freeze Record commit:

`d7e29bf179ca991018147af577ae85c60028ca30`

Both remain immutable historical records.

## 3. Revision 01 Manifest

Revised Manifest commit:

`dd36c1f2e5dbf080efab5230d5e9edeadb638b4e`

Manifest blob SHA:

`63d4eb102ec32d33e3738747d91a34cc7003272f`

Revision 01 becomes the active design baseline for implementation.

## 4. Continuity Evidence

Continuity diagnostic:

- workflow run: `37096651289`;
- artifact: `11264686520`;
- artifact digest: `sha256:bc6d5305382340ff9cf7c8a93e967eaf8ef5eeae0481bd1264cfee90bf9bbd5c`;
- dataset cells checked: 24;
- cells with duplicates: 0;
- cells with gaps: 8.

The gap timestamps are identical across all four pilot assets inside each affected segment.

### DEV-01
- 2021-02-11 04:00 UTC;
- 2021-03-06 02:00 UTC;
- 2021-04-20 02:00 UTC;
- 2021-04-20 03:00 UTC;
- 2021-04-25 05:00 UTC;
- 2021-04-25 06:00 UTC;
- 2021-04-25 07:00 UTC.

### VAL-01
- 2023-03-24 13:00 UTC.

## 5. Venue Evidence

The synchronized gaps align with Binance Spot system interruptions documented by Binance:

- Temporary System Maintenance Complete — 2021-02-11;
- Spot Trading System Upgrade Notice — 2021-03-06;
- Spot Trading System Upgrade Notice — 2021-04-20;
- Spot Trading System Upgrade Notice/Complete — 2021-04-25;
- temporary spot-trading maintenance / matching-engine interruption — 2023-03-24.

Reference pages:

- https://www.binance.com/en/support/announcement/detail/aad7639a0ed9424bad585b508a61a433
- https://www.binance.com/en/support/announcement/detail/f02cab4e685b46da803bb0a680546d4b
- https://www.binance.com/en/support/announcement/detail/69e82a64b2c442b18eb1cf11934b27eb
- https://www.binance.com/kk-KZ/support/announcement/detail/849160fe70214641baa6385619595aa1
- https://www.binance.com/en/support/announcement/detail/813a31506e9f478ea8c1058b425df87a

## 6. Data-Design Revision

The original DEV/VAL/Holdout calendar windows remain unchanged.

Registered synchronized venue gaps are accepted under these constraints:

- no interpolation;
- no synthetic candle insertion;
- incomplete derived 4h/Daily candles are excluded;
- each affected analytical stream is split into contiguous Analysis Islands;
- all D1 state resets at island boundaries;
- no swing, regime, Protected Swing or event may span an island boundary;
- metrics aggregate across islands but never calculate durations/matches across boundaries.

Any new gap that is not in the frozen registry, or whose timestamps differ across pilot assets, blocks Execution Freeze pending explicit adjudication.

## 7. Method Clarifications

Revision 01 freezes deterministic behavior for:

- M1 same-type confirmed pivots;
- M2 dual-extrema bootstrap and ambiguous initial triggers;
- M3 initialization only after the volatility estimator is available;
- strict candidate-extremum updates;
- same-bar event/swing processing order;
- latest-only generic swing references;
- Range outer boundaries;
- opposing-cycle Transition logic.

Canonical rules are in `P1_METHOD_SPECIFICATIONS.md`.

## 8. Metric Clarifications

Revision 01 freezes:

- Swing Stability formula;
- fragmentation/omission diagnostics;
- Confirmation Delay;
- Regime Churn;
- structural definition of Short-Lived Regime;
- Transition/Indeterminate utilization;
- Protected Swing turnover/stability;
- missing-Protected diagnostic;
- structural-event matching/stability/delay;
- event-order consistency;
- plateau width;
- cross-asset/timeframe reporting;
- anomaly and matching-sensitivity diagnostics.

Canonical rules are in `P1_METRICS_SPECIFICATION.md`.

## 9. Human Review Clarifications

Review is strictly causal:

- 4h trailing context: 120 evaluable bars;
- Daily trailing context: 90 evaluable bars;
- no future bar after the focal timestamp;
- windows never cross an Analysis Island;
- deterministic tie-breaking by earliest timestamp.

Canonical rules are in `P1_HUMAN_REVIEW_PROTOCOL.md`.

## 10. Consequence

P1 implementation may proceed only against Revision 01.

Formal P1 execution remains prohibited until Execution Freeze.

---

**End of Design Freeze Revision 01**
