# Ranking Institucional Simplificado — Microcaps
## Validação Metodológica e Encerramento dos Pilotos

**Projeto:** CRYPTO PRO SUITE  
**Status:** Draft 0.1  
**Data:** 22 de setembro de 2026

> **Finalidade:** consolidar os resultados dos três pilotos de validação, registrar as decisões metodológicas decorrentes e estabelecer o estado de maturidade do Ranking antes da formalização de sua metodologia-base.

---

# 1. Status do documento

Este documento registra o encerramento da fase experimental pré-v1.0 do **Ranking Institucional Simplificado — Microcaps**. Ele não atribui ainda uma versão formal ao módulo. A versão formal inicial será definida no processo de fechamento do CRYPTO PRO SUITE.

Os três pilotos são tratados como validação operacional e metodológica. Os resultados não constituem demonstração estatística de alpha, previsão de retorno ou capacidade sistemática de market timing.

# 2. Objetivo do Ranking

O Ranking Institucional Simplificado — Microcaps é um mecanismo de avaliação relativa, baseado em evidências, destinado a identificar a qualidade e a evolução de oportunidades microcap dentro de narrativas previamente definidas.

**Princípio central: preço é outcome, não ground truth fundamental.**

# 3. Arquitetura metodológica consolidada

## 3.1 Potential Score

O Potential Score permanece composto por cinco dimensões, cada uma avaliada em escala de 0 a 5, com os pesos congelados durante os pilotos:

| Dimensão | Peso |
|---|---:|
| Asset–Narrative Fit | 25% |
| Project Quality / Differentiation | 25% |
| Emerging Attention | 15% |
| Early Traction | 20% |
| Asymmetry / Relative Valuation | 15% |

**Potential = 20 × (0,25 Fit + 0,25 Quality + 0,15 Attention + 0,20 Traction + 0,15 Asymmetry)**

O Fit Gate permanece **≥ 3/5**. Os pilotos não forneceram evidência suficiente para recalibrar os pesos. Qualquer alteração com base nos outcomes observados constituiria ajuste post hoc.

## 3.2 Dimensões paralelas

- **Confidence** — confiabilidade da evidência e do scoring.
- **Risk** — riscos materiais que não devem ser confundidos automaticamente com perda de Potential.
- **Operability** — condições de acesso e negociação, sem funcionar como filtro fundamental.
- **Lifecycle State** — eventos de migração, merger, redenominação, substituição de token ou descontinuidade.

## 3.3 Potential Trend

Os estados consolidados são **Stable, Emerging, Accelerating, Cooling, Fading e Deteriorating**. O terceiro piloto também demonstrou a utilidade descritiva de **Stabilizing** após deterioração.

- **Stable:** tese aproximadamente constante; ausência de nova evidência não implica Cooling.
- **Emerging:** nova evidência começa a melhorar materialmente a tese.
- **Accelerating:** sucessivas evidências demonstram fortalecimento crescente.
- **Cooling:** existe evidência de desaceleração de algo anteriormente crescente.
- **Fading:** a evidência positiva anterior perde força material.
- **Deteriorating:** nova evidência contradiz ou enfraquece materialmente a tese.

# 4. Governança de evidências e dados

## 4.1 Regra temporal

A admissibilidade de uma evidência exige não apenas `effective_at` anterior ou igual ao checkpoint, mas também que a informação estivesse publicamente disponível no momento do scoring (`known_at_score_time = TRUE`).

## 4.2 Evidence Roles

Os papéis de evidência permanecem separados: **Fundamental State, Fundamental Growth, Catalyst, Attention, Traction, Token Economics, Market Data, Risk e Eligibility**. Cada dado possui um *primary scoring home*, reduzindo double counting.

## 4.3 Confidence

- **Datum Confidence** — confiabilidade do dado individual.
- **Dimension Confidence** — qualidade da evidência de uma dimensão.
- **Scoring Confidence** — confiabilidade global do Potential.
- **Eligibility Confidence** — separada de Scoring Confidence.

Regra preservada: **unknown = NA**; ausência de informação não recebe arbitrariamente nota neutra 3.

## 4.4 Asset Identity & Lifecycle

A identidade canônica deve preceder a reconstrução de preço e market cap. O Registry deve registrar canonical asset, contratos atual e legado, eventos de migração, successor asset, continuity flags e confiança da reconstrução. Lifecycle events não alteram automaticamente o Potential.

# 5. Detection Framework

## 5.1 Candidate e Confirmation

**Emerging Candidate** é o primeiro checkpoint em que nova evidência admissível produz estado Emerging. **Confirmed Detection** exige nova evidência admissível posterior ao Candidate que sustente Emerging ou produza Accelerating. Carry-forward não confirma Candidate.

## 5.2 Candidate Expiration

O terceiro piloto testou prospectivamente a validade de **três checkpoints subsequentes**. Sem confirmação nesse intervalo, o Candidate passa a **Expired Unconfirmed**. Evidência material posterior inicia um novo Candidate.

## 5.3 Detection Date

Quando confirmado, o Detection Date permanece a data do Candidate original. Candidate não confirmado não recebe Detection Date definitiva.

# 6. Fundamental Event Ledger

O terceiro piloto confirmou a utilidade operacional de um ledger independente do motor de scoring para registrar mudanças fundamentais materiais.

Campos mínimos:

- `asset_id`, `event_date`, `published_at`, `known_at`;
- `event_type`, `evidence_role`, `materiality`, `direction`;
- `source_quality`, `fundamental_change`, `lifecycle_event`.

O Fundamental Event Ledger não utiliza preço para definir materialidade fundamental e serve como base futura para avaliar **Detected Fundamental Changes** e **Missed Fundamental Changes**.

# 7. Síntese dos três pilotos

## 7.1 Primeiro piloto — desenvolvimento metodológico

O primeiro piloto revelou problemas de elegibilidade histórica, identidade de ativos, reconstrução de market cap e separação entre Attention, Traction, Risk e Confidence. O caso GFI demonstrou a necessidade de Eligibility Confidence e de auditoria PIT.

## 7.2 Segundo piloto — 31/12/2023 a 31/12/2024

Narrativas **AI e RWA**. O Snapshot não demonstrou relação monotônica robusta entre Potential e magnitude dos outcomes. O Rolling produziu Confirmed Detection para CGPT, NOS e OM; TRADE e RIO permaneceram Unconfirmed. CPOOL exemplificou Persistence.

O caso FAKEAI demonstrou que grande valorização pode ocorrer sem melhora equivalente da evidência fundamental. OM mostrou a capacidade do Rolling de reconhecer fortalecimento progressivo de uma tese, mas análises de sensibilidade indicaram que resultados quantitativos favoráveis eram fortemente dependentes desse caso extremo.

## 7.3 Terceiro e último piloto — 31/12/2021 a 31/12/2022

Narrativas **GameFi/P2E e DeFi 2.0**, em regime adverso. O Strict Universe final foi composto por GODS, SIPHER, SIDUS, SPA, HEC e KLIMA. O objetivo foi testar especialmente estados negativos do state machine e separar deterioração fundamental de queda generalizada de preço.

| Ativo | T0 | Final | Estado final |
|---|---:|---:|---|
| GODS | 87,0 | 89,0 | Persistent |
| HEC | 76,0 | 80,0 | Confirmed / Persistent |
| KLIMA | 82,0 | 77,0 | Stabilizing após deterioração |
| SIDUS | 70,0 | 76,0 | Confirmed / Stable |
| SIPHER | 75,5 | 72,5 | Cooling |
| SPA | 72,5 | 58,5 | Deteriorating |

O piloto demonstrou operacionalmente que o Ranking pode manter uma tese fundamental mesmo sob forte queda do token, bem como reduzir Potential quando há evidência adversa específica. GODS funcionou como controle importante: queda severa do token coexistiu com crescimento operacional do jogo, impedindo que preço fosse usado como proxy de deterioração.

# 8. Resultado da validação

## 8.1 Componentes considerados maduros para a metodologia-base

- Potential Score em cinco dimensões e pesos 25/25/15/20/15.
- Fit Gate ≥ 3/5.
- Evidence Roles e primary scoring home.
- Data Source Registry e `known_at_score_time`.
- Potential Trend e carry-forward.
- Candidate → Confirmation.
- Candidate Expiration em três checkpoints.
- Separação entre Potential, Confidence, Risk e Operability.
- Lifecycle handling e Canonical Asset Identity.
- Eligibility Confidence separada de Scoring Confidence.
- Datum → Dimension → Scoring Confidence.
- Fundamental Event Ledger.
- Preço e outcomes fora do scoring.

## 8.2 O que os pilotos não demonstraram

- capacidade consistente de prever retorno;
- capacidade de ordenar MFE;
- alpha estatisticamente demonstrado;
- capacidade sistemática de antecipar o início da reprecificação pelo mercado;
- que Potential elevado implica valorização futura.

## 8.3 Definição operacional resultante

**O Ranking mede a qualidade relativa e a evolução da evidência de uma oportunidade microcap dentro de uma narrativa previamente definida.**

# 9. Stop rule e encerramento dos pilotos

O terceiro piloto foi definido antecipadamente como o último gate obrigatório pré-v1.0. Os critérios de encerramento foram atendidos: execução sem alteração estrutural, ausência de contradição lógica grave, funcionamento determinístico de Candidate/Confirmation/Expiration, tratamento separado de Confidence/Risk/Lifecycle, utilidade do Fundamental Event Ledger e auditabilidade por informação disponível nos checkpoints.

**Decisão: não realizar um quarto piloto como condição para a v1.0.**

# 10. Metodologia viva e MEL

Após a formalização da metodologia-base, sua evolução deverá ocorrer de forma versionada, sem reescrever execuções históricas. O conceito de **MEL — Methodology Evaluation Layer** permanece registrado no backlog como componente interno do Ranking, não como módulo independente.

O MEL poderá avaliar periodicamente integridade metodológica, qualidade do scoring, Detection Quality, calibration drift e dependência de regime, produzindo recomendações para versões futuras. Ele não deverá alterar pesos ou regras automaticamente.

**Status do MEL: BACKLOG — decisão de inclusão na primeira versão do CRYPTO PRO SUITE somente após o fechamento dos demais módulos previstos para essa versão.**

# 11. Itens mantidos em pesquisa

- **Market Recognition Date e Recognition Lead** — métricas experimentais, fora do núcleo da v1.0.
- **MFE Lead** — útil para análise, sem função no scoring.
- **Persistence Quality** — hipótese de pesquisa; não criar novo score neste estágio.
- **Detection Rate** — depende de ground truth fundamental independente e volume maior de observações.

# 12. Próxima etapa documental

O próximo estágio é converter os elementos consolidados neste documento em uma especificação metodológica normativa do Ranking Institucional Simplificado — Microcaps, alinhada ao Manual Metodológico e aos documentos de governança do CRYPTO PRO SUITE. Questões experimentais devem permanecer separadas da metodologia normativa.

# Apêndice A — Princípios congelados

- Eligibility permissiva; scoring seletivo.
- Price = outcome, não ground truth.
- No new evidence normalmente implica carry-forward/Stable, não deterioração.
- Mais publicações não podem aumentar mecanicamente o Potential.
- Catalyst não é automaticamente Attention; Attention não é Traction.
- State pertence primariamente a Quality; mudança do state pode pertencer a Traction quando houver evidência operacional.
- Low market cap não implica high Asymmetry.
- Coverage gap não equivale a ausência econômica real.
- Lifecycle event não altera automaticamente Potential.
- Futures/perpetuals não são filtro de elegibilidade.
- Diversificação por narrativa pertence ao CSE/Portfolio Construction, não ao Ranking.
- Narrative Opportunity permanece upstream, fora do cálculo do Potential.

# Apêndice B — Registro de decisão

| Tema | Decisão | Status |
|---|---|---|
| Pesos | Manter 25/25/15/20/15 | Congelado |
| Candidate Expiration | 3 checkpoints subsequentes | Adotar na metodologia-base |
| Market Recognition | Não promover ao núcleo | Pesquisa |
| Fundamental Event Ledger | Incorporar como infraestrutura de auditoria | Adotar |
| MEL | Componente interno do Ranking | Backlog; decisão pós-fechamento dos demais módulos |
| Quarto piloto | Não realizar como gate pré-v1.0 | Encerrado |
