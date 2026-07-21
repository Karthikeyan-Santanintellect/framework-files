# Kenya Data Protection Act (No. 24 of 2019) — knowledge-graph CSVs

**Source document:** Kenya Data Protection Act (No. 24 of 2019), Laws of Kenya, published by the
National Council for Law Reporting with the Authority of the Attorney-General
(`KB 2/Africa/Kenya Data Protection Act.pdf`).
Date of assent: 8th November, 2019. Date of commencement: 25th November, 2019.

All text in these CSVs is verbatim from that source.

## Schema

The Act's own structure is Parts → numbered Sections → subsections `(1)` → paragraphs `(a)` →
subparagraphs `(i)`, with an Interpretation section (s. 2) and two Schedules. The schema mirrors
that vocabulary rather than a generic template.

### Node types
| File | Type | Notes |
|---|---|---|
| `nodes_Act.csv` | `Act` | Single root node: title, act number, assent/commencement dates, long title. |
| `nodes_Part.csv` | `Part` | The eleven Parts, I–XI, with the section range each covers. |
| `nodes_Section.csv` | `Section` | All 75 sections. `text` holds the section's own operative text where the section is not subdivided, or the chapeau where it is. |
| `nodes_Clause.csv` | `Clause` | Every subsection, paragraph and subparagraph carrying text, verbatim. `level` is `subsection` / `paragraph` / `subparagraph`; `parent_clause_id` gives nesting (empty when the parent is the section itself). |
| `nodes_Definition.csv` | `Definition` | The 25 defined terms in section 2, plus the term "data protection impact assessment" defined in-line at s. 31(4). |
| `nodes_Schedule.csv` | `Schedule` | First Schedule (oath of office, [Section 15.]) and Second Schedule (Consequential Amendments, [Section 75.]). |
| `nodes_Penalty.csv` | `Penalty` | Every stated offence / fine / administrative fine, with the monetary and custodial amounts split out where the Act states them. |
| `nodes_Deadline.csv` | `Deadline` | Every stated time period or threshold period (72 hours, 48 hours, 30/60/90 days, 21 days, three months, six years, etc.). |

### Relationship types
| File | Rel | Endpoints |
|---|---|---|
| `rels_has_part.csv` | `HAS_PART` | Act → Part |
| `rels_has_section.csv` | `HAS_SECTION` | Part → Section |
| `rels_has_clause.csv` | `HAS_CLAUSE` | Section → Clause, or Clause → Clause (nesting) |
| `rels_defines.csv` | `DEFINED_IN` | Definition → Section |
| `rels_has_schedule.csv` | `HAS_SCHEDULE` | Act → Schedule |
| `rels_schedule_under_section.csv` | `SCHEDULE_UNDER` | Schedule → enabling Section |
| `rels_imposes_penalty.csv` | `IMPOSES_PENALTY` | Section/Clause → Penalty |
| `rels_sets_deadline.csv` | `SETS_DEADLINE` | Section/Clause → Deadline |
| `rels_cross_references.csv` | `CROSS_REFERENCES` | Section/Clause/Definition → the Section or Schedule it cites, with the citing phrase verbatim |

Node ids: `ACT`, `PART_I`…`PART_XI`, `s<N>` for sections, `s<N>(1)(a)(i)`-style for clauses,
`def_<slug>`, `SCH_1`/`SCH_2`, `PEN_<clause>`, `DL_<clause>`.

## Row counts (excluding header)

| File | Rows |
|---|---|
| nodes_Act.csv | 1 |
| nodes_Part.csv | 11 |
| nodes_Section.csv | 75 |
| nodes_Clause.csv | 447 |
| nodes_Definition.csv | 26 |
| nodes_Schedule.csv | 2 |
| nodes_Penalty.csv | 12 |
| nodes_Deadline.csv | 12 |
| rels_has_part.csv | 11 |
| rels_has_section.csv | 75 |
| rels_has_clause.csv | 447 |
| rels_defines.csv | 26 |
| rels_has_schedule.csv | 2 |
| rels_schedule_under_section.csv | 2 |
| rels_imposes_penalty.csv | 12 |
| rels_sets_deadline.csv | 12 |
| rels_cross_references.csv | 16 |

Total distinct node ids: 586. Validation asserts unique ids per node file and that every
`source_id`/`target_id` resolves; it reports 0 errors.

## Caveats and gaps

- **Second Schedule is empty in the source.** The published PDF prints the heading
  "SECOND SCHEDULE [Section 75.] CONSEQUENTIAL AMENDMENTS" and then blank pages (pp. 34–37). The
  actual list of amended laws is not present in the source text, so `SCH_2` carries only the
  heading. No amendment content has been supplied from outside the document.
- **Section 61** is drafted with the offence and penalty split across the chapeau and the closing
  words after paragraph (d). The section-level `text` marks the omitted paragraphs as
  `[paragraphs (a) to (d)]`; the four paragraphs themselves are rows in `nodes_Clause.csv`.
- Section 45(c)(i)–(iii) are reproduced exactly as printed; the chapeau reads "processing is
  necessary—" and the subparagraphs do not repeat "for", which is how the source sets them out.
- Minor typographic artefacts in the source are preserved verbatim: "processingsensitive" in the
  arrangement of sections (the section heading itself reads "processing sensitive"), "social or
  social identity" in the definition of "identifiable natural person", "third Party" capitalised
  in section 2, "commit an offence" in s. 72(3)(b), and "subclause" used for subsection in s. 56.
- Em-dashes introducing lists in the source are rendered as a plain hyphen in the CSVs; no other
  wording has been changed.
- Sections 1, 10, 13–17, 20, 23, 36, 44, 50, 54, 59, 60, 63, 64, 66, 69 and 75 have no
  subdivisions; their full text sits on the `Section` row and they have no `Clause` children.
