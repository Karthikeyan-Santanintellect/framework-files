# DIFC Data Protection Law — knowledge-graph CSVs

## Source document

- **Instrument:** Data Protection Law, **DIFC Law No. 5 of 2020** (Dubai International Financial Centre).
- **Version extracted:** Consolidated Version (July 2025), as amended by DIFC Laws Amendment Law No. 1 of 2025 and DIFC Laws Amendment Law, DIFC Law No. 2 of 2022.
- **Enacted / in force:** made by the Ruler; comes into force on 1 July 2020 (Article 4). Repeals and replaces the Data Protection Law, Law No. 1 of 2007 (Article 1(2)).
- **Source PDF (citation only):** `KB 2/UAE/DIFC Data Protection Law.pdf`
- Every node file carries a `source_document` column recording this PDF path.

## Schema

The schema mirrors the law's own structure and vocabulary: **Parts → (lettered sub-)Parts → numbered Articles → paragraphs and sub-paragraphs**, plus the two **Schedules** (interpretation and defined terms; administrative fines).

### Node types

| File | Node type | What it is |
|---|---|---|
| `nodes_Part.csv` | Part | The ten numbered Parts (`PART 1: INTRODUCTION AND SCOPE` … `PART 10: GENERAL EXEMPTIONS`). |
| `nodes_Subpart.csv` | Subpart | The lettered sub-divisions the law uses inside Parts 2 and 3 (`Part 2A` … `Part 3B`). |
| `nodes_Article.csv` | Article | Each numbered Article 1–65 plus Article 64A. `chapeau` holds any un-numbered opening/whole-Article text (e.g. Articles 2, 4, 5, 10, 11, 25, 36, 40, 54). |
| `nodes_Clause.csv` | Clause | Every numbered/lettered subdivision that carries text: `(1)`, `(a)`, `(i)`, `(A)`, and the deepest `(1)`/`(2)` level used in Article 29(1)(h)(ix). `clause_ref` is the citation form (e.g. `24(5)(b)(ii)(A)`); `level`, `marker`, `kind` (numeric / alpha / roman / upper-alpha) and `parent_clause_id` record the hierarchy. |
| `nodes_Definition.csv` | Definition | Every defined term in Schedule 1, paragraph 3, with its verbatim definition. |
| `nodes_InterpretationRule.csv` | InterpretationRule | Schedule 1 paragraph 1 ("Rules of interpretation") and paragraph 2 ("Legislation in the DIFC"), at sub-item level. |
| `nodes_Schedule.csv` | Schedule | Schedule 1 and Schedule 2 (description text taken verbatim from Article 7). |
| `nodes_Fine.csv` | Fine | Each row of the Schedule 2 administrative-fine table: the Article contravened, the verbatim contravention description, and the maximum fine in USD ($25,000–$100,000). |

### Relationship types

| File | Pattern |
|---|---|
| `rels_HAS_SUBPART.csv` | Part → Subpart |
| `rels_CONTAINS_ARTICLE.csv` | Part or Subpart → Article |
| `rels_HAS_CLAUSE.csv` | Article → top-level Clause |
| `rels_HAS_SUBCLAUSE.csv` | Clause → nested Clause |
| `rels_CROSS_REFERENCES.csv` | Article/Clause → Article cited in its text ("Article 33", "Articles 29 and 30", …) |
| `rels_CONTAINS_RULE.csv` | Schedule 1 → top-level InterpretationRule |
| `rels_HAS_SUBRULE.csv` | InterpretationRule → nested InterpretationRule |
| `rels_DEFINES_TERM.csv` | Schedule 1 → Definition |
| `rels_DEFINED_IN.csv` | Definition → Article whose text supplies the meaning (e.g. *Requesting Authority* → Article 28, *Single Discrete Incident* → Article 12) |
| `rels_SPECIFIES_FINE.csv` | Schedule 2 → Fine |
| `rels_PENALISES.csv` | Fine → Article it penalises (carries `maximum_fine_usd`) |

## Row counts

| File | Rows |
|---|---|
| nodes_Part.csv | 10 |
| nodes_Subpart.csv | 6 |
| nodes_Article.csv | 66 |
| nodes_Clause.csv | 662 |
| nodes_Definition.csv | 37 |
| nodes_InterpretationRule.csv | 27 |
| nodes_Schedule.csv | 2 |
| nodes_Fine.csv | 37 |
| **nodes total** | **847** |
| rels_HAS_SUBPART.csv | 6 |
| rels_CONTAINS_ARTICLE.csv | 66 |
| rels_HAS_CLAUSE.csv | 288 |
| rels_HAS_SUBCLAUSE.csv | 374 |
| rels_CROSS_REFERENCES.csv | 214 |
| rels_CONTAINS_RULE.csv | 8 |
| rels_HAS_SUBRULE.csv | 19 |
| rels_DEFINES_TERM.csv | 37 |
| rels_DEFINED_IN.csv | 6 |
| rels_SPECIFIES_FINE.csv | 37 |
| rels_PENALISES.csv | 37 |
| **rels total** | **1,092** |

## Coverage notes

- Data subject rights (Part 6, Articles 32–40), controller/processor obligations (Parts 2 and 3), transfer rules (Part 4, Articles 26–28), the Commissioner (Part 8, Articles 43–58), remedies/liability/fines (Part 9, Articles 59–64A) and general exemptions (Part 10, Article 65) are all extracted at clause level.
- Deadlines and thresholds stated in the law are preserved verbatim inside clause text — e.g. one (1) month for access requests extendable by two (2) months (Article 33(1), 33(7)), four (4) weeks for prior consultation (Article 21(7)), thirty (30) days to appeal to the Court (Article 63(1)–(2)), a five (5) year Commissioner term (Article 43(3)), three (3) year certification validity (Article 50(4)), fourteen (14) days to seek review of a direction (Article 59(7)).

## Caveats

- **Verbatim only.** All text is taken from the `pdftotext -layout` extract; layout line-wrapping was rejoined into single-line prose without altering wording. Typographic quotes and the source's own spellings/typos (e.g. "pseudonynmised" in Article 22(2), "publically" in Article 19(3)) are preserved as printed.
- **Article 22(1) has no sub-paragraph (e)** in the source: item `(d)` reads "securely encrypted; or" and the list ends there. This is a drafting gap in the published consolidated text, not an extraction loss.
- The table of contents (pages i–ii), page headers/footers and page numbers were discarded as layout artifacts.
- `rels_CROSS_REFERENCES.csv` is derived by matching "Article(s) N" citations in clause text and resolves to Article granularity only (a reference to "Article 20(6)(e)" links to Article 20). References to Schedules, Parts and external instruments are left in the clause text but are not turned into relationships.
- Schedule 2 is, in the law's own words, not exhaustive: "This list is not exhaustive and may be updated from time to time." Article 62(3) additionally allows a general fine not limited to the Schedule 2 amounts.
- Amendment history (which provisions came from the 2022 or 2025 amendment laws) is not marked in the consolidated text and therefore is not modelled.

## Validation

A self-check script parsed every CSV, asserted that each node file's first column is `<type>_id` with unique values and a `source_document` column, and that every `source_id`/`target_id` in every relationship file resolves to an existing node id. Result: **0 errors**.
