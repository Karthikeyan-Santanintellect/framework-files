# Canada — Personal Information Protection and Electronic Documents Act (PIPEDA)

Knowledge-graph CSV extraction of the consolidated statute.

**Source document:** `KB 2/Canada/Personal Information Protection and Electronic Documents Act.pdf`
S.C. 2000, c. 5 — Department of Justice consolidation, **current to March 31, 2026**, **last amended on March 4, 2025**.

## Schema

The schema mirrors the Act's own drafting vocabulary: *Part → Division → Section → Subsection →
Paragraph → Subparagraph*, plus the schedules, and Schedule 1's CSA Model Code hierarchy
(*Schedule → Principle → Clause → Paragraph*). Schedule 1 is substantive (s. 5(1) makes it binding),
so it is modelled at clause level like the enacting sections rather than as an annex blob.

### Node types

| File | Type | What it holds |
| --- | --- | --- |
| `nodes_Part.csv` | Part | The six Parts, with their titles. |
| `nodes_Division.csv` | Division | The six Divisions of Part 1 (1, 1.1, 2, 3, 4, 5). |
| `nodes_Section.csv` | Section | Every numbered section, with its bold marginal note, the running subheading it sits under, its own text where the section is not divided into subsections, and the amendment citation trailer. |
| `nodes_Subsection.csv` | Subsection | Every `(n)` / `(n.n)` subsection with its marginal note and verbatim text. |
| `nodes_Paragraph.csv` | Paragraph | Every lettered paragraph `(a)`, `(b.1)`, `(d.21)` … and every roman subparagraph `(i)`, `(ii)` …, with `level` distinguishing the two. Paragraphs that belong to a definition's list hang off the Definition node. |
| `nodes_Definition.csv` | Definition | 28 defined terms — 23 from the formal definition subsections (ss. 2(1), 7.1(1), 31(1)) with their French equivalents, plus 5 terms defined inline in operative provisions (*significant harm* 10.1(7), *employee* / *employer* 27.1(3), *filing* 35(5), *should* 5(2)). |
| `nodes_Schedule.csv` | Schedule | Schedules 1–4 with their enabling-provision references. |
| `nodes_ScheduleItem.csv` | ScheduleItem | The tabular entries of Schedules 2, 3 and 4. |
| `nodes_Principle.csv` | Principle | The ten fair information principles of Schedule 1, clauses 4.1–4.10. |
| `nodes_Clause.csv` | Clause | Schedule 1 clauses 4.x.y, plus the two interpretive Notes attached to clauses 4.3 and 4.9 (`type` = `clause` / `note`). |
| `nodes_ClauseParagraph.csv` | ClauseParagraph | Lettered items inside Schedule 1 clauses (4.1.4, 4.3.7, 4.7.3, 4.8.2). |
| `nodes_Penalty.csv` | Penalty | The two fine ceilings in s. 28 ($10,000 summary / $100,000 indictable). |
| `nodes_Deadline.csv` | Deadline | Verbatim time-limit phrases ("as soon as feasible", "within thirty days", "within one year"…) linked to the provision that states them. |
| `nodes_PendingAmendment.csv` | PendingAmendment | The nine *Amendments Not in Force* provisions (2026, c. 3, ss. 389–397), which would add Division 1.2 *Mobility of Personal Information* (ss. 10.4–10.6). |

### Relationship types

| File | `rel_type` values |
| --- | --- |
| `rels_contains.csv` | `HAS_DIVISION`, `HAS_SECTION`, `HAS_SUBSECTION`, `HAS_PARAGRAPH`, `HAS_SUBPARAGRAPH`, `HAS_PRINCIPLE`, `HAS_CLAUSE`, `HAS_ITEM` |
| `rels_defines.csv` | `DEFINES` (Section → Definition) |
| `rels_references.csv` | `REFERENCES_CLAUSE` (provision → Schedule 1 clause), `REFERENCES_DIVISION`, `REFERENCES_SCHEDULE` |
| `rels_prescribes_penalty.csv` | `PRESCRIBES_PENALTY` |
| `rels_states_deadline.csv` | `STATES_DEADLINE` |
| `rels_amends.csv` | `AMENDS` (PendingAmendment → Section) |

Coverage highlights requested by the brief: breach reporting and notification is fully modelled at
clause level (Division 1.1, ss. 10.1–10.3, incl. the 10.1(7) *significant harm* definition and the
10.1(8) real-risk factors); the Privacy Commissioner's powers are captured across ss. 11–19 and
20–25 (investigation powers 12.1(1)(a)–(f), audit powers 18(1)(a)–(f), compliance agreements
17.1–17.2, confidentiality and disclosure 20, information sharing with provinces 23 and foreign
states 23.1).

## Row counts

| File | Rows |
| --- | --- |
| `nodes_Clause.csv` | 48 |
| `nodes_ClauseParagraph.csv` | 16 |
| `nodes_Deadline.csv` | 23 |
| `nodes_Definition.csv` | 28 |
| `nodes_Division.csv` | 6 |
| `nodes_Paragraph.csv` | 270 |
| `nodes_Part.csv` | 6 |
| `nodes_Penalty.csv` | 2 |
| `nodes_PendingAmendment.csv` | 9 |
| `nodes_Principle.csv` | 10 |
| `nodes_Schedule.csv` | 4 |
| `nodes_ScheduleItem.csv` | 5 |
| `nodes_Section.csv` | 71 |
| `nodes_Subsection.csv` | 142 |
| `rels_amends.csv` | 12 |
| `rels_contains.csv` | 567 |
| `rels_defines.csv` | 28 |
| `rels_prescribes_penalty.csv` | 2 |
| `rels_references.csv` | 106 |
| `rels_states_deadline.csv` | 23 |

Validation: all node ids are unique within their file, and all 738 relationship endpoints resolve
to an existing node id.

## Caveats and notes

- The PDF is the **bilingual** Justice Canada consolidation (English left column, French right
  column). Only the English column was extracted; French appears solely as the parenthetical
  equivalent term recorded in `french_term` on `nodes_Definition.csv`, exactly as printed.
- Parts 3, 4 and 5 consist only of amendments to other Acts and are printed in the consolidation as
  `52 to 57 [Amendments]`, `58 and 59 [Amendments]`, `60 to 71 [Amendments]`. They are kept as
  Section nodes with that verbatim placeholder text; the amending text itself is not in the source.
- Sections whose whole content sits in subsections have an empty `text` cell — the obligation text
  lives on the Subsection rows, not duplicated on the Section.
- `subheading` on `nodes_Section.csv` records the italic running heading (e.g. *Filing of
  Complaints*, *Hearing by Court*) where the section sits under one; it is blank otherwise.
- `nodes_PendingAmendment.csv` is **not in force**. Its text is reproduced verbatim from the
  "Amendments Not in Force" appendix and should not be treated as operative law.
- Schedules 2, 3 and 4 are printed as multi-column tables; the column cells were rejoined into
  single strings (`column_1` / `column_2`). Schedule 3's second column has no heading in the
  source, so it is empty. Schedule 4's `column_1` gives the English organization name only (the
  entry also prints the French name *Agence mondiale antidopage*).
- Repealed provisions are retained where the consolidation prints them (e.g. 7(3)(h.2)
  `[Repealed, 2015, c. 32, s. 6]`, 13(2), 26(1)(a.01)).
- Cross-reference edges are limited to references the text states explicitly to a Schedule 1 clause,
  a Division of Part 1, or a Schedule. Numeric section-to-section references are left inside the
  verbatim text rather than materialised as edges.
- `nodes_Deadline.csv` is a derived index of verbatim time-limit phrases lifted from the provision
  text; it adds no wording of its own.
