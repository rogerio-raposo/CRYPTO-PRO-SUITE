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
