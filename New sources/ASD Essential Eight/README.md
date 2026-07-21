# ASD Essential Eight Maturity Model — knowledge-graph CSVs

**Source document:** `KB 2/Australia/ASD Essential Eight Maturity Model.pdf`
**Publisher:** Australian Signals Directorate (ASD)
**Version / date:** First published June 2017; last updated **November 2023** (as stated on page 1 of the source).

## Schema

The document is a maturity model, not a statute, so the schema uses the document's own vocabulary:
*mitigation strategy*, *maturity level*, and the individual requirement statements listed in the
Description column of Appendices A–C (modelled as `Control`).

### Node types

| File | Type | Rows | Notes |
|---|---|---|---|
| `nodes_Framework.csv` | `Framework` | 1 | The maturity model itself, with publication dates. |
| `nodes_MitigationStrategy.csv` | `MitigationStrategy` | 8 | The Essential Eight, named verbatim from the Mitigation Strategy column. |
| `nodes_MaturityLevel.csv` | `MaturityLevel` | 4 | Maturity Level Zero–Three, each with its verbatim descriptive text from the "Maturity levels" section. |
| `nodes_Control.csv` | `Control` | 304 | Every individual requirement statement, verbatim, one row per statement per strategy per maturity level. |
| `nodes_GuidanceSection.csv` | `GuidanceSection` | 6 | Introduction, Implementation, Maturity levels, Requirements for each maturity level, Further information, Contact details. |
| `nodes_GuidanceParagraph.csv` | `GuidanceParagraph` | 15 | Clause-level verbatim paragraphs of the introductory guidance. |

`Control` ids encode strategy + level + sequence, e.g. `MFA-ML2-11` = 11th statement for
Multi-factor authentication at Maturity Level Two.

### Relationship types

| File | Rel type | Rows |
|---|---|---|
| `rels_HAS_STRATEGY.csv` | `HAS_STRATEGY` (Framework → MitigationStrategy) | 8 |
| `rels_HAS_MATURITY_LEVEL.csv` | `HAS_MATURITY_LEVEL` (Framework → MaturityLevel) | 4 |
| `rels_HAS_GUIDANCE_SECTION.csv` | `HAS_GUIDANCE_SECTION` (Framework → GuidanceSection) | 6 |
| `rels_HAS_PARAGRAPH.csv` | `HAS_PARAGRAPH` (GuidanceSection → GuidanceParagraph) | 15 |
| `rels_IMPLEMENTS_STRATEGY.csv` | `IMPLEMENTS_STRATEGY` (Control → MitigationStrategy) | 304 |
| `rels_AT_MATURITY_LEVEL.csv` | `AT_MATURITY_LEVEL` (Control → MaturityLevel) | 304 |
| `rels_PRECEDES.csv` | `PRECEDES` (MaturityLevel → next MaturityLevel) | 3 |

## Control counts per strategy per maturity level

| Mitigation Strategy | ML1 | ML2 | ML3 |
|---|---|---|---|
| Patch applications | 9 | 11 | 13 |
| Patch operating systems | 8 | 8 | 16 |
| Multi-factor authentication | 7 | 19 | 23 |
| Restrict administrative privileges | 7 | 20 | 29 |
| Application control | 3 | 14 | 19 |
| Restrict Microsoft Office macros | 4 | 5 | 11 |
| User application hardening | 4 | 22 | 27 |
| Regular backups | 6 | 8 | 11 |
| **Total** | **48** | **107** | **149** |

## Caveats and gaps

- **Maturity Level Zero has no control statements.** The document defines it only as a description of
  weakness ("This maturity level signifies that there are weaknesses…"); Appendices A–C cover Levels
  One to Three only. The `MaturityLevel` node for ML0 therefore has a description but no attached controls.
- **Appendix D (Comparison of maturity levels) is not extracted as separate rows.** It is a
  three-column side-by-side restatement of Appendices A–C with changes bolded; every statement in it
  already appears verbatim in Appendices A–C, so extracting it would duplicate rows. The `–` markers
  it uses to show absence are recoverable from the graph by comparing controls per level.
- Statements repeated identically across strategies/levels (e.g. the logging and incident-reporting
  statements) are retained as distinct rows, because the document lists them separately under each
  strategy and level.
- Typographic quotes in the source (`’`) were normalised to ASCII apostrophes; wording is otherwise
  verbatim, with `pdftotext -layout` column wrapping rejoined into single lines.
- The source is guidance published by ASD, not legislation; it states there is no requirement for
  independent certification.

## Self-check

A validation pass confirms: all node ids unique within each file, all 644 relationship endpoints
resolve to existing node ids, all files parse as valid UTF-8 CSV with the required first columns.
