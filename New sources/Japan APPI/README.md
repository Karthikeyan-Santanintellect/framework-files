# Japan — Act on the Protection of Personal Information (APPI)

Knowledge-graph CSV extraction of the Act on the Protection of Personal Information
(Act No. 57 of 2003), Japan.

## Source

- **Source document:** `KB 2/Japan/Act on the Protection of Personal Information (APPI).pdf`
- **Language / status:** The source is an **English translation**, and the document states it
  explicitly: *"This English translation of the Act on the Protection of Personal Information has
  been translated (through the revisions of Act No. 119 of 2003 ( Effective April 1, 2005)) in
  compliance with the Standard Bilingual Dictionary ( March 2006 edition)."* and *"This is an
  unofficial translation. Only the original Japanese texts of laws and regulations have legal
  effect, and the translations are to be used solely as reference material to aid in the
  understanding of Japanese laws and regulations."* The first page also carries the same notice in
  Japanese. All extracted text is the English translation verbatim.

## Schema

The Act's own hierarchy is Chapter → (Section, in Chapters 3 and 4) → Article → paragraph → item →
lettered sub-item, so the node types mirror that vocabulary exactly rather than a generic template.
Two cross-cutting node types were added because the Act itself isolates them as distinct legal
content: `DefinedTerm` (Article 2 and the "hereinafter referred to as" definitions elsewhere) and
`Penalty` (Chapter 6).

### Node types

| File | Node type | Rows | Notes |
|---|---|---|---|
| `nodes_Chapter.csv` | Chapter | 7 | Chapters 1–6 plus "Supplementary Provisions ( Extract)" |
| `nodes_Section.csv` | Section | 6 | Chapter 3 Sections 1–4; Chapter 4 Sections 1–2 |
| `nodes_Article.csv` | Article | 65 | Articles 1–59 plus Supplementary Provisions Articles 1–6. `text` is populated only for articles that have no numbered paragraphs; otherwise the text lives on the paragraph rows |
| `nodes_Paragraph.csv` | Paragraph | 77 | Numbered paragraphs `(1)`, `(2)`, … verbatim |
| `nodes_Item.csv` | Item | 68 | Numbered items `(i)`, `(ii)`, … Parent is a paragraph, or an article where the article has items but no paragraphs (Articles 38, 39, 59) |
| `nodes_Subitem.csv` | Subitem | 2 | Article 38 item (iii) letters (a) and (b) — the only lettered subdivisions in the Act |
| `nodes_DefinedTerm.csv` | DefinedTerm | 15 | Every term the Act defines, with its verbatim definition and the clause that defines it |
| `nodes_Penalty.csv` | Penalty | 5 | Chapter 6 offences with verbatim sanction text; `imprisonment_max` / `fine_max` filled only where the Act states a figure |

### Relationship types

| File | Rel type | Rows |
|---|---|---|
| `rels_HAS_SECTION.csv` | HAS_SECTION (Chapter → Section) | 6 |
| `rels_HAS_ARTICLE.csv` | HAS_ARTICLE (Chapter or Section → Article) | 65 |
| `rels_HAS_PARAGRAPH.csv` | HAS_PARAGRAPH (Article → Paragraph) | 77 |
| `rels_HAS_ITEM.csv` | HAS_ITEM (Paragraph or Article → Item) | 68 |
| `rels_HAS_SUBITEM.csv` | HAS_SUBITEM (Item → Subitem) | 2 |
| `rels_DEFINES.csv` | DEFINES (clause → DefinedTerm) | 15 |
| `rels_PRESCRIBES_PENALTY.csv` | PRESCRIBES_PENALTY (clause → Penalty) | 5 |
| `rels_REFERENCES.csv` | REFERENCES (clause → cited clause), with a `citation` column carrying the Act's own wording of the cross-reference | 78 |

Total node ids: 245. Validation script confirms ids are unique across all node files and every
relationship endpoint resolves.

## Caveats and gaps

- **Vintage.** This translation reflects the Act *as enacted in 2003 and in force from 1 April
  2005*. It therefore does **not** contain the Personal Information Protection Commission (PPC),
  which was created by the 2015/2016 amendments. In this text the supervisory authority is the
  "competent minister" (Articles 32–36, 46–49) with the Prime Minister designating competent
  ministers. Nothing about the PPC has been added — the graph reflects only what the source states.
  For the same reason there are no provisions on sensitive/special-care-required personal
  information, anonymously processed information, cross-border transfer restrictions, or
  breach-notification obligations: those postdate this text.
- **Unofficial translation**, per the source's own disclaimer; the Japanese original governs.
- The Supplementary Provisions are marked "( Extract)" in the source, so Articles 1–6 of the
  Supplementary Provisions are all that is present.
- Articles 7, 14, 56, 57, 58 and 59 and Supplementary Articles 3 and 5 carry no parenthetical
  heading in the source; their `heading` cells are deliberately empty.
- Layout artifacts from `pdftotext -layout` (page numbers, column wrapping, doubled spaces) were
  rejoined into single-line prose; wording, punctuation and the source's own irregular spacing
  inside parentheses (e.g. `( v)`, `( including`) are otherwise preserved as-is. The source also
  contains occasional typographic/grammatical oddities of the translation itself (e.g.
  "enforecement" in Article 54, "on the handle of personal information" in Articles 32–33); these
  are reproduced verbatim rather than corrected.
- Cross-references captured in `rels_REFERENCES.csv` are those stated in the text, including
  relative references ("the preceding article", "the next paragraph") resolved to the clause they
  denote; the `citation` column preserves the Act's original wording. External-statute references
  (e.g. the National Government Organization Law) are left inside the clause text and are not
  modelled as nodes, except where they point back into this Act.
