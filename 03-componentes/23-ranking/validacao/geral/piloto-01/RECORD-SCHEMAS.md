# PCP-01 — Audit Record Schemas

**Status:** pré-registrado

## Identificadores

- `EV-xxxx` — Evidence
- `IND-xxxx` — Indicator
- `CAR-xxxx` — Construct Assessment
- `FR-xxxx` — Friction
- `GDR-xxxx` — Gate Decision
- `CMP-xxxx` — Pairwise Comparison
- `VTO-xxxx` — Veto
- `PER-xxxx` — Preference Edge
- `MGR-xxxx` — Methodological Gap

## Evidence Registry — mínimo

`evidence_id, asset_id, flow_vector_id, construct, proposition_id, indicator_id, primary_evidence_home, secondary_use, source_name, source_type, source_location, published_at, effective_at, observed_at, as_of_compatible, evidence_type, direction, freshness_status, independence_group, causal_cluster, contradiction_flag, confidence_metadata, notes`.

## Construct Assessment Record

`asset, vector, construct, applicable_propositions, applicable_indicators, evidence_ids, missing_indicators, contradictions, state, confidence, status, anchor_rationale, epistemic_blocker, reviewer, timestamp, notes`.

## Friction Assessment Record

`friction_id, asset_id, vector_scope, family, condition, causal_mechanism, primary_owner, causal_cluster, severity, confidence, lifecycle, horizon_relevance, institutional_context, effect, evidence_ids, rationale, review_trigger`.

## Gate Decision Record

Materiality:
`Exposure state/confidence, Capture state/confidence, epistemic blockers, PASS/FAIL/IND/PROVISIONAL`.

Capacity:
`Accessibility state/confidence, Absorption state/confidence, RIP, RAS, epistemic blockers, PASS/FAIL/IND/PROVISIONAL`.

## Pairwise Comparison Record

`pair_id, asset_a, asset_b, comparison_context, comparability, construct_states, deltas, friction_effects, strong_opposition, comparative_veto, epistemic_veto, support_direction, opposition_direction, decision, status, evidence_refs, rationale`.

Decisions:
- DOMINATES;
- OUTRANKS;
- EQUIVALENT;
- INCOMPARABLE;
- UNRESOLVED.

## Veto Record

`veto_id, blocked_direction, origin, delta/severity, confidence, mechanism, evidence_ids, double_count_check, epistemic_blocker_check, rationale`.

## Preference Edge Record

Somente Confirmed DOMINATES e Confirmed OUTRANKS:
`edge_id, from_asset, to_asset, relation, source_cmp_id, status`.

## Methodological Gap Record

`gap_id, stage, asset_or_pair, expected_rule, problem_encountered, temporary_treatment, impact, severity, requires_method_change`.

## Inter-rater rule

Avaliadores recebem o mesmo Evidence Pack congelado. Divergência deve ser medida e preservada antes de qualquer reconciliação.
