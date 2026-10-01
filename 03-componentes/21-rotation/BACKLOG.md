# Capital Rotation PRO — Backlog Metodológico

**Status:** artefato operacional não normativo  
**Finalidade:** registrar questões deliberadamente adiadas para revisão futura do módulo, sem convertê-las em decisões metodológicas finais.

## BL-ROT-001 — Rotação intramercado cripto e interface com o CSM do Asset PRO

**Status:** Avaliação metodológica futura  
**Origem:** desenvolvimento da Metodologia Geral do Asset PRO — 2026-10-01  
**Escopo:** Capital Rotation PRO ↔ Asset PRO

### Contexto

Durante o desenvolvimento da Metodologia Geral do Asset PRO, foi identificada a necessidade de distinguir a estrutura técnica própria do ativo do **Contexto Sistêmico de Mercado (CSM)** em que essa estrutura ocorre.

Para o Asset PRO, o CSM deverá atuar como contexto externo de interpretação e, quando a Suite estiver sendo executada de forma integrada, deverá consumir prioritariamente informação produzida pelo Capital Rotation PRO, em vez de reconstruir internamente uma análise completa de rotação de capital.

### Questão a avaliar no Capital Rotation PRO

Na próxima revisão metodológica do Capital Rotation PRO, avaliar explicitamente se e de que forma o módulo deve contemplar a **rotação de capital dentro do próprio mercado cripto**, além da rotação intermercados.

A avaliação deve considerar, entre outros fenômenos potenciais, a alternância de liderança e participação entre segmentos como:

- BTC;
- ETH;
- large caps;
- mid caps;
- small caps / altcoins;
- setores ou narrativas, quando metodologicamente justificável.

A sequência histórica frequentemente descrita como rotação de BTC para ETH e posteriormente para segmentos mais amplos de altcoins deve ser tratada como **hipótese de comportamento de mercado a ser testada**, e não como regra fixa de ciclo.

### Questões metodológicas futuras

- definir o constructo exato de rotação intramercado cripto;
- distinguir rotação genuína de simples co-movimento causado por beta de mercado;
- definir se BTC, ETH, dominâncias, índices agregados, breadth, força relativa, fluxos ou outras métricas são evidências adequadas;
- determinar como identificar divergências entre BTC e o mercado de altcoins;
- avaliar granularidade por capitalização, setor e narrativa;
- definir horizontes e persistência mínima para classificar uma rotação;
- evitar duplicação com Institutional Flow PRO, Ranking Institucional e Asset PRO;
- definir a interface de saída consumível pelo CSM do Asset PRO;
- validar empiricamente se os padrões históricos de rotação permanecem suficientemente estáveis para uso metodológico.

### Interface provisória com o Asset PRO

No desenho corrente do Asset PRO:

- o **CSM não deve reproduzir o Capital Rotation PRO**;
- em execução integrada, o Capital Rotation PRO é a fonte primária candidata do contexto de rotação;
- o Asset PRO deverá usar esse contexto para interpretar alinhamento, neutralidade ou conflito entre a estrutura individual do ativo e o ambiente agregado;
- o tratamento standalone do CSM será especificado separadamente e deverá permanecer mais limitado que o módulo completo de Capital Rotation.

### Regra de escopo

Este item **não decide** que a rotação intramercado cripto fará parte da metodologia final do Capital Rotation PRO, nem define indicadores, pesos, estágios de ciclo ou uma sequência fixa BTC → ETH → large caps → demais altcoins.

Ele registra a necessidade de avaliar formalmente essa hipótese e sua eventual implementação quando o Capital Rotation PRO for revisado.
