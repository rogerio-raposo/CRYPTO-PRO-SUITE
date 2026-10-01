# PCP-01 — Candidate Discovery Register

**Status:** template pré-registrado  
**Execução:** vazia até conclusão do SMU-PCP01

## Discovery ontology — FV-01

| Código | Função |
|---|---|
| ISS | Issuance / Asset Lifecycle |
| SET | Settlement / Execution |
| INT | Interoperability / Messaging |
| DAT | Data / Oracle |
| LIQ | Liquidity / Market Infrastructure |
| CMP | Compliance / Identity / Access |

## Registro mínimo por hipótese

| Campo | Descrição |
|---|---|
| discovery_id | identificador |
| canonical_asset_id | ativo |
| function_tags | um ou mais códigos FV-01 |
| hypothesis | relação econômica proposta |
| discovery_source | fonte que gerou a hipótese |
| admissible_support_ids | evidências Tier 1–3 para Current Admission |
| active_at_uft | yes/no/indeterminate |
| economically_testable | yes/no/indeterminate |
| current_admission | CA-PASS / CA-FAIL / CA-IND |
| rationale | justificativa curta |
| reviewer | avaliador |
| timestamp | momento da decisão |

## Regra de Current Admission

`CA-PASS` exige uma relação atual e economicamente testável entre ativo e FV-01, sustentada por ao menos evidência admissível Tier 1–3.

Marketing, roadmap, ticker, categoria de agregador ou mera capacidade técnica não bastam.

## Redução de pool

- admitted pool <= 12: incluir todos;
- admitted pool > 12: stratified reproducible sampling.

Estrato primário:
- Functional Reference Class.

Estrato secundário:
- Supported Venue Breadth.

Seleção interna:
- pseudo-random determinística;
- seed: `PCP01-FV01`.

Não utilizar retorno, fama, expectativa de qualidade ou posição desejada no Ranking.
