# Russian Federal Law No. 152-FZ on Personal Data — knowledge-graph CSVs

## Source

**Primary source (used for all extraction):**
`Russia_en_20190809_russian_personal_data_federal_law_2.txt`
(`pdftotext -layout` extract of the second PDF supplied for this instrument, alongside
`KB 2/Russia/Russian Federal Law No. 152-FZ on Personal Data.pdf`).

- **Instrument:** RUSSIAN FEDERATION FEDERAL LAW ON PERSONAL DATA, N 152-FZ, Moscow, Kremlin,
  July 27, 2006. Adopted by the State Duma July 8, 2006; approved by the Federal Council
  July 14, 2006.
- **Language / status:** this is an **English translation**, and the document labels itself
  *"Unofficial translation … provided for reference purposes only and without any warranty or
  representation regarding its accuracy or completeness."* The document does **not name the
  translator or the body that produced it**, so the producer is recorded as unknown rather than
  guessed. The Russian original is the authoritative text.
- **Amendment date reflected:** the preamble lists 19 amending federal laws, the latest being
  **Federal Law dated December 31, 2017 N 498-FZ** (Legislation Bulletin 2018, N 1, art. 82).
  The consolidated text therefore reflects the law **as amended to 31 December 2017**. (The
  filename carries the date 2019-08-09, which appears to be a retrieval date, not an
  amendment date.)

**Second source, rejected as primary:**
`Russia_Russian_Federal_Law_No_152_FZ_on_Personal_Data.txt` — a different English translation
(Garant-style, with interleaved "Information on changes" editorial notes). Its own header states
it covers amendments only "to … June 4, 2014", and it **does not contain the data-localisation
requirement** (Article 18 part 5, introduced by Federal Law N 242-FZ of July 21, 2014) — verified
by search. It is therefore materially less current and was not used. Note the two translations
render terminology differently (e.g. "operator" vs "controller", "depersonalisation" vs
"anonymization", "transborder flow" vs "cross-border transfer"); all extracted text uses the
primary translation's wording.

## Schema

The schema mirrors the statute's own hierarchy and vocabulary — Chapters, numbered Articles,
numbered *parts* (including decimal parts such as 1.1, 3.1, 22.1), and lettered/numbered *items*
inside a part (`1)`, `2.1)` …).

Node types:

| Node type | Meaning |
|---|---|
| `Law` | The statute itself: title, number, adoption/approval dates, translation status |
| `Chapter` | Chapters 1–6, with their verbatim headings |
| `Article` | Articles 1–25 including 18.1 and 22.1, with verbatim headings |
| `Part` | A numbered part of an article, verbatim. Articles with no numbered parts (Art. 2, 3, 7) get one part with an empty `part_number` carrying the article's operative/lead-in text |
| `Item` | A numbered item inside a part (`1)`, `2.1)` …), verbatim — the clause level |
| `Definition` | The 11 defined terms of Article 3, term + verbatim definition |
| `Amendment` | The 19 amending federal laws cited in the preamble, with their Legislation Bulletin references |

Relationship types:

| File | Relationship |
|---|---|
| `rels_HAS_CHAPTER.csv` | Law → Chapter |
| `rels_HAS_ARTICLE.csv` | Chapter → Article |
| `rels_HAS_PART.csv` | Article → Part |
| `rels_HAS_ITEM.csv` | Part → Item |
| `rels_DEFINES.csv` | Article 3 item → Definition |
| `rels_AMENDED_BY.csv` | Law → Amendment, plus clause → Amendment for every in-text "(ed. Federal Law dated … N …-FZ)" marker |
| `rels_CROSS_REFERENCES.csv` | Clause → Article, from explicit in-text "article N" references |

Where the themes named in the brief live:
definitions — Article 3 (`nodes_Definition.csv`); principles — Article 5 parts 1–7;
consent — Articles 6, 9 (incl. the nine mandatory contents of written consent), 10, 11, 15, 16;
cross-border transfer — Article 12; **data localisation — Article 18 part 5** (and the related
notification duty in Article 22 part 3 item 10.1); supervisory authority — Article 23
("authorized body for the protection of the rights of data subjects", i.e. the federal executive
body for personal data), plus liability in Article 24.

## Files and row counts

| File | Rows (excl. header) |
|---|---|
| `nodes_Law.csv` | 1 |
| `nodes_Chapter.csv` | 6 |
| `nodes_Article.csv` | 27 |
| `nodes_Part.csv` | 123 |
| `nodes_Item.csv` | 144 |
| `nodes_Definition.csv` | 11 |
| `nodes_Amendment.csv` | 19 |
| `rels_HAS_CHAPTER.csv` | 6 |
| `rels_HAS_ARTICLE.csv` | 27 |
| `rels_HAS_PART.csv` | 123 |
| `rels_HAS_ITEM.csv` | 144 |
| `rels_DEFINES.csv` | 11 |
| `rels_AMENDED_BY.csv` | 89 |
| `rels_CROSS_REFERENCES.csv` | 24 |

Total node ids: 331. Self-check passed: all ids unique within each node file, all 424
relationship endpoints resolve to node ids, all node files carry `source_document`.

## Caveats and gaps

- The text is a **translation of unstated authorship**; wording is verbatim to the translation,
  not to the Russian original.
- Editorial amendment markers that appear inside the statutory text — e.g. "(ed. Federal Law
  dated July 25, 2011 N 261-FZ - Legislation Bulletin …)" — are retained **inside** the clause
  text as they appear in the source, and are additionally modelled as `AMENDED_BY` edges.
- Repealed provisions are kept as nodes with the source's own repeal note as their text
  (e.g. Article 1 part 2 item 3, item 5; Article 25 part 3).
- Chapter 5's heading in the source runs across two sentences ("State control and supervision of
  the processing of personal data" / "Liability for violation of the requirements of this Federal
  Law"); both are kept in `title`, and the trailing "(name in ed. …)" note is split into
  `amendment_note`.
- Article 10 part 2 item 2.1 cites "Federal Law dated November 25, **2019** N 266-FZ" while the
  preamble and the Bulletin reference for the same law give **2009**. This is an apparent typo in
  the source; it is reproduced verbatim and the resulting `AMENDED_BY` edge was resolved by
  law number.
- Cross-reference edges are derived from explicit "article N" phrases only; references to parts,
  clauses or other federal laws are present in the clause text but are not separately modelled.
- No penalty amounts appear in this law: Article 24 refers liability out to other Russian
  legislation without stating figures, so no fine values are recorded (correctly empty).
