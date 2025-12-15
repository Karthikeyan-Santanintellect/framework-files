TISAX Neo4j Graph Data Model - CSV Files Summary
==================================================

Trusted Information Security Assessment Exchange (TISAX)
Automotive Industry Security Assessment Model

NODE CSV FILES (10 files):
---------------------------
1. TISAX_Organization_nodes.csv - Automotive suppliers, OEMs, service providers (5 nodes)
2. TISAX_AssessmentLevel_nodes.csv - Maturity levels AL1, AL2, AL3 (3 nodes)
3. TISAX_Assessment_nodes.csv - Assessment process instances (6 nodes)
4. TISAX_AssessmentObjective_nodes.csv - Security objectives assessed (5 nodes)
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

ISA Catalogues:
- ISA 1: Information Security Fundamentals (180 questions)
- ISA 2: Advanced Security (250 questions)
- ISA 3: Prototype Protection (120 questions)

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

Document Version: 1.0
Status: Ready for Neo4j Implementation
