# Bahrain Personal Data Protection Law (Law No. (30) of 2018) — knowledge-graph CSVs

**Source document:** `KB 2/Bahrain/Bahrain Personal Data Protection Law.pdf`
(extracted with `pdftotext -layout`; 1,622 lines, read in full).

**Language:** The source text is an **English translation** of the Arabic statute. The PDF
carries no translator attribution or "unofficial translation" disclaimer, so the translation's
official status cannot be determined from the document itself. All text in these CSVs is
verbatim from that English text; nothing was re-translated, paraphrased or supplied from
outside the document.

## Schema

The schema follows the law's own structure and vocabulary: the instrument opens with a
royal preamble ("Having perused …"), four unnumbered promulgation articles (First–Fourth
Article), and then the Law proper, organised as **Part → Section → Article → numbered
paragraph → lettered sub-paragraph → roman sub-item**.

### Node types

| File | Node type | Rows | Notes |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | Title, King, place/date of promulgation (Riffa Palace, 28/10/1439 A.H. / 12/07/2018 A.D.), approving councils, language note |
| `nodes_PreambleCitation.csv` | PreambleCitation | 21 | Each instrument cited in the "Having perused" recital, in order |
| `nodes_PromulgationArticle.csv` | PromulgationArticle | 4 | First–Fourth Article (scope, treaty saving, 6-month deadline for Board resolutions, 1-year commencement) |
| `nodes_Part.csv` | Part | 3 | Part (1) Provisions with respect to processing; Part II Data Protection Authority; Part 3 Accountability of Data Controller and Data Guardian |
| `nodes_Section.csv` | Section | 11 | The document's own Sections, with their headings |
| `nodes_Article.csv` | Article | 60 | Articles (1)–(60), with heading; `text` carries the chapeau/full prose where the Article is not subdivided |
| `nodes_Clause.csv` | Clause | 310 | Every numbered paragraph, lettered sub-paragraph and roman sub-item that carries text; `level` 1/2/3, `parent_clause_id` for nesting |
| `nodes_Definition.csv` | Definition | 21 | Every defined term in Article (1), verbatim |
| `nodes_DataSubjectRight.csv` | DataSubjectRight | 9 | Section Five rights, named by the Article heading that grants them |
| `nodes_AuthorityBody.csv` | AuthorityBody | 5 | Authority, Board of Directors, Chief Executive, Appeal Tribunal, Investigation committee |
| `nodes_Penalty.csv` | Penalty | 5 | Administrative measures (Art. 55) and criminal penalties (Art. 58), with the verbatim amounts |
| `nodes_Deadline.csv` | Deadline | 29 | Verbatim time-period phrases stated in clauses, linked to the clause that states them |

### Relationship types

| File | Rel type | Rows |
|---|---|---|
| `rels_HAS_PREAMBLE_CITATION.csv` | HAS_PREAMBLE_CITATION | 21 |
| `rels_HAS_PROMULGATION_ARTICLE.csv` | HAS_PROMULGATION_ARTICLE | 4 |
| `rels_HAS_PART.csv` | HAS_PART | 3 |
| `rels_HAS_SECTION.csv` | HAS_SECTION | 11 |
| `rels_HAS_ARTICLE.csv` | HAS_ARTICLE | 60 |
| `rels_HAS_CLAUSE.csv` | HAS_CLAUSE | 175 |
| `rels_HAS_SUBCLAUSE.csv` | HAS_SUBCLAUSE | 135 |
| `rels_DEFINES_TERM.csv` | DEFINES_TERM | 21 |
| `rels_GRANTS_RIGHT.csv` | GRANTS_RIGHT | 9 |
| `rels_ESTABLISHES_BODY.csv` | ESTABLISHES_BODY | 5 |
| `rels_PRESCRIBES_PENALTY.csv` | PRESCRIBES_PENALTY | 5 |
| `rels_SETS_DEADLINE.csv` | SETS_DEADLINE | 29 |
| `rels_REFERENCES_ARTICLE.csv` | REFERENCES_ARTICLE | 43 |

`REFERENCES_ARTICLE` is derived only from explicit "Article (n)" citations appearing in the
clause text of this Law; the `citation` column records the citation string as written.

## Key content captured

- **Transfer rules:** Article (12) (adequacy record published in the Official Gazette;
  case-by-case authorisation with the three assessment factors) and Article (13) (consent,
  public register, contract/vital-interests/legal-obligation/legal-claim necessity, and
  Authority-approved safeguards).
- **Penal provisions:** Article (55) administrative measures — withdrawal of authorisation,
  daily penalty not exceeding BD1000/- per day (BD2000/- per day on a second violation within
  3 years), administrative penalty not exceeding twenty thousand Bahraini dinars; Article (58)
  crimes — imprisonment up to one year and/or fine BD 1000/– to BD 20,000/–, fine BD 3,000/– to
  BD 20,000/– for conflict-of-interest breaches, and imprisonment up to one month and/or fine
  BD 100/– to BD 500/– for misuse of the Authority's logo; Article (59) doubles fine limits for
  legal persons; Article (60) permits conciliation for Article (58)(1)(c)–(e).
- **Authority:** establishment, ministerial oversight, financing, 15 enumerated duties,
  conflict-of-interest register, annual report, Appeal Tribunal, inspection powers, CBB
  notification, seven-member Board, and the Chief Executive's appointment/duties/removal.

## Caveats and gaps

- **Translation.** See the language note above. Grammatical oddities, inconsistent
  capitalisation and typographical slips in the source ("date" for "data" in the Article (49)
  heading and text; "prescribe" for "prescribed"; "The Data Processor will only act on a
  processing"; "shall laps"; doubled full stop at the end of Article (43)(5)) are preserved
  verbatim rather than corrected.
- **Article (55) numbering is defective in the source.** After paragraphs 1 and 2 the printed
  text runs "5." (publication of violations) and then "4." (referral to the Public
  Prosecution); there is no paragraph 3. The printed labels and printed order are preserved
  as `ART-55-5` and `ART-55-4`. Similarly Article (20)(2) ends with an item "4." that states a
  complaint right rather than a notification outcome; it is kept as sub-item (d) as printed.
- **Sub-item lettering.** The layout extract renders second-level lists as "1., 2., 3.", but the
  Law cites them as letters (e.g. "Paragraph 2(c)", "Paragraphs (1)(a) to (1)(d)", "paragraph
  (1/b)"). Second-level items are therefore labelled a, b, c … in line with the Law's own
  citation practice; first-level paragraph numbering and third-level roman numbering follow the
  source.
- **No implementing resolutions.** The Law repeatedly delegates detail to Board resolutions and
  Ministerial decisions (fees, security conditions, guardian registration, complaint procedures).
  Those instruments are not in this PDF, so the corresponding cells contain only what the Law
  itself states.
- **Article (1) definition of "Third party"** contains an embedded 5-item list; it is stored as a
  single verbatim definition string rather than being split into clause rows, since the list is
  part of the definition.
- Sections and Parts are cited exactly as printed, including the inconsistent styling
  ("Part (1)", "Part II", "Part 3"; "Section two" / "Section Three").
- No incident data, examples, guidance or commentary appear in the source; none was added.

## Self-check

`bh_check.py` (run from the extraction scratchpad) parses every CSV, asserts node ids are
unique within each file and globally, asserts every relationship endpoint resolves to a node id,
checks the `<type>_id` first-column and `source_document` conventions, and prints row counts.
**Result: 0 errors.**
