# CRYPTO PRO SUITE

> Framework modular para análise de criptoativos, macroeconomia, rotação de capital, fluxos institucionais, ranking de oportunidades e suporte estruturado à decisão.

**Status:** em desenvolvimento — preparação da versão inicial formal.

## Objetivo

O CRYPTO PRO SUITE organiza modelos, metodologias, componentes e conhecimento necessários para produzir análises reproduzíveis e auditáveis. O projeto separa governança, metodologia transversal, componentes analíticos e conhecimento/estado histórico.

O repositório é a referência documental principal do projeto. Documentos em Markdown são tratados como fonte técnica canônica; representações editoriais (por exemplo, DOCX/PDF) podem ser mantidas quando necessário.

## Arquitetura documental

```text
CRYPTO-PRO-SUITE/
├── 01-governanca/
│   ├── 00-constituicao/
│   ├── 01-documento-mestre/
│   ├── 02-changelog/
│   ├── 03-glossario-oficial/
│   └── 04-protocolo-editorial/
├── 02-metodologia/
│   ├── 10-manual-metodologico/
│   ├── 11-blueprint-itmm/
│   ├── 12-itmm/
│   └── 13-manual-operacional/
├── 03-componentes/
│   ├── 20-macro/
│   ├── 21-rotation/
│   ├── 22-institutional/
│   ├── 23-ranking/
│   │   ├── metodologia/
│   │   └── validacao/
│   ├── 24-asset/
│   └── 25-cse/
└── 04-conhecimento/
    ├── 30-catalogo-geral/
    ├── 31-fichas/
    ├── 32-fontes/
    ├── 40-state/
    ├── 41-historico-cit/
    ├── 42-historico-cenarios/
    └── 43-historico-indicadores/
```

As pastas são materializadas no Git apenas quando contêm documentação ou um arquivo de orientação; o Git não versiona diretórios vazios.

## Volumes

**Volume I — Governança** define identidade, escopo, regras editoriais, documentação mestre, glossário e controle de mudanças.

**Volume II — Metodologia** reúne princípios e métodos transversais ao sistema, incluindo o Manual Metodológico, ITMM e procedimentos operacionais.

**Volume III — Componentes** documenta os módulos funcionais: Macro, Rotation, Institutional, Ranking, Asset e CSE.

**Volume IV — Conhecimento** mantém catálogo, fichas, fontes, estado e históricos necessários à continuidade e auditabilidade do sistema.

## Ranking Institucional Simplificado

O Ranking permanece um componente independente. Sua documentação específica reside em `03-componentes/23-ranking/`.

A metodologia de microcaps utiliza avaliação baseada em evidências e mantém separados Potential, Confidence, Risk, Operability e Lifecycle. Preço e retornos são outcomes de validação e não ground truth fundamental.

Os pilotos metodológicos pré-v1.0 foram encerrados. A documentação de validação deve permanecer em `03-componentes/23-ranking/validacao/`; a especificação normativa ficará em `03-componentes/23-ranking/metodologia/`.

## Data Feed

O **Crypto Pro Data Feed** permanece em repositório próprio, separado deste repositório documental. O CRYPTO PRO SUITE poderá consumir e referenciar seus dados sem duplicar o código-fonte do Data Feed.

## Convenções

- Markdown é a fonte técnica preferencial para documentação versionada.
- Alterações metodológicas relevantes devem ser explícitas e versionadas.
- Evidência histórica deve preservar a informação disponível no momento da análise.
- Resultados retrospectivos não devem ser usados para recalibrar silenciosamente regras ou pesos.
- Documentos experimentais, de validação e normativos devem permanecer identificáveis como classes distintas.
- A versão formal inicial dos módulos será atribuída no processo de fechamento da primeira versão do CRYPTO PRO SUITE.

## Estado atual

A governança e a documentação-base estão em consolidação. O Ranking Institucional Simplificado concluiu seus três pilotos metodológicos pré-v1.0 e entrou na fase de formalização da especificação metodológica.

---
Última atualização: 22 de setembro de 2026.
