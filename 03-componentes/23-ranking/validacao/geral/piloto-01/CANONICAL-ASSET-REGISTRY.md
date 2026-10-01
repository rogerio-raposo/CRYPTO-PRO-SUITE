# PCP-01 — Canonical Asset Registry

**Status:** economic identity resolution complete for Discovery Pool  
**As-of:** 2026-10-01  
**Scope:** PCP-01 / FV-01  
**Nature:** validation artifact; non-normative

## Identity rule used in this stage

The purpose of canonicalization here is to resolve the **economic cryptoasset being assessed**, not to build an exhaustive multi-chain contract registry.

A record may therefore be `RESOLVED_ECONOMIC_IDENTITY` even when every bridge/wrapped contract address is not enumerated. Before any onchain contract-specific evidence is used, that contract must still be verified against an authoritative source.

Ticker alone remains insufficient for formal assessment.

## Registry

| canonical_asset_id | symbol | canonical economic identity | asset role | identity status |
|---|---|---|---|---|
| CPS-ADA | ADA | Cardano native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ALGO | ALGO | Algorand native token (Algo) | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-APT | APT | Aptos native token | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ARB | ARB | Arbitrum governance token / Arbitrum ecosystem asset | governance/ecosystem token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ATOM | ATOM | Cosmos Hub native staking/governance asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-AVAX | AVAX | Avalanche native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-BNB | BNB | BNB Chain native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-GNO | GNO | Gnosis ecosystem governance/native staking asset | ecosystem/network asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-HBAR | HBAR | Hedera native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-HYPE | HYPE | Hyperliquid native token | network-native/protocol asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ICP | ICP | Internet Computer native token | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-INJ | INJ | Injective native token | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-LINK | LINK | Chainlink token | middleware/protocol token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ONDO | ONDO | Ondo Finance governance/ecosystem token | protocol/ecosystem token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-OP | OP | Optimism governance token / OP ecosystem asset | governance/ecosystem token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-OSMO | OSMO | Osmosis native token | network/protocol asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-PLUME | PLUME | Plume native token | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-POL | POL | Polygon ecosystem token | network/ecosystem asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-QNT | QNT | Quant Network token | infrastructure/protocol token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-RSR | RSR | Reserve Rights token | protocol/governance token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-SOL | SOL | Solana native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-SUI | SUI | Sui native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-SYRUP | SYRUP | Maple Finance governance token | protocol/governance token | RESOLVED_ECONOMIC_IDENTITY |
| CPS-TRX | TRX | TRON native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-XLM | XLM | Stellar native asset | network-native asset | RESOLVED_ECONOMIC_IDENTITY |
| CPS-ZK | ZK | ZKsync native ecosystem/governance asset | network/ecosystem asset | RESOLVED_ECONOMIC_IDENTITY |

## Identity evidence notes

Particular identity checks that matter for ambiguity/migration:

- **ALGO:** Algorand identifies Algo as the native token of the Algorand blockchain.
- **HYPE:** Hyperliquid documentation identifies HYPE as the network token used for security/network costs.
- **PLUME:** Plume identifies PLUME as the native token used for gas, governance, staking and ecosystem access.
- **RSR:** Reserve documentation identifies RSR as Reserve Rights, used for governance/risk/value-accrual functions.
- **SYRUP:** Maple documentation identifies SYRUP as the current governance token; legacy MPL/xMPL no longer carry governance utility.
- **ZK:** ZKsync identifies ZK as the network's native ecosystem asset/governance token.

## Limitation

This registry resolves economic identity only. It does not claim that the ranked token economically captures the activity of the associated network/protocol. That question belongs to the later **Economic Capture** construct.
