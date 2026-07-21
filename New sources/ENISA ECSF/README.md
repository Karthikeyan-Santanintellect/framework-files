# ENISA European Cybersecurity Skills Framework (ECSF) — User Manual

Knowledge-graph CSV extraction.

## Source

- **Instrument:** *User Manual: European Cybersecurity Skills Framework (ECSF)*
- **Publisher:** European Union Agency for Cybersecurity (ENISA)
- **Publication date / version:** **September 2022** (first edition of the ECSF User Manual; no other version number is printed)
- **ISBN:** 978-92-9204-583-8 — **DOI:** 10.2824/95989 — **Catalogue:** TP-09-22-509-EN-N
- **Licence:** CC-BY 4.0
- **PDF:** `KB 2/Europe/ENISA European Cybersecurity Skills Framework User Manual.pdf`
- Extracted from a `pdftotext -layout` rendering of the PDF.

## IMPORTANT CAVEAT — scope of this document

This is the **ECSF User Manual**, not the ECSF role-profile catalogue. **The manual does not
contain the 12 full role profiles.** It defines the *template* every profile uses (Table 1:
title, alternative titles, summary statement, mission, deliverables, main tasks, key skills,
key knowledge, e-Competences), explains how to apply the profiles, and refers to them — but the
per-profile bodies of alternative titles, summary statements, missions, deliverables, tasks,
skills, knowledge and e-CF competence assignments live in the separate companion publication
*"ENISA — European Cybersecurity Skills Framework (ECSF) Role Profiles"*.

Per the verbatim-only rule, **no profile content was supplied from outside this manual.**
`nodes_ProfileItem.csv` therefore contains only the profile-level clauses the manual itself
prints verbatim:

- the **CISO mission** statement (quoted in Annex B.6, ISACA use case);
- the **eight CISO "Key knowledge" items** (quoted in Annex B.6);
- the CISO key-skills sentence from Chapter 2;
- the 12 tasks/skills/knowledge bullets from **Example II** (section 3.1), which the manual
  explicitly states are drawn from the *Cyber Legal, Policy & Compliance Officer* and
  *Cybersecurity Auditor* profiles. These are linked with rel_type `ILLUSTRATIVELY_DRAWN_FROM`
  (not `ITEM_OF_PROFILE`) because the manual attributes them to the pair jointly, not to one
  profile individually.

The 12 role-profile **names** are recoverable verbatim from the manual (Annex A.4 Table 5,
Annex B.5 list of profiles 2.1–2.6, Example III narrative). Profile numbers 2.1–2.6 are given
by the ISC2 use case; the remaining six profiles are named but not numbered in this document.
"Cybersecurity Risk Manager" is the only profile whose name appears solely in running prose
("hire a cybersecurity risk manager", "the Risk Manager"); `note`/naming is flagged accordingly.

## Schema

Bespoke to a skills/role framework rather than a statute — the document's own vocabulary
(role profile, profile component, design principle, macro area, use case, e-Competence) is used
for node type names.

### Node types

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Document.csv` | 1 | The manual itself: title, publisher, date, ISBN/DOI, licence, legal notice |
| `nodes_Section.csv` | 32 | Chapters 1–5, sub-sections, Annexes A/B and their sub-sections, with printed page numbers |
| `nodes_RoleProfile.csv` | 12 | The 12 ECSF role profiles |
| `nodes_ProfileComponent.csv` | 9 | Table 1 — the components of each ECSF role profile, with verbatim definitions |
| `nodes_ProfileItem.csv` | 22 | Clause-level, verbatim task/skill/knowledge/mission items the manual states (see caveat) |
| `nodes_Viewpoint.csv` | 2 | Workplace vs learning perspective (section 3.2) |
| `nodes_DesignPrinciple.csv` | 4 | 2.1.1–2.1.4, full verbatim text |
| `nodes_Benefit.csv` | 5 | The five numbered benefits of section 2.2 |
| `nodes_Stakeholder.csv` | 6 | Table 2 stakeholder categories |
| `nodes_StakeholderBenefit.csv` | 29 | Every bullet in Table 2, one row per bullet |
| `nodes_ApplicationStep.csv` | 5 | Figure 4 five-step guide, verbatim |
| `nodes_ApplicationExample.csv` | 6 | Table 3's three worked examples + narrative Examples I–III |
| `nodes_MacroArea.csv` | 4 | Plan / Implement / Operate / Improve (Figure 9, Example III) |
| `nodes_Term.csv` | 13 | Chapter 4 terms and definitions, verbatim, with each definition's stated source |
| `nodes_ExternalFramework.csv` | 4 | e-CF, CWA 16458 ICT Profiles, EQF, ESCO (Annex A) |
| `nodes_eCFArea.csv` | 5 | Table 4 e-CF areas |
| `nodes_eCompetence.csv` | 41 | All 41 e-CF competences from Table 4 |
| `nodes_ProficiencyLevel.csv` | 5 | e-1 … e-5 |
| `nodes_ESCOOccupation.csv` | 12 | Table 5 ESCO occupations with codes |
| `nodes_MappingRelationshipType.csv` | 3 | "is" / "might include" / "might be included", verbatim definitions + the non-equivalence caveat |
| `nodes_UseCase.csv` | 7 | Annex B use cases B.1–B.7 with contributors |
| `nodes_Reference.csv` | 19 | Chapter 5 reference list |

### Relationship types

`HAS_SECTION`, `HAS_SUBSECTION`, `DEFINES_ROLE_PROFILE`, `DEFINES_PROFILE_COMPONENT`,
`HAS_COMPONENT`, `ITEM_OF_PROFILE`, `ILLUSTRATIVELY_DRAWN_FROM`, `OF_COMPONENT`,
`COVERS_COMPONENT`, `STATES_DESIGN_PRINCIPLE`, `STATES_BENEFIT`, `HAS_BENEFIT`, `APPLIES_STEP`,
`APPEARS_IN`, `CONTAINS_ROLE_PROFILE`, `DEFINED_IN`, `CONNECTS_TO`, `HAS_AREA`,
`HAS_COMPETENCE`, `HAS_PROFICIENCY_LEVEL`, `REFERS_TO_FRAMEWORK`, `MAPS_TO_ECSF_PROFILE`,
`DEFINED_FOR_MAPPING`, `REFERENCES_ROLE_PROFILE`, `CITES`.

| File | Rows |
|---|---:|
| `rels_benefit.csv` | 5 |
| `rels_connects_to_framework.csv` | 4 |
| `rels_defines_role_profile.csv` | 12 |
| `rels_design_principle.csv` | 4 |
| `rels_document_cites.csv` | 19 |
| `rels_document_structure.csv` | 32 |
| `rels_ecf_area_has_competence.csv` | 41 |
| `rels_ecf_has_area.csv` | 5 |
| `rels_ecf_has_level.csv` | 5 |
| `rels_ecompetence_component.csv` | 1 |
| `rels_esco_maps_to_profile.csv` | 13 |
| `rels_example_in_section.csv` | 6 |
| `rels_example_step.csv` | 15 |
| `rels_macroarea_contains_profile.csv` | 12 |
| `rels_mapping_type_used.csv` | 3 |
| `rels_profile_template.csv` | 9 |
| `rels_profileitem_of_component.csv` | 22 |
| `rels_profileitem_of_profile.csv` | 34 |
| `rels_roleprofile_has_component.csv` | 108 |
| `rels_stakeholder_benefit.csv` | 29 |
| `rels_term_defined_by.csv` | 13 |
| `rels_usecase_in_section.csv` | 7 |
| `rels_usecase_references_profile.csv` | 10 |
| `rels_viewpoint_covers_component.csv` | 6 |

## Mappings to other frameworks stated by the manual

- **EN 16234-1 (e-CF):** each ECSF profile carries an `e-Competences` component; "For each
  cybersecurity role, a set of applicable e-CF competences was selected at the application
  level". The specific per-profile competence assignments are **not** printed in this manual.
- **EQF:** e-CF levels e-1 to e-5 relate to EQF learning levels 3 to 8 (EQF levels 1 and 2 are
  not relevant in this context). Captured on `nodes_ProficiencyLevel.csv`.
- **CWA 16458 European ICT Professional Role Profiles:** 30 generic ICT profiles; the ECSF
  adopts its description scheme. "Loose links" only — no concrete profile-to-profile table.
- **ESCO:** Table 5 gives 13 indicative occupation→profile mappings, extracted in full.

## Other caveats

- Table 4's area label for the D-group competences is printed as **"E. Enable"** in the source
  layout (the e-CF's own label is "D. Enable"). The printed value is kept verbatim in
  `nodes_eCFArea.csv` with a `note` column flagging it.
- Figures 1–16 are images; their content is not in the text layer, so figure captions are
  recorded as attributes rather than as extracted content.
- Annex B use cases are third-party text reproduced by ENISA; the manual states they "should not
  be considered as an endorsement or validation statement from ENISA". They are modelled as
  `UseCase` nodes with contributors, not as ECSF normative content.
- Annex B.5 renders "(ISC)²" with a superscript that the text layer drops inconsistently;
  the use-case title is stored without the superscript character.

## Validation

`check_ecsf.py` parses every CSV, asserts node-id uniqueness per file, asserts the
`<type>_id` first-column and `source_document` conventions on node files, asserts the
`source_id,target_id,rel_type` prefix on relationship files, and resolves every relationship
endpoint against the node id set. **Result: 0 errors.**
