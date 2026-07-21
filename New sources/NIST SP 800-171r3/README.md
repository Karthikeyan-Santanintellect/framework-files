# NIST SP 800-171r3 — knowledge-graph CSV extraction

**Source document:** NIST Special Publication 800-171r3, *Protecting Controlled Unclassified
Information in Nonfederal Systems and Organizations*, Ron Ross and Victoria Pillitteri,
National Institute of Standards and Technology, **May 2024**
(approved by the NIST Editorial Review Board 2024-04-23; supersedes SP 800-171r2).
DOI https://doi.org/10.6028/NIST.SP.800-171r3.
PDF: `KB 2/USA/NIST.SP.800-171r3.pdf`. Extracted from a `pdftotext -layout` text render.

## Schema

The document is a **control catalog**, so the schema uses the publication's own vocabulary:
*security requirement families* → *security requirements* → lettered/numbered sub-requirements,
plus the publication's distinctive *organization-defined parameters* (ODPs) and its
SP 800-53 *tailoring* apparatus.

### Node types

| Type | What it is |
|---|---|
| `Publication` | The publication itself: identifier, authors, date, DOI, supersession, and the stated derivation from SP 800-53 / the SP 800-53B moderate baseline. |
| `Section` | The narrative sections (1, 1.1, 1.2, 2, 2.1, 2.2, 3) with their verbatim prose. |
| `Family` | The 17 security requirement families of Sec. 3 (§3.1–§3.17), with the SP 800-53 family abbreviation used by the document and the `03.NN` requirement prefix. |
| `SecurityRequirement` | Every numbered requirement `03.NN.NN` (130 rows: 97 active + 33 marked *Withdrawn*). Carries the verbatim statement, the verbatim DISCUSSION text, the REFERENCES "Source Controls" and "Supporting Publications" strings, and, for withdrawn entries, the withdrawal disposition ("Addressed by …" / "Incorporated into …"). |
| `Clause` | Clause-level rows: every lettered sub-requirement (`03.01.01.a`) and every numbered sub-sub-requirement (`03.01.01.c.01`), verbatim, with parent, level and a flag for whether it embeds an ODP. Ids use the document's own Appendix D notation. |
| `ODP` | Every Organization-Defined Parameter listed in Appendix D (Table 23), with its verbatim `[Assignment: …]` / `[Selection …]` text and its Assignment/Selection operation. |
| `SourceControl` | The NIST SP 800-53 controls and control enhancements named in Appendix C and in requirement REFERENCES sections — this is the **800-53 mapping** the document states. |
| `TailoringCriteria` | The five tailoring symbols of Table 2 (CUI, NCO, FED, ORC, N/A) with their verbatim criteria. |
| `TailoringDecision` | One row per Appendix C table row (Tables 3–22): SP 800-53 control, its name, the tailoring symbol applied, and the resulting 800-171r3 security requirement (blank where the table shows "—"). |
| `Reference` | The 84 numbered bibliography entries `[1]`–`[84]`. |
| `Acronym` | Appendix A acronyms. |
| `GlossaryTerm` | Appendix B glossary terms with verbatim definitions and the bracketed source citation where given. |
| `Appendix` | Appendices A–E with their introductory text. |
| `ChangeLogItem` | The Appendix E bullet list of changes from the previous edition. |

### Relationship types

`HAS_SECTION`, `HAS_FAMILY`, `HAS_REQUIREMENT`, `HAS_CLAUSE` (requirement→clause and
clause→sub-clause), `HAS_ODP`, `ODP_APPLIES_TO_CLAUSE`, `LISTS_ODP` (Appendix D→ODP),
`DERIVED_FROM_CONTROL` (requirement→SP 800-53 source control), `SUPPORTED_BY_PUBLICATION`
(requirement→bibliography entry), `CROSS_REFERENCES` (requirement→requirement, harvested from
the `03.NN.NN` citations inside statements and discussions), `HAS_APPENDIX`,
`HAS_TAILORING_DECISION`, `TAILORS_CONTROL`, `ASSIGNED_CRITERIA`, `MAPS_TO_REQUIREMENT`,
`DEFINES_TERM`, `DEFINES_ACRONYM`, `TERM_SOURCE`, `CITES`, `HAS_CHANGE`.

## Files

| File | Rows |
|---|---|
| `nodes_Acronym.csv` | 33 |
| `nodes_Appendix.csv` | 5 |
| `nodes_ChangeLogItem.csv` | 16 |
| `nodes_Clause.csv` | 252 |
| `nodes_Family.csv` | 17 |
| `nodes_GlossaryTerm.csv` | 86 |
| `nodes_ODP.csv` | 80 |
| `nodes_Publication.csv` | 1 |
| `nodes_Reference.csv` | 84 |
| `nodes_Section.csv` | 7 |
| `nodes_SecurityRequirement.csv` | 130 |
| `nodes_SourceControl.csv` | 345 |
| `nodes_TailoringCriteria.csv` | 5 |
| `nodes_TailoringDecision.csv` | 345 |
| `rels_ASSIGNED_CRITERIA.csv` | 345 |
| `rels_CITES.csv` | 84 |
| `rels_CROSS_REFERENCES.csv` | 73 |
| `rels_DEFINES_ACRONYM.csv` | 33 |
| `rels_DEFINES_TERM.csv` | 86 |
| `rels_DERIVED_FROM_CONTROL.csv` | 157 |
| `rels_HAS_APPENDIX.csv` | 5 |
| `rels_HAS_CHANGE.csv` | 16 |
| `rels_HAS_CLAUSE.csv` | 252 |
| `rels_HAS_FAMILY.csv` | 17 |
| `rels_HAS_ODP.csv` | 80 |
| `rels_HAS_REQUIREMENT.csv` | 130 |
| `rels_HAS_SECTION.csv` | 7 |
| `rels_HAS_TAILORING_DECISION.csv` | 345 |
| `rels_LISTS_ODP.csv` | 80 |
| `rels_MAPS_TO_REQUIREMENT.csv` | 156 |
| `rels_ODP_APPLIES_TO_CLAUSE.csv` | 72 |
| `rels_SUPPORTED_BY_PUBLICATION.csv` | 199 |
| `rels_TAILORS_CONTROL.csv` | 345 |
| `rels_TERM_SOURCE.csv` | 38 |

## Notable points and caveats

- **Publication date:** May 2024. **800-53 mapping:** stated twice — per requirement in the
  REFERENCES "Source Control(s)" line (`rels_DERIVED_FROM_CONTROL.csv`, 157 pairs) and
  exhaustively in Appendix C Tables 3–22 (`nodes_TailoringDecision.csv`, 345 rows, of which 156
  map a control to a security requirement).
- 33 requirement numbers are **Withdrawn**; they are retained as nodes with `status=Withdrawn`,
  an empty `statement`, and the document's disposition sentence in `withdrawal_disposition`.
- 8 of the 80 ODPs sit on requirements that have no lettered clauses (e.g. 03.01.11, 03.13.11);
  those have no `ODP_APPLIES_TO_CLAUSE` edge but retain `HAS_ODP` to the requirement, and their
  `clause_reference` column holds the requirement id exactly as Appendix D prints it.
- Page headers/footers, page numbers and bottom-of-page **footnotes** were removed as layout
  artifacts, so footnote text is not present in the `Section` node prose. The footnote reference
  markers were superscripts in the PDF and do not survive the text render.
- The sidebar callout boxes in Sec. 2 and Sec. 3 ("ORGANIZATION-DEFINED PARAMETERS",
  "ASSESSING SECURITY REQUIREMENTS", "SCOPE AND APPLICABILITY OF SECURITY REQUIREMENTS") are
  retained inline within the enclosing `Section` node text rather than modelled separately.
- Appendix E's Table 24 (Change Log) is **empty in the source** ("The current release of this
  publication does not include any errata updates."), so no table rows were extracted; only the
  bullet list of changes is captured.
- Tables 1 (Security Requirement Families) and 2 (Tailoring Criteria) are represented by the
  `Family` and `TailoringCriteria` node files respectively rather than as separate table nodes.

## Validation

`validate.py` (run from the extraction scratch directory) parses every CSV, asserts the first
column of each node file is `<type>_id`, asserts every node id is unique, asserts the first
three columns of every relationship file are `source_id,target_id,rel_type`, and asserts every
relationship endpoint resolves to a node id. Result: **1,406 node ids, 0 errors.**
