# PCP-01 — QPS Capability Matrix

**Status:** aberta para verificação técnica  
**QPS:** Qualified Pilot Source

Nenhuma fonte candidata é considerada QPS apenas por ter sido historicamente utilizada ou preferida. A qualificação deve ser baseada em capacidade verificável para o PCP-01.

## Fontes candidatas

| Fonte | Spot catalog | Market status | Order book | Timestamp | Volume/history | Pair metadata | Operational stability | Pilot-use terms checked | QPS status |
|---|---|---|---|---|---|---|---|---|---|
| Binance | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NOT YET QUALIFIED |
| Bybit | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NOT YET QUALIFIED |
| OKX | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NOT YET QUALIFIED |
| Bitget | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NOT YET QUALIFIED |
| MEXC | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NOT YET QUALIFIED |

## Critérios mínimos

Uma fonte só recebe `QUALIFIED` quando:
- expõe catálogo de instrumentos/mercados spot utilizável;
- informa status suficiente do mercado;
- fornece order book com profundidade suficiente ou detectável;
- fornece timestamps ou permite timestamp de observação auditável;
- fornece volume/histórico necessário ao protocolo;
- fornece metadata de par/base/quote;
- apresenta funcionamento suficientemente estável no dry-run;
- seu uso no experimento não viola condição de uso identificada.

## Estados

- `QUALIFIED`
- `QUALIFIED_WITH_LIMITATIONS`
- `NOT_QUALIFIED`
- `PENDING`

Limitações devem ser registradas por capacidade, não ocultadas em nota geral.

## Observação comercial

Qualificação para PCP-01 não equivale a aprovação para uso/redistribuição comercial no produto. A governança comercial definitiva pertence ao Crypto Pro Data Feed.
