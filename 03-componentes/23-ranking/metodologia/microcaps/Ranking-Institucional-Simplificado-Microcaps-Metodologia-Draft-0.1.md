# Ranking Institucional Simplificado — Microcaps
## Metodologia — Draft 0.1

**Projeto:** CRYPTO PRO SUITE  
**Componente:** 23 — Ranking Institucional Simplificado  
**Submetodologia:** Microcaps  
**Status:** Draft 0.1  
**Data:** 22 de setembro de 2026

> Este documento é normativo apenas para o escopo **Microcaps**. Não define, por extensão, a metodologia integral do Ranking Institucional Simplificado.

---

# 1. Objetivo e constructo

A submetodologia Microcaps avalia, de forma relativa e baseada em evidências, a qualidade e a evolução de oportunidades microcap dentro de narrativas previamente definidas.

**Constructo:** o Ranking mede a qualidade relativa e a evolução da evidência de uma oportunidade microcap dentro de uma narrativa.

Não é um motor de previsão de preço, retorno, MFE, market timing ou alpha.

**Princípio metodológico:** Price = outcome, não Fundamental Ground Truth.

# 2. Dependência de narrativa

A seleção e avaliação de Narrative Opportunity ocorrem upstream, fora do cálculo do Potential. O Ranking recebe a narrativa como contexto de entrada e avalia o Asset–Narrative Fit.

# 3. Universo e elegibilidade

O universo Microcaps utiliza como referência market cap inferior a **US$100 milhões** no checkpoint de elegibilidade.

**Princípio de seleção:** elegibilidade permissiva; scoring seletivo.

Ordem preferencial de prova PIT:
1. Direct PIT Snapshot;
2. Circulating Supply Reconstruction;
3. Conservative Upper Bound;
4. Inference somente quando o ativo estiver materialmente distante do cutoff.

Ativos na zona de aproximadamente US$90–110 milhões exigem reconstrução reforçada. Eligibility Confidence é registrada separadamente de Scoring Confidence.

**Futuros/perpétuos não são filtro de elegibilidade.**

A identidade canônica do ativo deve ser resolvida antes de reconstruções históricas. Ticker collision, contract migration, redenomination, merger, chain migration, token replacement e discontinuation devem ser registrados.

# 4. Potential Score

Cada dimensão recebe nota de 0 a 5.

| Dimensão | Peso |
|---|---:|
| Asset–Narrative Fit | 25% |
| Project Quality / Differentiation | 25% |
| Emerging Attention | 15% |
| Early Traction | 20% |
| Asymmetry / Relative Valuation | 15% |

**Potential = 20 × (0,25 Fit + 0,25 Quality + 0,15 Attention + 0,20 Traction + 0,15 Asymmetry)**

## 4.1 Fit Gate

Asset–Narrative Fit deve ser **≥3/5**.

## 4.2 Regras de interpretação

- Fundamental State pertence primariamente a Quality.
- Mudança ou crescimento verificável do estado pode alimentar Traction.
- Attention não equivale a Traction.
- Catalyst não equivale automaticamente a Attention.
- Baixo market cap não implica automaticamente alta Asymmetry.
- Diluição e estrutura de oferta devem ser consideradas em Asymmetry.
- Um mesmo datum deve possuir um primary scoring home, evitando double counting.
- Unknown é **NA**, nunca nota neutra arbitrária.

# 5. Evidence Roles

As evidências são classificadas em:
- Fundamental State;
- Fundamental Growth;
- Catalyst;
- Attention;
- Traction;
- Token Economics;
- Market Data;
- Risk;
- Eligibility.

A frequência de publicação de um projeto não pode elevar mecanicamente o Potential.

# 6. Governança temporal e Data Source Registry

Cada datum relevante deve registrar, quando aplicável:
- value;
- as_of;
- published_at;
- effective_at;
- observed_at;
- known_at_score_time;
- source;
- source_role;
- authority;
- temporal_fidelity;
- granularity;
- coverage_start;
- derivation;
- conflict_flag;
- confidence;
- contract/token identity;
- lifecycle events.

Uma evidência só pode afetar o checkpoint se estiver dentro do conjunto informacional publicamente disponível naquele momento. `effective_at <= checkpoint` não é suficiente: `known_at_score_time` deve ser verdadeiro.

# 7. Confidence

A arquitetura separa:
1. Datum Confidence;
2. Dimension Confidence;
3. Scoring Confidence;
4. Eligibility Confidence.

Missing data reduz Confidence; não deve ser convertido em nota artificial.

# 8. Risk, Operability e Lifecycle

**Risk**, **Operability** e **Lifecycle State** são dimensões paralelas ao Potential e não devem reordená-lo automaticamente.

Risk Trend: Improving / Stable / Increasing.  
Confidence Trend: Improving / Stable / Declining.

Lifecycle events devem ser tratados explicitamente. Não há transferência automática de score entre predecessor e successor asset. Coverage gap não equivale a ausência econômica real.

# 9. Potential Trend — state machine

Estados:
- Stable;
- Emerging;
- Accelerating;
- Cooling;
- Fading;
- Deteriorating;
- Stabilizing.

Definições operacionais:
- **Stable:** tese aproximadamente constante; ausência de nova evidência normalmente implica carry-forward.
- **Emerging:** nova evidência admissível melhora materialmente a tese.
- **Accelerating:** evidências sucessivas demonstram fortalecimento crescente.
- **Cooling:** evidência de desaceleração de crescimento anteriormente observado.
- **Fading:** perda material de força da tese anterior.
- **Deteriorating:** nova evidência contradiz ou destrói componente material da tese.
- **Stabilizing:** após deterioração, surgem evidências de adaptação ou contenção sem restabelecer ainda uma trajetória Emerging/Accelerating.

Ausência de notícias não constitui evidência negativa por si só.

# 10. Detection Framework

## 10.1 Emerging Candidate

Primeiro checkpoint que satisfaz Emerging com nova evidência admissível.

## 10.2 Confirmed Detection

Exige **nova evidência admissível posterior ao Candidate** que sustente Emerging ou produza Accelerating. Carry-forward, preço ou mera listagem não confirmam Candidate.

## 10.3 Candidate Expiration

O Candidate permanece ativo por **três checkpoints mensais subsequentes (~90 dias)**. Sem confirmação, torna-se **Expired Unconfirmed**. Nova evidência posterior pode iniciar novo Candidate com nova data.

## 10.4 Detection Date

Uma vez confirmado, o Detection Date permanece a data do primeiro Candidate. Candidate não confirmado não recebe Detection Date definitiva.

# 11. Fundamental Event Ledger

O ledger é infraestrutura de auditoria independente do score. Campos mínimos:
- asset_id;
- event_date;
- published_at;
- known_at;
- event_type;
- evidence_role;
- materiality;
- direction;
- source_quality;
- fundamental_change;
- lifecycle_event.

O ledger distingue mudança fundamental de movimento de preço e serve de base para avaliações futuras de Detected e Missed Fundamental Changes.

# 12. Outputs mínimos

Uma execução Microcaps deve produzir, por ativo elegível:
- Potential Score;
- cinco notas dimensionais;
- Potential Trend;
- Confidence e Confidence Trend;
- Risk Profile e Risk Trend;
- Operability;
- Lifecycle State/flags;
- Candidate/Confirmation/Expiration status, quando aplicável;
- evidências e fontes auditáveis;
- Eligibility Confidence;
- Scoring Confidence.

O Radar de Ativos Promissores pode destacar ativos Emerging/Accelerating sem necessariamente reproduzir o topo do ranking.

Uma execução deve preservar identificação da metodologia aplicada (`methodology_version`) e o checkpoint temporal correspondente.

# 13. Validation Layer

Preço, retorno, MFE, MAE, EOY Return e Time-to-MFE pertencem exclusivamente à camada de validação. Não entram no Potential.

**Price ≠ Fundamental Ground Truth.**

# 14. Limitações e non-claims

A metodologia não reivindica:
- previsão consistente de retorno;
- ordenação futura de MFE;
- alpha estatisticamente demonstrado;
- antecipação sistemática da reprecificação de mercado;
- valorização futura como consequência de Potential elevado.

# 15. Fronteiras arquiteturais

- Narrative Opportunity permanece upstream, na camada de rotação.
- Diversificação e regra de um ativo por narrativa não pertencem ao Ranking; são responsabilidade futura do CSE/Portfolio Construction.
- Futures/perpetuals não integram elegibilidade.
- O Ranking Microcaps permanece independente dos demais módulos.

# 16. Itens fora do núcleo deste Draft

**Pesquisa/experimental:** Market Recognition Date, Recognition Lead, MFE Lead, Persistence Quality, Detection Rate com ground truth fundamental independente.

**Backlog:** MEL — Methodology Evaluation Layer. O MEL deve detectar, diagnosticar e propor; nunca alterar automaticamente pesos ou regras. Sua inclusão na primeira versão do CRYPTO PRO SUITE será decidida após o fechamento dos demais módulos.

# 17. Governança de mudança

Os pesos 25/25/15/20/15 e demais regras consolidadas não devem ser recalibrados retrospectivamente a partir dos outcomes dos pilotos. Mudanças futuras exigem justificativa, registro de decisão e nova versão metodológica. Execuções históricas preservam a methodology_version aplicável.

# 18. Proveniência

A base empírica e as decisões que sustentam este Draft estão registradas em `../../validacao/microcaps/`, especialmente no documento **Ranking Institucional Simplificado — Microcaps — Validação Metodológica — Draft 0.1**.
