# PCP-01 — Functional Reference Classes

**Status:** FROZEN BEFORE SAMPLE DRAW  
**As-of:** 2026-10-01  
**Purpose:** stratified sampling and later Structural Position reference sets  
**Nature:** pilot-specific; non-normative

## Principle

Functional Reference Classes describe the **primary economic role by which an admitted candidate participates in FV-01**.

They are not merit tiers, sectors, market-cap buckets, or token-quality labels.

A candidate may perform multiple FV-01 functions, but one primary class is assigned for the Pilot 01 sampling frame. Secondary functions remain visible and may later inform evidence, but do not create duplicate sample entries.

## Classes

### FR-SET — Settlement / Execution Networks

General-purpose or specialized public blockchain networks that can host, execute, settle, or administer tokenized financial assets and related capital-markets activity.

Members:

`ADA, ALGO, APT, ARB, AVAX, BNB, HBAR, OP, PLUME, POL, SOL, SUI, TRX, XLM, ZK`

Count: **15**

### FR-MID — Interoperability / Data Middleware

Infrastructure whose primary FV-01 role is connecting systems, moving messages/value, supplying validated data, or enabling cross-system settlement/interoperability.

Members:

`LINK, QNT`

Count: **2**

### FR-ISS — Issuance / Asset Structuring Protocols

Protocols whose primary FV-01 role is issuance, structuring, administration, or lifecycle management of tokenized financial assets/products.

Members:

`ONDO, RSR`

Count: **2**

### FR-MKT — Institutional Market / Liquidity / Credit Infrastructure

Protocols or networks whose primary FV-01 role is trading, liquidity, credit, borrowing/lending, or market infrastructure for institutional/onchain capital activity.

Members:

`HYPE, INJ, SYRUP`

Count: **3**

## Boundary notes

- `PLUME` is classified in FR-SET because the ranked asset is the native asset of an RWA-specialized network, despite the ecosystem also providing issuance/compliance functions.
- `INJ` is classified in FR-MKT because its primary FV-01 role in the admission evidence is capital-markets/trading infrastructure rather than generic settlement.
- `RSR` is classified in FR-ISS because the relevant admission hypothesis is tied to issuance/management of DTF structures, even though RSR also has governance/risk functions.
- `LINK` and `QNT` are not grouped with settlement networks because their primary role is middleware/interoperability.

## Venue-breadth secondary variable

The pre-registered protocol named Supported Venue Breadth as a secondary sampling variable.

For Run A, the current Supported Market Universe is Binance-only. Therefore every admitted candidate has the same supported-venue breadth at this stage.

Result:

> Supported Venue Breadth is **non-discriminating** for this draw and is retained as a recorded but inactive secondary variable.

No substitute secondary variable is introduced after seeing the candidate pool.
