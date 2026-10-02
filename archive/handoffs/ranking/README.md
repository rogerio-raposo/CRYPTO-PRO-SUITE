# Ranking Institucional Simplificado — Handoffs de Continuidade

**Status:** artefato operacional  
**Finalidade:** servir como **único ponteiro operacional** para a retomada da conversa **Ranking Institucional Simplificado — Metodologia Geral**.

## Arquitetura de continuidade

`Template canônico → README/pointer → checkpoint vigente → Freshness Gate → Diagnóstico de Continuidade → retomada controlada`

## Checkpoint vigente

**CP15 — 2026-10-02**

Arquivo:

`archive/handoffs/ranking/CPS_Ranking_Institucional_Continuidade_Metodologica_2026-10-02_CP15.md`

Checkpoint anterior:

`CP14`

Status:
> vigente para continuidade operacional, sujeito ao Freshness Gate do template canônico.

## Referência ao template canônico

Utilizar:

`archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md`

em **Modo Continuidade**.

## Procedimento de retomada

1. consultar este `README.md` para identificar inequivocamente o checkpoint vigente;
2. consultar o template canônico e utilizar **Modo Continuidade**;
3. ler integralmente o checkpoint vigente indicado neste ponteiro;
4. aplicar o **Freshness Gate** contra o estado atual da branch `main`;
5. verificar também o estado corrente das dependências operacionais do Ranking, especialmente `rogerio-raposo/crypto-pro-datafeed`, quando o ponto de retomada depender de execução técnica;
6. apresentar o **Diagnóstico de Continuidade** antes de retomar desenvolvimento;
7. se não houver alteração material, retomar exatamente do **Ponto exato de retomada** registrado no checkpoint vigente;
8. se houver alteração material, registrar divergências e ajustar o ponto de retomada conforme a hierarquia documental do projeto.

## Prompt operacional de retomada

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **Modo Continuidade** para iniciar esta conversa, dedicada ao **Ranking Institucional Simplificado — Metodologia Geral**. Consulte `archive/handoffs/ranking/README.md` para identificar o checkpoint vigente e leia integralmente o handoff indicado. Aplique o Freshness Gate contra a branch `main` e verifique as dependências operacionais relevantes, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome do **Ponto exato de retomada** registrado no checkpoint vigente.

## Política de checkpoint

- os CPs são **snapshots autônomos e imutáveis** do estado de trabalho;
- um CP novo não incorpora integralmente os CPs anteriores;
- todo novo CP referencia o checkpoint anterior;
- checkpoints anteriores permanecem preservados para auditoria;
- este `README.md` é o **único ponteiro operacional** para o checkpoint vigente;
- **somente este README contém o prompt operacional de retomada**;
- checkpoints contêm apenas a referência estável `Ponteiro operacional de continuidade: archive/handoffs/ranking/README.md` e, quando aplicável, o checkpoint anterior;
- correções materiais geram novo CP; não se faz sobrescrita silenciosa de checkpoint publicado;
- handoffs são artefatos operacionais e **não normativos**;
- o Freshness Gate e o Diagnóstico de Continuidade continuam obrigatórios antes da retomada;
- documentação oficial posterior e de maior autoridade prevalece sobre o handoff quando houver conflito;
- mudanças no estado técnico de dependências externas não autorizam avanço metodológico automático sem verificação e, quando aplicável, gate humano.

## Migração do padrão anterior

- **CP01–CP12:** preservados como histórico do modelo cumulativo anterior;
- **CP12:** último checkpoint cumulativo; preservado sem correções retroativas, inclusive com inconsistências de metadados/referências internas que motivaram a mudança de arquitetura;
- **CP13:** primeiro checkpoint no modelo **snapshot + pointer**;
- a partir do CP13, nenhum novo checkpoint deve repetir o histórico cumulativo completo.

## Histórico do novo padrão

- **CP13 — 2026-10-01:** primeiro snapshot autônomo do Ranking e migração formal para o modelo snapshot + pointer.\n- **CP14 — 2026-10-02:** registra a correção de orquestração do dry-run temporal sem alteração metodológica.\n- **CP15 — 2026-10-02:** registra two-cycle PASS, QEV declaration e chegada ao human UFT gate; checkpoint vigente.
