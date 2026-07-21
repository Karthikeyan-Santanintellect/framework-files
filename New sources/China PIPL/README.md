# China PIPL — knowledge-graph CSV extraction

**Instrument:** Personal Information Protection Law of the People's Republic of China (PIPL)
**Source document:** `KB 2/China/Personal Information Protection Law.pdf`
**Promulgated:** Chairman's Order No. 91, 20 August 2021 (adopted at the 30th meeting of the
Standing Committee of the 13th National People's Congress). **In force:** 1 November 2021.

## Language of the source text

The source PDF is an **English translation** of the Chinese original. **The translation is
unattributed** — the document contains no translator, publisher, or "unofficial translation"
notice anywhere in its text, so no translator can be recorded. Article 74 confirms the text is
the full statute (all 8 chapters, Articles 1–74), not guidance or a commentary. Several
translation artifacts are preserved verbatim (see Caveats).

## Schema and rationale

PIPL is a civil-law statute that organises itself as **Chapters → (in Chapter II only)
Sections → Articles → unnumbered paragraphs → roman-numeral items**. The node types below use
the document's own vocabulary. Three cross-cutting node types were added because the statute
carries this content explicitly and it is the content most often queried: the definitions
(Articles 4, 28, 60, 73), the individual rights (Chapter IV plus Articles 15 and 24), and the
sanctions (Chapter VII). Every one of these carries verbatim source text plus a pointer back to
the exact clause it came from, so nothing is asserted that the statute does not say.

Extraction is at **clause level**: e.g. Article 38(1)(I) (cross-border security assessment) and
Article 47(1)(III) (deletion on withdrawal of consent) are each their own row.

### Node types
| File | Type | Rows | Notes |
|---|---|---:|---|
| `nodes_Law.csv` | Law | 1 | Title, order number, adoption/effective dates, counts |
| `nodes_Chapter.csv` | Chapter | 8 | Chapters I–VIII |
| `nodes_Section.csv` | Section | 3 | Sections 1–3 of Chapter II only |
| `nodes_Article.csv` | Article | 74 | Articles 1–74, with paragraph/item counts |
| `nodes_Paragraph.csv` | Paragraph | 106 | Verbatim; numbered within each article |
| `nodes_Item.csv` | Item | 62 | Verbatim roman-numeral items `(I)`, `(II)`, … |
| `nodes_Definition.csv` | Definition | 8 | Verbatim definitions, with defining clause |
| `nodes_Right.csv` | Right | 10 | Individual rights, with verbatim conferring clause |
| `nodes_Penalty.csv` | Penalty | 10 | Verbatim sanction wording + stated amounts |

### Relationship types
| File | Rel type | Rows |
|---|---|---:|
| `rels_HAS_CHAPTER.csv` | `Law -[HAS_CHAPTER]-> Chapter` | 8 |
| `rels_HAS_SECTION.csv` | `Chapter -[HAS_SECTION]-> Section` | 3 |
| `rels_HAS_ARTICLE.csv` | `Chapter\|Section -[HAS_ARTICLE]-> Article` | 74 |
| `rels_HAS_PARAGRAPH.csv` | `Article -[HAS_PARAGRAPH]-> Paragraph` | 106 |
| `rels_HAS_ITEM.csv` | `Paragraph -[HAS_ITEM]-> Item` | 62 |
| `rels_DEFINES.csv` | `Article -[DEFINES]-> Definition` | 8 |
| `rels_GRANTS_RIGHT.csv` | `Article -[GRANTS_RIGHT]-> Right` | 10 |
| `rels_IMPOSES_PENALTY.csv` | `Article -[IMPOSES_PENALTY]-> Penalty` | 10 |
| `rels_CROSS_REFERENCES.csv` | `Article -[CROSS_REFERENCES]-> Article` | 6 |

Articles in Chapter II are attached to their Section; all other Articles attach directly to
their Chapter. Id conventions: `chII`, `chII_s2`, `art38`, `art38_p1`, `art38_p1_I`.

## Key content captured

- **Extraterritorial scope** — Article 3(2)(I)–(III).
- **Lawful bases for processing** — Article 13(1)(I)–(VII); consent rules, Articles 14–16.
- **Sensitive personal information** (definition includes minors under 14) — Articles 28–32.
- **State organs** — Articles 33–37, including domestic storage in Article 36.
- **Cross-border provision** — Chapter III (Articles 38–43): the four Article 38 conditions,
  separate consent (Article 39), CIIO/threshold data localisation and security assessment
  (Article 40), foreign judicial/law-enforcement requests (Article 41), the restricted-provision
  list (Article 42) and reciprocal counter-measures (Article 43).
- **Individual rights** — Chapter IV (Articles 44–50), plus withdrawal of consent (Article 15)
  and automated-decision objection (Article 24(3)).
- **Processor obligations** — Chapter V (Articles 51–59): security measures, DPO threshold,
  in-China representative, audits, PIA triggers and content, three-year PIA record retention
  (Article 56), breach notification (Article 57), large-platform duties (Article 58).
- **Legal liability** — Chapter VII (Articles 66–71): RMB 1 million / RMB 10,000–100,000
  ordinary-tier fines; RMB 50 million or 5% of prior-year turnover and RMB 100,000–1 million
  personal fines for serious cases, plus licence revocation and director disqualification;
  credit-archive recording, reversed burden of proof in tort (Article 69), and procuratorate
  public-interest litigation (Article 70).

## Caveats and gaps

- All clause text is verbatim from the translation. Translation infelicities are preserved
  as-is and are **not** corrected: e.g. Article 38(1)(II) "certified by a specialized" (word
  apparently dropped in translation), Article 28 "personal dignity or natural persons",
  Article 63(1)(IV) capitalises "Articles" where it means physical articles/objects.
- `right_name` values in `nodes_Right.csv` and `penalty_id`/`applies_to` values in
  `nodes_Penalty.csv` are descriptive labels for graph navigation; the load-bearing verbatim
  content is in the `text` / `sanction_text` columns, each tied to a `clause_id`.
- Paragraphs are unnumbered in the source; `paragraph_number` is a positional index assigned by
  the extraction, matching the order the statute cites them in ("Paragraph 1 of Article 18").
- `rels_CROSS_REFERENCES.csv` covers only explicit "Article N" citations (6). Implicit
  references — "the preceding Article", "this Chapter", "this Law", "the preceding paragraph" —
  are left in the clause text and not materialised as edges.
- Two layout artifacts in the `pdftotext -layout` extract were rejoined during parsing: the
  Article 38 chapeau ran into item (I) on one line, and the two paragraphs of Article 66 ran
  together. Wording is unchanged in both cases.
- No penalty is stated for state organs beyond Article 68 (rectification and sanctions on
  responsible persons); the statute names no monetary figure there, so those cells are empty.

## Validation

A self-check parsed every CSV and confirmed: node-id column naming and uniqueness per file,
`source_document` present on every node file, `source_id,target_id,rel_type` as the first three
columns of every relationship file, and that all 287 relationship endpoints resolve to node ids.
A separate check confirmed every `text` / `definition_text` value is a whitespace-normalised
substring of the source file. Result: no problems.
