# UNECE WP.29 — UN Regulation No. 155 (Cyber Security and CSMS)

## Which regulation(s) does the source actually contain?

**Only UN Regulation No. 155.** The source PDF is UN document
**E/ECE/TRANS/505/Rev.3/Add.154, 4 March 2021** — "Addendum 154 – UN Regulation No. 155",
*Uniform provisions concerning the approval of vehicles with regards to cyber security and
cyber security management system*, in force as an annex to the 1958 Agreement from
22 January 2021.

**UN Regulation No. 156** (Software Update and Software Update Management System) is
**not present** in this source. R156 is published as a separate addendum
(E/ECE/TRANS/505/Rev.3/Add.155) and none of its text — no scope, no SUMS requirements, no
RXSWIN provisions — appears anywhere in the extract (the 30-page document runs from the
R155 title page through R155 Annex 5). Accordingly **one instrument node** is modelled here,
not two. No R156 content has been supplied from outside the source.

The source states of itself: "This document is meant purely as documentation tool. The
authentic and legal binding text is: ECE/TRANS/WP.29/2020/79 (as amended by
ECE/TRANS/WP.29/2020/94 and ECE/TRANS/WP.29/2020/97)."

## Schema

The document's own vocabulary is used: numbered Sections (1–12) → Paragraphs (the numbered
sub-paragraphs, to full depth, e.g. 7.2.2.4) → SubParagraphs (the lettered items (a), (b) …).
Definitions in section 2 are also broken out as their own nodes. Annexes 1–5 (plus
Annex 1 – Appendix 1) are Annex nodes with AnnexItem children.

Annex 5 is substantive and is modelled explicitly, following the document's own three-part
structure:

- **Part A** — `ThreatCategory` (4.3.1–4.3.7) → `Threat` (the high-level numbered threats of
  Table A1) → `VulnerabilityExample` (the indexed "example of vulnerability or attack method"
  rows, e.g. 5.3, 20.4).
- **Part B / Part C** — `MitigationTable` (Tables B1–B8, C1–C3) and `Mitigation` (M1–M24),
  linked to the Part A index by `MITIGATED_BY` relationships carrying the table, the part, and
  the threat/mitigation wording exactly as stated in that table (Parts B and C reword some
  entries relative to Table A1, so both wordings are preserved).
- The eight possible attack impacts of Annex 5 paragraph 4 are `AttackImpact` nodes.

Node types: Regulation, Section, Paragraph, SubParagraph, Definition, Annex, AnnexItem,
AttackImpact, ThreatCategory, Threat, VulnerabilityExample, Mitigation, MitigationTable.

Relationship types: HAS_SECTION, HAS_PARAGRAPH, HAS_SUBPARAGRAPH, HAS_ITEM, DEFINES,
HAS_ANNEX, REFERENCES_PARAGRAPH, REFERENCES_ANNEX, CONSIDERS_POSSIBLE_ATTACK_IMPACT,
HAS_THREAT_CATEGORY, HAS_THREAT, HAS_VULNERABILITY_EXAMPLE, LISTS_VULNERABILITY,
HAS_MITIGATION_TABLE, MITIGATED_BY, COVERS_MITIGATION.

## Files

| File | Rows |
|---|---|
| nodes_Regulation.csv | 1 |
| nodes_Section.csv | 12 |
| nodes_Paragraph.csv | 91 |
| nodes_SubParagraph.csv | 31 |
| nodes_Definition.csv | 13 |
| nodes_Annex.csv | 6 |
| nodes_AnnexItem.csv | 37 |
| nodes_AttackImpact.csv | 8 |
| nodes_ThreatCategory.csv | 7 |
| nodes_Threat.csv | 30 |
| nodes_VulnerabilityExample.csv | 70 |
| nodes_Mitigation.csv | 23 |
| nodes_MitigationTable.csv | 11 |
| rels_regulation_has_section.csv | 12 |
| rels_section_has_paragraph.csv | 50 |
| rels_paragraph_has_subparagraph.csv | 41 |
| rels_paragraph_has_item.csv | 31 |
| rels_paragraph_defines_term.csv | 13 |
| rels_regulation_has_annex.csv | 6 |
| rels_annex_has_item.csv | 37 |
| rels_paragraph_references.csv | 31 |
| rels_annex_considers_impact.csv | 8 |
| rels_annex_has_threat_category.csv | 7 |
| rels_category_has_threat.csv | 30 |
| rels_threat_has_vulnerability_example.csv | 67 |
| rels_annex_lists_vulnerability.csv | 3 |
| rels_annex_has_mitigation_table.csv | 11 |
| rels_vulnerability_mitigated_by.csv | 74 |
| rels_table_covers_mitigation.csv | 34 |

Validation: every id is unique within its node file and every relationship endpoint resolves
to a node id (0 errors).

## Notable points, caveats and gaps in the source

- **Threat numbering gaps in Table A1.** The published table jumps from 13 to 15 and from 29
  to 31: there is **no threat 14 and no threat 30** in Part A. This is a gap in the source, not
  in the extraction.
- **Vulnerability references 30.1, 30.2, 30.3** appear *only* in Annex 5 Part C, Table C3
  ("Physical loss of data") with no corresponding high-level threat in Table A1. They are kept
  as VulnerabilityExample rows with `threat_id` empty, a `note` recording this, and are attached
  to Annex 5 via `rels_annex_lists_vulnerability.csv`.
- **Mitigation M17 does not exist** in the document; the mitigation references run M1–M16 and
  M18–M24.
- **Threat 22 has a single example numbered 22.2** (no 22.1) in Table A1.
- **Merged table cells.** In Tables B1–B8 and C3 several consecutive threat rows share one
  mitigation cell. Those inherited assignments are flagged with
  `mitigation_cell_merged_with_previous_row = yes` in `rels_vulnerability_mitigated_by.csv`, so
  the inference is visible rather than hidden.
- **Wording drift between parts.** Parts B and C paraphrase several Table A1 entries (spelling
  "unauthorised" vs "unauthorized", 3.5 gains "storing data in servers in garages", 32.1 becomes
  "Manipulation of OEM hardware"). Both the Table A1 text (on the node) and the Part B/C text
  (on the relationship) are stored verbatim.
- **Dated thresholds in the text**: type approvals prior to **1 July 2024** (paras 7.3.1, 7.3.4);
  Certificate of Compliance for CSMS valid a maximum of **three years** (6.7, 6.10);
  documentation retained **10 years** after production is discontinued (3.3(a), 3.3(b), 9.1.1);
  CoP verification **once every three years** (9.1.2); DETA uploads **14 days** (5.3.3, 5.3.4,
  5.3.6); manufacturer reporting **at least once a year** (7.4.1).
- **Annexes 2, 3 and 4 are blank forms/figures** (communication form, approval-mark drawing,
  certificate model). Their field labels are captured for Annex 2 and Annex 1; the graphic in
  Annex 3 cannot be represented in text and only its explanatory caption is stored.
- Footnotes (references to ISO 26262-2018, ISO/PAS 21448, ISO/SAE 21434, DETA, GRVA) were
  present in the layout extract and were excluded from clause bodies to avoid contaminating the
  verbatim text.

Source document for every row: `E/ECE/TRANS/505/Rev.3/Add.154 (4 March 2021) - UN Regulation
No. 155; PDF: KB 2/UNECE WP.29 & UN Regulation No. 155 & 156.pdf`
