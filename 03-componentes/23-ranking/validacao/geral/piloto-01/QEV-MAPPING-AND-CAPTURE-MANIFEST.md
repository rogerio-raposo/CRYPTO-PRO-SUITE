# PCP-01 — QEV Mapping and Capture Manifest

**Status:** template pré-registrado

## QEV — Qualified Execution Venue

A qualificação é feita por `Asset × Venue × Market × T0`, não apenas por exchange.

Campos mínimos:

| Campo | Descrição |
|---|---|
| canonical_asset_id | ativo |
| venue | QPS |
| symbol | símbolo da venue |
| base_asset | base |
| quote_asset | quote |
| market_type | spot |
| quote_usd_equivalent | yes/no |
| market_active | yes/no |
| depth_available | yes/no |
| volume_history_available | yes/no |
| timestamp_quality | adequate/inadequate |
| deposit_withdraw_status_available | yes/no/NA |
| qev_status | QUALIFIED / LIMITED / NOT_QUALIFIED |
| limitations | observações |

## Capture Manifest

Para cada QEV qualificada:
- 24 capture events horários consecutivos;
- UTC;
- best bid/ask;
- order-book levels/depth;
- market status;
- venue timestamp quando disponível;
- observed_at;
- collection status;
- provenance;
- depth_limit_flag;
- retry/error metadata.

## Sincronização multi-venue

- target: <= 60 segundos;
- tolerância máxima para agregação consolidada: 180 segundos;
- acima de 180 segundos: manter venue-specific, sem agregação como snapshot simultâneo.

## Profundidade mínima desejada

O book deve alcançar pelo menos o child order de ~USD 208,3 mil por direção. Quando tecnicamente possível, coletar margem adicional para diagnosticar tail/fragilidade.

A insuficiência do endpoint deve ser registrada; não interpolar profundidade inexistente.
