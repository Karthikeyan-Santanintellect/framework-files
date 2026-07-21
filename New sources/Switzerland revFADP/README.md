# Swiss Federal Act on Data Protection (revised FADP / nFADP) — knowledge-graph CSVs

**Source document:** `KB 2/Switzerland/Switzerland Revised Federal Act on Data Protection.pdf`
(`pdftotext -layout` extract, 32 pages, SR 235.1)

**Instrument:** Federal Act on Data Protection (Data Protection Act, FADP), SR 235.1, of
25 September 2020, last amended on 7 July 2025, in force since 1 September 2023 (AS 2022 491).

## Language / translation status

**The source text is an English translation, not the authentic legal text.** The document
carries the standard Federal Chancellery notice on its first page:

> "English is not an official language of the Swiss Confederation. This translation is provided
> for information purposes only and has no legal force."

The authentic versions are the German, French and Italian originals. Note also footnote 22 to
Art. 57 para. 2, which records that the 2 July 2025 correction by the Federal Assembly Drafting
Committee "concerns the Italian text only (AS 2025 444)" — i.e. the English text carries no
corresponding change. All text in these CSVs is verbatim from the English translation supplied.

## Schema

The Act's own structure is Chapters → (in Chapters 2 and 7 only) Sections → Articles →
numbered paragraphs → lettered subdivisions → numbered sub-subdivisions. The node types use
that vocabulary directly, plus four cross-cutting node types for content the Act itself states.

| Node type | What it is |
|---|---|
| `Act` | The instrument itself: title, SR number, dates, constitutional basis, translation notice |
| `Chapter` | The 10 Chapters |
| `Section` | The 8 Sections (Ch. 2 §§1–3, Ch. 7 §§1–5); other Chapters have no Sections |
| `Article` | The 77 Articles, incl. inserted Arts. 44a, 47a, 72a |
| `Paragraph` | Every numbered paragraph (incl. `3bis`, `5bis`); unnumbered single-paragraph Articles are stored with an empty `paragraph_number` and id suffix `_p0` |
| `Letter` | Every lettered subdivision (a., b., c. …), the obligation-carrying clause level |
| `Number` | Every numbered sub-subdivision under a letter (1., 2., 3. …) |
| `Definition` | The 11 defined terms in Art. 5 let. a–k, each with its verbatim definition |
| `Penalty` | The criminal sanctions in Chapter 8, with maximum amount, liable person and whether prosecution is on complaint |
| `Deadline` | Every period, time limit or numeric threshold the Act states (30 days, two months, five years, 250 employees, ten years, …) with its verbatim source sentence |
| `Annex` | Annexes 1 and 2 (both largely refer out to AS 2022 491) |
| `ExternalInstrument` | Other enactments the Act cites (APA, FoIA, Civil Code, ACLA, Archiving Act, …) with SR numbers taken from the footnotes |

| Relationship | Meaning |
|---|---|
| `HAS_CHAPTER` | Act → Chapter |
| `HAS_SECTION` | Chapter → Section |
| `HAS_ARTICLE` | Section → Article, or Chapter → Article where the Chapter has no Sections |
| `HAS_PARAGRAPH` / `HAS_LETTER` / `HAS_NUMBER` | Clause containment |
| `DEFINES` | Art. 5 → Definition |
| `IMPOSES_PENALTY` | Paragraph → Penalty |
| `SETS_DEADLINE` | Clause → Deadline |
| `HAS_ANNEX` | Act → Annex |
| `REFERENCES` | Clause → Article of this Act that the clause text cites |
| `REFERS_TO_INSTRUMENT` | Clause/Annex → ExternalInstrument cited in the text |

Why this shape: the FADP is a statute whose obligations sit at letter level (e.g. Art. 12 para. 2
let. g, Art. 16 para. 2 let. d), and several of the most queried features — the data-subject
rights (Arts. 25–29), the cross-border disclosure regime (Arts. 16–18), the FDPIC's investigatory
and administrative powers (Arts. 49–53) and the criminal provisions (Arts. 60–66) — are only
usable in a graph if broken down to that depth. Definitions, penalties and deadlines are promoted
to their own node types because they are the cross-cutting facts most often queried independently
of where they sit in the document tree.

## Files and row counts

### Nodes
| File | Rows |
|---|---|
| `nodes_Act.csv` | 1 |
| `nodes_Chapter.csv` | 10 |
| `nodes_Section.csv` | 8 |
| `nodes_Article.csv` | 77 |
| `nodes_Paragraph.csv` | 209 |
| `nodes_Letter.csv` | 192 |
| `nodes_Number.csv` | 29 |
| `nodes_Definition.csv` | 11 |
| `nodes_Penalty.csv` | 7 |
| `nodes_Deadline.csv` | 13 |
| `nodes_Annex.csv` | 2 |
| `nodes_ExternalInstrument.csv` | 13 |

### Relationships
| File | Rows |
|---|---|
| `rels_HAS_CHAPTER.csv` | 10 |
| `rels_HAS_SECTION.csv` | 8 |
| `rels_HAS_ARTICLE.csv` | 77 |
| `rels_HAS_PARAGRAPH.csv` | 209 |
| `rels_HAS_LETTER.csv` | 192 |
| `rels_HAS_NUMBER.csv` | 29 |
| `rels_DEFINES.csv` | 11 |
| `rels_IMPOSES_PENALTY.csv` | 7 |
| `rels_SETS_DEADLINE.csv` | 13 |
| `rels_HAS_ANNEX.csv` | 2 |
| `rels_REFERENCES.csv` | 117 |
| `rels_REFERS_TO_INSTRUMENT.csv` | 19 |

Totals: 572 nodes, 694 relationships.

## Caveats and gaps

- **Translation, not authentic text** — see above. Terminology differences from the German/French
  originals (e.g. "sensitive personal data" for *besonders schützenswerte Personendaten*) are
  inherent to the source.
- **Annexes are stubs in the source.** Annex 1 part II ("The following enactments are amended as
  follows: …") and the whole of Annex 2 are not reproduced in the PDF; both footnotes say the
  content "may be consulted under AS 2022 491". The two Annex nodes record exactly that, and no
  amendment detail has been invented.
- **Footnotes** (SR references, amendment histories such as "Inserted by No I of the FA of 17 June
  2022 … AS 2023 231") were not made into nodes. The SR numbers they carry are used as the
  `sr_number` attribute of `ExternalInstrument` nodes; footnote markers were stripped from clause
  text so the prose reads cleanly (e.g. "the Host State Act of 22 June 2007" rather than
  "…20073").
- **Unnumbered Articles.** Articles 1, 5, 18, 33, 40, 42, 44a, 45, 46, 47a, 48, 56, 61, 63, 66,
  67, 68, 69, 70, 71, 72a and 73 consist of a single unnumbered paragraph. These are stored as a
  Paragraph with an empty `paragraph_number` (id suffix `_p0`) so the containment chain is uniform.
- **Articles without headings.** Art. 59 (Fees) and Art. 67 (Conclusion of International Treaties)
  carry no Article heading in the source; their `heading` cells are empty, as the source has none.
- **Typographic artefacts preserved.** The source contains "He or she is is not subject…"
  (Art. 43 para. 6), "if any one one of the following requirements" (Art. 34 para. 4) and "in
  particular if does not serve" (Art. 26 para. 1 let. c). These are reproduced verbatim.
- **Dashes.** En-dashes in ranges within clause text (e.g. "paragraphs 2–4", "Articles 25–27",
  "28g–28l") were normalised to hyphens for CSV safety; no words were changed.
- **`REFERENCES` is derived, not stated.** The edges are produced by matching "Article(s) N"
  patterns in verbatim clause text against Article ids; self-references are dropped. The clause
  text itself remains the authority. References to Articles of *other* enactments that share a
  number with an FADP Article (e.g. "Article 30 paragraph 2 APA", "Articles 16 and 17 of the APA")
  can produce a spurious internal edge; the accompanying `REFERS_TO_INSTRUMENT` edge on the same
  clause identifies these cases.

## Validation

`check_chfadp.py` (run at build time) parses every CSV, asserts each node file's first column is
`<type>_id`, asserts ids are unique within and across node files, asserts every relationship
endpoint resolves to a node id, and prints per-file row counts. Result: **0 errors**.
