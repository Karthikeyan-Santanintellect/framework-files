# SEBI Cybersecurity and Cyber Resilience Framework (CSCRF) — knowledge-graph CSVs

## Source document

* **Circular number:** `SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113`
* **Date:** August 20, 2024
* **Subject:** *Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities (REs)*
* **Issued by:** Securities and Exchange Board of India, under Section 11(1) of the Securities and Exchange of India Act, 1992; signed by Shweta Banerjee, Deputy General Manager.
* **Framework enclosed at Annexure-1:** *Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities (REs)*, **Version 1.0**, dated August 20, 2024 (205 pages; the first 10 pages are the bilingual Hindi/English circular, the rest is the framework).
* **PDF:** `KB 2/India/SEBI Cybersecurity & Cyber Resilience Framework.pdf`
* **Text used:** `pdftotext -layout` extract (`India_SEBI_Cybersecurity_Cyber_Resilience_Framework.txt`, 8,333 lines).

### Who it applies to

Clause 16 of the circular makes the framework applicable to: AIFs; Bankers to an Issue (BTI) and Self-Certified Syndicate Banks (SCSBs); Clearing Corporations; Collective Investment Schemes (CIS); Credit Rating Agencies; Custodians; Debenture Trustees; Depositories; Designated Depository Participants; Depository Participants through Depositories; Investment Advisors / Research Analysts; KYC Registration Agencies; Merchant Bankers; Mutual Funds / AMCs; Portfolio Managers; Registrars to an Issue and Share Transfer Agents; Stock Brokers through Exchanges; Stock Exchanges; and Venture Capital Funds (see `nodes_REType.csv`, `rels_circular_applies_to_retype.csv`).

CSCRF follows a **graded approach** with five RE categories — **MIIs, Qualified REs, Mid-size REs, Small-size REs, Self-certification REs** — assigned per entity type by the thresholds in section 2 (`nodes_Threshold.csv`). In the CSCRF context MIIs comprise Stock Exchanges, Depositories, Clearing Corporations, KRAs and QRTAs. Several entity types are excluded from compliance (FPIs, FVCIs, LPCC, QDPs, REITs/InvITs, Vault Managers, individual IAs, RTAs servicing <10,000 folios, and certain DTs) — these exclusions are captured verbatim as threshold rows.

**Implementation glide path:** by **January 01, 2025** for the six categories of REs where a cybersecurity/cyber resilience circular already existed, and by **April 01, 2025** for other REs (also the Market SOC set-up deadline of January 01, 2025).

## Schema and why

The document is a regulatory circular enclosing a standards framework, so the graph follows the document's own vocabulary rather than a statute template:

* `Circular` → `CircularClause` (the 23 numbered clauses of the covering circular) and `ENCLOSES` the `Framework`.
* `Framework` → `Part` (I–IV), `Section` (1–4 front matter) → `SectionClause`, and `Annexure` (A–P).
* Part I is modelled exactly as the framework structures it: `CyberResilienceGoal` (Anticipate/Withstand/Contain/Recover/Evolve) → `CybersecurityFunction` (Governance/Identify/Protect/Detect/Respond/Recover) → `Domain` (GV.OC … EV.ST, each with its verbatim *Objective*) → `Standard` (`GV.OC.S1` … `EV.ST.S5`, the framework's own clause-level identifiers).
* Part II `Guideline` items hang off their domain and link to the standards named in the table's *Standards* column; each carries its *Applicability* and whether it is mandatory.
* Compliance machinery gets its own node types because the framework states it in tables: `ComplianceRequirement` (Table 15), `ReportingRequirement` (Tables 16/17/23), `Timeline`, `Threshold`, `RECategory`, `REType`, `CCIParameter` + `MaturityRating`, `SOCEfficacyDomain`, `IncidentSeverity`, `RiskRating`, `VAPTScopeItem`, `SupersededInstrument` (Tables 1 and 2).

Every node file carries a `source_document` column identifying the circular and PDF.

## Files

### Node files
| File | Rows | Contents |
| --- | --- | --- |
| `nodes_Abbreviation.csv` | 126 | Abbreviations table (126 entries) with expansions. |
| `nodes_Annexure.csv` | 16 | Annexures A–P with titles and the Part they sit in. |
| `nodes_CCIParameter.csv` | 23 | The 23 Cyber Capability Index parameters (Annexure-K, Table 27): measure, type, formula, target, weightage, mapped standard(s). |
| `nodes_Circular.csv` | 1 | The covering circular: number, date, subject, legal basis, signatory. |
| `nodes_CircularClause.csv` | 50 | Numbered clauses/sub-clauses 1–23 of the circular (English text), verbatim. |
| `nodes_ComplianceRequirement.csv` | 24 | Table 15 – applicability and periodicity of standards/guidelines. |
| `nodes_CyberResilienceGoal.csv` | 5 | The five cyber resiliency goals with their verbatim definitions (section 1.1). |
| `nodes_CybersecurityFunction.csv` | 6 | The six cybersecurity functions (Governance, Identify, Protect, Detect, Respond, Recover). |
| `nodes_Definition.csv` | 22 | The 22 defined terms with verbatim definitions. |
| `nodes_Domain.csv` | 23 | The 23 Part I sub-domains (GV.OC … EV.ST) with their verbatim Objective statements. |
| `nodes_Framework.csv` | 1 | CSCRF itself (Annexure-1 of the circular), Version 1.0. |
| `nodes_Guideline.csv` | 230 | Every numbered Part II guideline item, verbatim, with applicability, mandatory flag and the standards column of its table row. |
| `nodes_IncidentSeverity.csv` | 4 | Table 35 – the four incident severity categories with their verbatim descriptions. |
| `nodes_MaturityRating.csv` | 6 | CCI rating bands (Table 24 / Annexure-K). |
| `nodes_Part.csv` | 4 | Parts I–IV with the circular’s description of each. |
| `nodes_RECategory.csv` | 5 | The five RE categories used by the graded approach. |
| `nodes_REType.csv` | 35 | Regulated-entity types named in section 2 (categorization) and circular clause 16 (applicability). |
| `nodes_ReportingRequirement.csv` | 8 | Tables 16, 17 and 23 – reporting authority per RE for ISO evidence, VAPT and cyber audit. |
| `nodes_RiskRating.csv` | 4 | Risk-rating descriptions used in VAPT and cyber audit reports (Annexures A and B). |
| `nodes_SOCEfficacyDomain.csv` | 5 | The five SOC functional-efficacy domains and weightages (Annexure-N, Table 28). |
| `nodes_Section.csv` | 4 | Front-matter sections 1–4 of the framework. |
| `nodes_SectionClause.csv` | 29 | Numbered clauses of sections 1–4 (compliance, ISO audit, VAPT, cyber audit, Market SOC, IT Committee), verbatim. |
| `nodes_Standard.csv` | 128 | All 128 Part I standards (GV.OC.S1 … EV.ST.S5), verbatim, with domain/function/goal. |
| `nodes_SupersededInstrument.csv` | 43 | Tables 1 and 2 – SEBI circulars/letters/advisories superseded by CSCRF. |
| `nodes_Threshold.csv` | 49 | Section 2 categorization criteria and thresholds per entity type and category. |
| `nodes_Timeline.csv` | 26 | Deadlines and periodicities stated in the framework (implementation glide path, ISO, VAPT, cyber audit, Market SOC, incident reporting, RTO/RPO). |
| `nodes_VAPTScopeItem.csv` | 10 | Annexure-L – the 10 mandated VAPT scope items. |

### Relationship files
| File | Rows | Edge |
| --- | --- | --- |
| `rels_cci_parameter_measures_standard.csv` | 23 | CCIParameter → Standard (MEASURES) |
| `rels_circular_applies_to_retype.csv` | 19 | Circular → REType (APPLIES_TO, clause 16) |
| `rels_circular_encloses_framework.csv` | 1 | Circular → Framework (ENCLOSES, Annexure-1) |
| `rels_circular_has_clause.csv` | 50 | Circular → CircularClause (HAS_CLAUSE) |
| `rels_compliance_requirement_for_standard.csv` | 23 | ComplianceRequirement → Standard (APPLIES_TO_STANDARD, with periodicity) |
| `rels_domain_has_guideline.csv` | 230 | Domain → Guideline (HAS_GUIDELINE) |
| `rels_domain_has_standard.csv` | 128 | Domain → Standard (HAS_STANDARD) |
| `rels_framework_has_part.csv` | 4 | Framework → Part (HAS_PART) |
| `rels_framework_has_section.csv` | 4 | Framework → Section (HAS_SECTION) |
| `rels_framework_supersedes.csv` | 43 | Framework → SupersededInstrument (SUPERSEDES) |
| `rels_function_has_domain.csv` | 22 | CybersecurityFunction → Domain (HAS_DOMAIN) |
| `rels_goal_has_domain.csv` | 1 | CyberResilienceGoal → Domain (HAS_DOMAIN; EVOLVE has no separate function) |
| `rels_goal_has_function.csv` | 7 | CyberResilienceGoal → CybersecurityFunction (HAS_FUNCTION) |
| `rels_guideline_implements_standard.csv` | 393 | Guideline → Standard (IMPLEMENTS, from the Standards column of the Part II table) |
| `rels_part_contains_annexure.csv` | 16 | Part → Annexure (CONTAINS) |
| `rels_recategory_exempt_from_standard.csv` | 103 | RECategory → Standard (EXEMPT_FROM, Tables 25 and 26 plus the PR.IP.S14/EV.ST.S5 carve-outs) |
| `rels_section_has_clause.csv` | 29 | Section → SectionClause (HAS_CLAUSE) |
| `rels_threshold_maps_to_category.csv` | 37 | Threshold → RECategory (MAPS_TO_CATEGORY) |
| `rels_threshold_of_retype.csv` | 49 | Threshold → REType (THRESHOLD_OF) |
| `rels_timeline_for_standard.csv` | 10 | Timeline → Standard (TIMELINE_FOR) |

Total: 887 node rows across 27 node files, 1192 relationship rows across 20 relationship files.

## Validation

`verify.py` (in the working directory) parses every CSV and asserts: each node file's first column is `<type>_id`, ids are unique within their file, every `source_id`/`target_id` resolves to a node id, every row has the same width as its header, and every node file carries `source_document`. **Result: 0 problems, 887 distinct node ids.**

## Caveats and gaps

* **Bilingual circular.** Pages 1–10 are a two-column Hindi/English circular. Only the **English** column is captured (clauses 1–23, `nodes_CircularClause.csv`); the Hindi text is not reproduced.
* **Part II is a three-column table** (Standards | CSCRF guidelines | Applicability) in the PDF. The **guideline text is verbatim**, but the *Standards* and *Applicability* values are reconstructed from column geometry: each guideline item is matched to the nearest standards-code block and applicability block within its domain's table region. Applicability strings are re-assembled from the wrapped column fragments and normalised to the document's own wording (e.g. `All REs except small-size, self-certification REs (Mandatory)`); a small number of row-to-row attributions may be approximate. Row boundaries inside a domain are not recorded — each numbered guideline item is a row of its own.
* **Numbered sub-items** inside a guideline/standard (a., b., i., ii.) are kept inline within the parent item's verbatim text rather than split into separate nodes, because the framework numbers only the top-level items.
* **Footnote superscripts** appear glued to the preceding word in the `pdftotext` output (e.g. "incidents28", "periodic24"); footnote *bodies* have been removed, but these digits remain inside otherwise verbatim text.
* **Form/report layouts not modelled row-by-row:** Annexure-A (VAPT report format), Annexure-B (cyber audit report format and exception-reporting format), Annexure-C (recovery plan template), Annexure-E (attack-scenario matrix), and the detailed SOC-efficacy scoring tables of Annexure-N (Tables 29–34) are recorded as `Annexure` nodes; their substantive content that carries obligations (risk-rating descriptions, VAPT scope, SOC efficacy domains and weightages, incident classification, post-incident timelines) is extracted into dedicated node files.
* **Annexures F, J and M** are pointers to other SEBI circulars (outsourcing circulars, cloud-services framework, Cyber-SOC framework) and are captured as annexure titles only.
* **Box Items 1–12** (explanatory boxes in Part I) are not separate nodes; the obligations they restate are already carried by the corresponding standards/guidelines.
* The framework says exemptions in Tables 25/26 apply to small-size, self-certification and mid-size REs **provided they are onboarded to Market SOC**; that condition is stated in `SC-`/`nodes_Standard` context but the `EXEMPT_FROM` edges themselves do not encode it.
