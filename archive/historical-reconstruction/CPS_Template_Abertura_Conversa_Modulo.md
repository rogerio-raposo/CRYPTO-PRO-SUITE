# CRYPTO PRO SUITE — Template de Abertura e Continuidade de Conversa por Módulo

**Status:** Artefato operacional  
**Finalidade:** Inicialização controlada de novas conversas e retomada controlada de conversas interrompidas por módulo, componente, documento ou domínio do CRYPTO PRO SUITE.

---

Esta conversa será dedicada ao desenvolvimento do domínio:

**[NOME DO MÓDULO / COMPONENTE / DOCUMENTO]**

do projeto **CRYPTO PRO SUITE**.

O projeto possui documentação persistida, histórico reconstruído e mecanismos formais de rastreabilidade. O contexto disponível no ChatGPT poderá ser utilizado para orientação, mas as decisões anteriores relevantes para este trabalho deverão ser verificadas na documentação persistida.

Este template possui dois modos operacionais:

- **Modo Partida:** quando não existe handoff/checkpoint válido da conversa anterior;
- **Modo Continuidade:** quando existe handoff/checkpoint válido e o objetivo é retomar trabalho já diagnosticado e parcialmente desenvolvido.

---

## 1. Recuperação do contexto específico

Antes de iniciar desenvolvimento, revisão ou alteração:

1. Consulte o repositório `rogerio-raposo/CRYPTO-PRO-SUITE`, branch `main`.

2. Identifique e examine os documentos atualmente existentes relacionados a:

   **[NOME DO DOMÍNIO]**

   especialmente em:

   **[CAMINHO PRINCIPAL NO REPOSITÓRIO]**

3. Consulte os documentos superiores de governança, arquitetura ou metodologia somente na extensão necessária para determinar requisitos, limites, dependências e autoridade documental aplicáveis ao domínio.

4. Consulte `archive/historical-reconstruction/` para recuperar decisões históricas relevantes, utilizando conforme necessário:
   - `README.md`;
   - `SOURCE_CATALOG.md`;
   - `HISTORICAL_REGISTER.md`;
   - `TRACEABILITY_MATRIX.md`;
   - `PENDING_DIVERGENCES.md`;
   - `CPS_Protocolo_Reconstrucao_Historica_Rastreabilidade_Working_Draft_Piloto01.md`.

5. Identifique os `RH`, `SRC` e `RPD` diretamente relacionados ao domínio desta conversa.

6. Consulte as fontes preservadas em `archive/historical-sources/` quando for necessário verificar proveniência, contexto, evolução, conflito ou significado de uma decisão.

7. **Se estiver em Modo Continuidade**, localize e leia integralmente no próprio repositório o handoff/checkpoint mais recente indicado para o domínio antes de concluir o diagnóstico. O handoff deve ser tratado como estado de trabalho validado da conversa anterior, mas não substitui a documentação persistida nem a reconstrução histórica como fonte de verdade.

---

## 2. Regras de continuidade

Durante todo o trabalho:

- memória do ChatGPT poderá orientar buscas, mas não constituirá evidência histórica;
- não preencha lacunas documentais por inferência;
- não transforme propostas anteriores em decisões sem evidência;
- preserve a distinção entre decisões vigentes, superadas, rejeitadas, adiadas e ainda indeterminadas;
- preserve a proveniência das definições utilizadas;
- diferencie regras gerais de regras específicas de submódulos ou casos particulares;
- não generalize automaticamente uma metodologia específica para outros domínios;
- não corrija silenciosamente divergências entre fontes;
- respeite a hierarquia e a autoridade contextual dos documentos;
- não atribua versão formal, status normativo ou aprovação a um artefato sem base documental ou decisão explícita;
- novas decisões tomadas nesta conversa deverão ser claramente diferenciadas de decisões históricas recuperadas;
- **em Modo Continuidade, não refaça automaticamente trabalho já validado no handoff, salvo quando nova evidência, conflito documental, mudança de autoridade ou decisão posterior exigir reabertura.**

---

## 2A. Freshness Gate

Antes de concluir a recuperação do contexto específico e iniciar o diagnóstico:

1. Verifique em `archive/historical-reconstruction/README.md` o checkpoint atual da reconstrução, incluindo:
   - o maior identificador `RH` registrado;
   - o intervalo de `SRC` catalogado;
   - os `RPD` ainda abertos ou recentemente resolvidos que possam afetar o domínio.

2. Confirme que `HISTORICAL_REGISTER.md` e `TRACEABILITY_MATRIX.md` foram examinados até esse checkpoint, e não apenas por busca temática ou por ocorrências do nome do módulo.

3. Considere também decisões recentes que afetem o domínio por interface, dependência ou limite de escopo, mesmo quando o respectivo RH esteja titulado sob outro módulo ou componente upstream/downstream.

4. Se um intervalo recente de RHs não for considerado materialmente relevante ao domínio, registre explicitamente essa exclusão e sua justificativa no diagnóstico.

5. Não conclua o diagnóstico com uma faixa de RHs inferior ao checkpoint vigente sem explicar documentalmente por que os registros posteriores não afetam o domínio.

6. **Em Modo Continuidade, compare o checkpoint temporal/documental do handoff com o estado atual da branch `main` e identifique alterações posteriores materialmente relevantes.**

---

## 3. Diagnóstico

### 3.1 Modo Partida — Diagnóstico de Partida do Domínio

Quando não houver handoff válido, antes de produzir ou modificar documentação normativa, apresente um **Diagnóstico de Partida do Domínio**, contendo:

- finalidade e posição do domínio dentro do CRYPTO PRO SUITE;
- documentos atualmente existentes;
- definições e decisões já consolidadas;
- requisitos superiores aplicáveis;
- dependências com outros módulos ou componentes;
- decisões históricas relevantes ainda vigentes;
- decisões superadas relevantes para compreender o estado atual;
- propostas ou decisões adiadas;
- divergências e RPDs relacionados;
- lacunas documentais conhecidas;
- fontes ainda necessárias, se houver;
- estado atual de maturidade do domínio;
- ponto seguro de retomada.

Para cada conclusão material, indique sua base documental.

### 3.2 Modo Continuidade — Diagnóstico de Continuidade

Quando houver handoff/checkpoint válido, substitua a reconstrução integral por uma **validação incremental**, contendo:

**A. Base do handoff confirmada**  
Quais decisões, definições, fronteiras, pendências e ponto de retomada permanecem compatíveis com a documentação atual.

**B. Alterações ou evidências posteriores ao checkpoint**  
Novos RH/SRC/RPD, arquivos alterados, decisões posteriores ou mudanças de autoridade documental que afetem o domínio.

**C. Divergências, impactos e pendências**  
Conflitos entre o handoff e a documentação atual, itens que exigem reabertura e questões ainda indeterminadas.

**D. Ponto exato de retomada**  
Etapa a partir da qual o trabalho pode continuar sem repetir desnecessariamente etapas já validadas.

Se não houver alteração material, registre explicitamente que o handoff permanece válido.

---

## 4. Classificação do diagnóstico

No **Modo Partida**, organize as conclusões em:

**A. Base documental consolidada**  
Elementos suficientemente sustentados para serem utilizados como premissas do trabalho.

**B. Elementos específicos ou condicionais**  
Definições válidas apenas para determinado submódulo, cenário, período ou condição.

**C. Lacunas, divergências e decisões pendentes**  
Elementos que não podem ser tratados como resolvidos.

**D. Próxima etapa proposta**  
A ação que decorre do estado documental encontrado, sem antecipar decisões ainda não tomadas.

No **Modo Continuidade**, utilize a classificação incremental definida na seção 3.2.

---

## 5. Gate de início

Não inicie automaticamente a elaboração normativa, alteração metodológica ou modificação de documentos existentes.

Primeiro apresente o diagnóstico correspondente ao modo utilizado para revisão.

Após sua revisão:

- no **Modo Partida**, o trabalho poderá prosseguir a partir da base documental validada;
- no **Modo Continuidade**, o trabalho poderá prosseguir do ponto exato de retomada confirmado no handoff.

---

## 6. Handoff / Checkpoint de continuidade

Quando uma conversa precisar ser encerrada antes da conclusão do domínio, gere ou atualize um handoff contendo, no mínimo:

- escopo da conversa;
- fontes consideradas e fontes explicitamente excluídas;
- decisões tomadas;
- hipóteses de trabalho ainda não normativas;
- decisões superadas durante a própria conversa;
- fronteiras com outros módulos;
- constructos e definições correntes;
- divergências e pendências;
- questões abertas;
- ponto exato de retomada;
- data/checkpoint;
- prompt mínimo de abertura para o próximo chat.

O handoff:

- **não é documento normativo**;
- **não substitui** documentos oficiais;
- **não substitui** a reconstrução histórica;
- funciona como checkpoint operacional entre conversas;
- deve ser versionado ou substituído de forma rastreável quando um checkpoint mais recente for produzido.

---

## 7. Prompt mínimo para o usuário

### Sem handoff

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **Modo Partida** para iniciar esta conversa, que será dedicada ao **[NOME DO MÓDULO / DOMÍNIO / DOCUMENTO]**.

### Com handoff

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **Modo Continuidade** para iniciar esta conversa, que será dedicada ao **[NOME DO MÓDULO / DOMÍNIO / DOCUMENTO]**. Considere também o handoff/checkpoint mais recente armazenado no repositório em **[CAMINHO DO HANDOFF NO REPOSITÓRIO]**.

---

## 8. Hierarquia operacional

`Template canônico → documentação persistida / reconstrução histórica → handoff mais recente → diagnóstico → retomada controlada`

Essa é a lógica única de abertura e continuidade.