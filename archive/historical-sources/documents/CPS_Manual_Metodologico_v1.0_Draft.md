# CRYPTO PRO SUITE
## Manual Metodológico v1.0

**Status:** Draft metodológico  
**Versão:** 1.0  
**Base arquitetural:** CRYPTO PRO SUITE - Constituição v1.0  

---

## 1. Objetivo do Manual

Este Manual Metodológico define as regras comuns de construção, interpretação e evolução dos módulos da CRYPTO PRO SUITE.

A suíte é composta por módulos independentes de apoio à decisão. Cada módulo possui missão específica, pode ser utilizado isoladamente ou em conjunto, e a convergência entre módulos aumenta a confiança analítica.

O objetivo central da metodologia é padronizar a leitura dos sinais de mercado para reduzir incerteza, antecipar movimentos de fluxo de capital e evitar sobreposição entre módulos.

---

## 2. Filosofia Analítica da Suíte

A CRYPTO PRO SUITE segue a sequência lógica:

> **Por quê? → Para onde? → Quem? → O quê? → Quando?**

Essa sequência corresponde aos módulos:

| Pergunta | Módulo | Função |
|---|---|---|
| Por quê? | CRYPTO MACRO PRO | Avalia se o ambiente favorece ativos de risco |
| Para onde? | CAPITAL ROTATION PRO | Identifica para onde o capital global está migrando |
| Quem? | INSTITUTIONAL FLOW PRO | Analisa quem está movimentando o capital |
| O quê? | Ranking Institucional Simplificado | Ranqueia ativos com maior probabilidade de capturar fluxo institucional |
| Quando? | ASSET PRO | Avalia oportunidade técnica e timing operacional |

Nenhum módulo determina sozinho uma decisão. A decisão ganha robustez quando há convergência entre múltiplos módulos.

---

## 3. Princípios Metodológicos Gerais

1. **Independência modular:** cada módulo deve responder à sua própria pergunta central.
2. **Não sobreposição:** um módulo pode dialogar com outro, mas não deve substituir sua função.
3. **Indicadores objetivos:** conclusões devem ser sustentadas por dados sempre que possível.
4. **Escala comum:** sempre que aplicável, todos os módulos devem usar escala de 0 a 100.
5. **Leitura probabilística:** os relatórios devem evitar afirmações determinísticas.
6. **Convergência:** quanto maior a concordância entre módulos, maior a confiança.
7. **Rastreabilidade:** toda conclusão relevante deve estar vinculada a indicadores, regras ou hipóteses explícitas.
8. **Atualização incremental:** mudanças metodológicas devem ser registradas em changelog.
9. **Separação entre diagnóstico e operação:** macro, fluxo e ranking não substituem análise técnica.
10. **Conservadorismo interpretativo:** sinais contraditórios devem reduzir a confiança, não ser ignorados.

---

## 4. Escala Padrão de Pontuação

Todos os scores principais devem utilizar escala de 0 a 100.

| Score | Classificação | Interpretação |
|---:|---|---|
| 85-100 | Extremamente favorável | Forte alinhamento positivo dos indicadores |
| 70-84 | Favorável | Ambiente construtivo, com riscos controlados |
| 55-69 | Moderadamente favorável | Viés positivo, mas sem confirmação plena |
| 45-54 | Neutro | Sinais mistos ou ausência de tendência clara |
| 30-44 | Desfavorável | Pressão negativa relevante |
| 15-29 | Muito desfavorável | Ambiente hostil, risco elevado |
| 0-14 | Crítico | Forte deterioração e baixa visibilidade |

### Regra de interpretação

O score indica **probabilidade e qualidade do ambiente**, não previsão exata de preço.

---

## 5. Níveis de Confiança

Além do score, cada relatório deve apresentar um nível de confiança.

| Confiança | Critério |
|---|---|
| Alta | Indicadores principais convergem e dados são recentes |
| Média | Há convergência parcial, mas com sinais divergentes |
| Baixa | Muitos sinais contraditórios ou dados incompletos |

### Fatores que aumentam a confiança

- Concordância entre indicadores leading e coincident.
- Dados recentes e consistentes.
- Confirmação por mais de um módulo.
- Ausência de eventos macro extraordinários.

### Fatores que reduzem a confiança

- Divergência entre liquidez, preço e fluxo.
- Dados defasados ou incompletos.
- Choques geopolíticos ou regulatórios.
- Movimentos de preço sem confirmação de fluxo.

---

## 6. Classificação Temporal dos Indicadores

Cada indicador deve ser classificado como:

| Tipo | Definição | Exemplo |
|---|---|---|
| Leading | Tende a antecipar mudanças de ciclo | Global M2, DXY, juros reais |
| Coincident | Acompanha o ciclo em andamento | Fluxos de ETF, stablecoins, volume |
| Lagging | Confirma movimentos já iniciados | Indicadores on-chain de euforia, métricas de lucro agregado |

### Regra metodológica

Indicadores leading devem ter maior relevância para antecipação. Indicadores coincident ajudam a confirmar o movimento. Indicadores lagging devem ser usados como confirmação ou alerta de excesso.

---

## 7. Normalização dos Indicadores

Para combinar indicadores diferentes, todos devem ser convertidos para uma escala comum de 0 a 100.

### 7.1 Direção do indicador

Antes da normalização, deve-se definir se o indicador é:

| Tipo | Interpretação |
|---|---|
| Positivo | Quanto maior, melhor para cripto |
| Negativo | Quanto maior, pior para cripto |
| Bidirecional | Extremos em qualquer direção podem indicar risco |

Exemplos:

- Global M2 crescente: positivo.
- DXY crescente: geralmente negativo.
- Funding muito positivo: pode ser negativo por excesso de alavancagem.

### 7.2 Métodos permitidos

Os métodos de normalização aceitos são:

1. **Percentil histórico:** posição do indicador em relação ao próprio histórico.
2. **Z-score:** distância em desvios-padrão da média histórica.
3. **Variação percentual:** mudança em janela definida.
4. **Regra binária:** presença ou ausência de sinal específico.
5. **Pontuação por faixas:** faixas pré-definidas quando há consenso técnico.

### 7.3 Preferência metodológica

Quando houver histórico suficiente, a preferência deve ser:

1. Percentil histórico.
2. Z-score.
3. Variação percentual.
4. Pontuação por faixas.
5. Regra binária.

---

## 8. Estrutura de Pesos

### 8.1 v1.0 - Pesos por consenso técnico

Na versão 1.0, os pesos podem ser definidos por relevância teórica, recorrência histórica e utilidade prática.

### 8.2 v2.0 - Pesos baseados em evidências

Na versão 2.0, os pesos devem ser calibrados por evidências históricas, utilizando:

- Correlação defasada com BTC.
- Taxa de acerto em mudanças de ciclo.
- Antecedência média do sinal.
- Consistência em diferentes regimes.
- Falsos positivos e falsos negativos.

### 8.3 v2.5 - Pesos dinâmicos

Na versão 2.5, os pesos podem variar conforme o regime de mercado:

| Regime | Indicadores com maior peso |
|---|---|
| Expansão monetária | Global M2, balanços de bancos centrais, stablecoins |
| Aperto monetário | DXY, juros reais, Treasury 10Y |
| Adoção institucional | ETFs, flows, custody, on-chain institucional |
| Euforia especulativa | Funding, open interest, altseason, MVRV |
| Estresse sistêmico | VIX, spreads de crédito, dólar, liquidez global |

---

## 9. Crypto Predictive Score (CPS)

O CPS mede a qualidade preditiva de cada indicador.

### Componentes do CPS

| Componente | Peso sugerido | Descrição |
|---|---:|---|
| Taxa de acerto | 30% | Frequência com que antecipou corretamente ciclos |
| Antecedência | 25% | Tempo médio entre sinal e movimento relevante |
| Correlação defasada | 20% | Relação estatística com BTC em janelas futuras |
| Consistência por regime | 15% | Funcionamento em bull, bear, QE, QT etc. |
| Penalidade por ruído | 10% | Falsos positivos e sinais contraditórios |

### Interpretação do CPS

| CPS | Qualidade preditiva |
|---:|---|
| 85-100 | Muito alta |
| 70-84 | Alta |
| 55-69 | Moderada |
| 40-54 | Baixa |
| 0-39 | Fraca ou inconclusiva |

---

## 10. Turning Point Score

O Turning Point Score mede a probabilidade de mudança de regime.

### Entradas sugeridas

- Mudança de inclinação em indicadores leading.
- Divergência entre preço e liquidez.
- Reversão do DXY.
- Mudança nas expectativas de juros.
- Inflação surpreendendo para cima ou para baixo.
- Alteração relevante em stablecoins ou fluxos institucionais.
- Exaustão em indicadores on-chain.

### Interpretação

| Score | Interpretação |
|---:|---|
| 80-100 | Alta probabilidade de inflexão |
| 60-79 | Atenção elevada |
| 40-59 | Monitoramento normal |
| 20-39 | Baixa probabilidade |
| 0-19 | Sem sinais relevantes de virada |

---

## 11. Regras de Convergência entre Módulos

A convergência entre módulos deve ser interpretada como aumento de confiança.

| Situação | Leitura |
|---|---|
| 5 módulos alinhados | Forte convicção |
| 4 módulos alinhados | Alta convicção |
| 3 módulos alinhados | Convicção moderada |
| 2 módulos alinhados | Sinal fraco |
| 1 módulo isolado | Não conclusivo |

### Exemplo

Se o CRYPTO MACRO PRO está favorável, o CAPITAL ROTATION PRO mostra migração para cripto, o INSTITUTIONAL FLOW PRO confirma entrada institucional e o Ranking Institucional Simplificado aponta ativos específicos, a confiança aumenta significativamente.

---

## 12. Regras por Módulo

### 12.1 CRYPTO MACRO PRO

**Pergunta:** Por que o ambiente favorece ou não os ativos de risco?

Deve avaliar:

- Liquidez global.
- Liquidez cripto.
- Macroeconomia.
- On-chain institucional.
- Rotação macro de capital.

Não deve selecionar ativos nem definir pontos de entrada.

### 12.2 CAPITAL ROTATION PRO

**Pergunta:** Para onde o capital global está migrando?

Deve avaliar:

- Rotação entre cripto, ações, ouro, bonds e dólar.
- Rotação dentro do mercado cripto.
- BTC dominance, ETH/BTC, TOTAL2, TOTAL3.
- Migração entre narrativas.

Não deve ranquear ativos individualmente com metodologia institucional.

### 12.3 INSTITUTIONAL FLOW PRO

**Pergunta:** Quem está movimentando o capital?

Deve avaliar:

- ETFs.
- Tesourarias corporativas.
- Fundos.
- Custodiantes.
- Venture capital.
- Baleias e carteiras institucionais quando rastreáveis.

Não deve substituir ranking de ativos.

### 12.4 Ranking Institucional Simplificado

**Pergunta:** Quais ativos têm maior probabilidade de capturar o próximo fluxo institucional?

Deve manter sua metodologia original e independente.

Pode receber contexto dos módulos anteriores, mas não deve ser absorvido por eles.

### 12.5 ASSET PRO

**Pergunta:** Quando um ativo apresenta oportunidade técnica?

Deve avaliar:

- Tendência por múltiplos timeframes.
- Suportes e resistências.
- Price Action.
- Fibonacci.
- Médias móveis.
- Volume Profile.
- Wyckoff.
- Smart Money Concepts.
- Cenários e invalidações.

Não deve substituir análise macro, fluxo institucional ou ranking.

---

## 13. Estrutura Padrão dos Relatórios

Todo relatório da suíte deve conter, quando aplicável:

1. Nome do módulo.
2. Data da atualização.
3. Executive Summary.
4. Score principal.
5. Classificação do ambiente.
6. Nível de confiança.
7. Principais vetores positivos.
8. Principais vetores negativos.
9. Mudanças desde a última atualização.
10. Cenários.
11. Riscos e invalidações.
12. Conclusão operacional.

---

## 14. Horizonte Temporal

Cada módulo deve deixar claro seu horizonte predominante.

| Módulo | Horizonte típico |
|---|---|
| CRYPTO MACRO PRO | 3 a 12 meses |
| CAPITAL ROTATION PRO | 1 a 6 meses |
| INSTITUTIONAL FLOW PRO | 1 semana a 6 meses |
| Ranking Institucional Simplificado | 1 a 12 meses |
| ASSET PRO | Intraday a vários meses, conforme timeframe |

---

## 15. Frequência de Atualização

| Módulo | Frequência recomendada |
|---|---|
| CRYPTO MACRO PRO | Semanal ou sob demanda |
| CAPITAL ROTATION PRO | Semanal |
| INSTITUTIONAL FLOW PRO | Semanal, com alertas relevantes |
| Ranking Institucional Simplificado | Semanal |
| ASSET PRO | Sob demanda |

---

## 16. Padrão de Linguagem

Os relatórios devem usar linguagem:

- Objetiva.
- Probabilística.
- Comparável entre atualizações.
- Transparente quanto a incertezas.
- Separando fatos, inferências e hipóteses.

Evitar:

- Afirmações determinísticas.
- Promessas de valorização.
- Linguagem promocional.
- Conclusões não sustentadas por indicadores.

---

## 17. Semáforo Padrão

| Cor | Significado |
|---|---|
| Verde forte | Sinal muito favorável |
| Verde | Favorável |
| Amarelo | Neutro ou misto |
| Laranja | Desfavorável |
| Vermelho | Crítico |

---

## 18. Regras de Invalidação

Cada relatório deve indicar o que invalidaria sua conclusão.

Exemplos:

- Deterioração abrupta da liquidez global.
- Reversão forte do DXY para cima.
- Saída líquida persistente de ETFs.
- Contração relevante de stablecoins.
- Perda de suporte técnico estrutural no BTC.
- Choque regulatório ou geopolítico.

---

## 19. Changelog e Controle de Versões

Toda alteração metodológica deve ser registrada.

### Formato recomendado

| Versão | Data | Alteração | Impacto |
|---|---|---|---|
| 1.0 | 2026-06-30 | Criação do manual metodológico | Define regras comuns da suíte |

### Tipos de alteração

- Arquitetural.
- Metodológica.
- Indicador adicionado.
- Indicador removido.
- Peso alterado.
- Fonte de dados alterada.
- Formato de relatório alterado.

---

## 20. Roadmap Metodológico

### v1.0

- Escalas comuns.
- Regras de confiança.
- Separação de funções por módulo.
- Estrutura padrão de relatório.
- Critérios iniciais de normalização.

### v2.0

- CPS calibrado historicamente.
- Pesos baseados em evidências.
- Backtests por ciclo do Bitcoin.
- Redução de arbitrariedade nos scores.

### v2.5

- Pesos dinâmicos.
- Classificação automática de regime.
- Ajuste de relevância por contexto macro.

### v3.0

- Motor probabilístico integrado.
- Alertas de mudança de regime.
- Painel consolidado da CRYPTO PRO SUITE.
- Integração entre módulos com score de convergência.

---

## 21. Conclusão

Este Manual Metodológico estabelece a base comum da CRYPTO PRO SUITE.

Sua função é garantir que todos os módulos evoluam de maneira consistente, comparável e rastreável, preservando a independência de cada módulo e reforçando a filosofia central da suíte:

> **Por quê? → Para onde? → Quem? → O quê? → Quando?**

A partir deste manual, cada novo módulo deve ser desenvolvido com escopo claro, indicadores objetivos, metodologia explícita, score interpretável e regras de atualização documentadas.