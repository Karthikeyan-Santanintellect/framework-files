# CMMC 2.0 — knowledge-graph CSV extraction

Instrument: **Cybersecurity Maturity Model Certification (CMMC) 2.0**, U.S. Department of Defense.

## Source documents

Four source texts (`pdftotext -layout` extracts) were read in full. Each is modelled as its own
`Document` node and every other node carries a `source_document` column pointing at it.

| document_id | Document | Version / date | Role | Source PDF |
|---|---|---|---|---|
| `CMMC-MODEL-OVERVIEW-V2.13` | CMMC Model Overview | v2.13, September 2024, DoD-CIO-00001 (ZRIN 0790-ZA17) | **primary** | `KB 2/USA/CMMC/USA_CMMC_ModelOverview.pdf` |
| `CMMC-MODEL-OVERVIEW-V2.0` | CMMC Model Overview | v2.0, December 2021 | superseded | `KB 2/USA/CMMC/USA_CMMC_ModelOverview_V2_0_FINAL2_20211202_508.pdf` |
| `COGR-CMMC-2.0-OVERVIEW-2025` | COGR "DoD CMMC 2.0 Overview" | updated 6 October 2025 | secondary / explanatory | `KB 2/USA/CMMC/USA_CMMC_COGR_CMMC_Overview_Update_October_2025.pdf` |
| `INFOR-EXEC-BRIEF-CMMC` | Infor executive brief, "Updated CMMC — Aerospace & Defense" | 2022 | secondary / vendor commentary | `KB 2/USA/CMMC/USA_CMMC_Cybersecurity_Maturity_Model_Certification_CMMC.pdf` |

**Which part came from where**

* All 149 CMMC **security requirements** (identifier, short name, verbatim statement, level, domain)
  and their FAR/NIST source citations: **Model Overview v2.13**, section 2.4.1 and Appendix A
  (CMMC Model Matrix).
* All 110 v2.0 **practices** (`nodes_Practice.csv`, ids prefixed `V20:`): **Model Overview v2.0**,
  section 2.4.2 and Appendix A.
* Domains, acronyms, bibliographic references, level definitions, requirement-ID format rule:
  **v2.13** (level descriptions also captured separately from **v2.0**).
* **Scoping** (§ 170.19(b)/(c)/(d)), **assessment and affirmation** requirements, conditional CMMC
  status, phased implementation, compliance steps, effective dates of the two final rules:
  **COGR overview (Oct 2025)** — the Model Overview documents contain none of this.
* CMMC 1.0 → 2.0 change rows: **COGR** comparison table, plus two rows and the POA&M paragraph from
  the **Infor** brief (flagged by `source_document`).

## Schema

Node types use the documents' own vocabulary (Level / Domain / Security Requirement / Practice).

| File | Rows | Contents |
|---|---|---|
| `nodes_Document.csv` | 4 | the four source documents |
| `nodes_Level.csv` | 6 | CMMC Levels 1–3 as stated in v2.13, and as stated in v2.0 (separate nodes — the wording differs materially) |
| `nodes_Domain.csv` | 14 | the 14 CMMC domains |
| `nodes_SecurityRequirement.csv` | 149 | v2.13 requirements: 15 at Level 1, 110 at Level 2, 24 at Level 3 |
| `nodes_Practice.csv` | 110 | v2.0 practices: 17 at Level 1, 93 at Level 2 (Level 3 was "TBD" in v2.0) |
| `nodes_SourceReference.csv` | 149 | distinct FAR 52.204-21 / NIST SP 800-171 Rev 2 / NIST SP 800-172 citations used by the model |
| `nodes_ScopingRule.csv` | 5 | Level 1/2/3 assessment-scope rules (FCI vs CUI vs CUI + Specialized Assets), plus the enterprise/enclave statements |
| `nodes_AssessmentRequirement.csv` | 7 | per-level assessment type, annual affirmation via SPRS, C3PAO/DIBCAC, conditional CMMC status (180 days), threshold-award rule |
| `nodes_ImplementationPhase.csv` | 4 | the four rollout phases (Nov 2025 → Nov 2028) |
| `nodes_ProgramRule.csv` | 10 | rule/basis statements: 32 CFR 170.14, final-rule effective dates, fundamental research, level independence vs cumulativeness, requirement-ID format, supporting documents |
| `nodes_DefinedTerm.csv` | 7 | FCI and CUI (both v2.13 by-reference form and v2.0 verbatim definitions), Practice, Process, Specialized Assets |
| `nodes_ModelChange.csv` | 7 | CMMC 1.0 vs CMMC 2.0 differences |
| `nodes_ComplianceStep.csv` | 4 | COGR "Steps for Compliance" |
| `nodes_Reference.csv` | 5 | v2.13 Appendix C bibliography |
| `nodes_Acronym.csv` | 35 | v2.13 Appendix B abbreviations |

| Relationship file | Rows | Meaning |
|---|---|---|
| `rels_HAS_REQUIREMENT.csv` | 259 | Level → SecurityRequirement / Practice |
| `rels_IN_DOMAIN.csv` | 259 | SecurityRequirement / Practice → Domain |
| `rels_DERIVED_FROM.csv` | 310 | requirement → FAR/NIST SourceReference (as bulleted in the model matrix) |
| `rels_CORRESPONDS_TO.csv` | 167 | v2.13 SecurityRequirement → v2.0 Practice, matched only where both cite the identical FAR/NIST reference (`matched_on_reference` column records the join key) |
| `rels_APPLIES_TO_LEVEL.csv` | 6 | ScopingRule / AssessmentRequirement → Level |
| `rels_PHASE_REQUIRES_LEVEL.csv` | 4 | ImplementationPhase → Level |
| `rels_APPEARS_IN.csv` | 512 | every node → its source Document |
| `rels_SUPERSEDES.csv` | 1 | v2.13 Model Overview supersedes v2.0 |

## v2.0 vs v2.13 — version differences recorded

* **Identifier scheme.** v2.0 numbers Level 1 practices with NIST numbers (`AC.L1-3.1.1`,
  `AC.L1-3.1.20`); v2.13 renumbers them to the FAR paragraph (`AC.L1-b.1.i`, `AC.L1-b.1.iii`).
  Both id forms are preserved in their respective node files.
* **Level 1/Level 2 split.** v2.0 lists 17 Level 1 practices and 93 Level 2 practices (110 total,
  levels cumulative). v2.13 lists 15 Level 1 requirements and repeats the full 110 NIST SP 800-171
  Rev 2 requirements at Level 2 (149 total with Level 3), and states each level is **independent**
  rather than cumulative.
* **Level 3.** "TBD" throughout v2.0; fully populated in v2.13 with 24 requirements drawn from
  NIST SP 800-172 with DoD-approved parameters.
* **Terminology.** v2.0 says "practices"; v2.13 says "security requirements".
* **Legal basis.** v2.0 cites FAR 52.204-21 and DFARS 252.204-7012; v2.13 is framed on 32 CFR
  § 170.14 and defines FCI/CUI by cross-reference to 32 CFR § 170.4 / 48 CFR 4.1901 / 32 CFR
  § 2002.4(h) instead of restating the definitions.
* **Wording changes to individual requirements.** Several statements were reworded, e.g. AT.L2-3.2.1
  "Ensure that managers … are made aware" (v2.0) → "Inform managers … of" (v2.13); AU.L2-3.3.2
  "Ensure that the actions … can be uniquely traced" → "Uniquely trace the actions". Both texts are
  stored verbatim, so the diff is queryable.
* v2.0 also carries an Appendix B "Source Mapping" to NIST SP 800-53 Rev 5, CIS Controls v7.1,
  NIST CSF v1.1 and CERT-RMM v1.2, which v2.13 drops (see caveats).

## Caveats and gaps

* **Incorporation by reference.** CMMC does not reprint NIST SP 800-171 / 800-172 text as a separate
  catalog; the model matrix cites them. Those citations are captured as `SourceReference` nodes and
  `DERIVED_FROM` relationships. **No NIST SP 800-171 or 800-172 text was reproduced from memory** —
  every requirement statement here is the CMMC statement as printed in the CMMC Model Overview.
* DoD-approved parameters in Level 3 statements are underlined/italicised in the PDF; the layout
  text extract carries no formatting, so the parameters are inside the statement text but not
  separately marked. The rule stating that they exist is in `nodes_ProgramRule.csv` / `nodes_Level.csv`.
* v2.0 Appendix B "Source Mapping" (NIST 800-53, CIS, CSF, CERT-RMM per practice) was **not**
  extracted: it is a wide multi-column table whose extraction is lossy, it belongs to the superseded
  version, and v2.0 itself states these mappings "do not represent additional CMMC requirements".
* Assessment, affirmation, scoping and phasing content comes from the COGR secondary summary, not
  from 32 CFR § 170 itself; those nodes are labelled with `COGR-CMMC-2.0-OVERVIEW-2025`. The Infor
  brief is vendor commentary and is used only for a few CMMC 1.0/2.0 change rows.
* Figures (Figure 1 level overview) and the CMMC 1.0/2.0 comparison graphic are images; only the
  OCR-extracted table values from the Infor brief were used, and only where unambiguous.
* CSVs were generated by script (`scratchpad/work_cmmc/build_cmmc.py`) and validated by
  `check_cmmc.py`: unique ids per node file, every relationship endpoint resolving, correct header
  conventions.
