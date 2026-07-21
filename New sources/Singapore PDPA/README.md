# Personal Data Protection Act 2012 (Singapore) — knowledge-graph CSVs

**Source document:** Personal Data Protection Act 2012, 2020 Revised Edition, Statutes of the
Republic of Singapore — `KB 2/Singapore/Personal Data Protection Act (PDPA).pdf`
(informal consolidation, version in force from 5/12/2025; revised edition incorporating all
amendments up to and including 1 December 2021, in operation from 31 December 2021).

Extraction was performed from a `pdftotext -layout` render of the full 124-page PDF. All text in
these CSVs is verbatim from that source; layout wrapping, running headers/footers, page numbers
and marginal amendment markers (e.g. `[40/2020]`) were removed and prose rejoined into single
lines. No cell contains content that is not in the Act.

## Schema

The schema mirrors the Act's own structure and vocabulary: an Act divided into **Parts**, some of
which are divided into **Divisions**, containing numbered **Sections**, each subdivided into
**Clauses** (the Act's subsections, paragraphs, sub-paragraphs and items). **Schedules** carry
their own **Parts**, **Divisions** and numbered **Paragraphs**, which are themselves subdivided
into clauses. Defined terms, penalties, stated time periods and the legislative history are
modelled separately because the Act treats them as free-standing content.

### Node files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Act.csv` | 1 | The Act: citation, edition, long title, commencement dates. |
| `nodes_Part.csv` | 15 | Parts 1–10 including 6A, 9A, 9B, 9C, 9D (and repealed Parts 7, 8). |
| `nodes_Division.csv` | 5 | Divisions within Part 4 (Consent, Purpose) and Part 9 (Preliminary, Administration, Specified message to Singapore telephone number). |
| `nodes_Section.csv` | 95 | Sections 1–68 including 15A, 22A, 26A–26E, 43A, 48A–48R, 52A; `heading`, `lead_text`, `status`, `repealed_by`. |
| `nodes_Clause.csv` | 1035 | Every numbered/lettered subdivision that carries text, verbatim, with `clause_type` (subsection / paragraph / subparagraph / item), `parent_id` and full `number` (e.g. `48J(3)(a)`). |
| `nodes_Definition.csv` | 108 | Every defined term with its verbatim definition, and the provision that defines it (s 2, 10(5), 26A, 36, 48, 48A–48F, 52, 52A, 59(7), 67(9), and Schedule definitions). |
| `nodes_Schedule.csv` | 11 | First to Eleventh Schedules, with the enabling provision and status (Third and Fourth are repealed). |
| `nodes_SchedulePart.csv` | 8 | Parts of the First and Second Schedules. |
| `nodes_ScheduleDivision.csv` | 5 | Divisions within Parts 2 and 3 of the Second Schedule. |
| `nodes_ScheduleParagraph.csv` | 63 | Numbered paragraphs of the Schedules, with headings where the Act supplies them. |
| `nodes_Penalty.csv` | 23 | Every stated penalty: maximum fine, maximum imprisonment, financial-penalty cap, turnover threshold, continuing-offence fine, plus the verbatim provision text. |
| `nodes_Deadline.csv` | 14 | Time periods the Act states expressly (e.g. "no later than 3 calendar days", "at least 14 days", "not earlier than 28 days"). |
| `nodes_Amendment.csv` | 9 | The Legislative History table (Acts 26/2012, 29/2014, 22/2016, 40/2019, 40/2020, 25/2021, 19/2025, G.N. S 19/2015, 2020 Revised Edition). |

### Relationship files

| File | Rows | Meaning |
|---|---:|---|
| `rels_HAS_PART.csv` | 15 | Act → Part |
| `rels_HAS_DIVISION.csv` | 5 | Part → Division |
| `rels_HAS_SECTION.csv` | 95 | Part/Division → Section |
| `rels_HAS_CLAUSE.csv` | 1035 | Section/Clause/ScheduleParagraph → Clause (recursive) |
| `rels_DEFINES.csv` | 108 | Defining provision → Definition |
| `rels_HAS_SCHEDULE.csv` | 11 | Act → Schedule |
| `rels_SCHEDULE_HAS_PART.csv` | 8 | Schedule → SchedulePart |
| `rels_SCHEDULE_HAS_DIVISION.csv` | 5 | SchedulePart → ScheduleDivision |
| `rels_HAS_PARAGRAPH.csv` | 63 | Schedule/SchedulePart/ScheduleDivision → ScheduleParagraph |
| `rels_IMPOSES_PENALTY.csv` | 23 | Provision → Penalty |
| `rels_HAS_DEADLINE.csv` | 14 | Provision → Deadline |
| `rels_REFERENCES.csv` | 206 | Provision → Section / Part / Schedule it cites |
| `rels_AMENDS.csv` | 9 | Amendment → Act |

## Caveats and gaps

- **Part 6B (data portability) is not in the source text.** Sections 26F–26J were never brought
  into force and do not appear in this consolidation, although other provisions still cross-refer
  to Part 6B and to sections 26H and 51(1)(c). Those dangling references are preserved verbatim in
  the clause text but produce no `rels_REFERENCES` row, because no such node exists.
- The First Schedule's enabling note cites a **Twelfth Schedule**, which likewise does not exist in
  this consolidation. It is preserved verbatim in `nodes_Schedule.authority` but is not linked.
- **Parts 7 and 8 (sections 27–35) and the Third and Fourth Schedules are repealed** by Act 40 of
  2020. They are retained as nodes with `status = repealed` and no clause text, exactly as the
  source presents them.
- Marginal amendment annotations (`[40/2020]`, `[22/2016]`, `[Act 40 of 2020 wef 01/10/2022]`) were
  treated as page furniture and dropped; provision-level amendment provenance is therefore not
  captured beyond the `nodes_Amendment.csv` legislative history.
- Where a provision ends with closing words after its lettered paragraphs (e.g. s 26E, s 42(4)),
  those words are attached to the parent block (the section `lead_text` or the parent clause), so
  the parent reads as opening text + closing text with the paragraphs held as child rows.
- Three places in the layout render a wrapped closing line beginning with a bracketed token that
  duplicates an existing label (s 17(2), s 48M(4), Ninth Schedule para 3(12)). These were re-joined
  to the block they belong to rather than emitted as duplicate clauses.
- `nodes_Penalty.csv` and `nodes_Deadline.csv` are indexes over verbatim provision text: the amount
  and period strings are copied from the Act, and each row carries the full provision text it was
  taken from. Amounts the Act leaves to be prescribed by regulation are, correspondingly, absent.
- Repealed section 51(1)(c) and s 48H(1)(c), (e) refer to data porting requests under s 26H; the
  clause text is captured but the referenced section does not exist here (see first caveat).

## Validation

All CSVs are UTF-8 with a header row, minimal quoting, and no embedded newlines. A validation pass
confirms that every node id is unique within its file, every node file's first column is
`<type>_id`, every relationship file begins with `source_id,target_id,rel_type`, and every
relationship endpoint resolves to an existing node id. Result: all checks passed.
