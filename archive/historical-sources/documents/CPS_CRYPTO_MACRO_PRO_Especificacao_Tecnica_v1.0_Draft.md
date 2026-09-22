# CRYPTO MACRO PRO
## Especificação Técnica v1.0 (Draft)

### Status
**Em desenvolvimento**

## Missão
Responder objetivamente à pergunta:

> **"Por que o ambiente macro favorece ou não os ativos de risco?"**

Seu objetivo é identificar, medir e monitorar as condições macroeconômicas e de liquidez que historicamente antecedem os grandes ciclos do mercado de criptoativos.

O CRYPTO MACRO PRO **não seleciona ativos** nem define pontos de entrada. Sua função é avaliar o contexto macro que influencia o mercado como um todo.

# Escopo

## O módulo FAZ
- Avalia a liquidez global.
- Avalia a política monetária.
- Avalia a liquidez específica do mercado cripto.
- Avalia indicadores macroeconômicos.
- Avalia sinais macro de rotação de capital.
- Gera um score quantitativo.
- Estima a probabilidade de continuidade ou mudança de regime macro.

## O módulo NÃO FAZ
- Escolha de criptomoedas.
- Ranking de ativos.
- Análise técnica.
- Price Action.
- Timing de entrada.
- Timing de saída.

# Arquitetura

## Módulo 1 — Liquidez Global
**Missão:** Medir a expansão ou contração da liquidez mundial.

Indicadores:
- Global M2
- Liquidez líquida global
- Balanço do Fed
- Balanço do BCE
- Balanço do Banco do Japão
- Balanço do Banco Popular da China
- Financial Conditions Index
- Reverse Repo (RRP)
- Treasury General Account (TGA)

## Módulo 2 — Liquidez Cripto
**Missão:** Medir o fluxo de capital disponível dentro do ecossistema.

Indicadores:
- Fluxo ETFs Spot BTC
- Fluxo ETFs Spot ETH
- Supply de Stablecoins
- Crescimento semanal das Stablecoins
- Reservas de Stablecoins nas Exchanges
- Exchange Netflows
- TVL DeFi
- Open Interest agregado

## Módulo 3 — Macroeconomia
**Missão:** Medir o custo global do dinheiro.

Indicadores:
- DXY
- Treasury 10Y
- Real Yield
- CPI / Core CPI
- PCE / Core PCE
- Fed Funds Rate
- Curva de Juros
- Probabilidade implícita de cortes
- Payroll
- Taxa de desemprego
- ISM Manufacturing
- ISM Services

## Módulo 4 — On-chain Institucional
**Missão:** Avaliar o comportamento estrutural do capital.

Indicadores:
- MVRV
- NUPL
- Long-Term Holder Supply
- Short-Term Holder Supply
- Exchange Reserves
- Dormancy
- Coin Days Destroyed
- RHODL
- Reserve Risk
- Puell Multiple

## Módulo 5 — Rotação de Capital
**Missão:** Identificar mudanças na direção dos fluxos financeiros.

Indicadores:
- BTC Dominance
- ETH/BTC
- TOTAL2
- TOTAL3
- Altseason Index
- BTC × Ouro
- BTC × Nasdaq
- BTC × S&P500
- BTC × Bonds
- BTC × DXY

# Macro Liquidity Score (MLS)

Escala: 0–100

- 85–100 → Extremamente Favorável
- 70–84 → Favorável
- 55–69 → Moderadamente Favorável
- 45–54 → Neutro
- 30–44 → Desfavorável
- 15–29 → Muito Desfavorável
- 0–14 → Ambiente Crítico

# Crypto Predictive Score (CPS)

O CPS mede a capacidade preditiva dos indicadores. Na v1.0 os pesos são definidos por consenso técnico; nas versões futuras serão calibrados por evidências históricas.

# Frequência de atualização

| Categoria | Frequência |
|---|---|
| Liquidez Global | Semanal |
| ETFs | Diária |
| Stablecoins | Diária |
| On-chain | Diária |
| Macroeconomia | Conforme divulgação |
| Score Geral | Sob demanda |

# Fontes de dados
- FRED
- BLS
- BEA
- Bancos Centrais
- TradingView
- Glassnode
- CryptoQuant
- CoinGlass
- DefiLlama
- SoSoValue
- Farside Investors

# Estrutura do relatório
1. Executive Summary
2. Macro Liquidity Score
3. Crypto Predictive Score
4. Scores por módulo
5. Heat Map dos indicadores
6. Semáforo Macro
7. Turning Point Score
8. Vetores positivos
9. Vetores negativos
10. Mudanças desde a última atualização
11. Cenários (30, 90 e 180 dias)
12. Conclusão operacional

# Roadmap
## v1.0
- Arquitetura consolidada
- Indicadores definidos
- Macro Liquidity Score
- Relatório padronizado

## v2.0
- CPS calibrado com dados históricos
- Pesos baseados em evidências

## v2.5
- Pesos dinâmicos por regime de mercado

## v3.0
- Motor probabilístico de antecipação de ciclos
- Aprendizado contínuo
- Alertas automáticos de mudança de regime