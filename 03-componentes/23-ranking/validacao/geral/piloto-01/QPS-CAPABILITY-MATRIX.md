# PCP-01 — QPS Capability Matrix

**Status:** revisão documental concluída; dry-run e avaliação jurídico-comercial pendentes  
**QPS:** Qualified Pilot Source  
**As-of da revisão:** 2026-09-30  
**Natureza:** artefato experimental; não normativo

Nenhuma fonte candidata é considerada QPS apenas por ter sido historicamente utilizada ou preferida. A qualificação exige três camadas independentes:

1. **Technical Capability** — a API documentada fornece os campos necessários.
2. **Operational Validation** — o endpoint funciona com estabilidade suficiente no dry-run.
3. **Use-Rights / Commercial Governance** — o uso pretendido é compatível com os termos/licenciamento aplicáveis.

A aprovação técnica não substitui as outras duas.

## 1. Matriz de capacidade

| Fonte | Spot catalog / status | Order book | Timestamp | Volume/history | Pair metadata | Technical review | Operational dry-run | Use-rights review | Estado PCP-01 |
|---|---|---|---|---|---|---|---|---|---|
| Binance | SUPPORTED | SUPPORTED* | SUPPORTED | SUPPORTED | SUPPORTED | PASS WITH OPEN ITEM | PENDING | UNRESOLVED | PENDING |
| Bybit | SUPPORTED | SUPPORTED — até 1000 níveis spot | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | RESTRICTIVE / REVIEW REQUIRED | LEGAL HOLD |
| OKX | SUPPORTED | SUPPORTED — books até 400; books-full até 5000 | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | COMMERCIAL USE REQUIRES WRITTEN LICENSING | LEGAL HOLD |
| Bitget | SUPPORTED | SUPPORTED — até 1000 níveis | SUPPORTED | SUPPORTED | SUPPORTED | PASS | PENDING | RESTRICTIVE / REVIEW REQUIRED | LEGAL HOLD |
| MEXC | SUPPORTED | SUPPORTED — REST até 5000 níveis | PARTIAL** | SUPPORTED | SUPPORTED | PASS WITH LIMITATION | PENDING | COMMERCIAL DATA USE RESTRICTED WITHOUT CONSENT | LEGAL HOLD |

* A documentação pública da Binance confirma a infraestrutura de market data spot e o uso do endpoint público dedicado; a capacidade de profundidade spot deve ser confirmada no dry-run do adaptador antes de qualificação operacional definitiva.

** O endpoint REST de depth da MEXC fornece update ID, mas não apresenta timestamp de geração no payload documentado; o piloto deverá preservar `observed_at` local e, se necessário, usar streams que fornecem `sendtime`. Isso é limitação de provenance temporal, não falha automática.

## 2. Evidência técnica resumida

### Binance

A documentação oficial atual:
- define market data público como security type `NONE`;
- recomenda `data-api.binance.vision` para market-data-only;
- documenta timestamps em milissegundos e rate limits;
- o Data Feed v1.0 já usa Binance Spot para BTCUSDT, mas ainda não implementa o capture de microstructure requerido pelo PCP-01.

**Estado:** capacidade técnica plausível/forte, mas order-book pilot capture e direitos de uso comercial ainda precisam de fechamento explícito.

### Bybit

A API V5 documenta:
- `/v5/market/instruments-info` para instrumentos spot;
- `/v5/market/orderbook` com até 1000 níveis para spot;
- `/v5/market/kline` com volume e turnover;
- timestamps nos retornos.

**Estado:** tecnicamente apta para adaptação ao PCP-01, sujeita a dry-run.

### OKX

A API V5 documenta:
- instrumentos públicos;
- `/api/v5/market/books` com até 400 níveis por lado;
- `/api/v5/market/books-full` com até 5000 níveis;
- candles e historical candles;
- timestamps de geração do book.

**Estado:** tecnicamente forte para Capacity, mas juridicamente bloqueada para rota comercial sem licença/consentimento escrito identificado.

### Bitget

A documentação V3 documenta:
- market data spot;
- order book com até 1000 níveis;
- timestamp de geração;
- candles com base volume e quote turnover;
- catálogo de símbolos/market endpoints.

**Estado:** tecnicamente apta, sujeita a dry-run e revisão de direitos.

### MEXC

A Spot API V3 documenta:
- `/api/v3/exchangeInfo`;
- `/api/v3/depth` com até 5000 níveis;
- klines com base e quote volume;
- streams de depth com `sendtime`;
- informações de moeda/rede em endpoints adicionais.

**Estado:** tecnicamente apta com ressalva temporal para snapshots REST e sujeita a dry-run.

## 3. Revisão de direitos de uso

### OKX — RED FLAG explícito

O API Agreement vigente declara que market data público permanece sujeito às restrições de uso e que uso comercial, redistribuição e uso em plataforma de análise exigem consentimento/licenciamento apropriado.

**Tratamento:** `LEGAL HOLD` até licença ou autorização escrita compatível com o produto.

### Bybit — RED FLAG explícito

Os API Terms & Conditions proíbem reempacotar/revender Service Data e comercialmente explorar as APIs sem autorização aplicável.

**Tratamento:** `LEGAL HOLD`.

### MEXC — RED FLAG explícito

Os Terms of Use proíbem, sem consentimento escrito, usos comerciais de market data incluindo data feeds/streaming e serviços que obtenham lucro com esses dados.

**Tratamento:** `LEGAL HOLD`.

### Bitget — RED FLAG / ambiguidade

Os Terms of Use restringem uso dos Services para resale/commercial purposes sem acordo escrito; os API Key Terms também reservam direitos amplos sobre API-related data. Há materiais Bitget que mencionam limited commercial use em contextos específicos, mas isso não deve ser presumido aplicável ao PCP-01 ou ao produto comercial sem confirmação jurídica/documental.

**Tratamento:** `LEGAL HOLD`.

### Binance — direitos comerciais não fechados nesta revisão

A documentação oficial incentiva integrações, dashboards, analytics e serviços internos e fornece public market data endpoints. Entretanto, esta revisão não encontrou texto suficientemente específico para concluir direitos de redistribuição/uso comercial do market data no produto planejado.

**Tratamento:** `UNRESOLVED`; obter confirmação/licença aplicável antes de qualquer publicação comercial.

## 4. Regra de qualificação revisada

Uma fonte só poderá receber `QUALIFIED` para o PCP-01 quando:

- **Technical Capability = PASS**;
- **Operational Dry-run = PASS**;
- **Use-Rights = ACCEPTABLE FOR THE PILOT USE CASE**.

Para a futura operação comercial, haverá um gate separado:

> **Commercial Source Approval**

Uma QPS do piloto não se transforma automaticamente em fonte comercial.

## 5. Decisão atual

Nenhuma das cinco fontes está autorizada ainda como `QUALIFIED` completa.

- Binance: `PENDING` por dry-run + direitos de uso não fechados.
- Bybit: `LEGAL HOLD`.
- OKX: `LEGAL HOLD`.
- Bitget: `LEGAL HOLD`.
- MEXC: `LEGAL HOLD`.

Isso não invalida o desenho do PCP-01. Significa que a próxima implementação deve ser **adapter-based e source-agnostic**, e que o run oficial só pode ser ativado quando houver pelo menos uma combinação de fontes tecnicamente e juridicamente admissíveis para o uso experimental definido.

## 6. Fontes oficiais consultadas

- Binance Developer Documentation — Spot REST API / public market data.
- Binance API Product / Developer portal.
- Bybit V5 API — Instruments Info, Orderbook, Kline.
- Bybit API Terms & Conditions.
- OKX API V5 — instruments, books, candles.
- OKX API Agreement (2026-03-26).
- Bitget API V3 — Market Data.
- Bitget Terms of Use / API Key Terms.
- MEXC Spot API V3.
- MEXC User Agreement.

Os termos devem ser revisitados no momento da ativação, pois podem ser alterados unilateralmente pelas plataformas.
