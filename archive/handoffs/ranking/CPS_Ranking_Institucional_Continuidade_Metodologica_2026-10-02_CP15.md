# CRYPTO PRO SUITE
## Ranking Institucional Simplificado — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP15  
**Checkpoint anterior:** CP14  
**Ponteiro operacional de continuidade:** `archive/handoffs/ranking/README.md`  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Ranking Institucional Simplificado — Metodologia Geral  
**Finalidade:** snapshot autônomo do estado imediatamente anterior ao human UFT gate do PCP-01.

---

# 1. Regras permanentes de retomada

- Repositório e documentação persistida são fonte de verdade.
- Memória orienta recuperação, não substitui evidência.
- Não preencher lacunas por inferência.
- Não transformar proposta em decisão.
- Não generalizar Microcaps para Ranking Geral sem decisão explícita.
- Handoffs são operacionais, não normativos.
- Freshness Gate é obrigatório antes de retomar.
- O prompt operacional existe somente em `archive/handoffs/ranking/README.md`.

---

# 2. Fenômeno-alvo e arquitetura vigente

Fenômeno-alvo:
> captura de fluxo institucional relevante no horizonte de análise.

Unidade elementar:
`Asset × Flow Vector × Horizon × As-of`.

Constructos nucleares:
- Causal Exposure;
- Economic Capture;
- Structural Position;
- Capacity = Institutional Accessibility + Absorption;
- Frictions;
- Confidence;
- Trajectory;
- Driver explicativo.

Materiality Confirmed PASS:
`Exposure >= E2/C3+ AND Capture >= E2/C3+`.

Capacity Confirmed PASS:
`Accessibility >= E2/C3+ AND Absorption >= E2/C3+`.

Sem score cardinal obrigatório, sem pesos e sem média simples entre constructos.

---

# 3. PCP-01 congelado

- desenho: static / cross-sectional / controlled / adversarial;
- FV-01: Institutional Tokenization & Onchain Capital Markets Infrastructure;
- horizonte: 90 dias após T0;
- RIP-01: Direct Digital-Asset-Capable Professional Allocator;
- RAS-01: USD 5 milhões / 24h;
- 24 child orders de aproximadamente USD 208.3k;
- Trajectory fora do Run A;
- retorno futuro não valida o piloto.

Run A:
`PLUME, OP, APT, ADA, SUI, LINK, QNT, ONDO, RSR, INJ, HYPE, SYRUP`.

Capacity population:
- Confirmed: `PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`;
- Provisional: `APT`;
- Materiality FAIL: `ADA, QNT, ONDO`.

---

# 4. Relationship / Position current state

| Asset | Exposure | Capture | Materiality | Position |
|---|---|---|---|---|
| PLUME | E4/C3 | E3/C3 | PASS | E3/C3 |
| OP | E2/C3 | E2/C3 | PASS | E2/C3 |
| APT | E3/C3 | E2/C2 | Provisional | E3/C4 |
| ADA | E2/C3 | E1/C3 | FAIL | — |
| SUI | E3/C3 | E2/C3 | PASS | E2/C3 |
| LINK | E3/C4 | E3/C4 | PASS | E4/C4 |
| QNT | E3/C4 | E1/C4 | FAIL | — |
| ONDO | E4/C4 | E1/C3 | FAIL | — |
| RSR | E3/C3 | E3/C4 | PASS | E2/C3 |
| INJ | E2/C3 | E2/C4 | PASS | E3/C3 |
| HYPE | E2/C3 | E2/C3 | PASS | E2/C3 |
| SYRUP | E4/C4 | E3/C4 | PASS | E3/C3 |

MGR-008 ONDO remains resolved.  
MGR-006 prospective institutional validation remains open as diagnostic.  
MGR-009 comparator heterogeneity remains open and non-blocking PRE-T0.

---

# 5. Capacity protocol

Accessibility:
- A1 Execution Access;
- A2 Custody/Holding Path;
- A3 Settlement/Transferability;
- A4 Access Resilience.

Absorption:
- child notional ≈ USD 208,333;
- standard depth = 1000 levels;
- escalate to target 5000 where required;
- 24 hourly events planned;
- >=18 valid required;
- median PEC threshold statistic;
- P90 diagnostic;
- PR = RAS / median daily qualified spot turnover over exact 7d.

Thresholds:
- E4: PEC <=0.50% AND PR <=2%;
- E3: PEC <=1.00% AND PR <=5%;
- E2: PEC <=2.00% AND PR <=10%.

Binance can prove E2 sufficiency alone. Binance-only failure cannot prove E1/E0 without the frozen source-expansion process.

---

# 6. Two-cycle dry-run — PASS

Authoritative Data Feed status:
`two_cycle_status = PASS`.

Workflow run:
`37059995273`.

Qualified cycles:
- A — `2026-10-02T20:00:00Z` — PASS 9/9;
- B — `2026-10-02T21:00:00Z` — PASS 9/9.

The pair is adjacent in UTC and the workflow verification step completed successfully.

The prior scheduler defect is resolved without changing the pre-registered rule.

---

# 7. QEV declaration

The nine frozen Binance Spot USDT mappings are now:
`QUALIFIED / DECLARED FOR PCP-01`.

Markets:
`PLUMEUSDT, OPUSDT, APTUSDT, SUIUSDT, LINKUSDT, RSRUSDT, INJUSDT, HYPEUSDT, SYRUPUSDT`.

QEV qualification is not an Institutional Accessibility PASS.

RSR remains a depth-escalation diagnostic, not an Absorption FAIL.

---

# 8. Parallel Data Feed work / conflict control

Data Feed main at the conflict review:
`8e77307af7e37d472875c4a6435778036e540dfc`.

Parallel Asset PRO work:
`experiment/asset-p0`.

Ranking Capacity work:
`experiment/pcp01-capacity`.

Asset PRO changes reviewed at the branch-isolation point affected only `docs/experimental/asset-p0/`.

PCP-01 official capture changes are isolated to the PCP-01 branch.

No merge to Data Feed main is required before the human gate.

Before activation:
- re-fetch main;
- compare both experiment branches;
- verify no overlapping file changes;
- freeze execution ref/commit.

---

# 9. Official capture orchestration

The former recurring cron is not relied upon for official capture because scheduler latency was empirically observed during dry-run qualification.

Controlled official-capture branch:
`experiment/pcp01-capacity`.

Current implementation commit:
`d439e1b29586cd08b560183654877bf16687337b`.

Design:
- manual workflow dispatch;
- sequential bounded segments covering events 00–23;
- target-hour waiting inside each segment;
- materially late target rejection;
- segment persistence on isolated branch;
- exact seven-day turnover collection at T0.

This is an operational engineering change only.

---

# 10. Current readiness

Etapa 60 has reached:
> **READY FOR HUMAN UFT GATE**.

Satisfied:
- configuration;
- universe/canonicalization/discovery/sample;
- QEV mapping;
- controlled two-cycle PASS;
- QEV declaration;
- capture/turnover producers;
- controlled official capture timing;
- Accessibility rubric;
- Absorption protocol;
- source-expansion rule.

Still not declared:
- UFT;
- Capture Start;
- T0;
- H dates;
- official activation;
- Capacity E-states;
- Ranking Classes.

---

# 11. Ponto exato de retomada

The next action is a **human gate**.

If the user authorizes UFT/T0 initiation:
1. perform final Data Feed freshness/branch-overlap check;
2. freeze execution commit/ref;
3. set UFT;
4. choose the next suitable full UTC hour as Capture Start, allowing enough lead time for workflow dispatch;
5. set T0 = Capture Start + 24h;
6. set H = T0 + 90d;
7. write and commit activation on `experiment/pcp01-capacity`;
8. manually dispatch the official workflow on that branch;
9. monitor technical validity through T0.

Do not activate official capture before explicit user authorization.
