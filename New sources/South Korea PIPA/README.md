# Personal Information Protection Act (PIPA), Republic of Korea — knowledge-graph CSVs

## Source

- **Source document:** `KB 2/South Korea/Personal Information Protection Act (PIPA).pdf`
- **Text used for extraction:** `pdftotext -layout` extract of that PDF (2,317 lines).
- **Language:** The source is an **English translation** of the Korean statute (the PDF contains no
  Korean text and carries no statement of official status; treat it as an unofficial/translated
  version). Terminology is the translation's own (e.g. "visual data processing devices" for CCTV,
  "administrative surcharge"/"penalty surcharge", "resident registration number").
- **Enactment / amendment status:** Enacted as **Act No. 10465, Mar. 29, 2011**. The masthead lists
  nine amending acts; the **latest amendment reflected in this text is Act No. 16930, Feb. 4, 2020**
  (the "Data 3 Act" amendment that created the independent Protection Commission, Chapter III
  Section 3 on pseudonymous data, and Chapter VI on information and communications service
  providers). The document footer states **"Last updated : 2021-03-31"**.
  Note that this therefore **predates the Mar. 14, 2023 amendment (Act No. 19234)**, so Chapter VI
  (Articles 39-3 to 39-15) and Articles 17(3)/39-12 are still the pre-2023 cross-border and
  online-service special-case regime.

## Schema and why

The Act's own vocabulary is *Chapter → (Section) → Article → paragraph (1) → subparagraph 1. →
item (a)*, followed by ADDENDA. The schema mirrors that literally rather than using a generic
template, and adds four analytic node types that the Act itself materialises (definitions in
Article 2 and in-line "hereinafter referred to as" definitions, the Article 4 rights catalogue,
the sanction provisions, and the amending acts named in the masthead).

### Node types

| File | Type | What it is |
|---|---|---|
| `nodes_Act.csv` | Act | The instrument itself (title, act numbers, dates, translation note) |
| `nodes_Chapter.csv` | Chapter | CHAPTER I–X |
| `nodes_Section.csv` | Section | The three SECTIONs inside Chapter III |
| `nodes_Article.csv` | Article | Articles 1–76 including hyphenated insertions (7-2…7-14, 8-2, 24-2, 28-2…28-7, 32-2, 34-2, 39-2…39-15, 58-2, 74-2); `is_deleted` flags Article 8 |
| `nodes_Paragraph.csv` | Paragraph | Numbered paragraphs `(1)`, `(2)`… — verbatim |
| `nodes_Subparagraph.csv` | Subparagraph | Numbered subparagraphs `1.`, `1-2.`… — verbatim |
| `nodes_Item.csv` | Item | Lettered items `(a)`, `(b)`… — verbatim |
| `nodes_Definition.csv` | Definition | Article 2 statutory definitions plus every in-line "hereinafter referred to as ..." term |
| `nodes_DataSubjectRight.csv` | DataSubjectRight | The five rights enumerated in Article 4 |
| `nodes_Penalty.csv` | Penalty | Sanction provisions (Arts. 28-6, 34-2, 39-15, 70–75) with the verbatim imprisonment / monetary ceiling as stated |
| `nodes_Amendment.csv` | Amendment | The ten acts listed on the masthead (enacting act + nine amendments) |
| `nodes_Addendum.csv` | Addendum | The ten ADDENDA / ADDENDUM blocks at the end of the Act |
| `nodes_AddendumArticle.csv` | AddendumArticle | Articles inside those addenda (enforcement dates, transitional measures) |

### Relationship types

`HAS_CHAPTER`, `HAS_SECTION`, `HAS_ARTICLE`, `HAS_PARAGRAPH`, `HAS_SUBPARAGRAPH`, `HAS_ITEM`
(structural containment); `DEFINES` (clause → Definition); `GRANTS_RIGHT` (Article 4 subparagraph →
DataSubjectRight); `IMPOSES_PENALTY` (clause → Penalty); `AMENDED_BY` (clause → Amendment, derived
from the `<Amended by Act No. …>` / `<Newly Inserted by …>` annotations carried in the clause text);
`CROSS_REFERENCES` (clause → Article, from in-text "Article N" citations);
`HAS_ADDENDUM`, `HAS_ADDENDUM_ARTICLE`.

## Files and row counts

| File | Rows |
|---|---|
| nodes_Act.csv | 1 |
| nodes_Chapter.csv | 10 |
| nodes_Section.csv | 3 |
| nodes_Article.csv | 115 |
| nodes_Paragraph.csv | 336 |
| nodes_Subparagraph.csv | 332 |
| nodes_Item.csv | 17 |
| nodes_Definition.csv | 33 |
| nodes_DataSubjectRight.csv | 5 |
| nodes_Penalty.csv | 12 |
| nodes_Amendment.csv | 10 |
| nodes_Addendum.csv | 10 |
| nodes_AddendumArticle.csv | 31 |
| **Total nodes** | **915** |
| rels_HAS_CHAPTER.csv | 10 |
| rels_HAS_SECTION.csv | 3 |
| rels_HAS_ARTICLE.csv | 115 |
| rels_HAS_PARAGRAPH.csv | 336 |
| rels_HAS_SUBPARAGRAPH.csv | 332 |
| rels_HAS_ITEM.csv | 17 |
| rels_DEFINES.csv | 33 |
| rels_GRANTS_RIGHT.csv | 5 |
| rels_IMPOSES_PENALTY.csv | 12 |
| rels_AMENDED_BY.csv | 251 |
| rels_CROSS_REFERENCES.csv | 184 |
| rels_HAS_ADDENDUM.csv | 10 |
| rels_HAS_ADDENDUM_ARTICLE.csv | 31 |
| **Total relationships** | **1,339** |

## Coverage notes

- Extraction is at **clause level and verbatim**: every `(n)` paragraph, every `n.` subparagraph and
  every `(a)` item that carries text is its own row, with the source's wording preserved exactly
  (layout line-wrapping rejoined, internal whitespace collapsed to single spaces).
- The `<Amended by …>`, `<Newly Inserted by …>` and `<Deleted by …>` annotations are **kept inside
  the clause text** (they are part of the source) and are additionally modelled via `AMENDED_BY`.
- Cross-border transfer material is fully present: Art. 14(2) (international policy), Art. 17(3)
  (consent for overseas provision), Art. 39-12 (transfer of users' information overseas, onward
  transfer to a third country), Art. 39-13 (reciprocity), Art. 39-11 (domestic agent), plus the
  sanctions in Arts. 39-15(1)7 and 75(3)3.
- The Protection Commission provisions (Arts. 7 to 7-14, 8-2 to 14) and the Dispute Mediation
  Committee (Chapter VII) are modelled clause by clause.

## Caveats / gaps

- **Translation, not the Korean original.** Article numbering and structure follow the translation.
- **Deleted provisions.** Article 8 is "Deleted"; Article 7(2)–(9), 18(2)4, 24(2) and 39(2) contain
  "Deleted" markers. These are retained as nodes with the source's own "Deleted" text so the
  numbering stays continuous — they carry no obligation.
- **Article 28-7** begins with a stray `@` character in the PDF text extract (`@Articles 20, 21, …`);
  it is preserved as-is rather than silently corrected.
- **Cross-references are endpoint-only.** Ranges such as "Articles 15 through 25" or "Articles 71
  through 73" produce edges to the two named articles, not to the intervening ones. References to
  *other* statutes ("Article 33 of the State Public Officials Act") are filtered out and produce no
  edge; a small residual risk of mis-linking remains for unusual phrasings.
- **`Penalty` nodes** record only the sanction ceiling that the provision itself states; the list of
  offences sits in the subparagraph nodes under the same article. Where the article states no
  ceiling (Art. 76, Art. 74-2 confiscation) no Penalty node is created.
- **Addenda text** for blocks whose bodies read "Articles 2 through 7 Omitted." is kept as addendum
  text rather than split into per-article rows, because the source does not spell those articles out.
- Presidential Decree content is out of scope: the Act repeatedly delegates detail to Presidential
  Decree, and those downstream rules are not in this document.

## Validation

A checker parsed every CSV, asserted node-id uniqueness (within each file and globally) and asserted
that every `source_id`/`target_id` in every relationship file resolves to an existing node id.
Result: **PASS** — 915 nodes, 1,339 relationships, 0 errors.
