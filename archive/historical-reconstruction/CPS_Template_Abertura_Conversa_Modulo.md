# CRYPTO PRO SUITE — Template de Abertura de Conversa por Módulo

**Status:** Artefato operacional  
**Finalidade:** Inicialização controlada de novas conversas de trabalho por módulo, componente, documento ou domínio do CRYPTO PRO SUITE.

---

Esta conversa será dedicada ao desenvolvimento do domínio:

**[NOME DO MÓDULO / COMPONENTE / DOCUMENTO]**

do projeto **CRYPTO PRO SUITE**.

O projeto possui documentação persistida, histórico reconstruído e mecanismos formais de rastreabilidade. O contexto disponível no ChatGPT poderá ser utilizado para orientação, mas as decisões anteriores relevantes para este trabalho deverão ser verificadas na documentação persistida.

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
- novas decisões tomadas nesta conversa deverão ser claramente diferenciadas de decisões históricas recuperadas.

## 2A. Freshness Gate

Antes de concluir a recuperação do contexto específico e iniciar o Diagnóstico de Partida:

1. Verifique em `archive/historical-reconstruction/README.md` o checkpoint atual da reconstrução, incluindo:
   - o maior identificador `RH` registrado;
   - o intervalo de `SRC` catalogado;
   - os `RPD` ainda abertos ou recentemente resolvidos que possam afetar o domínio.

2. Confirme que `HISTORICAL_REGISTER.md` e `TRACEABILITY_MATRIX.md` foram examinados até esse checkpoint, e não apenas por busca temática ou por ocorrências do nome do módulo.

3. Considere também decisões recentes que afetem o domínio por interface, dependência ou limite de escopo, mesmo quando o respectivo RH esteja titulado sob outro módulo ou componente upstream/downstream.

4. Se um intervalo recente de RHs não for considerado materialmente relevante ao domínio, registre explicitamente essa exclusão e sua justificativa no Diagnóstico de Partida.

5. Não conclua o Diagnóstico de Partida com uma faixa de RHs inferior ao checkpoint vigente sem explicar documentalmente por que os registros posteriores não afetam o domínio.

## 3. Diagnóstico de partida

Antes de produzir ou modificar documentação normativa, apresente um **Diagnóstico de Partida do Domínio**, contendo:

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

## 4. Classificação do diagnóstico

Ao final, organize as conclusões em:

**A. Base documental consolidada**

Elementos suficientemente sustentados para serem utilizados como premissas do trabalho.

**B. Elementos específicos ou condicionais**

Definições válidas apenas para determinado submódulo, cenário, período ou condição.

**C. Lacunas, divergências e decisões pendentes**

Elementos que não podem ser tratados como resolvidos.

**D. Próxima etapa proposta**

A ação que decorre do estado documental encontrado, sem antecipar decisões ainda não tomadas.

## 5. Gate de início

Não inicie automaticamente a elaboração normativa, alteração metodológica ou modificação de documentos existentes.

Primeiro apresente o **Diagnóstico de Partida** para revisão.

Após sua revisão, o trabalho poderá prosseguir a partir da base documental validada nesta conversa.
