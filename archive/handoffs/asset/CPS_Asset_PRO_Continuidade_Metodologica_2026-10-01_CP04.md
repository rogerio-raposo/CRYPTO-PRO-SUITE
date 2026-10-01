# CRYPTO PRO SUITE
## Asset PRO — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-01  
**Checkpoint:** CP04  
**Checkpoint anterior:** CP03  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Asset PRO — Metodologia Geral  
**Finalidade:** permitir retomada controlada em nova conversa sem depender da memória do modelo e sem regressão metodológica.
**Ponteiro operacional de continuidade:** `archive/handoffs/asset/README.md`
**Natureza deste CP:** snapshot autônomo do estado metodológico corrente.

---

# 1. Regras de fonte e continuidade

- Repositório e documentos persistidos são a fonte de verdade.
- Memória do modelo pode orientar recuperação, mas não constitui evidência.
- Não preencher lacunas por inferência.
- Não transformar proposta histórica em decisão vigente.
- Não transformar este handoff em documento normativo.
- Distinguir explicitamente: histórico, vigente, superado, proposto, adiado, indeterminado e decisão de trabalho desta conversa.
- Não reabrir automaticamente etapas já validadas neste checkpoint sem nova evidência, conflito documental ou decisão posterior.
- Alterações posteriores na branch `main` prevalecem quando possuírem autoridade documental superior.
- Decisões específicas de outro módulo não devem ser importadas para o Asset PRO sem análise de interface.

---

# 2. Base histórica recuperada no Modo Partida

O Diagnóstico de Partida foi realizado antes do desenvolvimento corrente.

Principais conclusões históricas recuperadas:

- Asset PRO é componente independente do Volume III.
- Sua função histórica consolidada é **análise técnica individual profunda + timing**.
- Pergunta funcional histórica: **“Quando um ativo apresenta oportunidade técnica?”**
- Macro e fluxo institucional agregados não devem ser reconstruídos dentro do Asset PRO.
- Capital Rotation trata contexto agregado/rotação; Asset PRO trata estrutura/timing do ativo individual.
- Ranking Institucional seleciona/compara ativos e não deve duplicar Full Technical Analysis.
- CSE integra evidências na camada estratégica; decisão/execution final permanece humana.
- Portfolio Construction pertence ao CSE.
- Data Feed é produtor de dados; interpretação pertence aos módulos analíticos.
- Dados utilizados devem ser verificáveis e possuir provenance.
- Versionamento formal dos módulos permanece adiado até o fechamento inicial da Suite.

Registros históricos particularmente relevantes incluem RH-0045, RH-0050, RH-0056–0059, RH-0067, RH-0071, RH-0101, RH-0158, RH-0159, RH-0164 e RH-0166.

Histórico técnico recuperado como baseline, mas **não automaticamente normativo**:
- multi-timeframe;
- Price Action;
- suporte/resistência;
- Fibonacci;
- médias móveis;
- Volume Profile;
- volume;
- Wyckoff;
- SMC;
- RSI/MACD;
- cenários;
- invalidação;
- executive summary.

Não existe decisão histórica suficiente para fixar automaticamente:
- conjunto específico de médias;
- parâmetros RSI/MACD;
- timeframes obrigatórios universais;
- score 0–100;
- probabilidades numéricas de cenários;
- pesos;
- confluence score.

---

# 3. Constructo central corrente

Formulação de trabalho:

> **Estado de Oportunidade Técnica do Ativo:** grau em que a estrutura observável de mercado de um criptoativo, em determinado momento e horizonte analítico, apresenta configuração tecnicamente coerente, suficientemente desenvolvida e falsificável para sustentar um ou mais cenários direcionais, com condições explícitas de confirmação e invalidação.

Princípios:
- avalia estado técnico, não qualidade fundamental do projeto;
- não é previsão determinística;
- não é recomendação automática de compra/venda;
- deve ser falsificável;
- não decide sizing, alocação ou portfólio;
- constructo vem antes de indicadores;
- ferramentas técnicas são evidências/instrumentos, não dimensões por tradição.

---

# 4. Arquitetura de contexto sistêmico — CSM

Foi identificada uma lacuna na análise isolada do ativo: altcoins podem sofrer forte interferência do regime agregado e da rotação interna do mercado cripto.

Foi criado o conceito:

> **CSM — Contexto Sistêmico de Mercado:** camada contextual do Asset PRO que incorpora informação upstream sobre regime agregado e rotação de capital para interpretar a estrutura individual do ativo.

Decisões de trabalho:
- CSM não é uma sexta dimensão intrínseca.
- Em execução integrada, **Capital Rotation PRO é a fonte primária candidata** do CSM.
- O CSM consome contexto; não reconstrói o Capital Rotation.
- CSM não deve funcionar como veto automático.
- Divergência ativo × mercado pode representar força idiossincrática.
- Systemic Alignment deverá preservar estados como alinhamento, neutralidade, divergência e conflito, a operacionalizar.
- O contexto deve preservar horizonte temporal.
- Execução standalone poderá usar um **CSM Lite**, deliberadamente inferior ao Capital Rotation completo.

Contrato semântico candidato recebido do Capital Rotation:
- Market Regime;
- Market Leadership;
- Market Breadth;
- Rotation State;
- Persistence;
- Confidence;
- Horizon;
- Freshness / Provenance.

Backlog criado no Capital Rotation:
`03-componentes/21-rotation/BACKLOG.md`
- **BL-ROT-001 — Rotação intramercado cripto e interface com o CSM do Asset PRO**.
- A sequência BTC → ETH → large caps → demais altcoins foi registrada como hipótese histórica a testar, não como regra fixa.

---

# 5. Dimensões primárias correntes do Asset PRO

O núcleo intrínseco foi decomposto em cinco dimensões.

## D1 — Estrutura e Regime do Ativo
Pergunta:
> qual é a organização estrutural atual do preço, sua direção quando existente e a integridade dessa estrutura?

Elementos correntes:
- swing estrutural objetivo;
- regimes: Trend / Range / Transition / Indeterminate;
- direção de Trend: Up / Down;
- integridade: Intact / Weakening / Broken;
- eventos: breach, confirmed structural break, failed break/reclaim;
- continuidade ≠ reversão;
- Transition evita falsa dicotomia uptrend/downtrend;
- multi-timeframe por papéis CTF / PTF / TTF;
- timeframe superior possui maior alcance, não veto absoluto.

D1 não deve ser definido por média móvel, RSI, MACD ou nomenclatura SMC.

## D2 — Localização e Contexto Estrutural
Pergunta:
> onde o preço está dentro da estrutura e quais regiões relevantes condicionam o cenário?

Elementos:
- Position;
- Reference Map;
- preferência por Structural Reference Zones em vez de linhas arbitrárias;
- relevância por evidência estrutural, reação, recência, timeframe, participação e persistência;
- hierarquia Primary / Secondary / Tactical References;
- posição em range ou tendência;
- congestionamento versus structural open space;
- distância deve futuramente ser normalizada por volatilidade;
- confluência = diversidade de evidência, não contagem de indicadores.

Fibonacci = complementar; Volume Profile = candidato forte condicionado a dados; suporte/resistência = nuclear desde que operacionalizado.

## D3 — Participação e Aceitação
Pergunta:
> a atividade negociada e a permanência do preço confirmam aceitação, rejeição ou evidência inconclusiva?

Subconstructos:
- Participation;
- Acceptance / Rejection.

Princípios:
- volume alto não possui direção por si só;
- participação deve ser relativa a baseline;
- breakout não equivale a acceptance;
- Volume temporal e Volume Profile observam objetos diferentes;
- value migration é hipótese útil a testar;
- spot e derivativos não devem ser misturados silenciosamente;
- OI, funding, delta/CVD etc. permanecem candidatos futuros;
- D3 mede atividade/aceitação; D5 mede comportamento do preço.

## D4 — Liquidez, Proxies e Deslocamentos
Definição corrente:
> avalia dados observáveis e inferências explicitamente classificadas relacionadas à capacidade de execução, concentração potencial de ordens, excursões através de referências estruturais e regiões geradas por deslocamentos, sem presumir intenção dos participantes.

Classes:
- Observed;
- Derived;
- Proxy;
- Model-estimated.

Subcamadas:
- liquidez observável;
- proxies estruturais;
- deslocamentos / price imbalances.

Princípios:
- liquidez real ≠ proxy de liquidez;
- equal highs/lows são proxies, não prova de stops;
- sweep deve ser evento observável, sem narrativa de “smart money”;
- FVG pode ser padrão geométrico testável, mas valor preditivo é aberto;
- order-book imbalance ≠ price imbalance;
- Order Blocks têm baixa prioridade até definição objetiva e valor incremental;
- mapas de liquidação/heatmaps exigem provenance e metodologia;
- regiões de liquidez não são “ímãs” inevitáveis.

## D5 — Impulso e Persistência
Pergunta:
> qual é a intensidade, persistência e evolução do movimento direcional do preço?

Componentes:
- Directional Impulse;
- Persistence;
- Directional Efficiency;
- Evolution: accelerating / stable / decelerating.

Princípios:
- D1 = existência/integridade da estrutura; D5 = força dinâmica;
- magnitude deve ser normalizada por volatilidade;
- burst ≠ persistência;
- divergence é flag, não dimensão nem sinal automático de reversão;
- preço deve ser fonte primária quando possível;
- RSI, MACD e médias são representações auxiliares e não votos independentes;
- múltiplas transformações da mesma série pertencem à mesma família de evidência.

---

# 6. Famílias de evidência

Arquitetura corrente:

- E1 — Estrutura de preço;
- E2 — Localização / Value;
- E3 — Participação / Acceptance;
- E4 — Liquidez / Imbalance;
- E5 — Momentum / Persistence.

Frameworks:
- Wyckoff = framework interpretativo complementar, não score independente;
- SMC = deve ser decomposto em componentes observáveis, não tratado como bloco;
- Price Action = linguagem estrutural transversal;
- volatilidade = contexto transversal, não mérito;
- força relativa = candidato para Asset × CSM, não sexta dimensão.

Princípio:
> múltiplas transformações do mesmo fenômeno não constituem múltiplas confirmações independentes.

---

# 7. Camada de síntese

D1–D5 não devem ser inicialmente comprimidas em média ponderada.

Objetos de síntese correntes:
- Horizon-Specific Directional Technical Bias;
- Scenario Coherence;
- Systemic Alignment;
- Setup Hypothesis;
- Setup Lifecycle;
- Scenario Architecture;
- Confidence.

Technical State, Scenario e Setup Hypothesis são objetos diferentes.

## Bias
Estados conceituais:
- Bullish;
- Bearish;
- Balanced / Two-Sided;
- Indeterminate.

Todo bias deve possuir Horizon Tag.

## Scenario Coherence
Avalia quão compatível o conjunto de evidências é com uma hipótese específica.
Não significa simples concordância direcional entre dimensões.

## Systemic Alignment
CSM contextualiza o cenário individual e não altera automaticamente o bias.

## Confidence
Permanece ortogonal ao mérito técnico e deve refletir robustez epistemológica, cobertura, provenance, conflitos, freshness e subjetividade residual.

Não foi definida escala formal do Confidence do Asset PRO.

---

# 8. Taxonomia mínima de famílias de setup

Quatro famílias primárias:

- **F1 — Trend Continuation**
- **F2 — Structural Breakout**
- **F3 — Structural Reversal**
- **F4 — Range Rotation / Mean Reversion**

`No Setup` é resultado válido, não quinta família.

Eventos como:
- pullback;
- retest;
- sweep;
- reclaim;
- FVG;
- padrões gráficos;
não são inicialmente famílias primárias; são mecanismos, eventos, subtipos ou evidências.

Todo Setup Hypothesis deve possuir:
- Setup ID;
- Family;
- Direction;
- Horizon;
- Structural Premise;
- Current State;
- Confirmation Conditions;
- Invalidation Conditions;
- Relevant D1–D5 Evidence;
- CSM Alignment;
- Confidence.

---

# 9. Gates universais e ciclo de vida

Universal Gates correntes:
- UG1 — Data Sufficiency;
- UG2 — Horizon Definition;
- UG3 — Structural Premise;
- UG4 — Falsifiability.

Ciclo de vida:
- No Setup;
- Watch;
- Developing;
- Confirmed;
- Extended;
- Invalidated;
- Lapsed.

Definições centrais:
- Confirmed = gates obrigatórios da hipótese satisfeitos;
- Extended = tese ainda válida, mas timing/localização original deteriorou;
- Invalidated = evento incompatível com a hipótese;
- Lapsed = oportunidade perdeu atualidade sem confirmação nem falsificação explícita.

A máquina de estados é comum; o conteúdo dos gates é family-specific.

---

# 10. Gates conceituais por família

## F1 — Trend Continuation
- elegibilidade: D1 identifica Trend válida;
- Watch: localização futura plausível;
- Developing: interação com a localização sem destruir estrutura;
- Confirmed: evidência objetiva de retomada da direção dominante;
- Extended: continuação ocorreu, timing/localização deterioraram;
- Invalidated: estrutura necessária à continuidade foi rompida conforme regra.

## F2 — Structural Breakout
- elegibilidade: estrutura de contenção/referência definida;
- Watch: aproximação/pressão no limite;
- Developing: breach relevante;
- Confirmed: evidência suficiente de acceptance fora da estrutura;
- Extended: preço já afastado da região de confirmação;
- Invalidated: ruptura falha e negociação relevante retorna à estrutura anterior.

## F3 — Structural Reversal
- elegibilidade: regime direcional anterior identificável;
- Watch: deterioração;
- Developing: ruptura contra estrutura anterior / Transition;
- Confirmed: nova estrutura oposta suficientemente estabelecida;
- Extended: nova estrutura já avançada;
- Invalidated: recuperação material da estrutura anterior ou falha da nova.

## F4 — Range Rotation
- elegibilidade: D1 identifica range válido;
- Watch: preço aproxima-se de extremo relevante;
- Developing: reação compatível com preservação;
- Confirmed: rejeição/retorno ao interior satisfaz critérios;
- Extended: parcela material do range já percorrida;
- Invalidated: acceptance além do limite que deveria permanecer válido.

CSM não é Hard Gate universal.
D4 não é Hard Gate universal.
Importância relativa das dimensões pode variar por família/subtipo.

---

# 11. Invalidação e falsificabilidade

Definição corrente:
> **Technical Invalidation:** ocorrência de condição observável, previamente associada a uma hipótese e ao seu horizonte, que torna incompatível a manutenção daquela hipótese em seu estado atual.

Distinções:
- Setup Invalidation;
- Scenario Invalidation;
- Structural Invalidation.

Princípios:
- adversidade ≠ invalidação;
- toda invalidação possui Horizon Tag;
- breach ≠ trigger confirmado;
- invalidação pode exigir close, persistence, acceptance, evento estrutural ou combinação;
- volatilidade pode exigir tolerance rule;
- deterioration flags antecedem possível invalidação, mas não a substituem;
- CSM adverso não invalida automaticamente setup;
- falha de dados gera insufficiency/suspension, não invalidação de mercado;
- Canonical Venue/Market precisa ser identificável para gatilhos;
- Setup ID invalidado permanece historicamente invalidado; recuperação gera nova hipótese;
- Initial Invalidation e Active Invalidation podem diferir somente por regra pré-especificada e auditável;
- histórico de mudanças de invalidação deve ser preservado;
- stop operacional pertence ao CSE/Execution, não ao Asset PRO.

---

# 12. Fontes de mercado e Data Feed

A dependência Asset PRO ↔ dados foi formalizada em três artefatos de trabalho:

1. `03-componentes/24-asset/MARKET_DATA_REQUIREMENTS.md`
2. `03-componentes/24-asset/CANONICAL_MARKET_POLICY.md`
3. `03-componentes/24-asset/DATA_SUFFICIENCY_GATE.md`

Status dos três:
> WORKING / NON-NORMATIVE.

Princípio arquitetural:
> Asset PRO deve consumir contrato de dados do Crypto Pro Data Feed; não deve depender de consultas ad hoc diretas às exchanges como parte da metodologia.

## Canonical Market
Conceitos separados:
- Canonical Market;
- Validation Venue;
- Fallback Source.

Foi proposto **Canonical Structural Market** para D1/D2/D5 e baseline compatível de D3/D4.

A seleção deve usar:
- Eligibility Gates;
- Comparative Assessment;
- provenance;
- lifecycle control.

Não foi fixada ordem Binance/Bybit/OKX/Bitget/MEXC.

Spot e derivatives permanecem distintos.

Cross-venue validation pode ser necessária para eventos críticos/anômalos.

Canonical Market change é evento metodológico; deve ser auditável e, quando viável, reconstruir a janela histórica.

## Data Sufficiency
Estados:
- SUFFICIENT;
- DEGRADED;
- INSUFFICIENT;
- SUSPENDED.

Sufficiency deve existir globalmente e por dimensão.

Ausência de evidência não pode ser transformada em evidência neutra/negativa.

Advanced D4 data podem estar indisponíveis sem impedir D4 estrutural-proxy.

---

# 13. Artefatos persistidos durante esta conversa

### Asset PRO
- `03-componentes/24-asset/MARKET_DATA_REQUIREMENTS.md`
  - criado no commit `6663d8f9f52a55c2382b158017f772160a5ffa08`;
  - alinhamento posterior de estados de sufficiency no commit `18e8da3f4b479fb13461de4cb018d2f9c4249616`.

- `03-componentes/24-asset/CANONICAL_MARKET_POLICY.md`
  - commit `730ebac450e5bce919cfd0389f1ba999712f2d53`.

- `03-componentes/24-asset/DATA_SUFFICIENCY_GATE.md`
  - commit `fc75b9799039f9d726a2ad81c20018d3b2560987`.

### Capital Rotation
- `03-componentes/21-rotation/BACKLOG.md`
  - BL-ROT-001 — rotação intramercado cripto e interface com CSM;
  - commit `122ae09d09890c0d5eae7c585940c05f08b9d88a`.

---

# 14. Questões deliberadamente abertas

Não estão fechados:

1. operacionalização numérica de swings;
2. thresholds de confirmação/ruptura;
3. timeframes universais ou presets por horizonte;
4. parâmetros de médias, RSI, MACD ou outros indicadores;
5. escolha final dos instrumentos por dimensão;
6. score, pesos ou cardinalização;
7. escala formal de Confidence do Asset PRO;
8. taxonomia de subtipos de setup;
9. regras operacionais completas de Developing → Confirmed;
10. regras quantitativas de Extended e Lapsed;
11. tolerance rules de invalidação;
12. thresholds de cross-venue anomaly;
13. seleção efetiva de Approved Market Sources;
14. algoritmo final de Canonical Market;
15. spot versus perpetual como referência por classe de ativo/fenômeno;
16. profundidade histórica mínima por CTF/PTF/TTF;
17. freshness thresholds;
18. agregação multi-venue de volume/OI/funding;
19. advanced order-flow / CVD / liquidation data;
20. validação empírica/backtest;
21. eventual necessidade de score;
22. interface técnica final Asset PRO → CSE;
23. especificação operacional final CSM Lite;
24. metodologia final do Capital Rotation para rotação intramercado, registrada em backlog.

---

# 15. Decisões/regras que não devem ser reintroduzidas sem justificativa

- Não recriar Macro ou Institutional Flow dentro do Asset PRO.
- Não usar BTC/ETH como fórmula fixa do CSM.
- Não assumir sequência fixa BTC → ETH → large caps → alts.
- Não tratar Wyckoff ou SMC como scores independentes.
- Não contar RSI + MACD + médias como três confirmações independentes do mesmo momentum.
- Não usar Fibonacci como prova autônoma de suporte/resistência.
- Não tratar proxy de liquidez como liquidez observada.
- Não atribuir intenção a “smart money” a partir do gráfico.
- Não transformar ausência de dados em zero/neutralidade.
- Não usar CSM como veto automático.
- Não transformar invalidation de setup em reversão automática.
- Não confundir invalidação técnica com stop operacional.
- Não escolher exchange canônica apenas por hábito/preferência.
- Não misturar spot/perpetual ou múltiplas venues silenciosamente.
- Não introduzir score/pesos antes de demonstrar necessidade.

---

# 16. Estado de maturidade no CP04

- propósito do módulo: alto;
- fronteiras: altas em nível conceitual;
- constructo: definido em nível de trabalho;
- D1–D5: decompostas conceitualmente;
- CSM: contrato conceitual definido;
- famílias de evidência: definidas;
- síntese: arquitetura definida;
- famílias F1–F4: definidas;
- lifecycle: definido;
- invalidação: arquitetura definida;
- requisitos de dados: especificados em nível de trabalho;
- Canonical Market Policy: especificada conceitualmente;
- Data Sufficiency Gate: especificado conceitualmente;
- parâmetros operacionais: ainda abertos;
- validação empírica: não iniciada;
- metodologia normativa final: não existe.

---

# 17. Ponto exato de retomada

## Etapa 15 — Confirmação de Setup: Developing → Confirmed

Objetivo:
> definir formalmente o que significa um setup satisfazer seus confirmation gates sem confundir confirmação técnica com aumento de Confidence e sem produzir confirmação excessivamente tardia.

Questões mínimas:
- confirmação é evento instantâneo, janela de evidência ou combinação?
- quais gates são universais e quais family-specific?
- como distinguir confirmation evidence de soft evidence?
- quando D3 acceptance é obrigatória;
- como D1/D3/D5 interagem sem double counting;
- como usar CSM sem transformá-lo em gate universal;
- como registrar confirmação provisória quando dados estão DEGRADED;
- relação entre Confirmed, Extended e timing tardio;
- tratamento de confirmação por CTF/PTF/TTF;
- quando cross-venue validation é necessária para confirmation;
- diferença entre confirmation e Confidence;
- necessidade ou não de estados intermediários adicionais.

Regra:
> não definir ainda parâmetros numéricos universais, score ou pesos. Primeiro fechar a lógica conceitual de confirmação.

---

**Fim do CP04**
