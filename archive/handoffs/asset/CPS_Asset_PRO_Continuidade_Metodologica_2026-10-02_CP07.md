# CRYPTO PRO SUITE
## Asset PRO — Registro de Continuidade Metodológica

**Data do checkpoint:** 2026-10-02  
**Checkpoint:** CP07  
**Checkpoint anterior:** CP06  
**Status:** documento de continuidade de conversa; **não normativo**  
**Escopo:** Asset PRO — Metodologia Geral  
**Finalidade:** preservar o estado posterior à materialização experimental do P0 e ao Design Freeze de ASSET-P0-001, incluindo a governança concorrencial do Data Feed.  
**Ponteiro operacional de continuidade:** `archive/handoffs/asset/README.md`  
**Natureza deste CP:** snapshot autônomo da transição entre Design Freeze e implementação rumo ao Execution Freeze.

---

# 1. Regras de continuidade

- Repositório e documentos persistidos são a fonte de verdade.
- Memória pode orientar recuperação, mas não constitui evidência.
- Este handoff é operacional e **não normativo**.
- Freshness Gate e Diagnóstico de Continuidade permanecem obrigatórios.
- Correções materiais futuras geram novo checkpoint.
- P1 permanece bloqueado até P0 formalmente executado e aprovado.
- Nenhum artefato experimental é promovido automaticamente a metodologia.

---

# 2. Etapas concluídas desde CP06

Foram concluídas:

- **Etapa 39 — Materialização do pacote P0**;
- **Etapa 40 — Preparação do Freeze do P0**.

Marco atual:

> **ASSET-P0-001 encontra-se em DESIGN FREEZE; implementação é autorizada, execução formal ainda não.**

---

# 3. Materialização do P0

## CRYPTO-PRO-SUITE

Criada área:

`03-componentes/24-asset/experimental/P0/`

Artefatos principais:

- `README.md`;
- `P0_EXPERIMENT_MANIFEST.md`;
- `P0_REPLAY_SPECIFICATION.md`;
- `P0_VALIDATION_CONTROLS.md`;
- `P0_FIXTURE_EXPECTATIONS.md`;
- `P0_DESIGN_FREEZE_RECORD.md`;
- `P0_DECISION_RECORD.md`.

## crypto-pro-datafeed

Criadas/estendidas áreas:

- `docs/experimental/asset-p0/`;
- `data/experimental/asset-p0/`;
- `src/experimental/asset_p0/`.

Producer-side specifications incluem:

- Dataset Contract;
- Historical Source Specification;
- Data Validation Specification;
- Resampling Specification;
- Provenance Specification;
- Candle Boundary Policy;
- Canonical Serialization Specification;
- P0 Dataset Plan.

---

# 4. Concorrência no Data Feed

Foi detectada outra conversa trabalhando simultaneamente no mesmo repositório, principalmente sobre **PCP-01**.

Verificações realizadas:

- commits PCP-01 permanecem preservados;
- Asset P0 e PCP-01 usam caminhos distintos;
- nenhuma alteração do Asset P0 sobrescreveu arquivos PCP-01;
- `main` continha ambos os conjuntos de mudanças anteriores à segregação.

Medida adotada:

> todo desenvolvimento producer-side futuro do Asset P0 ocorre na branch `experiment/asset-p0`.

Regra:

- não escrever novas alterações Asset P0 diretamente em Data Feed `main`;
- antes de qualquer integração, comparar branch Asset P0 × `main`;
- inspecionar overlaps;
- reconciliar arquivos compartilhados explicitamente;
- nunca sobrescrever PCP-01 ou outros experimentos.

---

# 5. ASSET-P0-001 — Design Freeze

## Identidade

- Experiment ID: `ASSET-P0-001`;
- Specification Version: `ASSET-P0-SPEC-0.1.0`;
- Parameter Profile: `P0-NONE`.

## Dataset principal

- provider: Binance Public Data;
- venue: Binance Spot;
- instrument: BTCUSDT;
- market type: Spot;
- data type: klines;
- native timeframe: 1h;
- início: 2025-01-01 00:00 UTC inclusive;
- fim: 2025-04-01 00:00 UTC exclusive;
- expected native candles: 2160;
- derived: 4h e 1d;
- expected 4h: 540;
- expected 1d: 90.

## Tempo

- UTC;
- intervalos half-open `[start,end)`;
- timestamp canônico em Unix epoch microseconds;
- `interval_end_us` é boundary causal autoritativo;
- provider close timestamp pode ser preservado separadamente.

## Serialização

- deterministic UTF-8 JSON/JSONL;
- sorted keys;
- compact separators;
- LF;
- canonical decimal strings;
- SHA-256.

## Source integrity

- ZIPs oficiais Binance Public Data;
- correspondente `.CHECKSUM` quando disponível;
- checksum do archive deve ser validado antes da extração.

---

# 6. Golden Fixtures congeladas em design

## Synthetic Golden Fixture

- 48 expected hourly slots / dois dias UTC;
- um intervalo 1h deliberadamente ausente;
- uma observação extrema porém OHLC-valid;
- boundaries 4h e Daily;
- checkpoint/restart antes do segundo dia;
- expected flags/resampling/hashes serão congelados antes do Execution Freeze.

## Real Golden Fixture

- BTCUSDT Spot 1h;
- 2024-12-31 até 2025-01-03 UTC exclusive;
- expected slots: 72, sujeito a validação;
- cruza 2025-01-01 para testar transição documentada de timestamp unit do arquivo público Spot;
- normalização final sempre para epoch microseconds.

---

# 7. Regras de validação congeladas

P0 é binário:

- PASS;
- FAIL.

Blockers incluem:

- schema/data integrity;
- timestamp integrity;
- archive checksum failure;
- missing/duplicate native 1h interval no dataset principal;
- nondeterministic resampling;
- look-ahead;
- incomplete higher-TF leakage;
- repeated-run nondeterminism;
- checkpoint/restart mismatch.

Warnings não criam terceiro status formal.

---

# 8. Design Freeze records

Suite:

- Manifest freeze commit: `915d3ef01c5c273348a84078ca1dfc81fe701781`;
- Design Freeze Record commit: `6caf26f65f5f6af3f255f06816ea23dbf9e958d6`;
- P0 README pós-freeze: `ba8f2758eea107080e9b9a7b6e8bb4e7374a8009`.

Data Feed producer-side immutable design reference:

- `35e8c1120c6d13acb16617507d770aa2b0ea0b7e`;
- branch operacional: `experiment/asset-p0`.

O commit SHA é a referência imutável; a branch pode continuar evoluindo na implementação.

---

# 9. Execution Freeze — ainda pendente

Antes do Execution Freeze ainda são necessários:

- producer-side implementation;
- causal replay harness implementation;
- Synthetic Golden Fixture bytes + expected outputs/hashes;
- Real Golden Fixture bytes + expected outputs/hashes;
- main validation dataset acquisition/normalization;
- canonical Dataset Manifest;
- Data Version;
- final dataset checksum;
- implementation/review SHAs;
- Code Version;
- final Experiment Manifest hash.

Nenhuma execução formal P0 é permitida antes disso.

---

# 10. Estado atual

- metodologia conceitual Asset PRO Core: fechada em nível de trabalho;
- P0 design: frozen;
- P0 implementation: não concluída;
- P0 Execution Freeze: pendente;
- P0 formal execution: não iniciada;
- P1: bloqueado;
- Data Feed concurrency: mitigada por branch isolada;
- metodologia normativa final: inexistente.

---

# 11. Ponto exato de retomada

## Etapa 41 — Implementação do P0 rumo ao Execution Freeze

Objetivo:

> implementar o producer-side histórico e o Causal Replay Harness contra o Design Freeze de ASSET-P0-001, gerar as Golden Fixtures e preparar os artefatos necessários ao Execution Freeze sem executar ainda o P0 formal.

Ordem recomendada:

1. implementar producer-side em `experiment/asset-p0`;
2. implementar archive/checksum acquisition contract;
3. implementar parser explícito de timestamps e normalização microseconds;
4. implementar OHLC/data-quality validation;
5. implementar deterministic resampling;
6. implementar canonical serialization/checksum;
7. gerar Synthetic Golden Fixture e expected outputs;
8. adquirir/gerar Real Golden Fixture e expected outputs;
9. implementar Causal Replay Harness na Suite;
10. validar localmente determinismo das fixtures;
11. produzir Code Version / Dataset Version preliminares;
12. realizar Freshness/Conflict Check;
13. preparar Execution Freeze.

Regra:

> fixture/regression testing durante implementação não constitui execução formal P0. A execução formal só começa após Execution Freeze.

---

**Fim do CP07**
