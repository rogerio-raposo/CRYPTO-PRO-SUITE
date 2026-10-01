# PCP-01 — Reference Comparator Profile Schema

**Status:** FROZEN FOR PILOT 01  
**Purpose:** provide the minimum evidence needed to assess Structural Position without performing a full Ranking evaluation for non-sampled comparators.

## Required fields

| Field | Meaning |
|---|---|
| rcp_id | persistent comparator-profile ID |
| canonical_asset_id | economic asset identity |
| functional_class | frozen FR class |
| flow_vector_id | FV-01 |
| as_of | evidence cut |
| admission_status | must be CA-PASS |
| sample_status | RUN_A / NON_SAMPLED |
| activity_share_evidence | comparable vector-activity evidence, if available |
| institutional_issuer_footprint | issuers/institutions and deployment significance |
| asset_value_footprint | tokenized asset/value footprint, if methodologically comparable |
| integration_breadth | breadth of relevant production integrations |
| functional_centrality | evidence that the system is difficult to bypass or central to the function |
| persistence | one-off / recurring / established |
| evidence_ids | supporting evidence |
| missing_fields | unavailable comparator dimensions |
| confidence | C0–C4 for comparator adequacy |
| notes | limitations / denominator issues |

## Evidence states

A comparator field may be:
- `OBSERVED`
- `OBSERVED_ZERO`
- `N/A`
- `MISSING`
- `EXCLUDED`

Missing data is not converted to zero.

## Comparator adequacy

- **RCP-C3+**: enough evidence for the asset to function as a reliable Position comparator.
- **RCP-C2**: usable only with caution; may make Position provisional.
- **RCP-C0/C1**: insufficient; if the missing comparator could materially change the sampled asset's Position, that Position must remain IND/provisional.

## Anti-contamination rule

RCP evidence may be used for Structural Position only.

A non-sampled comparator does not acquire an E-state for Exposure, Capture, Accessibility, Absorption, Frictions or overall Ranking merely because Position evidence was collected.
