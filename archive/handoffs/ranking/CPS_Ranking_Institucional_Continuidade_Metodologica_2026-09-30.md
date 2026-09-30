# CRYPTO PRO SUITE
## Ranking Institucional Simplificado — Registro de Continuidade Metodológica

**Data do checkpoint:** 30/09/2026  
**Status:** documento de continuidade de conversa; **não é documento normativo final**  
**Finalidade:** permitir a retomada do desenvolvimento em nova conversa sem depender da memória do modelo e sem regressão metodológica.

---

# 0. Como usar este documento

Este arquivo é o **handoff de continuidade** da conversa em que a metodologia geral do Ranking Institucional Simplificado está sendo reconstruída/desenvolvida.

Ao abrir uma nova conversa:

1. utilizar o template canônico armazenado em `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` em **Modo Continuidade**;
2. recuperar este handoff diretamente do repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30.md`;
3. tratá-lo como **estado de trabalho validado da conversa anterior**, sujeito ao Freshness Gate e à hierarquia documental do projeto;
4. exigir que o ChatGPT **não generalize a metodologia Microcaps** para o Ranking Geral;
5. exigir que ele **não preencha lacunas por inferência**;
6. retomar a partir da seção **“Próximo passo”** somente após o Diagnóstico de Continuidade;
7. quando houver conflito entre este checkpoint e documento oficial posterior do repositório, o documento oficial posterior prevalece;
8. este arquivo registra decisões e hipóteses de trabalho da conversa, mas **não substitui futuras especificações normativas aprovadas**.

---

# 1. Regras metodológicas permanentes nesta conversa

## 1.1 Fonte de verdade
- Repositório e arquivos oficiais são a fonte de verdade.
- Memória do modelo pode orientar recuperação, mas **não é evidência**.
- Não preencher lacunas silenciosamente.
- Não transformar proposta em decisão.
- Distinguir: vigente, histórico, superado, rejeitado, adiado e indeterminado.

## 1.2 Ranking Geral versus Microcaps
Regra explícita validada:
> **A metodologia Microcaps é específica e não deve ser generalizada automaticamente para o Ranking Geral.**

Consequências:
- sem promoção automática de regras Microcaps;
- sem usar semelhança como prova de generalidade;
- qualquer regra Microcaps só pode migrar para o Ranking Geral mediante evidência independente de generalidade ou nova decisão explícita.

## 1.3 Fronteiras
- Ranking permanece módulo independente.
- Full Technical Analysis/timing pertence ao Asset PRO.
- Full Tokenomics não pertence ao núcleo do Ranking.
- Portfolio Construction pertence ao CSE.
- Institutional Flow não deve ser reconstruído dentro do Ranking.
- Força da narrativa não deve ser recalculada no Ranking.
- Evitar double counting entre módulos e entre constructos internos.

## 1.4 Versionamento
A formalização de uma versão oficial do módulo permanece adiada até o lançamento inicial formal da Suite.

## 1.5 MEL
MEL — Methodology Evaluation Layer:
- componente interno do Ranking;
- não é módulo independente;
- inclusão na v1.0 da Suite permanece adiada até que os demais módulos estejam fechados.

---

# 2. Higiene de fontes

## 2.1 Primeiro arquivo enviado — IGNORAR
O usuário determinou explicitamente que o **primeiro arquivo enviado por engano** deve ser ignorado, porque já havia sido analisado em fases anteriores e sua reutilização poderia causar regressão metodológica.

Regra:
> **Não usar esse primeiro arquivo para reforçar, reinterpretar ou justificar decisões desta etapa, salvo revogação explícita do usuário.**

## 2.2 Segundo arquivo — válido apenas como insumo exploratório
Arquivo:
**“Critérios para Escolha de Criptomoedas, Avaliação de Tokenomics e Ajustes para Microcaps”**

Uso permitido:
- gerar hipóteses;
- testar conceitos;
- comparar arquitetura;
- identificar questões a investigar.

Uso não permitido:
- tratá-lo como documento normativo da Suite;
- importar hierarquias, critérios ou fórmulas automaticamente.

Pontos aproveitados:
- propagação típica BTC → ETH → large caps → midcaps → microcaps/memecoins;
- papel de liquidez, acessibilidade, risco relativo e narrativas;
- distinção entre fluxo geral e fluxo institucional;
- importância de verificar se crescimento do projeto gera demanda econômica pelo token.

---

# 3. Base histórica recuperada antes do desenvolvimento atual

## 3.1 Ranking histórico
Registros recuperados mostraram:
- Radar de Narrativas com pontuação + fase;
- NTF histórico combinando Narrative + Technical + Flow;
- monitoramento semanal;
- nível 1 semi-automático;
- universo Principal historicamente fixo em estágio anterior;
- Microcaps < US$100M;
- Índice de Convicção histórico;
- histórico comparável semanal;
- regra antiga de futuros obrigatórios para Microcaps posteriormente superada na metodologia atual de Microcaps;
- separação entre Ranking objetivo / Watchlist / Radar de Ativos Promissores;
- Driver preservado;
- Confidence acrescentado sem substituir Driver.

## 3.2 Arquitetura histórica de referência
**Macro → Capital Rotation → Institutional Flow → Ranking → Asset PRO**

Esta conversa revisou essa ordenação e concluiu posteriormente que **Institutional Flow deve ser logicamente upstream de Capital Rotation**.

## 3.3 Fronteiras históricas importantes
- Ranking independente.
- Institutional Flow:
  1. Investment Product Flows;
  2. Strategic Institutional Activity;
  3. Structural Institutional Adoption.
- Asset PRO = análise individual profunda + timing.
- Full tokenomics excluído do Ranking.
- Supply dynamics pode existir de forma estreita/complementar.
- Portfolio Construction fora do Ranking.

## 3.4 Microcaps atual
A metodologia Microcaps possui arquitetura e validações próprias.
Regra:
> **não usar Microcaps como “modelo geral reduzido” do Ranking.**

---

# 4. Fenômeno-alvo do Ranking

Decisão explícita do usuário:
> **“Para esta versão do CRYPTO PRO SUITE, mantenha o fluxo institucional como fenômeno-alvo do Ranking.”**

Formulação inicial:
> estimar quais criptoativos apresentam maior probabilidade relativa de capturar o próximo fluxo institucional.

Essa formulação foi **corrigida**, porque “próximo fluxo” sugeria que o fluxo atual teria de terminar antes de se procurar uma nova rotação.

## 4.1 Formulação atual
Fenômeno-alvo:
> **captura de fluxo institucional relevante no horizonte de análise.**

Finalidade:
> **estimar quais criptoativos estão relativamente mais bem posicionados para capturar fluxo institucional adicional no horizonte considerado, incluindo tanto a continuidade/intensificação de fluxos vigentes quanto a emergência de novos vetores.**

Regra temporal:
- evidências disponíveis até `t₀`;
- fenômeno prospectivo em `(t₀, t₀ + H]`;
- fluxo já ocorrido pode ser evidência de persistência, aceleração, desaceleração, saturação ou reversão;
- fluxo realizado **não pode ser confundido automaticamente com fluxo futuro**.

---

# 5. Arquitetura conceitual anterior à Etapa 9

## 5.1 Primeira decomposição
Famílias inicialmente consideradas:
1. Aderência ao vetor de fluxo;
2. Qualidade/robustez;
3. Tração/adoção;
4. Atratividade/assimetria;
5. Acessibilidade/operabilidade institucional.

Após testes, a arquitetura foi simplificada.

## 5.2 Arquitetura de trabalho
1. **Posicionamento em relação ao Fluxo**
2. **Capacidade de Captura**
3. **Trajetória das Evidências**
4. **Fricções à Captura**
5. **Confidence**
6. **Driver** como explicabilidade, não dimensão.

## 5.3 Capacidade de Captura
Definição provisória:
> conjunto de condições observáveis do ativo e de sua infraestrutura de mercado que tornam viável a entrada de capital institucional em escala relevante, caso exista um vetor de fluxo ao qual o ativo esteja adequadamente exposto.

Subcomponentes:
- **Acessibilidade Institucional**
- **Capacidade de Absorção**

Distinção:
- Exposição/Aderência: existe razão para o capital se dirigir ao ativo?
- Capacidade: se houver intenção, existem condições para o capital efetivamente entrar?

## 5.4 Trajetória
Conclusão:
> dimensão temporal é necessária, mas não foi demonstrado que deva ser score autônomo.

Termo preferido:
**Trajetória das Evidências**, não Momentum genérico.

## 5.5 Fricções
Definição provisória:
> condição observável capaz de impedir, restringir, desincentivar ou comprometer materialmente a captura ou sua sustentabilidade.

Regras:
- não duplicar liquidez/acesso/custódia se já estão em Capacidade;
- algumas fricções podem ser não lineares;
- algumas podem futuramente ser penalties, flags ou gates;
- Friction ≠ Confidence.

---

# 6. Etapa 9 — Teste adversarial

Foram testados cenários como:
- alto alinhamento + alta capacidade;
- alta aderência + baixa acessibilidade;
- alta capacidade + baixa aderência;
- estado forte mas deteriorando;
- estado intermediário mas fortalecendo;
- alto potencial + fricção grave;
- alta aparência de potencial + baixa qualidade de evidência;
- caso Microcap sem importar metodologia Microcaps.

Conclusões:
- Posicionamento e Capacidade são ortogonais.
- Trajectory agrega informação temporal sem precisar duplicar score.
- Frictions devem ficar separadas.
- Confidence é epistemológico.
- risco de double counting principal: **Capacidade × Fricções**.
- arquitetura sobreviveu ao teste adversarial inicial.

---

# 7. Etapa 10 — Especificação dos constructos

## 7.1 Relação do Ativo com o Vetor
Pergunta:
> Por que este ativo seria destinatário plausível do vetor identificado?

Não inclui:
- força geral da narrativa;
- magnitude agregada do fluxo;
- liquidez;
- deep TA;
- qualidade genérica.

## 7.2 Capacidade de Captura
Pergunta:
> Se houver intenção de alocar capital, existem condições práticas para isso ocorrer em escala relevante?

Subconstructos:
- Acessibilidade Institucional;
- Capacidade de Absorção.

## 7.3 Trajetória
Pergunta:
> O estado relevante está fortalecendo, estável ou deteriorando?

## 7.4 Fricções
Pergunta:
> Existe condição relevante capaz de impedir ou comprometer materialização/sustentabilidade?

Regra anti-double-counting:
> ausência/deterioração de propriedade positiva não vira automaticamente fricção independente.

## 7.5 Confidence
Pergunta:
> Quão robusta é a conclusão?

Regra:
> Confidence mede confiança na avaliação, não no ativo.

## 7.6 Driver
Função:
> explicar o principal fator da posição/classificação; não é score.

---

# 8. Etapa 11 — Universo e unidade de comparação

Decisões/hipóteses:
- universo de entrada deve ser dinâmico;
- elegibilidade ≠ mérito;
- avaliação ruim não deve ser confundida automaticamente com inelegibilidade;
- surgiu a unidade elementar **Ativo × Vetor**, depois refinada para **Ativo × Vetor × Horizonte**;
- saída final do Ranking continua sendo **ativo**.

---

# 9. Etapa 12 — Contrato upstream → Ranking

Princípio:
> módulos upstream devem entregar contexto suficientemente estruturado para orientar o Ranking sem decidir previamente quais ativos devem vencer.

Objetos diferenciados:
- contexto;
- direção de capital;
- evidência institucional.

Regras:
- Ranking consome conclusões upstream; não reconstrói o mesmo fenômeno;
- origem da evidência precisa ser rastreável;
- incerteza upstream precisa ser propagada;
- coerência temporal/freshness necessária;
- horizonte precisa ser explícito;
- narrativa ≠ vetor;
- fluxo observado pode ser usado como evidência, mas não como futuro já “contabilizado”.

---

# 10. Etapa 12A — Propagação do fluxo e rotação intracripto

Motivação:
o segundo arquivo apresentou hierarquia típica:
**BTC → ETH → large caps → midcaps → microcaps/memecoins**.

Conclusão:
- tratar como **hipótese recorrente de propagação**, não regra fixa;
- não usar como prior fixo do Ranking.

Forças explicativas:
- gradiente de risco;
- gradiente de liquidez;
- gradiente de acessibilidade institucional;
- tolerância a risco.

Distinção crítica:
- **propagação institucional direta**
versus
- **transmissão indireta de liquidez / difusão especulativa**.

Estados conceituais:
- concentração institucional;
- ampliação institucional;
- difusão especulativa.

Novo objeto upstream:
**Estado de Propagação do Fluxo**

BTC Dominance foi considerada variável prioritariamente pertencente ao Capital Rotation, não ao Ranking.

---

# 11. Etapa 12B — Bifurcação BTC / ETH / universo ranqueável

## 11.1 Bitcoin
Decisão:
> Bitcoin não depende da identificação de uma narrativa para justificar sua inclusão analítica.

BTC fica fora do Ranking narrativo/seletivo e permanece ligado aos módulos iniciais e ao BTC PRO.

## 11.2 Ethereum
ETH não deve ser tratado nem como “BTC 2” nem como altcoin ordinária.

Hipótese aprovada:
> **ETH = estrutura + vetores**

Razões:
- pode receber fluxo estrutural direto;
- pode receber fluxo associado a RWA, tokenização, DeFi, stablecoins etc.;
- “estrutura + narrativas” seria estreito demais, pois nem todo vetor é narrativo.

ETH possui status híbrido.

## 11.3 Altcoins
Universo nuclear do Ranking:
> ativos cuja captura relativa de fluxo exige discriminação entre vetores, setores, teses e características próprias.

---

# 12. Etapa 12C — Vetor de Fluxo versus Narrativa

## Narrativa
> tese/estrutura interpretativa compartilhada que concentra atenção e expectativas em torno de tema, setor, tecnologia ou transformação econômica.

## Vetor de Fluxo
> direção economicamente identificável de alocação de capital, vigente ou emergente, relevante em determinado horizonte.

Relação:
> narrativa pode originar, reforçar, organizar ou sinalizar um vetor, mas não é necessária nem suficiente para que ele exista.

Conclusões:
- Ranking deve receber **Vetores de Fluxo**, não simples Narrative Scores;
- unidade continua **Ativo × Vetor × Horizonte**.

---

# 13. Etapa 13 — Propriedade do Vetor de Fluxo

Alternativas testadas:
- Macro como proprietário — rejeitada;
- Institutional Flow como proprietário — insuficiente;
- Narrative Opportunity como proprietário — rejeitada;
- Ranking como proprietário — rejeitada;
- CSE como integrador upstream — não atribuído;
- **Capital Rotation como proprietário primário** — hipótese mais coerente.

Motivo:
> Capital Rotation responde “para onde o capital está se deslocando?”

Regra:
> Ranking recebe o vetor; não o produz.

---

# 14. Etapa 13A — Ordem Institutional Flow ↔ Capital Rotation

Conclusão validada:
> **Institutional Flow deve ser logicamente upstream de Capital Rotation.**

Razões:
- evita circularidade;
- permite que Capital Rotation já conheça a atividade institucional ao formar o vetor;
- melhora distinção entre propagação institucional e rotação geral/especulativa.

Arquitetura passou a ser tratada como **grafo de dependências**, não cadeia rígida.

Estado atual:
- Macro → regime;
- Institutional Flow → estado da atividade institucional;
- Narrative Opportunity → estado de teses/narrativas;
- Capital Rotation → integra entradas + dados próprios e forma Vetores de Fluxo;
- Ranking → avalia ativos;
- Asset PRO → timing/análise individual.

---

# 15. Etapa 14 — Múltiplos vetores

Conclusões:
- vários Vetores podem coexistir;
- relevância do vetor é upstream;
- Market Relevance ≠ Institutional Relevance;
- vetores podem ser independentes, relacionados ou redundantes;
- ativos podem ter múltiplas exposições;
- amplitude de exposição não é vantagem automática;
- vetores favoráveis/adversos devem permanecer visíveis;
- scores Ativo–Vetor não devem ser comparados transversalmente sem garantir comparabilidade.

---

# 16. Etapa 14A — Correção Capital Rotation ↔ Ranking

Decisão:
> **A identificação, comparação e priorização relativa dos Vetores de Fluxo pertencem ao Capital Rotation.**

Ranking:
> classifica **ativos**, não vetores.

Responsabilidades:

| Questão | Responsável |
|---|---|
| Regime | Macro |
| Atividade institucional | Institutional Flow |
| Narrativas/teses | Narrative Opportunity / Radar de Narrativas |
| Direção/rotação | Capital Rotation |
| Vetores de Fluxo | Capital Rotation |
| Relevância relativa dos Vetores | Capital Rotation |
| Propagação | Capital Rotation |
| Relação Ativo–Vetor | Ranking |
| Capacidade de Captura | Ranking |
| Trajectory | Ranking |
| Frictions | Ranking |
| Timing/TA profundo | Asset PRO |

---

# 17. Dois Radares, Ranking e Watchlist

## 17.1 Radar de Narrativas
Função:
> detectar e acompanhar teses/narrativas, fase e evolução.

Não deve:
- ordenar ativos como resultado final;
- provar sozinho a existência de Vetor de Fluxo.

## 17.2 Radar de Ativos Promissores
Função histórica recuperada:
> acompanhar ativos que ainda não entraram no Ranking, mas apresentam sinais iniciais relevantes.

Não faz parte do Ranking.

Historicamente:
- limite proposto de até 5 ativos;
- não alterava posição do Ranking;
- existia para evitar contaminar a objetividade;
- LIT e ASTER foram exemplos históricos dessa separação.

## 17.3 Watchlist
Decisão histórica:
> deve ser derivada objetivamente do Ranking, e não do “potencial percebido”.

## 17.4 Enquadramento atual do Radar de Ativos Promissores
Hipótese:
> camada auxiliar do domínio do Ranking para relações Ativo–Vetor promissoras, mas ainda insuficientemente demonstradas.

Não é obrigatório passar pelo Radar antes do Ranking.

---

# 18. Etapa 15 — Materialidade da relação Ativo–Vetor

Definição provisória:
> **Relação Ativo–Vetor Material:** vínculo economicamente relevante, observável e demonstrável entre criptoativo e mecanismo de alocação representado pelo Vetor, com plausibilidade causal suficiente.

Exigências:
1. relevância econômica;
2. observabilidade;
3. plausibilidade causal.

Teste contrafactual:
> se retirarmos o vetor, parte material da tese de captura do ativo desaparece?

Tipos:
- direta;
- funcional;
- infraestrutural;
- captura de valor;
- indireta.

Regra:
> Projeto–Vetor ≠ automaticamente Token–Vetor.

Candidate discovery ≠ relationship confirmation.

Estados provisórios:
- candidata;
- materialmente sustentada;
- insuficiente/não demonstrada;
- indeterminada.

Confidence não substitui ausência de relação.

---

# 19. Etapa 15A — Papel dos dois Radares

Consolidação:
- Radar de Narrativas = teses;
- Radar de Ativos Promissores = ativos ainda não prontos para Ranking;
- Ranking = ativos admitidos na metodologia;
- Watchlist = subconjunto objetivo derivado do Ranking.

O Radar de Ativos Promissores deve registrar:
- por que o ativo merece observação;
- **qual lacuna ainda impede sua admissão no Ranking**.

---

# 20. Etapa 16 — Decomposição da Relação Ativo–Vetor

Primeira hipótese:
1. Exposição Causal;
2. Captura Econômica pelo Ativo;
3. Evidência de Materialização;
4. Posicionamento Relativo no Vetor.

Essa arquitetura foi corrigida na Etapa 17.

---

# 21. Etapa 17 — Ortogonalidade, necessidade e suficiência

## 21.1 Evidência de Materialização
Não é dimensão autônoma.

É:
> camada empírica que sustenta ou contradiz os constructos.

## 21.2 Posicionamento Relativo
Substituído por:
> **Posição Estrutural no Vetor**

Definição:
> grau em que o ativo ocupa posição funcional, competitiva ou infraestrutural favorável dentro do mecanismo econômico representado pelo vetor.

## 21.3 Arquitetura atual da Relação Ativo–Vetor
Três propriedades substantivas:

1. **Exposição Causal**
   - existe mecanismo pelo qual o vetor afeta o projeto/ativo?

2. **Captura Econômica pelo Ativo**
   - o benefício chega economicamente ao token/criptoativo?

3. **Posição Estrutural no Vetor**
   - qual posição o ativo ocupa dentro desse mecanismo em relação aos peers?

Camadas transversais:
- Evidence / Materialization;
- Trajectory;
- Confidence.

Outros constructos:
- Capacidade de Captura;
- Fricções à Captura.

Os três componentes passaram provisoriamente pelos testes de:
- ortogonalidade;
- necessidade;
- suficiência.

## 21.4 Materiality Gate
Hipótese:
- Exposição Causal + Captura Econômica precisam de demonstração mínima para entrada;
- Posição Estrutural diferencia candidatos válidos.

Ainda sem thresholds.

---

# 22. Etapa 18 — Evidências e indicadores candidatos

Princípio:
> **Constructo → proposição → evidência admissível → indicador**

Não partir do indicador disponível.

## 22.1 Regras gerais de evidência
1. pertinência causal;
2. observabilidade;
3. especificidade Ativo × Vetor;
4. temporalidade;
5. comparabilidade;
6. independência informacional;
7. aceitar evidência contraditória.

## 22.2 Hierarquia provisória
- evidência direta;
- observacional relacionada;
- proxy;
- contextual.

Regra:
> constructo nuclear não deve ser demonstrado apenas por contexto ou proxy fraco.

## 22.3 Exposição Causal
Evidências candidatas:
- utilização específica ligada ao vetor;
- integração funcional real;
- dependência técnica/econômica;
- atividade originada no caso de uso;
- participação infraestrutural.

Associação temática/agregador não basta.

## 22.4 Captura Econômica
Subconjunto estreito de tokenomics pertinente ao Ranking.

Evidências candidatas:
- fees;
- staking funcional;
- collateral;
- segurança econômica;
- burn ligado ao uso;
- lock funcional;
- receita/distribuição quando aplicável;
- demanda obrigatória pelo token.

Não avaliar full tokenomics.

## 22.5 Posição Estrutural
Evidências candidatas:
- market share funcional;
- utilização relativa;
- centralidade;
- integrações relevantes;
- dependência do ecossistema;
- posição na cadeia de valor;
- diferenciação demonstrável.

Market cap não prova posição estrutural.
Liquidez de trading pertence à Capacidade de Captura.

## 22.6 Provenance / Evidence ID
Hipótese de registro:
- Evidence ID;
- Asset;
- Vector;
- Construct supported;
- Observation;
- Evidence type;
- Direction;
- Source;
- Observed at;
- Known at score time;
- Freshness;
- Independence/related evidence;
- Confidence contribution.

Uma mesma evidência pode informar mais de um constructo, mas não deve ser contada duas vezes como informação independente.

## 22.7 Trajectory
Pode reutilizar evolução temporal das mesmas evidências.
Não precisa de conjunto totalmente novo de indicadores.

## 22.8 Radar de Ativos Promissores
Exemplo:
- Exposição Causal boa;
- Captura Econômica ainda não materializada;
- Posição Estrutural indeterminada;
- Trajectory fortalecendo;
- Confidence média;
→ Radar, com gap explícito para admissão.

---

# 23. Arquitetura corrente da Suite

```text
                 ┌───────────────┐
                 │     MACRO     │
                 │ Regime/Contexto│
                 └───────┬───────┘
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
┌────────────────────────┐   ┌──────────────────────┐
│   INSTITUTIONAL FLOW   │   │ RADAR DE NARRATIVAS │
│ Atividade institucional│   │ Narrative Opportunity│
└────────────┬───────────┘   └──────────┬───────────┘
             │                          │
             └──────────┬───────────────┘
                        ▼
             ┌──────────────────────┐
             │   CAPITAL ROTATION   │
             │ Vetores de Fluxo     │
             │ relevância/rotação   │
             │ propagação           │
             └──────────┬───────────┘
                        │
          ┌─────────────┼──────────────────┐
          │             │                  │
          ▼             ▼                  ▼
     ┌────────┐    ┌───────────┐    ┌─────────────────┐
     │  BTC   │    │    ETH    │    │    ALTCOINS     │
     │ estrut.│    │ híbrido   │    │ vetores/Ranking │
     └───┬────┘    └─────┬─────┘    └────────┬────────┘
         │               │                   │
         ▼               ▼                   ▼
     BTC PRO          ETH PRO       RANKING INSTITUCIONAL
                                             │
                                   ┌─────────┴─────────┐
                                   │                   │
                                   ▼                   ▼
                         Radar de Ativos          Asset PRO
                           Promissores*       (após seleção)
```

`*` camada auxiliar/observacional, não etapa obrigatória nem “segunda divisão” automática.

---

# 24. Constructos correntes do Ranking

## Relação Ativo–Vetor
- Exposição Causal
- Captura Econômica pelo Ativo
- Posição Estrutural no Vetor

## Capacidade de Captura
- Acessibilidade Institucional
- Capacidade de Absorção

## Trajectory
- evolução das evidências relevantes

## Frictions
- condições não já representadas que podem limitar/impedir captura ou sustentabilidade

## Confidence
- robustez epistemológica da conclusão

## Driver
- explicação principal da posição; não é dimensão de score

---

# 25. Exclusões correntes do núcleo

Não tratar como dimensão nuclear autônoma, salvo decisão posterior:
- Project Quality genérico;
- full Tokenomics;
- full Technical Analysis;
- price momentum;
- Institutional Flow agregado dentro do Ranking;
- Narrative Strength recalculada pelo Ranking;
- Portfolio Construction;
- Catalyst Score;
- Risk genérico;
- Asymmetry como dimensão presumida;
- market cap como prova de posição estrutural;
- hype/social attention como prova causal.

---

# 26. Questões ainda abertas

Ainda **não definidos**:
1. indicadores finais por constructo;
2. quais indicadores são universais versus específicos por ativo/vetor;
3. thresholds;
4. pesos;
5. normalização;
6. fórmula;
7. gates quantitativos;
8. regra final de eligibility;
9. consolidação de múltiplas exposições do mesmo ativo sem double counting;
10. tratamento quantitativo de Trajectory;
11. tratamento de Frictions: penalty / flag / gate / camada paralela;
12. cálculo de Confidence;
13. lifecycle Ranking ↔ Radar de Ativos Promissores;
14. tratamento formal definitivo de ETH;
15. schema técnico de Flow Vector;
16. metodologia formal do Capital Rotation para priorização de Vetores;
17. revisão futura da metodologia histórica do Radar de Narrativas;
18. papel final do Radar de Ativos Promissores na saída;
19. integração final com Asset PRO;
20. validação empírica.

---

# 27. Próximo passo exato

A conversa foi interrompida **antes da Etapa 19**.

## **Etapa 19 — Catálogo de indicadores candidatos e teste de universalidade**

Objetivo:
para cada indicador potencial, classificar se é:
- **universal**;
- **dependente do tipo de ativo**;
- **dependente do Vetor**;
- **inaplicável em determinados modelos econômicos**.

Motivação:
evitar metodologia que favoreça DeFi, L1s ou qualquer categoria apenas porque possui dados on-chain mais fáceis de medir.

**Não criar pesos ou fórmula nesta etapa.**

---

# 28. Pontos de controle antes de prosseguir

Na nova conversa, confirmar:
1. este documento foi lido integralmente;
2. primeiro arquivo enviado por engano continua ignorado;
3. segundo arquivo continua apenas exploratório;
4. Microcaps não será generalizada;
5. BTC permanece fora do Ranking narrativo/seletivo;
6. ETH permanece híbrido: estrutura + vetores;
7. Institutional Flow permanece upstream de Capital Rotation;
8. Capital Rotation é proprietário dos Vetores e de sua relevância relativa;
9. Ranking classifica ativos, não Vetores;
10. Radar de Narrativas ≠ Radar de Ativos Promissores ≠ Watchlist;
11. próxima etapa é a Etapa 19;
12. nenhum score/peso/fórmula deve ser antecipado.

---

# 29. Prompt de abertura consolidado — modo continuidade

Este checkpoint **não cria um segundo protocolo de abertura**. O processo canônico continua sendo o definido em:

`archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md`

O arquivo de handoff funciona como **checkpoint operacional adicional** para evitar repetir toda a reconstrução já validada e para preservar o ponto exato de retomada.

Na próxima conversa, usar o seguinte prompt:

> **Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em MODO CONTINUIDADE para iniciar esta conversa, dedicada ao `Ranking Institucional Simplificado — Metodologia Geral`.**
>
> **Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30.md`.**
>
> O handoff deve ser tratado como **estado de trabalho validado da conversa anterior**, mas não substitui a documentação persistida nem a reconstrução histórica como fonte de verdade.
>
> Antes de prosseguir:
>
> 1. aplique as regras de continuidade e o Freshness Gate do template canônico;
> 2. valide no repositório `rogerio-raposo/CRYPTO-PRO-SUITE`, branch `main`, se houve alteração documental, novo RH/SRC/RPD, divergência resolvida ou nova decisão que afete o domínio desde o checkpoint registrado no handoff;
> 3. não refaça automaticamente etapas já validadas no handoff, salvo quando nova evidência, conflito documental ou mudança de autoridade exigir reabertura;
> 4. não use memória do ChatGPT como evidência, não preencha lacunas por inferência, não generalize a metodologia Microcaps e preserve a distinção entre decisão vigente, histórica, superada, rejeitada, adiada, proposta e indeterminada;
> 5. apresente primeiro um **Diagnóstico de Continuidade**, contendo:
>    - **A. Base do handoff confirmada**;
>    - **B. Alterações ou evidências posteriores ao checkpoint**;
>    - **C. Divergências, impactos e pendências**;
>    - **D. Ponto exato de retomada**;
> 6. não inicie automaticamente nova elaboração normativa ou metodológica antes da revisão desse diagnóstico;
> 7. se não houver alteração material, confirme expressamente que o handoff permanece válido e retome do ponto indicado nele.
>
> **Ponto de retomada esperado neste checkpoint:** Etapa 19 — Catálogo de indicadores candidatos e teste de universalidade.

## 29.1 Regra do processo único

O processo de abertura passa a ter **uma única lógica**, com dois estados operacionais:

- **Sem handoff válido:** aplicar o `CPS_Template_Abertura_Conversa_Modulo.md` integralmente e produzir o Diagnóstico de Partida.
- **Com handoff válido:** aplicar o mesmo template em **Modo Continuidade**, recuperando o handoff mais recente diretamente do repositório e realizando apenas a validação incremental necessária para produzir o Diagnóstico de Continuidade.

Portanto, o handoff **não substitui** o template e o template **não ignora** o handoff.

A hierarquia de uso é:

`Template canônico de abertura → documentação/reconstrução histórica → handoff mais recente → diagnóstico → retomada controlada`
---

# 30. Política recomendada de continuidade

Atualizar este checkpoint:
- no fechamento de cada bloco metodológico;
- antes de trocar de conversa;
- quando houver mudança arquitetural relevante;
- antes de formalizar documento normativo;
- quando o chat se aproximar do limite.

Estrutura sugerida no GitHub:

```text
archive/
  handoffs/
    ranking/
      CPS_Ranking_Handoff_2026-09-30.md
      CPS_Ranking_Handoff_YYYY-MM-DD.md
```

Cada novo handoff deve:
- incorporar o anterior;
- registrar decisões novas;
- marcar regras superadas;
- atualizar “Próximo passo”;
- manter provenance das decisões.

Assim, a continuidade deixa de depender do contexto residual do ChatGPT.

---

# 31. Status final deste checkpoint

**Arquitetura causal:** suficientemente madura para prosseguir.  
**Constructos:** definidos em nível conceitual.  
**Evidência:** arquitetura inicial definida.  
**Operacionalização quantitativa:** ainda não iniciada.  
**Próximo passo:** Etapa 19.  
**Documento:** continuidade de trabalho, não norma final.