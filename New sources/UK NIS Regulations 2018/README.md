# UK Network and Information Systems (NIS) Regulations 2018 — knowledge-graph CSVs

**Instrument:** The Network and Information Systems Regulations 2018 (S.I. 2018 No. 506),
made 19th April 2018, laid before Parliament 20th April 2018, in force 10th May 2018.

**Source document:** `KB 2/Europe/UK Network and Information Systems (NIS) Regulations 2018.pdf`
(extracted via `pdftotext -layout`; the whole 36-page instrument was read and parsed).

All text in these CSVs is verbatim from that source. Nothing has been paraphrased, summarised
or supplied from outside the instrument. Cells are empty where the instrument says nothing.

## Schema

The schema mirrors the drafting structure of a UK statutory instrument, using the instrument's
own vocabulary (Part, regulation, paragraph, sub-paragraph, Schedule, definition, threshold
requirement, designated competent authority, penalty).

### Node types

| File | Node | What it holds |
|---|---|---|
| `nodes_Instrument.csv` | Instrument | The SI itself: title, SI number, made/laid/in-force dates, signatories. |
| `nodes_Preamble.csv` | Preamble | The three recital paragraphs preceding Part 1 (designation, EU-reference construction, enabling powers). |
| `nodes_Part.csv` | Part | Parts 1–6 with their titles. |
| `nodes_Regulation.csv` | Regulation | Regulations 1–25 with their side headings and owning Part. |
| `nodes_Provision.csv` | Provision | **Clause-level unit.** Every numbered paragraph, lettered sub-paragraph, romanised sub-sub-paragraph and `(aa)/(bb)` sub-sub-sub-paragraph, in both the regulations and Schedule 2, each with its full verbatim text, marker, depth, clause type, citation and parent. |
| `nodes_Schedule.csv` | Schedule | Schedules 1 and 2. |
| `nodes_SchedulePara.csv` | SchedulePara | The ten numbered paragraphs of Schedule 2 (one per subsector), with their headings. |
| `nodes_Definition.csv` | Definition | Every defined term with its verbatim definition, the provision that defines it and the scope of that definition (whole Regulations, one regulation, or one Schedule 2 paragraph). |
| `nodes_Sector.csv` | Sector | Column 1 of the Schedule 1 table (relevant sectors). |
| `nodes_Subsector.csv` | Subsector | Column 2 of the Schedule 1 table. |
| `nodes_CompetentAuthority.csv` | CompetentAuthority | Column 3 bodies, plus the Information Commissioner (reg 3(2)) and GCHQ as SPOC (reg 4(1)) and CSIRT (reg 5(1)). |
| `nodes_CompetentAuthorityDesignation.csv` | CompetentAuthorityDesignation | One row per sector/subsector/authority/territory cell combination in the Schedule 1 table. |
| `nodes_EssentialService.csv` | EssentialService | Each kind of essential service named in Schedule 2. |
| `nodes_ThresholdRequirement.csv` | ThresholdRequirement | The verbatim threshold requirement text for each essential service. |
| `nodes_PenaltyTier.csv` | PenaltyTier | The four maximum-penalty bands in regulation 18(6) (£1,000,000 / £3,400,000 / £8,500,000 / £17,000,000). |
| `nodes_Deadline.csv` | Deadline | Provisions that state a date or period (72 hours, 30 days, 28 days, three months, 10th August 2018, 9th May 2020, annual/biennial intervals, etc.), with the date expressions found and the clause text. |
| `nodes_ExplanatoryNote.csv` | ExplanatoryNote | The Explanatory Note paragraphs (expressly not part of the Regulations). |

### Relationship types

`HAS_PREAMBLE`, `HAS_PART`, `HAS_REGULATION`, `HAS_PROVISION`, `HAS_SUBCLAUSE`,
`HAS_SCHEDULE`, `HAS_PARAGRAPH`, `DEFINES`, `CROSS_REFERENCES`, `DESIGNATES`,
`DESIGNATES_AUTHORITY`, `HAS_DESIGNATION`, `FOR_SUBSECTOR`, `HAS_SUBSECTOR`,
`COVERS_SUBSECTOR`, `SPECIFIES_ESSENTIAL_SERVICE`, `IN_SUBSECTOR`,
`HAS_THRESHOLD_REQUIREMENT`, `SPECIFIES_THRESHOLD`, `SETS_PENALTY_TIER`,
`HAS_DEADLINE`, `HAS_EXPLANATORY_NOTE`.

Provision ids are citations: `reg11(3)(b)(i)`, `reg18(6)(d)`, `sch2p2(8)(q)(ii)(aa)`.

## Files and row counts

### Nodes (1,031 rows)

| File | Rows |
|---|---|
| nodes_CompetentAuthority.csv | 17 |
| nodes_CompetentAuthorityDesignation.csv | 23 |
| nodes_Deadline.csv | 21 |
| nodes_Definition.csv | 107 |
| nodes_EssentialService.csv | 33 |
| nodes_ExplanatoryNote.csv | 18 |
| nodes_Instrument.csv | 1 |
| nodes_Part.csv | 6 |
| nodes_PenaltyTier.csv | 4 |
| nodes_Preamble.csv | 3 |
| nodes_Provision.csv | 713 |
| nodes_Regulation.csv | 25 |
| nodes_Schedule.csv | 2 |
| nodes_SchedulePara.csv | 10 |
| nodes_Sector.csv | 5 |
| nodes_Subsector.csv | 10 |
| nodes_ThresholdRequirement.csv | 33 |

### Relationships (1,226 rows)

| File | Rows |
|---|---|
| rels_designation_for_subsector.csv | 23 |
| rels_designation_names_authority.csv | 23 |
| rels_essentialservice_has_threshold.csv | 33 |
| rels_essentialservice_in_subsector.csv | 33 |
| rels_has_preamble.csv | 3 |
| rels_instrument_has_explanatory_note.csv | 18 |
| rels_instrument_has_part.csv | 6 |
| rels_instrument_has_schedule.csv | 2 |
| rels_part_has_regulation.csv | 25 |
| rels_provision_cross_references.csv | 70 |
| rels_provision_defines_term.csv | 107 |
| rels_provision_designates.csv | 23 |
| rels_provision_designates_authority.csv | 3 |
| rels_provision_has_deadline.csv | 21 |
| rels_provision_has_subclause.csv | 506 |
| rels_provision_sets_penalty_tier.csv | 4 |
| rels_provision_specifies_threshold.csv | 33 |
| rels_regulation_has_provision.csv | 150 |
| rels_schedule_has_designation.csv | 23 |
| rels_schedule_has_para.csv | 10 |
| rels_schedulepara_covers_subsector.csv | 10 |
| rels_schedulepara_has_provision.csv | 57 |
| rels_schedulepara_specifies_service.csv | 33 |
| rels_sector_has_subsector.csv | 10 |

## Validation

A checker confirmed: every node file's first column is `<type>_id` and carries
`source_document`; all node ids are unique within their file; every relationship file starts
with `source_id,target_id,rel_type`; all 2,452 relationship endpoints resolve to an existing
node id (0 unresolved, 0 duplicates).

## Caveats and gaps

- **Footnotes are excluded.** The instrument's statutory footnotes (`(a) 1972 c.68 …` — citations
  of amending Acts and OJ references) were stripped during parsing and are not modelled as nodes.
  Footnote *markers* remain inside the clause text exactly as `pdftotext` rendered them, e.g.
  "the Communications Act 2003(f)".
- **Schedule 1 is a table**, not numbered clauses, so it is transcribed cell-by-cell into
  `nodes_CompetentAuthorityDesignation.csv` rather than into `nodes_Provision.csv`. Cells spanning
  multiple authorities/territories are split into one row per authority; the territorial
  jurisdiction column is taken from the parenthetical in the authority cell as printed.
- **Regulation 1(2)** is a run-on definition list rather than a lettered list. Its definitions are
  extracted individually into `nodes_Definition.csv`; the lettered fragments inside two of those
  definitions ("digital service", "network and information system") also appear as Provision rows
  nested under `reg1(2)`, which is an artefact of the flat layout rather than the drafting.
- **Closing "tail" text** (words after a lettered list that complete the parent paragraph, e.g. the
  final line of regulation 8(1) or 16(1)) is attached to the parent paragraph's text, so those
  paragraphs read as "…that service— that person is deemed…" with the list items held separately.
- A handful of provision ids carry a `_2` style suffix only where the same citation would otherwise
  repeat; none occur in the current output.
- Cross-references were extracted mechanically from phrases of the form "regulation N" and
  "Schedule N"; references expressed only as "paragraph (3)(c)" or to external enactments
  (Electricity Act 1989, Gas Directive, Directive 2016/1148, etc.) are preserved inside the clause
  text but are not modelled as edges.
- The Explanatory Note is included because it is printed with the instrument, but it states that it
  "is not part of the Regulations".
- No amendments made after 2018 (including EU-exit amendments) are reflected — this is the
  instrument as originally made.
