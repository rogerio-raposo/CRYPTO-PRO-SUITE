# PCP-01 — PRE-T0 Relationship Assessment — Evaluator A

**Status:** FROZEN PRE-T0 ASSESSMENT  
**Evaluator:** A — primary analytical pass  
**Evidence basis:** `RUN-A-RELATIONSHIP-EVIDENCE-REGISTRY-PRET0.md`  
**Not official T0 assessment:** freshness/event review required at T0.

## Assessment rule

Sequence:

```text
EMP / active mechanism
    ↓
Causal Exposure
    ↓
Economic Capture
    ↓
Materiality Gate
```

State and Confidence remain separate. Required gas or governance utility alone does not automatically establish Capture E2+.

## Results

| Asset | Primary EMP / Capture Pathway | Exposure | Capture | PRE-T0 Materiality |
|---|---|---:|---:|---|
| PLUME | RWA-native settlement/issuance network → institutional asset activity → PLUME gas + staking/security + ecosystem utility | **E4 / C3** | **E3 / C3** | **CONFIRMED PASS** |
| OP | OP Mainnet/Superchain tokenization activity → sequencer/Superchain revenue → scoped OP buybacks | **E2 / C3** | **E2 / C3** | **CONFIRMED PASS** |
| APT | institutional tokenized funds on Aptos → network transactions → APT gas burn / staking economics | **E3 / C3** | **E2 / C2** | **PROVISIONAL PASS** |
| ADA | tokenized/RWA activity on Cardano → Cardano transactions → ADA fees/rewards | **E2 / C3** | **E1 / C3** | **CONFIRMED FAIL** |
| SUI | regulated securities/funds on Sui → network operations/storage → SUI gas + staking/storage-fund economics | **E3 / C3** | **E2 / C3** | **CONFIRMED PASS** |
| LINK | institutional tokenization/data/interoperability use → Chainlink service revenue → Payment Abstraction/LINK + staking | **E3 / C4** | **E3 / C4** | **CONFIRMED PASS** |
| QNT | institutional interoperability/tokenized-deposit use → Overledger access/subscription → optional QNT payment | **E3 / C3** | **E1 / C3** | **CONFIRMED FAIL** |
| ONDO | Ondo tokenized securities/funds → Ondo product activity → ONDO governance mainly at DAO/Flux layer | **E4 / C4** | **E1 / C3** | **CONFIRMED FAIL** |
| RSR | DTF issuance/management → DTF fees/revenue/risk capital → RSR staking/rewards + buy-and-burn | **E3 / C3** | **E3 / C4** | **CONFIRMED PASS** |
| INJ | tokenization/trading/receivables on Injective → onchain revenue → recurring INJ buyback/burn + staking | **E2 / C3** | **E2 / C3** | **CONFIRMED PASS** |
| HYPE | tokenized-equity trading on HyperCore → trading fees → automated HYPE purchases/burn | **E2 / C3** | **E2 / C3** | **CONFIRMED PASS** |
| SYRUP | institutional onchain credit/asset management → protocol revenue → rules-based SYRUP buybacks + governance | **E4 / C4** | **E3 / C4** | **CONFIRMED PASS** |

## Anchor rationales

### PLUME
**Exposure E4:** FV-01 is structural to Plume's present economic identity; institutional/RWA issuance, distribution and productive use are not peripheral products.

**Capture E3:** PLUME is required for gas and network security and is integrated into ecosystem utility. The mechanism is recurring and directly tied to network use, but the pack does not demonstrate that vector-driven monetary demand is so dominant as to justify E4.

### OP
**Exposure E2:** tokenization/institutional finance is active and economically relevant on OP Mainnet/OP Stack, but it remains one vertical within a much broader Superchain.

**Capture E2:** an executed buyback mechanism links scoped Superchain revenue to OP demand. The link is material and real, but incomplete: OP Enterprise revenue is outside the current buyback scope.

### APT
**Exposure E3:** several major institutional tokenized funds are live on Aptos; this is recurring rather than an isolated proof of concept.

**Capture E2 / C2:** APT gas is burned and network utilization can reduce supply, but the pack does not isolate the contribution of FV-01 activity and Aptos itself notes very low transaction fees. The mechanism is plausible for E2 but not sufficiently evidenced for C3 confirmation.

### ADA
**Exposure E2:** Cardano has current programmable-token infrastructure and active RWA use cases.

**Capture E1:** ADA is technically required for fees/rewards, but the pack does not demonstrate that current FV-01 activity produces economically material ADA transmission beyond incidental network fees.

### SUI
**Exposure E3:** institutional securities infrastructure is actively integrating with Sui, with issuance/trading/settlement capabilities.

**Capture E2:** SUI is required for gas and network security, while storage demand also enters network economics. This creates a current direct transmission pathway; evidence does not support E3 vector-specific materiality.

### LINK
**Exposure E3:** institutional tokenization is a major recurring use of Chainlink, but Chainlink also has substantial non-FV-01 oracle/DeFi functions, so E4 is not required.

**Capture E3:** enterprise/onchain service revenue is programmatically converted into LINK and LINK participates in service payment/security. This is a recurring direct economic linkage; E4 is withheld because the pack does not show that FV-01 alone is structurally dominant in total LINK economics.

### QNT
**Exposure E3:** Quant is directly integrated into tokenized-deposit/digital-bond capital-markets workflows.

**Capture E1:** current Quant materials permit platform payment in USD or QNT. The evidence therefore does not establish QNT as a necessary or materially recurring economic transmission channel for institutional FV-01 usage.

### ONDO
**Exposure E4:** tokenized finance is the core current economic purpose of the Ondo ecosystem.

**Capture E1:** ONDO governance rights are documented, especially around Ondo DAO/Flux, but no current direct transmission from the principal tokenized-securities products to ONDO through mandatory use, fees, staking, buyback or burn is demonstrated.

### RSR
**Exposure E3:** tokenized asset baskets/DTFs and their financial administration are a recurring central Reserve activity.

**Capture E3:** DTF activity can require RSR risk capital/governance and protocol fees can buy and burn RSR; this is a material recurring pathway.

### INJ
**Exposure E2:** real commercial receivables and tokenized-asset initiatives are active, but FV-01 is still one portion of Injective's broader trading/finance activity.

**Capture E2:** onchain revenue funds INJ buybacks/burns and INJ secures/governs the network. The pathway is direct, but vector-specific revenue share is not isolated.

### HYPE
**Exposure E2:** live tokenized-equity trading establishes a real relationship, but it is peripheral relative to Hyperliquid's much larger crypto trading activity.

**Capture E2:** trading fees feed an automated HYPE purchase-and-burn mechanism, so tokenized-equity trading has a direct route to HYPE demand/burn. Current FV-01 scale is not sufficient for E3.

### SYRUP
**Exposure E4:** institutional/onchain credit and asset management are Maple's core economic activity.

**Capture E3:** current rules-based revenue buybacks create a direct recurring connection between protocol revenue and SYRUP; the linkage is active and observable.

## PRE-T0 gate summary

- Confirmed PASS: **8**
  - PLUME
  - OP
  - SUI
  - LINK
  - RSR
  - INJ
  - HYPE
  - SYRUP
- Provisional PASS: **1**
  - APT
- Confirmed FAIL: **3**
  - ADA
  - QNT
  - ONDO
- IND: **0**

## Important interpretation

A Confirmed FAIL here does not mean a weak project or weak tokenized-asset ecosystem.

It means:
> under the current PCP-01 construct definition, the evidence does not support a material enough economic transmission from FV-01 activity to the **ranked token**.

That distinction is the intended purpose of the Economic Capture construct.
