# CRYPTO PRO SUITE
## Protocolo de Reconstrução Histórica e Rastreabilidade

**Status:** Documento de trabalho  
**Escopo desta consolidação:** Etapas 1 a 5 + ajustes derivados do Piloto 01  
**Data de consolidação:** 22/09/2026

---

## 1. Finalidade

O **Protocolo de Reconstrução Histórica e Rastreabilidade do CRYPTO PRO SUITE** estabelece critérios, procedimentos e controles para recuperar, validar, classificar e registrar decisões, definições metodológicas, requisitos, alterações de escopo e demais eventos relevantes ocorridos durante o desenvolvimento do projeto quando esses elementos não estiverem adequadamente representados na documentação oficial vigente.

O protocolo tem quatro objetivos fundamentais:

- preservar a **fidelidade histórica** do projeto;
- estabelecer **rastreabilidade documental** entre decisões, fontes e artefatos;
- impedir que memória, interpretação posterior ou inferência sejam apresentadas como decisões históricas comprovadas;
- permitir que conhecimento disperso em conversas, documentos, arquivos e repositórios seja incorporado de maneira controlada ao corpus documental do CRYPTO PRO SUITE.

## 2. Princípios

### 2.1. Primazia da evidência

Toda reconstrução deverá estar vinculada, sempre que possível, a uma fonte verificável. A ausência de evidência não poderá ser substituída pela plausibilidade da informação.

### 2.2. Separação entre memória e evidência

Memória contextual, inclusive aquela mantida pelo próprio ChatGPT, poderá ser utilizada para **localização, orientação e formulação de hipóteses de busca**, mas não deverá, isoladamente, constituir evidência suficiente para consolidar uma decisão histórica.

### 2.3. Não retroatividade decisória

Uma decisão tomada durante o processo de reconstrução não deverá ser registrada como se tivesse sido tomada originalmente.

O protocolo deverá distinguir explicitamente:

- **Decisão histórica:** comprovadamente tomada no período reconstruído.
- **Reconstrução interpretativa:** conclusão obtida posteriormente a partir de evidências incompletas.
- **Nova decisão:** decisão tomada no presente para resolver uma lacuna identificada durante a reconstrução.

### 2.4. Preservação da evolução

Definições posteriormente abandonadas ou substituídas não deverão necessariamente desaparecer do registro histórico. Quando relevantes para compreender a evolução do projeto, deverão permanecer registradas como **superadas**, com indicação da decisão que as substituiu.

### 2.5. Temporalidade

Sempre que possível, cada evento reconstruído deverá possuir referência temporal. Quando a data exata não puder ser determinada, deverá ser registrado o intervalo temporal conhecido ou explicitada a indeterminação.

### 2.6. Proveniência

Toda informação incorporada ao histórico deverá preservar sua origem: conversa, documento, arquivo do repositório, registro de execução ou outra fonte admitida pelo protocolo.

### 2.7. Auditabilidade

Um terceiro que tenha acesso às mesmas fontes deverá conseguir compreender o encadeamento:

**fonte → evidência → interpretação → decisão reconstruída → impacto documental.**

Esse encadeamento será a base da futura **Matriz de Rastreabilidade Histórica**.

### 2.8. Conservadorismo documental

Na existência de dúvida material, a informação deverá permanecer pendente ou receber classificação de confiança inferior, em vez de ser artificialmente consolidada.

## 3. Escopo da reconstrução

O protocolo poderá ser aplicado a elementos historicamente relevantes do CRYPTO PRO SUITE, incluindo:

- decisões arquiteturais;
- decisões de governança;
- requisitos funcionais e não funcionais;
- definição e evolução dos módulos;
- metodologias, indicadores, fórmulas e critérios;
- alterações de escopo;
- dependências entre componentes;
- decisões relativas ao Crypto Pro Data Feed;
- estruturas documentais e convenções editoriais;
- decisões de implementação;
- testes e resultados relevantes;
- pendências e decisões adiadas;
- propostas posteriormente rejeitadas ou substituídas, quando relevantes para compreender a evolução do projeto.

## 4. Fora do escopo

O processo não deverá tentar preservar indiscriminadamente todo o conteúdo das conversas.

Comentários circunstanciais, repetições, explicações intermediárias, erros posteriormente corrigidos e discussões sem consequência para a evolução do projeto não precisam se transformar em registros históricos individuais.

O objeto de preservação é a **evolução decisória e metodológica do sistema**, e não uma transcrição integral de seu processo conversacional.

## 5. Regra fundamental

> **Nenhuma reconstrução deverá adquirir status histórico superior ao permitido pelas evidências que a sustentam.**

Essa regra deverá orientar inclusive situações em que o estado atual do CRYPTO PRO SUITE seja conhecido, mas não seja possível demonstrar documentalmente **quando, onde ou de que maneira** determinada definição foi adotada.

Regra complementar de proveniência:

> **A veracidade de uma informação não comprova sua proveniência. Cada fonte somente poderá sustentar os eventos que seu próprio conteúdo permita demonstrar.**

Conhecimento oriundo de outras fontes, memória contextual ou estado posterior do projeto não deverá completar silenciosamente a cadeia histórica da fonte examinada.

---

## 6. Princípio da autoridade contextual

A autoridade de uma fonte deverá ser determinada conjuntamente por:

**autenticidade + proximidade temporal + finalidade documental + estado de aprovação + relação direta com o fato investigado.**

A fonte hierarquicamente superior não deverá prevalecer de maneira automática quando estiver respondendo a uma pergunta diferente.

Para determinar **qual é a metodologia vigente**, um documento metodológico aprovado tende a possuir maior autoridade. Para determinar **como determinada regra surgiu**, a conversa original em que a decisão foi tomada poderá constituir evidência histórica mais adequada.

## 7. Classes de fontes

### 7.1. Nível A — Fonte normativa ou consolidada

Compreende documentos formalmente incorporados à estrutura documental do CRYPTO PRO SUITE, especialmente quando sua situação de aprovação puder ser comprovada.

Exemplos:

- Constituição;
- Documento Mestre;
- manuais metodológicos;
- especificações formalmente consolidadas;
- documentos de arquitetura;
- protocolos aprovados;
- versões oficiais armazenadas no repositório.

**Capacidade probatória:** elevada para determinar o estado formal do projeto no momento correspondente à versão analisada.

Um documento dessa categoria, porém, não prova automaticamente que determinada regra tenha se originado nele.

### 7.2. Nível B — Registro técnico versionado

Inclui evidências produzidas diretamente durante desenvolvimento ou execução:

- commits;
- histórico Git;
- código;
- workflows;
- arquivos de configuração;
- snapshots;
- testes;
- logs;
- releases;
- alterações documentais versionadas.

Essas fontes possuem especial relevância para estabelecer **cronologia técnica e implementação efetiva**.

### 7.3. Nível C — Registro deliberativo primário

Inclui conversas e outros registros nos quais determinada decisão foi discutida ou tomada.

No contexto atual, isso inclui principalmente as **conversas exportadas do desenvolvimento do CRYPTO PRO SUITE**.

Esses registros são particularmente importantes para reconstruir:

- origem de requisitos;
- alternativas consideradas;
- decisões;
- rejeições;
- mudanças de direção;
- justificativas;
- pendências;
- decisões explicitamente adiadas.

Uma declaração explícita como **“Concordo. Opção A.”** poderá constituir evidência decisória relevante quando interpretada junto ao conteúdo imediatamente anterior que define a Opção A.

### 7.4. Nível D — Artefato intermediário

Inclui:

- drafts;
- relatórios experimentais;
- planilhas provisórias;
- diagramas não aprovados;
- documentos de trabalho;
- resultados de testes;
- propostas estruturadas.

Essas fontes demonstram que determinada ideia ou estrutura **existiu**, mas não necessariamente que tenha sido aprovada.

### 7.5. Nível E — Evidência secundária

Inclui referências posteriores a eventos anteriores, por exemplo:

> “Como definimos anteriormente...”

ou

> “Mantemos a decisão tomada no módulo X...”

Essas referências podem corroborar uma reconstrução, mas possuem autoridade inferior ao registro original da decisão. São especialmente úteis quando a fonte primária ainda não foi localizada.

### 7.6. Nível F — Memória contextual

Inclui informações recuperadas da memória contextual mantida pelo sistema sobre o projeto.

A memória poderá ser utilizada para:

- localizar possíveis decisões;
- identificar conversas relevantes;
- formular consultas;
- apontar possíveis inconsistências;
- gerar hipóteses de reconstrução.

Porém:

> **Memória contextual não constitui, isoladamente, prova documental de uma decisão histórica.**

Uma informação recuperada exclusivamente dessa camada deverá permanecer como **hipótese a verificar**.

## 8. Distinção entre autoridade normativa e autoridade histórica

Uma fonte pode possuir:

- **Autoridade normativa (AN):** capacidade de demonstrar qual regra ou definição é oficialmente válida.
- **Autoridade histórica (AH):** capacidade de demonstrar quando, como ou por que determinada decisão ocorreu.

Uma conversa pode apresentar **AN baixa / AH alta**, enquanto um documento consolidado pode apresentar **AN alta / AH média**.

## 9. Corroboração

Sempre que possível, uma reconstrução relevante deverá utilizar mais de uma evidência.

Exemplo:

**Conversa original → decisão explícita.**  
**Commit posterior → implementação da decisão.**  
**Documento metodológico → consolidação da decisão.**

A cadeia **deliberação → implementação → formalização** deverá receber o maior grau de confiança na futura classificação de evidências.

## 10. Conflito entre fontes

Quando duas fontes apresentarem informações incompatíveis, não deverá ocorrer substituição automática.

O conflito deverá ser analisado segundo:

**temporalidade → autoridade contextual → explicitabilidade → estado de aprovação → implementação → evidência de supersessão.**

### 10.1. Decisão posterior explícita

A decisão posterior substitui a anterior.

Registro:

**Decisão original → SUPERADA POR → decisão posterior.**

Ambas permanecem no histórico.

### 10.2. Documento posterior diferente da conversa

Deverá ser investigado se houve:

- mudança deliberada;
- consolidação editorial;
- erro documental;
- decisão intermediária ainda não localizada.

Não se presume automaticamente que a conversa ou o documento esteja errado.

### 10.3. Implementação diverge da metodologia

Código ou execução não alteram automaticamente a metodologia.

A divergência poderá representar:

- bug;
- implementação incompleta;
- metodologia desatualizada;
- alteração ainda não documentada.

O caso deverá ser registrado como divergência até resolução.

### 10.4. Duas conversas aparentemente incompatíveis

Deverá ser verificado se:

1. tratam exatamente do mesmo objeto;
2. pertencem à mesma fase do projeto;
3. uma decisão substituiu a outra;
4. uma delas era apenas proposta.

## 11. Ausência da fonte primária

Quando houver referência consistente a uma decisão, mas a fonte original não estiver disponível, o registro poderá assumir provisoriamente a condição:

**DECISÃO REFERENCIADA — FONTE PRIMÁRIA NÃO LOCALIZADA**

Isso permite preservar a pista histórica sem transformá-la em fato definitivamente comprovado.

## 12. Regra de não promoção automática

Uma informação não deverá ganhar autoridade simplesmente por ter sido repetida muitas vezes.

Cinco referências posteriores derivadas da mesma informação não equivalem necessariamente a cinco evidências independentes.

A dependência entre fontes deverá ser registrada, evitando falsa corroboração.

## 13. Cadeia de proveniência

Para cada elemento histórico relevante, deverá ser buscada a seguinte cadeia:

**ID da decisão/evento  
↓  
fonte primária  
↓  
fontes corroborantes  
↓  
data/período  
↓  
interpretação histórica  
↓  
estado da decisão  
↓  
artefatos afetados  
↓  
implementação, quando existente  
↓  
estado atual**

Essa cadeia será posteriormente convertida em estrutura operacional na **Matriz de Rastreabilidade Histórica**.

---

## 14. Estados históricos

### 14.1. `PROPOSTO`

A fonte demonstra que determinada ideia, regra, estrutura ou alteração foi apresentada para consideração, sem evidência suficiente de aprovação.

### 14.2. `EM_DISCUSSÃO`

Há evidência de análise ativa da proposta, incluindo alternativas, objeções ou refinamentos, mas ainda sem decisão conclusiva.

### 14.3. `DECIDIDO`

Existe evidência explícita de aprovação.

Expressões como “Concordo”, “Opção A” ou “Vamos manter dessa forma” podem caracterizar `DECIDIDO`, desde que seja possível determinar inequivocamente qual proposição estava sendo aprovada.

O contexto é parte da evidência.

### 14.4. `FORMALIZADO`

A decisão foi incorporada a documento normativo, metodológico ou arquitetural reconhecido pelo projeto.

**DECIDIDO ≠ FORMALIZADO.**

### 14.5. `IMPLEMENTADO`

Há evidência de que a decisão passou a existir operacionalmente em código, workflow, processo, relatório ou mecanismo equivalente.

**DECIDIDO ≠ IMPLEMENTADO.**

### 14.6. `VALIDADO`

A implementação ou metodologia foi submetida ao teste ou processo de validação previsto e considerada aceitável segundo os critérios então aplicáveis.

Não deverá ser utilizado `VALIDADO` simplesmente porque algo “funcionou”. Deverá existir evidência de algum procedimento reconhecível de validação.

### 14.7. `SUPERADO`

A decisão existiu validamente, mas foi posteriormente substituída por outra.

O registro original não é apagado.

Deverá existir relação:

**RH-XXXX `SUPERADO_POR` RH-YYYY**

### 14.8. `REJEITADO`

A proposta foi explicitamente recusada.

Deverá permanecer no histórico quando sua existência for relevante para compreender escolhas arquiteturais ou metodológicas posteriores.

### 14.9. `ADIADO`

A decisão foi explicitamente postergada.

`ADIADO` significa que **a decisão de decidir posteriormente foi tomada**, e não ausência de decisão.

### 14.9.1. Decisões negativas explícitas

Uma decisão explícita de **não implementar, não incluir, não alterar, não criar ou não prosseguir** deverá ser tratada como evento histórico quando produzir consequência material para escopo, arquitetura, metodologia, implementação ou governança.

Decisão negativa não equivale a ausência de decisão.

### 14.10. `INDETERMINADO`

As evidências disponíveis não permitem estabelecer o estado histórico com segurança.

Não significa necessariamente que não houve decisão; significa que atualmente não é possível demonstrar qual foi a decisão.

## 15. Marcadores complementares

Algumas características não deverão ser tratadas como estados:

- `INFERIDO`: conclusão resultante de interpretação das evidências, e não de declaração explícita.
- `REFERENCIADO`: há menção posterior à existência da decisão, mas sua fonte primária ainda não foi localizada.
- `DIVERGENTE`: as fontes apresentam incompatibilidade material ainda não resolvida.

Esses elementos funcionam como **marcadores**, podendo coexistir com um estado.

## 16. Trajetória histórica de estados

A evolução de uma decisão deverá ser representada como trajetória datada, não apenas pelo último estado. Cada transição relevante deverá preservar, quando disponível, o estado, a data ou período e a evidência que a sustenta.

O campo **Trajetória Histórica** deverá coexistir com o campo **Estado atual**, evitando que decisão, implementação, validação ou supersessão ocorridas em momentos diferentes sejam comprimidas em um único rótulo.

Intervalos de latência entre estados deverão permanecer visíveis. Uma implementação posterior não desloca retroativamente a data da decisão que a originou.

Exemplos:

**PROPOSTO → EM_DISCUSSÃO → DECIDIDO → FORMALIZADO → IMPLEMENTADO → VALIDADO**

**PROPOSTO → DECIDIDO → ADIADO**

**DECIDIDO → IMPLEMENTADO → SUPERADO**

---

## 17. Grau de confiança da reconstrução

Deverá ser utilizada uma escala ordinal, evitando percentuais que transmitam precisão não sustentada pelas evidências.

### `C4 — COMPROVADO`

Evidência primária explícita e inequívoca, idealmente acompanhada por corroboração independente.

### `C3 — FORTEMENTE SUSTENTADO`

Evidência direta suficientemente clara para sustentar a reconstrução, embora a cadeia documental não esteja completa.

### `C2 — PARCIALMENTE SUSTENTADO`

Existem evidências relevantes, porém incompletas ou indiretas.

### `C1 — HIPÓTESE`

A reconstrução é plausível e possui algum indício documental, mas não existe evidência suficiente para tratá-la como fato histórico.

### `C0 — NÃO DETERMINÁVEL`

As fontes disponíveis não permitem reconstrução responsável.

## 18. Confiança não altera o estado

Estado histórico e confiança são dimensões independentes.

Podem existir, por exemplo:

**DECIDIDO — C4**

**DECIDIDO — C2**

**INDETERMINADO — C4**

## 19. Promoção e rebaixamento da confiança

O grau de confiança poderá mudar quando novas fontes forem incorporadas.

Exemplo:

**C1 → C2 → C3 → C4**

Também deverá ser permitido o movimento contrário quando nova evidência alterar a interpretação.

Toda alteração relevante deverá ser registrada, evitando reescrever silenciosamente a reconstrução.

## 20. Matriz básica

| Dimensão | Pergunta |
|---|---|
| Estado histórico | O que aconteceu? |
| Marcador | Há alguma condição especial? |
| Confiança | Quão bem conseguimos provar? |
| Fonte | Com base em quê? |
| Temporalidade | Quando aconteceu? |
| Relação | O que veio antes/depois? |
| Impacto | O que essa decisão afetou? |

## 21. Regra de consolidação

> **Somente registros com confiança C3 ou C4 poderão ser tratados como fatos históricos consolidados sem revisão adicional.**

Registros `C0`, `C1` ou `C2` continuam preservados, mas permanecem na camada de investigação/reconstrução.

---

## 22. Registro Histórico — RH

A unidade fundamental do protocolo será o **Registro Histórico (RH)**.

Cada decisão, alteração, proposta relevante, implementação ou outro evento sujeito à reconstrução deverá possuir um registro individual.

> **Um RH deve representar um evento que possa mudar de estado, ser rastreado ou ser referenciado independentemente dos demais.**

Uma única conversa poderá gerar diversos RHs, enquanto várias mensagens relacionadas à mesma decisão poderão produzir apenas um.

## 23. Identificador

Formato proposto:

**`RH-AAAA-NNNN`**

Exemplo:

`RH-2026-0047`

Onde:

- `RH` = Registro Histórico;
- `AAAA` = ano atribuído ao evento;
- `NNNN` = sequência do registro.

O identificador não deverá conter módulo, categoria ou estado.

O identificador `RH` somente deverá ser atribuído **após a conclusão do gate de validação do candidato**. Durante extração, confronto, fusão, desmembramento ou investigação, o evento deverá permanecer identificado como `CRH`.

Não deverá ser criado `RH` provisório para evento ainda não validado. Se o ano do evento permanecer indeterminado após o gate, a política de identificação aplicável deverá ser registrada sem comprometer a imutabilidade do identificador definitivo.

Uma vez atribuído, o identificador `RH` deverá permanecer imutável.

## 24. Data do evento × data da reconstrução

Deverão ser armazenadas separadamente:

- `event_date`: quando o evento histórico ocorreu;
- `recorded_at`: quando o RH foi criado durante a reconstrução.

Quando não houver precisão suficiente, `event_date` poderá registrar apenas ano/mês ou um intervalo, acompanhado da precisão temporal.

Quando a decisão ou evento possuir formação distribuída no tempo, poderão ser registrados adicionalmente:

- `event_start`: início conhecido do processo;
- `event_end`: encerramento conhecido do processo;
- `decision_date`: data da decisão, quando identificável;
- `temporal_precision`: exata, aproximada, intervalo ou desconhecida.

Esses campos não deverão ser artificialmente preenchidos quando a fonte não fornecer precisão suficiente.

## 25. Estrutura mínima do RH

| Campo | Função |
|---|---|
| `RH_ID` | Identificador permanente |
| `Título` | Descrição curta |
| `Data do evento` | Data/período reconstruído; pode incluir início, fim e data de decisão |
| `Precisão temporal` | Exata, aproximada, intervalo ou desconhecida |
| `Objeto` | Elemento do projeto afetado |
| `Descrição` | O que ocorreu |
| `Trajetória histórica` | Sequência datada de estados, quando aplicável |
| `Marcadores` | INFERIDO, REFERENCIADO etc. |
| `Confiança` | C0–C4 |
| `Fonte primária` | Evidência principal |
| `Fontes corroborantes` | Evidências adicionais |
| `Relações` | Outros RHs relacionados |
| `Impacto` | Elementos afetados |
| `Estado atual` | Situação da decisão hoje |
| `Observações` | Limitações ou contexto relevante |

## 26. Evidência textual

Além da referência à fonte, deverá ser preservado o **fragmento mínimo necessário para demonstrar a interpretação**.

Uma resposta isolada como “Concordo” não constitui evidência suficiente sem o objeto da concordância.

> **O contexto necessário à interpretação faz parte da evidência.**

Ao mesmo tempo, blocos extensos de conversas não deverão ser duplicados dentro do RH. O registro deverá apontar para a fonte original.

## 27. Referência de fonte

As fontes deverão possuir identificadores próprios:

**`SRC-XXXX`**

Exemplo:

`SRC-0017`

O catálogo de fontes poderá registrar:

- identificador;
- tipo;
- título;
- data;
- formato;
- localização;
- estado de integridade.

Um RH deverá referenciar o `SRC`, evitando dependência de nomes de arquivos potencialmente mutáveis.

## 28. Localização interna da evidência

A referência deverá ser mais específica que apenas o arquivo.

Exemplos:

- Markdown: `SRC-0017:L245-L267`
- Documento: `SRC-0021:§4.3`
- Git: `SRC-0042:<commit-hash>`
- Código: `SRC-0048:datafeed.py:L110-L143`

Quando a fonte possuir identificadores estruturais nativos e estáveis, estes deverão constituir o **localizador primário** da evidência. Localizadores auxiliares poderão incluir timestamp, posição sequencial, página ou linha de derivado de trabalho.

Ordem preferencial:

**identificador estrutural nativo → localização estrutural interna → timestamp/posição → linha de derivado de trabalho**

Exemplo para exportação estruturada de conversa:

`SRC-0001 | node_id:<UUID> | timestamp:<data-hora>`

## 29. Relações entre RHs

Os registros deverão formar um **grafo histórico**, e não apenas uma lista cronológica.

Relações iniciais:

- `DERIVA_DE`
- `REFINA`
- `IMPLEMENTA`
- `FORMALIZA`
- `VALIDA`
- `CONTRADIZ`
- `SUBSTITUI`
- `SUPERADO_POR`
- `DEPENDE_DE`
- `RELACIONADO_A`

Exemplos:

`RH-2026-0048 REFINA RH-2026-0042`

`RH-2026-0053 IMPLEMENTA RH-2026-0048`

`RH-2026-0071 SUBSTITUI RH-2026-0048`

## 30. Relação com módulos e documentos

Cada RH deverá poder apontar para mais de um objeto, módulo, documento ou componente afetado.

Não deverá existir limitação de um único módulo por registro.

## 31. Estado histórico × estado atual

Esses campos deverão permanecer separados.

Uma regra aprovada em determinado momento e posteriormente substituída poderá registrar:

- **Estado histórico:** `DECIDIDO`
- **Estado atual:** `SUPERADO`

A trajetória completa será representada pelas relações entre RHs.

## 32. Exemplo simplificado

```text
RH_ID: RH-2026-0047

Título:
Inclusão da OKX entre exchanges de verificação

Data do evento:
2026-06

Objeto:
Ranking Institucional Simplificado

Descrição:
Ampliação do conjunto de exchanges utilizado para verificação
de mercados futuros.

Estado histórico:
DECIDIDO

Marcadores:
—

Confiança:
C3

Fonte primária:
SRC-0017

Evidência:
[localização precisa na conversa]

Relações:
REFINA RH-2026-0038

Impacto:
Critério de elegibilidade / verificação de futures

Estado atual:
VIGENTE

Observações:
Verificar formalização posterior no documento metodológico.
```

O exemplo é ilustrativo. Um registro real somente deverá ser criado após exame da fonte original.

## 33. Registro não equivale a decisão

Nem todo RH representará uma decisão.

Categorias iniciais:

- `DEC` — decisão;
- `REQ` — requisito;
- `MET` — definição metodológica;
- `ARC` — arquitetura;
- `IMP` — implementação;
- `TST` — teste/validação;
- `GOV` — governança;
- `PEN` — pendência;
- `DOC` — evento documental.

A categoria deverá ser um **campo do RH**, não parte do identificador.

## 34. Imutabilidade e correção

Uma vez criado, o RH não deverá ser silenciosamente reescrito.

Correções relevantes deverão registrar:

- valor anterior;
- valor novo;
- data;
- motivo;
- evidência que provocou a alteração.

Isso constituirá o **audit trail da própria reconstrução**.

## 35. Não duplicação

Antes de criar um RH, deverá ser verificado se o evento já possui registro.

Como regra:

> **1 evento + N fontes = 1 RH.**

Registros separados somente deverão ser criados quando existirem eventos historicamente distintos.

## 36. Três níveis de armazenamento

A estrutura deverá distinguir três artefatos:

### Catálogo de Fontes — `SRC`

Responde: **De onde vieram as evidências?**

### Registro Mestre Histórico — `RH`

Responde: **O que aconteceu?**

### Matriz de Rastreabilidade — `MRT`

Responde: **Como decisões, fontes, módulos, documentos e implementações se relacionam?**

Estrutura conceitual:

**SRC → RH → MRT**

## 37. Consequência arquitetural

A reconstrução histórica passa a constituir um **sistema de proveniência documental**, e não apenas um relatório narrativo.

Fluxo conceitual:

**Fonte  
→ Evidência  
→ Evento histórico  
→ Relações  
→ Decisão/metodologia  
→ Documento  
→ Implementação  
→ Estado atual**

Esse modelo poderá servir futuramente como base para automação parcial da auditoria documental do CRYPTO PRO SUITE.

---

## 38. Procedimento Operacional de Reconstrução Histórica

### 38.1. Finalidade operacional

O procedimento estabelece a sequência obrigatória para transformar fontes históricas dispersas em registros rastreáveis e auditáveis.

Fluxo-base:

**Inventariar → Registrar → Examinar → Extrair → Confrontar → Classificar → Validar → Registrar RH → Relacionar → Consolidar**

Princípio operacional:

> **A reconstrução parte das fontes e chega às conclusões; nunca parte da conclusão desejada em busca de evidências que a confirmem.**

### 38.2. Fase 1 — Inventário das fontes

Antes da reconstrução de determinado domínio, deverão ser identificadas as fontes potencialmente relevantes.

Exemplos:

- conversas exportadas;
- documentos MD/DOCX;
- arquivos do GitHub;
- histórico Git;
- código;
- workflows;
- relatórios;
- planilhas;
- snapshots;
- logs.

Não será necessário inventariar todo o CRYPTO PRO SUITE antes de começar. O inventário poderá ser feito **por domínio de reconstrução**, tornando o processo incremental.

### 38.3. Fase 2 — Registro no Catálogo de Fontes

Cada fonte relevante receberá um identificador `SRC`.

Exemplo:

`SRC-0001`

O registro deverá conter pelo menos:

**ID | título | tipo | data/período | origem | localização | integridade | observações**

Nesse momento ainda não são extraídas decisões; apenas se estabelece a proveniência.

### 38.4. Fase 3 — Preservação da fonte

A fonte utilizada na reconstrução deverá permanecer preservada em sua forma original sempre que possível.

Versões processadas poderão ser criadas para facilitar a análise, mas deverá existir relação explícita:

**fonte original → derivado de trabalho**

Quando a fonte possuir estrutura lógica nativa — como relações de ancestralidade, sequência, versão, ramificação, `mapping` ou `current_node` — essa estrutura deverá ser preservada e considerada na reconstrução.

> **A estrutura nativa da fonte prevalece sobre ordenação cronológica simples quando ela representar de maneira mais fiel a sequência histórica efetiva.**

### 38.5. Fase 4 — Leitura orientada a eventos

A análise da fonte não deverá simplesmente resumir seu conteúdo. Deverá procurar **eventos historicamente relevantes**.

Perguntas operacionais:

- Foi feita uma proposta?
- Foi tomada uma decisão?
- Uma decisão anterior foi alterada?
- Foi definido um requisito?
- Foi estabelecida uma metodologia?
- Algo foi explicitamente rejeitado ou adiado?
- Foi tomada decisão explícita de não incluir, não criar, não alterar ou não prosseguir?
- Foi realizada uma implementação?
- Houve teste ou validação?
- Foi identificada uma pendência?
- Um documento foi criado ou alterado em consequência disso?

Cada resposta potencialmente relevante gera um **candidato a RH**.

### 38.6. Fase 5 — Extração de candidatos

Antes da criação definitiva de RHs, os eventos identificados deverão entrar em uma área intermediária:

**Candidatos a Registro Histórico — CRH**

Exemplo:

`CRH-00023`

O candidato conterá:

- fonte;
- localização;
- trecho relevante;
- evento identificado;
- classificação preliminar;
- observações.

O `CRH` é temporário. Após análise poderá:

**virar RH → ser fundido com outro CRH → ser descartado → permanecer pendente**

### 38.7. Fase 6 — Contextualização

O candidato deverá ser interpretado no contexto necessário.

Respostas curtas como “Concordo”, “Perfeito”, “Opção A” ou “Pode seguir” não deverão ser classificadas isoladamente como decisão sem identificação precisa da proposição à qual respondem.

O trecho contextual necessário passa a integrar a evidência.

### 38.8. Fase 7 — Busca de corroboração

Antes da consolidação, deverão ser procuradas outras evidências relacionadas ao evento.

Exemplo:

**Conversa → decisão**  
**Outra conversa → referência posterior**  
**Documento → formalização**  
**GitHub → implementação**

A busca deverá considerar evidências favoráveis e contraditórias, evitando viés de confirmação.

### 38.9. Fase 8 — Detecção de duplicidade

Antes de criar um RH, deverá ser verificado se o evento já está registrado.

**novo documento ≠ novo evento**

**nova evidência ≠ novo RH**

Se o evento já existir, a nova fonte deverá ser adicionada ao RH correspondente.

### 38.10. Fase 9 — Resolução de conflitos

Caso as fontes sejam incompatíveis, aplicam-se as regras de conflito estabelecidas neste protocolo.

O evento não deverá ser artificialmente consolidado. Poderá receber o marcador `DIVERGENTE` e permanecer em investigação.

Quando existirem eventos historicamente distintos, poderão ser criados RHs separados, preservando a cadeia:

**decisão original → decisão posterior → supersessão**

### 38.11. Fase 10 — Classificação histórica

Somente após contextualização e confronto das fontes serão atribuídos:

- **Categoria:** DEC, MET, REQ, ARC etc.;
- **Estado histórico:** PROPOSTO, DECIDIDO, ADIADO etc.;
- **Marcadores:** INFERIDO, REFERENCIADO, DIVERGENTE;
- **Confiança:** C0–C4.

Princípio:

> **Não se classifica antes de investigar.**

### 38.12. Fase 11 — Criação do RH

O identificador RH somente será criado depois que o candidato tiver concluído contextualização, confronto, verificação de duplicidade, análise de granularidade, classificação e validação.

Fluxo obrigatório:

**Fonte → evidência → CRH → contextualização → corroboração/conflito → granularidade → classificação → validação → RH definitivo → MRT**

Exemplo:

`CRH-00023 → [gate aprovado] → RH-2026-0047`

O candidato deverá conservar referência ao RH resultante para manutenção do audit trail. CRHs fundidos, desmembrados, descartados ou mantidos em investigação também deverão preservar seu histórico de tratamento.

### 38.13. Fase 12 — Construção das relações

O novo RH será confrontado com registros existentes para identificação de relações como:

- `DERIVA_DE`
- `REFINA`
- `IMPLEMENTA`
- `FORMALIZA`
- `VALIDA`
- `CONTRADIZ`
- `SUBSTITUI`
- `SUPERADO_POR`
- `DEPENDE_DE`
- `RELACIONADO_A`

Esse processo transforma registros isolados em **cadeias decisórias**.

### 38.14. Fase 13 — Impacto documental e técnico

Para cada RH relevante deverá ser identificado quais partes do CRYPTO PRO SUITE foram afetadas.

Poderão ser relacionados:

- módulos;
- documentos;
- metodologias;
- código;
- Data Feed;
- indicadores;
- relatórios;
- processos de governança.

Essas relações alimentarão a Matriz de Rastreabilidade Histórica.

### 38.15. Fase 14 — Validação da reconstrução

Antes da consolidação, deverá ser executado o seguinte checklist mínimo:

- Fonte identificada?
- A fonte citada comprova este evento específico, ou o conhecimento provém de outra fonte?
- Evidência localizável?
- Contexto suficiente?
- Evento individualizado?
- Duplicidade verificada?
- Fontes contraditórias pesquisadas?
- Estado histórico justificado?
- Confiança compatível com a evidência?
- Relações identificadas?
- Impactos registrados?

Somente depois disso o RH poderá ser considerado validado pelo processo de reconstrução.

A validação do registro histórico não equivale à validação técnica da metodologia descrita nele.

### 38.16. Fase 15 — Consolidação

Os candidatos validados com confiança `C3` e `C4` poderão ser promovidos a RH e integrar o **Histórico Consolidado**.

Itens `C0`, `C1` e `C2` permanecerão, em regra, como `CRH` e/ou no `RPD`, preservados na camada de investigação. Exceções deverão ser justificadas quando for necessário registrar formalmente uma divergência histórica.

Assim deverão coexistir:

- **Histórico Consolidado**
- **Reconstrução Pendente**

As incertezas não deverão ser apagadas para produzir uma narrativa artificialmente completa.

## 39. Processamento incremental

Não será necessário reconstruir todo o projeto de uma vez.

A unidade prática recomendada será:

**domínio → fontes → reconstrução → validação → consolidação**

A ordem dos domínios deverá ser definida conforme necessidade, dependências e disponibilidade das fontes.

## 40. Reabertura

Nenhum domínio será considerado historicamente imutável.

Nova evidência poderá exigir:

**reabertura → reavaliação → alteração de confiança → novo RH ou correção controlada → atualização das relações**

Qualquer alteração deverá preservar o audit trail.

## 41. Papel da memória durante a execução

A memória contextual poderá orientar a localização de possíveis decisões, conversas e documentos.

Não poderá, isoladamente, transformar uma lembrança contextual em decisão histórica comprovada.

Toda afirmação histórica consolidada deverá respeitar os requisitos de evidência estabelecidos neste protocolo.

## 42. Saídas do processo

A execução do protocolo deverá produzir quatro artefatos principais:

### 42.1. Catálogo de Fontes — `SRC`

Inventário controlado das evidências.

### 42.2. Registro Mestre Histórico — `RH`

Base dos eventos reconstruídos.

### 42.3. Matriz de Rastreabilidade Histórica — `MRT`

Relações entre fontes, eventos, módulos, documentos e implementação.

### 42.4. Registro de Pendências e Divergências — `RPD`

Repositório dos itens C0–C2, conflitos, fontes ausentes, questões ainda não resolvidas e incidentes detectados no próprio processo de reconstrução.

O RPD poderá registrar, entre outros:

- divergência histórica;
- fonte primária ausente;
- insuficiência de evidência;
- conflito não resolvido;
- incidente de reconstrução, incluindo erro de proveniência, classificação ou consolidação detectado durante a auditoria.

## 43. Critério de encerramento de um domínio

Um domínio poderá ser declarado **RECONSTRUÍDO** quando:

- as fontes relevantes conhecidas tiverem sido examinadas;
- os eventos materiais tiverem RH;
- duplicidades tiverem sido tratadas;
- divergências conhecidas estiverem resolvidas ou explicitamente registradas no RPD;
- as principais cadeias decisórias estiverem representadas;
- os impactos documentais estiverem identificados;
- nenhuma lacuna conhecida comprometer materialmente a compreensão da evolução do domínio.

`RECONSTRUÍDO` não significa história absolutamente completa.

Significa:

> **Reconstrução suficientemente sustentada, rastreável e auditável segundo o protocolo.**

## 44. Gate de reconstrução

Antes de utilizar a reconstrução para corrigir ou consolidar documentação oficial, deverá ser aplicado o seguinte gate:

**Fonte → RH → confiança ≥ C3 → rastreabilidade → revisão → incorporação documental**

Esse gate estabelece uma separação formal entre:

**descobrir o passado**

e

**alterar a documentação vigente**

e reduz o risco de propagação de erros históricos.

---

## 45. Estado de desenvolvimento deste protocolo

Esta consolidação cobre as cinco etapas metodológicas do protocolo e incorpora os ajustes derivados de sua primeira aplicação prática controlada.

O documento permanece com status de **Documento de Trabalho**, sem atribuição de versão formal.

## 46. Validação Experimental — Piloto 01

### 46.1. Fonte e domínio

O **Piloto 01** aplicou o protocolo à fonte `SRC-0001 — Análise de Criptomoedas`, utilizando a exportação estruturada original como fonte deliberativa primária.

O domínio foi delimitado à gênese e evolução dos elementos do CRYPTO PRO SUITE efetivamente demonstráveis pela fonte, com ênfase no padrão PRO e no desenvolvimento do Crypto Pro Data Feed.

### 46.2. Resultados metodológicos

A aplicação percorreu o ciclo:

**fonte → inventário → leitura orientada a eventos → CRH → confronto → correção de granularidade → MRT → gate de promoção → RH**

O piloto também detectou e corrigiu um incidente de proveniência no qual conhecimento oriundo de outras partes do projeto havia sido atribuído indevidamente a `SRC-0001`. O incidente deverá permanecer registrado no RPD como evidência do funcionamento autocorretivo do protocolo.

### 46.3. Ajustes incorporados

O Piloto 01 resultou nos seguintes aperfeiçoamentos metodológicos:

1. preservação da estrutura lógica nativa da fonte e prevalência dessa estrutura sobre ordenação cronológica simples quando aplicável;
2. materialização da trajetória histórica como sequência datada de estados;
3. reconhecimento de decisões negativas explícitas como eventos históricos;
4. preservação dos intervalos de latência entre decisão, implementação, validação e outros estados;
5. representação do período de formação de eventos por início, fim, data de decisão e precisão temporal quando suportados pela fonte;
6. validação da proveniência independentemente da veracidade conhecida da informação;
7. atribuição de identificador RH somente após aprovação no gate de validação;
8. preferência por identificadores estruturais nativos como localizadores primários da evidência;
9. ampliação do RPD para registrar incidentes do próprio processo de reconstrução.

### 46.4. Consequência operacional

As próximas fontes deverão ser processadas segundo o protocolo já revisado pelos achados do Piloto 01.

A próxima atividade prevista é selecionar e registrar `SRC-0002`, aplicando a versão revisada do procedimento antes de qualquer nova consolidação histórica em escala maior.
