# Mexico — LFPDPPP (new Law, DOF 20-03-2025) + Regulations (2011)

Knowledge-graph CSV extraction of **two distinct instruments**, modelled separately in this folder.

## ⚠️ Read this first

1. **This is the NEW law.** `nodes_Law.csv` holds the *Federal Law for the Protection of Personal
   Data Held by Private Parties*, **New Law published in the Official Gazette of the Federation on
   March 20, 2025** (DOF 20-03-2025), enacted by the decree that also created the General Law of
   Transparency and Access to Public Information. Its Second transitory provision **repeals** the
   previous LFPDPPP of 5 July 2010. Under the new law the supervisory authority is the
   **Anticorruption and Good Governance Secretariat** ("the Secretariat"), not INAI — INAI is wound
   up by the transitory provisions.
2. **The Regulations date from 2011 and predate the new Law.** `nodes_Regulation.csv` holds the
   *Regulations to the Federal Law on the Protection of Personal Data Held by Private Parties*,
   published in the Federal Official Gazette on **21 December 2011**, i.e. regulations made under
   the **2010** Law. They still refer throughout to "the Institute" (INAI/IFAI) and to article
   numbers of the 2010 Law. Whether and how they survive the 2025 Law is **not stated in either
   source document** and is therefore not asserted anywhere in these CSVs.
3. **Cross-instrument links are citations only.** Because the Regulations' article references point
   at the *repealed 2010* numbering (e.g. "Article 3(X) of the Law" = definitions, which is
   Article 2 in the 2025 Law), linking them directly to 2025 `Article` nodes would be wrong. Every
   such reference is captured verbatim as a `CitedLawReference` node instead. The only asserted
   Regulation→Law edge is `rels_Regulation_REGULATES_LAW.csv` (1 row), justified by the
   Regulations' own Article 1.
4. **Language.** Both source extracts are **English translations**, not the Spanish originals. The
   Regulations file is explicitly stamped "Translation from Spanish". All text in these CSVs is
   verbatim from those English sources; nothing was translated, paraphrased or re-worded here.

## Sources

| Instrument | Source PDF | Text extract |
|---|---|---|
| Law (2025) | `KB 2/Mexico/Federal LAW.pdf` | `Mexico_Federal_LAW.txt` |
| Regulations (2011) | `KB 2/Mexico/2_regulations_to_the_flppdhpp.pdf` | `Mexico_2_regulations_to_the_flppdhpp.txt` |

`Mexico_Evolution_of_the_new_Federal_Law...txt` was supplied as background only and was **not**
extracted — no content from it appears in these CSVs.

## Schema

The schema follows each document's own vocabulary. The Law uses Chapter → Article →
fracción/paragraph; the Regulations add a Section level and lettered sub-paragraphs, and give every
article a rubric (heading), which is preserved.

### Law nodes (`LFPDPPP_2025`)
- **Law** — title, publication status, enacting clause.
- **Chapter** — Chapters I–XII with their titles.
- **Article** — Articles 1–64, with chapter context and full reassembled text.
- **Clause** — clause-level unit of obligation: every fracción (`..._F_I`) and every unnumbered
  paragraph (`..._P1`, `..._P2`, …) of every article. This is the row you cite.
- **Definition** — the 20 defined terms of Article 2 (fracciones I–XX), term + verbatim definition.
- **ARCORight** — the four ARCO rights, each carrying the Article 2(VII) definition and the text of
  the article that states it (22 access, 23 rectification, 24 cancellation, 26 opposition).
- **Infringement** — Article 58 fracciones I–XIX (conduct constituting a violation).
- **Sanction** — Article 59 fracciones I–IV (warning; fine 100–160,000 UMA; fine 200–320,000 UMA;
  additional persistence fine 100–320,000 UMA, doubled for sensitive data).
- **Offense** — Chapter XII criminal offences, Articles 62 (3 months–3 years), 63 (6 months–5
  years), 64 (penalties doubled for sensitive personal data).
- **TransitoryProvision** / **TransitoryClause** — the twenty transitory articles of the decree
  (First–Twentieth) and the fracciones of the repeal provision.

### Regulations nodes (`REG_LFPDPPP_2011`) — separate node types
- **Regulation**, **RegChapter**, **RegSection**, **RegArticle** (1–144, with rubric),
  **RegClause** (paragraphs, fracciones, lettered sub-paragraphs), **RegDefinition** (Article 2,
  12 terms), **RegTransitoryProvision** (First–Fifth), **CitedLawReference**.

### Relationships
`HAS_CHAPTER`, `HAS_SECTION`, `HAS_ARTICLE`, `HAS_CLAUSE`, `HAS_SUBPARAGRAPH`, `DEFINES_TERM`,
`STATES_ARCO_RIGHT`, `HAS_INFRINGEMENT`, `HAS_SANCTION`, `SANCTIONED_BY`, `DEFINES_OFFENSE`,
`HAS_TRANSITORY`, `CROSS_REFERENCES`, `CITES_LAW_PROVISION`, `REGULATES`.

`SANCTIONED_BY` is built strictly from the wording of Article 59 itself, which maps its fracciones
onto the preceding article's fracciones ("section I", "sections II to VII", "sections VIII to
XVIII"). Article 58(XIX) is deliberately unmapped: Article 59 does not assign it a sanction band.

`CROSS_REFERENCES` contains only references the Law makes to its own articles using the explicit
phrase "…of this Law"; the citation string is kept on the edge.

## Files

| File | Rows |
|---|---|
| nodes_Law.csv | 1 |
| nodes_Chapter.csv | 12 |
| nodes_Article.csv | 64 |
| nodes_Clause.csv | 235 |
| nodes_Definition.csv | 20 |
| nodes_ARCORight.csv | 4 |
| nodes_Infringement.csv | 19 |
| nodes_Sanction.csv | 4 |
| nodes_Offense.csv | 3 |
| nodes_TransitoryProvision.csv | 20 |
| nodes_TransitoryClause.csv | 5 |
| nodes_Regulation.csv | 1 |
| nodes_RegChapter.csv | 10 |
| nodes_RegSection.csv | 11 |
| nodes_RegArticle.csv | 144 |
| nodes_RegClause.csv | 459 |
| nodes_RegDefinition.csv | 12 |
| nodes_RegTransitoryProvision.csv | 5 |
| nodes_CitedLawReference.csv | 46 |
| rels_Law_HAS_CHAPTER.csv | 12 |
| rels_Chapter_HAS_ARTICLE.csv | 64 |
| rels_Article_HAS_CLAUSE.csv | 235 |
| rels_Article_DEFINES_TERM.csv | 20 |
| rels_Article_STATES_ARCO_RIGHT.csv | 4 |
| rels_Article_HAS_INFRINGEMENT.csv | 19 |
| rels_Article_HAS_SANCTION.csv | 4 |
| rels_Infringement_SANCTIONED_BY.csv | 18 |
| rels_Article_DEFINES_OFFENSE.csv | 3 |
| rels_Law_HAS_TRANSITORY.csv | 20 |
| rels_Transitory_HAS_CLAUSE.csv | 5 |
| rels_Clause_CROSS_REFERENCES.csv | 12 |
| rels_Regulation_HAS_CHAPTER.csv | 10 |
| rels_RegChapter_HAS_SECTION.csv | 11 |
| rels_RegChapter_HAS_ARTICLE.csv | 144 |
| rels_RegSection_HAS_ARTICLE.csv | 84 |
| rels_RegArticle_HAS_CLAUSE.csv | 459 |
| rels_RegClause_HAS_SUBPARAGRAPH.csv | 20 |
| rels_RegArticle_DEFINES_TERM.csv | 12 |
| rels_Regulation_HAS_TRANSITORY.csv | 5 |
| rels_RegClause_CITES_LAW_PROVISION.csv | 61 |
| rels_Regulation_REGULATES_LAW.csv | 1 |

**Totals:** 19 node files / 1,075 node rows; 22 relationship files / 1,223 relationship rows.
All ids are unique across the whole folder and every relationship endpoint resolves.

## Caveats and gaps

- Both texts are English translations of Spanish originals; article rubrics, headings and defined
  terms are therefore the translators' wording, not the DOF Spanish.
- The Law extract contains only Article Three of the enacting decree in full. Article One, Article
  Two and Article Four appear in the source only as "........" and are not modelled.
- The Regulations source numbers its chapters **I, II, III, IV, V, VII, VII, VIII, IX, X** — there
  is no Chapter VI and "Chapter VII" appears twice. This is reproduced verbatim: chapter ids are
  sequential (`REG_CH_1`…`REG_CH_10`) while the `number` column keeps the source's own (faulty)
  roman numeral.
- Regulations Article 60 and a few others contain two consecutive enumerated lists both running
  I, II, III…; the second list is given ids of the form `REG_ART_60_L2_F_I`.
- Page headers, footers, running titles and page numbers were removed; wrapped lines were rejoined
  into single-line prose with wording unchanged.
- The Regulations' Chapter V refers to secondary regulation by "departments or agencies"; no such
  secondary regulations are in the sources, so none are modelled.
