# PCP-01 — Candidate Discovery Register

**Status:** CURRENT ADMISSION COMPLETE / SAMPLING PENDING  
**As-of:** 2026-10-01  
**Flow Vector:** FV-01 — Institutional Tokenization & Onchain Capital Markets Infrastructure

## Discovery ontology

| Code | Function |
|---|---|
| ISS | Issuance / Asset Lifecycle |
| SET | Settlement / Execution |
| INT | Interoperability / Messaging |
| DAT | Data / Oracle |
| LIQ | Liquidity / Market Infrastructure |
| CMP | Compliance / Identity / Access |

## Admission outcome

| Symbol | Admission | Next status |
|---|---|---|
| ADA | CA-PASS | eligible for sampling |
| ALGO | CA-PASS | eligible for sampling |
| APT | CA-PASS | eligible for sampling |
| ARB | CA-PASS | eligible for sampling |
| ATOM | CA-IND | outside Run A sample unless resolved in a later revision |
| AVAX | CA-PASS | eligible for sampling |
| BNB | CA-PASS | eligible for sampling |
| GNO | CA-IND | outside Run A sample unless resolved in a later revision |
| HBAR | CA-PASS | eligible for sampling |
| HYPE | CA-PASS | eligible for sampling |
| ICP | CA-IND | outside Run A sample unless resolved in a later revision |
| INJ | CA-PASS | eligible for sampling |
| LINK | CA-PASS | eligible for sampling |
| ONDO | CA-PASS | eligible for sampling |
| OP | CA-PASS | eligible for sampling |
| OSMO | CA-IND | outside Run A sample unless resolved in a later revision |
| PLUME | CA-PASS | eligible for sampling |
| POL | CA-PASS | eligible for sampling |
| QNT | CA-PASS | eligible for sampling |
| RSR | CA-PASS | eligible for sampling |
| SOL | CA-PASS | eligible for sampling |
| SUI | CA-PASS | eligible for sampling |
| SYRUP | CA-PASS | eligible for sampling |
| TRX | CA-PASS | eligible for sampling |
| XLM | CA-PASS | eligible for sampling |
| ZK | CA-PASS | eligible for sampling |

Totals:
- CA-PASS: 22
- CA-IND: 4
- CA-FAIL: 0

Detailed rationales and source references are maintained in `CURRENT-ADMISSION-REGISTER.md`.

## Sampling rule reminder

Because the admitted pool exceeds 12, deterministic stratified sampling is required.

The functional reference classes and allocation rule must be frozen **before** applying the pseudo-random draw.

Seed already pre-registered:
`PCP01-FV01`.

No asset may be manually inserted or removed because its later construct profile appears desirable or undesirable.
