# Nigeria Data Protection Act 2023 (+ NDP Act-GAID 2024) — knowledge-graph CSVs

Two instruments are modelled in this folder, as separate node families that are linked where the
directive itself states the link:

1. **Nigeria Data Protection Act, 2023** (Act No. 37) — the statute.
2. **Nigeria Data Protection Act (NDP Act) 2023 General Application and Implementation Directive
   (GAID) 2024**, ref. `NDPC/NDP ACT-GAID/001/2024` — subsidiary legislation issued by the
   Nigeria Data Protection Commission under sections 1(a), 6(c) and 62 of the Act.

## Sources — exactly which file each part came from

| Part of the extraction | Source text used |
|---|---|
| Entire Act: Parts I–XII, sections 1–66, all subsections/paragraphs/subparagraphs, section 65 definitions, the Schedule, long title, commencement, gazette details, explanatory memorandum | `Africa_Nigeria_Data_Protection_Act_2023.txt` (clean `pdftotext -layout` extract of the Gazette copy, `KB 2/Africa/Nigeria_Data_Protection_Act_2023.pdf`) — **sole authority for the Act** |
| Entire GAID: Authority, Preamble, Articles 1–53 and their sub-articles/items, Article 53 definitions, list of abbreviated terms, schedule titles, fees and administrative penalty | `Africa_Nigeria_Data_Protection_Act_NDP_ACT_2023_GAID_2024.txt` (`KB 2/Africa/Nigeria-Data-Protection-Act(NDP ACT)2023(GAID)2024.pdf`) |
| OCR of the third scanned copy (`OCR_NIGERIA.txt` / `KB 2/Africa/Nigeria_DPA.pdf`) | **Not used.** It was read and compared; it contains the same Act with OCR noise (e.g. "Power to borrow **end** accept gifts"). The Gazette text was complete, so no gap needed filling and no OCR text was taken as authoritative. |

Every clause is verbatim from the source. Layout artifacts (column wrapping, running page headers,
marginal notes) were rejoined into single-line prose; only whitespace was normalised (the Gazette's
space-before-semicolon typography is collapsed, e.g. `data ;` → `data;`). Nothing was supplied from
outside the two source texts.

## Schema

The schema mirrors the documents' own vocabulary. The Act calls its divisions *Parts*, *sections*,
*subsections*, *paragraphs* and *subparagraphs*; the directive calls its divisions *Articles*,
*Sub-Articles* and lettered items. They are therefore modelled as two parallel hierarchies rather
than forced into one generic "clause" type, so a query can distinguish a statutory obligation from
a regulator's implementation directive.

**Act nodes:** `Act` → `Part` → `Section` → `Subsection` → `Paragraph` → `Subparagraph`; plus
`Definition` (s.65), `Schedule` + `ScheduleParagraph` (the Schedule under s.8(3)).
Sections whose lettered items hang directly off the section (5, 6, 15, 16, 33, 57, 62) attach
`Paragraph` nodes straight to the `Section`; `parent_type` records which.

**Directive nodes:** `Directive` → `Article` → `SubArticle` → `ArticleItem` → `ArticleSubItem`;
plus `Preamble` (the six recitals), `DirectiveDefinition` (Article 53), `DirectiveSchedule`
(Schedules 1–4), `AbbreviatedTerm` (the list of abbreviated terms).

**Shared analytic nodes:** `Penalty` (fines, imprisonment, the higher/standard maximum amounts, and
the GAID's fees and administrative penalty) and `Deadline` (every stated time limit, in both
instruments), each linked back to the provision that states it.

**Relationship types:** `HAS_PART`, `HAS_SECTION`, `HAS_SUBSECTION`, `HAS_PARAGRAPH`,
`HAS_SUBPARAGRAPH`, `DEFINES`, `HAS_SCHEDULE`, `APPLIES_SCHEDULE`, `HAS_SCHEDULE_PARAGRAPH`,
`PRESCRIBED_BY`, `STATED_IN`, `CROSS_REFERENCES`, `HAS_PREAMBLE_RECITAL`, `HAS_ARTICLE`,
`HAS_SUB_ARTICLE`, `HAS_ITEM`, `HAS_SUB_ITEM`, `USES_ABBREVIATION`, `IMPLEMENTS`,
`REFERS_TO_SCHEDULE`.

`rels_directive_implements.csv` is the bridge between the two instruments. It contains **only**
links the directive itself asserts (e.g. Article 11(1) "Section 32 of the NDP Act mandates the
designation of a DPO", Article 34(1) quoting section 40(2)); the `quoted_text` column carries the
directive's own words that establish the link. No inferred or thematic links were added.

## Files

### Node files
| File | Rows |
|---|---|
| nodes_Act.csv | 1 |
| nodes_Part.csv | 12 |
| nodes_Section.csv | 66 |
| nodes_Subsection.csv | 161 |
| nodes_Paragraph.csv | 300 |
| nodes_Subparagraph.csv | 44 |
| nodes_Definition.csv | 24 |
| nodes_Schedule.csv | 1 |
| nodes_ScheduleParagraph.csv | 18 |
| nodes_Penalty.csv | 9 |
| nodes_Deadline.csv | 25 |
| nodes_Directive.csv | 1 |
| nodes_Preamble.csv | 6 |
| nodes_Article.csv | 53 |
| nodes_SubArticle.csv | 250 |
| nodes_ArticleItem.csv | 334 |
| nodes_ArticleSubItem.csv | 50 |
| nodes_DirectiveDefinition.csv | 18 |
| nodes_DirectiveSchedule.csv | 4 |
| nodes_AbbreviatedTerm.csv | 28 |
| **Total nodes** | **1,405** |

### Relationship files
| File | Rows |
|---|---|
| rels_has_part.csv | 12 |
| rels_has_section.csv | 66 |
| rels_has_subsection.csv | 161 |
| rels_has_paragraph.csv | 300 |
| rels_has_subparagraph.csv | 44 |
| rels_defines.csv | 24 |
| rels_has_schedule.csv | 2 |
| rels_schedule_has_paragraph.csv | 18 |
| rels_penalty_prescribed_by.csv | 9 |
| rels_deadline_stated_in.csv | 25 |
| rels_cross_reference.csv | 61 |
| rels_directive_has_preamble.csv | 6 |
| rels_directive_has_article.csv | 53 |
| rels_article_has_subarticle.csv | 250 |
| rels_article_has_item.csv | 334 |
| rels_item_has_subitem.csv | 50 |
| rels_directive_defines.csv | 18 |
| rels_directive_has_schedule.csv | 4 |
| rels_directive_uses_abbreviation.csv | 28 |
| rels_directive_implements.csv | 53 |
| **Total relationships** | **1,518** |

Id conventions: Act clauses use `S<section>[-<subsection>][-<paragraph>][-<subparagraph>]`
(e.g. `S48-2-d` = section 48(2)(d)); directive clauses use `A<article>[-…]`
(e.g. `A29-3-k` = Article 29(3)(k)). Parts are `P1`–`P12`.

## Caveats and gaps

- **The GAID's Schedules 1–4 are titles only.** The source PDF text ends at Article 53; the four
  schedules named in its table of contents (Principles of Data Processing; DPO Assessment Metrics;
  Cross-Border Data Transfer; Guidance Notice on Data Controllers and Data Processors of Major
  Importance, ref. NDPC/HQ/GN/VOL.02/24) are not reproduced in the extract. They are modelled as
  `DirectiveSchedule` nodes with `text_present_in_source = no`, so the Articles that point to them
  (15(2), 8(5), 9(1), 46(2)) still resolve.
- **Defects reproduced as printed, not corrected.** Section 13(2)(a)/(b) penalise contravention of
  "paragraphs (b) and (e)" but then describe contraventions of paragraphs (b) and (d); section
  13(1)(d) refers to a "subsection (3)" that section 13 does not contain; section 19 is headed
  "Funds of the Commission" in the arrangement of sections but "Fund of the Commission" in the
  body margin (the arrangement-of-sections wording is used); section 19(4) reads "under to this
  Act" and duplicates the borrowing power restated in section 21(1); section
  43(1) contains a stray character before "42" in the Gazette (`ż42`), removed as a print artifact.
  GAID Article 14(5) is an incomplete sentence in the source ("verification scores or decline
  verification where the evidence wholly lacks credibility.") and is stored as printed.
- **No Section 55/59/60/63/66-style plain sections were split** — sections with no numbered
  subdivisions carry their whole text in the `text` column of `nodes_Section.csv`.
- `Penalty` rows PEN-06..PEN-09 are the GAID's fees and administrative penalty, not statutory
  offences; the `type` column distinguishes them.
- No instance data of any kind (organisations, incidents, people) appears in these files.

## Self-check

`build.py` (kept outside this folder) parses every CSV it writes and asserts: (a) all node ids are
unique within their file *and* globally across all node files; (b) every `source_id`/`target_id` in
every relationship file resolves to an existing node id. Result: **0 duplicate ids, 0 unresolved
endpoints**, 40 CSV files, 2,923 data rows (1,405 nodes + 1,518 relationships).
