# PCP-01 — QPS Capability Matrix

**Status:** revisão documental técnica concluída; dry-run operacional pendente  
**QPS:** Qualified Pilot Source  
**As-of da revisão:** 2026-09-30  
**Natureza:** artefato experimental; não normativo

## 1. Regra vigente do PCP-01

Para o **piloto metodológico**, a qualificação da fonte fica deliberadamente separada da futura aprovação comercial.

### Pilot Source Qualification

Uma fonte pode alimentar o PCP-01 quando:

1. **Technical Capability = PASS** — a API fornece os campos necessários;
2. **Operational Validation = PASS** — o adapter e os endpoints funcionam com estabilidade suficiente no dry-run;
3. provenance, timestamps, falhas e limitações podem ser preservados de forma auditável.

### Commercial Source Approval

Licenciamento, redistribuição, uso em SaaS e demais direitos comerciais permanecem registrados como dependência futura, mas **não bloqueiam a validação metodológica interna do PCP-01**.

Essa separação não constitui conclusão jurídica sobre permissões de uso. Apenas retira a aprovação comercial do caminho crítico deste experimento.

## 2. Matriz de capacidade

| Fonte | Spot catalog / status | Order book | Timestamp | Volume/history | Pair metadata | Technical review | Operational dry-run | Pilot status | Commercial approval |
|---|---|---|---|---|---|---|---|---|---|
| Binance | SUPPORTED | SUPPORTED — 1000 níveis validados no probe | SUPPORTED | SUPPORTED | SUPPORTED | PASS | TECHNICAL PROBE PASS (1 run) | TECHNICALLY ELIGIBLE | DEFERRED |
| Bybit | SUPPORTED | SUPPORTED — até 1000 níveis spot | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | TECHNICALLY ELIGIBLE | DEFERRED |
| OKX | SUPPORTED | SUPPORTED — books até 400; books-full até 5000 | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | TECHNICALLY ELIGIBLE | DEFERRED |
| Bitget | SUPPORTED | SUPPORTED — até 1000 níveis | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | TECHNICALLY ELIGIBLE | DEFERRED |
| MEXC | SUPPORTED | SUPPORTED — REST até 5000 níveis | PARTIAL** | SUPPORTED | SUPPORTED | PASS WITH LIMITATION | PENDING | TECHNICALLY ELIGIBLE | DEFERRED |

* A capacidade efetiva de profundidade e a suficiência para o child order do PCP-01 devem ser confirmadas no dry-run.

** O endpoint REST de depth da MEXC não fornece no payload documentado um timestamp de geração equivalente ao de algumas outras venues; o piloto deve preservar `observed_at` local e registrar a limitação temporal.

## 3. Interpretação dos estados

- `TECHNICALLY ELIGIBLE` — documentação técnica suficiente para justificar implementação experimental do adapter.
- `PENDING` — depende de dry-run ou verificação técnica ainda aberta.
- `PILOT QUALIFIED` — Technical Capability PASS + Operational Validation PASS + provenance adequada.
- `PILOT QUALIFIED WITH LIMITATIONS` — utilizável no piloto com limitação explicitamente registrada.
- `NOT QUALIFIED` — incapaz de atender ao contrato mínimo do PCP-01.
- `COMMERCIAL APPROVAL = DEFERRED` — questão propositalmente fora do caminho crítico da validação metodológica.

## 4. Evidência técnica resumida

### Binance
A infraestrutura pública já é usada pelo Data Feed v1.0 para Binance Spot/BTCUSDT. O primeiro probe experimental do PCP-01 foi executado com sucesso no GitHub Actions em 2026-10-01.

Registro operacional:
- workflow run: `36809639883`;
- commit testado: `0c02c23918df830f0c3adfabdd23fd8406f607cc`;
- símbolo: `BTCUSDT`;
- resultado: `PASS`;
- 1000 bids + 1000 asks recebidos;
- depth visível em ambos os lados superior ao child order de ~USD 208,3k;
- catálogo spot retornado: 3680 mercados;
- 7 dias de turnover obtidos;
- artifact digest: `sha256:574ffb2f74b08ad824f55a1c51ce443f2e208db43c3d21a708588cb0ccf795c1`.

Esse resultado valida o caminho técnico inicial, mas não substitui o dry-run temporal de dois ciclos horários exigido antes de UFT/T0.

### Bybit
A API V5 documenta instrumentos spot, order book, klines/turnover e timestamps suficientes para adaptação experimental.

### OKX
A API V5 documenta instrumentos, books com diferentes profundidades, candles/historical candles e timestamps de geração do book.

### Bitget
A API V3 documenta market data spot, order book, timestamps, candles e metadata de símbolos.

### MEXC
A Spot API V3 documenta exchangeInfo, depth, klines e streams de depth. A principal ressalva inicial é a provenance temporal do snapshot REST.

## 5. Decisão operacional

O PCP-01 deve avançar pela rota:

```text
Technical review
      ↓
Implement one adapter
      ↓
Operational dry-run
      ↓
PILOT QUALIFIED SOURCE
      ↓
Methodological pilot
```

A primeira fonte experimental será **Binance**, porque:
- já existe integração estável no Data Feed;
- reduz o número de mudanças simultâneas;
- permite validar primeiro o schema, provenance e capture pipeline;
- não implica preferência metodológica ou aprovação comercial permanente.

As demais fontes devem ser adicionadas somente se o piloto exigir maior cobertura, multi-venue Capacity ou teste de sensibilidade.

## 6. Governança comercial

A revisão de direitos comerciais já realizada permanece preservada como informação de governança, mas não determina o Run A.

Antes de qualquer produção/comercialização da Suite, deverá existir um **Commercial Source Approval Gate** independente.

## 7. Fontes documentais técnicas

- Binance Developer Documentation — Spot REST API / public market data.
- Bybit V5 API — Instruments Info, Orderbook, Kline.
- OKX API V5 — instruments, books, candles.
- Bitget API V3 — Market Data.
- MEXC Spot API V3.

Os endpoints e limites devem ser reconfirmados durante implementação/dry-run.
