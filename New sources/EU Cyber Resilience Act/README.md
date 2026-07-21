# EU Cyber Resilience Act — knowledge-graph CSV extraction

**Source document:** `KB 2/Europe/EU Cyber Resilience Act.pdf` — Regulation (EU) 2024/2847 of the
European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements
for products with digital elements and amending Regulations (EU) No 168/2013 and (EU) No 2019/1020
and Directive (EU) 2020/1828 (Cyber Resilience Act), *Official Journal of the European Union*,
L series, 20.11.2024, 81 pages. ELI: http://data.europa.eu/eli/reg/2024/2847/oj

Extraction was made from a `pdftotext -layout` extract of the full 81-page PDF. All text is
verbatim; page headers, page footers and OJ footnote apparatus were removed and column-wrapped
lines rejoined into single-line prose without altering wording.

## Schema

The schema mirrors the instrument's own structure — an EU regulation: recitals, then enacting
terms organised as Chapters → Articles → numbered paragraphs → lettered points → roman sub-points,
then Annexes (with Parts in Annexes I and VIII). The document's own vocabulary is used for node
type names ("Chapter", "Article", "Annex", "Recital", "Definition").

### Node types

| File | Node type | Rows | Contents |
|---|---|---|---|
| `nodes_Regulation.csv` | Regulation | 1 | The instrument itself (identifier, full title, adoption/publication/application dates, ELI). |
| `nodes_Recital.csv` | Recital | 130 | Recitals (1)–(130) of the preamble, full verbatim text. |
| `nodes_Chapter.csv` | Chapter | 8 | Chapters I–VIII with their headings. |
| `nodes_Article.csv` | Article | 71 | Articles 1–71 with their headings and parent chapter. |
| `nodes_Provision.csv` | Provision | 527 | Clause-level units of the enacting terms: numbered paragraphs, unnumbered sub­paragraphs, lettered points, roman sub-points. `label` gives the citable reference (e.g. `14(2)(c)(i)`), `level` gives the kind of subdivision. |
| `nodes_Definition.csv` | Definition | 51 | The 51 defined terms of Article 3, with the term, the verbatim definition, and the full point text. |
| `nodes_Annex.csv` | Annex | 8 | Annexes I–VIII with their titles. |
| `nodes_AnnexProvision.csv` | AnnexProvision | 142 | Clause-level units of Annexes I, II, V, VI, VII, VIII (Parts, points, sub-points), including the essential cybersecurity requirements (Annex I Part I), the vulnerability handling requirements (Annex I Part II), the user information items (Annex II), the technical documentation content (Annex VII) and the four conformity assessment modules (Annex VIII Parts I–IV). |
| `nodes_ProductCategory.csv` | ProductCategory | 26 | The important product categories of Annex III (class I: 19, class II: 4) and the critical product categories of Annex IV (3). |
| `nodes_Penalty.csv` | Penalty | 3 | The three administrative-fine tiers stated in Article 64(2), (3) and (4), with the ceiling in EUR and as a share of worldwide annual turnover, plus the verbatim clause. |
| `nodes_Date.csv` | Date | 11 | Every calendar date stated in the enacting terms/annexes (application dates, deadlines for delegated and implementing acts, transitional dates). |

### Relationship types

| File | Rows | Meaning |
|---|---|---|
| `rels_HAS_RECITAL.csv` | 130 | Regulation → Recital |
| `rels_HAS_CHAPTER.csv` | 8 | Regulation → Chapter |
| `rels_HAS_ARTICLE.csv` | 71 | Chapter → Article |
| `rels_HAS_PROVISION.csv` | 527 | Article → Provision and Provision → Provision (nesting) |
| `rels_DEFINES.csv` | 51 | Article 3 → Definition |
| `rels_HAS_ANNEX.csv` | 8 | Regulation → Annex |
| `rels_HAS_ANNEX_PROVISION.csv` | 142 | Annex → AnnexProvision and AnnexProvision → AnnexProvision (nesting) |
| `rels_LISTS_PRODUCT_CATEGORY.csv` | 26 | Annex III / Annex IV → ProductCategory |
| `rels_IMPOSES_PENALTY.csv` | 3 | Provision (Article 64(2)–(4)) → Penalty |
| `rels_SETS_DATE.csv` | 16 | Provision / AnnexProvision → Date stated in it |
| `rels_REFERENCES_ARTICLE.csv` | 155 | Provision / AnnexProvision → Article of *this* Regulation cited in it (`citation` column keeps the exact citation string, e.g. `Article 32(2)`) |
| `rels_REFERENCES_ANNEX.csv` | 121 | Provision / AnnexProvision → Annex of *this* Regulation cited in it |

## Validation

A self-check script parsed every CSV and confirmed: 978 node ids, all unique within their file;
every `source_id`/`target_id` in every relationship file resolves to an existing node id; every
node file starts with its `<type>_id` column and carries `source_document`; every relationship file
starts with `source_id,target_id,rel_type`. Result: **OK**.

## Caveats and notes

- **Cross-references are internal only.** References to other Union acts (Directive (EU) 2022/2555,
  Regulation (EU) 2019/881, Regulation (EU) 2019/1020, etc.) are left inside the verbatim clause
  text and are not modelled as relationships, because those instruments are not in this graph.
- Article 3 points appear twice by design: as `Provision` rows (they are clauses of Article 3) and
  as `Definition` rows (the defined-term view).
- Annex III/IV items are modelled only as `ProductCategory` nodes, not as `AnnexProvision` rows,
  since they are a flat product list rather than obligation text.
- Annex VIII sub-headings that sit on the same numbered point as their text (e.g. Part I point 3
  "Design, development, production and vulnerability handling of products with digital elements")
  are stored joined with that point's following paragraph, exactly as the point reads in the source.
- Article 68 amends a table in Annex II to Regulation (EU) No 168/2013; the table row is preserved
  as flattened text (`16 18 protection of vehicle against x x … cyberattacks`) — the column layout
  of the original table is not reconstructable from the text extract.
- Obvious wording of the source is preserved verbatim including its own typographic oddities
  (e.g. Article 64(2): "up to 2,5 % of the its total worldwide annual turnover").
- OJ footnotes (references to the cited external acts, 38 in total) were treated as page apparatus
  and are not modelled; footnote reference markers such as "(34)" remain inline in recital text as
  they appear in the extract.
- The signature block, the closing statement note (OJ C, 2024/6786) and the running ELI/page
  furniture are not modelled.
