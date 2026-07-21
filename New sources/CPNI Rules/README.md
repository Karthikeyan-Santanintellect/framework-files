# Customer Proprietary Network Information (CPNI) — FCC 01-247

Knowledge-graph CSV extraction of the source document.

## What this source actually is (important)

**Source document:** `KB 2/USA/Customer Proprietary Network Information Rules.pdf`
(text extract: `USA_Customer_Proprietary_Network_Information_Rules.txt`, `pdftotext -layout`).

Despite the file name, this document is **not** the codified CPNI rules at
47 C.F.R. §§ 64.2001–64.2011. It is:

> Federal Communications Commission, **FCC 01-247**, *Clarification Order and Second Further
> Notice of Proposed Rulemaking*, CC Docket No. 96-115 and CC Docket No. 96-149,
> adopted August 28, 2001, released September 7, 2001.

The order (a) explains the effect of the Tenth Circuit's decision in *U S WEST, Inc. v. FCC*,
182 F.3d 1224 (10th Cir. 1999) on the Commission's existing CPNI rules, concluding that the
vacatur reached only 47 C.F.R. § 64.2007(c); (b) gives interim guidance on obtaining customer
consent (opt-out or opt-in) pending resolution of the docket; and (c) seeks comment on the form
of approval under Section 222(c)(1).

**It contains no regulatory rule text.** The order refers to and cites rule sections
(§§ 64.2005, 64.2007(c), 64.2007(f), etc.) but never reproduces them, and its only appendix
(Appendix A) is an Initial Regulatory Flexibility Analysis, not appended amended rule text.
Consequently there are **no `nodes_Rule*.csv` files** in this extraction — inventing rule text
would violate the verbatim requirement. The obligations that appear here are the order's own
statements (interim guidance, ordering clauses, filing requirements), not codified rules.

## Schema

Modelled on the document's own structure and vocabulary (Roman-numeral Parts → lettered/numbered
Sections → numbered paragraphs), with the ordering clauses, the appendix, the separate statement
and the footnote apparatus kept as distinct types.

| Node type | Meaning |
|---|---|
| `Instrument` | The order itself: caption, docket numbers, adoption/release dates, scope note |
| `Part` | Roman-numeral parts (I INTRODUCTION … XI ORDERING CLAUSES) |
| `Section` | Lettered (A/B/C) and numbered (1–4) subheadings within a Part |
| `Paragraph` | Numbered paragraphs 1–35, verbatim, clause level of this instrument |
| `OrderingClause` | Numbered paragraphs 36–37 under Part XI ORDERING CLAUSES |
| `Appendix` | APPENDIX A – INITIAL REGULATORY FLEXIBILITY ANALYSIS (`contains_rule_text = no`) |
| `AppendixSection` | Appendix A sections A–F |
| `AppendixParagraph` | Appendix A numbered paragraphs 1–31, verbatim |
| `SeparateStatement` | Separate statement of Commissioners Tristani and Copps |
| `StatementParagraph` | Paragraphs of that statement, verbatim |
| `Footnote` | Every footnote (order 1–70, appendix 1–37, statement 1–12), verbatim |
| `ExternalReference` | Statutes, C.F.R. provisions, court decisions and prior FCC orders cited by the document — referenced, never reproduced beyond text the document itself quotes |
| `DefinedTerm` | Terms the document itself defines or explains, with the verbatim defining sentence(s) |
| `Deadline` | Comment/reply dates, the 30-day opt-out safe harbor, OMB and effective dates |

| Relationship file | Rel types |
|---|---|
| `rels_contains.csv` | `HAS_PART`, `HAS_SECTION`, `HAS_PARAGRAPH`, `HAS_ORDERING_CLAUSE`, `HAS_APPENDIX`, `HAS_SEPARATE_STATEMENT` |
| `rels_cites.csv` | `CITES` (paragraph/appendix/statement text → external reference) |
| `rels_has_footnote.csv` | `HAS_FOOTNOTE` (text unit → footnote, from the footnote markers stripped out of that unit) |
| `rels_defines.csv` | `DEFINES` |
| `rels_sets_deadline.csv` | `SETS_DEADLINE` |
| `rels_instrument_relations.csv` | `IMPLEMENTS`, `CLARIFIES`, `RESPONDS_TO`, `ADOPTED_PURSUANT_TO`, `VACATES` |

## Files and row counts

| File | Rows |
|---|---|
| nodes_Instrument.csv | 1 |
| nodes_Part.csv | 6 |
| nodes_Section.csv | 8 |
| nodes_Paragraph.csv | 35 |
| nodes_OrderingClause.csv | 2 |
| nodes_Appendix.csv | 1 |
| nodes_AppendixSection.csv | 6 |
| nodes_AppendixParagraph.csv | 31 |
| nodes_SeparateStatement.csv | 1 |
| nodes_StatementParagraph.csv | 6 |
| nodes_Footnote.csv | 119 |
| nodes_ExternalReference.csv | 41 |
| nodes_DefinedTerm.csv | 15 |
| nodes_Deadline.csv | 7 |
| **Total nodes** | **279** |
| rels_contains.csv | 96 |
| rels_cites.csv | 99 |
| rels_has_footnote.csv | 78 |
| rels_defines.csv | 15 |
| rels_sets_deadline.csv | 7 |
| rels_instrument_relations.csv | 10 |
| **Total relationships** | **305** |

Self-check (id uniqueness across all node files, resolution of every `source_id`/`target_id`
and of every embedded foreign key such as `part_id`, `section_id`, `defined_in`, `stated_in`,
plus header conformance): **0 errors**.

## Caveats and notes

- **No rule text.** As explained above, the codified CPNI rules are cited but not reproduced.
  Anyone needing 47 C.F.R. §§ 64.2001–64.2011 must extract them from the C.F.R., not this file.
- **Superseded content.** The order's interim guidance was later replaced by the Commission's
  2002 CPNI order and subsequent rulemakings. Nothing about later developments is recorded here —
  only what this document states.
- **Footnotes are separated from body text.** Footnote bodies live in `nodes_Footnote.csv`;
  in-line superscript reference numbers were removed from paragraph text (the layout extract glues
  them to the preceding word, e.g. `opinion1`) and preserved in the `footnote_refs` column and in
  `rels_has_footnote.csv`. Attribution is by footnote number within the document scope
  (`order` / `appendix_a` / `separate_statement`), which restart their numbering.
- **Layout repair.** Running headers, page numbers, and column-wrapped lines were rejoined.
  pdftotext placed superscript ordinals on their own lines; `10 Circuit` and `445 12 Street` were
  restored to `10th Circuit` and `445 12th Street`. Wording is otherwise untouched.
- **Verbatim artifacts preserved.** Appendix A para. 9 begins `.Although` and Appendix A para. 4
  cites "Section 64.7002 of our rules, 47 C.F.R. § 64.7002" (an apparent typo for 64.2007 in the
  original); both are left exactly as printed.
- **Part numbering.** The document jumps from Part V (PROCEDURAL MATTERS) to Part XI (ORDERING
  CLAUSES); Parts VI–X do not exist in the source. The `numeral` field records what is printed.
- **`CITES` edges** are derived from mention phrases occurring in the verbatim body text
  (e.g. "Section 64.2007(f)", "Tenth Circuit", "CPNI Order"). They are indicative reading aids;
  the authoritative citation strings sit on `ExternalReference.citation`, taken verbatim from the
  document's own footnotes.
- **No penalties** are stated anywhere in this document, so no penalty nodes exist.
