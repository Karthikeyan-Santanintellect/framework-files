TISAX Neo4j Graph Data Model - CSV Files Summary
==================================================

Trusted Information Security Assessment Exchange (TISAX)
Automotive Industry Security Assessment Model

NODE CSV FILES (10 files):
---------------------------
1. TISAX_Organization_nodes.csv - Automotive suppliers, OEMs, service providers (5 nodes)
2. TISAX_AssessmentLevel_nodes.csv - Maturity levels AL1, AL2, AL3 (3 nodes)
3. TISAX_Assessment_nodes.csv - Assessment process instances (6 nodes)
4. TISAX_AssessmentObjective_nodes.csv - The 12 canonical TISAX assessment objectives / labels (12 nodes)
5. TISAX_AuditProvider_nodes.csv - TISAX-accredited audit firms (4 nodes)
6. TISAX_ISACatalogue_nodes.csv - Assessment criteria catalogues (3 nodes)
7. TISAX_ControlQuestion_nodes.csv - Specific security control questions (8 nodes)
8. TISAX_ProtectionObject_nodes.csv - Assets requiring protection (5 nodes)
9. TISAX_Participant_nodes.csv - Organizations exchanging results (4 nodes)
10. TISAX_AssessmentResult_nodes.csv - Assessment outcomes and certifications (3 nodes)

Total Nodes: 46

RELATIONSHIP CSV FILES (11 files):
----------------------------------
1. TISAX_REGISTERS_IN_TISAX_relationships.csv - Organization registration (5 relationships)
2. TISAX_UNDERGOES_ASSESSMENT_relationships.csv - Assessment instances (6 relationships)
3. TISAX_SELECTS_ASSESSMENT_LEVEL_relationships.csv - Level selection (5 relationships)
4. TISAX_CHOOSES_AUDIT_PROVIDER_relationships.csv - Provider selection (5 relationships)
5. TISAX_SUBJECT_TO_ISA_CATALOGUE_relationships.csv - Catalogue applicability (6 relationships)
6. TISAX_CONTAINS_ASSESSMENT_OBJECTIVE_relationships.csv - Objectives in assessments (6 relationships)
7. TISAX_PROTECTS_OBJECT_relationships.csv - Asset protection mapping (5 relationships)
8. TISAX_ANSWERS_CONTROL_QUESTION_relationships.csv - Control question responses (5 relationships)
9. TISAX_MEETS_CRITERIA_relationships.csv - Criteria verification (3 relationships)
10. TISAX_PARTICIPATES_IN_EXCHANGE_relationships.csv - Exchange participation (4 relationships)
11. TISAX_SHARES_RESULTS_WITH_relationships.csv - Result sharing between orgs (4 relationships)

Total Relationships: 54

═══════════════════════════════════════════════════════════════════════

KEY CONCEPTS
═══════════════════════════════════════════════════════════════════════

Assessment Levels:
- AL1: Basic security assessment (self-assessment allowed)
- AL2: Moderate security assessment (third-party audit required)
- AL3: Advanced security assessment (full external audit required)

ISA Catalogues (the ISA has three criteria catalogues by topic, per Handbook 5.2.2.1):
- ISA-001: Information Security
- ISA-002: Prototype Protection
- ISA-003: Data Protection

Protection Levels:
- Basic: Minimal protection measures
- Standard: Industry-standard protections
- High: Enhanced security controls
- Maximum: Complete protection with encryption

Assessment Scope:
- StandardScope: Predefined assessment criteria
- CustomScope: Tailored assessment requirements

═══════════════════════════════════════════════════════════════════════

TOTAL: 21 CSV files (10 node files + 11 relationship files)

All CSV files are properly formatted and ready for import into Neo4j
using LOAD CSV commands.

Assessment Validity: Typically 3 years from certification date
Audit Provider Accreditation: Required for AL2 and AL3 assessments
Compliance Coverage: ISO 27001, ISO 27002, BSI IT-Grundschutz alignment

Document Version: 1.1
Status: Ready for Neo4j Implementation

═══════════════════════════════════════════════════════════════════════
DATA PROVENANCE / CORRECTIONS (grounded in TISAX Participant Handbook 2.8,
ENX doc ID 602)
═══════════════════════════════════════════════════════════════════════

Framework-layer (authoritative, sourced from the handbook):
- TISAX_AssessmentObjective_nodes.csv: the 12 canonical assessment
  objectives / TISAX labels (Handbook Table 3, p.33). Attributes
  isa_criteria_catalogues from Table 7 (p.58-59), assessment_level from
  Table 5 (p.39), catalogue_group from the color coding.
- TISAX_LABEL_HIERARCHY_relationships.csv (NEW): the label superset
  hierarchy from Handbook 5.4.14.1, p.98 (e.g. "Info high" superset of
  "Confidential"/"High availability"; "Very high availability" superset of
  "High availability"; "Special data" superset of "Data").
- TISAX_ISACatalogue_nodes.csv: the three ISA criteria catalogues by topic
  (Information Security, Prototype Protection, Data Protection), Handbook
  5.2.2.1, p.58. Fabricated versions/URLs/question-counts removed.
- TISAX_AssessmentLevel_nodes.csv: AL1/AL2/AL3 attributes from Handbook
  4.3.3.5 / Table 6 (p.40-42). 3-year label validity retained (5.4.14.2).
  Note: the VDA ISA control catalog is a separate document and is
  intentionally NOT modeled here.

SYNTHETIC / FICTIONAL instance data (NOT from the handbook - illustrative
only, flagged for review):
- Organizations, audit providers, participants, assessments, results,
  findings, and all instance-level relationship rows (ASS-xxx, ORG-xxx,
  PO-xxx, CQ-xxx, etc.) contain invented organisation/auditor names,
  dates, and metrics.
- Instance relationship rows that reference OBJ-xxx and ISA-xxx IDs
  (e.g. TISAX_CONTAINS_ASSESSMENT_OBJECTIVE, TISAX_ISA_CATALOGUE,
  TISAX_ISA_CONTAINS_QUESTIONS) still resolve to valid node IDs but their
  pairings, counts, weights and dates are synthetic and were not corrected.
