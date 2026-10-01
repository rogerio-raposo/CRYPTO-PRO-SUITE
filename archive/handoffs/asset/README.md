# Asset PRO — Handoffs de Continuidade

**Status:** artefato operacional  
**Finalidade:** apontar de forma inequívoca o checkpoint vigente para retomada da conversa **Asset PRO — Metodologia Geral**.

## Checkpoint vigente

**CP01 — 2026-10-01**

Arquivo:

`archive/handoffs/asset/CPS_Asset_PRO_Continuidade_Metodologica_2026-10-01_CP01.md`

Status:
> vigente para continuidade operacional, sujeito ao Freshness Gate do template canônico.

## Como retomar em nova conversa

1. consultar `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md`;
2. utilizar **Modo Continuidade**;
3. ler integralmente o checkpoint vigente indicado acima;
4. aplicar o Freshness Gate contra a branch `main`;
5. apresentar o Diagnóstico de Continuidade;
6. retomar somente do ponto exato indicado no checkpoint, salvo mudança material detectada.

## Prompt mínimo

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **Modo Continuidade** para iniciar esta conversa, dedicada ao **Asset PRO — Metodologia Geral**. Consulte `archive/handoffs/asset/README.md` para localizar o checkpoint vigente e leia integralmente o handoff indicado. Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome do **Ponto exato de retomada** registrado no checkpoint vigente.

## Política de checkpoint

- cada CP é snapshot autônomo e imutável do estado de trabalho;
- novos CPs não incorporam cumulativamente o conteúdo integral dos anteriores;
- o checkpoint mais recente referencia o checkpoint anterior;
- este README é o único ponteiro operacional para o CP vigente;
- checkpoints anteriores permanecem preservados para auditoria;
- correções materiais devem gerar novo CP, não sobrescrita silenciosa;
- handoffs são operacionais e não normativos.
