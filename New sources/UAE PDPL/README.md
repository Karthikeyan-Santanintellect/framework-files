# UAE PDPL — Federal Decree by Law No. (45) of 2021 Concerning the Protection of Personal Data

Knowledge-graph CSV extraction of the UAE Personal Data Protection Law (PDPL).

## Source document

- **Instrument:** Federal Decree by Law No. (45) of 2021 Concerning the Protection of Personal Data (United Arab Emirates)
- **Source PDF:** `KB 2/UAE/Federal Decree by Law No. (45) of 2021 Concerning the Protection of Personal Data.pdf`
- **Issued:** 13 / Safar / 1443 AH, corresponding 20 / September / 2021 AD, at the Presidency Palace in Abu Dhabi
- **Entry into force:** 02 January 2022 (Article 31)

### Language — this text IS a translation

**The source text is an English translation of the Arabic original.** The Arabic text is the
authoritative version; this extraction reproduces the English translation verbatim. The
translation shows characteristic artefacts that are preserved as-is in the CSVs, e.g.:

- Article 1 defines the term **"Office"** as "The UAE Data **Bureau**…", while every operative
  Article thereafter uses **"the Bureau"**. Both renderings of the same body (the UAE Data
  Office, established under Federal Decree by Law No. (44) of 2021) appear in the text.
- Article 2(2)(g) says "free zones in the **Country**" where the defined term is "State".
- Minor typographic/grammatical slips: "processing of **date**" (Art. 6(1)), "the **Date** Subject's"
  (Art. 22(1)), "a judicial **o** regulatory authority" (Art. 22(1)), "this **By-Law**" (Art. 13(1)(g)),
  "Paragraph**1**" (Art. 20(2)), "shall **by** published" (Art. 31), "the Bureau**'** powers" (Art. 27),
  "competencies **prescribes** for the Bureau" (Art. 3), "employees' ability **of** to work" (Art. 4(4)).

All of the above are reproduced verbatim. Nothing has been silently corrected.

## Schema and why

The decree-law has no Chapters or Parts — it is a flat run of 31 numbered Articles, each with a
title, and each subdividing into numbered paragraphs (Clauses) and lettered items (SubClauses).
The schema therefore mirrors the document's own vocabulary and nesting exactly:

```
Instrument ──HAS_ARTICLE──▶ Article ──HAS_CLAUSE──▶ Clause ──HAS_SUBCLAUSE──▶ SubClause
     │                         │
     │                    (Article 1) ──DEFINES──▶ Definition
     └──CITES──▶ CitedLegislation        (preamble "Having reviewed" list)

any node ──CROSS_REFERENCES──▶ Article / Clause / CitedLegislation
```

### Node types

| File | Type | What it holds |
|---|---|---|
| `nodes_Instrument.csv` | Instrument | The decree-law itself: number, year, promulgating authority, issue dates (Hijri + Gregorian), place of issue, entry-into-force date. |
| `nodes_CitedLegislation.csv` | CitedLegislation | The Constitution and the seven federal laws/decree-laws reviewed in the preamble, plus the Cabinet-presentation recital. Amendment notes ("as amended") retained in their own column. |
| `nodes_Article.csv` | Article | All 31 Articles with number, title, citation, and — where the Article has no numbered paragraphs (Arts. 3, 19, 25–31) or has a chapeau introducing them (Arts. 1, 4, 5, 7, 8, 17, 22) — its verbatim text. |
| `nodes_Clause.csv` | Clause | Every numbered paragraph, e.g. Article (13)(1). Verbatim. |
| `nodes_SubClause.csv` | SubClause | Every lettered item, e.g. Article (13)(1)(g). Verbatim. |
| `nodes_Definition.csv` | Definition | The 20 defined terms of Article (1) with verbatim definitions. |

### Relationship types

| File | Rel | Endpoints |
|---|---|---|
| `rels_has_article.csv` | HAS_ARTICLE | Instrument → Article (with document order) |
| `rels_has_clause.csv` | HAS_CLAUSE | Article → Clause |
| `rels_has_subclause.csv` | HAS_SUBCLAUSE | Clause → SubClause |
| `rels_defines.csv` | DEFINES | Article (1) → Definition |
| `rels_cites.csv` | CITES | Instrument → CitedLegislation |
| `rels_cross_references.csv` | CROSS_REFERENCES | Article/Clause/SubClause → the Article or Clause it names, carrying the verbatim referring phrase |

## Row counts

| File | Rows (excl. header) |
|---|---|
| `nodes_Instrument.csv` | 1 |
| `nodes_CitedLegislation.csv` | 9 |
| `nodes_Article.csv` | 31 |
| `nodes_Clause.csv` | 88 |
| `nodes_SubClause.csv` | 80 |
| `nodes_Definition.csv` | 20 |
| `rels_has_article.csv` | 31 |
| `rels_has_clause.csv` | 88 |
| `rels_has_subclause.csv` | 80 |
| `rels_defines.csv` | 20 |
| `rels_cites.csv` | 9 |
| `rels_cross_references.csv` | 21 |
| **Total nodes** | **229** |
| **Total relationships** | **249** |

Validated: all node ids unique (globally, not just per file); all 249 relationship endpoints
resolve to an existing node id; every node file's first column is `<type>_id` and carries
`source_document`.

## Subject-matter coverage

- **Article 1** — 20 definitions, including Personal Data, Sensitive Personal Data, Biometric
  Data, Controller, Processor, Data Protection Officer, Processing, Automated Processing,
  Pseudonymisation, Anonymization, Data Breach, Profiling, Cross-Border Processing, Consent.
- **Articles 2–3** — scope (extraterritorial reach in 2(1)(b)–(c); seven exclusions in 2(2),
  including government data, health/banking data under other legislation, and free-zone entities
  with special legislation) and the Bureau's exemption power.
- **Article 4** — lawful bases: the 11 cases in which Personal Data may be processed without the
  data subject's consent.
- **Articles 5–6** — processing principles and the conditions/withdrawal of consent.
- **Articles 7–8** — Controller and Processor general obligations, including records of processing.
- **Article 9** — data-breach reporting to the Bureau and to the data subject.
- **Articles 10–12** — appointing the Data Protection Officer, DPO roles, and the
  Controller/Processor duties towards the DPO.
- **Articles 13–19** — data subject rights: information, portability/transfer, correction and
  erasure, restriction of processing, objection/stop processing, automated decision-making
  (with a human-review requirement in 18(4)), and contacting the Controller.
- **Articles 20–21** — Personal Data Security measures and Data Protection Impact Assessment.
- **Articles 22–23** — cross-border transfer where an adequate protection level exists (22) and
  where it does not (23: contracts, explicit consent, judicial claims, contract performance,
  international judicial cooperation, public interest).
- **Articles 24–27** — complaints to the Bureau, grievance against Bureau decisions, administrative
  penalties, and delegation of Bureau powers to local authorities.
- **Articles 28–31** — Executive Regulations, regularisation, repeals, publication and enforcement.

### Deadlines and thresholds stated in the text

| Provision | Stated period |
|---|---|
| Article 25 | Grievance to the General Director within **(30) thirty days** of notice; decision within **(30) thirty days** of submission |
| Article 28 | Executive Regulations to be issued within **six (6) months** of promulgation |
| Article 29 | Controllers/Processors to regularize within **six (6) months** of the Executive Regulations, extendable by a similar period |
| Article 31 | In force as of **02 January 2022** |

## Caveats and gaps

- **Translation, not the authoritative Arabic.** See the language section above. Any legal
  reliance should be checked against the Arabic original in the Official Gazette.
- **Article 11(1) item lettering is defective in the source.** The list runs `b., b., c., d., e.` —
  the first item is printed as "b." where "a." is evidently intended. The `item_label` column
  preserves the printed labels verbatim (two rows labelled `b`); the ids are disambiguated as
  `art_11_1_b_i` and `art_11_1_b_ii` so that ids remain unique. No text was altered.
- **Article 26 states no monetary penalty amounts.** The decree-law delegates the list of
  violations and their administrative penalties to a future Cabinet decision, so no fine
  figures exist in this instrument and none were supplied.
- **"Office" vs "Bureau".** These are the same institution — the UAE Data Office established under
  Federal Decree by Law No. (44) of 2021. The definition node uses the term as printed in
  Article 1 ("Office" → "The UAE Data Bureau…"); operative Articles use "the Bureau".
- **No Chapters/Parts** exist in the instrument, so no such node type was created.
- **Article headings** are rendered "Article (N)" throughout except Article 21, printed as
  "Article 21" without parentheses. Citations in the CSVs are normalised to the "Article (N)"
  form used by the rest of the document; article numbers themselves are plain integers.
- **Article 22** has an unnumbered chapeau followed by two numbered cases; the chapeau is stored
  as the Article's `article_text`. The same pattern applies to Articles 1, 4, 5, 7, 8 and 17.
- **Article 3** has no cross-referenceable clause structure and carries its full text at Article level.
- The preamble recital "Pursuant to what was presented by the Minister of Cabinet Affairs, and the
  approval of the Council of Ministers" is modelled as a CitedLegislation row because it sits in
  the same bulleted "Having reviewed" list in the source layout; it is a procedural recital rather
  than a cited enactment.
- Page headers ("Federal Decree by Law Concerning the Protection of Personal Data") and page
  numbers were removed, and column-wrapped lines rejoined, with wording preserved exactly.
