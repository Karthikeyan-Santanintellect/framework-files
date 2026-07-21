# Australia — Privacy Act 1988 material (knowledge-graph CSVs)

## IMPORTANT: what the sources actually are

The extraction was commissioned as "Privacy Act 1988 (Australia) — the Act is the priority …
model Parts and Divisions → Sections → subsections → paragraphs at clause level … and the
Part IIIC notifiable data breaches provisions".

**None of the four supplied source files contain the statutory text of the Privacy Act 1988.**
This was verified by reading the whole of each file:

| Supplied file | What it really is |
|---|---|
| `Australia_Australian_Privacy_Act_1988.txt` (~217 pp) | OAIC **Australian Privacy Principles guidelines** (combined October 2025). Regulator guidance, expressly "not legally binding". It contains Chapters A–D and 1–13 of numbered guidance paragraphs. It does **not** reproduce Schedule 1 (the APPs) or any section of the Act. |
| `Australia_Notifiable_Data_Breaches_scheme_2018_Guideline.txt` | A 3-page **AMSRO industry factsheet** on the NDB scheme (not an OAIC guideline). |
| `Australia_Notifiable_Data_Breach.txt` | A **Fortinet vendor white paper** ("Preparing for Australia's new privacy Amendment Act 2017"). Marketing material. |
| `Australia_Notifiable_data_breaches_report_January_to_June_2024.txt` | OAIC **statistical report**, January to June 2024. |

Consequences, and how they were handled:

* **No Part/Division/Section/subsection/paragraph hierarchy of the Act could be extracted**, because
  no statutory text is present. Inventing it from memory would violate the verbatim rule, so it was
  not done. There are therefore **no `nodes_Part.csv`, `nodes_Division.csv`, `nodes_Section.csv` or
  `nodes_Clause.csv` files**, and no `nodes_Definition.csv` of statutory definitions.
* **Part IIIC (notifiable data breaches) is likewise absent** from every source. The Act's NDB
  provisions (ss 26WA–26WT) are not reproduced anywhere in the supplied text. Part IIIC survives in
  this graph only as a *citation stub* in `nodes_ActProvision.csv`, with a note saying its text is
  not in the sources.
* To preserve the citation structure that *is* present, every Privacy Act provision the guidance
  **cites** (e.g. `s 6(1)`, `s 6D(4)`, `Part IIIC`, `APP 6.2(e)`) is captured as an `ActProvision`
  stub node — citation, kind and instrument only, with an explicit `note` that the statutory text is
  not present. These are pointers, **not** statutory text.

To load the actual Act into this graph, a fresh source is required — the consolidated
*Privacy Act 1988 (Cth)* from the Federal Register of Legislation.

## Schema

The schema models what the documents actually are: a regulator guidance manual plus three NDB
documents, using each document's own vocabulary (Chapter / paragraph / Key points / APP).

### Node types

| File | Type | What it holds |
|---|---|---|
| `nodes_Document.csv` | `Document` | The 4 source documents, each with `document_type` and `legal_status` so guidance can never be mistaken for statute. |
| `nodes_Chapter.csv` | `Chapter` | The 17 chapters of the APP guidelines (A, B, C, D and 1–13) with their titles. |
| `nodes_AustralianPrivacyPrinciple.csv` | `AustralianPrivacyPrinciple` | The 13 APPs, modelled explicitly, with number and title as given in the chapter headings. |
| `nodes_GuidanceParagraph.csv` | `GuidanceParagraph` | Every numbered guidance paragraph (A.1, B.2, 6.14 …), verbatim, with its running `heading`. |
| `nodes_KeyPoint.csv` | `KeyPoint` | Each bullet of the "Key points" box that opens Chapters 1–13, verbatim. |
| `nodes_ActProvision.csv` | `ActProvision` | Citation stubs for Privacy Act provisions referred to by the guidance. **Text not available** — see caveat above. |
| `nodes_NDBGuidanceSection.csv` | `NDBGuidanceSection` | Sections of the AMSRO factsheet and the Fortinet white paper, verbatim, clearly attributed to their non-regulator issuers. |
| `nodes_NDBReportSection.csv` | `NDBReportSection` | Narrative sections of the OAIC statistics report. Every row carries `content_type = "descriptive statistics and commentary — not an obligation"`. |

### Relationship types

| File | Shape |
|---|---|
| `rels_HAS_CHAPTER.csv` | `Document → Chapter` |
| `rels_HAS_PARAGRAPH.csv` | `Chapter → GuidanceParagraph` |
| `rels_HAS_KEY_POINT.csv` | `Chapter → KeyPoint` |
| `rels_EXPLAINS_APP.csv` | `Chapter → AustralianPrivacyPrinciple` |
| `rels_GUIDES_ON.csv` | `Document → AustralianPrivacyPrinciple` |
| `rels_ENACTED_BY.csv` | `AustralianPrivacyPrinciple → ActProvision` (the Schedule 1 principle it corresponds to) |
| `rels_CITES_PROVISION.csv` | `GuidanceParagraph`/`KeyPoint` → `ActProvision`, from citations appearing in the text |
| `rels_HAS_SECTION.csv` | `Document → NDBGuidanceSection` |
| `rels_HAS_REPORT_SECTION.csv` | `Document → NDBReportSection` |
| `rels_EXPLAINS.csv` | `NDBGuidanceSection`/`NDBReportSection` → `ActProvision` — only where the section's own text names the Privacy Act 1988 |

## Row counts

| File | Rows |
|---|---|
| `nodes_ActProvision.csv` | 174 |
| `nodes_AustralianPrivacyPrinciple.csv` | 13 |
| `nodes_Chapter.csv` | 17 |
| `nodes_Document.csv` | 4 |
| `nodes_GuidanceParagraph.csv` | 837 |
| `nodes_KeyPoint.csv` | 56 |
| `nodes_NDBGuidanceSection.csv` | 17 |
| `nodes_NDBReportSection.csv` | 17 |
| `rels_CITES_PROVISION.csv` | 555 |
| `rels_ENACTED_BY.csv` | 13 |
| `rels_EXPLAINS.csv` | 7 |
| `rels_EXPLAINS_APP.csv` | 13 |
| `rels_GUIDES_ON.csv` | 13 |
| `rels_HAS_CHAPTER.csv` | 17 |
| `rels_HAS_KEY_POINT.csv` | 56 |
| `rels_HAS_PARAGRAPH.csv` | 837 |
| `rels_HAS_REPORT_SECTION.csv` | 17 |
| `rels_HAS_SECTION.csv` | 17 |

Self-check (`work_au_privacy/check.py`) passes: every node id is unique within its file, every
`source_id`/`target_id` in every `rels_*.csv` resolves to a node id, and every node file's first
column is `<type>_id`.

## Source documents

* Office of the Australian Information Commissioner, *Australian Privacy Principles guidelines*,
  Privacy Act 1988, combined October 2025 — `KB 2/Australia/Australian Privacy Act 1988.pdf`
* Notifiable Data Breaches (NDB) scheme factsheet, AMSRO —
  `KB 2/Australia/Notifiable Data Breaches scheme 2018 Guideline.pdf`
* White Paper: Notifiable Data Breaches (NDB) Scheme, Fortinet —
  `KB 2/Australia/Notifiable Data Breach.pdf`
* Office of the Australian Information Commissioner, *Notifiable data breaches report:
  January to June 2024*, 16 September 2024 —
  `KB 2/Australia/Notifiable data breaches report January to June 2024.pdf`

## Caveats and gaps

1. **No statutory text anywhere** — see the section at the top. This is the dominant caveat.
2. **Chapters 12 and 13 have lost their paragraph numbers** in the PDF text layer (the prose still
   cross-references "paragraphs 12.22–12.24", but the numbers themselves are not in the extract).
   Those two chapters are therefore modelled as one passage node per heading, with
   `number` left empty and ids of the form `p_12_u7`. Their headings match the chapters' own
   contents pages exactly. All other chapters keep their real paragraph numbers.
3. **Footnote markers appear inline** in some paragraph text (e.g. "the Commissioner 1 issues"),
   an unavoidable artefact of `pdftotext -layout` on a document with superscript footnote numbers.
   Footnote *bodies* were stripped page by page and are not stored.
4. **The statistics report is included only as 17 narrative section nodes**, per instruction, and
   is marked as descriptive rather than obligation-bearing. Its numeric content is delivered almost
   entirely as infographics and charts, which `pdftotext -layout` scrambles into unattributable
   fragments (labels and values separated across the page). Extracting figures from that would
   require guessing which number goes with which label, so **no statistic nodes were created** — a
   deliberate omission in favour of accuracy. The report's glossary was also dropped for the same
   reason: it is a two-column table whose term/definition pairs interleave incorrectly in the text
   extract.
5. The Fortinet white paper and the AMSRO factsheet are **not regulator guidance**. They are kept in
   `nodes_NDBGuidanceSection.csv` but their `Document` rows record the issuer and the document type
   so they cannot be confused with OAIC material — and neither is statutory.
6. `ActProvision` nodes are derived from citations in running text by pattern match. A small number
   of false positives is possible where an unrelated "s N" appears; each row carries the citation
   verbatim so it can be verified.
