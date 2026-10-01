# PCP-01 — Pilot Data Capture Specification

**Status:** pré-registro de interface  
**Implementação permanente:** responsabilidade do Crypto Pro Data Feed

## Objetivo

Especificar os dados necessários ao PCP-01 sem duplicar a responsabilidade arquitetural de aquisição dentro do módulo Ranking.

## Dados requeridos

### Market universe / availability
- venue;
- instrument/symbol;
- base;
- quote;
- market type;
- trading status;
- observed_at;
- source provenance.

### Market microstructure
- best bid;
- best ask;
- ordered bid levels;
- ordered ask levels;
- price and quantity per level;
- venue/exchange timestamp quando disponível;
- observed_at;
- capture status.

### Turnover
- qualified spot volume;
- intervalo temporal;
- quote currency;
- normalização USD-equivalent;
- venue;
- provenance.

### Operational availability
Quando disponível e metodologicamente aplicável:
- deposits enabled/disabled;
- withdrawals enabled/disabled;
- network status.

## Janela

- microstructure: 24 snapshots horários consecutivos antes de T0;
- turnover: 7 dias terminando em T0;
- minimum per-asset microstructure coverage proposta: 18/24 snapshots.

## PEC_core

`PEC_core` exclui fees account-specific.

Deve refletir:
- spread;
- book slippage;
- execution impact observável no snapshot.

Fees públicas/base podem ser mantidas em overlay diagnóstico separado.

## PR

`PR = RAS-01 / mediana do volume spot diário qualificado nos 7 dias`.

PR é sanity check e não score.

## Parâmetros experimentais de Absorption

- E2: PEC mediano <= 2,0% e PR <= 10%;
- E3: PEC mediano <= 1,0% e PR <= 5%;
- E4: PEC mediano <= 0,50% e PR <= 2%.

P90 do PEC é registrado como diagnóstico, sem threshold autônomo no Run A.

## Falhas

Distinguir:
- venue/market unavailability documentada;
- API/source transport failure;
- collector-side failure.

API/collector failure não é evidência de baixa liquidez.

Falha sistêmica de aquisição que afete >25% dos capture events planejados invalida tecnicamente o run.

## Saída mínima do produtor

Cada registro deve preservar:
- schema/version;
- run_id;
- asset_id;
- venue;
- market;
- timestamp(s);
- raw/normalized values;
- provenance;
- collection status;
- error/limitation flags.

O Ranking deve consumir artefatos publicados/validados pelo Data Feed, não realizar fallback silencioso para fontes ad hoc.
