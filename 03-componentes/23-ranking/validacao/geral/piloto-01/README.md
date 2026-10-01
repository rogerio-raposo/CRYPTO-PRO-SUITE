# Ranking Institucional Simplificado — Piloto Metodológico 01

**Escopo:** Ranking Geral  
**Identificador:** PCP-01  
**Status:** Pré-registro operacional — NÃO EXECUTADO  
**Data:** 2026-09-30  
**Natureza:** artefato de validação; não normativo

## Finalidade

Este diretório contém o pré-registro e os artefatos operacionais do primeiro piloto controlado da metodologia geral do Ranking Institucional Simplificado.

O PCP-01 testa executabilidade, reprodutibilidade, discriminação, auditabilidade e custo analítico do método. Não testa retorno futuro, alpha, previsão de preço ou performance de portfólio.

## Estado atual

- metodologia conceitual: congelada provisoriamente para o piloto;
- score cardinal: ausente por desenho;
- pesos: ausentes por desenho;
- candidatos: ainda não selecionados;
- UFT: ainda não declarado;
- T0: ainda não declarado;
- coleta prospectiva: ainda não iniciada;
- avaliação de ativos: NÃO AUTORIZADA.

## Artefatos

- `PCP-01-CONFIGURATION.md` — configuração congelável do piloto;
- `QPS-CAPABILITY-MATRIX.md` — qualificação das fontes candidatas;
- `CANONICAL-ASSET-REGISTRY-SCHEMA.md` — identidade canônica dos ativos;
- `CANDIDATE-DISCOVERY-REGISTER.md` — descoberta e Current Admission;
- `QEV-MAPPING-AND-CAPTURE-MANIFEST.md` — mercados e eventos de coleta planejados;
- `PILOT-DATA-CAPTURE-SPEC.md` — contrato de dados requerido pelo Ranking;
- `DRY-RUN-AND-T0-PROTOCOL.md` — readiness, dry-run, UFT e T0;
- `RECORD-SCHEMAS.md` — registros auditáveis de evidência, constructos, gates, frictions e comparações.

## Regra de integridade

Nenhum ativo poderá receber E-state, Confidence, Friction Severity, Δ, veto ou Ranking Class antes de:
1. concluir a qualificação mínima das fontes;
2. congelar configuração, universo e candidatos;
3. validar o pipeline de captura;
4. concluir a janela prospectiva de 24h;
5. declarar T0;
6. congelar o Evidence Pack.

## Fronteira com o Crypto Pro Data Feed

O Ranking especifica **quais dados precisa**. A aquisição e publicação desses dados pertencem arquiteturalmente ao Crypto Pro Data Feed. O PCP-01 pode usar uma implementação experimental do Data Feed, mas não deve criar um segundo sistema permanente de aquisição dentro do módulo Ranking.
