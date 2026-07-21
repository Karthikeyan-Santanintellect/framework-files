# FFIEC Cybersecurity Assessment Tool — knowledge-graph CSVs

**Source document:** `KB 2/USA/FFIEC Cybersecurity Assessment Tool.pdf`
**Issuing body:** Federal Financial Institutions Examination Council (FFIEC)
**Version / date printed on the cover:** May 2017 (running footer "May 2017" on every page; 57 pages)
**PRA notice on the cover:** OMB Control No. 1557-0328; Expiration date: 09/30/2025

## Schema

The Assessment states its own two-part structure, so the graph is modelled on the
document's own vocabulary rather than a generic controls template.

```
Instrument ─HAS_PART→ Part
  Part One: Inherent Risk Profile
    ─HAS_RISK_CATEGORY→ RiskCategory (5)
        ─HAS_ACTIVITY→ RiskActivity ("activity, service, or product", 39)
            ─HAS_RISK_LEVEL_STATEMENT→ RiskLevelStatement (39 × 5 = 195)
                ─AT_RISK_LEVEL→ RiskLevel (Least … Most)
  Part Two: Cybersecurity Maturity
    ─HAS_DOMAIN→ Domain (5)
        ─HAS_ASSESSMENT_FACTOR→ AssessmentFactor (15)
            ─HAS_COMPONENT→ Component (30)
                ─HAS_DECLARATIVE_STATEMENT→ DeclarativeStatement (494)
                    ─AT_MATURITY_LEVEL→ MaturityLevel (Baseline … Innovative)
                    ─MAPS_TO_IT_HANDBOOK→ ITHandbookReference
Instrument ─HAS_RESOURCE→ Resource      (the companion appendices the tool names)
Instrument ─DEFINES_TERM→ DefinedTerm
```

**Clause-level granularity.** Each of the 494 declarative statements is one row,
verbatim, tied to its Component → Assessment Factor → Domain and to its maturity
level. Each of the 195 Inherent Risk Profile cells (one activity × one risk level)
is likewise its own row, verbatim. Risk-level, maturity-level, domain and
assessment-factor definitions are the verbatim definitions printed in the User's
Guide (Tables 1 and 2 and the risk-level bullets).

**Mappings.** The tool's Baseline statements carry inline FFIEC IT Examination
Handbook citations, e.g. `(FFIEC Information Security Booklet, page 3)`. These are
extracted into `nodes_ITHandbookReference.csv` (71 distinct booklet/page citations)
and `rels_declarative_statement_maps_to_it_handbook.csv` (118 links). The NIST
Cybersecurity Framework mapping is *named* by the document (Appendix B) but is a
separate publication and is **not** contained in this PDF; it is recorded only as a
`Resource` node with the document's verbatim statement about it.

## Files

| File | Rows |
| --- | --- |
| nodes_Instrument.csv | 1 |
| nodes_Part.csv | 2 |
| nodes_RiskCategory.csv | 5 |
| nodes_RiskActivity.csv | 39 |
| nodes_RiskLevel.csv | 5 |
| nodes_RiskLevelStatement.csv | 195 |
| nodes_Domain.csv | 5 |
| nodes_AssessmentFactor.csv | 15 |
| nodes_Component.csv | 30 |
| nodes_MaturityLevel.csv | 5 |
| nodes_DeclarativeStatement.csv | 494 |
| nodes_ITHandbookReference.csv | 71 |
| nodes_Resource.csv | 4 |
| nodes_DefinedTerm.csv | 2 |
| rels_has_part.csv | 2 |
| rels_part_has_risk_category.csv | 5 |
| rels_category_has_activity.csv | 39 |
| rels_activity_has_risk_level_statement.csv | 195 |
| rels_risk_statement_at_risk_level.csv | 195 |
| rels_part_has_domain.csv | 5 |
| rels_domain_has_assessment_factor.csv | 15 |
| rels_assessment_factor_has_component.csv | 30 |
| rels_component_has_declarative_statement.csv | 494 |
| rels_declarative_statement_at_maturity_level.csv | 494 |
| rels_instrument_has_resource.csv | 4 |
| rels_instrument_defines_term.csv | 2 |
| rels_declarative_statement_maps_to_it_handbook.csv | 118 |

Node totals: 873 unique ids. All relationship endpoints resolve; all ids unique.

## Notes and caveats

- The PDF contains the User's Guide, the Inherent Risk Profile and the
  Cybersecurity Maturity parts only. Appendix A (Baseline-to-IT-Handbook mapping),
  Appendix B (NIST CSF mapping), Appendix C (Glossary) and the "Overview for Chief
  Executive Officers and Boards of Directors" are listed as separate FFIEC
  documents and are not present in this file, so their content is not extracted.
- `nodes_Component.csv` keeps both `name_as_printed` (the all-caps sidebar label
  used in the PDF, e.g. `STRATEGY/ POLICIES`) and a normalised `name`.
- 16 declarative statements carry an applicability note such as
  `(*N/A if there are no wireless networks.)`; this is preserved inside the
  verbatim `text` and also surfaced in the `applicability_note` column.
- The Assessment Factor names differ slightly between the headings and Table 1
  (`Detection, Response, & Mitigation` vs `Detection, Response, and Mitigation`).
  The heading form is used as the node `name`; the Table 1 wording is preserved
  verbatim inside `definition`.
- Layout artefacts of `pdftotext -layout` (page headers/footers, the `Y, Y(C), N`
  answer-column label, five-column table wrapping and mid-page-break line splits)
  were rejoined programmatically; wording is unmodified.
- The two summary tables ("Number of Statements Selected in Each Risk Level") are
  blank worksheet grids in the source and carry no text, so they are not modelled.
