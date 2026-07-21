# FISMA — knowledge-graph CSV extraction

Instrument family: **FISMA (Federal Information Security Modernization Act) and its FY 2025
reporting metrics.** Six source documents were modelled, each as its own `Instrument` node.
The enacted law is the primary instrument; the 2021 bill is kept strictly separate from it.

## Source documents

| instrument_id | Document | Type | Source text |
|---|---|---|---|
| `FISMA-2014` | Federal Information Security Modernization Act of 2014, Public Law 113–283, 128 STAT. 3073 (approved December 18, 2014) | **Enacted public law (primary)** | `USA_FISMA_Federal_Information_Security_Modernization_Act2.txt` |
| `S2902-2021` | S. 2902, 117th Congress, 1st Session, "Federal Information Security Modernization Act of 2021" (Sept 29, 2021) | **BILL — introduced only, never enacted** | `USA_FISMA_Federal_Information_Security_Modernization_Act1.txt` |
| `CIO-FY25` | FY 2025 CIO FISMA Metrics, Version 1.1 | Reporting metrics | `USA_FISMA_FY25_FISMA_CIO_Metrics_v1_1.txt` |
| `SAOP-FY25` | FY 2025 SAOP FISMA Reporting Metrics (August 2025) | Reporting metrics | `USA_FISMA_FY25_SAOP_FISMA_Metrics_508.txt` |
| `IG-FY25` | FY 2025 Inspector General FISMA Reporting Metrics v2.0 (April 3, 2025) | Reporting metrics | `USA_FISMA_Final_FY_2025_IG_FISMA_Reporting_Metrics_Ver_2_0_April_2025_508_0.txt` |
| `IGGUIDE-FY25` | FY 2025 IG FISMA Metrics Evaluator's Guide, Version 1.0 (May 5, 2025) | Evaluation guidance | `USA_FISMA_Final_FY_2025_IG_FISMA_Metrics_Evaluation_Guide_05_May_2025_508.txt` |

Original PDFs: `KB 2/USA/FISMA/*.pdf` (citation only).

## Schema rationale

The six documents have genuinely different internal structures, so the schema uses each
document's own vocabulary rather than one generic node type:

* **Statute (PL 113–283).** The Act is a short enacting Act that *inserts* a new subchapter into
  44 U.S.C. chapter 35. Both layers are modelled: `ActSection`/`ActClause` for the Act's own
  provisions (SEC. 1, SEC. 2(b)–(f) — major-incident guidance, continuous diagnostics, breach
  notification, technical and conforming amendments), and `UscSection`/`UscClause` for
  §§ 3551–3558 **as printed in the Act**. Every lettered/numbered subdivision down to item level
  (`(b)(7)(C)(iii)(III)(aa)`) is its own row with a `citation` such as `44 U.S.C. § 3554(b)(7)(C)`.
* **Bill (S. 2902).** Deliberately parallel but separate node types (`BillTitle`, `BillSection`,
  `BillProposedSection`, `BillClause`) so that proposed text can never be confused with law.
  `BillClause.quoted_matter` marks text the bill would insert into the U.S. Code.
* **Definitions.** `Definition` holds every term defined in 44 U.S.C. § 3552(b) plus the CIO
  metrics' Appendix A definitions.
* **CIO metrics.** Ten named sections → hierarchical numbered metrics (`1.1`, `1.1.5.2`, …),
  self-nesting through `rels_contains.csv`.
* **SAOP metrics.** Fourteen numbered sections → lettered questions (`1a` … `14k`) with
  their multiple-choice `ResponseOption`s.
* **IG metrics.** NIST CSF 2.0 `IGFunction` (6) → `IGDomain` (10, with the document's verbatim
  "Related Cybersecurity Framework 2.0 Categories") → `IGMetric` (35, each with its bracketed
  identifier, criteria, supplemental guidance and review cycle) → `IGMaturityCriterion`
  (the verbatim cell for each of the five `MaturityLevel`s).
* **Evaluator's Guide.** `GuideMetric` mirrors each IG metric and carries `SourceEvidence`
  bullets ("Suggested Standard Source Evidence") and `AssessorBestPractice` blocks keyed to a
  maturity level.

### Node types
`Instrument`, `ActSection`, `ActClause`, `UscSection`, `UscClause`, `Definition`, `BillTitle`,
`BillSection`, `BillProposedSection`, `BillClause`, `CIOMetricSection`, `CIOMetric`,
`SAOPSection`, `SAOPQuestion`, `ResponseOption`, `IGFunction`, `IGDomain`, `IGMetric`,
`MaturityLevel`, `IGMaturityCriterion`, `GuideMetric`, `SourceEvidence`, `AssessorBestPractice`.

### Relationship types
`CONTAINS`, `INSERTS` (Act SEC. 2 → inserted 44 U.S.C. section), `PROPOSES_SECTION`,
`DEFINES`, `HAS_RESPONSE_OPTION`, `HAS_MATURITY_CRITERION`, `AT_MATURITY_LEVEL`,
`EVALUATION_GUIDANCE_FOR`, `SUGGESTS_SOURCE_EVIDENCE`, `HAS_ASSESSOR_BEST_PRACTICE`,
`REPORTS_UNDER`, `COMPANION_DOCUMENT_TO`, `WOULD_AMEND`.

## Files and row counts

| File | Rows |
|---|---|
| nodes_Instrument.csv | 6 |
| nodes_ActSection.csv | 2 |
| nodes_ActClause.csv | 49 |
| nodes_UscSection.csv | 8 |
| nodes_UscClause.csv | 192 |
| nodes_Definition.csv | 18 |
| nodes_BillTitle.csv | 3 |
| nodes_BillSection.csv | 20 |
| nodes_BillProposedSection.csv | 10 |
| nodes_BillClause.csv | 876 |
| nodes_CIOMetricSection.csv | 10 |
| nodes_CIOMetric.csv | 139 |
| nodes_SAOPSection.csv | 14 |
| nodes_SAOPQuestion.csv | 82 |
| nodes_ResponseOption.csv | 245 |
| nodes_IGFunction.csv | 6 |
| nodes_IGDomain.csv | 10 |
| nodes_IGMetric.csv | 35 |
| nodes_MaturityLevel.csv | 5 |
| nodes_IGMaturityCriterion.csv | 125 |
| nodes_GuideMetric.csv | 35 |
| nodes_SourceEvidence.csv | 192 |
| nodes_AssessorBestPractice.csv | 57 |
| rels_contains.csv | 1501 |
| rels_defines.csv | 18 |
| rels_has_response_option.csv | 245 |
| rels_maturity.csv | 250 |
| rels_evaluation_guidance_for.csv | 35 |
| rels_suggests_source_evidence.csv | 192 |
| rels_assessor_best_practice.csv | 114 |
| rels_instrument_reference.csv | 5 |

(`rels_assessor_best_practice.csv` carries one `HAS_ASSESSOR_BEST_PRACTICE` and one
`AT_MATURITY_LEVEL` edge per practice; `rels_maturity.csv` likewise carries two edges per
criterion.)

Validation: all node ids are unique within and across node files (2,139 ids); every
`source_id`/`target_id` in every relationship file resolves to a node id; 0 errors.

## Caveats and gaps

* **Verbatim, with layout repair only.** Text was rejoined from `pdftotext -layout` output:
  page headers/footers, the Statutes-at-Large marginal notes (e.g. "Consultation.",
  "44 USC 3553."), running titles and line-break hyphenation were removed/repaired. No wording
  was altered, paraphrased or supplied from outside the documents.
* Clause text retains its printed subdivision marker (e.g. `(b)(1) The term ‘binding
  operational directive’ means …`); the opening `‘‘` of quoted amendatory matter is stripped.
* Where a paragraph `(1)` is printed **inline** with its subsection (e.g. 44 U.S.C. § 3553(e),
  § 3554(d), § 3555(a)), its text stays inside the subsection row; its children are still
  addressed as `(d)(1)(A)` etc.
* A small number of clause paths repeat inside one section because amendatory text re-uses
  labels (e.g. quoted "(3)" inserted inside SEC. 2(e)(3)). Those ids carry a `#2` suffix.
* **IG metrics tables** are wide five-column maturity tables. Columns were recovered by
  positional slicing. On the pages for metrics 1–4, 10 and 27 the "Supplemental Guidance" and
  "Review Cycle" columns are typeset flush against each other and could not be separated: those
  rows carry the merged text in `supplemental_guidance`, and `review_cycle` is set to
  `FY 2025 Supplemental` where the document states it. Elsewhere both columns are clean.
* Ten of the 35 IG questions (identifiers `*.SUM`, one per domain) are free-text summary
  questions and have no maturity-level criteria — hence 125 (25 metrics x 5 levels), not 175,
  criterion rows. The document also prints
  function-level summary tags (`GV.SUM`, `PR.SUM`, …) inside those same summary rows; only the
  domain-level tag is stored in `identifier`.
* IG metrics 17–19 are tagged `IDAM-01`…`IDAM-03` in the source (hyphen, not period); the
  identifiers are recorded exactly as printed.
* Assessor Best Practices are empty in the guide for several metrics (the headings are printed
  with no text); only the 57 populated blocks are stored.
* CIO metric numbers such as `1.1.5.1` include table-cell placeholders in the PDF
  (`4.1.1.a`, `6.1.1.id`); those placeholder cells are **not** stored as metrics, only the
  numbered questions are. Superscript footnote markers occasionally survive as a bare digit
  inside a metric's text (e.g. "Organization-operated 1 systems"); footnote bodies themselves
  were dropped.
* The SAOP document's checkbox glyphs were removed from response-option text; option wording is
  otherwise verbatim.
* No penalties or monetary thresholds appear in any of these documents; deadlines that are
  stated (7 days, 30 days, March 1, August 1, 2025) remain inside the verbatim clause text.
