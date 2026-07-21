# EU Artificial Intelligence Act — knowledge-graph CSVs

**Instrument:** Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024
laying down harmonised rules on artificial intelligence (Artificial Intelligence Act).

**Source document:** `KB 2/Europe/EU Artificial Intelligence Act.pdf`
(Official Journal L series, 12.7.2024, 144 pages; ELI `http://data.europa.eu/eli/reg/2024/1689/oj`).
All text was taken from a `pdftotext -layout` extract of that PDF; layout artefacts (page headers,
page footers, running ELI lines, footnote blocks, column wrapping) were removed and wrapped lines
re-joined so that every stored value is the source wording, unmodified.

Every node row carries `source_document`, and every provision-bearing row carries `source_line`,
the line number in the layout extract where the provision begins — so any cell can be traced back
to the PDF text.

## Schema and why

The Regulation is a classic EU legislative act, so the schema mirrors the document's own
divisions and uses its own vocabulary: **Recitals** ("Whereas" numbered (1)–(180)) →
**Chapters** → **Sections** → **Articles** → numbered **Paragraphs** (and their unnumbered
subparagraphs) → lettered / roman / numbered **Points**, plus the **Annexes** with their
**Annex Sections** and annex points.

Four further node types are lifted out because the Regulation itself treats them as distinct
regulatory objects and they are the things a compliance graph is normally queried on:

| Node type | Why it exists |
|---|---|
| `Definition` | Article 3 contains 68 numbered defined terms, each with its own verbatim definition. |
| `ProhibitedPractice` | Article 5(1) points (a)–(h) are the exhaustive list of prohibited AI practices. |
| `HighRiskArea` | Annex III points 1–8 are the eight areas whose systems are high-risk under Article 6(2). |
| `Penalty` | The administrative-fine tiers stated in Articles 99, 100 and 101, with the euro ceiling and turnover percentage each provision states. |
| `Deadline` | Every calendar date stated in the enacting terms (application dates, reporting dates, compliance dates), linked to the provisions that state it. |

These are *projections* of provisions that also remain in `nodes_Point.csv` /
`nodes_Paragraph.csv`; each carries a `point_id` / `provision_id` back-pointer, so nothing is
orphaned or restated in different words.

### Node files

| File | Rows | First column | Notes |
|---|---:|---|---|
| `nodes_Regulation.csv` | 1 | `regulation_id` | The instrument: full title, adoption/publication dates, ELI, legal basis. |
| `nodes_Recital.csv` | 180 | `recital_id` | Recitals (1)–(180), full verbatim text. |
| `nodes_Chapter.csv` | 13 | `chapter_id` | Chapters I–XIII with headings. |
| `nodes_Section.csv` | 16 | `section_id` | Sections within Chapters III, V, VII and IX. |
| `nodes_Article.csv` | 113 | `article_id` | Articles 1–113 with titles and their chapter/section. |
| `nodes_Paragraph.csv` | 605 | `paragraph_id` | Numbered paragraphs plus unnumbered subparagraphs (`subparagraph` column). |
| `nodes_Point.csv` | 698 | `point_id` | Lettered `(a)`, roman `(i)`, numbered `(1)` points and all annex points, with `parent_id` and `level`. |
| `nodes_Definition.csv` | 68 | `definition_id` | Article 3 terms: `term`, full verbatim `definition`, and `definition_body` (the text after "means"). |
| `nodes_ProhibitedPractice.csv` | 8 | `prohibited_practice_id` | Article 5(1)(a)–(h). |
| `nodes_Annex.csv` | 13 | `annex_id` | Annexes I–XIII with titles. |
| `nodes_AnnexSection.csv` | 6 | `annex_section_id` | Annex I Sections A/B, Annex VIII Sections A/B/C, Annex XI Section 2. |
| `nodes_HighRiskArea.csv` | 8 | `area_id` | Annex III areas 1–8. |
| `nodes_Penalty.csv` | 6 | `penalty_id` | Fine tiers: `max_fine_eur`, `max_turnover_percent`, verbatim provision text. |
| `nodes_Deadline.csv` | 39 | `deadline_id` | Distinct calendar dates stated in the enacting terms. |

### Relationship files

| File | Rows | Meaning |
|---|---:|---|
| `rels_CONTAINS.csv` | 1644 | Structural containment: Regulation→Chapter/Annex/Recital, Chapter→Section→Article, Article→Paragraph→subparagraph, Paragraph→Point→sub-Point, Annex→AnnexSection→point. |
| `rels_DEFINES.csv` | 68 | Article 3 → Definition. |
| `rels_PROHIBITS.csv` | 8 | Article 5 → ProhibitedPractice. |
| `rels_IMPOSES_PENALTY.csv` | 6 | Article 99/100/101 → Penalty. |
| `rels_SANCTIONS.csv` | 3 | Penalty → the Article whose infringement it sanctions (only where the penalty provision names an Article). |
| `rels_HAS_DEADLINE.csv` | 69 | Provision → Deadline, for every provision stating a calendar date. |
| `rels_REFERENCES.csv` | 466 | Provision → Article / Annex it cites by name ("Article 43", "Annex III"). |

## Caveats and gaps

- **Verbatim only.** No text was paraphrased, summarised or supplied from outside the PDF.
  `max_fine_eur` / `max_turnover_percent` and `Deadline.date` are literal strings lifted out of the
  provision text that is stored alongside them in full.
- The Regulation numbers footnotes 1–58; these bibliographic footnotes were dropped as page
  furniture and are not modelled. Footnote reference markers therefore do not appear in the text.
- **Article 113** (entry into force) is typeset without paragraph numbers; its opening sentences
  ("…shall enter into force…", "It shall apply from 2 August 2026.", "However:") are stored as one
  unnumbered paragraph, with points (a)–(c) beneath it. Annex VII points 4.3–4.7 and 5.1–5.3 are
  typeset as running prose in the source and are likewise stored inside their parent point rather
  than as separate rows. **Annex XI Section 1** is captured in the Annex XI title line rather than
  as its own `AnnexSection` row (its points are attached to the annex).
- Articles 102–110 are amending provisions; the quoted text they insert into other instruments is
  stored verbatim as their paragraph text.
- The signature block ("Done at Brussels…", the Presidents' names) is not modelled.
- `rels_REFERENCES.csv` is built from explicit "Article N" / "Annex N" citations in provision text;
  references expressed only as "that Regulation", "this Section" etc. are not resolved.
- The source text is the English-language Official Journal version.

## Validation

`aiact_check.py` (run at build time) parses every CSV, asserts each node id is unique within its
file, asserts every `source_id`/`target_id` in every relationship file resolves to a node id, and
prints per-file row counts. Result: **all ids unique, all 2264 relationship endpoints resolve, no
errors.**
