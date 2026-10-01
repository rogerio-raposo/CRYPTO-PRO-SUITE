# PCP-01 — Structural Position Reference Rule

**Status:** FROZEN FOR PILOT 01  
**As-of:** 2026-10-01  
**Resolves:** MGR-001  
**Nature:** pilot operational rule; non-normative outside PCP-01

## 1. Decision

For PCP-01, **Structural Position is not measured against the Run A sample**.

The Position Reference Universe (PRU) for an asset is:

> **all CA-PASS assets in the same frozen Functional Reference Class, within the PCP-01 Supported Market Universe and the same Flow Vector / as-of context.**

Formally:

```text
PRU(asset, FV-01, T)
=
{ x :
  x ∈ SMU-PCP01
  AND CurrentAdmission(x, FV-01, T) = CA-PASS
  AND FunctionalClass(x) = FunctionalClass(asset)
}
```

The deterministic Run A sample determines **which assets receive full Ranking evaluation**, not which assets define the structural market landscape used for Position.

## 2. Why the sample cannot be the reference universe

The sample is an experimental device.

Ten CA-PASS assets were excluded by deterministic sampling, not because they lacked vector relevance. If they were removed from the Position denominator, Structural Position could change merely because of the sample draw.

That would make Position partly a function of experimental sampling rather than an economic property.

Therefore:

> **Sampling must not create or destroy Structural Position.**

## 3. Why the reference universe is not restricted to Materiality PASS

Structural Position describes the relative position of the **system/project/protocol in the Flow Vector**.

Economic Capture separately asks whether that system-level activity transmits materially to the ranked token.

Restricting the PRU to Materiality-PASS tokens would allow Economic Capture to alter the comparator landscape for Structural Position, creating construct contamination.

Example:

```text
system has major FV-01 footprint
        +
ranked token has weak Capture
        ↓
token may fail Materiality
        BUT
system remains a valid structural comparator
```

Accordingly, a CA-PASS asset can remain in the Position reference set even when its ranked token later fails the Materiality Gate.

## 4. Why CA-IND and CA-FAIL are excluded

- `CA-FAIL`: no active admissible Asset–Vector hypothesis.
- `CA-IND`: relation to FV-01 is not established with sufficient evidence.

Including either would force the Position denominator to rely on unvalidated comparators.

If a future run resolves a CA-IND asset to CA-PASS, it can enter that run's PRU prospectively. The historical PCP-01 reference set is not retroactively rewritten.

## 5. Why an unrestricted external market universe is not used

PCP-01 uses a bounded Supported Market Universe.

Introducing external comparators ad hoc after the sample is known would:
- violate source/universe governance;
- make coverage non-reproducible;
- create asymmetric evidence availability;
- reopen Candidate Discovery after freeze.

Therefore, PCP-01 Structural Position must be interpreted as:

> **position within the supported and admitted PCP-01 reference universe**, not a claim of exhaustive global market leadership.

External coverage gaps are recorded as a pilot limitation.

## 6. Reference Comparator Profile — RCP

Every member of a PRU must have enough evidence to function as a Position comparator.

Non-sampled comparators do **not** receive a full Ranking evaluation.

They receive only a lightweight:

> **Reference Comparator Profile — RCP**

An RCP may contain:
- Activity Share evidence;
- Institutional / Issuer Footprint;
- Asset / Value Footprint;
- Integration Breadth;
- Functional Centrality;
- Persistence;
- missing-data and Confidence metadata.

An RCP must not contain or imply:
- overall Ranking merit;
- Materiality Gate outcome;
- Capacity Gate outcome;
- Friction conclusion;
- Ranking Class.

## 7. Which sampled assets receive Structural Position

For efficiency and conceptual order:

- Confirmed Materiality PASS → eligible for Confirmed Position assessment.
- Provisional Materiality PASS → Position may be assessed provisionally, but cannot become a confirmed Ranking input until Materiality is confirmed.
- Confirmed Materiality FAIL → no formal Position state is needed for that asset in Run A, although it remains an RCP comparator for other assets when applicable.
- Materiality IND → Position deferred.

## 8. PCP-01 reference universes

### FR-SET

Full PRU:

`ADA, ALGO, APT, ARB, AVAX, BNB, HBAR, OP, PLUME, POL, SOL, SUI, TRX, XLM, ZK`

Run A assets requiring Position work after Materiality:
- PLUME — Confirmed PASS
- OP — Confirmed PASS
- APT — Provisional PASS
- SUI — Confirmed PASS

ADA is Materiality FAIL but remains a comparator.

### FR-MID

Full PRU:

`LINK, QNT`

Run A Position target:
- LINK — Confirmed PASS

QNT is Materiality FAIL but remains a comparator.

### FR-ISS

Full PRU:

`ONDO, RSR`

Run A Position target:
- RSR — Confirmed PASS

ONDO is Materiality FAIL but remains a comparator.

### FR-MKT

Full PRU:

`HYPE, INJ, SYRUP`

All three are Confirmed Materiality PASS and all receive Position assessment.

## 9. Anchor discipline

Structural Position keeps the existing E0–E4 / IND semantic anchors.

No state is derived mechanically from:
- ordinal rank;
- market capitalization;
- count of partnerships;
- number of chains;
- one isolated TVL/RWA metric.

E3/E4 require evidence of material relative importance and, for E4, structural centrality supported by converging evidence.

## 10. Pilot interpretation

The output must be phrased as:

> `Structural Position within FR-[class] / PCP-01 PRU`

and not:

> `global Structural Position`.

This limitation remains until the product's Supported Market Universe and coverage governance are broader and validated.
