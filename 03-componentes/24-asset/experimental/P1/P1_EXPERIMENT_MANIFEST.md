# Asset PRO — P1 Experiment Manifest

**Status:** DRAFT / NON-NORMATIVE  
**Experiment ID:** ASSET-P1-D1-001  
**Pilot:** P1 — D1 Structural Engine Validation  
**P0 dependency:** ASSET-P0-001 = PASS  
**Freeze status:** NOT FROZEN

---

## 1. Question

Which candidate swing-detection architecture(s) provide a causal, deterministic, stable, interpretable and sufficiently responsive basis for D1 structural sequence, regime, Protected Swing and structural-event classification?

## 2. Universe

| Role | Instrument | Function |
|---|---|---|
| A1 | BTCUSDT | high-liquidity market reference |
| A2 | ETHUSDT | second large-cap, distinct structural behavior |
| A3 | SOLUSDT | liquid high-beta large-cap |
| A4 | XRPUSDT | liquid large-cap alt with distinct episodic structure |

Canonical planned market for the pilot: Binance Spot.

Historical-source eligibility for every frozen segment must be verified before P1 Design Freeze.

## 3. Data Contract

- producer repository: `rogerio-raposo/crypto-pro-datafeed`;
- isolated development branch: `experiment/asset-p1`;
- source: Binance Public Data Spot klines;
- native timeframe: 1h;
- analytical timeframes: 4h and 1d;
- boundaries: UTC;
- derived candles must use the deterministic P0-approved resampling semantics;
- large datasets remain outside Git; manifests/checksums remain auditable.

P1 producer code must be new P1 code. Frozen P0 code is not mutated.

## 4. Phase Split

- DEV: `DEV-01`, `DEV-02`;
- VAL: `VAL-01`, `VAL-02`;
- Structural Holdout: `HOLD-01`, `HOLD-02`.

The same calendar segments are used for all four assets and both analytical timeframes where source eligibility is confirmed.

## 5. Methods

- M1 — Fixed-Window Pivot;
- M2 — Fixed-Percentage Reversal;
- M3 — Volatility-Normalized Reversal.

No hybrid M4 is permitted in ASSET-P1-D1-001 unless a formal design revision is approved before VAL.

## 6. Structural Pipeline

`Swing Detector → Confirmed Structural Swings → HH/EH/LH/HL/EL/LL → Regime → Protected Swing → Structural Events`

P1 structural events include:

- Breach;
- PCSB;
- Continuation Break;
- Counter-Structural Break;
- price-based Reclaim.

Final D3-dependent Failed Break classification is excluded from P1.

## 7. Anti-Leakage Rules

P1 shall not use:

- P&L;
- future return;
- trade outcome;
- post-event price success;
- Holdout metrics for parameter tuning;
- composite weighted score.

## 8. Candidate-Lock Rule

At the end of DEV:

- only profiles satisfying all hard blockers may continue;
- profiles should belong to a documented local parameter plateau;
- at most one Responsive, one Balanced and one Conservative profile per method/timeframe continue when enough eligible profiles exist;
- the categories describe behavior, not quality.

At the end of VAL:

- provisional candidates are frozen;
- no parameter change is permitted before Holdout;
- Holdout results may confirm, reject or expose limitations, but may not retune the same experiment.

## 9. P1 Final Decision States

- `P1-PASS — Single Candidate`;
- `P1-PASS — Multiple Candidates`;
- `P1-REVISE`;
- `P1-FAIL`.

## 10. Current Status

Dataset source validation: PENDING.  
P1 Design Freeze: PENDING.  
P1 execution: NOT STARTED.
