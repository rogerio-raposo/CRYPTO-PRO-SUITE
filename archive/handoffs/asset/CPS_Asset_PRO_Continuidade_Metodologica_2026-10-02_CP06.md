# CRYPTO PRO SUITE
## Asset PRO — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP06  
**Checkpoint anterior:** CP05  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Asset PRO — Metodologia Geral  
**Finalidade:** preservar o encerramento do desenho pré-implementação de P0/P1 e permitir retomada controlada sem depender da memória do modelo.  
**Ponteiro operacional de continuidade:** `archive/handoffs/asset/README.md`  
**Natureza deste CP:** snapshot autônomo do estado corrente na transição entre desenho metodológico e materialização experimental.

---

# 1. Regras de continuidade

- Repositório e documentos persistidos são a fonte de verdade.
- Memória do modelo pode orientar recuperação, mas não constitui evidência.
- Este handoff é operacional e **não normativo**.
- Freshness Gate e Diagnóstico de Continuidade permanecem obrigatórios.
- Não sobrescrever este checkpoint; correções materiais futuras geram novo CP.
- Não promover artefatos experimentais a metodologia normativa sem Decision Record + gate humano.
- Não iniciar P1 sem P0 formalmente aprovado.

---

# 2. Marco registrado no CP06

Desde o CP05 foram fechadas:

- **Etapa 36 — Pacote de especificações de implementação do P0**;
- **Etapa 37 — Especificação executável do P1 / D1 Experiment**;
- **Etapa 38 — Arquitetura dos artefatos experimentais e governança P0/P1**.

Marco de fase:

> **o desenho pré-implementação do Asset PRO P0/P1 está fechado; o próximo trabalho deve materializar artefatos persistentes e só depois iniciar implementação/execução.**

---

# 3. P0 — arquitetura técnica fechada

Objetivo:
> provar que o ambiente histórico usado na validação é causal, determinístico, auditável e reproduzível.

Arquitetura:
> historical source → dataset preparation/validation → immutable dataset version → causal replay → snapshots/event log → determinism/restart tests → P0 PASS/FAIL.

## Dataset Manifest mínimo
- dataset_id;
- data_version;
- asset;
- venue;
- market_type;
- instrument;
- base_asset;
- quote_asset;
- source_provider;
- source_endpoint_or_contract;
- native_timeframe;
- start_timestamp;
- end_timestamp;
- timezone_policy;
- candle_boundary_policy_id;
- missing_data_policy_id;
- raw_record_count;
- validated_record_count;
- ingestion_timestamp;
- checksum;
- schema_version;
- notes.

## Candle schema
- identity/venue/market/timeframe;
- open_time / close_time;
- OHLCV;
- optional quote_volume/trade_count/source_record_id;
- data_quality_flags;
- dataset_version.

Princípios:
- persistência decimal apropriada;
- OHLC invariants obrigatórios;
- dados suspeitos recebem flags, não correção silenciosa;
- sem interpolação silenciosa;
- outlier ≠ erro automaticamente;
- candle fechado é unidade padrão;
- higher-timeframe incompleto não pode ser usado como fechado;
- native e derived candles devem ser distinguíveis.

## Data Quality Flags iniciais
- INVALID_OHLC;
- DUPLICATE_CANDLE;
- MISSING_INTERVAL;
- ZERO_VOLUME;
- EXTREME_PRICE_MOVE;
- EXTREME_VOLUME;
- TIMESTAMP_IRREGULARITY;
- SOURCE_DISCONTINUITY;
- INSTRUMENT_CHANGE;
- SUSPENSION;
- CROSS_VENUE_ANOMALY.

## Replay
- clock lógico único;
- somente dados com close_time ≤ replay_timestamp;
- snapshots por etapa temporal;
- Event Log append-only;
- checkpoint/restart obrigatório;
- canonical serialization para hashes;
- replay contínuo e replay retomado devem produzir output idêntico.

Identidade experimental:
> Data Version + Method Version + Parameter Profile + Code Version.

P0 Decision Gate:
- resultado formal binário: PASS ou FAIL;
- critical controls bloqueiam P1;
- warnings não criam terceiro estado formal.

Fixtures:
- Synthetic Golden Fixture;
- Real Golden Fixture;
- regression suite permanente.

---

# 4. P1 — protocolo executável fechado

Pré-condição:
> P0 = PASS.

Pergunta:
> qual arquitetura de swing detection fornece base causal, estável, reproduzível e suficientemente responsiva para D1?

Métodos concorrentes:
- M1 — Fixed-Window Pivot;
- M2 — Fixed-Percentage Reversal;
- M3 — Volatility-Normalized Reversal.

Sem M4 híbrido inicialmente.

Pipeline comum:
> Swing Detector → Confirmed Structural Swings → HH/EH/LH/HL/EL/LL → Regime → Protected Swing → Structural Events.

Universo inicial:
- quatro ativos líquidos e heterogêneos;
- BTC e ETH obrigatórios;
- A3/A4 selecionados por critérios ex ante;
- microcaps excluídas da primeira rodada.

Timeframes:
- 4h;
- Daily.

Historical segments devem cobrir:
- bull trend;
- bear trend;
- range;
- transition;
- volatility shock.

Separação:
- P1-DEV;
- P1-VAL;
- Structural Holdout recomendado antes da seleção final provisória.

Parameter Grid:
- pequeno;
- interpretável;
- Low / Medium / High Sensitivity;
- buscar plateau, não ponto ótimo.

M3:
- screening de volatility estimator;
- depois sensitivity de window e multiplier k;
- evitar explosão combinatória.

Swing matching:
- same type;
- timestamp window;
- normalized price distance;
- one-to-one;
- regra congelada antes da comparação final.

Métricas principais:
- Swing Density;
- Confirmation Delay;
- Normalized Confirmation Delay;
- Swing Stability;
- Swing Fragmentation;
- Swing Omission;
- Regime Churn;
- Short-Lived Regime Rate;
- Transition Utilization;
- Direct Trend Flip Rate;
- Protected Swing Turnover;
- Protected Swing Sensitivity;
- Event Stability;
- Event Delay;
- Indeterminate Rate;
- Parameter Plateau Width;
- Cross-Asset Stability;
- Cross-Timeframe Stability;
- Data-Anomaly Sensitivity;
- Causal Integrity.

Sem composite score.

Blockers:
- look-ahead;
- nondeterminism;
- extreme parameter fragility;
- structural inconsistency;
- pathological regime behavior;
- failure across multiple assets/timeframes.

P1 Decision Gate:
- P1-PASS — Single Candidate;
- P1-PASS — Multiple Candidates;
- P1-REVISE;
- P1-FAIL.

Predictive outcome/P&L não participa da seleção.

---

# 5. Governança cross-repository fechada

## CRYPTO-PRO-SUITE owns
- metodologia do Asset;
- P0/P1 Experiment Manifests;
- replay metodológico;
- D1 methods;
- P1 metrics;
- human review;
- Decision Records.

## crypto-pro-datafeed owns
- aquisição histórica;
- source/provenance;
- producer-side validation;
- normalização/resampling;
- dataset technical manifest;
- fixtures e geração do dataset experimental.

Princípio:
> um artefato canônico + referências imutáveis; evitar duplicação cross-repository.

Dependências formais devem registrar:
- Suite commit SHA;
- Data Feed commit SHA;
- Dataset Version;
- Experiment Manifest hash.

---

# 6. Estrutura experimental candidata

## Suite
`03-componentes/24-asset/experimental/`
- `P0/`;
- `P1/`.

P0 deve conter, em nível documental:
- README;
- P0_EXPERIMENT_MANIFEST;
- P0_REPLAY_SPECIFICATION;
- P0_VALIDATION_CONTROLS;
- P0_FIXTURE_EXPECTATIONS;
- P0_DECISION_RECORD.

P1 deve conter, posteriormente:
- README;
- P1_EXPERIMENT_MANIFEST;
- P1_METHOD_SPECIFICATIONS;
- P1_PARAMETER_PROFILE_REGISTRY;
- P1_MATCHING_SPECIFICATION;
- P1_METRICS_SPECIFICATION;
- P1_HUMAN_REVIEW_PROTOCOL;
- P1_DECISION_RECORD.

## Data Feed
Aproveitar estrutura experimental já existente:
- `docs/experimental/`;
- `src/experimental/`;
- `data/experimental/`.

Para Asset P0:
- `docs/experimental/asset-p0/`;
- `src/experimental/asset_p0/`;
- `data/experimental/asset-p0/`.

Grandes datasets e grandes outputs não devem ser commitados indiscriminadamente.
Git deve preservar:
- manifests;
- specifications;
- hashes;
- decision-critical summaries;
- reproduction metadata;
- pequenas fixtures.

---

# 7. Regras de promoção e preservação

- `experimental/` é WORKING / NON-NORMATIVE.
- Experiment Manifest congela desenho experimental.
- Decision Record registra resultado.
- Checkpoint preserva continuidade da conversa/metodologia.
- Nenhum desses artefatos substitui os demais.
- Experimentos rejeitados permanecem preservados.
- Bug material durante execução gera nova Code Version e execução formalmente separada.
- mudança material após Experiment Freeze exige novo Experiment ID.

---

# 8. Estado de maturidade no CP06

- Asset PRO Core conceitual: fechado em nível de trabalho;
- D1–D5: arquiteturas conceituais definidas;
- CSM: contrato conceitual definido;
- Setup Hypothesis e F1–F4: fechados conceitualmente;
- validation architecture P0–P11: definida;
- P0: especificação técnica pronta para materialização;
- P1: protocolo executável pronto para materialização;
- governança Suite × Data Feed: definida;
- estrutura experimental: candidata e pronta para criação;
- código experimental: ainda não iniciado;
- datasets históricos P0: ainda não construídos;
- P0: ainda não executado;
- P1: bloqueado até P0 PASS;
- metodologia normativa final: inexistente.

---

# 9. Ponto exato de retomada

## Etapa 39 — Materialização do pacote P0

Objetivo:
> criar nos repositórios os artefatos experimentais persistentes necessários para P0, ainda sem executar o experimento.

Sequência mínima:
1. criar área `03-componentes/24-asset/experimental/` na Suite;
2. criar pacote documental P0 na Suite;
3. criar/estender área `asset-p0` nas estruturas experimentais do Data Feed;
4. materializar Dataset Contract, Historical Source Spec, Data Validation Spec, Resampling Spec e Provenance Spec;
5. materializar P0 Experiment Manifest, Replay Specification, Validation Controls, Fixture Expectations e Decision Record template;
6. registrar explicitamente status WORKING / NON-NORMATIVE;
7. usar referências cross-repository, não duplicação;
8. ainda **não executar P0**;
9. revisar consistência documental e somente depois iniciar implementação/código.

Regra:
> P1 permanece bloqueado até P0 PASS.

---

**Fim do CP06**
