# Philippines — Implementing Rules and Regulations of the Data Privacy Act of 2012 (RA 10173)

**Source document:** `KB 2/Philippines/IRR-of-the-DPA.pdf`
(National Privacy Commission, promulgated 24 August 2016; 14 Rules, 72 Sections.)

## IMPORTANT — this is the IRR, not the Act

These CSVs contain **only the Implementing Rules and Regulations**. The statute they
implement — **Republic Act No. 10173, the Data Privacy Act of 2012 — is NOT present in this
knowledge base**. No text of the Act has been reproduced or reconstructed here.

Wherever the IRR cites a provision of the Act (e.g. Section 57's reference to "Section 20(f)
of the Act") or any other Philippine statute, the citation is recorded as an edge to an
`ExternalReference` node rather than as content. `ExternalReference` nodes carry only the
instrument's own name and a note that the cited instrument is not in the knowledge base.
The `nodes_Instrument.csv` row carries the same warning in the `act_text_in_kb` column.

## Schema

The schema mirrors the document's own vocabulary: the IRR is organised as
**Rules (roman-numbered) → Sections (1–72) → lettered clauses → numbered sub-clauses →
parenthesised sub-sub-clauses**. Four cross-cutting node types pick out the material the
document itself enumerates (definitions, data subject rights, penalties, external citations).

### Node types
| File | Node | Rows | Notes |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | Title, issuing body, promulgation date, effectivity clause, verbatim preamble, signatories, and the "Act not in KB" caveat. |
| `nodes_Rule.csv` | Rule | 14 | RULE I–XIV with verbatim headings. |
| `nodes_Section.csv` | Section | 72 | `title` = the section's own rubric (e.g. "Data Breach Notification"); `text` = any chapeau text before the lettered clauses. |
| `nodes_Clause.csv` | Clause | 311 | Every lettered / numbered / parenthesised subdivision, verbatim, with `level` (1–3), `parent_id`, `parent_type` and a `citation` such as `Section 31(b)(2)(c)`. |
| `nodes_Definition.csv` | Definition | 20 | Section 3(a)–(t): defined term + verbatim definition. |
| `nodes_Right.csv` | Right | 7 | Section 34(a)–(f) plus Section 36 (right to data portability). |
| `nodes_Penalty.csv` | Penalty | 14 | Rule XIII offences carrying imprisonment/fines, with verbatim imprisonment range and fine minimum/maximum parsed out of the clause text. |
| `nodes_ExternalReference.csv` | ExternalReference | 13 | Instruments cited but not contained: RA 10173 itself, RA 53, RA 1405, RA 6426, RA 9510, RA 9160, RA 9372, RA 8349, EO 292 / Administrative Code of 1987, New Civil Code, Rules of Court, General Appropriations Act, Philippine Constitution. |

### Relationship types
| File | Rel | Rows | Meaning |
|---|---|---|---|
| `rels_CONTAINS.csv` | CONTAINS | 397 | Instrument→Rule, Rule→Section, Section→Clause, Clause→Clause. |
| `rels_DEFINES.csv` | DEFINES | 20 | Section 3 → Definition (carries the originating `clause_id`). |
| `rels_GRANTS_RIGHT.csv` | GRANTS_RIGHT | 7 | Section 34 / Section 36 → Right. |
| `rels_IMPOSES_PENALTY.csv` | IMPOSES_PENALTY | 14 | Section or Clause → Penalty. |
| `rels_CITES_EXTERNAL.csv` | CITES_EXTERNAL | 69 | Section/Clause → ExternalReference, with the matched citation text. |

## Verification

A self-check script asserted: unique ids within every node file, `<type>_id` as first column,
`source_id,target_id,rel_type` as first three columns of every rel file, a non-empty
`source_document` on every node row, and that all 507 relationship endpoints resolve to an
existing node id. Result: **0 errors**. A coverage check confirmed that every substantive
paragraph of the source text appears in some node's verbatim text (the only two unmatched
fragments are the PDF cover header and one rule heading whose trailing full stop is stripped).

## Caveats and notable points

- All text is verbatim from the `pdftotext -layout` extract; layout line-wraps and page
  headers/footers/page numbers were rejoined/removed, wording untouched.
- Unlabelled continuation paragraphs (e.g. the second and third paragraphs of Section 13, the
  proviso closing Section 5, the second paragraph of Section 34(b)) are appended to the text of
  the labelled provision they follow, since the document gives them no separate number.
- Section titles were split from body text at the first full stop of the section; a handful of
  sections (6, 7, 31, 38, 41, 51, 52–55, 59) consist entirely of a title plus lettered
  clauses and therefore have empty `text`.
- Key thresholds and deadlines are preserved in clause text: the 72-hour breach notification
  (Section 38(a)), the 1,000-record and 250-person registration thresholds (Sections 33, 46(a),
  47), the two-business-day off-site access decision (Section 31(b)(2)(a)), the one-year
  registration/compliance period (Section 67), the 100-person large-scale aggravating threshold
  (Section 62), and effectivity 15 days after publication in the Official Gazette (Section 72).
- Section 24 states that Section 7 of RA 9372 (Human Security Act of 2007) "is hereby amended";
  this is recorded as the IRR's own verbatim text plus a citation edge to RA 9372, which is not
  in this knowledge base.
- Minor typographical errors in the source (e.g. "the the name of the individual" in Section
  5(a)(2), "The polices" in Section 26(b)(3)) are reproduced as printed.
