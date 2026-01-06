Colorado Privacy Act (CPA) Neo4j Graph Data Model - CSV Files Summary
======================================================================

Colorado Privacy Act - Consumer Data Rights & Business Compliance Model
Effective Date: July 1, 2023

NODE CSV FILES (12 files):
---------------------------
1. CPA_DataController_nodes.csv - Organizations processing consumer data (5 nodes)
2. CPA_Consumer_nodes.csv - Colorado residents (7 nodes)
3. CPA_PersonalData_nodes.csv - Data categories collected (8 nodes)
4. CPA_SensitiveData_nodes.csv - Special category data requiring consent (5 nodes)
5. CPA_DataProcessor_nodes.csv - Service providers processing data (4 nodes)
6. CPA_ProcessingActivity_nodes.csv - Specific processing operations (6 nodes)
7. CPA_Consent_nodes.csv - Consumer consent records (6 nodes)
8. CPA_DataProtectionAssessment_nodes.csv - Risk assessments for processing (5 nodes)
9. CPA_ConsumerRequest_nodes.csv - Consumer rights requests (6 nodes)
10. CPA_DataBreach_nodes.csv - Unauthorized data access incidents (3 nodes)
11. CPA_PrivacyNotice_nodes.csv - Required privacy disclosures (4 nodes)
12. CPA_OptOutMechanism_nodes.csv - Consumer opt-out tools (3 nodes)

Total Nodes: 62

RELATIONSHIP CSV FILES (10 files):
----------------------------------
1. CPA_COLLECTS_PERSONAL_DATA_relationships.csv - Data collection (5)
2. CPA_PROCESSES_PERSONAL_DATA_relationships.csv - Data processing (6)
3. CPA_SHARES_WITH_PROCESSOR_relationships.csv - Processor agreements (4)
4. CPA_OBTAINS_CONSENT_relationships.csv - Consent management (5)
5. CPA_RESPONDS_TO_REQUEST_relationships.csv - Consumer request responses (5)
6. CPA_CONDUCTS_DATA_PROTECTION_ASSESSMENT_relationships.csv - DPA conduct (5)
7. CPA_IMPLEMENTS_SECURITY_MEASURES_relationships.csv - Security controls (5)
8. CPA_REPORTS_DATA_BREACH_relationships.csv - Breach reporting (3)
9. CPA_ENFORCES_OPT_OUT_relationships.csv - Opt-out enforcement (4)
10. CPA_PROVIDES_PRIVACY_NOTICE_relationships.csv - Privacy notices (4)

Total Relationships: 46

═══════════════════════════════════════════════════════════════════════

KEY CONCEPTS
═══════════════════════════════════════════════════════════════════════

Applicability Threshold:
- Processes data of 100,000+ Colorado residents annually, OR
- Derives revenue from sale of personal data of 25,000+ Colorado residents

Consumer Rights (CPA § 6-1-1304):
- Right to Know: Access personal data collected
- Right to Delete: Request deletion of personal data
- Right to Correct: Correct inaccurate data
- Right to Portability: Obtain data in portable format
- Right to Opt-Out: Refuse sale/targeted advertising/profiling

Data Controller vs. Data Processor:
- Controller: Determines purposes and means of processing
- Processor: Processes data on behalf of controller

Sensitive Personal Information (CPA § 6-1-1303):
- Health information and medical records
- Social Security numbers
- Financial account and payment information
- Precise geolocation data
- Biometric identifiers (fingerprints, facial recognition)
- Children's data (under 18)
- Genetic information
- Ethnic origin, religious beliefs, union membership

Consent Requirements:
- Freely given, specific, informed, and unambiguous
- Obtained through clear affirmative action (not inaction)
- Separate consent for different purposes
- Cannot condition service on unnecessary data sharing
- No dark patterns allowed

Response Timeline:
- 45 calendar days to respond to consumer requests
- No fee for access/deletion/correction unless frivolous/excessive
- Portable format must be machine-readable (JSON, CSV, etc.)

Data Protection Assessment (DPA):
- Required for high-risk processing:
  * Targeted advertising
  * Sale of data
  * Sensitive data processing
  * Automated decision-making
  * Certain profiling activities
- Must document benefits, risks, and mitigations
- Must be available for Attorney General review

Opt-Out Mechanisms:
- Clear, easy-to-use method to opt out
- "Do Not Track" signals must be honored
- Single request covers all purposes
- Opt-out must be effective within 45 days
- No account required for opt-out

Breach Notification:
- Required if sensitive personal data exposed
- Notify without unreasonable delay
- Notification to Colorado AG if affects 250+ residents
- Must offer credit monitoring if financial data exposed

Processor Agreements (DPA):
- Required for all data processors
- Must include:
  * Processing instructions
  * Security requirements
  * Data return/deletion clause
  * Audit rights
  * Subprocessor restrictions

Penalties and Enforcement:
- Enforcement: Colorado Attorney General & District Attorneys
- Civil Penalties: $2,000 - $20,000 per violation
- Initial 60-day cure period
- No private right of action (government enforcement only)
- Enhanced penalties for violations affecting minors

Compliance Status Levels:
- Compliant: Full CPA implementation
- Partially Compliant: Some requirements met
- Non-Compliant: Significant gaps
- Under Review: Pending assessment

═══════════════════════════════════════════════════════════════════════

TOTAL: 22 CSV files (12 node files + 10 relationship files)

All CSV files are properly formatted and ready for import into Neo4j
using LOAD CSV commands.

Compliance Framework: Colorado Consumer Privacy Act (SB 21-190)
Jurisdiction: Colorado, USA
Applicability: Any business serving Colorado residents meeting threshold
Enforcement: Colorado Attorney General; District Attorneys
Status: Fully Effective (July 1, 2023)

Document Version: 1.0
Status: Ready for Neo4j Implementation
