# Asset PRO — Handoffs de Continuidade

**Status:** artefato operacional  
**Finalidade:** servir como **único ponteiro operacional** para a retomada da conversa **Asset PRO — Metodologia Geral**.

## Arquitetura de continuidade

`Template canônico → README/pointer → checkpoint vigente → Freshness Gate → Diagnóstico de Continuidade → retomada controlada`

## Checkpoint vigente

**CP02 — 2026-10-01**

Arquivo:

`archive/handoffs/asset/CPS_Asset_PRO_Continuidade_Metodologica_2026-10-01_CP02.md`

Checkpoint anterior:

`CP01`

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
5. apresentar o **Diagnóstico de Continuidade** antes de retomar desenvolvimento;
6. se não houver alteração material, retomar exatamente do **Ponto exato de retomada** registrado no checkpoint vigente;
7. se houver alteração material, registrar divergências e ajustar o ponto de retomada conforme a hierarquia documental do projeto.

## Prompt operacional de retomada

> Consulte no repositório do CRYPTO PRO SUITE o arquivo `archive/historical-reconstruction/CPS_Template_Abertura_Conversa_Modulo.md` e utilize-o em **Modo Continuidade** para iniciar esta conversa, dedicada ao **Asset PRO — Metodologia Geral**. Consulte `archive/handoffs/asset/README.md` para identificar o checkpoint vigente e leia integralmente o handoff indicado. Aplique o Freshness Gate, apresente primeiro o Diagnóstico de Continuidade e, se não houver alteração material, retome do **Ponto exato de retomada** registrado no checkpoint vigente.

## Política de checkpoint

- os CPs são **snapshots autônomos e imutáveis** do estado de trabalho;
- um CP novo não incorpora integralmente os CPs anteriores;
- todo novo CP referencia o checkpoint anterior;
- checkpoints anteriores permanecem preservados para auditoria;
- este `README.md` é o **único ponteiro operacional** para o checkpoint vigente;
- **somente este README contém o prompt operacional de retomada**;
- checkpoints contêm apenas a referência estável `Ponteiro operacional de continuidade: archive/handoffs/asset/README.md` e, quando aplicável, o checkpoint anterior;
- correções materiais geram novo CP; não se faz sobrescrita silenciosa de checkpoint publicado;
- handoffs são artefatos operacionais e **não normativos**;
- o Freshness Gate e o Diagnóstico de Continuidade continuam obrigatórios antes da retomada;
- documentação oficial posterior e de maior autoridade prevalece sobre o handoff quando houver conflito.

## Histórico

- **CP01 — 2026-10-01:** primeira implementação do mecanismo de continuidade. Preservado para auditoria. Continha prompt interno, padrão posteriormente corrigido.
- **CP02 — 2026-10-01:** checkpoint vigente. Adota integralmente o modelo **snapshot + pointer**, com prompt e procedimento centralizados exclusivamente neste README.
