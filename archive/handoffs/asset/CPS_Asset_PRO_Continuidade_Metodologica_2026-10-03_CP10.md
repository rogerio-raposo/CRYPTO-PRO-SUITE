# CRYPTO PRO SUITE
## Asset PRO — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-03  
**Checkpoint:** CP10  
**Checkpoint anterior:** CP09  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Asset PRO — Metodologia Geral  
**Finalidade:** preservar o marco em que ASSET-P1-D1-001 está em Design Freeze e autorizado exclusivamente para implementação rumo ao Execution Freeze.  
**Ponteiro operacional de continuidade:** `archive/handoffs/asset/README.md`

---

# 1. Marco do CP10

Estado formal:

> **P0 = PASS**  
> **P1 Design Freeze = COMPLETE**  
> **P1 implementation = NOT STARTED**  
> **P1 Execution Freeze = NOT STARTED**  
> **P1 formal execution = NOT STARTED**

---

# 2. Frozen P1 identity

Experiment:

`ASSET-P1-D1-001`

Design Freeze manifest:

- commit: `9e234e1d5d5975ffc111309a7eafaf345e670cc7`;
- blob SHA: `649fc0d5e7d90ec4e0c257cd1b03554ee1a6e482`.

Design Freeze Record:

- commit: `d7e29bf179ca991018147af577ae85c60028ca30`.

---

# 3. Frozen universe

- A1 BTCUSDT;
- A2 ETHUSDT;
- A3 SOLUSDT;
- A4 XRPUSDT;
- Binance Spot;
- native 1h;
- analytical 4h and Daily.

Source eligibility:

- BTCUSDT 36/36 months;
- ETHUSDT 36/36 months;
- SOLUSDT 36/36 months;
- XRPUSDT 36/36 months;
- workflow run `37095698535` = success.

---

# 4. Frozen phase design

DEV:
- DEV-01: 2021-01-01 → 2021-07-01 UTC exclusive;
- DEV-02: 2022-06-01 → 2022-12-01 UTC exclusive.

VAL:
- VAL-01: 2023-01-01 → 2023-07-01 UTC exclusive;
- VAL-02: 2023-07-01 → 2024-01-01 UTC exclusive.

Structural Holdout:
- HOLD-01: 2024-01-01 → 2024-07-01 UTC exclusive;
- HOLD-02: 2024-07-01 → 2025-01-01 UTC exclusive.

Holdout analytical outputs may not be used for tuning.

---

# 5. Frozen methods and semantics

- M1 Fixed-Window Pivot;
- M2 Fixed-Percentage Reversal;
- M3 Volatility-Normalized Reversal;
- Close-confirmed primary reversal basis;
- M3 estimator screen: Wilder ATR vs rolling Median True Range;
- confirmed swings immutable;
- extremum timestamp distinct from confirmation timestamp;
- causal ATR reference timing frozen;
- directional structural-cycle definition frozen;
- Regime rules frozen;
- Protected Swing promotion frozen;
- P1 structural events: Breach, PCSB, Continuation Break, Counter-Structural Break, Reclaim;
- D3 Acceptance/Re-Acceptance excluded.

---

# 6. Frozen parameter design

M1:
- 4h: w ∈ {2,3,4,6,8,12};
- Daily: w ∈ {2,3,4,5,7,10}.

M2:
- 4h: p ∈ {1.0%,1.5%,2.5%,4.0%,6.0%,9.0%};
- Daily: p ∈ {2.0%,3.0%,5.0%,8.0%,12.0%,18.0%}.

M3:
- screen: n=14, k=2.0;
- n ∈ {10,14,21,34};
- k ∈ {1.0,1.5,2.0,2.5,3.0,4.0}.

Structural grid:
- q ∈ {0.25,0.50,0.75};
- b ∈ {0,0.25,0.50};
- m ∈ {2,3}.

---

# 7. Frozen validation logic

- no P&L;
- no future return;
- no weighted score;
- no Holdout retuning;
- DEV local plateaus via componentwise robust IQR fences;
- DEV reference bands frozen before VAL;
- VAL tests frozen candidates;
- Holdout tests VAL-locked provisional candidates;
- retuning requirement → P1-REVISE.

---

# 8. Concurrency / repository state

Data Feed P1 branch:

`experiment/asset-p1`

Frozen design/evidence commit:

`199c301b5ee14a1b322b86d4b992d4de9d2157cf`

At freeze:

- 25 commits ahead of Data Feed main;
- 0 behind;
- no P1 modification to `pcp-01` paths.

P1 implementation must remain isolated from PCP-01 and must not mutate frozen P0 evidence.

---

# 9. Ponto exato de retomada

## Etapa 44 — Implementação do P1/D1 rumo ao Execution Freeze

Objetivo:

> implementar o producer multiativo, os datasets/manifests, o D1 Structural Engine, matching/metrics/review tooling e os controles de determinismo/Holdout necessários ao Execution Freeze, sem executar DEV, VAL ou Holdout formalmente.

Ordem recomendada:

1. criar branch de implementação da Suite;
2. generalizar producer P1 no Data Feed sem mutar P0;
3. adquirir/validar datasets por asset×segment;
4. implementar Holdout access segregation;
5. implementar M1;
6. implementar M2;
7. implementar M3;
8. implementar structural sequence/regime;
9. implementar Protected Swing;
10. implementar P1 structural events;
11. implementar matching;
12. implementar metrics/plateau engine;
13. implementar Human Review export;
14. criar fixtures/reference tests;
15. validar determinismo/restart;
16. revisar código;
17. pin Code/Data Versions;
18. preparar Execution Freeze.

Regra:

> nenhum resultado DEV/VAL/Holdout formal pode ser produzido antes do Execution Freeze.

---

**Fim do CP10**
