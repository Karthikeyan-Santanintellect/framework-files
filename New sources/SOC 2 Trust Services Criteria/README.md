# SOC 2 Trust Services Criteria — knowledge-graph CSVs

**Source document:** AICPA TSP Section 100, *2017 Trust Services Criteria for Security,
Availability, Processing Integrity, Confidentiality, and Privacy* — "This version includes
revisions made in March 2020, as discussed in the Notice to Readers."
Issued by the Assurance Services Executive Committee (ASEC) of the AICPA.
© 2020 Association of International Certified Professional Accountants.
Original PDF: `KB 2/USA/SOC 2.pdf`. Extracted from a `pdftotext -layout` render.

## Schema and why

This instrument is a **criteria catalog**, not a statute, so the schema mirrors the document's own
vocabulary and the layout of the criteria table in paragraph .24 rather than a Part/Section/Clause
statutory model.

| Node file | Type | What it holds |
|---|---|---|
| `nodes_Document.csv` | `Document` | The instrument itself: title, version/effective note, publisher, copyright. |
| `nodes_Paragraph.csv` | `Paragraph` | The numbered explanatory paragraphs `.01`–`.24` (Background, Organization of the Trust Services Criteria, Trust Services Categories, Application and Use, Professional Standards Governing Engagements). Verbatim, with the running heading they sit under. |
| `nodes_TrustServicesCategory.csv` | `TrustServicesCategory` | The five categories (Security, Availability, Processing Integrity, Confidentiality, Privacy) with their verbatim definitions from paragraph .09(a)–(e). |
| `nodes_Section.csv` | `Section` | The nine top-level headings of the criteria table: the five COSO components (CONTROL ENVIRONMENT … CONTROL ACTIVITIES) plus ADDITIONAL CRITERIA FOR AVAILABILITY / CONFIDENTIALITY / PROCESSING INTEGRITY / PRIVACY. |
| `nodes_CriteriaGroup.csv` | `CriteriaGroup` | The 12 intermediate groupings: the four supplemental-criteria groups under CONTROL ACTIVITIES (Logical and Physical Access Controls, System Operations, Change Management, Risk Mitigation) and the eight privacy sub-series headings `P1.0`–`P8.0`. |
| `nodes_Criterion.csv` | `Criterion` | All 61 criteria (`CC1.1`–`CC9.2`, `A1.1`–`A1.3`, `C1.1`–`C1.2`, `PI1.1`–`PI1.5`, `P1.1`–`P8.1`), each with its verbatim criterion text and, where the document states one, the mapped `coso_principle` (e.g. "COSO Principle 1"). |
| `nodes_PointOfFocus.csv` | `PointOfFocus` | Every point of focus — the clause-level rows — verbatim, with `name` (the bold lead-in before the em dash), `sequence` within its criterion, `applicability` (the verbatim lead-in sentence that governs it, e.g. "Points of focus specified in the COSO framework:", "Additional points of focus that apply only to an engagement using the trust services criteria for privacy:"), and `subgrouping` for the CC3.1 objective classes (Operations Objectives, External Financial Reporting Objectives, …). Nested em-dash sub-items are kept inline within the parent point-of-focus text, as in the source. |
| `nodes_Definition.csv` | `Definition` | Every defined term in Appendix A — Glossary (paragraph .25), verbatim. |

Relationships:

| Rel file | Shape |
|---|---|
| `rels_HAS_PARAGRAPH.csv` | Document → Paragraph |
| `rels_HAS_CATEGORY.csv` | Document → TrustServicesCategory |
| `rels_HAS_SECTION.csv` | Document → Section |
| `rels_HAS_GROUP.csv` | Section → CriteriaGroup |
| `rels_HAS_CRITERION.csv` | Section (or CriteriaGroup, where one exists) → Criterion |
| `rels_HAS_POINT_OF_FOCUS.csv` | Criterion → PointOfFocus |
| `rels_APPLIES_TO_CATEGORY.csv` | Criterion → TrustServicesCategory. Per paragraph .07 and the table in .07, common criteria (CC series) link to all five categories; A/PI/C/P series link to their own category only. |
| `rels_DEFINES_TERM.csv` | Document → Definition |

## Row counts

| File | Rows |
|---|---|
| nodes_Document.csv | 1 |
| nodes_Paragraph.csv | 24 |
| nodes_TrustServicesCategory.csv | 5 |
| nodes_Section.csv | 9 |
| nodes_CriteriaGroup.csv | 12 |
| nodes_Criterion.csv | 61 |
| nodes_PointOfFocus.csv | 299 |
| nodes_Definition.csv | 63 |
| rels_HAS_PARAGRAPH.csv | 24 |
| rels_HAS_CATEGORY.csv | 5 |
| rels_HAS_SECTION.csv | 9 |
| rels_HAS_GROUP.csv | 12 |
| rels_HAS_CRITERION.csv | 61 |
| rels_HAS_POINT_OF_FOCUS.csv | 299 |
| rels_APPLIES_TO_CATEGORY.csv | 193 |
| rels_DEFINES_TERM.csv | 63 |

Validation: all node ids unique within their file; all 665 relationship endpoints resolve to an
existing node id.

## Caveats and gaps

- **Version / effective date.** The document is the *2017* trust services criteria and carries no
  explicit "effective date". The only dating statements it makes are "Includes March 2020 updates"
  and the Notice to Readers wording, both recorded on the `Document` node. Nothing has been inferred.
- **Typography carries meaning that plain text loses.** Paragraph .24 states that COSO-derived
  material is in normal font, supplemental trust-services material in italics, and system-level-only
  material in bold italics. The `pdftotext` extract has no font information, so that distinction is
  not recoverable directly. It is instead captured indirectly and verbatim through the
  `applicability` lead-in sentence on each point of focus, which states the same thing in words.
- **Points of focus with nested em-dash lists** (for example `P1.1` "Communicates to Data Subjects")
  keep their sub-items inline in the single point-of-focus row rather than as separate nodes; the
  source does not number or reference those sub-items independently.
- **Criteria count** is 61: 33 common criteria (CC1.1–CC9.2), 3 availability, 2 confidentiality,
  5 processing integrity and 18 privacy criteria. `P1.0`–`P8.0` are grouping headings, not criteria,
  and are modelled as `CriteriaGroup`.
- Footnotes (`fn 1`–`fn 12`) and the running page furniture ("TSP / Ref. #" table headers, page
  numbers) were treated as layout artifacts and removed. Footnote bodies are therefore not modelled.
- Words hyphenated across line breaks by the PDF layout were rejoined; genuine hyphenated compounds
  broken at a line end (`sub-objectives`, `change-detection`) were preserved.
