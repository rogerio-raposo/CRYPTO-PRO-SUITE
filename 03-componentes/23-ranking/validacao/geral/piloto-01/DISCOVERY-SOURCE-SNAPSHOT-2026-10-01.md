# PCP-01 — Discovery Source Snapshot — 2026-10-01

**Status:** FROZEN FOR DISCOVERY STAGE  
**Purpose:** generate a high-recall candidate pool for FV-01 without assigning Materiality or merit.

## FV-01

`Institutional Tokenization & Onchain Capital Markets Infrastructure`

## Discovery sources frozen for this stage

### DS-01 — CoinGecko Real World Assets (RWA) category

Source:
`https://www.coingecko.com/en/categories/real-world-assets-rwa?items=50`

Role:
**Tier 4 / discovery only.**

The page observed on 2026-10-01 identified, among the visible leading crypto-native RWA-category tokens, the following protocol/network tokens:

`LINK, XLM, ONDO, QNT, ALGO, INJ, SYRUP, ZBCN, TRAC, PLUME, RSR`.

Tokenized representations of stocks, funds, commodities and other underlying RWAs are not treated as project-token candidates merely because they appear in the category.

After intersection with SMU-PCP01/Binance:
- retained: `LINK, XLM, ONDO, QNT, ALGO, INJ, SYRUP, PLUME, RSR`;
- absent from current Binance SMU: `ZBCN, TRAC`.

### DS-02 — CoinGecko RWA chain filters

The same discovery page exposed networks supporting RWA activity. For PCP-01, only networks with a reasonably identifiable cryptoasset and presence in the current Binance SMU are taken forward as **provisional mapping hypotheses**.

Provisional Binance-supported network candidates:

`APT, ARB, AVAX, BNB, ADA, ATOM, HBAR, HYPE, ICP, OP, OSMO, PLUME, POL, SOL, XLM, SUI, TRX, ZK, GNO`.

Networks without a clearly mapped Binance-supported rankable token at this stage are not silently mapped.

## Discovery interpretation

Presence in DS-01 or DS-02 means only:

> there is enough external discovery signal to investigate an Asset–Vector hypothesis.

It does **not** establish:
- Current Admission;
- Causal Exposure E2+;
- Economic Capture;
- institutional suitability;
- Ranking merit.

Each discovered candidate must now pass:
1. full canonical identity resolution;
2. active Asset–Vector hypothesis confirmation using admissible Tier 1–3 evidence;
3. Current Admission decision.
