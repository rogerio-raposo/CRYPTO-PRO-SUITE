# CRYPTO PRO SUITE
## Ranking Institucional Simplificado — Registro de Continuidade Metodológica

**Data do checkpoint:** 30/09/2026  
**Checkpoint:** CP09  
**Checkpoint anterior:** archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-10-01_CP08.md  
**Status:** documento de continuidade de conversa; **não é documento normativo final**  
**Finalidade:** permitir a retomada do desenvolvimento em nova conversa sem depender da memória do modelo e sem regressão metodológica.

---

# 0. Como usar este documento

Este arquivo é o **handoff de continuidade** da conversa em que a metodologia geral do Ranking Institucional Simplificado está sendo reconstruída/desenvolvida.

Ao abrir uma nova conversa:

1. utilizar o template canônico armazenado em `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` em **Modo Continuidade**;
2. recuperar este handoff diretamente do repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP06.md`;
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

## 2.1 Fonte explicitamente excluída — roadmap-do-crypto-pro.md — IGNORAR NESTA ETAPA
O usuário determinou explicitamente que o arquivo **roadmap-do-crypto-pro.md**, enviado por engano nesta conversa, deve ser ignorado como nova fonte de análise, porque já havia sido analisado em fases anteriores e sua reutilização poderia causar regressão metodológica.

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

Este trecho pertence ao checkpoint anterior e é **superado pela atualização CP02 das seções 32–36**.

## **Ponto vigente: ver Seção 34 — Etapa 22**

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
> **Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP02.md`.**
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
> **Ponto de retomada esperado neste checkpoint:** Etapa 22 — Modelo de avaliação dos constructos e comparabilidade semântica.

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
**Aplicabilidade e roteamento de indicadores:** Etapas 19–21 concluídas em nível metodológico de trabalho.  
**Operacionalização quantitativa:** ainda não iniciada.  
**Próximo passo:** Etapa 22.  
**Documento:** continuidade de trabalho, não norma final.
---

# 32. CHECKPOINT CP02 — Atualização após as Etapas 19–21

Esta seção prevalece sobre as seções 26–31 deste arquivo sempre que houver diferença de estado, próximo passo ou prompt de retomada.

## 32.1 Etapa 19 — Indicadores e universalidade

Decisões de trabalho:
- os constructos podem ser universais sem que seus indicadores também sejam;
- não haverá bateria única de métricas econômicas brutas obrigatória para todos os criptoativos;
- aplicabilidade passa a usar tags U (Universal), T (Type-dependent), V (Vector-dependent) e C (Conditional);
- comparabilidade deve ocorrer no nível do constructo, não pela comparação direta de métricas brutas heterogêneas;
- a regra conceitual é: normalizar significado antes de normalizar número;
- Trajectory reutiliza a evolução temporal das evidências existentes;
- Confidence permanece epistemológico e deriva de qualidade, cobertura, atualidade, consistência, independência, verificabilidade e suficiência da evidência.

Estados inicialmente distinguidos:
- 0 = aplicável e valor efetivamente zero;
- N/A = estruturalmente não aplicável;
- Missing = aplicável, mas evidência indisponível ou insuficiente.

Regras:
- N/A não penaliza;
- Missing não é convertido automaticamente em zero;
- ausência de um mecanismo específico não é penalidade;
- ausência de qualquer mecanismo economicamente relevante de captura pode ser evidência adversa.

## 32.2 Etapa 20 — Economic Mechanism Profile (EMP)

Foi introduzido o Economic Mechanism Profile (EMP) como camada descritiva, multirrótulo, point-in-time e não pontuável.

Função:
> determinar quais evidências e indicadores são economicamente aplicáveis a cada Ativo × Vetor, sem classificar o ativo por uma taxonomia rígida de categorias nominais.

Três blocos:
1. Project Economic Function — o que o projeto economicamente faz;
2. Token Economic Transmission — como a atividade chega ao token/criptoativo;
3. Vector Exposure Channel — como o Vetor de Fluxo alcança projeto/ativo.

Arquétipos funcionais candidatos incluem Execution/Settlement, Intermediation, Infrastructure/Middleware, Asset Issuance/Tokenization, Resource Coordination e Application/Service.

Mecanismos de transmissão candidatos incluem gas/transaction demand, staking/security, collateral, liquidity provisioning, fee payment, revenue/value distribution, burn/supply sink, functional lock e governance-only/weak utility.

Canais de exposição candidatos incluem direct allocation, usage transmission, infrastructure dependency, liquidity transmission, collateral transmission, revenue transmission e ecosystem transmission.

Cadeia causal mínima:
> Vetor → função econômica do projeto → mecanismo de transmissão → ativo.

Regras do EMP:
- EMP seleciona indicadores; não gera score;
- múltiplos mecanismos podem coexistir;
- quantidade de mecanismos não gera mérito;
- mecanismos precisam de evidência verificável;
- status: active / inactive / planned / indeterminate;
- planned não habilita Ranking corrente, mas pode ser relevante para o Radar de Ativos Promissores;
- N/A decorre da ausência estrutural do mecanismo; Missing decorre da falta de dados em mecanismo aplicável.

## 32.3 Etapa 21 — Mechanism → Indicator

Regra de ativação:
> um indicador é aplicável somente quando existe uma proposição causal explícita que o conecta a um mecanismo ativo do EMP e ao constructo que pretende medir.

Estados operacionais consolidados:
- Observed = aplicável e observado;
- 0 = aplicável e valor zero;
- Missing = aplicável, mas evidência indisponível/insuficiente;
- N/A = mecanismo estruturalmente inexistente;
- Excluded = aplicável, mas removido por regra metodológica, especialmente redundância.

Regras adicionais:
- existência formal de mecanismo não implica materialidade;
- Exposição Causal exige vector specificity, economic linkage e causal relevance;
- Captura Econômica exige ponte demonstrável entre atividade econômica e consequência econômica para o próprio ativo;
- protocol revenue não prova automaticamente captura pelo token;
- Posição Estrutural exige Reference Class, denominador economicamente coerente e peer comparability;
- Reference Class deve ser definida por função econômica relevante ao vetor, não por rótulo tecnológico rígido;
- redundância informacional deve ser classificada como Independent / Complementary / Redundant;
- Evidence ID único pode suportar múltiplas proposições, mas não deve gerar multiplicação artificial da mesma evidência;
- maior número de indicadores disponíveis não aumenta score por si só;
- Missing afeta prioritariamente Confidence, não mérito econômico automaticamente;
- suficiência evidencial é cobertura das proposições essenciais do constructo, não quantidade absoluta de métricas.

## 32.4 Indicator Specification Card — campos candidatos

- Indicator ID
- Name
- Construct
- Economic proposition
- Required EMP mechanism(s)
- Vector dependence
- Asset-model dependence
- Unit
- Direction
- Reference class
- Preferred source
- Fallback source
- Freshness requirement
- Applicability rule
- N/A rule
- Missing rule
- Redundancy group
- Known limitations

Meta operacional:
> dado Asset + Vector + Horizon + EMP, o sistema deve conseguir determinar de forma reproduzível indicadores Observed / 0 / Missing / N/A / Excluded.

---

# 33. Questões abertas após CP02

Permanecem abertas:
1. indicadores finais e suas Indicator Specification Cards;
2. modelo de avaliação de cada constructo;
3. método de comparabilidade semântica entre mecanismos econômicos distintos;
4. regras formais de construção da Reference Class;
5. tratamento ordinal/quantitativo de evidências heterogêneas;
6. thresholds;
7. pesos entre constructos;
8. normalização;
9. fórmula final;
10. gates quantitativos e regra final de eligibility;
11. consolidação de múltiplas exposições sem double counting;
12. tratamento quantitativo de Trajectory;
13. tratamento de Frictions;
14. cálculo formal de Confidence;
15. lifecycle Ranking ↔ Radar de Ativos Promissores;
16. tratamento formal definitivo de ETH;
17. schema técnico de Flow Vector;
18. metodologia formal do Capital Rotation para priorização de Vetores;
19. papel final do Radar de Ativos Promissores;
20. integração final com Asset PRO;
21. validação empírica.

---

# 34. Próximo passo exato após CP02

Bloco Etapas 19–21 encerrado em nível metodológico de trabalho.

## Etapa 22 — Modelo de avaliação dos constructos e comparabilidade semântica

Objetivo:
> definir como transformar evidências heterogêneas em uma avaliação comum de cada constructo sem fingir que métricas economicamente diferentes são diretamente comparáveis.

Alternativas a testar:
- avaliação ordinal;
- scoring baseado em rubricas;
- normalização quantitativa contextual;
- modelo híbrido.

Regra:
> ainda não definir pesos entre constructos nem fórmula final.

---

# 35. Prompt de retomada — CP02 — SUPERADO PELO CP03

> Consulte no repositório do CRYPTO PRO SUITE o arquivo archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md e utilize-o em MODO CONTINUIDADE para iniciar esta conversa, dedicada ao Ranking Institucional Simplificado — Metodologia Geral. Considere também o checkpoint/handoff armazenado no repositório em archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP02.md.

Após o Diagnóstico de Continuidade, o ponto esperado de retomada é a Etapa 22.

---

# 36. Status do CP02 — SUPERADO PELO CP03

- Arquitetura causal: suficientemente madura para prosseguir.
- Constructos: definidos em nível conceitual.
- Evidência: arquitetura inicial definida.
- Aplicabilidade de indicadores: bloco Etapas 19–21 fechado em nível metodológico de trabalho.
- EMP: definido como camada descritiva, point-in-time e não pontuável.
- Operacionalização quantitativa: ainda não iniciada.
- Pesos e fórmula: permanecem abertos.
- Próximo passo: Etapa 22.
- Documento: handoff operacional; não normativo.

---

# 37. CHECKPOINT CP03 — Fechamento da arquitetura lógica pré-quantitativa

Esta seção e as seções 38–41 constituem o estado operacional vigente deste handoff e prevalecem sobre trechos anteriores quando houver diferença de estado, próximo passo ou prompt de retomada.

Cobertura deste checkpoint:
- Etapa 22 — Modelo de avaliação dos constructos e comparabilidade semântica;
- Etapa 23 — Anchors, decision rules e consistência interavaliador;
- Etapa 24 — Lógica de composição da Relação Ativo–Vetor;
- Etapa 25 — Materiality Gate e estados de admissão;
- Etapa 26 — Decomposição e operacionalização da Capacidade de Captura Institucional;
- Etapa 27 — Taxonomia e lógica das Frictions;
- Etapa 28 — Formalização de Confidence;
- Etapa 29 — Integração lógica do Ranking antes de pesos e fórmula.

## 37.1 Etapa 22 — Modelo híbrido de avaliação

Decisão de trabalho:
> utilizar evidência quantitativa/contextual dentro de contextos semanticamente comparáveis, seguida de rubricas semanticamente ancoradas por constructo; normalização estatística não substitui interpretação econômica.

Saída ordinal provisória comum aos constructos positivos:
- E0 — Não sustentada / marginal conforme o constructo;
- E1 — Fraca / periférica;
- E2 — Moderada / economicamente relevante;
- E3 — Forte / material;
- E4 — Muito forte / estrutural;
- IND — Indeterminada.

Regras:
- E0 não significa ausência de dados;
- IND não significa fraqueza;
- métricas quantitativas só podem ser normalizadas dentro de famílias semanticamente equivalentes ou suficientemente comparáveis;
- evidência absoluta e evidência relativa têm funções distintas;
- cada classificação deve manter Evidence IDs, rationale e evidência contraditória;
- Construct State e Confidence permanecem separados;
- score cardinal ainda não é obrigatório nem definido.

## 37.2 Etapa 23 — Anchors e decision rules

Princípio:
> atribuir o nível mais alto suficientemente sustentado pela evidência disponível e não contradito por evidência material mais forte.

Regras consolidadas:
- cada nível E0–E4 exige anchors semanticamente explícitos por constructo;
- ausência de evidência suficiente para o nível superior mantém o nível inferior comprovado;
- blockers impedem determinado nível quando contradizem condição necessária;
- modifiers alteram interpretação sem necessariamente invalidar o nível;
- proxies podem complementar, mas não devem sozinhos sustentar E3/E4 dos constructos nucleares;
- thresholds quantitativos, quando usados, devem ser contextuais à Reference Class e semanticamente coerentes;
- todo IND exige Indeterminacy Reason;
- divergência interavaliador não é resolvida por média;
- Trajectory não eleva silenciosamente o Construct State;
- Confidence alta não compensa constructo baixo.

Objetivo de consistência futura:
> avaliações independentes, com o mesmo Evidence Set e a mesma rubrica, devem convergir ao mesmo nível ou predominantemente a níveis adjacentes; validação empírica fica para pilotos.

## 37.3 Etapa 24 — Composição da Relação Ativo–Vetor

Modelos rejeitados nesta fase:
- aditivo puro;
- multiplicativo sobre E0–E4;
- mínimo puro como resultado final;
- lexicografia rígida.

Arquitetura corrente:
- Exposição Causal + Captura Econômica formam a camada de validade econômica da relação;
- Posição Estrutural atua principalmente como discriminador relativo depois que a relação é economicamente sustentada;
- Exposição e Captura são não compensáveis entre si;
- Posição não pode compensar deficiência material de Exposição ou Captura;
- os três estados devem permanecer visíveis no Perfil da Relação Ativo–Vetor;
- Pareto dominance pode comparar perfis quando um ativo é igual ou superior em todos os componentes e superior em pelo menos um;
- casos com trade-off permanecem não resolvidos até regra metodológica posterior.

## 37.4 Etapa 25 — Materiality Gate e admissão

Separação obrigatória:
> Eligibility ≠ Materiality ≠ Ranking Readiness.

Unidade:
> Ativo × Vetor × Horizonte × As-of.

Materiality Gate provisório:
- PASS quando Exposição Causal >= E2 e Captura Econômica >= E2, com evidência suficiente para sustentar os estados;
- FAIL quando pelo menos um dos dois está em E0/E1 com evidência robusta suficiente;
- INDETERMINATE quando Exposição ou Captura está em IND ou a confirmação epistemológica é insuficiente.

O limiar E2 é semântico, não matemático: é o primeiro estado definido como economicamente relevante.

Regras adicionais:
- Posição Estrutural não participa do Materiality Gate;
- Posição precisa ser avaliável para comparação plena no Ranking;
- Confidence pode impedir promoção para status Confirmed, mas não altera mérito;
- Capacity e Frictions ficam fora do Materiality Gate;
- Radar de Ativos Promissores é flag auxiliar, não destino automático de não admitidos;
- todo item no Radar deve registrar blocker/lacuna e condição de promoção;
- não admissão deve possuir reason code explícito.

## 37.5 Etapa 26 — Capacidade de Captura Institucional

A decomposição original foi mantida com dois subconstructos:
1. Institutional Accessibility;
2. Absorption Capacity.

Definições de trabalho:
> Accessibility = grau em que a população institucional relevante dispõe de canais utilizáveis para adquirir, custodiar, movimentar, administrar e liquidar exposição ao ativo.

> Absorption = grau em que os mercados institucionalmente acessíveis conseguem acomodar entrada, manutenção, rebalanceamento e saída de capital em magnitude relevante, preservando condições de execução compatíveis.

Novos parâmetros contextuais:
- Institutional Access Context — define a população e os canais institucionais relevantes;
- Reference Allocation Scale (RAS) — define a ordem de grandeza de capital em relação à qual Absorption é avaliada.

Regras:
- liquidez deve ser medida nos canais institucionalmente acessíveis;
- market cap não prova Absorption;
- volume bruto não equivale a executable liquidity;
- derivativos são condicionais e não requisito universal;
- wrappers/produtos podem elevar Accessibility sem garantir Absorption;
- persistence/resilience permanece dentro de Absorption;
- impossibilidade atual de acesso pertence a Accessibility; risco prospectivo pertence a Frictions;
- nenhum terceiro subconstructo foi justificado;
- Accessibility e Absorption podem usar E0–E4 + IND com rubricas próprias;
- Capacity é point-in-time.

## 37.6 Etapa 27 — Frictions

Definição consolidada:
> Friction é condição observável, material e não já representada por outro constructo, capaz de restringir, desincentivar, atrasar, deteriorar ou inviabilizar a captura ou sua sustentabilidade no horizonte.

Famílias provisórias:
- Regulatory / Legal;
- Supply / Dilution;
- Concentration / Control;
- Protocol / Security;
- Governance / Dependency;
- Market-Structure / Counterparty.

Regras:
- toda condição adversa possui um constructo proprietário primário;
- Friction não replica ausência de mérito de outro constructo;
- estado operacional atual pertence prioritariamente a Capacity; vulnerabilidade adicional/prospectiva pode pertencer a Frictions;
- Frictions precisam ser materiais e relevantes ao horizonte;
- comportamento possível: Flag / Modifier / Blocker;
- não existe penalidade aritmética universal definida;
- Frictions são point-in-time e possuem lifecycle;
- causa única não deve produzir penalização múltipla por consequências correlacionadas;
- Friction pode ser Asset-level ou Asset × Vector;
- escala provisória F0–F4 + IND não é score;
- blockers exigem regra objetiva e evidência forte.

Foi proposta a ideia de Friction Event Registry para preservar causalidade, provenance, status, horizonte, efeitos e resolução.

## 37.7 Etapa 28 — Confidence

Definição:
> Confidence é avaliação ordinal da robustez epistemológica de uma conclusão; não mede mérito econômico nem probabilidade estatística de acerto.

Dimensões epistemológicas:
- Source Quality;
- Evidence Directness;
- Coverage / Sufficiency;
- Freshness / Temporal Fit;
- Independence;
- Consistency.

Escala provisória:
- C0 — Insuficiente;
- C1 — Baixa;
- C2 — Moderada;
- C3 — Alta;
- C4 — Muito alta.

Regras:
- Confidence é avaliada por constructo;
- não compensa constructo fraco;
- não substitui evidência ausente;
- não deve ser média simples das dimensões epistemológicas;
- blockers epistemológicos podem limitar o nível;
- quantidade de fontes não equivale a independência nem a robustez;
- conflitos materiais devem ser registrados e reduzem Confidence até resolução;
- status Confirmed depende de Confidence suficiente, threshold ainda a calibrar;
- Confidence agregada do Ranking permanece indefinida;
- Coverage Map pode explicitar proposições cobertas, parciais e ausentes.

## 37.8 Etapa 29 — Integração lógica pré-quantitativa

Princípio:
> gates devem operar antes de qualquer agregação.

Sequência lógica corrente:
1. Eligibility;
2. Relação Ativo–Vetor;
3. Materiality Gate;
4. Posição Estrutural;
5. Capacity — Accessibility + Absorption;
6. Frictions — Flag / Modifier / Blocker;
7. Confirmation Gate;
8. Comparative Classification;
9. agregação futura apenas se necessária.

Perfil positivo conceitual:
> [Exposure, Economic Capture, Structural Position, Accessibility, Absorption]

Regras:
- Exposição e Captura continuam discriminando depois de passar o Materiality Gate;
- Posição é discriminador, não condição de existência da relação;
- Capacity provavelmente terá fronteira mínima de viabilidade, ainda não calibrada;
- Accessibility e Absorption são não compensáveis em extremos;
- Frictions permanecem condicionais;
- Confidence qualifica a robustez da comparação, não entra como mérito;
- candidatos Ranking-Ready podem ser comparados inicialmente por Pareto dominance;
- Positive Dominance deve ser distinguida de Qualified Dominance, que também considera blockers, Frictions materialmente relevantes e confirmação;
- Pareto produz ordem parcial, não necessariamente ranking total;
- pesos ou outro método multicritério só se tornam necessários quando persistem trade-offs entre candidatos Ranking-Ready e a saída exige ordenação adicional;
- a necessidade real de pesos deve ser determinada empiricamente;
- score 0–100 histórico não obriga a arquitetura atual;
- Trajectory permanece qualificador temporal;
- Driver permanece explicativo;
- tratamento de múltiplos Vetores por ativo continua aberto.

---

# 38. Arquitetura lógica vigente no CP03

```text
UPSTREAM
Macro / Institutional Flow / Narrative Opportunity / Capital Rotation
                           │
                           ▼
                     FLOW VECTOR
                           │
                           ▼
                Candidate Universe
                           │
                           ▼
                     Eligibility
                           │
                           ▼
             RELAÇÃO ATIVO–VETOR
          Exposure + Capture + Position
                    │
                    ▼
              Materiality Gate
                    │
                    ▼
       CAPACIDADE INSTITUCIONAL
       Accessibility + Absorption
                    │
                    ▼
                 Frictions
          Flag / Modifier / Blocker
                    │
                    ▼
             Confirmation Gate
                    │
                    ▼
               Ranking-Ready
                    │
                    ▼
          Pareto / comparative logic
                    │
             ┌──────┴──────┐
             │             │
         Dominated    Non-dominated
                           │
                           ▼
               future aggregation
                only if necessary
```

Trajectory e Confidence permanecem transversais. Driver permanece explicativo.

---

# 39. Questões abertas após CP03

Permanecem abertas:
1. tratamento formal de múltiplos Vetores por ativo e consolidação para saída asset-level;
2. prevenção de double counting entre Vetores relacionados/redundantes;
3. regra para Vetores favoráveis e adversos coexistentes;
4. eventual priorização relativa dos Vetores recebida do Capital Rotation e como ela entra no Ranking sem ser recalculada;
5. frontier/ordem parcial quando um ativo possui múltiplos perfis Ativo–Vetor;
6. método multicritério para trade-offs residuais entre candidatos Ranking-Ready;
7. necessidade efetiva de pesos e, se necessária, metodologia para obtê-los;
8. thresholds definitivos de Capacity viability;
9. threshold de Confidence para status Confirmed;
10. regra final de Eligibility geral;
11. tratamento quantitativo/operacional definitivo de Trajectory;
12. comportamento formal de Frictions como Flag / Modifier / Blocker;
13. critérios objetivos de blocker;
14. Confidence agregada da classificação final;
15. Indicator Specification Cards finais;
16. schema técnico definitivo do Evidence Registry, Coverage Map e Friction Event Registry;
17. lifecycle formal Ranking ↔ Radar de Ativos Promissores;
18. tratamento formal definitivo de ETH;
19. schema técnico de Flow Vector;
20. metodologia formal do Capital Rotation para priorização de Vetores;
21. revisão futura da metodologia histórica do Radar de Narrativas;
22. integração final com Asset PRO;
23. desenho dos pilotos e validação empírica;
24. decisão sobre eventual score cardinal e compatibilidade com antecedente histórico 0–100;
25. MEL permanece backlog interno e não módulo independente.

---

# 40. Próximo passo exato após CP03

A arquitetura lógica pré-quantitativa foi fechada em nível metodológico de trabalho até a Etapa 29.

## Etapa 30 — Múltiplos Vetores por ativo e consolidação asset-level

Objetivo:
> definir como transformar múltiplas avaliações Ativo × Vetor × Horizonte em uma saída por ativo sem premiar mecanicamente a quantidade de Vetores, sem recalcular a relevância upstream dos Vetores e sem double counting entre Vetores relacionados.

Questões mínimas a resolver:
- um ativo exposto a vários Vetores deve ser avaliado por melhor Vetor, conjunto de Vetores ou perfil multicamada?
- como incorporar relevância relativa do Vetor produzida pelo Capital Rotation sem o Ranking voltar a classificar Vetores?
- como tratar Vetores correlacionados/redundantes;
- como preservar Vetores favoráveis e adversos;
- como evitar que amplitude de exposição gere vantagem automática;
- como produzir saída final por ativo mantendo provenance das relações Ativo–Vetor.

Regra:
> ainda não definir pesos gerais entre constructos nem fórmula final do Ranking.

Após resolver múltiplos Vetores, o bloco seguinte deverá testar o mecanismo multicritério necessário para os trade-offs remanescentes entre candidatos Ranking-Ready.

---

# 41. Prompt de retomada — CP03 — SUPERADO PELO CP04

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **MODO CONTINUIDADE** para iniciar esta conversa, dedicada ao `Ranking Institucional Simplificado — Metodologia Geral`. Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP03.md`.

> Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome da **Etapa 30 — Múltiplos Vetores por ativo e consolidação asset-level**.

---

# 42. Status do CP03 — SUPERADO PELO CP04

- Fenômeno-alvo: preservado — captura de fluxo institucional relevante no horizonte.
- Relação Ativo–Vetor: arquitetura conceitual e lógica de materialidade definidas em nível de trabalho.
- EMP e aplicabilidade de indicadores: definidos em nível de trabalho.
- Avaliação dos constructos: modelo híbrido E0–E4 + IND definido em nível de trabalho.
- Materiality Gate: threshold semântico provisório E2/E2 definido.
- Capacity: Accessibility + Absorption mantidas como dois subconstructos.
- Frictions: taxonomia e lógica condicional definidas em nível de trabalho.
- Confidence: arquitetura epistemológica C0–C4 definida em nível de trabalho.
- Integração pré-quantitativa: fechada até gates + Pareto/ordem parcial.
- Pesos: não definidos.
- Fórmula final: não definida.
- Score cardinal: não obrigatório e não definido.
- Múltiplos Vetores: próximo problema metodológico.
- Documento: handoff operacional; não normativo.

---

# 43. CHECKPOINT CP04 — Fechamento do núcleo comparativo ordinal

Esta seção e as seções 44–47 constituem o estado operacional vigente deste handoff e prevalecem sobre trechos anteriores quando houver diferença de estado, próximo passo ou prompt de retomada.

Cobertura deste checkpoint:
- Etapa 30 — Múltiplos Vetores por ativo e consolidação asset-level;
- Etapa 31 — Método multicritério para trade-offs residuais;
- Etapa 32 — Comparative Decision Protocol;
- Etapa 33 — Calibração semântica das diferenças e regras de veto;
- Etapa 34 — Concordance Rules e formação da relação de preferência.

## 43.1 Etapa 30 — Múltiplos Vetores e consolidação asset-level

Decisões de trabalho:
- múltiplos Vetores não são somados nem promediados automaticamente;
- quantidade de Vetores não gera mérito;
- Vector Relevance permanece propriedade upstream do Capital Rotation;
- o Ranking não recalcula Vector Relevance nem cria Vector Score concorrente;
- Vector Relevance não vira multiplicador automático;
- distinguir redundância entre Vetores da redundância da via de captura do ativo;
- Capture Pathway deriva da cadeia econômica já descrita pelo EMP;
- múltiplos Vetores podem compartilhar total ou parcialmente uma Capture Pathway;
- evidência compartilhada permanece um único Evidence ID;
- cada relação Ativo–Vetor recebe orientação Favorable / Adverse / Mixed / IND;
- Vetor adverso não é Friction;
- não realizar netting precoce entre Vetores favoráveis e adversos;
- relações favoráveis não dominadas podem formar uma Primary Vector Frontier;
- Supporting Pathways permanecem visíveis sem bônus automático;
- breadth of exposure é descriptor, não score;
- consolidação ocorre dentro do mesmo horizonte;
- Confidence controla confirmação, não mérito;
- ETH estrutural + Vetores permanece tratamento específico aberto;
- saída asset-level deve preservar provenance Ativo–Vetor.

Saída conceitual:
> Asset × Vector profiles → redundancy/pathway control → favorable/adverse frontiers → Primary/Supporting Pathways → Asset-Level Consolidated Profile.

## 43.2 Etapa 31 — Método multicritério residual

Princípio:
> aplicar a agregação mínima necessária; não introduzir compensação mais forte enquanto regras estruturais menos compensatórias forem suficientes.

Arquitetura preferencial:
1. Gates;
2. Pareto dominance;
3. análise por blocos;
4. outranking não compensatório;
5. classes ordenadas, se necessárias;
6. pesos/cardinalização apenas se pilotos demonstrarem necessidade.

Decisões:
- weighted additive scoring rejeitado como método primário;
- modelo multiplicativo rejeitado;
- lexicografia total rejeitada;
- ordem parcial é saída admissível;
- incomparabilidade é informação metodológica legítima;
- Relationship, Structural Position e Capacity são blocos substantivamente distintos;
- Confidence qualifica a robustez da preferência, não entra como mérito;
- Trajectory permanece fora da regra nuclear até validação;
- pesos continuam indefinidos.

## 43.3 Etapa 32 — Comparative Decision Protocol

Fluxo:
> Comparability → Confirmation → Dominance → Block Comparison → Difference Classification → Veto → Concordance → Decision.

Resultados possíveis:
- DOMINATES;
- OUTRANKS;
- EQUIVALENT;
- INCOMPARABLE;
- UNRESOLVED.

Distinções:
- INCOMPARABLE = trade-off econômico genuíno sob evidência suficiente;
- UNRESOLVED = insuficiência epistemológica ou incompatibilidade contextual;
- Confirmed Outranking e Provisional Outranking devem ser distinguíveis;
- Comparative Veto é diferente de blocker de admissão;
- Epistemic Veto bloqueia conclusão, não mérito;
- preference cycles podem existir e não devem ser corrigidos silenciosamente;
- transitividade não é pressuposta.

Comparative Difference:
- Δ0 — Indistinguishable;
- Δ1 — Limited;
- Δ2 — Material;
- Δ3 — Critical.

## 43.4 Etapa 33 — Diferenças e vetos

Princípio:
> Δ é determinado por transições semânticas entre anchors do constructo, não por subtração numérica de E0–E4.

Elementos usados:
- Anchor Transition;
- Economic Consequence;
- Decision Relevance.

Matriz provisória de veto:
- Exposição Causal: pode gerar Δ3 e Comparative Veto nuclear;
- Captura Econômica: pode gerar Δ3 e Comparative Veto nuclear;
- Posição Estrutural: pode gerar Δ3, mas não veto por padrão;
- Accessibility: potencialmente veto-eligible, dependendo do Capacity Gate e Institutional Access Context;
- Absorption: potencialmente veto-eligible, dependendo do Capacity Gate e Reference Allocation Scale;
- Frictions: podem gerar Comparative Veto de forma condicional;
- Confidence: pode gerar Epistemic Veto, nunca veto econômico.

Regras:
- veto é direcional;
- veto não implica preferência automática pelo outro ativo;
- veto não é compensável por vantagens em outros constructos;
- diferenças críticas não ativam veto automaticamente;
- veto exige rationale baseado em anchor e consequência econômica;
- decisão deve preservar Evidence IDs e provenance.

## 43.5 Etapa 34 — Concordance Rules

Princípio:
> concordance não é contagem de critérios nem índice percentual; é suficiência lógica de suporte favorável na ausência de oposição material capaz de invalidar a preferência.

Blocos:
- Relationship = Exposure + Economic Capture;
- Structural Position = Position;
- Capacity = Accessibility + Absorption.

Regra de trabalho para OUTRANKS:
- comparabilidade válida;
- ausência de blocker e Comparative Veto contra a direção proposta;
- pelo menos uma vantagem material confirmada (Δ2 ou Δ3) em um constructo/bloco, ou um Friction Modifier material confirmado que afete adversamente o outro ativo;
- todas as desvantagens remanescentes do ativo preferido devem ser no máximo limitadas (Δ1);
- não pode existir trade-off material confirmado dentro de Relationship ou Capacity que permaneça sem resolução;
- Confidence das evidências decisivas deve ser suficiente para Confirmed Outranking.

Consequências:
- se houver vantagens materiais confirmadas em ambos os sentidos, o resultado é INCOMPARABLE;
- se não houver vantagem material em nenhum sentido e as diferenças forem apenas Δ0/Δ1, o resultado é EQUIVALENT;
- se informação decisiva for insuficiente, o resultado é UNRESOLVED;
- se a direção favorável existe mas a confirmação é insuficiente, pode haver PROVISIONAL OUTRANKING somente quando nenhuma lacuna plausível puder esconder veto/oposição material; caso contrário, UNRESOLVED;
- material opposition não pode ser superada por acumulação de vantagens menores;
- Position pode sustentar outranking quando for materialmente superior e Relationship/Capacity não apresentarem oposição material;
- Relationship ou Capacity materialmente opostos em direções diferentes produzem incomparabilidade, não compensação;
- Friction Flag não altera preferência; Modifier material pode afetar concordance; Blocker retira o ativo antes da comparação; Comparative Veto impede apenas a direção de preferência.

Não há Concordance Index numérico nesta fase.

---

# 44. Arquitetura comparativa vigente no CP04

```text
Candidate pair A × B
        │
        ▼
Comparability Check
        │
        ├── falha ───────────────► UNRESOLVED
        │
        ▼
Confirmation / Epistemic Check
        │
        ▼
Pareto Dominance
        │
        ├── sim ─────────────────► DOMINATES
        │
        ▼
Block Comparison
Relationship / Position / Capacity
        │
        ▼
Comparative Difference
Δ0 / Δ1 / Δ2 / Δ3
        │
        ▼
Veto Check
        │
        ├── blocker ─────────────► fora da comparação
        ├── comparative veto ────► direção vetada
        ├── epistemic veto ──────► UNRESOLVED / PROVISIONAL
        │
        ▼
Concordance
        │
        ├── material support +
        │   opposition <= Δ1 ────► OUTRANKS
        ├── only Δ0/Δ1 ──────────► EQUIVALENT
        ├── material support
        │   both directions ─────► INCOMPARABLE
        └── insufficient evidence► UNRESOLVED
```

Princípio de preservação:
> nenhuma etapa converte E0–E4, Δ0–Δ3, Confidence ou Frictions em soma cardinal neste estágio.

---

# 45. Questões abertas após CP04

Permanecem abertas:
1. transformar o grafo de DOMINATES / OUTRANKS / EQUIVALENT / INCOMPARABLE em classes/saída operacional do Ranking;
2. tratamento de ciclos de preferência e componentes fortemente conectados;
3. regra de construção de Pareto layers e sua relação com classes;
4. decidir se a saída final será ordem parcial, classes ordenadas ou combinação das duas;
5. testar discriminabilidade do motor sem pesos;
6. Capacity viability threshold definitivo;
7. Confidence threshold definitivo para Confirmed;
8. regra final de Eligibility geral;
9. regras detalhadas por constructo para Δ0–Δ3;
10. critérios objetivos definitivos de Comparative Veto;
11. comportamento definitivo de Friction Modifier;
12. Confidence agregada da classificação final;
13. tratamento operacional/quantitativo de Trajectory;
14. Indicator Specification Cards finais;
15. schemas técnicos do Evidence Registry, Coverage Map, Friction Event Registry e Comparative Decision Record;
16. lifecycle formal Ranking ↔ Radar de Ativos Promissores;
17. tratamento definitivo de ETH estrutural + Vetores;
18. schema técnico de Flow Vector e metadados de redundância upstream;
19. metodologia formal do Capital Rotation para priorização de Vetores;
20. revisão futura da metodologia histórica do Radar de Narrativas;
21. integração final com Asset PRO;
22. desenho dos pilotos e validação empírica;
23. decisão sobre eventual score cardinal;
24. se pesos se tornarem necessários, metodologia para obtê-los sem arbitrariedade;
25. MEL permanece backlog interno e não módulo independente.

---

# 46. Próximo passo exato após CP04

## Etapa 35 — Do grafo de preferência às classes do Ranking

Objetivo:
> transformar as relações par a par DOMINATES / OUTRANKS / EQUIVALENT / INCOMPARABLE em uma saída operacional asset-level sem impor transitividade artificial nem criar score cardinal prematuramente.

Questões mínimas:
- como representar o grafo dirigido de preferência;
- como tratar EQUIVALENT;
- como tratar INCOMPARABLE;
- como detectar e preservar preference cycles;
- se e como formar componentes/grupos;
- como derivar Pareto/dominance layers;
- como transformar estrutura parcial em classes ordenadas;
- quando uma classe é estável o suficiente para saída formal;
- como preservar Confidence e provenance da classificação.

Regra:
> ainda não introduzir pesos ou score cardinal antes de testar se classes derivadas do grafo produzem discriminabilidade suficiente.

---

# 47. Prompt de retomada — CP04 — SUPERADO PELO CP05

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **MODO CONTINUIDADE** para iniciar esta conversa, dedicada ao `Ranking Institucional Simplificado — Metodologia Geral`. Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP04.md`.

> Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome da **Etapa 35 — Do grafo de preferência às classes do Ranking**.

---

# 48. Status do CP04 — SUPERADO PELO CP05

- Fenômeno-alvo: preservado — captura de fluxo institucional relevante no horizonte.
- Arquitetura pré-quantitativa: fechada.
- Consolidação multivetorial asset-level: definida em nível de trabalho sem soma de Vetores.
- Método multicritério primário: outranking não compensatório.
- Comparative Decision Protocol: definido em nível conceitual.
- Comparative Difference Δ0–Δ3: definida semanticamente em nível de trabalho.
- Comparative Veto / Epistemic Veto: funções definidas em nível de trabalho.
- Concordance Rules: definidas sem índice numérico.
- Pareto dominance: preservada como etapa anterior ao outranking.
- Ordem parcial e incomparabilidade: aceitas metodologicamente.
- Pesos: não definidos.
- Score cardinal: não definido e não obrigatório.
- Próximo problema: transformar o grafo de preferência em classes/saída operacional.
- Documento: handoff operacional; não normativo.

---

# 49. CHECKPOINT CP05 — Classes do Ranking, dinâmica temporal e mapa conceitual simplificado

Esta seção e as seções 50–54 constituem o estado operacional vigente deste handoff e prevalecem sobre trechos anteriores quando houver diferença de estado, próximo passo ou prompt de retomada.

Cobertura deste checkpoint:
- Etapa 35 — Do grafo de preferência às classes do Ranking;
- Etapa 36 — De Preference Layers a Ranking Classes;
- Etapa 37 — Formalização de Trajectory e dinâmica temporal;
- mapa conceitual simplificado da metodologia, produzido para facilitar a retomada humana sem substituir a especificação detalhada.

## 49.1 Etapa 35 — Grafo de preferência

Representação:
- nós = ativos Ranking-Ready;
- arestas direcionadas confirmadas = DOMINATES ou OUTRANKS;
- EQUIVALENT, INCOMPARABLE e UNRESOLVED permanecem relações explicitamente registradas e não devem ser reduzidas a ausência genérica de aresta.

Regras:
- DOMINATES e OUTRANKS preservam seus tipos;
- EQUIVALENT não é presumido transitivo;
- Equivalence Group só pode ser formado quando houver consistência par a par suficiente;
- preference cycles são permitidos e devem ser preservados;
- Strongly Connected Components (SCCs) identificam ciclos, mas SCC não significa equivalência;
- o condensation graph dos SCCs forma um DAG;
- Preference Layers podem ser obtidas por remoção iterativa dos source components;
- layer expressa profundidade na estrutura de preferência, não superioridade universal sobre todos os ativos de layers inferiores;
- número de vitórias, outdegree, PageRank e centralidade não são métricas de mérito econômico;
- Pareto permanece útil como etapa anterior e invariant check;
- relações UNRESOLVED e PROVISIONAL devem informar a estabilidade da classificação.

## 49.2 Etapa 36 — Ranking Classes

Definição de trabalho:
> Ranking Class é o estrato ordinal ocupado por um ativo ou componente no grafo consolidado de preferência, derivado das relações confirmadas de DOMINATES e OUTRANKS e qualificado pela estabilidade epistemológica dessa posição.

Regra-base:
- Preference Layer 1 → RC-1;
- Preference Layer 2 → RC-2;
- Preference Layer 3 → RC-3;
- e assim sucessivamente.

Regras:
- layers distintas não são fundidas por conveniência;
- uma layer não é subdividida arbitrariamente;
- classes formam ordem parcial estratificada, não ranking linear completo;
- RC-1 significa “não outranked/dominated no grafo confirmado”, não “melhor ativo absoluto”;
- SCCs permanecem indivisíveis na mesma classe e recebem Cycle Flag;
- Equivalence Groups permanecem semanticamente distintos de SCCs;
- conflito entre equivalência confirmada e classes diferentes gera Equivalence–Class Consistency Alert;
- Base Class é calculada apenas com arestas confirmadas;
- relações provisórias e UNRESOLVED entram em análise de sensibilidade;
- Stability Envelope = conjunto de classes plausíveis sob resoluções metodologicamente admissíveis das relações ainda não confirmadas;
- envelope unitário → Confirmed Class;
- envelope múltiplo → Provisional Class;
- INCOMPARABLE não reduz automaticamente estabilidade;
- UNRESOLVED só afeta o status quando sua resolução plausível puder alterar a classe;
- não foi criada nova escala numérica de Class Confidence;
- número de classes é endógeno;
- não existe ordenação interna artificial dentro da mesma classe;
- mudanças de classe são point-in-time e precisam de causal provenance.

Saída resumida conceitual:
```text
RC-1
 ├─ Asset A — Confirmed
 ├─ Asset B — Confirmed / Incomparable with A
 └─ Asset C — Provisional {RC-1, RC-2}

RC-2
 ├─ Asset D — Confirmed / SCC-01
 └─ Asset E — Confirmed / SCC-01
```

## 49.3 Etapa 37 — Trajectory e dinâmica temporal

Princípio:
> Trajectory é camada temporal transversal e não constitui constructo de mérito independente.

Separações:
- Evidence Trajectory = evolução das evidências;
- Construct Trajectory = direção temporal do constructo;
- Classification Movement = mudança efetiva de Ranking Class;
- Economic Change ≠ Epistemic Change ≠ Comparative Change.

Estados:
- Strengthening;
- Stable;
- Deteriorating;
- IND.

Regras:
- Trajectory é avaliada primariamente por constructo;
- Stable não significa ausência de variação, mas ausência de mudança material;
- Trajectory pode mudar sem mudança de E-state;
- mudança de E-state é evidência forte de Trajectory, mas não condição necessária;
- não existe lookback universal;
- Ranking Horizon e Trajectory Lookback são parâmetros distintos;
- lookback depende do indicador/constructo;
- sinais contínuos exigem persistência, salvo eventos estruturais discretos;
- price momentum, RSI, MACD, médias móveis e demais TA permanecem excluídos do Ranking e pertencem ao Asset PRO;
- métricas sensíveis ao preço devem ser tratadas para não importar momentum indiretamente;
- mudança de Confidence é epistemológica, não Trajectory econômica;
- Block Trajectory só deve ser sintetizada quando seus componentes forem coerentes;
- Trajectory não muda Ranking Class diretamente;
- Nearest State Transition pode registrar próximo anchor, evidência faltante e condição de mudança;
- Trajectory pode futuramente apoiar Radar, Watchlist e cadence, mas não é bônus/pontos;
- Class Movement é obtido reconstruindo o grafo em sucessivos as-of.

## 49.4 Mapa conceitual simplificado da metodologia

Finalidade:
> comparar e classificar criptoativos segundo seu posicionamento relativo para potencial captura do próximo fluxo institucional, com metodologia explícita, baseada em evidências e sem interpretar a posição como probabilidade estatística calibrada.

Fluxo simplificado:

```text
Fluxo Institucional / Capital Rotation
                ↓
          Flow Vectors
                ↓
       Candidate Universe
                ↓
      Relação Ativo–Vetor
 Exposure + Economic Capture + Position
                ↓
        Materiality Gate
                ↓
 Institutional Capture Capacity
 Accessibility + Absorption
                ↓
            Frictions
                ↓
           Confidence
                ↓
   Comparative Decision Engine
 Dominance + Outranking + Veto
                ↓
      Preference Graph
                ↓
        Ranking Classes
     RC-1 / RC-2 / RC-3...
```

Quatro perguntas centrais para leitura humana:
1. Por que este ativo deveria capturar este fluxo? — Relação Ativo–Vetor.
2. O próprio token captura economicamente o benefício? — Economic Capture.
3. Capital institucional consegue entrar e sair em escala relevante? — Accessibility + Absorption.
4. Existe condição adversa ou insuficiência de evidência que comprometa a conclusão? — Frictions + Confidence.

Regras de interpretação:
- o Ranking não é previsão de preço;
- não é avaliação genérica de “melhor projeto”;
- não pressupõe score 0–100;
- não premia quantidade de Vetores;
- não força ordem linear quando a evidência sustenta apenas ordem parcial;
- pesos só serão considerados se os pilotos demonstrarem necessidade real;
- Trajectory descreve direção das propriedades, sem acrescentar pontos;
- Asset PRO permanece responsável por timing e análise técnica.

---

# 50. Arquitetura vigente no CP05

```text
UPSTREAM
Macro / Institutional Flow / Narrative Opportunity / Capital Rotation
                           │
                           ▼
                     FLOW VECTOR
                           │
                           ▼
                Candidate Universe
                           │
                           ▼
                     Eligibility
                           │
                           ▼
             RELAÇÃO ATIVO–VETOR
      Exposure + Capture + Structural Position
                    │
                    ▼
              Materiality Gate
                    │
                    ▼
        INSTITUTIONAL CAPACITY
       Accessibility + Absorption
                    │
                    ▼
                 Frictions
                    │
                    ▼
                 Confidence
                    │
                    ▼
         Comparative Decision Protocol
 Dominance → Δ → Veto → Concordance → Outranking
                    │
                    ▼
              Preference Graph
       SCCs / Equivalence / Incomparability
                    │
                    ▼
             Preference Layers
                    │
                    ▼
              Ranking Classes
         Base Class + Stability Envelope
                    │
                    ▼
            Temporal Monitoring
   Construct Trajectory + Class Movement
```

Princípio de preservação:
> nenhuma etapa converte automaticamente E0–E4, Δ0–Δ3, Confidence, Frictions, Trajectory ou Ranking Classes em score cardinal.

---

# 51. Questões abertas após CP05

Permanecem abertas:
1. Freshness, cadence e triggers de reavaliação;
2. regra final de Eligibility geral;
3. Capacity viability threshold definitivo;
4. Confidence threshold definitivo para Confirmed;
5. regras detalhadas por constructo para Δ0–Δ3;
6. critérios objetivos definitivos de Comparative Veto;
7. comportamento definitivo de Friction Modifier;
8. eventuais regras de hysteresis, se empiricamente justificadas;
9. tratamento definitivo de Classification Stability além de Confirmed/Provisional + Stability Envelope;
10. Indicator Specification Cards finais;
11. schemas técnicos do Evidence Registry, Coverage Map, Friction Event Registry, Comparative Decision Record, Historical Class Ledger e registros de Trajectory;
12. lifecycle formal Ranking ↔ Radar de Ativos Promissores;
13. regra objetiva de derivação da Watchlist;
14. tratamento definitivo de ETH estrutural + Vetores;
15. schema técnico de Flow Vector e metadados de redundância upstream;
16. metodologia formal do Capital Rotation para priorização de Vetores;
17. revisão futura da metodologia histórica do Radar de Narrativas;
18. integração final com Asset PRO;
19. desenho dos pilotos e validação empírica;
20. testar discriminabilidade do motor sem pesos;
21. decisão sobre eventual score cardinal;
22. se pesos se tornarem necessários, metodologia para obtê-los sem arbitrariedade;
23. MEL permanece backlog interno e não módulo independente.

---

# 52. Próximo passo exato após CP05

## Etapa 38 — Freshness, cadence e triggers de reavaliação

Objetivo:
> definir quando evidências, constructos, relações comparativas e Ranking Classes devem ser reavaliados, coordenando atualizações periódicas e event-driven sem reconstrução desnecessária de todo o Ranking.

Questões mínimas:
- frequência periódica do Ranking;
- compatibilidade com a cadência semanal histórica;
- freshness por família de evidência/indicador;
- quando um Construct State expira ou precisa de recertificação;
- triggers extraordinários;
- propagação de atualização upstream para o Ranking;
- quando recalcular apenas um ativo, um Vetor, um bloco comparativo ou todo o grafo;
- quando reconstruir Preference Layers e Ranking Classes;
- tratamento de dados stale;
- auditoria temporal e as-of discipline.

Regra:
> cadence operacional não deve alterar mérito, score ou constructo; apenas determina quando o estado precisa ser novamente observado e validado.

---

# 53. Prompt de retomada — CP05 — SUPERADO PELO CP06

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **MODO CONTINUIDADE** para iniciar esta conversa, dedicada ao `Ranking Institucional Simplificado — Metodologia Geral`. Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP05.md`.

> Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome da **Etapa 38 — Freshness, cadence e triggers de reavaliação**.

---

# 54. Status do CP05 — SUPERADO PELO CP06

- Fenômeno-alvo: preservado — captura de fluxo institucional relevante no horizonte.
- Arquitetura pré-quantitativa: fechada em nível de trabalho.
- Consolidação multivetorial: definida sem soma ou prêmio por quantidade de Vetores.
- Motor comparativo ordinal: definido até dominance, Δ, veto, concordance e outranking.
- Preference Graph: definido conceitualmente.
- SCCs / cycles / equivalence / incomparability: tratamento conceitual definido.
- Preference Layers: definidas.
- Ranking Classes: definidas como estratos da ordem parcial.
- Base Class + Stability Envelope: definidos.
- Confirmed vs Provisional Class: definidos sem nova escala numérica.
- Trajectory: formalizada por constructo e separada de Confidence e Class Movement.
- Mapa conceitual simplificado: incorporado para facilitar retomada humana.
- Pesos: não definidos.
- Score cardinal: não definido e não obrigatório.
- Próximo problema: Freshness, cadence e triggers de reavaliação.
- Documento: handoff operacional; não normativo.

---

# 55. CHECKPOINT CP06 — Cadência, universo suportado, Capacity, Confidence, Δ/Veto e Frictions

Esta seção e as seções 56–60 constituem o estado operacional vigente deste handoff e prevalecem sobre trechos anteriores quando houver diferença de estado, próximo passo, terminologia ou arquitetura.

Cobertura deste checkpoint:
- Etapa 38 — Freshness, cadence e triggers de reavaliação;
- Etapa 39 — Eligibility Geral revisada e Supported Market Universe;
- Etapa 40 — Capacity Viability Gate;
- Etapa 41 — threshold de Confidence para estados e decisões Confirmed;
- Etapa 42 — calibração operacional de Δ0–Δ3 e Comparative Veto;
- Etapa 43 — Friction Severity, Modifier, Comparative Veto e Blocker;
- correções arquiteturais sobre uso comercial da Suite e papel das fontes de mercado;
- itens de backlog BL-RANK-001 e BL-RANK-002.

## 55.1 Premissa de produto

A CRYPTO PRO SUITE não deve mais ser tratada como solução de uso exclusivamente pessoal. A direção atual é de **serviço comercial**.

Consequências:
- preferências pessoais do autor/usuário não constituem justificativa metodológica;
- decisões de arquitetura, fontes e cobertura devem ser defendidas por critérios técnicos, metodológicos, operacionais, econômicos e de licenciamento;
- sugestões do usuário devem ser tratadas como hipóteses ou decisões candidatas a serem criticamente avaliadas, não como diretrizes automáticas.

## 55.2 Etapa 38 — Freshness, cadence e triggers

Premissa:
> a versão inicial da CRYPTO PRO SUITE terá execução oficial semanal.

Regras de trabalho:
- cada Weekly Run produz snapshot oficial com as-of explícito;
- execução semanal não implica recolher todos os dados do zero;
- freshness é indicator-dependent;
- perfis de evidência: fast-moving, medium-moving, structural/slow-moving e event-driven;
- dado stale não vira evidência negativa;
- perda de freshness afeta primeiro Confidence/Confirmation;
- Construct State não expira mecanicamente;
- movimento de preço isolado não é trigger metodológico do Ranking;
- pesquisa/estado podem ser atualizados incrementalmente;
- mudanças em arestas de preferência exigem reconstrução global do Preference Graph e Ranking Classes;
- comparação A×B só precisa ser refeita quando informação decisiva muda;
- mudanças sistêmicas podem exigir Full Reassessment;
- upstream e Ranking precisam de coerência temporal;
- toda mudança de classe exige Change Reason auditável.

### Backlog relacionado — BL-RANK-001

Foi criado `03-componentes/23-ranking/BACKLOG.md` com o item:
**BL-RANK-001 — Critical Event Watch / Interim Methodological Update**.

Direção conceitual aceita, mas ainda não especificada:
- Weekly Run = execução oficial;
- Critical Event Watch = vigilância leve entre runs, potencialmente diária;
- Interim Methodological Update = saída excepcional;
- respostas candidatas: Monitor / Partial Reassessment / Critical Invalidation.

Esse item permanece backlog e não requisito fechado da v1.0.

## 55.3 Etapa 39 — Supported Market Universe, Eligibility e Data Sufficiency

Correção estrutural:
> a ordem das perguntas de Eligibility é operacional, não apenas lógica, e o Ranking não deve pressupor varredura exaustiva do universo global de criptoativos.

Arquitetura vigente:

```text
Approved / Supported Market Sources
                ↓
       Supported Market Universe
                ↓
       Asset / Scope Eligibility
                ↓
          Current Admission
      relação com Flow Vectors
                ↓
        Data Sufficiency Gate
                ↓
      Asset × Vector Assessment
                ↓
          Materiality Gate
                ↓
          Capacity Gate
                ↓
     Frictions + Confidence
                ↓
       Ranking-Ready Universe
                ↓
        Comparative Engine
                ↓
          Ranking Classes
```

### Supported Market Universe

- representa cobertura do produto, não mérito do ativo;
- não deve ser confundido com universo econômico completo de criptoativos;
- grandes CEXs podem ser uma fronteira inicial eficiente, mas não devem ser presumidas como universo completo;
- ativos emergentes relevantes podem surgir fora de grandes CEXs;
- arquitetura deve permanecer extensível a DEXs, venues institucionais e outras fontes aprovadas;
- nomes específicos de exchanges pertencem à source governance/datafeed configuration, não à metodologia permanente do Ranking.

### Asset / Scope Eligibility

Avalia se o objeto é conceitualmente analisável:
- identidade canônica resolvida;
- ativo econômico identificável;
- existência de mercado/representação relevante;
- dados básicos verificáveis;
- compatibilidade com o escopo.

### Current Admission

Exige ao menos uma hipótese economicamente testável de relação Ativo–Vetor para os Flow Vectors vigentes.

### Data Sufficiency Gate

Pergunta se os dados oficiais disponíveis são suficientes, válidos e frescos para executar os constructos aplicáveis.

Data Sufficiency ≠ mérito e ≠ Capacity.

### Fonte e Data Feed

- o Ranking deve consumir o contrato oficial do Crypto Pro Data Feed, não buscar silenciosamente fontes ad hoc durante execução formal;
- seleção de fontes deve ser objetiva e compatível com serviço comercial;
- API gratuita não implica automaticamente licença de uso/redistribuição comercial;
- para Asset PRO, dados como volume/candles precisam de provenance explícita de venue;
- hipótese atual: Asset PRO pode exigir Canonical Venue/Market; Capacity pode demandar visão multi-venue.

### Backlog relacionado — BL-RANK-002

Foi adicionado ao backlog:
**BL-RANK-002 — Supported Market Universe e governança de fontes do Data Feed**.

Questões futuras:
- Approved Market Sources por versão;
- critérios de cobertura, qualidade, API, histórico, custo, continuidade e licenciamento;
- política de Canonical Market/Venue para Asset PRO;
- possível Capacity multi-venue;
- Data Coverage Expansion Request;
- eventual expansão para DEXs/venues institucionais.

## 55.4 Etapa 40 — Capacity Viability Gate

Constructos:
- Institutional Accessibility;
- Absorption Capacity.

Regra provisória:
> CAP-PASS quando Accessibility ≥ E2 AND Absorption ≥ E2, sob Institutional Access Context e Reference Allocation Scale explícitos, com evidência suficiente.

Estados:
- CAP-PASS;
- CAP-FAIL;
- CAP-IND.

Princípios:
- Accessibility e Absorption são não compensatórios no gate;
- Capacity é contextual;
- IAC precisa ser padronizado para o produto;
- RAS deve ser definida antes da avaliação;
- valor quantitativo da RAS ainda não foi calibrado;
- multi-RAS permanece hipótese a testar;
- listing ≠ Accessibility;
- Data Sufficiency ≠ Capacity;
- volume bruto não demonstra Absorption;
- Capacity provavelmente exigirá abordagem multi-venue em uma oferta comercial madura;
- metodologia permanece venue-agnostic;
- Capacity FAIL pode alimentar Radar com condição objetiva de promoção;
- após o gate, Capacity continua sendo discriminador comparativo.

## 55.5 Etapa 41 — Confidence threshold

Escala:
- C0 Insuficiente;
- C1 Baixa;
- C2 Moderada;
- C3 Alta;
- C4 Muito alta.

Regra operacional provisória:
> **C3 é o threshold normal para uma conclusão Confirmed.**

Interpretação:
- C0/C1 → insuficiente para conclusão formal;
- C2 → normalmente Provisional;
- C3/C4 → elegível para Confirmed;
- C3 não supera Epistemic Blocker.

Regras:
- Confidence não é média aritmética simples;
- pode ser bottleneck-aware;
- confirmação depende das proposições decision-relevant;
- fonte única primária e autoritativa pode ser suficiente quando semanticamente apropriado;
- autoridade não substitui pertinência;
- missing/stale data não equivale a evidência negativa;
- Confirmed PASS e Confirmed FAIL requerem robustez epistemológica;
- Materiality e Capacity Gates requerem C3+ nos componentes decisivos para confirmação;
- Confirmed Outranking exige C3+ nas evidências decisivas;
- lacuna outcome-sensitive impede confirmação;
- Provisional Outranking só é admissível quando a lacuna residual não puder plausivelmente esconder veto/oposição material;
- Base Graph usa apenas relações confirmadas;
- relações provisórias entram no Stability Envelope;
- threshold C3 deve ser validado empiricamente antes da versão formal.

## 55.6 Etapa 42 — Δ0–Δ3 e Comparative Veto

Estados:
- Δ0 Indistinguishable;
- Δ1 Limited;
- Δ2 Material;
- Δ3 Critical.

Regras:
- Δ é diferença semântica/econômica, não distância aritmética;
- mesmo E-state → Δ0 por padrão, excepcionalmente Δ1;
- mesmo E-state não pode gerar Δ2/Δ3;
- estados adjacentes → Δ1 ou Δ2;
- E2 versus E4 → Δ2 ou Δ3;
- Δ3 exige consequência crítica, não apenas distância ordinal.

Veto eligibility:
- Exposure: sim, condicional;
- Economic Capture: sim, nuclear;
- Position: não por padrão;
- Accessibility: sim, condicional;
- Absorption: sim, condicional.

Comparative Veto exige:
- Δ3;
- constructo veto-eligible;
- consequência diretamente relevante;
- contexto/horizonte comparável;
- Confidence ≥ C3;
- ausência de Epistemic Blocker;
- ausência de double counting.

Δ3 sem veto = **Strong Opposition**.

Veto é direcional. Vetos bilaterais podem produzir INCOMPARABLE.

Relationship e Capacity preservam trade-offs internos sem média.

Regra de concordance refinada:
> A OUTRANKS B quando existe pelo menos uma diferença material Δ2/Δ3 confirmada favorável a A, nenhuma oposição material Δ2/Δ3 confirmada favorece B e nenhum veto econômico ou epistemológico bloqueia a direção.

## 55.7 Etapa 43 — Frictions

Friction ≠ Risk Score genérico.

Severity:
- F0 None/Immaterial;
- F1 Limited;
- F2 Material;
- F3 Severe;
- F4 Critical;
- IND.

Famílias:
- Regulatory / Legal;
- Supply / Dilution;
- Concentration / Control;
- Protocol / Security;
- Governance / Dependency;
- Market Structure / Counterparty.

Lifecycle:
- Active;
- Mitigating;
- Resolved;
- Expired;
- Indeterminate.

Effect:
- Flag;
- Modifier;
- Comparative Veto;
- Blocker.

Princípios:
- Severity e Effect são objetos distintos;
- F2 tende a Modifier; F3 a Modifier/Veto; F4 a Veto/Blocker, sem automatismo;
- toda Friction precisa de mecanismo causal;
- Primary Owner obrigatório para evitar double counting;
- Frictions podem ser asset-wide, Asset×Vector ou context-specific;
- quantidade de Frictions não constitui score;
- causal clusters evitam contagem duplicada;
- efeitos compostos exigem interação causal demonstrada;
- Comparative Veto por Friction exige gravidade, causal relevance, horizon/context relevance, C3+ e ausência de double counting;
- Blocker deve ser raro;
- F4 é tipicamente necessário, mas não suficiente, para Friction Blocker;
- condições pertencentes a Eligibility/Accessibility/Absorption não devem ser duplicadas como Friction Blocker;
- Friction resolvida remove obstáculo, não cria bônus;
- ativo com tese forte mas Friction impeditiva temporária pode ir ao Radar com condição objetiva de retorno.

---

# 56. Arquitetura vigente no CP06

```text
SUPPORTED MARKET UNIVERSE
        ↓
Asset / Scope Eligibility
        ↓
Current Admission
        ↓
Data Sufficiency
        ↓
Asset × Vector Relationship
        ↓
Materiality Gate
        ↓
Capacity Gate
        ↓
Frictions
        ↓
Confidence
        ↓
Δ + Veto + Concordance
        ↓
Dominance / Outranking
        ↓
Preference Graph
        ↓
Ranking Classes
        ↓
Trajectory / Weekly Monitoring
```

Sem score cardinal obrigatório, sem pesos e sem majority voting.

---

# 57. Decisões e hipóteses que ainda precisam de teste

Antes de pilotos, permanecem provisórios ou abertos:
1. valores e classes de Reference Allocation Scale;
2. definição da Reference Institutional Population / Institutional Access Context;
3. thresholds quantitativos dos indicadores de Accessibility/Absorption;
4. source governance comercial do Data Feed;
5. Canonical Venue/Market do Asset PRO;
6. escopo multi-venue de Capacity;
7. eventual cobertura de DEXs/venues institucionais;
8. threshold C3 de confirmação;
9. regras específicas de Δ por constructo;
10. critérios objetivos de veto;
11. regras de Friction Modifier/Blocker;
12. tratamento de stablecoins;
13. integração estrutural + vetorial de ETH;
14. regra definitiva da Watchlist;
15. lifecycle formal do Radar;
16. schemas técnicos de registros;
17. discriminação efetiva do motor sem score;
18. eventual necessidade futura de pesos/cardinalização.

---

# 58. Próximo passo exato após CP06

## Etapa 44 — Revisão de Prontidão Metodológica para Pilotos

Objetivo:
> auditar a metodologia geral construída até aqui e separar claramente o que está suficientemente definido para teste, o que precisa ser parametrizado antes do primeiro piloto, o que deve ser calibrado durante os pilotos e o que deve permanecer deliberadamente para depois.

A revisão deve produzir pelo menos quatro blocos:
1. **Ready for Pilot** — conceitos e regras suficientemente definidos;
2. **Pre-Pilot Parameters Required** — parâmetros mínimos sem os quais o piloto não é executável;
3. **Pilot-Calibrated Items** — itens que devem ser testados/calibrados empiricamente;
4. **Post-Pilot / Deferred** — itens que não devem bloquear o primeiro piloto.

Regra:
> a partir desta etapa, evitar adicionar novas camadas teóricas sem evidência de necessidade. O próximo foco deve ser executabilidade, falsificabilidade, auditabilidade e capacidade de discriminação do método.

---

# 59. Prompt de retomada — CP06 — SUPERADO PELO CP07

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **MODO CONTINUIDADE** para iniciar esta conversa, dedicada ao `Ranking Institucional Simplificado — Metodologia Geral`. Considere também o checkpoint/handoff armazenado no repositório em `archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-09-30_CP06.md`.

> Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome da **Etapa 44 — Revisão de Prontidão Metodológica para Pilotos**.

---

# 60. Status do CP06 — SUPERADO PELO CP07

- Produto: direção comercial registrada.
- Weekly Run: premissa operacional vigente.
- Critical Event Watch / Interim Update: backlog.
- Supported Market Universe: incorporado à arquitetura.
- Source governance comercial: backlog/dependência futura do Data Feed.
- Asset Eligibility / Current Admission / Data Sufficiency: separados.
- Materiality Gate: preservado.
- Capacity Gate: definido provisoriamente em E2/E2 sob IAC + RAS.
- Confidence: C3 como threshold provisório de Confirmed.
- Δ0–Δ3: regras operacionais refinadas.
- Comparative Veto: condições explícitas.
- Frictions: Severity, lifecycle e effects definidos.
- Score cardinal: não definido e não obrigatório.
- Pesos: não definidos.
- Próxima etapa: revisão de prontidão para pilotos.
- Documento: handoff operacional; não normativo.

---

# 61. CHECKPOINT CP07 — Prontidão e desenho do Piloto Metodológico 01

Esta seção e as seções seguintes constituem o estado operacional vigente do handoff e prevalecem sobre trechos anteriores quando houver diferença de status, parâmetros experimentais, próximo passo ou arquitetura do piloto.

Cobertura:
- Etapa 44 — Revisão de Prontidão Metodológica para Pilotos;
- Etapa 45 — desenho do Piloto Metodológico 01;
- Etapa 46 — Pilot Configuration Package — PCP-01;
- Etapa 47 — MVIP-01: Exposure, Economic Capture e Structural Position;
- Etapa 48 — MVIP-01: Institutional Accessibility e Absorption Capacity;
- Etapa 49 — Frictions, Evidence Registry e Decision Records;
- Etapa 50 — Candidate Discovery Protocol, Pilot Data Capture e T0 Activation.

## 61.1 Etapa 44 — Readiness

Decisão:
> GO condicional para piloto metodológico controlado; NO-GO para produção/comercialização.

Núcleo suficientemente maduro:
- fenômeno-alvo;
- unidade Asset × Vector × Horizon × As-of;
- Exposure / Capture / Position;
- EMP / Capture Pathway;
- Materiality Gate;
- Capacity architecture;
- Frictions;
- Confidence;
- Δ0–Δ3;
- veto/concordance;
- graph/classes.

Bloqueadores pré-piloto identificados:
- Reference Institutional Population;
- Reference Allocation Scale;
- Minimum Viable Indicator Pack;
- Pilot Data Requirement Matrix.

Regra:
> não adicionar novos constructos, score ou pesos antes de evidência empírica de necessidade.

## 61.2 Etapa 45 — Pilot 01

Tipo:
- static;
- cross-sectional;
- controlled;
- adversarial.

Objetivo:
> testar executabilidade, reprodutibilidade, discriminação, auditabilidade e custo analítico do Ranking Geral sem score cardinal nem pesos.

Estrutura inicial:
- 1 Flow Vector;
- 1 horizon;
- 1 institutional profile;
- 1 RAS;
- ~8–12 ativos;
- pairwise comparison;
- sem Trajectory no primeiro run;
- outcome de preço não é critério de sucesso.

O piloto deve preservar INCOMPARABLE, IND, cycles e outras saídas não ordenadas como evidência sobre o método, sem forçar ranking total.

## 61.3 Etapa 46 — PCP-01

Parâmetros de trabalho:
- horizon = 90 dias;
- 1 Flow Vector;
- FV-01 = Institutional Tokenization & Onchain Capital Markets Infrastructure;
- RIP-01 = Direct Digital-Asset-Capable Professional Allocator (DDAPA);
- RAS-01 = US$ 5 milhões executados em até 24h;
- target de aproximadamente 10 ativos;
- BTC, ETH, stablecoins e memecoins fora do Pilot 01;
- no weights;
- no cardinal score.

FV-01:
> direção de adoção, atividade e alocação institucional em infraestrutura pública de blockchain e protocolos utilizados para emissão, registro, liquidação, distribuição, interoperabilidade ou liquidez de ativos financeiros e real-world assets tokenizados.

RIP-01:
> entidade profissional com capacidade legal, operacional e tecnológica para adquirir e manter diretamente criptoativos spot sob controles institucionais de execução, custody, liquidity e compliance.

RAS-01:
> probe experimental, não parâmetro estrutural da Suite.

Fontes candidatas do piloto:
- Binance;
- Bybit;
- OKX;
- Bitget;
- MEXC.

Essas fontes não estão ratificadas como fontes comerciais definitivas.

## 61.4 Correção temporal do PCP-01

A proposta anterior de as-of retroativo em 30/09/2026 23:59 UTC foi SUPERADA.

Motivo:
> Absorption depende de dados prospectivos de microestrutura (books/spread/depth) que podem não ser historicamente reconstruíveis com fidelidade suficiente.

Regra vigente:
- Pilot 01 terá T0 futuro;
- T0 será definido somente após infraestrutura mínima de captura estar pronta;
- candidate membership será congelado antes do início da janela de captura;
- H = 90 dias contado a partir de T0.

## 61.5 Etapa 47 — MVIP Relationship

Constructos instrumentados:
- Causal Exposure;
- Economic Capture;
- Structural Position.

Exposure:
- exige mecanismo ativo + uso econômico verificável para E2+;
- marketing, preço, volume, market cap e mera capacidade técnica não bastam;
- E1→E2 = Material Exposure Boundary.

Capture:
- exige cadeia Vector activity → project/protocol function → token economic transmission → ranked asset;
- activity metrics não demonstram Capture sozinhas;
- gas/staking/utility não implicam automaticamente alta captura;
- para E2+: mecanismo + materialidade;
- Planned mechanism não habilita Capture atual;
- E1→E2 = Economic Capture Boundary.

Position:
- exige Functional Reference Class;
- mede posição econômica relativa, não qualidade geral;
- requer denominador/reference set defensável;
- E4 exige convergência quantitativa + centralidade estrutural.

Materiality Gate PCP-01:
- Confirmed PASS = Exposure ≥ E2/C3+ AND Capture ≥ E2/C3+;
- Confirmed FAIL = Exposure ≤ E1/C3+ OR Capture ≤ E1/C3+;
- C2 pode gerar Provisional;
- insufficient evidence gera IND.

## 61.6 Etapa 48 — MVIP Capacity

RIP-01 no piloto pressupõe mandato legal para spot direto e acesso legítimo às fontes aprovadas; não pretende modelar todas as jurisdições.

Introduzido:
**Qualified Execution Venue — QEV**, avaliado por Asset × Venue × Market × T0.

Accessibility propositions:
- Execution Access;
- Custody/Holding Path;
- Settlement/Transferability;
- Access Resilience.

Accessibility:
- E1→E2 = Institutional Viability Boundary;
- número de exchanges não determina E-state;
- derivatives são supporting, não requisito universal.

Absorption:
- mede Executable Liquidity relative to RAS-01;
- market cap e volume isolado são insuficientes;
- RAS-01 dividida em 24 child orders de ~US$208,3k;
- simulação buy/sell;
- multi-QEV execution permitida;
- venue concentration pertence primariamente a Market Structure/Counterparty Friction, evitando double counting.

Janela piloto:
- 24 snapshots horários antes de T0;
- 7 dias de turnover persistence;
- cobertura mínima proposta de 18/24 snapshots;
- PEC — Projected Execution Cost;
- PR — Participation Ratio;
- P90 do PEC como diagnóstico.

Thresholds experimentais:
- E2: PEC mediano ≤ 2,0% e PR ≤ 10%;
- E3: PEC mediano ≤ 1,0% e PR ≤ 5%;
- E4: PEC mediano ≤ 0,50% e PR ≤ 2%.

Esses thresholds são exclusivos do PCP-01 e precisam de validação.

Capacity Gate:
- Confirmed PASS = Accessibility ≥ E2/C3+ AND Absorption ≥ E2/C3+;
- Confirmed FAIL = qualquer componente ≤ E1/C3+;
- C2 pode gerar Provisional;
- insufficiency/conflict pode gerar CAP-IND.

## 61.7 Etapa 49 — registros auditáveis

Evidence Registry — ER-PCP01:
- Evidence ID;
- asset/vector/construct/proposition;
- source/source type;
- temporal metadata;
- evidence type;
- direction;
- freshness;
- independence group;
- causal cluster;
- contradiction flag;
- confidence metadata.

Registros:
- FAR — Friction Assessment Record;
- CAR — Construct Assessment Record;
- GDR — Gate Decision Record;
- CMP — Pairwise Decision Record;
- VTO — Veto Record;
- PER — Preference Edge Record;
- MGR — Methodological Gap Record.

Somente Confirmed DOMINATES e Confirmed OUTRANKS criam arestas no Base Preference Graph.

Inter-rater:
- dois avaliadores devem receber o mesmo Evidence Pack congelado;
- divergências são medidas antes da reconciliação;
- reconciliação não apaga avaliações originais.

Freeze hierarchy:
1. Protocol;
2. Parameters;
3. Evidence Pack;
4. Individual Assessments.

## 61.8 Etapa 50 — Candidate Discovery, Pilot Data Capture e T0 Activation

### Qualified Pilot Source — QPS

As cinco exchanges candidatas não entram automaticamente no piloto. Cada uma deve passar uma capability review.

QPS precisa suportar, conforme aplicável:
- instrument/market catalog;
- market status;
- spot order book;
- timestamps;
- volume/history;
- pair metadata;
- estabilidade operacional mínima;
- uso permitido para o experimento.

O conjunto efetivamente aprovado forma as fontes do SMU-PCP01.

### Supported Market Universe

SMU-PCP01 = união dos spot markets das QPS, seguida de canonicalização e Scope/Eligibility.

Excluir do objeto de Ranking no Pilot 01:
- BTC;
- ETH;
- stablecoins;
- memecoins;
- wrapped duplicates sem independência econômica;
- leveraged/synthetic exchange products;
- ativos/migrações não resolvidos;
- objetos que não constituam o criptoativo econômico rankeável.

### FV-01 Discovery Ontology

Funções de descoberta:
- Issuance / Asset Lifecycle;
- Settlement / Execution;
- Interoperability / Messaging;
- Data / Oracle;
- Liquidity / Market Infrastructure;
- Compliance / Identity / Access.

Discovery pode usar fontes amplas para gerar hipótese, mas Current Admission exige relação ativa e testável apoiada por evidência admissível Tier 1–3.

Estados:
- CA-PASS;
- CA-FAIL;
- CA-IND.

CA-PASS não equivale a Materiality PASS.

### Candidate reduction

Se admitted pool ≤12:
> incluir todos.

Se >12:
> aplicar stratified reproducible sampling.

Estratos:
- Functional Reference Class;
- Supported Venue Breadth como variável secundária.

Seleção dentro do estrato:
> pseudo-random determinística com seed fixa `PCP01-FV01`.

Não usar:
- retorno;
- popularidade;
- expectativa de qualidade;
- posição desejada;
- market-cap ranking como escolha subjetiva.

A proposta anterior de stratificação por market cap fica superada para o PCP-01.

### Temporal design

Definições:
- UFT — Universe Freeze Time;
- Capture Start = UFT;
- T0 = UFT + 24h;
- H = T0 + 90 dias.

Membership da amostra congela em UFT.

Eventos entre UFT e T0:
- podem alterar avaliação;
- não adicionam/substituem candidatos;
- hard identity/scope invalidation é registrada, sem replacement.

### Order-book capture

Para cada QEV:
- captura horária;
- UTC;
- 24 observações planejadas;
- best bid/ask;
- depth suficiente para simular child order, idealmente com margem;
- market/pair status;
- exchange timestamp + observed_at;
- provenance.

Cross-venue alignment:
- target ≤60s;
- tolerância máxima para agregação consolidada = 180s;
- além disso, dados permanecem venue-specific para aquela observação.

### PEC fee treatment — correção

Para garantir reprodutibilidade:
> **PEC_core exclui fees account-specific.**

Fees podem ser registradas como:
> standardized fee overlay diagnóstico, usando fee pública/base quando disponível.

Isto supera a formulação anterior de incorporar fees diretamente ao PEC principal.

### Turnover / PR

- usar 7 dias terminando em T0;
- normalizar quote para USD;
- preservar volume_reliability_flag quando depth/turnover forem inconsistentes;
- PR continua sanity check, não score.

### T0 Activation Rule

T0 só pode ser agendado após:
- PCP-01 configuration freeze;
- QPS capability matrix concluída;
- SMU/canonicalization concluídos;
- candidate set congelado;
- QEV map congelado;
- capture pipeline validada;
- timestamp/provenance/retry/logging validados;
- pelo menos dois ciclos horários consecutivos de dry-run tecnicamente bem-sucedidos.

Após readiness:
> Capture Start = próxima hora UTC cheia; T0 = Capture Start + 24h.

### Run integrity

Distinguir:
- venue/market unavailability documentada pela própria venue = possível evidência operacional de Accessibility/market status;
- API/source transport failure = falha de aquisição de dados, não evidência de baixa liquidez ou baixo mérito do ativo;
- collector-side failure = falha técnica do piloto.

Se collector-side failure ou API/source transport failure sistêmica afetar >25% dos capture events planejados:
> marcar o run como TECHNICALLY INVALID e repetir, sem reinterpretar a falha de dados como condição econômica dos ativos.

---

# 62. Arquitetura operacional vigente após CP07

```text
QPS capability review
        ↓
Supported Market Universe
        ↓
Canonicalization + Scope Eligibility
        ↓
FV-01 Candidate Discovery
        ↓
Current Admission
        ↓
Candidate sampling / freeze (UFT)
        ↓
24h prospective market-microstructure capture
        ↓
T0
        ↓
Evidence Pack freeze
        ↓
Construct Assessments
        ↓
Materiality Gate
        ↓
Capacity Gate
        ↓
Frictions + Confidence
        ↓
Pairwise Δ / Veto / Concordance
        ↓
Preference Graph
        ↓
Ranking Classes
        ↓
Pilot diagnostics / inter-rater / MGRs
```

---

# 63. Próximo passo exato após CP07

## Etapa 51 — Pré-registro operacional e implementação mínima do Pilot Data Capture

Objetivo:
> transformar o PCP-01 em artefatos executáveis antes de qualquer candidate scoring.

A Etapa 51 deverá:
- criar Pilot Configuration formal;
- criar QPS Capability Matrix;
- criar Canonical Asset Registry schema;
- criar Candidate Discovery Register;
- criar QEV Mapping schema;
- criar Capture Manifest;
- definir estrutura de arquivos/diretórios do piloto;
- especificar o coletor mínimo de books/market status/volume;
- definir dry-run protocol;
- só então autorizar UFT/T0.

Regra:
> nenhum ativo deve receber E-state, Confidence, Friction, Δ ou Ranking Class antes da conclusão do pré-registro operacional.

---

# 64. Status do CP07

- Core methodology: frozen provisionally for pilot.
- Pilot 01: static, single-vector, adversarial.
- FV-01: tokenization/onchain capital-markets infrastructure.
- RIP-01: DDAPA.
- RAS-01: US$5M/24h, experimental.
- Retroactive as-of: rejected.
- T0: future, post-readiness.
- MVIP Relationship: instrumented.
- MVIP Capacity: instrumented.
- Frictions/Confidence/records: instrumented.
- Candidate Discovery Protocol: defined.
- QPS/QEV architecture: defined.
- Pilot Data Capture: defined conceptually.
- Score/weights: absent by design.
- Candidate scoring: not yet authorized.
- Next step: operational preregistration + minimal capture implementation.
- Documento: handoff operacional; não normativo.

---

# 65. CHECKPOINT CP08 — Execução pré-avaliação do PCP-01

Este checkpoint registra a passagem do PCP-01 de pré-registro conceitual para execução operacional controlada, sem ainda iniciar avaliação de constructos.

Cobertura:
- Etapa 51 — pré-registro operacional persistido;
- Etapa 52 — revisão QPS e extensão experimental do Data Feed;
- Etapa 53 — separação Pilot Source Qualification vs Commercial Source Approval;
- Etapa 54 — primeiro probe técnico + Supported Market Universe + Discovery Pool;
- Etapa 55 — canonicalização econômica + Current Admission;
- Etapa 56 — Functional Reference Classes + amostragem determinística do Run A.

## 65.1 Artefatos persistidos do PCP-01

Diretório:
`03-componentes/23-ranking/validacao/geral/piloto-01/`

Artefatos principais:
- `README.md`
- `PCP-01-CONFIGURATION.md`
- `QPS-CAPABILITY-MATRIX.md`
- `CANONICAL-ASSET-REGISTRY-SCHEMA.md`
- `CANONICAL-ASSET-REGISTRY.md`
- `CANDIDATE-DISCOVERY-REGISTER.md`
- `CURRENT-ADMISSION-REGISTER.md`
- `FUNCTIONAL-REFERENCE-CLASSES.md`
- `DETERMINISTIC-SAMPLING-PROTOCOL.md`
- `RUN-A-SAMPLE-RECORD.md`
- `RUN-A-SAMPLE.json`
- `QEV-MAPPING-AND-CAPTURE-MANIFEST.md`
- `PILOT-DATA-CAPTURE-SPEC.md`
- `DRY-RUN-AND-T0-PROTOCOL.md`
- `RECORD-SCHEMAS.md`

## 65.2 Source qualification policy

Commercial source approval no longer blocks PCP-01 methodological validation.

Pilot Source Qualification requires:
- technical capability;
- operational dry-run;
- auditable provenance/failure semantics.

Commercial rights/licensing remain a separate future production gate.

## 65.3 Binance experimental path

Data Feed experimental implementation:
- `src/experimental/pcp01/binance_qps_probe.py`
- workflow `.github/workflows/pcp01-binance-qps-probe.yml`

Successful technical probe:
- workflow run `36809639883`;
- result `PASS`;
- tested symbol `BTCUSDT`;
- 1000 bid + 1000 ask levels;
- visible depth above PCP-01 child-order notional on both sides;
- 7-day turnover retrieved;
- provenance preserved.

Result:
> Binance = TECHNICALLY ELIGIBLE.

It is not yet PILOT QUALIFIED because the two-cycle temporal dry-run required before UFT/T0 has not been completed.

## 65.4 Supported Market Universe

Experimental Data Feed generated and persisted:
`data/experimental/pcp-01/universe/binance-supported-market-universe.json`

Observed snapshot:
- 1374 active Binance spot markets;
- 504 provisional base-asset symbols.

Data Feed commit containing snapshot:
`7cb176a9dbe294d3e256095cbcfdca79f710c463`

The SMU is pilot coverage, not the complete crypto economic universe.

Canonicalization strategy is staged:
market-native provisional identity → FV-01 discovery → full economic identity only for discovered candidates.

## 65.5 Discovery Pool

FV-01 discovery produced 26 provisional candidates.

Current Admission results:
- CA-PASS = 22;
- CA-IND = 4;
- CA-FAIL = 0.

CA-IND:
- ATOM
- GNO
- ICP
- OSMO

CA-PASS:
- ADA
- ALGO
- APT
- ARB
- AVAX
- BNB
- HBAR
- HYPE
- INJ
- LINK
- ONDO
- OP
- PLUME
- POL
- QNT
- RSR
- SOL
- SUI
- SYRUP
- TRX
- XLM
- ZK

CA-PASS means only that an active, economically testable Asset–Vector hypothesis exists. It does not imply Materiality PASS or token Economic Capture.

## 65.6 Functional Reference Classes

Frozen before sample draw:

- FR-SET — Settlement / Execution Networks: 15
- FR-MID — Interoperability / Data Middleware: 2
- FR-ISS — Issuance / Asset Structuring Protocols: 2
- FR-MKT — Institutional Market / Liquidity / Credit Infrastructure: 3

Supported Venue Breadth is inactive as a secondary sampling variable in Run A because the current SMU is Binance-only and therefore non-discriminating across admitted candidates.

## 65.7 Deterministic Run A sample

Sampling protocol frozen in commit:
`022fba8f087a474185f7522bcb0c8ab5a68dc0c9`

Rules:
- sample size = 12;
- include all members of classes with population <=3;
- remaining slots assigned to larger class(es);
- internal subsampling by SHA-256 ascending;
- seed = `PCP01-FV01`.

Allocation:
- FR-SET: 5/15
- FR-MID: 2/2
- FR-ISS: 2/2
- FR-MKT: 3/3

Official Run A sample:
- PLUME
- OP
- APT
- ADA
- SUI
- LINK
- QNT
- ONDO
- RSR
- INJ
- HYPE
- SYRUP

Sample record commit:
`2935b9dec9a30fe7def36a1c4c681273aa922f31`

Non-selected CA-PASS assets remain admitted and may be used in later pilots/sensitivity tests. Exclusion from Run A has no merit interpretation.

## 65.8 Current pilot state

```text
Methodology core              FROZEN PROVISIONALLY
Pilot configuration           FROZEN
Binance technical probe       PASS
SMU                            CAPTURED
Discovery                     COMPLETE
Canonicalization              COMPLETE for discovery pool
Current Admission             COMPLETE
Functional classes            FROZEN
Run A sample                  FROZEN
Evidence Packs                NOT STARTED
Construct E-states            NOT STARTED
Materiality Gate              NOT EXECUTED
Capacity Gate                 NOT EXECUTED
UFT                            NOT DECLARED
T0                             NOT DECLARED
Ranking Classes               NOT CALCULATED
```

## 65.9 Next step

### Etapa 57 — Evidence Pack Design + Relationship Assessment Run A

The next block should:
1. instantiate Evidence Registry rows for the 12 sampled assets;
2. build EMP / Capture Pathway records;
3. assess Causal Exposure;
4. assess Economic Capture;
5. apply Materiality Gate;
6. only after Materiality confirmation, assess Structural Position;
7. preserve inter-rater independence.

Important:
> no Capacity or Ranking comparison should be executed before the individual Relationship block is frozen.

Because T0 is still future, the first Relationship Evidence Packs should use structural/event evidence valid up to the eventual freeze point, while market-microstructure data remains pending for Capacity.

---

# 66. Status of CP08

- Pre-evaluation universe construction: complete.
- Run A sample: frozen.
- Commercial source licensing: deferred from pilot path.
- First technical Data Feed path: validated.
- Full temporal dry-run: pending.
- UFT/T0: not declared.
- Relationship evidence assessment: next.
- Document: operational handoff; non-normative.

---

# 67. CP09 — QNT Exception Review e diagnóstico prospectivo

Após a Etapa 58, o caso QNT revelou dois problemas distintos:

1. **falha de completude de evidências**: o anúncio de 2026-09-24 da The Clearing House estava dentro do corte PRE-T0 e foi omitido do Evidence Pack original;
2. **possível lacuna metodológica**: validação institucional extraordinária pode anteceder a materialização observável do token-level Economic Capture.

## 67.1 Preservação de auditoria

O Evidence Registry e o Evaluator A originais permanecem imutáveis.

Foram criados:
- `QNT-EVIDENCE-SUPPLEMENT-PRET0.md`;
- `QNT-EXCEPTION-REVIEW-2026-10-01.md`;
- `PROSPECTIVE-INSTITUTIONAL-VALIDATION-SHADOW-TEST.md`;
- `PROSPECTIVE-INSTITUTIONAL-VALIDATION-SHADOW-RESULTS-PRET0.md`.

## 67.2 QNT reassessment com regras inalteradas

Resultado controlado:
- Exposure: E3/C3 → E3/C4;
- Capture: E1/C3 → E1/C4;
- Materiality: permanece CONFIRMED FAIL.

A evidência da The Clearing House confirma fortemente a relação institucional da Quant com FV-01, mas a documentação pública atual não demonstra obrigação de TCH/bancos adquirirem QNT nem mecanismo obrigatório de conversão de receita/uso em QNT. O current FAQ permite fee em USD ou QNT.

## 67.3 Ex-post market outcome

A forte reprecificação de QNT após o anúncio é registrada apenas como diagnóstico ex post. Preço/volume não alteram E-state nem Materiality.

## 67.4 MGR-006

`Prospective Institutional Validation / Future-Capture Gap` permanece OPEN.

O shadow test IV/PM/PTC foi aplicado simetricamente aos 12 ativos do Run A. QNT apresentou padrão distintivo:

`IV3 / PM2 / PTC1`

Interpretação:
- validação institucional excepcionalmente forte;
- implantação futura com caminho/timing concreto;
- token-level capture prospectivo ainda fracamente demonstrado.

Esse diagnóstico permanece fora do mérito do Ranking.

## 67.5 MGR-007

`Evidence Completeness / Material Event Retrieval Failure` permanece OPEN.

Antes do T0 oficial será obrigatório executar um Material Event Completeness Check asset-by-asset nos 12 ativos do Run A, cobrindo fontes primárias do projeto e contrapartes institucionais/emissores relevantes em janela recente definida.

## 67.6 Sequenciamento

A Etapa 59 de Structural Position não deve avançar antes da auditoria de completude de eventos materiais, pois uma omissão semelhante pode contaminar Position e outros constructos.

Próximo passo:
`Etapa 58B — Material Event Completeness Audit do Run A`.

## 67.7 Status

- Structural Position reference rule: RESOLVED;
- QNT exception review: COMPLETE;
- shadow prospective-validation diagnostic: EXECUTED, non-decisional;
- MGR-006: OPEN, no methodology change authorized;
- MGR-007: OPEN;
- T0: not declared;
- Ranking Classes: not calculated.