# PCP-01 — Dry-Run and T0 Protocol

**Status:** pré-registrado

## Definições

- `UFT` — Universe Freeze Time;
- `Capture Start` — início da janela oficial de captura;
- `T0` — Analytical As-of;
- `H` — 90 dias após T0.

## Readiness Gate

UFT/T0 não podem ser declarados antes de:
- PCP-01 configuration frozen;
- QPS Capability Matrix concluída;
- SMU-PCP01 construído;
- canonicalization concluída;
- Candidate Discovery concluído;
- candidate sample congelado;
- QEV mapping congelado;
- capture pipeline operacional;
- UTC timestamps/provenance/retry/logging validados.

## Dry-run

Exigir dois ciclos horários consecutivos tecnicamente bem-sucedidos.

Dry-run:
- não integra PEC;
- não integra PR;
- não integra Evidence Pack;
- não gera E-state;
- não altera candidate membership.

## Ativação

Após readiness + dry-run:
- UFT = momento do freeze final da amostra;
- Capture Start = próxima hora UTC cheia;
- T0 = Capture Start + 24h;
- H = T0 + 90 dias.

## Membership freeze

Após UFT:
- novos ativos não entram;
- candidatos não são substituídos por conveniência;
- eventos entre UFT e T0 entram como evidência;
- hard identity/scope invalidation é registrada sem replacement.

## Technical invalidation

Se API/source transport failure ou collector-side failure sistêmica afetar >25% dos capture events planejados:
- status do run = `TECHNICALLY_INVALID`;
- não inferir condição econômica dos ativos;
- preservar logs;
- repetir em novo run identificado.

## T0 Declaration

A declaração formal deve registrar:
- run_id;
- UFT;
- Capture Start;
- T0;
- horizon_end;
- QPS list;
- candidate list hash/reference;
- QEV map reference;
- capture coverage summary;
- technical validity;
- approver/reviewer.
