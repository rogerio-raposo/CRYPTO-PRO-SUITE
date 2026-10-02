# CRYPTO PRO SUITE
## Ranking Institucional Simplificado — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP14  
**Checkpoint anterior:** CP13  
**Ponteiro operacional de continuidade:** `archive/handoffs/ranking/README.md`  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Ranking Institucional Simplificado — Metodologia Geral  
**Finalidade:** registrar um snapshot autônomo do estado de trabalho corrente para retomada controlada, sem depender da memória do modelo e sem carregar cumulativamente os checkpoints anteriores.  
**Nota:** snapshot autônomo no modelo **snapshot + pointer**, posterior à migração iniciada no CP13.

---

# 1. Regras de fonte e continuidade

- Repositório e documentos persistidos são a fonte de verdade.
- Memória do modelo pode orientar recuperação, mas não constitui evidência.
- Não preencher lacunas por inferência.
- Não transformar proposta histórica em decisão vigente.
- Não transformar este handoff em documento normativo.
- Distinguir explicitamente: histórico, vigente, superado, proposto, adiado, indeterminado e decisão de trabalho.
- Não generalizar automaticamente a metodologia Microcaps para o Ranking Geral.
- Não reabrir trabalho já validado sem nova evidência, conflito documental, mudança de autoridade ou decisão posterior.
- Alterações posteriores na branch `main` e em dependências operacionais relevantes prevalecem quando tiverem maior autoridade ou atualidade factual.
- O procedimento de retomada e o prompt operacional não ficam neste checkpoint; ficam exclusivamente em `archive/handoffs/ranking/README.md`.

Fontes de conversa anteriormente excluídas ou limitadas:
- `roadmap-do-crypto-pro.md`: não reutilizar como nova fonte de decisão nesta linha metodológica;
- “Critérios para Escolha de Criptomoedas, Avaliação de Tokenomics e Ajustes para Microcaps”: uso apenas exploratório/hipotético, não normativo.

---

# 2. Fenômeno-alvo e unidade de análise

Fenômeno-alvo vigente:

> **captura de fluxo institucional relevante no horizonte de análise.**

Finalidade operacional:

> estimar quais criptoativos estão relativamente mais bem posicionados para capturar fluxo institucional adicional no horizonte considerado, incluindo continuidade/intensificação de fluxos vigentes e emergência de novos vetores.

Unidade metodológica elementar:

`Asset × Flow Vector × Horizon × As-of`

A saída comparativa final continua sendo o ativo, mas a relação é avaliada no contexto explícito do vetor e horizonte.

Regra temporal:
- evidência disponível até `t0`;
- fenômeno prospectivo em `(t0, t0 + H]`;
- fluxo já ocorrido pode informar persistência, aceleração, desaceleração, saturação ou reversão;
- fluxo realizado não é confundido automaticamente com fluxo futuro.

---

# 3. Fronteiras do módulo

O Ranking permanece módulo independente.

Não pertence ao núcleo do Ranking:
- Full Technical Analysis / timing — pertence ao Asset PRO;
- reconstrução de Institutional Flow agregado;
- recalcular força de narrativa;
- full tokenomics;
- Portfolio Construction / sizing — pertence ao CSE;
- decisão final de investimento.

O Ranking consome contexto upstream e produz classificação comparativa auditável sem duplicar módulos vizinhos.

MEL — Methodology Evaluation Layer:
- componente interno do Ranking;
- não é módulo independente;
- inclusão na versão inicial formal da Suite permanece adiada até fechamento dos demais módulos.

---

# 4. Arquitetura metodológica vigente

## 4.1 Relação Asset–Vector

Constructos nucleares:
1. **Causal Exposure**
2. **Economic Capture**
3. **Structural Position**

Materiality Gate:
- Confirmed PASS = Exposure >= E2/C3+ AND Capture >= E2/C3+;
- Confirmed FAIL = Exposure <= E1/C3+ OR Capture <= E1/C3+ com evidência suficiente;
- C2 pode produzir estado Provisional;
- evidência insuficiente/conflitante pode produzir IND.

Structural Position:
- não participa do Materiality Gate;
- é relativo ao `PCP-01 Position Reference Universe`;
- não pode compensar deficiência material de Exposure ou Capture;
- não autoriza alegações globais de liderança quando o PRU é limitado pela cobertura do Supported Market Universe.

## 4.2 Capacity

Subconstructos:
1. **Institutional Accessibility**
2. **Absorption Capacity**

Gate:
- Confirmed PASS = Accessibility >= E2/C3+ AND Absorption >= E2/C3+;
- qualquer componente <= E1/C3+ pode produzir FAIL quando a evidência e cobertura forem suficientes;
- C2 pode gerar Provisional;
- insuficiência/conflito/coverage ambiguity pode gerar CAP-IND.

Accessibility e Absorption são não compensatórios no gate.

## 4.3 Frictions

Famílias vigentes:
- Regulatory / Legal;
- Supply / Dilution;
- Concentration / Control;
- Protocol / Security;
- Governance / Dependency;
- Market-Structure / Counterparty.

Escala:
`F0–F4 + IND`

Efeitos possíveis:
- Flag;
- Modifier;
- Comparative Veto;
- Blocker.

Não existe penalidade aritmética universal.

## 4.4 Confidence

Escala:
- C0 — Insufficient;
- C1 — Low;
- C2 — Moderate;
- C3 — High;
- C4 — Very High.

Confidence é epistemológico, avaliado por constructo, não score de mérito.

## 4.5 Trajectory

Estados:
- Strengthening;
- Stable;
- Deteriorating;
- IND.

Trajectory mede evolução da evidência/constructo, não momentum de preço e não integra o Run A do PCP-01.

## 4.6 Driver

Driver permanece explicativo e não integra score.

---

# 5. Motor comparativo

Arquitetura vigente:
1. Gates;
2. Pareto dominance;
3. blocos positivos de comparação;
4. non-compensatory outranking;
5. preference graph;
6. SCCs/cycles;
7. condensation DAG;
8. Preference Layers;
9. Ranking Classes.

Saídas pairwise:
- DOMINATES;
- OUTRANKS;
- EQUIVALENT;
- INCOMPARABLE;
- UNRESOLVED.

`Δ0–Δ3` expressa diferença semântica/econômica, não subtração de códigos ordinais.

Comparative Veto exige condição forte e evidência robusta; veto bilateral conduz a incomparabilidade.

Não há:
- score cardinal obrigatório;
- pesos definidos;
- média simples entre constructos;
- regra de vitória por contagem de vetores;
- centralidade do grafo interpretada como mérito econômico.

---

# 6. Supported Market Universe e fonte de dados

O Ranking não assume varredura exaustiva do universo global.

Fluxo operacional:
`Approved/Supported Market Sources → Supported Market Universe → Eligibility → Current Admission → Data Sufficiency → Materiality → Capacity → Frictions/Confidence → Ranking-Ready Universe`

O Supported Market Universe representa cobertura do produto, não mérito do ativo.

Para o PCP-01:
- cobertura experimental corrente = Binance Spot;
- isso minimiza mudanças de engenharia e não constitui seleção comercial definitiva;
- commercial source approval permanece DEFERRED para o piloto metodológico;
- eventual uso comercial exige gate próprio de direitos/licenciamento;
- Data Feed é o produtor de aquisição, normalização e provenance;
- Ranking interpreta os dados e calcula estados metodológicos.

---

# 7. PCP-01 — configuração congelada

Tipo:
- static;
- cross-sectional;
- controlled;
- adversarial.

Parâmetros:
- Flow Vector: `FV-01 — Institutional Tokenization & Onchain Capital Markets Infrastructure`;
- horizonte: 90 dias após T0;
- RIP-01: `Direct Digital-Asset-Capable Professional Allocator (DDAPA)`;
- RAS-01: USD 5 milhões em até 24h;
- 24 child orders de aproximadamente USD 208,333;
- sem pesos;
- sem score agregado;
- Trajectory fora do Run A;
- retorno/preço futuro não valida o Run A.

Run A sample congelado:
`PLUME, OP, APT, ADA, SUI, LINK, QNT, ONDO, RSR, INJ, HYPE, SYRUP`.

---

# 8. PRE-T0 Relationship — estado corrente

| Asset | Exposure | Capture | Materiality | Structural Position | Estado |
|---|---|---|---|---|---|
| PLUME | E4/C3 | E3/C3 | Confirmed PASS | E3/C3 | Relationship complete |
| OP | E2/C3 | E2/C3 | Confirmed PASS | E2/C3 | Relationship complete |
| APT | E3/C3 | E2/C2 | Provisional PASS | E3/C4 | Provisional |
| ADA | E2/C3 | E1/C3 | Confirmed FAIL | not assigned | stops at Materiality |
| SUI | E3/C3 | E2/C3 | Confirmed PASS | E2/C3 | Relationship complete |
| LINK | E3/C4 | E3/C4 | Confirmed PASS | E4/C4 | Relationship complete |
| QNT | E3/C4 | E1/C4 | Confirmed FAIL | not assigned | stops at Materiality |
| ONDO | E4/C4 | E1/C3 | Confirmed FAIL | not assigned | stops at Materiality |
| RSR | E3/C3 | E3/C4 | Confirmed PASS | E2/C3 | Relationship complete |
| INJ | E2/C3 | E2/C4 | Confirmed PASS | E3/C3 | Relationship complete |
| HYPE | E2/C3 | E2/C3 | Confirmed PASS | E2/C3 | Relationship complete |
| SYRUP | E4/C4 | E3/C4 | Confirmed PASS | E3/C3 | Relationship complete |

Confirmed Relationship-complete:
`PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`

Provisional:
`APT`

Materiality FAIL:
`ADA, QNT, ONDO`

Important:
- ONDO result remains methodologically valid under the current construct: platform/franchise success does not equal current token Economic Capture; MGR-008 is resolved.
- QNT remains the main MGR-006 prospective institutional-validation pattern; no method change authorized.
- no Materiality state was changed because of ex-post price behavior.

---

# 9. Evidence completeness and Position

PRE-T0 Material Event Completeness Audit completed.

Material omissions were found and versioned for multiple assets. Relationship changes:
- QNT confidence correction handled separately;
- INJ Capture confidence corrected to C4;
- no Materiality PASS/FAIL changed.

MGR-007:
- resolved for PRE-T0 baseline;
- same completeness discipline must be repeated before official T0 Evidence Pack freeze.

Structural Position rule:
- comparator universe = all CA-PASS assets in the same frozen Functional Reference Class within SMU-PCP01;
- sampled and non-sampled comparators are distinguished;
- non-sampled comparators receive lightweight RCP evidence only;
- raw TVL/AUM/partnership counts are not converted into arithmetic Position scores.

MGR-009 remains open:
- comparator heterogeneity, especially FR-SET metric definitions and FR-MKT subfunctions;
- non-blocking for PRE-T0;
- FR-MKT confidence capped at C3 in PCP-01.

---

# 10. Capacity — protocol congelado

Capacity population:
- Confirmed: `PLUME, OP, SUI, LINK, RSR, INJ, HYPE, SYRUP`;
- Provisional: `APT`;
- ADA, QNT and ONDO do not proceed to Capacity in Run A.

Frozen Binance Spot QEV mapping:
- PLUMEUSDT;
- OPUSDT;
- APTUSDT;
- SUIUSDT;
- LINKUSDT;
- RSRUSDT;
- INJUSDT;
- HYPEUSDT;
- SYRUPUSDT.

QEV status remains formally UNDECLARED until two-cycle dry-run qualification.

## 10.1 Accessibility rubric

Propositions:
- A1 Execution Access;
- A2 Custody / Holding Path;
- A3 Settlement / Transferability;
- A4 Access Resilience.

E2 boundary:
> at least one complete current path for RIP-01 through execution, holding and transfer/settlement, without identified present blocker.

Listing alone does not establish E2.

## 10.2 Absorption

`RAS-01 = USD 5m / 24h`

`child order ≈ USD 208,333`

For each valid snapshot:
- simulate buy by walking asks;
- simulate sell by walking bids;
- `PEC_core_snapshot = max(PEC_buy, PEC_sell)`;
- standard depth request = 1000 levels;
- if child notional is not covered, escalate to deepest supported pilot snapshot, target 5000;
- do not interpolate unobserved depth;
- planned = 24 hourly events;
- minimum valid = 18;
- median PEC is threshold statistic;
- P90 PEC is diagnostic.

Participation Ratio:
`PR = RAS-01 / median daily qualified spot turnover over 7 days`

Experimental thresholds:
- E4: median PEC <= 0.50% AND PR <= 2%;
- E3: median PEC <= 1.00% AND PR <= 5%;
- E2: median PEC <= 2.00% AND PR <= 10%.

Single-source asymmetry:
- Binance alone may prove E2 sufficiency;
- Binance-only failure cannot automatically prove E1/E0;
- below-E2 cases trigger depth escalation and, if necessary, source expansion;
- if expansion is infeasible, use `IND / bounded source coverage`.

---

# 11. Data Feed operational state at this checkpoint

Repository:
`rogerio-raposo/crypto-pro-datafeed`

Stable v1.0.0 contract remains untouched by PCP-01 experimental work.

Experimental components implemented:
- Binance technical probe;
- Binance Supported Market Universe builder;
- multi-asset Capacity dry-run;
- official raw Capacity capture pipeline;
- exact 7-day turnover-at-T0 collector.

Official activation remains disabled.

Current dry-run status file:
`data/experimental/pcp-01/dry-run/capacity-status.json`

Repeated technical PASS cycles were observed, including:
- `2026-10-01T05:00:00Z`;
- `2026-10-01T13:00:00Z`;
- `2026-10-01T18:00:00Z`;
- `2026-10-01T23:00:00Z`;
- `2026-10-02T02:00:00Z`;
- `2026-10-02T08:00:00Z`;
- `2026-10-02T15:00:00Z`.

All persisted cycles listed above were technically successful for 9/9 markets, but no pair was in adjacent UTC hour slots.

Therefore:
`two_cycle_status = PENDING`.

## 11.1 Orchestration defect identified

The previous GitHub Actions workflow used `cron: "17 * * * *"` and depended on GitHub scheduler start times to produce adjacent UTC-hour observations.

Observed schedule delays were irregular and large enough that successful runs landed in non-adjacent hour slots. This is an orchestration defect, not a market-data acquisition defect.

The pre-registered methodological condition is unchanged:
> two technically successful cycles in adjacent UTC hour slots.

Prior non-adjacent PASS observations are not retroactively accepted as satisfying the gate.

## 11.2 Controlled-pair correction

Data Feed commit:
`70b9a58bbef3a3be6c4dcf1b7857b4fcfa9ad6e8`

The dry-run workflow now:
1. runs controlled cycle A;
2. waits 3600 seconds inside the same workflow;
3. runs controlled cycle B;
4. verifies `two_cycle_status = PASS`;
5. verifies that the qualified cycle IDs are exactly the A/B pair from the same run;
6. persists the lightweight status only after qualification.

The unreliable recurring cron was removed from this qualification workflow.

Controlled qualification run:
`37059995273`

Status at CP14 creation:
`IN PROGRESS`.

This correction changes execution orchestration only. It does not alter the PCP-01 methodology, the dry-run gate, QEV mapping, RAS, PEC/PR thresholds, or any E-state.

RSR diagnostic remains:
- valid market acquisition;
- standard 1000-level book repeatedly showed visible bid notional below the child order;
- this is not a technical failure and not yet an Absorption FAIL;
- official protocol requires depth escalation and possibly source expansion before negative economic conclusion.

---

# 12. UFT / Capture Start / T0

Current status:
- `UFT`: NOT DECLARED;
- `Capture Start`: NOT DECLARED;
- `T0`: NOT DECLARED;
- official T0 Evidence Pack: NOT FROZEN;
- Capacity E-states: NOT CALCULATED;
- Frictions: NOT ASSESSED;
- Ranking Classes: NOT CALCULATED.

Dry-run prerequisite:
> two technically successful cycles in adjacent UTC hour slots.

After prerequisite + readiness:
- UFT = final sample freeze time;
- Capture Start = next full UTC hour;
- T0 = Capture Start + 24h;
- H = T0 + 90d.

Dry-run data:
- does not integrate PEC;
- does not integrate PR;
- does not generate E-state;
- does not enter official Evidence Pack.

---

# 13. Open gaps and controls

## Open / active
- **MGR-002** — independent Evaluator B still pending;
- **MGR-003** — T0 not declared;
- **MGR-004** — gas-token materiality calibration remains pilot diagnostic;
- **MGR-005** — Structural Position bounded by SMU coverage;
- **MGR-006** — prospective institutional validation / future-capture gap; shadow diagnostic retained, no method change;
- **MGR-009** — Structural Position comparator heterogeneity.

## Resolved with continuing controls
- **MGR-001** — Position Reference Universe rule resolved;
- **MGR-007** — PRE-T0 evidence-completeness defect resolved; repeat control at T0 mandatory;
- **MGR-008** — ONDO AUM/franchise thesis does not establish current Economic Capture; no methodology defect.

---

# 14. Backlog

`BL-RANK-001 — Critical Event Watch / Interim Methodological Update`
- conceptually accepted direction;
- not yet specified or integrated into v1;
- Weekly Run remains the official execution cadence.

`BL-RANK-002 — Supported Market Universe / Data Feed source governance`
- future commercial source governance;
- coverage, reliability, licensing, storage/redistribution rights;
- potential DEX/institutional venue expansion;
- Capacity may require multi-venue sensitivity/coverage.

MEL:
- internal Ranking component/backlog;
- formal inclusion decision deferred.

---

# 15. Freshness Gate CP13 → CP14

Suite `main` and Data Feed operational state were checked before this checkpoint.

No new Ranking methodological decision was identified that supersedes CP13.

Material operational change:
- additional scheduled dry-runs continued to return PASS 9/9;
- no adjacent UTC-hour pair was produced because GitHub scheduler starts were irregular;
- the defect was isolated to orchestration;
- Data Feed workflow was corrected to run a controlled A/B pair one hour apart inside the same workflow;
- controlled run `37059995273` is in progress.

Conclusion:
> Ranking methodology remains unchanged. Etapa 60 remains open pending completion and verification of the controlled pair.

---

# 16. Migration of continuity architecture

Previous state:
- CP01–CP12 used a cumulatively growing handoff pattern.

Observed maintenance defect:
- CP12 header correctly identifies CP12/CP11;
- its internal usage section still points to CP06;
- its checkpoint date header remained 30/09/2026 despite CP12 filename/date being 01/10/2026.

Treatment:
- do **not** rewrite CP12;
- preserve it as historical evidence;
- migrate from CP13 onward to autonomous immutable snapshots;
- use `archive/handoffs/ranking/README.md` as the only operational pointer;
- keep the operational restart prompt only in README.

This is an operational continuity improvement, not a methodological change.

---

# 17. Ponto exato de retomada

**Etapa 60 — Capacity Operational Readiness permanece EM ANDAMENTO.**

Current controlled qualification:
- Data Feed run `37059995273`;
- cycle A / wait 3600s / cycle B;
- status at checkpoint: **IN PROGRESS**.

Blocking condition:
> controlled pair completes successfully and `two_cycle_status = PASS` with the A/B cycle IDs from the same run.

When PASS is observed, do not advance automatically.

Next controlled actions:
1. verify the Data Feed workflow result and persisted status;
2. confirm that cycles A and B are technically successful and belong to adjacent UTC hour slots;
3. verify that the status file identifies exactly those cycles as the qualifying pair;
4. declare/freeze QEV status for mapped markets;
5. perform the readiness/Freshness check required before UFT;
6. present the transition for the applicable human gate;
7. only then declare `UFT → Capture Start → T0` and activate official raw capture.

Until then:
- do not calculate PEC/PR from dry-run data;
- do not assign Capacity E-states;
- do not assess Frictions as if Capacity were complete;
- do not calculate Ranking Classes.
