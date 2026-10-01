# PCP-01 — Pilot Configuration

**Status:** pré-registrado; parâmetros experimentais sujeitos a validação posterior  
**Execução:** ainda não iniciada

## Objetivo

Avaliar se a metodologia geral do Ranking Institucional Simplificado consegue identificar, avaliar e comparar de forma reproduzível, auditável e economicamente interpretável criptoativos candidatos à captura de um Flow Vector previamente especificado, produzindo relações de preferência e Ranking Classes sem score cardinal nem pesos.

## Desenho

| Parâmetro | PCP-01 |
|---|---|
| desenho | static / cross-sectional / controlled / adversarial |
| Flow Vectors | 1 |
| Flow Vector | FV-01 — Institutional Tokenization & Onchain Capital Markets Infrastructure |
| horizonte | 90 dias a partir de T0 |
| RIP | RIP-01 — Direct Digital-Asset-Capable Professional Allocator |
| RAS | RAS-01 — USD 5.000.000 em até 24h |
| amostra-alvo | 8–12 ativos |
| target operacional | ~10 |
| pesos | nenhum |
| score agregado | nenhum |
| Trajectory | fora do Run A |
| preço/retorno futuro | não usado para validar Run A |

## FV-01

Direção de adoção, atividade e alocação institucional em infraestrutura pública de blockchain e protocolos utilizados para emissão, registro, liquidação, distribuição, interoperabilidade ou liquidez de ativos financeiros e real-world assets tokenizados.

A classificação temática “RWA” não é prova de relação material.

## RIP-01

Entidade profissional com capacidade legal, operacional e tecnológica para adquirir e manter diretamente criptoativos spot, utilizando infraestrutura profissional de execução e custódia e sujeita a requisitos institucionais de liquidez, risco operacional e compliance.

O PCP-01 assume mandato legal para spot direto e acesso legítimo às fontes qualificadas do piloto. Não pretende modelar todas as jurisdições.

## RAS-01

USD 5 milhões de notional para estabelecimento ou redução de posição em janela máxima de 24 horas.

Para a simulação experimental:
- 24 child orders iguais;
- aproximadamente USD 208,3 mil por hora;
- buy e sell avaliados;
- RAS-01 é probe experimental, não parâmetro estrutural da Suite.

## Exclusões do Pilot 01

- BTC;
- ETH;
- stablecoins;
- memecoins;
- wrapped duplicates sem independência econômica;
- produtos alavancados/sintéticos de exchange;
- ativos inativos ou com identidade/migração não resolvida.

## Gates

**Materiality — Confirmed PASS**
- Exposure >= E2 / C3+
- Capture >= E2 / C3+

**Capacity — Confirmed PASS**
- Accessibility >= E2 / C3+
- Absorption >= E2 / C3+

Apenas Confirmed PASS em ambos pode ingressar plenamente no Base Ranking.

## Freeze rule

Após o início do run não alterar retroativamente:
- Flow Vector;
- horizonte;
- RIP;
- RAS;
- fontes qualificadas;
- universo/amostra;
- anchors;
- C3;
- regras Δ/veto;
- parâmetros PEC/PR.

Qualquer revisão exige novo run/versionamento do piloto.
