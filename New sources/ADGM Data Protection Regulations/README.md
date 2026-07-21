# ADGM Data Protection Regulations — knowledge-graph CSVs

## Source

- **Instrument:** Data Protection Regulations 2021, Abu Dhabi Global Market (ADGM)
- **Version / year:** **Data Protection Regulations 2021 — Consolidated version February 2024**
  (title page: "DATA PROTECTION REGULATIONS 2021 (CONSOLIDATED VERSION FEBRUARY 2024)")
- **Date of enactment:** 11 February 2021
- **Consolidation amendments recorded in the source footnotes:** amendments of 26 July 2022
  (sections 15, 24, 35, 49, 51, 52, 53, 62) and 28 February 2024 (section 55)
- **Source document (citation only):** `KB 2/UAE/ADGM Data Protection Regulations.pdf`
- **Extracted from:** `pdftotext -layout` text of that PDF

## Schema

The schema mirrors the document's own vocabulary and subdivision scheme. The Regulations are
organised as **Parts I–VIII → numbered Sections 1–64 → subsections `(1)` → paragraphs `(a)` →
subparagraphs `(i)`**, with all defined terms collected in section 62.

### Node types

| File | Node type | Meaning |
|---|---|---|
| `nodes_Instrument.csv` | Instrument | The Regulations themselves: short title, long title, enacting formula, version, enactment date |
| `nodes_Part.csv` | Part | Parts I–VIII with their headings |
| `nodes_Section.csv` | Section | Numbered sections 1–64 with heading; `text` holds body text for sections whose obligation is unnumbered prose (sections 27, 29, 61) |
| `nodes_Subsection.csv` | Subsection | Numbered subsections, e.g. `12(2)` — verbatim text |
| `nodes_Paragraph.csv` | Paragraph | Lettered paragraphs, e.g. `12(2)(a)` — verbatim text |
| `nodes_Subparagraph.csv` | Subparagraph | Roman-numeral subparagraphs, e.g. `7(2)(k)(vi)` — verbatim text |
| `nodes_Definition.csv` | Definition | Every capitalised term defined in section 62(1), verbatim |

Every node file carries a `source_document` column.

### Relationship types

| File | Relationships |
|---|---|
| `rels_structure.csv` | `HAS_PART`, `HAS_SECTION`, `HAS_SUBSECTION`, `HAS_PARAGRAPH`, `HAS_SUBPARAGRAPH` — the containment tree |
| `rels_defines.csv` | `DEFINES` — section 62 → each Definition (extra column: `term`) |
| `rels_cross_references.csv` | `CROSS_REFERENCES` — clause → the most specific clause it cites (extra column: `reference`, the literal citation token such as `50(5)(a)`); explicit `sections A to B` ranges are expanded |
| `rels_uses_term.csv` | `USES_TERM` — clause → Definition whose defined term appears verbatim in that clause |

### Id conventions

`part_I`, `sec_12`, `sub_12-2`, `para_12-2-a`, `subp_7-2-k-vi`, `def_personal_data`,
`instr_adgm_dpr_2021`. Ids are unique within each file and every relationship endpoint resolves.

## Row counts

| File | Rows |
|---|---|
| `nodes_Instrument.csv` | 1 |
| `nodes_Part.csv` | 8 |
| `nodes_Section.csv` | 64 |
| `nodes_Subsection.csv` | 242 |
| `nodes_Paragraph.csv` | 355 |
| `nodes_Subparagraph.csv` | 39 |
| `nodes_Definition.csv` | 39 |
| `rels_structure.csv` | 708 |
| `rels_defines.csv` | 39 |
| `rels_cross_references.csv` | 351 |
| `rels_uses_term.csv` | 1086 |

Total node ids: 748.

## Coverage notes

- All 8 Parts and all 64 sections of the consolidated text are present, including the key
  obligations requested: definitions (s.62), data subject rights (Part III, ss.10–21),
  controller/processor obligations (Part IV, ss.22–39), international transfers (Part V,
  ss.40–46), the Commissioner of Data Protection (Part VI, ss.47–53) and fines and remedies
  (Part VII, ss.54–59).
- Stated monetary thresholds are preserved verbatim in the clause text, e.g. the administrative
  fine cap of USD 28 million (s.55(1) and s.55(6)) and the fixed penalty of up to 150 per cent of
  the Data Protection Fee or Renewal Fee (s.56(1)). Deadlines such as the 72-hour breach
  notification (s.32(1)), the two-month response period (s.10(3)) and the 21-day and three-month
  review periods (ss.54(4), 58(1)) sit inside their clause text.

## Caveats and gaps

- **No Schedules.** The consolidated text contains no Schedules or Annexes — the document ends at
  section 64. No Schedule nodes are therefore present.
- **Section 62 (Definitions)** is modelled as `Definition` nodes rather than as
  subsection/paragraph clauses. Lists that appear *inside* individual definitions (the (a)–(e)
  list in "High Risk Processing Activities" and the (a)–(b) list in "Supervisory Authority") are
  kept inline in the `definition` field rather than split into paragraph rows, so that definition
  text stays whole. Subsection `62(1)` retains only its introductory sentence.
- **Sections 27, 29 and 61** consist of a single unnumbered paragraph; their text is stored on the
  `Section` node's `text` column, with no subsection row.
- Where a subsection's closing words follow its final lettered paragraph on the page (e.g. the
  closing words of s.7(1), s.10(6) and s.35(2)), those closing words are appended to the last
  paragraph's text, since the layout extract does not separate them.
- Footnote reference digits attached to headings (marking the 2022/2024 amendments) were removed
  from headings; one inline footnote marker remains inside s.15(3)(a) ("ADGM's Board1") exactly as
  it appears in the extract.
- `USES_TERM` edges are derived by literal string matching of defined terms in clause text; they
  are a navigational aid, not a statement made by the instrument.
- `CROSS_REFERENCES` covers explicit "section"/"sections" citations only. References written as
  bare cross-Part prose (e.g. "this Part", "Part III") are not edges.
