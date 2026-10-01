# Ranking Institucional Simplificado — Backlog Operacional

**Status:** artefato operacional não normativo  
**Finalidade:** registrar assuntos deliberadamente adiados para tratamento posterior, sem convertê-los em decisões metodológicas finais.

## BL-RANK-001 — Critical Event Watch / Interim Methodological Update

**Status:** Adiado para especificação posterior  
**Origem:** desenvolvimento da Etapa 38 — Freshness, cadence e triggers de reavaliação  
**Escopo:** Ranking Institucional Simplificado / operação da CRYPTO PRO SUITE

### Premissa já acordada

A versão inicial da CRYPTO PRO SUITE terá **execução oficial semanal**.

Além dessa execução, ficou conceitualmente aceita a possibilidade de uma camada leve de vigilância entre execuções, destinada exclusivamente a detectar eventos extraordinários capazes de tornar materialmente desatualizada ou inválida alguma conclusão vigente da Suite.

### Arquitetura candidata

- **Weekly Run:** execução metodológica oficial e coordenada da Suite.
- **Critical Event Watch:** monitoramento leve, potencialmente diário, sem reexecutar toda a Suite.
- **Interim Methodological Update:** saída excepcional produzida somente quando um evento ultrapassar threshold elevado de materialidade.
- O watch não deve ser confundido com execução diária da Suite.

### Respostas candidatas a eventos

1. **Monitor** — registrar e aguardar a próxima execução semanal.
2. **Partial Reassessment** — reavaliar apenas ativo, Vetor, constructo, Friction e comparações afetadas.
3. **Critical Invalidation** — sinalizar imediatamente que parte da classificação vigente deixou de ser metodologicamente válida, sem aguardar o próximo Weekly Run.

### Eventos candidatos

Exemplos a avaliar futuramente:
- exploit ou falha técnica grave;
- perda/obtenção material de acesso institucional;
- delisting ou suspensão operacional relevante;
- decisão regulatória material;
- alteração extraordinária de tokenomics ou supply;
- unlock material;
- lançamento/encerramento de produto institucional importante;
- mudança extraordinária da estrutura de liquidez;
- alteração upstream material de Flow Vector.

Movimento de preço isolado e sinais de análise técnica não constituem, por si só, trigger metodológico do Ranking.

### Questões pendentes

- definir cadência exata do Critical Event Watch;
- definir universo de fontes;
- definir thresholds de materialidade;
- definir regras formais de Monitor / Partial Reassessment / Critical Invalidation;
- definir formato e validade de um Interim Methodological Update;
- definir propagação entre módulos;
- definir integração com automação/datafeed;
- definir auditoria e lifecycle até a consolidação no Weekly Run seguinte.

### Regra de escopo

Este item permanece **backlog**. Sua inclusão aqui não formaliza a implementação do Critical Event Watch nem do Interim Methodological Update na versão inicial da Suite.


## BL-RANK-002 — Supported Market Universe e governança de fontes do Data Feed

**Status:** Adiado para especificação conjunta com o Crypto Pro Data Feed  
**Origem:** revisão da Etapa 39 — Eligibility Geral / universo operacional  
**Escopo:** interface Ranking Institucional Simplificado ↔ Crypto Pro Data Feed

### Decisão de arquitetura em nível de trabalho

O Ranking Geral não deve pressupor a varredura exaustiva do universo global de criptoativos. A execução deverá partir de um **Supported Market Universe** construído a partir das fontes de mercado aprovadas e suportadas pelo Crypto Pro Data Feed na versão vigente.

Esse universo representa **cobertura do produto**, não mérito do ativo nem definição permanente do universo econômico de criptoativos.

### Requisito futuro do Data Feed

A seleção das fontes deverá ser justificada por critérios objetivos compatíveis com uma oferta comercial da CRYPTO PRO SUITE, incluindo, no mínimo:
- cobertura de ativos e mercados;
- relevância e qualidade de mercado;
- disponibilidade e granularidade dos dados requeridos pelos módulos;
- estabilidade e limites das APIs;
- confiabilidade operacional;
- facilidade de canonicalização e identificação de ativos/mercados;
- disponibilidade histórica;
- custo;
- continuidade da fonte;
- termos de uso, direitos de uso comercial, armazenamento e eventual redistribuição dos dados.

APIs gratuitas não devem ser presumidas como automaticamente aptas a uso ou redistribuição comercial.

### Fronteira CEX e descoberta de ativos emergentes

Grandes CEXs podem fornecer uma fronteira operacional eficiente e auditável para a versão inicial, mas não devem ser presumidas como universo econômico completo. Ativos novos ou de alto potencial podem surgir fora das grandes CEXs. A arquitetura deve permanecer extensível a outras fontes aprovadas, inclusive DEXs, venues institucionais ou outras infraestruturas de mercado, caso os requisitos metodológicos e comerciais o justifiquem.

### Dependências futuras

- formalizar o Supported Market Universe por versão;
- definir Approved Market Sources e política de source governance;
- definir política de canonical market/venue para o Asset PRO;
- avaliar se Capacity/Absorption requer dados multi-venue;
- definir Data Sufficiency Gate por módulo e por tipo de dado;
- criar processo de Data Coverage Expansion Request quando um ativo relevante ficar fora da cobertura vigente.

### Regra de escopo

Este item registra uma dependência e uma direção arquitetural. Não fixa ainda Binance, Bybit, Bitget, MEXC, OKX ou qualquer outro conjunto de fontes como seleção definitiva para a versão comercial do Data Feed.
