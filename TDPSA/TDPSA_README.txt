Texas Data Privacy and Security Act (TDPSA) Neo4j Graph Data Model - CSV Files Summary
=======================================================================================

Texas Data Privacy and Security Act - Consumer Privacy & Business Compliance Model
Effective Date: July 1, 2024 (Universal Opt-Out: January 1, 2025)

NODE CSV FILES (13 files):
----------------------------
1. TDPSA_BusinessEntity_nodes.csv - Organizations subject to TDPSA (6 nodes)
2. TDPSA_Consumer_nodes.csv - Texas residents (7 nodes)
3. TDPSA_PersonalData_nodes.csv - Data categories collected (8 nodes)
4. TDPSA_SensitiveData_nodes.csv - Data requiring explicit consent (6 nodes)
5. TDPSA_ProcessingActivity_nodes.csv - Data processing operations (6 nodes)
6. TDPSA_Consent_nodes.csv - Consumer consent records (6 nodes)
7. TDPSA_PrivacyNotice_nodes.csv - Privacy policies and notices (4 nodes)
8. TDPSA_DataProtectionAssessment_nodes.csv - Risk assessments (5 nodes)
9. TDPSA_ConsumerRequest_nodes.csv - Consumer rights requests (6 nodes)
10. TDPSA_DataProcessor_nodes.csv - Service providers processing data (4 nodes)
11. TDPSA_DataBreach_nodes.csv - Unauthorized data access incidents (3 nodes)
12. TDPSA_OptOutMechanism_nodes.csv - Consumer opt-out tools (3 nodes)
13. TDPSA_ComplianceAudit_nodes.csv - Compliance reviews and audits (4 nodes)

Total Nodes: 68

RELATIONSHIP CSV FILES (13 files):
-----------------------------------
1. TDPSA_PROCESSES_CONSUMER_DATA_relationships.csv - Data processing (6)
2. TDPSA_COLLECTS_PERSONAL_DATA_relationships.csv - Data collection (6)
3. TDPSA_PROCESSES_SENSITIVE_DATA_relationships.csv - Sensitive data processing (4)
4. TDPSA_OBTAINS_CONSENT_relationships.csv - Consent management (6)
5. TDPSA_CONDUCTS_PROCESSING_ACTIVITY_relationships.csv - Processing activities (6)
6. TDPSA_REQUIRES_DATA_PROTECTION_ASSESSMENT_relationships.csv - DPA requirements (4)
7. TDPSA_RESPONDS_TO_CONSUMER_REQUEST_relationships.csv - Consumer responses (6)
8. TDPSA_USES_DATA_PROCESSOR_relationships.csv - Processor relationships (4)
9. TDPSA_OFFERS_PRIVACY_NOTICE_relationships.csv - Privacy notice provision (4)
10. TDPSA_PROVIDES_OPT_OUT_MECHANISM_relationships.csv - Opt-out mechanisms (6)
11. TDPSA_EXPERIENCES_DATA_BREACH_relationships.csv - Breach incidents (3)
12. TDPSA_UNDERGOES_COMPLIANCE_AUDIT_relationships.csv - Audit participation (4)
13. TDPSA_EXERCISES_CONSUMER_RIGHT_relationships.csv - Consumer rights (6)

Total Relationships: 59

═══════════════════════════════════════════════════════════════════════

KEY CONCEPTS
═══════════════════════════════════════════════════════════════════════

Applicability:
- Applies to for-profit entities conducting business in Texas
- Processes data of Texas consumers OR residents
- No size threshold - all businesses must comply
- Not limited to Texas residents

Exemptions:
- Financial institutions regulated by GLBA
- Healthcare entities covered by HIPAA
- Nonprofit organizations
- Educational institutions
- Electric utilities
- SBA-defined small businesses (for most requirements)
- Special exemptions for legal compliance

Consumer Rights:
- Right to Confirm: Confirm whether data is collected/processed
- Right to Access: Obtain personal data collected about them
- Right to Correct: Correct inaccurate data
- Right to Delete: Request deletion of personal data
- Right to Portability: Get data in portable format
- Right to Opt-Out: Refuse sale/targeted ads/profiling (Jan 1, 2025)
- Right to Appeal: Challenge business decision

Data Controller vs. Data Processor:
- Controller: Determines purposes and means of processing
- Processor: Processes data on behalf of controller
- Requires written contract (DPA equivalent)

Sensitive Personal Information:
- Racial origin; Religious beliefs; Health diagnosis
- Sexual orientation; Citizenship status
- Genetic or biometric data for identification
- Precise geolocation (within 1750 feet)
- Children's data (under 13 requires parental consent)

Consumer Request Response:
- 45 calendar days to respond without undue delay
- Extensions possible if reasonably necessary (additional 45 days)
- Free responses at least twice per calendar year per consumer
- Can charge for excessive/repetitive/frivolous requests
- Must provide in portable format if requested
- No fees for access, deletion, correction requests

Data Protection Assessment (DPA):
- Required for:
  * Targeted advertising
  * Data sale activities
  * Profiling operations
  * Sensitive data processing
  * High-risk processing
- Must document benefits vs. risks
- Must consider deidentification and aggregation
- Must evaluate consumer expectations
- Available for Attorney General review

Privacy Notice Requirements:
- Clear, accessible, conspicuous disclosure
- Categories of personal data collected
- Processing purposes
- Third-party sharing information
- Consumer rights and how to exercise
- Appeal process
- Request submission methods
- Sale/targeted ads/profiling notices if applicable

Consent Requirements:
- Explicit opt-in for sensitive data
- Clear affirmative action (no pre-checked boxes)
- No dark patterns or manipulation
- Freely given, specific, informed consent
- Parental/guardian consent for children under 13
- Right to withdraw consent

Opt-Out Mechanism (Effective Jan 1, 2025):
- Must support Global Privacy Control (GPC) signal
- One request covers: targeted ads, data sale, profiling
- Effective within 45 days
- Free to consumer
- Revocable by consumer
- No account required to opt-out

Breach Notification:
- Notify without unreasonable delay
- Notification to Texas Attorney General (if more than small number)
- Offer credit monitoring if financial data exposed
- Document breach in writing

Processor Requirements:
- Clear written processing instructions
- Confidentiality obligations on all staff
- Subprocessor restrictions
- Conforming subprocessor contracts
- Data deletion/return upon termination
- Cooperation with assessments
- Audit and inspection rights

Exemptions for Processing:
- Compliance with law/regulation
- Legal claims/defense
- Safety/security/fraud prevention
- Government-requested disclosure
- Service delivery per contract
- Services provided at consumer request

Enforcement:
- Authority: Texas Attorney General exclusively
- No private right of action
- 30-day cure period after notice
- Penalties: Up to $7,500 per violation
- Injunctive relief available
- AG investigation costs recoverable

═══════════════════════════════════════════════════════════════════════

TOTAL: 26 CSV files (13 node files + 13 relationship files)

All CSV files are properly formatted and ready for import into Neo4j
using LOAD CSV commands.

Compliance Framework: Texas Business & Commerce Code § 541.001+
Jurisdiction: Texas, USA
Scope: All for-profit entities processing personal data
Effective: July 1, 2024
Universal Opt-Out: January 1, 2025
Enforcement: Attorney General only (no private action)
Response Deadline: 45 days (45-day extension possible)

Document Version: 1.0
Status: Ready for Neo4j Implementation
