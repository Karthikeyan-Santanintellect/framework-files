# COSO ERM — knowledge-graph extraction

Two source documents, modelled as two separate `Instrument` nodes in this one folder.

## What the sources actually contain (read this first)

**1. `KB 2/USA/COSO Enterprise Risk Management Framework.pdf`**
→ instrument id `coso_erm_2017_appendices`

Despite the file name, this PDF is **not the COSO ERM framework body**. Its cover page reads
"Enterprise Risk Management — Integrating with Strategy and Performance / **Appendices** / June 2017 /
**Volume II**". The whole file (28 numbered pages) is the appendices volume only:

* A. Project Background and Approach for Revising the Framework
* B. Summary of Public Comments
* C. Roles and Responsibilities for Enterprise Risk Management
* D. Risk Profile Illustrations

**It therefore contains no chapters 1–9, no component chapters, no statements of the five components
or the twenty principles, and no glossary.** Volume I (the framework body, which carries the
principles and the glossary) is not present in the supplied text. Nothing in this extraction invents
that material.

**2. `KB 2/USA/Compliance-Risk-Management-Applying-the-COSO-ERM-Framework.pdf`**
→ instrument id `coso_compliance_risk_2020`

COSO application paper (November 2020, authored by SCCE & HCCA). This document **does** enumerate
the five ERM components and all twenty principles (Figure 1.3 and the section-opening lists), and it
gives, per principle, a discussion and a "Key characteristics" table. All component names, principle
numbers and principle statements in this extraction come from *this* document — they are quoted from
it, not supplied from outside knowledge. The paper reproduces the principle **names**; it does not
reproduce the full framework's per-principle explanatory text from Volume I.

Combined coverage of what the task asked for:

| Asked for | Where it came from |
|---|---|
| Five components | doc 2 (Figure 1.2/1.3 and section headings) |
| Twenty principles + statements | doc 2 (Figure 1.3, section principle lists, `Principle n —` headings) |
| Per-principle supporting discussion at clause level | doc 2, §2–6 |
| Chapters / sections | doc 2 §1–6 + Appendices 1–2; doc 1 Appendices A–D |
| Roles and responsibilities | doc 1 Appendix C (full lines-of-accountability treatment) + doc 2 (CCO, board, Three Lines Model) |
| Glossary | **absent from both PDFs.** `nodes_DefinedTerm.csv` instead holds every term either of the documents defines in-line, incl. the whole of doc 2's Figure 1.4 term table |

## Schema

Bespoke to these two documents; node type names use the documents' own vocabulary.

Node types

| File | Rows | What it is |
|---|---|---|
| `nodes_Instrument.csv` | 2 | the two publications, with issuing body, author, date, contents |
| `nodes_Component.csv` | 5 | the five ERM components (doc 2) |
| `nodes_Principle.csv` | 20 | the twenty principles: number, name (Figure 1.3 form), statement (section-list form), component, key-characteristics table reference |
| `nodes_KeyCharacteristic.csv` | 120 | every bullet of Tables 2.1–6.3 ("Key characteristics" per principle), verbatim |
| `nodes_Section.csv` | 6 | doc 2 numbered sections 1–6 |
| `nodes_Appendix.csv` | 6 | doc 1 Appendices A–D and doc 2 Appendices 1–2 |
| `nodes_Subsection.csv` | 57 | every headed sub-part of a section/appendix |
| `nodes_Clause.csv` | 552 | clause-level unit: each paragraph, bullet and numbered item, verbatim; `label` holds the item's own marker (`•`, `1.`, `(2)`, …) |
| `nodes_DefinedTerm.csv` | 27 | defined terms with verbatim definitions and where they are stated |
| `nodes_USSGProvision.csv` | 13 | U.S. Federal Sentencing Guidelines ¶8B2.1(b)(1)–(7) and (c), quoted in doc 2 Appendix 1, split to sub-paragraph level |
| `nodes_ProgramElement.csv` | 8 | the seven elements of an effective C&E program plus the "eighth element" |
| `nodes_ExternalGuidance.csv` | 10 | other regimes the paper summarises (USSG, UK MoJ Bribery Act guidance, ISO 37001, ISO/DIS 37301, France AFA, Brazil, Costa Rica, New Zealand, Singapore, Spain) |
| `nodes_Role.csv` | 18 | board, committees, CEO, CRO, management, ERM committee, the three lines, external auditors, CCO, Three Lines Model roles |
| `nodes_RiskResponse.csv` | 7 | Accept / Avoid / Pursue / Reduce / Share / Review business objective / Review strategy (doc 1 Appendix D), with verbatim descriptions |
| `nodes_PrioritizationCriterion.csv` | 5 | adaptability, complexity, velocity, persistence, recovery (doc 1 Appendix D) |
| `nodes_Figure.csv` | 24 | every figure/table caption in both documents, attached to its parent |
| `nodes_ScaleLevel.csv` | 10 | the 1–5 likelihood scale (Figure 4.2) and 1–5 impact scale (Figure 4.3) with their verbatim anchors and thresholds (e.g. `$25–$100 million`, `At least once in 5 years`) |

Relationship types

| File | Rows | Meaning |
|---|---|---|
| `rels_contains.csv` | 641 | instrument→section/appendix→subsection→clause; also principle→clause, guidance→clause, appendix→element/risk-response/criterion |
| `rels_has_principle.csv` | 20 | component → principle |
| `rels_applies_component.csv` | 5 | doc 2 section → component it applies |
| `rels_has_key_characteristic.csv` | 120 | principle → key characteristic |
| `rels_defines_term.csv` | 27 | instrument → defined term |
| `rels_cites_provision.csv` | 13 | Appendix 1 → USSG provision |
| `rels_element_provision.csv` | 13 | program element → USSG provision it rests on |
| `rels_element_discussion.csv` | 8 | program element → the Appendix 1 subsection discussing it |
| `rels_references_guidance.csv` | 10 | instrument → external guidance regime |
| `rels_lists_expectation.csv` | 50 | external guidance → each of its listed elements (clause) |
| `rels_role_responsibility.csv` | 58 | role → responsibility clause |
| `rels_role_description.csv` | 4 | board committee role → its descriptive clause |
| `rels_has_figure.csv` | 24 | section/appendix/principle → figure |
| `rels_has_scale_level.csv` | 10 | figure → scale level |
| `rels_cross_reference.csv` | 19 | clause/criterion → the principle it cites by number |

Totals: 890 node rows, 1,022 relationship rows.

## Verification

`validate.py` (in the working scratch directory) re-parses every CSV: all node ids unique within
their file, every `source_id`/`target_id` resolves to an existing node id, every node file starts
with a `<type>_id` column and carries `source_document`. Result: **0 errors**.

## Caveats and gaps

* **Doc 1 is appendices only** (see above). The framework body and glossary are not in the supplied
  material, so no component/principle text is attributed to doc 1.
* Doc 2 is **guidance**, not a statute. The only quasi-legal text in it is the USSG extract in
  Appendix 1, captured verbatim in `nodes_USSGProvision.csv`.
* The sources are `pdftotext -layout` extracts. Doc 2 is two-column; columns were separated
  per prose block, tables were extracted from the raw layout separately, and wrap hyphens were
  rejoined only where the two fragments form a real word (so `decision-making` and `not-for-profit`
  keep their hyphens). A dozen paragraphs in which figure captions/axis labels were interleaved with
  running prose (doc 1 Appendix D, doc 2 Figures 1.3/4.2/4.3/5.1) were reassembled by removing the
  interleaved figure labels; wording is unchanged.
* Graphics-only content (risk-curve plots, the COSO cube, Figure 4.4's colour matrix, Figure 5.1's
  cell grid, Figure C.2's role lists laid out in three columns, Figure D.9's boxes) has no text that
  survives extraction; those figures are recorded as `Figure` nodes with their captions but their
  interior graphics are not reconstructed. Figures 4.2 and 4.3, which are genuine text tables, are
  fully captured in `nodes_ScaleLevel.csv`.
* Front matter (COSO board lists, contributor lists, acknowledgments, copyright pages) is recorded
  only as instrument-level metadata, not as clauses.

Source documents cited on every row:
`COSO Enterprise Risk Management Framework.pdf` and
`Compliance-Risk-Management-Applying-the-COSO-ERM-Framework.pdf` (both `KB 2/USA/`).
