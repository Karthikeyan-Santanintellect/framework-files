# MAS Technology Risk Management Guidelines — knowledge-graph CSVs

## Source document

- **Instrument:** Technology Risk Management Guidelines
- **Issuer:** Monetary Authority of Singapore (MAS)
- **Date carried on the document:** **January 2021** (cover page and every page running header read
  "JANUARY 2021"). The document refers to itself in clause 1.4 as "The revised MAS Technology Risk
  Management Guidelines".
- **Source PDF (citation only):** `KB 2/Singapore/MAS Technology Risk Management Guidelines.pdf`
- **Text used for extraction:** a `pdftotext -layout` extract of that PDF (57 pages).

## Status: Guidelines, not legally binding regulation

These are **Guidelines**, not a statute, notice or regulation, and they are **not legally binding**.
The document states its own status in section 2:

- 2.1 — the aim "is to promote the adoption of sound and robust practices for the management of
  technology risk".
- 2.2 — "The Guidelines do not affect, and should not be regarded as a statement of the standard of
  care owed by FIs to their customers. The extent and degree to which an FI implements the
  Guidelines should be commensurate with the level of risk and complexity of the financial services
  offered ... the degree of observance with the spirit of the Guidelines by an FI is an area of
  consideration by MAS."
- 2.3 — "These Guidelines provide general guidance, and are not intended to be comprehensive nor
  replace or override any legislative provisions."

Accordingly the obligation language throughout is "should", not "shall"/"must". Nothing in this
extraction should be read as a legal requirement; MAS Notices and the relevant legislation are the
binding instruments.

## Schema

The schema mirrors the document's own structure and vocabulary: numbered **Sections** (1–15) plus
lettered **Annexes** (A–C), sub-numbered **Subsections** (e.g. 3.1), and sub-sub-numbered
**Clauses** (e.g. 3.1.1), which are the guideline statements themselves. Clauses that introduce a
list carry unlabelled bullet items or lettered items `(a)`, `(b)`, `(c)`, modelled as **SubItem**.
The Guidelines have no definitions section; every defined term and explanatory gloss (e.g. "least
privilege", "multi-factor authentication", "virtualisation", "cyber range") appears in a numbered
**Footnote**, so footnotes are first-class nodes linked to the clause whose marker they carry.

Sections 1 (Preface) and 2 (Application) have no sub-headings, so their `x.y` items are Clauses
attached directly to the Section; Annex clauses (`A.1`, `A.2`, `B.1`, `C.1`) likewise attach
directly to the Annex Section node.

### Node files

| File | Rows | Description |
| --- | ---: | --- |
| `nodes_Document.csv` | 1 | The instrument itself: issuer, jurisdiction, issue date, type, self-declared status |
| `nodes_Section.csv` | 18 | Sections 1–15 and Annexes A, B, C (`kind` = Section / Annex) |
| `nodes_Subsection.csv` | 61 | Sub-headings such as 3.1 "Role of the Board of Directors and Senior Management" |
| `nodes_Clause.csv` | 255 | Clause-level guideline text, verbatim (244 numbered `x.y.z`, 7 in sections 1–2, 4 annex clauses) |
| `nodes_SubItem.csv` | 56 | Bullet and lettered items inside clauses, verbatim |
| `nodes_Footnote.csv` | 42 | All 42 footnotes verbatim — these carry the document's definitions and examples |

### Relationship files

| File | Rows | Pattern |
| --- | ---: | --- |
| `rels_document_has_section.csv` | 18 | `(Document)-[:HAS_SECTION]->(Section)` |
| `rels_section_has_subsection.csv` | 61 | `(Section)-[:HAS_SUBSECTION]->(Subsection)` |
| `rels_subsection_has_clause.csv` | 244 | `(Subsection)-[:HAS_CLAUSE]->(Clause)` |
| `rels_section_has_clause.csv` | 11 | `(Section)-[:HAS_CLAUSE]->(Clause)` for sections 1, 2 and the annexes |
| `rels_clause_has_subitem.csv` | 56 | `(Clause)-[:HAS_SUBITEM]->(SubItem)` |
| `rels_footnote_annotates_clause.csv` | 42 | `(Footnote)-[:ANNOTATES]->(Clause)` |
| `rels_clause_references_section.csv` | 3 | `(Clause)-[:REFERENCES]->(Section)` — the explicit "Refer to Annex A/B/C" cross-references in 6.1.6, 11.3.7 and 14.1.4 |

Totals: **433 nodes, 435 relationships.** All ids are unique within their file and every
relationship endpoint resolves (verified by script).

## Caveats and gaps

- **No penalties, deadlines or numeric thresholds of the usual regulatory kind.** As guidance, the
  document sets no sanctions and almost no hard figures. The few time-bound expectations it does
  state are captured verbatim in the clause text: annual security-awareness training (3.6.2), at
  least annual review of the disaster recovery plan (8.2.2), 24 by 7 monitoring of data centre
  physical and environmental controls (8.5.5), and penetration testing of internet-facing systems
  "at least once annually or whenever these systems undergo major changes" (13.2.4). Nothing has
  been added beyond what the text says.
- **Definitions live in footnotes.** There is no glossary, so no `DefinedTerm` node type was
  created; footnote text is stored verbatim and linked to the clause that carries its marker.
- **Footnote-to-clause links are marker-derived.** Superscript numbers survive `pdftotext` as inline
  digits (e.g. "framework6", "access tokens,10"), and links were matched on the same page as the
  footnote. Footnote 5 (the SDLC definition, clause 5.4.1) lost its marker entirely in the layout
  extract and was linked explicitly from its page position; all other 41 links were matched
  automatically.
- **Bullet items are unlabelled in the source.** Where a list uses plain bullets rather than
  `(a)/(b)/(c)`, SubItem ids are synthesised as `<clause>-<n>` in document order and the `label`
  column is left empty. Lettered items keep their own label.
- Page headers, footers and the table of contents were stripped; wrapped lines were rejoined into
  single-line prose with wording, punctuation and typographic quotes preserved exactly.
- Superscript footnote-marker digits remain embedded in some clause and footnote strings (an
  artefact of the PDF extract) and were deliberately not removed, since removing them would alter
  the verbatim text.
