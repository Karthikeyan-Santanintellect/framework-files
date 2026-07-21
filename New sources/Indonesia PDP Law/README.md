# Indonesia — Personal Data Protection Law (UU No. 27 of 2022)

Knowledge-graph CSV extraction of **Law of the Republic of Indonesia Number 27 of 2022 on Personal
Data Protection** ("UU PDP").

## Source

- **Source PDF:** `KB 2/Indonesia/Personal Data Protection Law.pdf` (text extract produced with
  `pdftotext -layout`; 37 pages, header dated "Update: Oct 18, 2022").
- **Status: this is the ENACTED LAW, not a draft.** The text carries the enacting formula
  ("HAS DECIDED: To enact: A LAW ON PERSONAL DATA PROTECTION"), the signature blocks of President
  Joko Widodo and Minister of State Secretary Pratikno, "Ratified in Jakarta On October 17, 2022",
  "Promulgated in Jakarta On October 17, 2022", and the gazette citation *State Gazette of the
  Republic of Indonesia Number 196 of 2022 / Supplement Number 6820*.
- **Language: this is an ENGLISH TRANSLATION.** The PDF is a two-column bilingual document with the
  Indonesian original (Bahasa Indonesia) on the left and the English translation on the right.
  The translation is credited to **Wishnu Basuki (wbasuki@abnrlaw.com)** and carries the note:
  *"This translation uses the EU General Data Personal Regulation (GDPR) 2016/679, 27 Apr 2016, as
  the main reference."* It is an unofficial translation, not an official government text.
  **All text captured in these CSVs is the verbatim English column.**

## Schema and rationale

The document is a civil-law statute organised as *Bab* (Chapter) → *Bagian* (Part, only inside
Chapters VI and VII) → *Pasal* (Article) → *ayat* (numbered paragraph) → *huruf* (lettered point) →
*angka* (number). The node types below use that vocabulary. A distinctive feature of this document
is that the **Elucidation (Penjelasan)** is interleaved: explanatory paragraphs sit directly beneath
the clause they explain ("NOTE: WHERE NO ELUCIDATION IS PROVIDED UNDERNEATH A CLAUSE, THE CLAUSE IS
SUFFICIENTLY CLEAR"). Those elucidation passages are almost all of the form *"X means …"*, so they
are modelled as `Definition` nodes attached to the clause they elucidate, rather than as a separate
structural tier. Rights, obligations, prohibitions, principles and sanctions are given their own
node types because the statute itself organises whole chapters around them and cross-refers to them
by article number (Art. 15, 50, 52, 57, 67–68).

### Node files

| File | Rows | Description |
|---|---|---|
| `nodes_Law.csv` | 1 | The instrument itself: citation, number/year, ratification and promulgation dates, gazette numbers. |
| `nodes_Chapter.csv` | 16 | Chapters I–XVI with title and article range (from the document's own Table of Contents). |
| `nodes_Part.csv` | 6 | *Bagian* — Parts One–Four of Chapter VI, Parts One–Two of Chapter VII. |
| `nodes_Article.csv` | 76 | Articles 1–76. `text` holds the full verbatim body for articles that are not subdivided (and the chapeau where the article opens with one). |
| `nodes_Clause.csv` | 280 | Every numbered paragraph `(n)`, lettered point `a.`, and number `1.` that carries text — e.g. `art_2_1_b_2`, `art_57_2_d`. `level` = paragraph / letter / number / note. |
| `nodes_Definition.csv` | 49 | 11 Article 1 statutory definitions + 38 definitions stated in the interleaved Elucidation. `definition_source` distinguishes the two. |
| `nodes_Principle.csv` | 8 | The eight key principles of Article 3 (protection, legal certainty, public interest, benefit, prudence, balance, accountability, confidentiality). |
| `nodes_Right.csv` | 10 | Data subject rights, Articles 5–13 (Article 13 yields two: portability format and transmission). |
| `nodes_Obligation.csv` | 42 | Controller / processor / DPO-appointment obligations expressed as "must …", Articles 20–56 plus the Article 74 transitional duty. `bearer` names the duty-holder. |
| `nodes_Sanction.csv` | 20 | 4 administrative sanctions (Art. 57(2)), criminal penalties (Arts. 67–68), additional sentence (Art. 69), corporate penalties (Art. 70), substitute corporate penalty (Art. 72). `imprisonment_max` / `fine_max` carry the stated ceilings verbatim. |
| `nodes_Prohibition.csv` | 4 | The Chapter XIII prohibitions, Articles 65(1)–(3) and 66. |

### Relationship files

| File | Rows | Meaning |
|---|---|---|
| `rels_has_chapter.csv` | 16 | Law → Chapter |
| `rels_has_part.csv` | 6 | Chapter → Part |
| `rels_has_article.csv` | 76 | Chapter or Part → Article |
| `rels_has_clause.csv` | 280 | Article → Clause, Clause → sub-Clause (`HAS_CLAUSE` / `HAS_SUBCLAUSE`) |
| `rels_defines.csv` | 49 | Clause or Article → Definition |
| `rels_states_principle.csv` | 8 | Article 3 → Principle |
| `rels_grants_right.csv` | 10 | Article → Right |
| `rels_imposes_obligation.csv` | 42 | Article → Obligation |
| `rels_prohibits.csv` | 4 | Article → Prohibition |
| `rels_prescribes_sanction.csv` | 20 | Article → Sanction |
| `rels_penalized_by.csv` | 4 | Prohibition → criminal Sanction (Art. 65(1)→67(1), 65(2)→67(2), 65(3)→67(3), 66→68) |
| `rels_sanctionable_breach.csv` | 33 | Article 57(1) → each Article whose breach it makes administratively sanctionable |
| `rels_exempts.csv` | 13 | Article 15(1) → the rights it exempts; Article 50(1) → the controller obligations it exempts |
| `rels_cross_references.csv` | 28 | Explicit article-to-article references stated in the text (e.g. Art. 52 → Arts. 29, 31, 35–39) |
| `rels_delegates_to.csv` | 11 | Clause → Law, with `instrument` = the implementing instrument named ("Regulation of the Government" ×10, "Regulation of the President" ×1) |

## Notable content captured

- **Deadlines:** 3 x 24 hours (rectification Art. 30(1), access Art. 32(2), cessation on consent
  withdrawal Art. 40(2), postponement/restriction Art. 41(1), breach notification Art. 46(1));
  1 month to pay a fine, extendable by 1 month (Art. 71(1)–(2)); 2 years transition (Art. 74);
  suspension of corporate business up to 5 years (Art. 72(1)).
- **Thresholds:** administrative fine ≤ 2% of annual income/revenue (Art. 57(3)); criminal fines
  Rp4bn / Rp5bn / Rp6bn with 4–6 years imprisonment (Arts. 67–68); corporate fine ≤ 10× the maximum
  (Art. 70(3)).

## Caveats and gaps

- **Translation, unofficial.** Only the English column was extracted; the Indonesian original is in
  the PDF but is not represented in these CSVs. Where the English is defective the source wording is
  preserved verbatim rather than corrected. Known defects reproduced as-is:
  - Article 4(1)(b) reads "Special category Personal Data" in English where the Indonesian reads
    *Data Pribadi yang bersifat umum* (general category) — an evident translation error, kept verbatim.
  - Article 19 letters are printed "a., b., d." in the English column (no "c."), kept verbatim.
  - Article 60 letter "e" is printed without a full stop; Art. 41(2)(a) has a stray space before the
    semicolon; Art. 39(3) reads "must be comply". All kept verbatim.
- **Preamble / General Elucidation not modelled as nodes.** The *Considering* recitals (a–d), the
  *By virtue of* constitutional citations, and the multi-paragraph GENERAL ELUCIDATION are prose
  context rather than clause-level obligations, and were left out of the CSVs. The enacting and
  promulgation details are captured on `nodes_Law.csv`.
- **The regulator is unnamed in the statute.** The Law refers only to "the institution" (*lembaga*),
  to be established by the President (Art. 58(3)); no name is stated, so none is supplied. For the
  same reason no `Institution` node type was created — its powers live as Article 59/60 clauses.
- **Clause-level ids are stable and derived from the citation**, e.g. `art_57_2_d` = Article 57(2)(d).
- **Self-check:** all 512 node ids are unique within their files and all 600 relationship endpoints
  resolve to an existing node id.
