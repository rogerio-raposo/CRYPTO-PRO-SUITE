# Pending Items and Divergences Register (RPD)

Status: **WORKING / NON-NORMATIVE**  
Checkpoint: 2026-09-22

| RPD | Subject | Status |
|---|---|---|
| RPD-2026-0001 | Pilot provenance error: Macro/Rotation/Ranking/CSE events initially attributed to SRC-0001 | **RESOLVED** |
| RPD-2026-0002 | Ranking methodological continuity pending latest/full `Roadmap do Crypto Pro` source | **RESOLVED — SOURCE RECOVERED** |
| RPD-2026-0003 | Historical collision involving ED-001 | **DIVERGENT / OPEN** |
| RPD-2026-0004 | Exact original content of `00 - Constituição — Draft 0.1` not recovered from SRC-0005 | **OPEN** |
| RPD-2026-0005 | Exact original content of `Protocolo Editorial — Draft 0.1` not recovered from SRC-0006 | **OPEN** |
| RPD-2026-0006 | Constitution v1.0 referenced by Manual Metodológico: SRC-0004 proves that a Constitution v1.0 was treated as an already concluded artifact before the Manual was generated, but the exact file/content is not present in the recovered documentary corpus. Possible relationship with Arquitetura v1.0 remains unproven. | **REFINED / OPEN** |
| RPD-2026-0007 | Legacy module-versioning roadmap versus later decision to defer formal module versioning until Suite launch | **OPEN** |

## Handling rule

An RPD is not silently normalized. Resolution requires evidence, an explicit present decision where appropriate, or a documented determination that the historical state cannot be recovered.


## RPD-2026-0006 — Evidence review (SRC-0004)

A targeted review of `SRC-0004 — Concepção + Sprint 0` found direct historical references that materially refine this pending item:

- immediately before generating the Methodological Manual, the assistant states that it will be aligned to **“Constituição v1.0”**;
- shortly afterward, the project status explicitly lists **“Constituição da CRYPTO PRO SUITE v1.0”** as **concluded**;
- later, the proposed Foundation Edition also lists **“Constituição v1.0”** as an existing/concluded document;
- only afterward does the conversation evolve through CSE/three-layer architecture and produce **Constituição v1.1**;
- still later, the Marco Zero editorial reset explicitly calls for a new **“00 - Constituição v1.0”**, demonstrating that version labels were reused/reset during the project's evolution.

### Determination

The evidence supports the historical existence **as a recognized project artifact/state** of a pre-v1.1 Constitution v1.0. It does **not** establish that `Arquitetura v1.0` and that Constitution were the same file or the same text.

Therefore:

- do not equate `CPS_Arquitetura_v1.0.md` with the missing Constitution v1.0 without further evidence;
- do not describe Constitution v1.0 as merely an erroneous reference in the Manual;
- keep the RPD open for recovery of the exact artifact/content or stronger identity evidence;
- distinguish this early Constitution v1.0 from the later Marco Zero reuse/reset of the v1.0 version label.


## RPD-2026-0002 — Refinement after SRC-0018

`SRC-0018 — Ranking Institucional Simplificado — Microcaps — Metodologia — Draft 0.1` (22/09/2026) provides a current versioned methodological artifact for the **Microcaps submethodology only**.

It explicitly states that it is normative only for Microcaps and does not define the complete Ranking Institucional Simplificado methodology. Therefore the RPD cannot be closed.

A material succession is now documented:

- earlier SRC-0002 / RH-0032–0033: futures/perpetual market availability became a Microcaps eligibility requirement;
- SRC-0018: **futures/perpetuals are not an eligibility filter** and Operability is parallel to Potential.

This is treated as methodological evolution/supersession, not as correction of the earlier historical record.

The complete Roadmap export was subsequently recovered. The source gap that motivated this RPD is therefore resolved. This does **not** mean that the complete Ranking methodology is itself closed; it means the missing-source condition has been removed and the recovered continuation can now be used to reconstruct the deliberative path.


## RPD-2026-0008 — Misnamed Ranking validation DOCX / content duplicates Microcaps methodology

**Status:** RESOLVED — DOCUMENTARY HYGIENE

**Observed artifact:** `03-componentes/23-ranking/validacao/Ranking_Institucional_Simplificado_Validacao_Metodologica_Draft_0.1.docx` (GitHub blob SHA `39afbcd1e70c890633f8186dc03965b76e8185d4`).

A copy supplied directly for inspection contains **Ranking Institucional Simplificado — Microcaps — Metodologia — Draft 0.1**, explicitly normative only for Microcaps and explicitly not the complete Ranking methodology. Its substantive content corresponds to SRC-0018 rather than to a general Ranking validation document.

**Reconstruction treatment:** do not register the DOCX as a new historical source and do not infer existence of a completed general Ranking validation from its filename. Treat it as an apparent filename/content mismatch or misplaced duplicate until repository hygiene is resolved.

**Impact:** reinforces that the full Ranking methodology remains open; does not close RPD-2026-0002.

**Resolution:** the misnamed/misplaced DOCX was removed from `03-componentes/23-ranking/validacao/` by the repository owner after the mismatch was identified. The historical RPD is retained for auditability; no SRC or RH was created from the duplicate artifact.


## RPD-2026-0009 — Complete SRC-0017 recovered but canonical archive replacement pending

**Status:** OPEN — OPERATIONAL PERSISTENCE

The complete `Roadmap do Crypto Pro` conversation was recovered from the 2026-09-21 export and examined through the canonical `current_node` ancestry chain.

- recovered canonical textual messages: **517**;
- recovered source period: **2026-09-15–2026-09-20**;
- the terminal user message `Sig` is incomplete in the original conversation because that conversation ended abnormally after the ChatGPT conversation-time limit was reached;
- this terminal condition is not treated as export truncation.

The repository currently still contains the earlier 217-message archival copy at `archive/historical-sources/conversations/roadmap-do-crypto-pro.md`. The complete Markdown is approximately 1 MB and could not be safely replaced through the current text-write connector in this session.

**Resolution condition:** replace the archived conversation file with the complete 517-message canonical Markdown and update its manifest/integrity metadata. Historical analysis in the meantime must use the recovered complete source, not infer absence from the older repository copy.
