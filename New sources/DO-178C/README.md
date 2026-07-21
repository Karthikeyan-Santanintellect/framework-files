# DO-178C — knowledge-graph extraction

## What the source document actually is

**The source is NOT the RTCA DO-178C standard.** It is a commercial marketing ebook published
by **Parasoft**, titled *"DO-178C Software Compliance for Aerospace & Defense"* (94 pages). It is
a condensed third-party overview of DO-178C interleaved with promotion of Parasoft's test
automation products (C/C++test, DTP, SOAtest, Virtualize, ASMTools, Qualification Kits).

The ebook says so in its own words: *"This ebook provides a condensed overview of each of the
DO-178C sections, highlighting the key takeaways."*

Consequences for this extraction:

- There is **no clause-level normative text** of DO-178C in the source. DO-178C's own numbered
  sections (2–12) appear only as one- or two-paragraph third-party summaries.
- The **Annex A objectives tables (A-1 … A-10) are reproduced only as page images.** The
  `pdftotext -layout` extract contains nothing but their captions. Objective statements, their
  applicability by software level, independence markings, and control categories are therefore
  **absent from the source and are NOT in these CSVs.** Supplying them would have required
  inventing content, which the contract forbids.
- **Software levels A–E** are likewise only summarised in prose (Table 2-1 is an image). Verbatim
  descriptions exist for levels A, B and E; the cells for C and D are empty because the source
  says nothing about them.
- There is **no glossary** in the source. `nodes_Definition.csv` holds the terms the ebook itself
  defines or quotes inline, not the DO-178C glossary.

So the schema below models **what is actually present**: the ebook's own heading hierarchy plus
the DO-178C artefacts it names, always tagged as "as described in the ebook".

## Schema

Bespoke to this document. Node types (file → meaning):

| File | Node type | What it is |
|---|---|---|
| `nodes_Document.csv` | Document | The ebook itself, typed as vendor guidance |
| `nodes_Section.csv` | Section | The ebook's own heading tree (levels 1–4), verbatim body prose |
| `nodes_StandardSection.csv` | StandardSection | DO-178C's own sections 1–12, with the ebook's description of each |
| `nodes_ObjectivesTable.csv` | ObjectivesTable | Annex A tables A-1…A-10 (captions only — see caveats) |
| `nodes_SoftwareLevel.csv` | SoftwareLevel | Software levels / DAL A–E |
| `nodes_LifeCycleProcess.csv` | LifeCycleProcess | Planning / development / integral processes and their sub-processes |
| `nodes_LifeCycleData.csv` | LifeCycleData | The Section 11 software life cycle data items |
| `nodes_PlanningOutput.csv` | PlanningOutput | Documents listed as Table A-1 expected outputs |
| `nodes_SCMActivity.csv` | SCMActivity | The seven Section 7 configuration management activities |
| `nodes_ControlCategory.csv` | ControlCategory | CC1 / CC2 |
| `nodes_ToolQualificationLevel.csv` | ToolQualificationLevel | TQL-1 … TQL-5 |
| `nodes_ToolCriterion.csv` | ToolCriterion | Tool impact Criteria 1–3 (verbatim) |
| `nodes_ToolQualificationStep.csv` | ToolQualificationStep | DO-330 key steps as listed by the ebook |
| `nodes_CoverageType.csv` | CoverageType | Statement / branch / MC-DC / object code coverage |
| `nodes_CitedClause.csv` | CitedClause | Specific DO-178C clause numbers the ebook cites (6.3.4, 6.4.4.2, 11.8 …) |
| `nodes_TypicalError.csv` | TypicalError | Errors the ebook attributes to DO-178C for unit and integration testing |
| `nodes_RelatedStandard.csv` | RelatedStandard | DO-330/331/332/333, DO-254, DO-278A, DO-326A, ARP4754A, AS9100D, MISRA, CERT, CWE, earlier DO-178 revisions |
| `nodes_CWEWeakness.csv` | CWEWeakness | The 2023 CWE Top 25 (the one full data table present as text) |
| `nodes_Definition.csv` | Definition | Terms defined or quoted inline |
| `nodes_GuidanceElement.csv` | GuidanceElement | The six kinds of guidance DO-178C provides |
| `nodes_Exhibit.csv` | Exhibit | Figure and table captions |
| `nodes_Resource.csv` | Resource | The "More Resources" bibliography |
| `nodes_VendorProduct.csv` | VendorProduct | Parasoft products named (recorded so the promotional layer is explicit, not hidden) |

Relationship types: `HAS_SECTION`, `HAS_SUBSECTION`, `DESCRIBES_STANDARD_SECTION`,
`PRESENTS_OBJECTIVES_TABLE`, `DEFINES_SOFTWARE_LEVEL`, `INCLUDES_PROCESS`, `HAS_SUBPROCESS`,
`PRODUCES_LIFE_CYCLE_DATA`, `HAS_EXPECTED_OUTPUT`, `HAS_ACTIVITY`, `ASSIGNS_CONTROL_CATEGORY`,
`DEFINES_TOOL_CRITERION`, `DEFINES_TOOL_QUALIFICATION_LEVEL`, `PRESCRIBES_STEP`,
`LISTS_COVERAGE_TYPE`, `REQUIRED_AT_SOFTWARE_LEVEL`, `REFERENCES_STANDARD`, `CITES_CLAUSE`,
`REVEALS_TYPICAL_ERROR`, `LISTS_WEAKNESS`, `DEFINES_TERM`, `PROVIDES_GUIDANCE`, `LISTS_RESOURCE`,
`PROMOTES_PRODUCT`.

## Files and row counts

### Nodes (416 ids, all unique)

| File | Rows |
|---|---|
| nodes_CWEWeakness.csv | 25 |
| nodes_CitedClause.csv | 18 |
| nodes_ControlCategory.csv | 2 |
| nodes_CoverageType.csv | 4 |
| nodes_Definition.csv | 12 |
| nodes_Document.csv | 1 |
| nodes_Exhibit.csv | 55 |
| nodes_GuidanceElement.csv | 6 |
| nodes_LifeCycleData.csv | 22 |
| nodes_LifeCycleProcess.csv | 11 |
| nodes_ObjectivesTable.csv | 10 |
| nodes_PlanningOutput.csv | 9 |
| nodes_RelatedStandard.csv | 19 |
| nodes_Resource.csv | 32 |
| nodes_SCMActivity.csv | 7 |
| nodes_Section.csv | 114 |
| nodes_SoftwareLevel.csv | 5 |
| nodes_StandardSection.csv | 12 |
| nodes_ToolCriterion.csv | 3 |
| nodes_ToolQualificationLevel.csv | 5 |
| nodes_ToolQualificationStep.csv | 8 |
| nodes_TypicalError.csv | 24 |
| nodes_VendorProduct.csv | 12 |

### Relationships (390 rows)

| File | Rows |
|---|---|
| rels_cites_clause.csv | 18 |
| rels_coverage.csv | 5 |
| rels_defines_software_level.csv | 5 |
| rels_defines_term.csv | 12 |
| rels_describes_standard_section.csv | 11 |
| rels_has_section.csv | 114 |
| rels_lists_resource.csv | 32 |
| rels_lists_weakness.csv | 25 |
| rels_planning_output.csv | 9 |
| rels_presents_objectives_table.csv | 10 |
| rels_process_structure.csv | 11 |
| rels_produces_life_cycle_data.csv | 22 |
| rels_promotes_product.csv | 12 |
| rels_provides_guidance.csv | 6 |
| rels_references_standard.csv | 28 |
| rels_scm.csv | 9 |
| rels_tool_qualification.csv | 17 |
| rels_typical_error.csv | 24 |

## Source

- Source PDF: `KB 2/USA/DO-178C Software Considerations in Airborne Systems.pdf`
- Text used: `pdftotext -layout` extract, 3,952 lines / 94 pages.
- `source_document` on every node row records the PDF path above.

## Caveats and gaps

1. **Not the standard.** See the first section. Anything requiring DO-178C's normative wording
   must be sourced from the actual RTCA/EUROCAE publication.
2. **Annex A objective rows are unavailable** — images only in the PDF. `nodes_ObjectivesTable.csv`
   carries an explicit `content_available_in_source` column saying so. Tables A-1…A-10 are present
   as ten nodes with their captioned titles and their owning DO-178C section, and nothing more.
   The same applies to Table 2-1 (DAL table), Table 2-10 (CC1/CC2 data map) and Table 2-13 (tool
   qualification level determination).
3. **Software levels C and D have empty description cells** — the source characterises only A, B
   and E.
4. **No glossary** in the source, so no glossary extraction.
5. **Objectives counts.** The only numeric claim about objectives in the text is "There are seven
   objectives that must be satisfied based on the software level (A-D)" for Table A-1; it is
   captured in the body text of the Section-4 node, not as structured objective rows.
6. **Layout artefacts.** The PDF places figure/table captions in a left margin gutter that
   `pdftotext -layout` interleaves with body text. The build script strips gutter columns
   heuristically; one badly interleaved passage (Section 2, Figure 2-2 caption) was repaired by
   explicit string surgery. A small number of caption fragments may survive elsewhere in
   `nodes_Section.csv` body text. No wording was rewritten — only page numbers, running headers
   and caption fragments were removed, and line breaks collapsed to single spaces.
7. **Bullet markers.** The source's `»` bullet glyph was normalised to `-` inside body text; list
   items are joined into single-line prose. Ligature `ﬁ` and curly apostrophes were normalised.
8. **Seven Section nodes have empty `text`** (S001, S025, S037, S042, S084, S107, S108). These are
   pure container headings immediately followed by a subheading; an empty cell is correct.
9. **Vendor content is retained, not filtered.** Roughly half the ebook is Parasoft product
   marketing. It is preserved verbatim in the Section bodies and surfaced as `VendorProduct`
   nodes so that downstream consumers can exclude it deliberately.

## Validation

`scratchpad/work_do178c/check.py` parses every CSV, asserts id uniqueness within each node file,
asserts every relationship endpoint resolves, and prints row counts. Result: **416 node ids, 0
duplicates, 0 unresolved relationship endpoints.**
