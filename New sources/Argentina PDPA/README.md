# Argentina — Personal Data Protection Act (Law 25.326, 2000)

Knowledge-graph CSV extraction of Argentina's Ley 25.326 ("Personal Data Protection Act"),
together with Decree 995/2000 (the partial-veto / enactment decree printed with it).

**Source document:** `KB 2/South America/Argentina Personal Data Protection Act 2000.pdf`
(text layer extracted with `pdftotext -layout`).

**Language:** The source PDF is an **English translation** of the Spanish original
(Ley 25.326). All text in these CSVs is verbatim from that English translation — including
its own typos and translation artefacts, which have been preserved rather than corrected
(e.g. "Health-date data" in Article 8, "subArticle" used for *inciso*, "hábeas"/"habeas"
spelled both ways, "jointly and severely liable" in Article 11(4)). No Spanish source text
was available, so nothing here is Spanish.

## Schema

The statute's own vocabulary is used: it is organised into **Chapters** (I–VII) containing
numbered **Articles**, whose bodies divide into numbered *subArticles* / lettered items and
unnumbered paragraphs. Those subdivisions are modelled as **Clause** (first level of
subdivision inside an Article, whether a numbered subArticle or an unnumbered paragraph) and
**SubClause** (lettered or numbered items nested inside a clause, e.g. Article 5(2)(a)).
Definitions, sanctions, and the enacting decree get their own node types because they are the
elements most often queried independently of position in the text.

### Node types

| File | Rows | What it holds |
|---|---|---|
| `nodes_Instrument.csv` | 1 | The Act itself: law number, year, jurisdiction, subject-matter line, enacting formula. |
| `nodes_Chapter.csv` | 7 | Chapters I–VII with their headings. |
| `nodes_Article.csv` | 48 | Articles 1–48, with verbatim heading line and the parenthetical rubric as `title`. |
| `nodes_Clause.csv` | 118 | First-level subdivisions: numbered subArticles and unnumbered paragraphs. Verbatim `text`, plus `deadline_or_term` where the clause states a period. |
| `nodes_SubClause.csv` | 54 | Lettered/numbered items nested inside a clause (Art. 5(2), 6, 11(3), 12(2), 21(2), 22(2), 29(1), 32, 33(1), 36 second paragraph). |
| `nodes_Definition.csv` | 9 | The nine defined terms of Article 2, term and verbatim definition. |
| `nodes_Sanction.csv` | 7 | The administrative penalty of Article 31(1) (with its $1,000–$100,000 peso range) and the six criminal penalties Article 32 inserts as Criminal Code Articles 117 bis and 157 bis. |
| `nodes_Decree.csv` | 1 | Decree 995/2000. |
| `nodes_Recital.csv` | 15 | The "CONSIDERING"/"WHEREAS" paragraphs of Decree 995/2000, in document order. |
| `nodes_DecreeArticle.csv` | 5 | Articles 1–5 of Decree 995/2000. |

### Relationship types

| File | Rows | Meaning |
|---|---|---|
| `rels_HAS_CHAPTER.csv` | 7 | Instrument → Chapter |
| `rels_HAS_ARTICLE.csv` | 48 | Chapter → Article; Articles 44–48 sit outside any Chapter and hang off the Instrument (flagged in the `note` column). |
| `rels_HAS_CLAUSE.csv` | 118 | Article → Clause |
| `rels_HAS_SUBCLAUSE.csv` | 54 | Clause → SubClause |
| `rels_DEFINES.csv` | 9 | Article 2 → Definition |
| `rels_IMPOSES_SANCTION.csv` | 7 | Clause/SubClause → Sanction |
| `rels_CROSS_REFERENCES.csv` | 16 | Clause/SubClause/Recital → Article, for internal references to other Articles of this Act. |
| `rels_ENACTED_BY_DECREE.csv` | 1 | Instrument → Decree 995/2000 |
| `rels_HAS_RECITAL.csv` | 15 | Decree → Recital |
| `rels_HAS_DECREE_ARTICLE.csv` | 5 | Decree → Decree Article |
| `rels_OBSERVES.csv` | 2 | Decree Article → the Act's Article it vetoes ("observes"): Articles 29 and 47. |

## Caveats and gaps

- **Article 16 has no subArticle 5.** The printed text jumps from a blank "5." to "6."; the
  blank item is simply absent from the CSVs rather than being invented.
- **Article 29(2) and 29(3) read only "(vetoed)"**, and **Article 47** likewise — these were
  observed by Decree 995/2000. Their clause rows carry that verbatim text and nothing more.
- Cross-references are only created for references to Articles *of this Act*. References to
  the National Constitution (Art. 43), Act 21526 (Art. 39), Act 17622, Act 25237 and to the
  Criminal Code Articles 117 bis / 157 bis are left as text inside the clause and are not
  edges, since those targets are outside this instrument.
- Page headers/footers ("Law 25.326 / Personal Data Protection Act", page numbers) were
  excluded; column-wrapped lines were rejoined into single-line prose with wording unchanged.
- `deadline_or_term` is a verbatim phrase lifted from the clause text where the clause states
  a period; it is empty where the clause states none.
- The heading of Article 8 and of Articles 45, 47 and 48 shares a line with the body text in
  the source; the heading prefix is kept in `nodes_Article.heading` and removed from the
  clause text (except for Article 47, where the whole line is the content).

## Validation

All CSVs are UTF-8 with a header row, minimal quoting, and no embedded newlines. A checker
verified that every node id is unique within its file, that every node row carries
`source_document`, that every relationship file begins with `source_id,target_id,rel_type`,
and that both endpoints of all 282 relationships resolve to an existing node id. Result: pass.
