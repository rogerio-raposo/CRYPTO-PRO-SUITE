# PCP-01 — Run A Sample Record

**Status:** FROZEN  
**Protocol commit:** `022fba8f087a474185f7522bcb0c8ab5a68dc0c9`  
**Seed:** `PCP01-FV01`  
**Algorithm:** SHA-256 ascending  
**Population:** 22 CA-PASS assets  
**Sample:** 12 assets

## Allocation

| Functional class | Population | Sample |
|---|---:|---:|
| FR-SET | 15 | 5 |
| FR-MID | 2 | 2 |
| FR-ISS | 2 | 2 |
| FR-MKT | 3 | 3 |
| **Total** | **22** | **12** |

## FR-SET deterministic ordering

The hash input was:

`PCP01-FV01|FR-SET|<canonical_asset_id>`

| Rank | Asset | SHA-256 | Selected |
|---:|---|---|---|
| 1 | PLUME | `072db71004d8945772593cdf7fe693a13ad0912f179ea366ab91c024accbf242` | YES |
| 2 | OP | `15689a6508c211b6cc804ca84540999050861c244bd777199f1d0eaed23c337e` | YES |
| 3 | APT | `1c385f1503a9b5d1c9ab3d343edf3d0447e7ba861368b3eadde62a66a0c5ab8a` | YES |
| 4 | ADA | `2434e1a8ade82834e86904fb8fcd5a7bab7301ae0a39ddca77efe185be134c68` | YES |
| 5 | SUI | `481acdb19305f850a185ee60422934f89d4eb606b08d906a8fef96617ae9eb21` | YES |
| 6 | ZK | `6dacb90d76e7b8c91e0700b1a754cb34f343daa233e1b17f800b3c6fddcae9cd` | NO |
| 7 | POL | `79036a5bc8591abf9f21ab07a0040131e84cf4dd0cb098bc4afc470db0ef5120` | NO |
| 8 | HBAR | `8d5923aef9c1cfd631f1555dcb679f4d90be210107f26f4c0a3fde01e2ba9c80` | NO |
| 9 | XLM | `9b93842ca440514afdfd3a8e9dba2fccb17ff83d3cb3536b7bdc8c9a4a50b0ab` | NO |
| 10 | SOL | `ab282e1afd6242e92de024bb51881e25a524a267f49539fe64632efd03e5f467` | NO |
| 11 | TRX | `bdb8a63203a30d4fa724924f0d240687bd385b6c2dc7f136c37a0a3d8ddc2dbb` | NO |
| 12 | BNB | `bee3c24a6118e95f8afb5cc854a501b92ed7dcc40509b9e815f7a17a3a99930b` | NO |
| 13 | ALGO | `c8d90866b2e0b6478b12dc40a7096d1d78fddae0773161065586298bbb1dabe5` | NO |
| 14 | ARB | `d17988829aaaad0aac7adcb150dbf079018c10528bd2fb6d4bb21579740a80ea` | NO |
| 15 | AVAX | `e4d1446712c235011bfbdd63af79223392ba9cc79a5f87a2e245dc7ef6e2b191` | NO |

## Small classes

Because their population size was <= 3, every member was included by the frozen allocation rule.

### FR-MID
- LINK
- QNT

### FR-ISS
- ONDO
- RSR

### FR-MKT
- INJ
- HYPE
- SYRUP

## Frozen Run A sample

```text
PLUME
OP
APT
ADA
SUI
LINK
QNT
ONDO
RSR
INJ
HYPE
SYRUP
```

## Non-selected CA-PASS population

```text
ZK
POL
HBAR
XLM
SOL
TRX
BNB
ALGO
ARB
AVAX
```

These remain admitted assets and may be used in later pilots/sensitivity tests. Their exclusion from Run A is solely the deterministic sampling result and must not be interpreted as lower merit.

## Sample lock

No selected asset may be replaced because later:
- evidence is inconvenient;
- a gate fails;
- liquidity is poor;
- the asset produces IND;
- the final graph becomes less orderly.

A hard identity/scope invalidation must be recorded as an event, not silently replaced.
