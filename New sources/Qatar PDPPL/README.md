# Qatar Personal Data Privacy Protection Law (Law No. 13 of 2016) — knowledge-graph CSVs

## Source document

- **Instrument:** Law No. (13) of 2016 on Protecting Personal Data Privacy, State of Qatar
- **Source PDF:** `KB 2/Qatar/Qatar Personal Data Privacy Protection Law.pdf`
- **Publisher of this copy:** Compliance and Data Protection (CDP) Department, compliance.qcert.org
- **Issued:** 03/02/1438 (AH), corresponding to 03/11/2016 (AD), at the Emiri Diwan, by Tamim Bin Hamad Al-Thani, Emir of the State of Qatar.

### Is the text an English translation?

**Yes.** The source is an English-language rendering of an Arabic statute. The PDF carries the
publisher's own disclaimer on every page, reproduced verbatim in `nodes_Law.csv`
(`official_status_note`):

> "This document is not official and the official version of the law is the one published in the
> Official Gazette number 15 of year 2016 that is available on almeezan.qa"

All clause text in these CSVs is verbatim from that English translation. Translation artefacts are
preserved rather than corrected — e.g. Article (19) reads "Articles (4), (5\ Items 1, 2, and 3)"
and Article (24) reads "(16\ paragraph 3)", where the backslash appears to stand for a slash or
comma in the original; Article (16) paragraph 4 reads "imposing" where "impose" is grammatically
expected; Article (21) reads "the preceding two Article". These are left exactly as printed.

### Are implementing regulations included?

**No.** The PDF contains only the statute itself (Articles 1–32, Chapters One–Eight, preamble and
signature block). The Law repeatedly delegates detail to future ministerial decisions — Articles
(7), (8)(4), (16) paragraphs 3 and 4, (18) final paragraph and (31) all require a "decision of the
Minister" — but none of those decisions, and no executive/implementing regulations, are present in
the source. Nothing about their content has been supplied from outside the document.

## Schema

The schema mirrors the statute's own vocabulary: the Law divides itself into **Chapters**, each
Chapter into numbered **Articles**, and many Articles into numbered **items** or unnumbered
**paragraphs** (both modelled as `Clause`). Four cross-cutting node types capture things the Law
itself enumerates and that a compliance graph needs to query directly: the Article (1)
**Definitions**, the individual **Rights** of Chapter Two, the **SpecialNatureDataCategory** list in
Article (16), and the **Penalty** ceilings of Chapter Seven. `Deadline` and `ExternalInstrument`
capture the stated time limits and the instruments cited in the preamble and Article (2).

### Node types

| File | Node type | Rows | Contents |
|---|---|---|---|
| `nodes_Law.csv` | Law | 1 | The statute, its promulgation details and the unofficial-copy disclaimer |
| `nodes_Preamble.csv` | Preamble | 1 | The "After having perused…" recital block, verbatim |
| `nodes_Chapter.csv` | Chapter | 8 | Chapters One–Eight with their titles and article ranges |
| `nodes_Article.csv` | Article | 32 | Articles (1)–(32), full verbatim text, parent chapter, subject actor |
| `nodes_Clause.csv` | Clause | 61 | Every numbered item and every distinct unnumbered paragraph that carries obligation text |
| `nodes_Definition.csv` | Definition | 17 | Every term defined in Article (1), verbatim |
| `nodes_Right.csv` | Right | 10 | Individual rights in Articles (3), (5), (6) and (26) |
| `nodes_SpecialNatureDataCategory.csv` | SpecialNatureDataCategory | 7 | The seven categories listed in Article (16) paragraph 1 |
| `nodes_Penalty.csv` | Penalty | 3 | Fine ceilings in Articles (23), (24), (25) with amounts and addressees |
| `nodes_Deadline.csv` | Deadline | 3 | The sixty-day grievance periods (Article 26) and the six-month adjustment period (Article 30) |
| `nodes_ExternalInstrument.csv` | ExternalInstrument | 7 | Laws and resolutions cited in the preamble and Article (2) |

**Total: 150 nodes.**

### Relationship types

| File | Rel type | Rows | Meaning |
|---|---|---|---|
| `rels_HAS_PREAMBLE.csv` | HAS_PREAMBLE | 1 | Law → Preamble |
| `rels_HAS_CHAPTER.csv` | HAS_CHAPTER | 8 | Law → Chapter |
| `rels_HAS_ARTICLE.csv` | HAS_ARTICLE | 32 | Chapter → Article |
| `rels_HAS_CLAUSE.csv` | HAS_CLAUSE | 61 | Article → Clause |
| `rels_DEFINES.csv` | DEFINES | 17 | Article (1) → Definition |
| `rels_GRANTS_RIGHT.csv` | GRANTS_RIGHT | 10 | Article/Clause → Right |
| `rels_CLASSIFIES_AS_SPECIAL_NATURE.csv` | CLASSIFIES_AS_SPECIAL_NATURE | 7 | Article (16) → data category |
| `rels_IMPOSED_BY.csv` | IMPOSED_BY | 3 | Penalty → the Article that imposes it |
| `rels_PENALISES.csv` | PENALISES | 13 | Penalty → each provision whose breach it sanctions |
| `rels_EXEMPTS_FROM.csv` | EXEMPTS_FROM | 11 | Exemption Article → the provision disapplied |
| `rels_CROSS_REFERENCES.csv` | CROSS_REFERENCES | 9 | Internal references ("the preceding Article", etc.) |
| `rels_SETS_DEADLINE.csv` | SETS_DEADLINE | 3 | Clause → Deadline |
| `rels_REFERENCES_INSTRUMENT.csv` | REFERENCES_INSTRUMENT | 8 | Law/Article → external instrument |

**Total: 183 relationships.**

## Modelling notes and caveats

- **Clause granularity.** Articles that are a single block of prose with no subdivisions (e.g. 3, 4,
  7, 10, 12, 14, 15, 20, 23, 24, 25, 28, 29, 31, 32) have no `Clause` rows; their full text lives on
  the `Article` node. Articles whose text splits into distinct normative paragraphs (2, 13, 16, 22,
  26, 30) or numbered items (5, 6, 8, 9, 11, 17, 18, 19, 21, 27) are decomposed. Article (18) has
  four numbered purposes plus a closing paragraph on the special record, captured as
  `ART-18-P-FINAL`.
- **Paragraph numbering.** The statute does not itself number the unnumbered paragraphs, except in
  Article (24) which cites "(16\ paragraph 3)". Paragraph ids (`-P1`, `-P2`, …) are positional
  identifiers assigned for graph addressing; the `clause_number` column records them as
  "paragraph N". The Article (24) citation resolves correctly onto `ART-16-P3` under this numbering.
- **Penalty scope.** Article (23) and (24) enumerate the articles they sanction, so `PENALISES`
  edges are literal. Article (25) sanctions "any of those crimes stipulated herein" without listing
  articles, so it is linked to the Law node rather than to individual provisions.
- **`subject_actor` on Article rows** is taken from the actor named in the article's own opening
  words; it is empty where the article names no single actor.
- **`modal` on Clause rows** is derived mechanically from the presence of "shall not" / "shall" /
  "may" in the clause's own text; it is empty where none appears.
- **No enforcement body node.** The Law assigns supervision to the "Competent Department" and
  "Competent Authority", which are captured as Article (1) definitions rather than as separate
  organisation nodes, since the statute defines them only by definition text.
- **Nothing inferred.** No article numbers, amounts, dates or obligations have been supplied from
  outside the source text. Where the source is garbled (the backslash citations), the garbled form
  is preserved.

## Validation

A validation script parsed every CSV, asserted node-id uniqueness within and across files, and
checked that every relationship `source_id` and `target_id` resolves to a node id. Result: **OK** —
150 unique node ids, 183 relationships, zero duplicates, zero unresolved endpoints.
