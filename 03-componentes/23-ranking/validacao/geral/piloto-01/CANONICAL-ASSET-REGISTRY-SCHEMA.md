# PCP-01 — Canonical Asset Registry Schema

**Status:** pré-registrado

## Objetivo

Deduplicar mercados e representações de um mesmo ativo econômico antes de Candidate Discovery e impedir ticker collision, double counting e tratamento de wrapped representations como ativos independentes sem justificativa.

## Campos mínimos

| Campo | Descrição |
|---|---|
| canonical_asset_id | identificador persistente do ativo econômico |
| canonical_symbol | ticker canônico do piloto |
| canonical_name | nome canônico |
| primary_chain | rede primária, quando aplicável |
| contract_address | contrato canônico, quando aplicável |
| lifecycle_state | active / migrated / discontinued / unresolved |
| predecessor_asset_id | ativo predecessor, se houver |
| successor_asset_id | ativo sucessor, se houver |
| wrapped_representation | yes/no |
| economically_independent | yes/no/indeterminate |
| venue_symbols | mapeamento venue → symbol/pair |
| identity_sources | referências de identidade |
| identity_confidence | C0–C4 |
| eligibility_status | ELIGIBLE / INELIGIBLE / IND |
| exclusion_reason | razão codificada quando aplicável |
| notes | observações |

## Regras

- ticker nunca é identificador suficiente;
- representações wrapped do mesmo exposure não geram candidato independente por padrão;
- migração/token replacement deve preservar lineage;
- identidade C0/C1 impede avaliação formal;
- conflito não resolvido produz `IND`, não escolha silenciosa.
