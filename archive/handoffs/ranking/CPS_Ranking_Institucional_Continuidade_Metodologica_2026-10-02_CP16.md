# CRYPTO PRO SUITE
## Ranking Institucional Simplificado — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP16  
**Checkpoint anterior:** CP15  
**Ponteiro operacional de continuidade:** `archive/handoffs/ranking/README.md`  
**Status:** handoff operacional; não normativo

## Estado metodológico
Nenhuma regra metodológica foi alterada na passagem CP15 → CP16.

Permanecem vigentes:
- fenômeno-alvo = captura de fluxo institucional relevante;
- unidade = `Asset × Flow Vector × Horizon × As-of`;
- Materiality = Causal Exposure + Economic Capture;
- Capacity = Institutional Accessibility + Absorption;
- sem score cardinal obrigatório;
- sem pesos;
- Trajectory fora do Run A;
- Ranking Geral não herda automaticamente regras de Microcaps.

## PCP-01 congelado
- FV-01 = Institutional Tokenization & Onchain Capital Markets Infrastructure;
- RIP-01 = Direct Digital-Asset-Capable Professional Allocator;
- RAS-01 = USD 5 milhões / 24h;
- child order ≈ USD 208.3k;
- horizonte = 90 dias após T0.

Amostra:
`PLUME, OP, APT, ADA, SUI, LINK, QNT, ONDO, RSR, INJ, HYPE, SYRUP`.

Capacity population:
`PLUME, OP, APT, SUI, LINK, RSR, INJ, HYPE, SYRUP`.

Materiality FAIL:
`ADA, QNT, ONDO`.

## Dry-run / QEV
`two_cycle_status = PASS`.

Qualified pair:
- `2026-10-02T20:00:00Z` — PASS 9/9;
- `2026-10-02T21:00:00Z` — PASS 9/9.

Dry-run workflow:
`37059995273`.

Binance Spot:
`PILOT QUALIFIED` for PCP-01.

Declared QEVs:
`PLUMEUSDT, OPUSDT, APTUSDT, SUIUSDT, LINKUSDT, RSRUSDT, INJUSDT, HYPEUSDT, SYRUPUSDT`.

## Human UFT gate
Status:
`AUTHORIZED / PASSED`.

- UFT = `2026-10-02T23:22:34Z`
- Capture Start = `2026-10-03T00:00:00Z`
- T0 = `2026-10-04T00:00:00Z`
- Horizon End = `2027-01-02T00:00:00Z`
- Run ID = `PCP01-CAP-20261003T0000Z`

## Data Feed execution
Repository:
`rogerio-raposo/crypto-pro-datafeed`

Branch:
`experiment/pcp01-capacity`

Frozen execution-code commit:
`468738b56a965c43169afa21bd31452bcc65e8a1`

Activation commit:
`82dd32a341e60201bc1c8c03bf45ad846a56f6a0`

Official workflow:
`37077293144`

At checkpoint creation:
- activation = active;
- validation job = PASS;
- first controlled capture segment = in progress;
- technical validity = PENDING.

## Concurrency isolation
Final pre-activation check:
- Data Feed main = `8e77307af7e37d472875c4a6435778036e540dfc`;
- Asset PRO work isolated on `experiment/asset-p0`;
- Ranking work isolated on `experiment/pcp01-capacity`;
- both experiment branches were 0 behind main;
- changed-file overlap = none;
- no workflow was already in progress before activation.

## Capture contract
- events 00–23;
- 24 hourly target slots;
- >=18 valid snapshots required;
- standard depth 1000;
- depth escalation to target 5000 where required;
- exact seven-day turnover at T0;
- >25% systemic acquisition failure ⇒ technically invalid run.

Data Feed captures raw evidence only; PEC, PR and E-states are downstream Ranking calculations.

## Ponto exato de retomada
**Etapa 60 — OFFICIAL CAPACITY CAPTURE IN PROGRESS.**

Do not advance to final Capacity assessment before T0.

After workflow completion:
1. verify workflow conclusion;
2. verify events 00–23 and capture-manifest;
3. calculate valid-event coverage by asset;
4. apply the technical invalidation rule;
5. verify turnover-at-T0;
6. inspect RSR depth-escalation evidence;
7. if technically valid, calculate PEC and PR downstream;
8. assess Absorption;
9. complete Institutional Accessibility;
10. form Capacity states with Confidence;
11. continue to the next methodological stage.

No silent fallback to ad hoc sources.
