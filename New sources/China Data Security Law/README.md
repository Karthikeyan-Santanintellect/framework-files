# Data Security Law of the People's Republic of China — knowledge-graph CSVs

## Source

- **Instrument:** Data Security Law of the People's Republic of China (DSL)
- **Source document:** `KB 2/China/Data Security Law of China.pdf`
- **Promulgator:** Standing Committee of the National People's Congress
- **Document number:** Order of the President of the People's Republic of China No. 84
- **Adopted:** 10 June 2021, at the 29th session of the Standing Committee of the 13th National People's Congress
- **In force:** 1 September 2021
- **Structure:** 7 Chapters, 55 Articles

### Language / translation

**The extracted text is an English translation, not the authentic Chinese text.** The authentic
text of the DSL is the Chinese original adopted by the NPC Standing Committee. The source PDF
does not name the translator or the translating body — it carries only document metadata
(promulgation date, effectiveness, taxonomy, industry category) of the kind produced by
commercial Chinese-law databases. **Whose translation this is therefore cannot be stated from
the source**, and no attribution has been invented here. One evident translation/typesetting
error is preserved verbatim in Article 21 ("umportant aspects of people's livelihood").

This is a **distinct instrument from the Personal Information Protection Law (PIPL)**, which is
extracted separately. The DSL governs data handling activities and data security generally; it
defers personal-information matters to other law (Article 53).

## Schema

The document's own vocabulary is used: it is organised into Chapters and numbered Articles, and
Articles are composed of unnumbered but typographically distinct paragraphs. There are no
lettered items or sub-items anywhere in this statute — the paragraph is the deepest subdivision
the instrument uses, so the paragraph is the clause-level unit here.

### Node types

| File | Node | Rows | Description |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | The Law itself with promulgation/effect metadata |
| `nodes_Chapter.csv` | Chapter | 7 | Chapters I–VII with verbatim titles |
| `nodes_Article.csv` | Article | 55 | Articles 1–55, full verbatim text and paragraph count |
| `nodes_Paragraph.csv` | Paragraph | 75 | Every paragraph of every Article, verbatim (clause level) |
| `nodes_Definition.csv` | Definition | 4 | Defined terms: data, data handling, data security (Art. 3); core data of the State (Art. 21) |
| `nodes_DataSecuritySystem.csv` | DataSecuritySystem | 9 | The classified-and-graded protection system, important-data catalogues, risk assessment/reporting/early-warning mechanism, emergency response mechanism, security review system, export controls, reciprocal measures, national coordination mechanism |
| `nodes_Obligation.csv` | Obligation | 17 | Duty-bearing paragraphs of Chapters IV and V, with the duty-bearer as named by the text |
| `nodes_Penalty.csv` | Penalty | 15 | Liability provisions of Chapter VI, with fine floors/ceilings as separate fields |
| `nodes_Authority.csv` | Authority | 7 | Bodies the Law assigns duties to, named verbatim |
| `nodes_ExternalInstrument.csv` | ExternalInstrument | 2 | Other laws the DSL defers to (Cybersecurity Law; Law on Protecting State Secrets) |

### Relationship types

| File | Rel type | Rows |
|---|---|---|
| `rels_has_chapter.csv` | HAS_CHAPTER | 7 |
| `rels_has_article.csv` | HAS_ARTICLE | 55 |
| `rels_has_paragraph.csv` | HAS_PARAGRAPH | 75 |
| `rels_defines_term.csv` | DEFINES_TERM | 4 |
| `rels_establishes_system.csv` | ESTABLISHES_SYSTEM | 9 |
| `rels_imposes_obligation.csv` | IMPOSES_OBLIGATION | 17 |
| `rels_prescribes_penalty.csv` | PRESCRIBES_PENALTY | 15 |
| `rels_penalty_for_article.csv` | PENALTY_FOR_ARTICLE | 13 |
| `rels_assigns_authority.csv` | ASSIGNS_AUTHORITY | 7 |
| `rels_cites_external_instrument.csv` | CITES_EXTERNAL_INSTRUMENT | 2 |
| `rels_cross_reference.csv` | CROSS_REFERENCES | 6 |

Total: 192 nodes, 210 relationships.

## Coverage of the requested topics

- **Definitions** — Article 3 (data, data handling, data security); Article 21 paragraph 2 (core
  data of the State). These are the only definitional provisions in the Law.
- **Data classification/grading** — Article 21 (classified and graded data protection system,
  important data catalogues, core data of the State, regional/departmental catalogues), modelled
  as `DataSecuritySystem` nodes anchored to their paragraphs.
- **Important data rules** — Article 27 paragraph 2 (responsible personnel), Article 30
  (periodic risk assessment and report contents), Article 31 (cross-border transfer),
  Article 46 (penalties for unlawful outbound provision).
- **Security obligations** — Chapter IV (Articles 27–36) and Chapter V (Articles 37–43),
  captured both as verbatim paragraphs and as `Obligation` nodes.
- **Cross-border provisions** — Article 11 (secure and free cross-border flow), Article 25
  (export controls), Article 26 (reciprocal measures), Article 31 (cross-border transfer of
  important data), Article 36 (foreign judicial/law-enforcement requests), Article 46 and
  Article 48 paragraph 2 (corresponding penalties).
- **Legal liability** — Chapter VI (Articles 44–52), with monetary thresholds recorded verbatim
  in the currency wording used by the translation (e.g. `CNY50,000`, `CNY2 million`).

## Caveats and gaps

- **Translation, translator unnamed** — see above. Terminology in this translation ("data
  handling", "those conducting data handling activities") differs from other common renderings
  ("data processing", "data processors"); the source wording is preserved unchanged.
- **Paragraph numbering is editorial.** The statute's paragraphs are unnumbered; `ART27-P2` etc.
  are ordinal identifiers assigned during extraction. Paragraph boundaries were taken from the
  source's own paragraph breaks, with page-break artefacts in the `pdftotext -layout` extract
  reconciled against an explicit, source-verified list of paragraph-opening phrases.
- **Interpretive fields.** On `nodes_Obligation.csv` and `nodes_Penalty.csv` the `duty_bearer`,
  `subject`, `violation` and `sanctions` fields are short labels drawn from the wording of the
  paragraph they summarise; the adjacent `text` column always carries the verbatim paragraph.
  All other text fields are verbatim.
- **`ART21-P2` is the source of the typo `umportant`.** Retained deliberately, per verbatim rule.
- **Article 43** extends Chapter V to organizations with public affairs management functions;
  this is modelled as CROSS_REFERENCES edges from Article 43 to Articles 37–42.
- The front-matter table on page 1 of the PDF (taxonomy, industry category) is database metadata
  rather than statutory text and is not modelled, apart from the promulgation dates and document
  number recorded on the Instrument node.
