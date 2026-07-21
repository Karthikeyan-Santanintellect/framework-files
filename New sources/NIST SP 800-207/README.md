# NIST SP 800-207 — Zero Trust Architecture — knowledge-graph CSVs

**Source document:** NIST Special Publication 800-207, *Zero Trust Architecture*, Scott Rose,
Oliver Borchert, Stu Mitchell, Sean Connelly. National Institute of Standards and Technology,
**August 2020**, 59 pages. DOI https://doi.org/10.6028/NIST.SP.800-207.
PDF: `KB 2/USA/NIST.SP.800-207.pdf`. Extracted from a `pdftotext -layout` text rendering.

## Schema and why

SP 800-207 is a conceptual architecture document, not a control catalog, so a generic
Domain → Control → Enhancement schema would misrepresent it. The schema mirrors the document's
own structure and vocabulary: a numbered section/subsection spine, plus first-class node types
for each of the enumerated constructs the document actually defines (tenets, network-view
assumptions, logical components, approach variations, deployment models, trust-algorithm inputs
and variations, network requirements, use cases, threats, federal-guidance interactions,
migration steps, candidate-solution criteria, and Appendix B gaps).

Clause-level depth: every numbered/lettered enumerated item that carries substantive content is
its own row (each of the seven tenets, each of the six network assumptions, each of the ten
network requirements, each 3.1.x / 3.2.x / 4.x / 5.x / 6.x / 7.3.x subsection), with the full
verbatim text of that item. Subsections that are already represented by a typed node
(e.g. 4.1 as a `UseCase`, 5.3 as a `Threat`) are not duplicated in `nodes_Section.csv`; they hang
off their parent section via their typed relationship and carry a `clause` column.

### Node types
| File | Rows | Contents |
|---|---|---|
| nodes_Publication.csv | 1 | Title, series, publication date (August 2020), authors, DOI, citation, abstract, keywords, audience |
| nodes_Section.csv | 20 | Numbered sections 1–7 and untyped subsections (1.1–1.2, 2.1–2.2, 3.1–3.4.1, 7.1–7.3) with verbatim body text |
| nodes_Tenet.csv | 7 | The seven zero trust basic tenets (§2.1), statement + full verbatim text |
| nodes_NetworkAssumption.csv | 6 | The six network-connectivity assumptions of a zero trust view of a network (§2.2) |
| nodes_LogicalComponent.csv | 11 | Core components PE, PA, PEP plus the eight supporting data sources (CDM, industry compliance, threat intel feeds, activity logs, data access policies, PKI, ID management, SIEM) (§3) |
| nodes_Approach.csv | 3 | ZTA approach variations §3.1.1–3.1.3 |
| nodes_DeploymentModel.csv | 4 | Deployed variations of the abstract architecture §3.2.1–3.2.4 |
| nodes_TrustAlgorithmInput.csv | 5 | Trust algorithm inputs (§3.3) |
| nodes_TrustAlgorithmVariation.csv | 2 | Criteria- vs score-based; singular vs contextual (§3.3.1) |
| nodes_NetworkRequirement.csv | 10 | Network requirements to support ZTA (§3.4.1) |
| nodes_UseCase.csv | 5 | Deployment scenarios/use cases §4.1–4.5 |
| nodes_Threat.csv | 7 | Threats associated with ZTA §5.1–5.7 |
| nodes_FederalGuidanceInteraction.csv | 7 | Interactions with existing federal guidance §6.1–6.7 |
| nodes_MigrationStep.csv | 7 | Steps to introducing ZTA §7.3.1–7.3.7, with step order |
| nodes_SolutionCriterion.csv | 5 | The five candidate-solution evaluation questions (§7.3.5) |
| nodes_Definition.csv | 8 | Defined terms with verbatim definitions: zero trust (ZT), zero trust architecture (ZTA), zero trust enterprise, implicit trust zone, trust algorithm (TA), control plane, data plane, security fatigue |
| nodes_Appendix.csv | 2 | Appendix A (Acronyms) and Appendix B (Identified Gaps), with Appendix B's introductory finding |
| nodes_Acronym.csv | 21 | Appendix A acronym list |
| nodes_Gap.csv | 11 | Appendix B gap categories and individual gaps B.1–B.4.7 |
| nodes_Figure.csv | 13 | The 12 figures plus Table B-1 (labels and captions) |
| nodes_Reference.csv | 29 | Main reference list (24) and Appendix B.5 references (5) |

### Relationship types
| File | Rows | Meaning |
|---|---|---|
| rels_HAS_SECTION.csv | 7 | Publication → top-level Section |
| rels_HAS_SUBSECTION.csv | 13 | Section → Subsection |
| rels_DEFINES_TENET.csv | 7 | §2.1 → Tenet |
| rels_STATES_ASSUMPTION.csv | 6 | §2.2 → NetworkAssumption |
| rels_DEFINES_COMPONENT.csv | 11 | §3 → LogicalComponent (note = core / data source) |
| rels_DESCRIBES_APPROACH.csv | 3 | §3.1 → Approach |
| rels_DESCRIBES_DEPLOYMENT_MODEL.csv | 4 | §3.2 → DeploymentModel |
| rels_HAS_TA_INPUT.csv | 5 | §3.3 → TrustAlgorithmInput |
| rels_HAS_TA_VARIATION.csv | 2 | §3.3.1 → TrustAlgorithmVariation |
| rels_STATES_NETWORK_REQUIREMENT.csv | 10 | §3.4.1 → NetworkRequirement |
| rels_DESCRIBES_USE_CASE.csv | 5 | §4 → UseCase |
| rels_IDENTIFIES_THREAT.csv | 7 | §5 → Threat |
| rels_ADDRESSES_GUIDANCE.csv | 7 | §6 → FederalGuidanceInteraction |
| rels_HAS_MIGRATION_STEP.csv | 7 | §7.3 → MigrationStep (note = step order) |
| rels_HAS_SOLUTION_CRITERION.csv | 5 | §7.3.5 → SolutionCriterion |
| rels_DEFINES_TERM.csv | 8 | Publication → Definition (note = clause) |
| rels_HAS_APPENDIX.csv | 2 | Publication → Appendix |
| rels_DEFINES_ACRONYM.csv | 21 | Appendix A → Acronym |
| rels_IDENTIFIES_GAP.csv | 11 | Appendix B → Gap (note = category) |
| rels_CONTAINS_FIGURE.csv | 13 | Publication → Figure / Table |
| rels_CITES_REFERENCE.csv | 29 | Publication → Reference (note = References or B.5) |

Totals: 21 node files (184 nodes), 21 relationship files (183 relationships).

## Caveats and gaps
- SP 800-207 is **guidance**, not a statute or a control catalog. It contains no penalties,
  deadlines, thresholds or mandatory requirements; those columns therefore do not exist. The
  "network requirements" of §3.4.1 are architectural preconditions, not legal obligations.
- **Figures carry substantive content that cannot be extracted from text.** Figures 1–12
  (e.g. Figure 2 "Core Zero Trust Logical Components", Figure 7 "Trust Algorithm Input",
  Figure 12 "ZTA Deployment Cycle") are images in the PDF; only labels and captions are captured.
- **Table B-1** ("Summary of Identified Deployment Gaps") is a three-column layout table whose
  cells interleave unreliably in the `-layout` text extract; it is recorded as a node with its
  caption only. Its content is fully represented in prose by the `nodes_Gap.csv` rows (B.2.1,
  B.2.2, B.3.3, B.3.4, B.4.5, B.4.6, B.4.7).
- Appendix B's numbering in the source is irregular (B.3 is followed by B.3.3/B.3.4, and B.4 by
  B.4.5–B.4.7); the document's own numbering is preserved verbatim rather than corrected.
- Section bodies exclude figure captions, running headers/footers, page numbers and footnote
  lines (footnote URLs), which are page-layout artifacts of the extract. Footnote-marker digits
  that were inlined into sentences by `pdftotext` (e.g. "John Kindervag 1") remain as in the
  source.
- Only terms the document explicitly defines are in `nodes_Definition.csv`; descriptive passages
  about "subject", "resource", etc. are left inside their section text rather than promoted to
  definitions.
