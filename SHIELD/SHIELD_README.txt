New York SHIELD Act Neo4j Graph Data Model - CSV Files Summary
====================================================================

New York Stop Hacks and Improve Electronic Data Security (SHIELD) Act
Security & Breach Notification Compliance Model

Effective Date: November 1, 2023
Amendment Effective: December 2024 (30-day notification)
Implementation Deadline: March 21, 2025

NODE CSV FILES (13 files):
----------------------------
1. SHIELD_DataController_nodes.csv - Organizations holding NY resident data (6 nodes)
2. SHIELD_NYResident_nodes.csv - New York residents (7 nodes)
3. SHIELD_PrivateInformation_nodes.csv - Sensitive data types (6 nodes)
4. SHIELD_DataBreach_nodes.csv - Breach incidents (3 nodes)
5. SHIELD_SecurityProgram_nodes.csv - Data security programs (4 nodes)
6. SHIELD_AdministrativeSafeguard_nodes.csv - Admin controls (5 nodes)
7. SHIELD_TechnicalSafeguard_nodes.csv - Technical security (5 nodes)
8. SHIELD_ServiceProvider_nodes.csv - Third-party vendors (4 nodes)
9. SHIELD_NotificationProcess_nodes.csv - Breach notifications (3 nodes)
10. SHIELD_SecurityPolicy_nodes.csv - Security policies (4 nodes)
11. SHIELD_EmployeeTraining_nodes.csv - Staff training programs (3 nodes)
12. SHIELD_IncidentResponse_nodes.csv - Breach response activities (5 nodes)
13. SHIELD_ComplianceAssessment_nodes.csv - Compliance audits (3 nodes)

Total Nodes: 58

RELATIONSHIP CSV FILES (13 files):
-----------------------------------
1. SHIELD_OWNS_LICENSES_PRIVATE_INFORMATION_relationships.csv - Data ownership (6)
2. SHIELD_HOLDS_PERSONAL_DATA_OF_relationships.csv - Data holding (6)
3. SHIELD_IMPLEMENTS_SECURITY_PROGRAM_relationships.csv - Program implementation (4)
4. SHIELD_DETECTS_DATA_BREACH_relationships.csv - Breach detection (3)
5. SHIELD_NOTIFIES_AFFECTED_INDIVIDUAL_relationships.csv - Individual notification (3)
6. SHIELD_MANAGES_THIRD_PARTY_relationships.csv - Vendor management (4)
7. SHIELD_APPLIES_SAFEGUARDS_TO_relationships.csv - Safeguard application (6)
8. SHIELD_CONDUCTS_RISK_ASSESSMENT_relationships.csv - Risk assessments (4)
9. SHIELD_PROVIDES_TRAINING_TO_relationships.csv - Training delivery (6)
10. SHIELD_REPORTS_TO_GOVERNMENT_relationships.csv - Government reporting (2)
11. SHIELD_ENFORCES_POLICY_relationships.csv - Policy enforcement (4)
12. SHIELD_UNDERGOES_COMPLIANCE_ASSESSMENT_relationships.csv - Compliance reviews (3)
13. SHIELD_COMBINES_WITH_DATA_ELEMENT_relationships.csv - Data combinations (4)

Total Relationships: 46

═══════════════════════════════════════════════════════════════════════

KEY CONCEPTS
═══════════════════════════════════════════════════════════════════════

Applicability:
- ANY person or business in NY or operating in NY
- Collects, maintains, or licenses private information
- No size thresholds or exemptions for location
- Applies even if entity is not based in NY

Scope Expansion (December 2024 - Effective March 21, 2025):
- Expands definition of "private information"
- Adds new data elements requiring protection
- Strengthens security requirements

Private Information Definition:
- COMBINATION of Personal Information WITH any:
  * Social Security Number
  * Driver's License or State ID Number
  * Financial Account Number + Access Credentials
  * Biometric Information for ID
  * Email/Username + Password/Security Answer

Personal Information Includes:
- First and last name
- Address
- Telephone number
- Email address

Key Amendments (December 2024):
1. 30-Day Breach Notification Requirement (was "without unreasonable delay")
2. NYSDFS Reporting Obligations for regulated entities
3. Expanded definition of private information (effective March 21, 2025)
4. Greater emphasis on reasonable safeguards
5. Enhanced government notification requirements

Required Security Safeguards:
- Administrative: Risk assessment, policies, training, vendor mgmt
- Technical: Encryption, MFA, monitoring, access controls
- Physical: Access controls, secure storage, destruction procedures

Administrative Safeguards:
- Annual risk assessment (minimum)
- Data security policies and procedures
- Employee security training program
- Third-party service provider management
- Incident response plan with 30-day notification timeline

Technical Safeguards:
- Encryption for data at rest and in transit
- Multi-factor authentication for admin access
- Network monitoring and intrusion detection
- Access controls and least privilege
- Regular vulnerability assessments

Physical Safeguards:
- Facility access controls
- Secure data storage and disposal
- Visitor management policies
- Environmental controls (fire, climate)
- Chain of custody maintenance

Service Provider Requirements:
- Written security agreement required
- Must address data security obligations
- Audit rights reserved
- Must comply with SHIELD requirements
- Regular security assessments required

Breach Notification Timeline:
- DISCOVERY: When breach is identified
- NOTIFICATION DEADLINE: Within 30 days of discovery
- INVESTIGATION: Must determine scope
- GOVERNMENT NOTIFICATION: NYSAG + NYSDFS (if regulated)
- RESIDENT NOTIFICATION: Required if breach involves private info

Notification Requirements:
- Email, mail, phone, or public notice
- Information about breach type
- Data elements involved
- Steps affected residents should take
- Contact information for more details
- Credit monitoring information (if financial data)
- Available to NY Attorney General

Enforcement Authority:
- New York Attorney General (NYSAG)
- New York Department of Financial Services (NYSDFS)
- Exclusive government enforcement
- No private right of action for residents

Penalties:
- $20 per failed notification (up from $10)
- Maximum: $250,000 per violation
- Actual damages for negligent violations
- $5,000 per failure to implement safeguards
- 3-year statute of limitations (6 years if concealed)

Equivalent Compliance:
- If complying with GLBA, HIPAA, or NYDFS requirements
- SHIELD compliance may be deemed satisfied
- Otherwise must follow SHIELD-specific requirements

Data Retention:
- Keep only as long as necessary
- Regular review and deletion
- Secure destruction procedures
- Documentation of destruction

Reporting Requirements:
- All breaches to NY Attorney General (no threshold)
- Breaches affecting 5000+ residents: Consumer reporting agencies
- NYSDFS regulated entities: Additional NYSDFS reporting
- Investigation completion: Final report to NYSAG

═══════════════════════════════════════════════════════════════════════

TOTAL: 26 CSV files (13 node files + 13 relationship files)

All CSV files are properly formatted and ready for import into Neo4j
using LOAD CSV commands.

Compliance Framework: New York General Business Law § 899-aa & 899-bb
Jurisdiction: New York, USA (applies to any entity serving NY residents)
Status: Effective November 1, 2023
Amendment Status: December 2024 (30-day notification mandate)
Implementation: March 21, 2025 (expanded definition)
Enforcement: Attorney General only (no private action)
Notification Deadline: 30 days from discovery

Document Version: 1.0
Status: Ready for Neo4j Implementation
