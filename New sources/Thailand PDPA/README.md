# Personal Data Protection Act, B.E. 2562 (2019) — Thailand — knowledge-graph CSVs

## Source

- **Instrument:** Personal Data Protection Act, B.E. 2562 (2019), Kingdom of Thailand
- **Source document:** `KB 2/Thailand/Personal Data Protection Act.pdf`
- **Publication:** Government Gazette, No. 136 Chapter 69 Gor, 27 May 2019
- **Language:** The source text is an **unofficial English translation** of the Thai statute.
  The PDF is an English-language rendering of the Government Gazette publication; the
  authoritative text of the Act is the Thai original. All text in these CSVs is reproduced
  verbatim from that English translation, including its typographical and grammatical
  irregularities (e.g. "does not deceptive or misleading", "may be may be undertaken",
  the truncated Section 1, and "In the absent of a decision").

## Schema and rationale

The Act is a Thai statute organised as **Chapters → (Parts) → Sections → paragraphs and
numbered/lettered items**. The schema mirrors that structure using the document's own
vocabulary, plus four thematic node types for the substantive content the Act itself
enumerates (defined terms, lawful bases, data subject rights, penalties).

### Node types

| File | Node type | Rows | Notes |
|---|---|---|---|
| `nodes_Chapter.csv` | Chapter | 9 | Chapters I–VII, plus the un-numbered "Preliminary Provisions" (Sections 1–7) and "Transitional Provisions" (Sections 91–96) groupings. The two un-numbered groups carry an empty `chapter_label`; the Transitional Provisions heading is verbatim, "Preliminary Provisions" is a structural label for the pre-Chapter I sections. |
| `nodes_Part.csv` | Part | 5 | Part 1–3 of Chapter II; Part I (Criminal Liability) and Part II (Administrative Liability) of Chapter VII. |
| `nodes_Section.csv` | Section | 96 | Sections 1–96, complete. |
| `nodes_Clause.csv` | Clause | 414 | Every paragraph, numbered item and lettered sub-item, with verbatim `text`. `clause_type` is `paragraph`, `item` or `sub-item`. |
| `nodes_Definition.csv` | Definition | 10 | The nine terms defined in Section 6, plus the definition of "biometric data" given in Section 26 paragraph two. |
| `nodes_LawfulBasis.csv` | LawfulBasis | 13 | Consent (s.19), the six exemptions in s.24, explicit consent and the five exemptions in s.26. |
| `nodes_DataSubjectRight.csv` | DataSubjectRight | 8 | The rights the Act itself cross-lists in Section 23(6): withdrawal of consent (s.19 ¶5), access (s.30), portability (s.31), objection (s.32), erasure (s.33), restriction (s.34), accuracy (s.36), complaint (s.73). |
| `nodes_Penalty.csv` | Penalty | 14 | Criminal (s.79–81), administrative (s.82–89) and civil (s.77–78) liability, with verbatim sanction text and the stated imprisonment / fine ceilings. |

### Relationship types

| File | Rel type(s) | Rows |
|---|---|---|
| `rels_CONTAINS.csv` | `HAS_PART` (Chapter→Part), `HAS_SECTION` (Chapter or Part→Section) | 101 |
| `rels_HAS_CLAUSE.csv` | `HAS_CLAUSE` (Section→Clause), `HAS_SUBCLAUSE` (Clause→Clause) | 414 |
| `rels_DEFINES.csv` | `DEFINES` (Section→Definition) | 10 |
| `rels_PROVIDES_BASIS.csv` | `PROVIDES_BASIS` (Clause→LawfulBasis) | 13 |
| `rels_GRANTS_RIGHT.csv` | `GRANTS_RIGHT` (Clause→DataSubjectRight) | 8 |
| `rels_IMPOSES_PENALTY.csv` | `IMPOSES_PENALTY` (Section→Penalty) | 14 |
| `rels_REFERENCES.csv` | `REFERENCES` (Clause→Section), with `citation` column | 131 |

## Deadlines, thresholds and figures captured

Captured verbatim inside clause text and, where applicable, in `nodes_Penalty.csv`:
72 hours (breach notification, s.37(4)); thirty days (s.25(1), s.25 ¶3, s.30 ¶4); ninety
days (s.13 ¶2, s.52 ¶2, s.91, s.92); 60 days (s.51 ¶2, s.52 ¶2); one year (commencement,
s.2; s.93; s.96); 120 / 180 days (s.69, s.70, s.94 ¶4); age of ten years (s.20(2));
four-year terms and two-term limits (s.12, s.51, s.60); punitive damages up to 2× actual
compensation and 3-/10-year prescription (s.78); administrative fines of 500,000 /
1,000,000 / 3,000,000 / 5,000,000 Baht; criminal penalties of up to six months or one
year imprisonment.

## Caveats and gaps

- **Section 1 is truncated in the source.** The PDF reads: `This Act is called the
  "Personal Data Protection Act, B.E. 2562` — the closing quotation and the trailing
  words are absent from the extract. Reproduced as-is; nothing supplied.
- **Preamble, royal recital, countersignature and the closing "Remarks" note** were not
  modelled as nodes: they are not Sections and carry no clause-level obligations. The
  Section 26/32/33/37 references in the preamble are to the **Constitution of the Kingdom
  of Thailand**, not to this Act, and are deliberately excluded from `rels_REFERENCES.csv`.
- **`rels_REFERENCES.csv`** is derived by matching "Section NN" strings in clause text
  against this Act's own section numbers. References to Sections 22, 23, 24 and 27 of the
  **Civil and Commercial Code** (Section 20) are excluded. Self-references within the same
  Section are excluded. Sub-clause targeting (e.g. "Section 24(3)") is recorded at Section
  granularity, with the literal citation preserved in the `citation` column.
- **Chapter boundaries** were inferred from heading placement in the source: Chapter II
  covers Sections 19–29 and Chapter III covers Sections 30–42. Note that Sections 35–42
  (Data Controller / Data Processor / DPO duties) sit physically under the Chapter III
  heading "Rights of the Data subject" in the source text with no intervening heading; this
  grouping reflects the document as printed, not a re-classification.
- **`nodes_DataSubjectRight.csv` and `nodes_LawfulBasis.csv`** are index nodes over clauses
  already present in `nodes_Clause.csv`; their `*_name` values are short descriptors built
  from the wording of the cited clause. The binding verbatim text is on the Clause node.
- No paragraph numbering is printed in the source for most paragraphs; paragraph labels
  ("paragraph one", "paragraph two", …) follow the Act's own citation convention, which the
  Act uses throughout (e.g. "Section 30 paragraph four").
- No OCR noise correction was performed beyond rejoining layout-wrapped lines and letter-
  spaced words (e.g. "gr ant ing" → "granting") into single-line prose.
