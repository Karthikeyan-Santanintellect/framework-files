# BSI C5 — Cloud Computing Compliance Criteria Catalogue (C5:2026)

**Source document:** BSI Cloud Computing Compliance Criteria Catalogue (C5:2026), **Version 1.0.1**,
initial publication **07.04.2026**, Federal Office for Information Security (BSI), Germany.
PDF: `KB 2/Germany/BSI Cloud Computing Compliance Controls Catalogue.pdf` (~222 pages, English).
Licence stated in the document: CC BY-ND 4.0.

> Version note: although the file is named "Compliance Controls Catalogue", the document itself is the
> **C5:2026** ("Cloud Computing Compliance **Criteria** Catalogue"), version 1.0.1 — the second substantive
> revision, building on C5:2020 and aligned with EUCS Substantial / CEN/TS 18026:2024.

## Schema

The schema mirrors the catalogue's own vocabulary: *Areas* → *Criteria* → *Subcriteria* (basic /
additional sharpening / additional complementing), with *Supplementary Information* attached to criteria
and scoped by "Applicable to:" lists, plus the *General Conditions* (GC) of chapter 4 and the narrative
chapters 1–3.

### Node types

| File | Rows | Contents |
|---|---|---|
| `nodes_Instrument.csv` | 1 | The catalogue itself: title, version 1.0.1, publisher, licence, contact. |
| `nodes_Section.csv` | 32 | Narrative sections 1–5 and their numbered subsections (incl. 3.4.x audit requirements), with verbatim text. Container headings (1, 1.2, 2, 3, 3.4.5, 5) have empty text because the document places no prose under them. |
| `nodes_Definition.csv` | 69 | Every defined term from §1.2.1 (Terms related to Cloud Security) and §1.2.2 (Terms related to Audits), verbatim. |
| `nodes_Standard.csv` | 11 | The 11 standards/publications listed in §2.3 as taken into account (ISO/IEC 27001:2022, 27002:2022, 27017:2015, IT-Grundschutz-Compendium 2023, CSA CCM 4.0.12, AICPA TSP 100, ANSSI SecNumCloud v3.2, IDW RS FAIT 5, NIS2 implementing regulation annex, CEN/TS 18026:2024, NATO AC/322-D(2021)0032-REV1). |
| `nodes_Area.csv` | 17 | The 17 criteria areas (OIS, SP, HR, AM, PS, OPS, IAM, CRY, COS, PI, DEV, SSO, SIM, BCM, COM, INQ, PSS) with the verbatim objective from Table 2 / §5.x. |
| `nodes_GeneralCondition.csv` | 6 | GC-01…GC-06 with full verbatim requirement text. |
| `nodes_GeneralConditionClause.csv` | 32 | Each numbered item inside a GC requirement, as its own clause row. |
| `nodes_GeneralConditionNote.csv` | 6 | "Supplementary Information – Notes on the General Conditions" per GC. |
| `nodes_Criterion.csv` | 168 | Every criterion (e.g. `OIS-01`) with title and owning area. |
| `nodes_Subcriterion.csv` | 623 | Clause-level: every subcriterion (`OIS-01.01B`, `OIS-01.01AS`, `OIS-01.01AC`) with verbatim text and `criterion_type` = basic (462) / additional_sharpening (29) / additional_complementing (132). |
| `nodes_SupplementaryInformation.csv` | 340 | 251 "About the Criteria" blocks (each with its verbatim `applicable_to` subcriterion list) + 89 non-empty "Complementary Customer Criteria" blocks. Blocks printed as "–" are omitted. |

### Relationship types

| File | Rows | Pattern |
|---|---|---|
| `rels_instrument_has_section.csv` | 5 | Instrument -[HAS_SECTION]-> Section |
| `rels_section_has_subsection.csv` | 27 | Section -[HAS_SUBSECTION]-> Section |
| `rels_instrument_defines_term.csv` | 69 | Instrument -[DEFINES]-> Definition |
| `rels_instrument_references_standard.csv` | 11 | Instrument -[TAKES_INTO_ACCOUNT]-> Standard |
| `rels_instrument_has_area.csv` | 17 | Instrument -[HAS_AREA]-> Area |
| `rels_instrument_has_general_condition.csv` | 6 | Instrument -[HAS_GENERAL_CONDITION]-> GeneralCondition |
| `rels_general_condition_has_clause.csv` | 32 | GeneralCondition -[HAS_CLAUSE]-> GeneralConditionClause |
| `rels_general_condition_has_note.csv` | 6 | GeneralCondition -[HAS_NOTE]-> GeneralConditionNote |
| `rels_area_has_criterion.csv` | 168 | Area -[HAS_CRITERION]-> Criterion |
| `rels_criterion_has_subcriterion.csv` | 623 | Criterion -[HAS_SUBCRITERION]-> Subcriterion |
| `rels_subcriterion_sharpens.csv` | 29 | Subcriterion(AS) -[SHARPENS]-> Subcriterion(B) |
| `rels_criterion_has_supplementary_information.csv` | 340 | Criterion -[HAS_SUPPLEMENTARY_INFORMATION]-> SupplementaryInformation |
| `rels_supplementary_information_applies_to.csv` | 474 | SupplementaryInformation -[APPLIES_TO]-> Subcriterion |
| `rels_subcriterion_cross_references_criterion.csv` | 196 | Subcriterion -[CROSS_REFERENCES]-> Criterion (from "cf. XXX-nn" / "in accordance with XXX-nn" in the criterion text) |

Totals: 1,305 nodes, 2,003 relationships.

## Caveats and notes

- **Mappings to other standards.** The document does **not** contain a per-control cross-reference table.
  §2.3 lists the 11 underlying standards/publications (captured in `nodes_Standard.csv`) and states that
  "a cross-reference table of the BSI supports the mapping and is available on its website
  (https://www.bsi.bund.de/C5)". Only the ad-hoc references embedded in criterion text (e.g. ISO/IEC 27001
  sections cited inside `OIS-01.02B`) are present, and they remain inside the verbatim text rather than
  being modelled as mapping edges. §2.2 states the 17 areas are grouped "based on the structure of the
  objectives in ISO/IEC 27001:2013 Annex A".
- **No continuous-auditing section.** C5:2026 contains no "continuous auditing" criteria or notes (those
  existed in earlier C5 editions). The supplementary information present is of two kinds only —
  "About the Criteria" and "Complementary Customer Criteria" — both captured.
- **Environment / parameters.** Recovery and availability parameters are stated only in the General
  Conditions (GC-02 availability & incident handling, GC-03 recovery parameters MTPD/RTO/RPO/MBCO) and are
  captured as GC clause rows; the catalogue states no numeric thresholds for them.
- Text was rejoined from a `pdftotext -layout` extract: page headers/footers removed, wrapped lines
  rejoined, hyphenated line-break splits (e.g. "SP-\n02") repaired, and numbered list items kept inline
  within the clause they belong to (newlines collapsed to spaces per the CSV contract).
- Table 2 (areas/objectives) is a layout table; objectives were taken from the per-area "Objective:" line
  in section 5, which is the same wording in single-column form.
- Verified: all node ids unique within file, all 2,003 relationship endpoints resolve to node ids.
