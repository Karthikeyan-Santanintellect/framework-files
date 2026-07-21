# FDA Cybersecurity in Medical Devices — knowledge-graph extraction

## What this document actually is

The source PDF (`KB 2/USA/FDA Cybersecurity for Medical Devices.pdf`) is:

> **Cybersecurity in Medical Devices: Quality Management System Considerations and Content of
> Premarket Submissions — Guidance for Industry and Food and Drug Administration Staff**
> Document issued on **February 3, 2026**. Docket **FDA-2021-D-1158**; CDRH document number
> **GUI00001825**. Issued by CDRH and CBER (U.S. Department of Health and Human Services, FDA).

It is the **premarket** cybersecurity guidance — not the postmarket guidance, not a webpage print,
and not the statutory text of section 524B. It is the full guidance document, complete with
preface, table of contents, Sections I–VII, Appendices 1–5, and the Guidance History table.

**Binding status: non-binding guidance.** Every page carries the running banner
"Contains Nonbinding Recommendations", and the document states:

> "This guidance represents the current thinking of the Food and Drug Administration (FDA or
> Agency) on this topic. It does not establish any rights for any person and is not binding on FDA
> or the public."

and

> "In general, FDA's guidance documents do not establish legally enforceable responsibilities. …
> The use of the word *should* in Agency guidances means that something is suggested or
> recommended, but not required."

The guidance does, however, quote and explain **binding** law that it sits alongside: section 524B
of the FD&C Act (added by section 3305 of FDORA 2022), the QMSR at 21 CFR Part 820 (which
incorporates ISO 13485:2016 by reference), the misbranding provisions of sections 502(a)(1),
502(f) and 502(j), and the prohibited-act provision at section 301(q). Those are modelled
separately as `StatutoryProvision` nodes so binding requirements are never conflated with the
document's own non-binding recommendations. It supersedes the June 27, 2025 edition of the same
guidance and was issued under Level 2 guidance procedures (21 CFR 10.115(g)(4)).

## Schema

The schema mirrors the guidance's own structure and vocabulary: Roman-numeral **Sections**,
lettered/numbered/parenthesised **Subsections** (to the deepest level the document uses, e.g.
V.A.4(b), V.B.2(c), VII.C.1), and **Appendices** 1–5 with their own subsections. On top of that
skeleton, the document's named constructs each become their own node type, because they are the
things a compliance graph is actually asked about: the five **security objectives**, the eight
**security control categories** and their Appendix 1 **recommendations**, the four **architecture
views**, the **testing types**, **labeling recommendations**, **cybersecurity management plan
elements**, the Appendix 4 Table 1 **submission documentation elements**, the section 524B
**statutory provisions** and **cyber device criteria**, and the Appendix 5 **terminology**.

### Node files

| File | Rows | Contents |
|---|---|---|
| nodes_Document.csv | 1 | Document identity, dates, docket, binding status and statement, supersession |
| nodes_Section.csv | 7 | Sections I–VII, verbatim body text |
| nodes_Subsection.csv | 44 | All lettered/numbered subsections incl. Appendix 1 and 2 subsections |
| nodes_Appendix.csv | 5 | Appendices 1–5 |
| nodes_GuidanceHistoryEntry.csv | 3 | Guidance History table (Feb 2026, June 2025, March 2024) |
| nodes_SecurityObjective.csv | 5 | Security Objectives listed in Section IV.B |
| nodes_ScalingFactor.csv | 6 | Factors that determine extent of security requirements (IV.B) |
| nodes_SubmissionType.csv | 8 | Premarket submission types in scope (Section II) |
| nodes_RiskManagementReportElement.csv | 4 | Required contents of the security risk management report (V.A) |
| nodes_ThreatModelRequirement.csv | 3 | "The threat model should:" bullets (V.A.1) |
| nodes_MeasureMetric.csv | 3 | SPDF measures and metrics (V.A.6) |
| nodes_SecurityControlCategory.csv | 8 | Security control categories (V.B.1), linked to Appendix 1 |
| nodes_SecurityControlRecommendation.csv | 41 | Per-category control recommendations (Appendix 1) |
| nodes_ArchitectureView.csv | 4 | Global System, Multi-Patient Harm, Updateability/Patchability, Security Use Case |
| nodes_ArchitectureViewRequirement.csv | 4 | "These security architecture views should:" (V.B.2) |
| nodes_ArchitectureViewInformationDetail.csv | 26 | Information details for an architecture view (Appendix 2.B) |
| nodes_TestingType.csv | 4 | Cybersecurity testing types recommended in V.C |
| nodes_LabelingRecommendation.csv | 14 | Labeling information examples (VI.A) |
| nodes_CybersecurityManagementPlanElement.csv | 9 | Cybersecurity management plan elements (VI.B) |
| nodes_CoordinatedVulnerabilityDisclosureElement.csv | 3 | What CVD "could include" (VII.C.1) |
| nodes_CyberDeviceCriterion.csv | 3 | The three limbs of the 524B(c) "cyber device" definition |
| nodes_InternetConnectivityFeature.csv | 4 | Features FDA considers to give "ability to connect to the internet" (VII.B) |
| nodes_StatutoryProvision.csv | 15 | FD&C Act / FDORA / 21 CFR provisions quoted by the guidance |
| nodes_SubmissionDocumentationElement.csv | 14 | Appendix 4 Table 1 rows, incl. IDE column |
| nodes_IDEDocumentationElement.csv | 5 | IDE application documentation (Appendix 3) |
| nodes_Term.csv | 51 | Appendix 5 terminology, verbatim definitions |
| nodes_Footnote.csv | 125 | All numbered footnotes, verbatim |

### Relationship files

| File | Rows | Meaning |
|---|---|---|
| rels_contains.csv | 56 | Document → Section/Appendix → Subsection hierarchy |
| rels_states_security_objective.csv | 5 | IV.B → SecurityObjective |
| rels_scaling_factor.csv | 6 | IV.B → ScalingFactor |
| rels_applies_to_submission_type.csv | 8 | Section II → SubmissionType |
| rels_provision_applies_to_submission_type.csv | 5 | 524B(a) → the five pathways it names |
| rels_report_element.csv | 4 | V.A → RiskManagementReportElement |
| rels_threat_model_requirement.csv | 3 | V.A.1 → ThreatModelRequirement |
| rels_recommends_measure.csv | 3 | V.A.6 → MeasureMetric |
| rels_recommends_control_category.csv | 8 | V.B.1 → SecurityControlCategory |
| rels_category_detailed_in.csv | 8 | SecurityControlCategory → Appendix 1 subsection |
| rels_has_control_recommendation.csv | 41 | Appendix 1 subsection → SecurityControlRecommendation |
| rels_recommends_view.csv | 4 | V.B.2 → ArchitectureView |
| rels_view_described_in.csv | 4 | ArchitectureView → its V.B.2(a)–(d) subsection |
| rels_view_requirement.csv | 4 | V.B.2 → ArchitectureViewRequirement |
| rels_architecture_information_detail.csv | 26 | Appendix 2.B → ArchitectureViewInformationDetail |
| rels_recommends_testing.csv | 4 | V.C → TestingType |
| rels_recommends_labeling.csv | 14 | VI.A → LabelingRecommendation |
| rels_plan_element.csv | 9 | VI.B → CybersecurityManagementPlanElement |
| rels_cvd_element.csv | 3 | VII.C.1 → CVD element |
| rels_cyber_device_criterion.csv | 3 | 524B(c) → criterion |
| rels_internet_connectivity_feature.csv | 4 | VII.B → InternetConnectivityFeature |
| rels_discusses_provision.csv | 15 | Subsection → StatutoryProvision it discusses |
| rels_documentation_element.csv | 22 | Appendix 4 → Table 1 element; element → sub-element |
| rels_ide_documentation.csv | 5 | Appendix 3 → IDEDocumentationElement |
| rels_defines_term.csv | 51 | Appendix 5 → Term |

Totals: 419 nodes, 315 relationships across 25 relationship files.

## Method and caveats

- Built by script from a `pdftotext -layout` extract. Page furniture (the "Contains Nonbinding
  Recommendations" banner and page numbers) and footnote blocks were removed from body text; the
  footnotes are preserved separately in `nodes_Footnote.csv`.
- Text is verbatim, with hard line wraps rejoined into single-line prose.
- **Inline superscript footnote markers survive as digits glued to words** in some body and bullet
  text (e.g. "device software function1", "Identity management84", "cryptographically strong76").
  This is an artefact of the PDF text layer, not an edit; the wording is otherwise unaltered.
- Nested bullet lists were modelled as one node per top-level bullet with its sub-bullets merged
  into the same verbatim text (Appendix 1, Section V.C). Appendix 2.B is the exception: because its
  operative content is the sub-bullets, every bullet there is its own node.
- **Appendix 4 Table 1** is a real table and does not survive layout extraction as rows, so its 14
  rows were transcribed field-by-field into `nodes_SubmissionDocumentationElement.csv` (guidance
  section references and IDE-submission column preserved verbatim). The prose introducing the table
  is in the `APP4` node text; the table itself is not repeated there.
- `nodes_StatutoryProvision.csv` holds the guidance's own verbatim quotations of, and statements
  about, each provision — it is not an extract of the statutes themselves.
- Sections I, II, III and the front matter (preface, public comment, additional copies, table of
  contents) are captured as body text / document attributes; the table of contents is not
  duplicated as nodes.
- No content was added from outside the document. Where the document says nothing, cells are empty.
