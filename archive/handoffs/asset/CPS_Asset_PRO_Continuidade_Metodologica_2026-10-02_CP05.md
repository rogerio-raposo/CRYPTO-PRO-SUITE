# CRYPTO PRO SUITE
## Asset PRO — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP05  
**Checkpoint anterior:** CP04  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Asset PRO — Metodologia Geral  
**Finalidade:** preservar o estado metodológico corrente e permitir retomada controlada sem depender da memória do modelo.  
**Ponteiro operacional de continuidade:** `archive/handoffs/asset/README.md`  
**Natureza deste CP:** snapshot autônomo do estado metodológico corrente, com foco nas decisões consolidadas após o CP04 e no ponto de transição da fase conceitual para implementação/validação.

---

# 1. Regra de continuidade

- Repositório e documentos persistidos são a fonte de verdade.
- Memória do modelo pode orientar recuperação, mas não constitui evidência.
- Este handoff é operacional e **não normativo**.
- O Freshness Gate e o Diagnóstico de Continuidade permanecem obrigatórios antes de qualquer retomada.
- Alterações posteriores na branch `main` e documentação de maior autoridade prevalecem quando houver conflito.
- Não reabrir automaticamente decisões conceituais registradas neste checkpoint sem nova evidência, conflito documental ou decisão explícita posterior.
- Não preencher lacunas por inferência e não transformar hipótese de trabalho em regra normativa.
- Não sobrescrever este CP: qualquer correção material futura deverá gerar novo checkpoint.

---

# 2. Mudança de fase registrada no CP05

Desde o CP04, a conversa avançou da **Etapa 15** à **Etapa 35**.

O marco principal é:

> **a arquitetura conceitual do Asset PRO Core está suficientemente fechada para interromper a expansão de constructos e iniciar preparação de implementação e validação empírica.**

A próxima fase não deve introduzir novos indicadores, scores ou pesos por conveniência. Deve transformar os constructos existentes em especificações executáveis, começando por P0/P1.

---

# 3. Confirmação de setup — decisão consolidada

`Developing → Confirmed` ocorre somente quando todos os **Hard Confirmation Gates** aplicáveis à Setup Hypothesis estão simultaneamente:

- `SATISFIED`;
- ainda válidos;
- epistemicamente verificáveis;
- sem invalidação;
- sem lapse;
- sem ambiguidade crítica não resolvida.

Confirmação possui dois componentes:

- **Confirmation Evidence Window** — janela em que as condições se desenvolvem;
- **Confirmation Event** — primeiro instante em que o último Hard Gate necessário se torna satisfeito enquanto os demais permanecem válidos.

Tipos de gate:

- `State Gate`;
- `Event Gate`;
- `Persistence Gate`.

Estados de gate:

- `SATISFIED`;
- `NOT SATISFIED`;
- `INDETERMINATE`.

Princípios:
- Hard Confirmation Evidence é diferente de Soft Evidence.
- Confirmation ≠ Confidence.
- `DEGRADED` não bloqueia automaticamente confirmação; bloqueia quando afeta evidência decisiva.
- “Provisional Confirmation Candidate” é qualificador, não novo lifecycle state.
- F2 exige D3 Acceptance como Hard Gate de família.
- F4 exige Rejection/Re-Acceptance como Hard Gate de família.
- D3 não é Hard Gate universal de F1.
- D5 e CSM não são Hard Gates universais.
- Cross-venue validation é acionada por anomalia/criticidade, não universalmente.
- Temporal ambiguity pode tornar gate `INDETERMINATE`.
- Confirmação tardia deve ser tratada por Timing/Extended, não pelo enfraquecimento arbitrário dos gates.

---

# 4. Timing, Extended, Lapsed e Resolved

Foi formalmente separado:

- validade da tese;
- lifecycle do setup;
- qualidade do timing.

## Timing Quality
Escala conceitual:
- Favorable;
- Acceptable;
- Degraded;
- Indeterminate.

Componentes candidatos:
- distância ao Opportunity Anchor;
- Remaining Technical Room;
- Setup Freshness.

Setup Freshness ≠ Data Freshness.

## Extended
> setup previamente confirmado cuja tese permanece válida, mas cuja localização, Technical Room ou distância em relação à oportunidade original se deteriorou materialmente.

Regras:
- `Confirmed → Extended` é irreversível para o mesmo Setup ID;
- retorno posterior a uma boa localização gera novo Setup ID;
- Extended não significa overbought, bearish ou invalidated.

## Lapsed
> estado terminal pré-confirmação no qual a hipótese perde relevância temporal/estrutural sem falsificação explícita.

Só pode ocorrer a partir de Watch ou Developing.

## Resolved
> estado terminal pós-confirmação no qual a hipótese cumpre suficientemente a função técnica que lhe dava identidade sem ser invalidada.

Resolved não significa trade vencedor ou target financeiro atingido.

---

# 5. Confidence do Asset PRO

Definition:
> avaliação da robustez epistemológica de uma conclusão, e não probabilidade de sucesso, mérito técnico ou retorno esperado.

Confidence é **claim-specific**.

Componentes conceituais:
- C1 — Source Quality;
- C2 — Data Coverage & Sufficiency;
- C3 — Evidence Directness;
- C4 — Evidence Independence;
- C5 — Consistency & Conflict;
- C6 — Classification Stability.

Escala ordinal candidata:
- C0 — Insufficient;
- C1 — Low;
- C2 — Moderate;
- C3 — High;
- C4 — Very High.

Princípios:
- sem fórmula aditiva por enquanto;
- bottlenecks epistemológicos devem ser preservados;
- Setup Confidence depende prioritariamente das evidências decisivas;
- queda de Confidence não invalida setup;
- C0 impede conclusão substantiva;
- threshold mínimo universal de Confidence para `Confirmed` permanece aberto para validação;
- Confidence não multiplica Bias, Timing ou CSM.

---

# 6. Arquitetura formal do output

O output do Asset PRO foi consolidado em seis blocos:

1. **O1 — Analysis Context**
2. **O2 — Technical State**
3. **O3 — Systemic Context**
4. **O4 — Scenario Layer**
5. **O5 — Setup Layer**
6. **O6 — Confidence & Limitations**

Princípios:
- output multidimensional e hierárquico;
- sem score único obrigatório;
- Human-Readable Report e Structured Output devem refletir a mesma metodologia;
- Asset PRO não produz Buy/Sell, sizing, leverage, allocation ou stop financeiro;
- CSE consome o resultado técnico, mas não recalcula D1–D5;
- persistência futura deve combinar snapshot + event log;
- `No Active Setup` e `Indeterminate` são saídas válidas.

---

# 7. Plano de operacionalização das dimensões

Sequência operacional definida:

> **D1 → D2 → D3 → D5 → D4**

Princípio geral:

> **constructo → observable → detection rule → parameters → robustness → validation**

e não:

> indicador → sinal → score.

Indicadores derivados só permanecem se demonstrarem valor incremental.

---

# 8. D1 — operacionalização consolidada

## 8.1 Swing Detection
Arquitetura de referência:
> **Detector Causal de Swing por Reversão Normalizada pela Volatilidade.**

Distinções obrigatórias:
- Local Extremum;
- Candidate Swing;
- Confirmed Structural Swing.

Regras:
- Extremum Timestamp ≠ Confirmation Timestamp;
- Candidate Swing pode atualizar;
- Confirmed Swing não deve repaintar;
- somente swings confirmados podem sustentar mudanças estruturais irreversíveis;
- alternância High ↔ Low;
- EH/EL devem ser permitidos dentro de tolerance futura;
- swings são timeframe-specific;
- ambiguidade intrabar deve ser explicitada;
- Canonical Market/anomaly control se aplica.

Métodos concorrentes do primeiro piloto:
- Fixed-Window Pivot;
- Fixed-Percentage Reversal;
- Volatility-Normalized Reversal.

## 8.2 Structural Sequence e Regime
Regimes:
- Trend;
- Range;
- Transition;
- Indeterminate.

Trend:
- Up / Down.

Integrity:
- Intact;
- Weakening;
- Broken.

Princípios:
- um único HH/LL não cria Trend;
- Range é regime positivo, não ausência de Trend;
- Transition é estado real de reorganização;
- Indeterminate é estado epistemológico;
- mudança de Trend para oposta passa normalmente por Transition;
- regimes permanecem timeframe-specific;
- sem agregação aritmética CTF/PTF/TTF.

## 8.3 Protected Swing
> último Confirmed Structural Swing cuja preservação é necessária para manter a progressão estrutural vigente no timeframe.

- Uptrend → Primary Protected Low;
- Downtrend → Primary Protected High;
- promoção ocorre após nova progressão/Continuation Break confirmada;
- um Primary Protected Swing por timeframe nesta arquitetura inicial;
- swings internos não quebram automaticamente a tendência.

## 8.4 Structural Events
Taxonomia:
- Breach;
- Price-Confirmed Structural Break — PCSB;
- Continuation Break;
- Counter-Structural Break;
- Reclaim;
- Failed Break.

Regras:
- Breach ≠ PCSB;
- PCSB ≠ Acceptance;
- Counter-Structural Break exige Primary Protected Swing;
- Range Boundary PCSB leva Current Regime a Transition;
- Reclaim ≠ Failed Break;
- Rejected Breach ≠ Failed Break;
- event history nunca é apagado por restauração posterior.

## 8.5 Parametrização de D1
Famílias:
- P1 — Volatility Reference;
- P2 — Swing Reversal;
- P3 — Equality Tolerance;
- P4 — Break Confirmation;
- P5 — Structural Restoration;
- P6 — Regime Evidence.

Princípios:
- parameter plateau > ponto ótimo isolado;
- normalização cross-asset > tuning por ativo;
- parameter profiles por horizonte são candidatos;
- sensitivity testing obrigatório;
- Parameter Freeze antes de validação prospectiva.

---

# 9. D2 — operacionalização consolidada

Objetos:
- **Structural Reference Zones — SRZs**;
- **Structural Position**;
- **Technical Room**.

Famílias de referência:
- R1 — Structural Swing Zones;
- R2 — Regime Boundary Zones;
- R3 — Event-Derived Zones;
- R4 — Value/Derived Context Zones.

Princípios:
- D2 organiza a estrutura, não a reinventa;
- SRZ é região, não linha exata;
- Protected Swing gera referência de alta prioridade;
- zone width deve ser volatility-aware;
- Anchor e Bounds são distintos;
- provenance e Zone Construction Method devem ser preservados;
- hierarquia Primary / Secondary / Tactical;
- overlap pode gerar Composite Reference Zone sem apagar origins;
- confluence = diversidade informacional, não contagem;
- Fibonacci permanece auxiliar;
- Volume Profile é candidato forte condicionado a dados;
- Interaction Count e Recency são descritivos, não bônus universais.

Technical Room:
> espaço estrutural entre preço atual/ponto de confirmação e próxima referência material contrária ao cenário.

- direcional;
- horizon-specific;
- scenario-relative;
- Initial e Current Technical Room devem ser preservados;
- não é expected return nem risk/reward.

---

# 10. D3 — Acceptance, Rejection e Participação

## 10.1 Interaction Episode
Unidade temporal de análise vinculada a Reference ID e, quando aplicável, a Event ID.

Estados:
- PENDING;
- ACCEPTED;
- REJECTED;
- RE-ACCEPTED;
- INDETERMINATE.

Acceptance:
> negociação suficientemente persistente e estruturalmente coerente na nova região sem restabelecimento material da região anterior.

Evidências candidatas:
- A1 Persistence;
- A2 Closing Behavior;
- A3 Retest Behavior;
- A4 Value Formation.

Regras:
- um fechamento não equivale automaticamente a Acceptance;
- retest não é requisito universal;
- Reclaim ≠ Re-Acceptance;
- wick ≠ Rejection;
- Acceptance é direcional e horizon-specific;
- sem estado “Partial Acceptance”; usa-se Pending/Indeterminate;
- F2 exige Acceptance;
- F4 depende de Rejection/Re-Acceptance.

## 10.2 Participação
> intensidade relativa da atividade negociada em relação a baseline do próprio mercado.

Princípios:
- relativa, não absoluta;
- não possui direção por si só;
- Event Participation e Episode Participation são distintos;
- volume elevado não é requisito universal de Acceptance;
- Temporal Volume ≠ Volume Profile;
- Spot e derivatives permanecem separados;
- OI ≠ volume;
- CVD/order flow são advanced evidence;
- multi-venue volume não deve ser somado ingenuamente;
- baseline robusta é candidata preferencial a média simples;
- participação não será reduzida a Volume Score.

---

# 11. D5 — Impulso e Persistência

Subcomponentes:
- M1 — Impulse;
- M2 — Persistence;
- M3 — Efficiency;
- M4 — Evolution.

Outputs:
- Direction;
- Strength;
- Persistence;
- Efficiency;
- Evolution.

Princípios:
- Impulse normalizado por volatilidade;
- magnitude ≠ velocidade;
- Impulse ≠ Trend;
- Persistence ≠ contagem simples de candles;
- Directional Efficiency é descritiva;
- Evolution: Accelerating / Stable / Decelerating / Indeterminate;
- Deceleration ≠ reversal;
- structural-leg comparison deve ser priorizada;
- divergência é flag, não trigger autônomo;
- RSI, MACD e médias só entram se demonstrarem valor incremental;
- múltiplas transformações da mesma série não são evidências independentes.

---

# 12. D4 — Core e dados avançados

## 12.1 D4-Core
Classes epistemológicas obrigatórias:
- Observed;
- Derived;
- Proxy;
- Model-Estimated.

Structural Liquidity Proxy ≠ Observed Liquidity.

Núcleo inicial:
- prior structural highs/lows;
- equal highs/lows;
- structural clusters;
- range extremes;
- objective sweeps;
- price displacement.

Termo preferencial:
> **Structural Liquidity Proxy Zone — SLPZ**

Regras:
- SLPZ é proxy, não prova de stops;
- referência deve existir antes do sweep;
- sweep ≠ manipulação;
- sweep não é bullish/bearish por si só;
- displacement ≠ order imbalance observado;
- FVG = geometria derivada candidata, não prova institucional nem fill obrigatório;
- Order Blocks permanecem condicionais.

## 12.2 D4 avançado
Arquitetura modular:
- Core;
- Observed;
- Derivatives;
- Flow.

Evidence Families:
- AF1 — Execution Liquidity;
- AF2 — Derivatives Positioning;
- AF3 — Liquidation Activity;
- AF4 — Aggressor Flow;
- AF5 — Structural Proxy.

Princípios:
- Core é suficiente para versão inicial;
- spread/depth/impact são venue-specific;
- OI não possui direção própria;
- funding não é contrarian signal automático;
- observed liquidations ≠ estimated liquidation maps;
- CVD depende de metodologia;
- nenhuma evidência avançada é Hard Gate universal;
- ausência de advanced data não invalida Asset Core;
- complexidade de aquisição deve demonstrar valor incremental;
- Data Feed deverá evoluir explicitamente se dados avançados forem incorporados.

---

# 13. Integração D1–D5

A síntese será:

> **hierárquica, scenario-relative e baseada na função semântica das evidências.**

Sem média ponderada ou majority voting.

Papéis das evidências:
- Premise-Defining;
- Gate Evidence;
- Supporting;
- Opposing;
- Contextual.

Tipos de conflito:
- CFT-1 — Compatible Tension;
- CFT-2 — Material Tension;
- CFT-3 — Critical Contradiction;
- CFT-4 — Epistemic Conflict.

Technical Bias:
- Bullish;
- Bearish;
- Balanced;
- Indeterminate.

Scenario Coherence:
- High;
- Moderate;
- Low;
- Indeterminate.

Princípios:
- D1 possui primazia estrutural, não veto universal;
- evidência auxiliar não compensa falha de Hard Gate;
- Range tende a Bias Balanced, mas pode ter setup direcional;
- setup direction, regime direction e bias não são sinônimos;
- hipótese concorrente deve permanecer visível;
- missing optional data não constitui evidência negativa;
- Classification precede Confidence.

---

# 14. CSM — contrato consolidado

Pipeline:
> D1–D5 → Intrinsic Technical State → CSM → Systemic Alignment.

CSM não reclassifica D1–D5.

Contrato mínimo:
- Market Regime;
- Leadership;
- Breadth;
- Rotation State;
- Persistence;
- Confidence;
- Freshness / Provenance.

Interface Asset × CSM:
- Relative Strength;
- Systemic Alignment.

Taxonomia de Systemic Alignment:
- Aligned;
- Neutral;
- Divergent-Idiosyncratic;
- Conflicting.

Princípios:
- CSM ≠ BTC;
- BTC e ETH são evidências sistêmicas importantes, não fórmula fixa;
- sequência BTC→ETH→alts não é lei;
- Relative Strength não é D6;
- CSM não é Hard Gate universal;
- CSM Full consome Capital Rotation;
- CSM Lite é deliberadamente limitado;
- ausência de CSM não inviabiliza Asset Core;
- CSM favorável não satisfaz Hard Gate intrínseco;
- CSM adverso não invalida tecnicamente um setup por si só;
- Setup Confidence e CSM Confidence permanecem separados.

---

# 15. Setup Hypothesis — contrato e lifecycle

Setup Hypothesis:
> hipótese técnica formal, horizon-specific, falsificável, versionada e temporalmente rastreável.

Identidade:
- Setup ID único e imutável;
- Family;
- Direction;
- Horizon;
- Structural Premise;
- Origin Scenario ID;
- Confirmation Specification;
- Invalidation Specification;
- Validity Rule;
- Resolution Rule;
- Timing;
- Technical Room;
- CSM;
- Confidence;
- Evidence Links;
- Method Version.

`No Setup` = ausência de objeto, não lifecycle state.

Lifecycle:
- Watch;
- Developing;
- Confirmed;
- Extended;
- Lapsed;
- Invalidated;
- Resolved.

Estados terminais:
- Lapsed;
- Invalidated;
- Resolved.

Regras:
- Lapsed apenas pré-confirmação;
- Resolved apenas pós-confirmação;
- Extended é irreversível para o mesmo Setup ID;
- Assessment Suspended é metaestado;
- Indeterminate é estado epistemológico, não lifecycle;
- família, direção e horizonte não mudam dentro do mesmo ID;
- nova oportunidade = novo Setup ID;
- Transition Log obrigatório;
- snapshot e event log são complementares.

---

# 16. Famílias F1–F4 — especificações consolidadas

## F1 — Trend Continuation
Eligibility:
- D1 Trend;
- direção definida;
- estrutura não Broken;
- região plausível em D2.

Developing:
- interação material com região de continuação.

Hard Gates:
- Trend Integrity Preserved;
- Valid Continuation Location;
- Directional Resumption.

D3 e D4 não são gates universais.

Invalidation:
- falha da premissa específica de continuação; pode ocorrer antes da quebra do Protected Swing.

Lapse:
- região abandonada sem retomada ou perda de atualidade.

Extended:
- afastamento material e Technical Room deteriorado.

Resolved:
- perna de continuidade cumpre função estrutural.

## F2 — Structural Breakout
Eligibility:
- estrutura de contenção válida;
- boundary identificável;
- direção definida.

Developing:
- Breach/PCSB.

Hard Gates:
- Valid Structure;
- PCSB;
- Acceptance Outside Structure.

Invalidation:
- Reclaim + Re-Acceptance interna ou condição equivalente predefinida.

Lapse:
- pressão/ruptura não evolui e hipótese perde atualidade.

Extended:
- afastamento material da breakout zone.

Resolved:
- nova estrutura direcional se estabelece ou caminho estrutural previsto é cumprido.

## F3 — Structural Reversal
Eligibility:
- estrutura direcional anterior;
- deterioração/counter-structural evidence.

Developing:
- Counter-Structural Break / Transition.

Hard Gates:
- Prior Structure Lost;
- Transition Resolved;
- Opposite Structure Established.

Invalidation:
- restauração da estrutura anterior ou falha material da nova.

Lapse:
- deterioração não evolui / transition perde atualidade sem falsificação formal.

Extended:
- primeira perna da nova estrutura já avançada.

Resolved:
- nova tendência está estabelecida; oportunidades subsequentes migram para F1.

## F4 — Range Rotation
Eligibility:
- Range válido;
- interação com extremo relevante;
- direção de rotação definida.

Developing:
- interação material, breach/sweep/reclaim candidate.

Hard Gates:
- Range Remains Valid;
- Relevant Extreme Interaction;
- Rejection or Re-Acceptance Inside Range.

Invalidation:
- Acceptance além da boundary que deveria conter o preço.

Lapse:
- tentativa abandona região sem confirmação.

Extended:
- parcela material da rotação já percorrida.

Resolved:
- referência estrutural definida na hipótese é alcançada ou a função do setup se encerra.

Competições principais:
- F2 × F4;
- F1 × F3.

Subtipos permanecem adiados até validação das famílias principais.

---

# 17. Plano de validação empírica

Três níveis:

- **V1 — Construct Validation**
- **V2 — Classification Validation**
- **V3 — Predictive Validation**

Progressão de pilotos:

- P0 — Data & Causal Replay Integrity;
- P1 — D1;
- P2 — D2;
- P3 — D3;
- P4 — D5;
- P5 — D4-Core;
- P6 — Síntese;
- P7 — F1–F4 e lifecycle;
- P8 — Confidence;
- P9 — CSM;
- P10 — Predictive Validation;
- P11 — Prospective Shadow Mode.

Princípios:
- causal replay obrigatório;
- outcomes futuros nunca alteram labels históricos;
- retorno financeiro não é primeiro critério;
- calibration / validation / holdout separados;
- walk-forward e sensitivity testing;
- parameter plateau > pico isolado;
- ablation e additive tests;
- Version Freeze antes de piloto formal;
- Experiment Log auditável;
- complexidade precisa demonstrar ganho incremental.

Status candidatos de componentes:
- Candidate;
- Under Validation;
- Provisionally Accepted;
- Accepted;
- Rejected;
- Deferred.

---

# 18. Especificação executável de P0/P1

## P0 — objetivo
Validar:
- dataset identity/provenance;
- OHLCV;
- gaps/anomalias;
- resampling;
- candle boundaries;
- causal replay;
- determinismo;
- checkpoint/restart;
- timestamps causais.

Dataset Manifest mínimo:
- Dataset ID;
- Asset;
- Venue;
- Market Type;
- Instrument;
- Source;
- Start/End;
- Native Granularity;
- Derived Timeframes;
- Timezone;
- Missing Data Policy;
- Data Version;
- Ingestion Timestamp;
- Checksum.

Regras:
- dataset imutável por experimento;
- sem interpolação silenciosa;
- outlier ≠ erro automaticamente;
- replay chronological-only;
- snapshots por candle;
- Event Log;
- execução idêntica deve reproduzir resultados idênticos.

P0 é gate obrigatório de P1.

## P1 — objetivo
Comparar:
- M1 Fixed-Window Pivot;
- M2 Fixed-Percentage Reversal;
- M3 Volatility-Normalized Reversal.

Sem método híbrido na primeira rodada.

Universo inicial:
- poucos ativos líquidos e heterogêneos;
- BTC e ETH incluídos;
- microcaps fora do primeiro piloto.

Timeframes preferenciais da primeira rodada:
- Daily;
- 4h.

Períodos devem incluir:
- bull trend;
- bear trend;
- range;
- transition;
- volatility shock.

Métricas principais:
- Swing Count;
- Confirmation Delay;
- Parameter Sensitivity;
- Swing Stability;
- Regime Churn;
- Regime Duration;
- Indeterminate Rate;
- Protected Swing Stability;
- Structural Event Stability;
- Transition Quality;
- Look-Ahead Audit;
- Cross-Timeframe Behavior.

Princípios:
- não escolher “melhor gráfico” visualmente;
- human review é diagnóstico secundário;
- blind labels desejáveis;
- um ou mais métodos podem ser Provisionally Accepted;
- predictive outcome não decide P1.

Artefatos previstos:
### P0
1. Dataset Manifest;
2. Data Validation Report;
3. Gap/Anomaly Log;
4. Resampling Specification;
5. Causal Replay Specification;
6. Determinism Test Report;
7. P0 Decision Record.

### P1
1. D1 Experiment Manifest;
2. Method Specifications M1–M3;
3. Parameter Grid Manifest;
4. Swing Event Dataset;
5. Regime Timeline Dataset;
6. Structural Event Log;
7. Sensitivity Matrix;
8. Metrics Report;
9. Human Review Set;
10. Diagnostic Notes;
11. P1 Decision Record.

Reprodutibilidade:
> Experiment = Data Version + Method Version + Parameter Profile + Code Version.

---

# 19. Estado atual de maturidade no CP05

- propósito do módulo: alto;
- fronteiras intermodulares: altas em nível conceitual;
- constructo central: definido em nível de trabalho;
- D1–D5: conceitualmente fechadas e com plano de operacionalização;
- D1: arquitetura operacional detalhada, parâmetros ainda não escolhidos;
- D2: SRZ / Position / Technical Room definidos conceitualmente;
- D3: Interaction Episodes + Acceptance/Rejection + Participation definidos;
- D4-Core: proxies/sweeps/displacement definidos;
- D4 Advanced: arquitetura modular definida, implementação opcional;
- D5: Impulse/Persistence/Efficiency/Evolution definidos;
- síntese D1–D5: lógica hierárquica definida;
- CSM: contrato e regras de não contaminação definidos;
- Confidence: arquitetura epistemológica e escala candidata definidas;
- Setup Hypothesis: contrato formal e lifecycle definidos;
- F1–F4: family specifications conceitualmente fechadas;
- validation architecture: definida;
- P0/P1: protocolo de alto nível especificado;
- parâmetros numéricos: não escolhidos;
- implementação: não iniciada nesta conversa;
- validação empírica: não iniciada;
- metodologia normativa final: inexistente.

---

# 20. Questões deliberadamente abertas após o CP05

Permanecem abertas principalmente questões de **operacionalização, parametrização e validação**, e não de arquitetura conceitual nuclear:

1. medida final de volatilidade para swing/zonas/impulso;
2. valores e profiles de Swing Reversal;
3. tolerance de EH/EL;
4. regras numéricas de PCSB;
5. Structural Restoration parameters;
6. critérios quantitativos de Trend/Range/Transition;
7. largura operacional de SRZ;
8. zone consolidation thresholds;
9. parâmetros de Structural Position;
10. thresholds de Technical Room e Extended;
11. Acceptance Evidence Window;
12. regras numéricas de Persistence/Closing/Re-Acceptance;
13. baseline e classes quantitativas de Participation;
14. D5 windows e thresholds;
15. SLPZ/equal-high/sweep/displacement parameters;
16. utilidade incremental de FVG;
17. necessidade efetiva de RSI/MACD/MAs;
18. escala operacional final e threshold mínimo de Confidence;
19. critérios quantitativos de Lapsed/Resolved;
20. tolerance rules de invalidation;
21. benchmark e operacionalização de Relative Strength;
22. especificação final do CSM Lite;
23. metodologia upstream final de Capital Rotation para CSM Full;
24. Approved Market Sources;
25. algoritmo final de Canonical Market;
26. cross-venue anomaly thresholds;
27. historical depth e freshness thresholds;
28. uso futuro de OI/funding/order book/CVD/liquidations;
29. schema técnico final Asset PRO → CSE;
30. Dataset Manifest real do P0;
31. seleção efetiva de ativos/períodos do P1;
32. Parameter Grid real de M1–M3;
33. implementação do Causal Replay Engine;
34. execução e decisão de P0;
35. execução e decisão de P1;
36. posterior validação P2–P11.

---

# 21. Regras que não devem ser reintroduzidas sem nova justificativa

- Não reconstruir Macro ou Institutional Flow dentro do Asset PRO.
- Não transformar Capital Rotation em cálculo interno completo do Asset.
- Não usar BTC/ETH como fórmula fixa do CSM.
- Não assumir ciclo fixo BTC → ETH → large caps → alts.
- Não usar CSM como veto ou confirmação automática de setup.
- Não converter D1–D5 em média ponderada ou majority voting sem evidência posterior.
- Não permitir soft evidence compensar Hard Gate ausente.
- Não contar indicadores derivados do mesmo preço como evidências independentes.
- Não definir tendência por média móvel.
- Não equiparar Breach, PCSB e Acceptance.
- Não equiparar Reclaim e Re-Acceptance.
- Não equiparar sweep a manipulação/smart money.
- Não equiparar proxy estrutural a liquidez observada.
- Não tratar FVG como institutional footprint ou guaranteed fill.
- Não tratar OI/funding/CVD/liquidations como sinais direcionais autônomos.
- Não transformar missing data em zero/neutral.
- Não transformar invalidação técnica em stop operacional.
- Não reutilizar Setup ID após terminalidade.
- Não mudar família, direção ou horizonte de um Setup ID.
- Não utilizar outcomes futuros para redefinir labels históricos.
- Não escolher parâmetros por P&L antes de construct/classification validation.
- Não promover resultado experimental diretamente a norma.

---

# 22. Ponto exato de retomada

## Etapa 36 — Pacote de especificações de implementação do P0

Objetivo:

> transformar o protocolo P0 em artefatos técnicos concretos e implementáveis antes de escrever ou validar o Structural Engine de D1.

Deve definir, no mínimo:

1. schema formal do **Dataset Manifest**;
2. schema formal do **candle OHLCV**;
3. regras automatizáveis de validação de integridade;
4. política de gaps/anomalias;
5. Candle Boundary Policy;
6. Resampling Specification;
7. interface do **Causal Replay Engine**;
8. formato do estado persistido/snapshot;
9. formato do Event Log;
10. checkpoint/restart contract;
11. determinism test;
12. critérios automatizáveis de aprovação/reprovação de P0;
13. versionamento de Data / Method / Code;
14. separação entre artefatos experimentais e documentação metodológica;
15. decisão de quais requisitos exigem implementação no repositório da Suite e quais pertencem ao Data Feed.

Regra de retomada:

> não iniciar escolha de parâmetros D1 nem executar P1 antes de fechar a especificação de P0 e demonstrar que o ambiente de replay é causal, determinístico, auditável e reproduzível.

---

**Fim do CP05**
