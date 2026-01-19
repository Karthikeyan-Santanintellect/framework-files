#Regulation


regulation = """
MERGE (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  i.name = "Gramm-Leach-Bliley Act",
  i.version = "1999 (Pub. L. 106-102)",
  i.status = "Active",
  i.jurisdiction = "United States (Federal)",
  i.effective_date = date("1999-11-12"),
  i.enactment_date = date("1999-11-12"),
  i.description = "Federal law that requires financial institutions to explain their information-sharing practices to their customers and to safeguard sensitive data. It includes the Financial Privacy Rule, Safeguards Rule, and pretexting provisions.";
"""

#standard
standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Standard {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  s.name                = row.node_name,
  s.nodeType            = row.node_type,
  s.definition          = row.definition,
  s.officialDescription = row.official_description,
  s.applicableTo        = row.applicable_to,
  s.organizationOwner   = row.organization_owner,
  s.version             = row.version,
  s.status              = row.status,
  s.keyFeatures         = row.key_features;

"""

#Requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  req.name                = row.node_name,
  req.nodeType            = row.node_type,
  req.definition          = row.definition,
  req.officialDescription = row.official_description,
  req.applicableTo        = row.applicable_to,
  req.organizationOwner   = row.organization_owner,
  req.version             = row.version,
  req.status              = row.status,
  req.keyFeatures         = row.key_features;
"""
#Domain
domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  d.name                = row.node_name,
  d.nodeType            = row.node_type,
  d.definition          = row.definition,
  d.officialDescription = row.official_description,
  d.applicableTo        = row.applicable_to,
  d.organizationOwner   = row.organization_owner,
  d.version             = row.version,
  d.status              = row.status,
  d.keyFeatures         = row.key_features;
"""
#Financial Institution
financial_institution = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fi:FinancialInstitution {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  fi.name                = row.node_name,
  fi.nodeType            = row.node_type,
  fi.definition          = row.definition,
  fi.officialDescription = row.official_description,
  fi.applicableTo        = row.applicable_to,
  fi.organizationOwner   = row.organization_owner,
  fi.version             = row.version,
  fi.status              = row.status,
  fi.keyFeatures         = row.key_features;
"""
#NPI
NPI = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (n:NPI {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  n.name                = row.node_name,
  n.nodeType            = row.node_type,
  n.definition          = row.definition,
  n.officialDescription = row.official_description,
  n.applicableTo        = row.applicable_to,
  n.organizationOwner   = row.organization_owner,
  n.version             = row.version,
  n.status              = row.status,
  n.keyFeatures         = row.key_features;
"""
# Privacy Notice
privacy_notice = """
MERGE (pn:PrivacyNotice {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  pn.name                = row.node_name,
  pn.nodeType            = row.node_type,
  pn.definition          = row.definition,
  pn.officialDescription = row.official_description,
  pn.applicableTo        = row.applicable_to,
  pn.organizationOwner   = row.organization_owner,
  pn.version             = row.version,
  pn.status              = row.status,
  pn.keyFeatures         = row.key_features;
"""

#info_sec_program
info_sec_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (isp:InfoSecProgram {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  isp.name                = row.node_name,
  isp.nodeType            = row.node_type,
  isp.definition          = row.definition,
  isp.officialDescription = row.official_description,
  isp.applicableTo        = row.applicable_to,
  isp.organizationOwner   = row.organization_owner,
  isp.version             = row.version,
  isp.status              = row.status,
  isp.keyFeatures         = row.key_features;
"""
#RiskAssessment
risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ra:RiskAssessment {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ra.name                = row.node_name,
  ra.nodeType            = row.node_type,
  ra.definition          = row.definition,
  ra.officialDescription = row.official_description,
  ra.applicableTo        = row.applicable_to,
  ra.organizationOwner   = row.organization_owner,
  ra.version             = row.version,
  ra.status              = row.status,
  ra.keyFeatures         = row.key_features;
"""
#Safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row  
MERGE (s:Safeguard {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  s.name                = row.node_name,
  s.nodeType            = row.node_type,
  s.definition          = row.definition,
  s.officialDescription = row.official_description,
  s.applicableTo        = row.applicable_to,
  s.organizationOwner   = row.organization_owner,
  s.version             = row.version,
  s.status              = row.status,
  s.keyFeatures         = row.key_features;
"""
#Regulator
regulator = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Regulator {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  r.name                = row.node_name,
  r.nodeType            = row.node_type,
  r.definition          = row.definition,
  r.officialDescription = row.official_description,
  r.applicableTo        = row.applicable_to,
  r.organizationOwner   = row.organization_owner,
  r.version             = row.version,
  r.status              = row.status,
  r.keyFeatures         = row.key_features;
"""
#consumer_consumer
consumer_consumer = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:ConsumerCustomer {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  c.name                = row.node_name,
  c.nodeType            = row.node_type,
  c.definition          = row.definition,
  c.officialDescription = row.official_description,
  c.applicableTo        = row.applicable_to,
  c.organizationOwner   = row.organization_owner,
  c.version             = row.version,
  c.status              = row.status,
  c.keyFeatures         = row.key_features;
"""
#Third_party_service
third_party_service = """
MERGE (tps:ThirdPartyService {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  tps.name                = row.node_name,
  tps.nodeType            = row.node_type,
  tps.definition          = row.definition,
  tps.officialDescription = row.official_description,
  tps.applicableTo        = row.applicable_to,
  tps.organizationOwner   = row.organization_owner,
  tps.version             = row.version,
  tps.status              = row.status,
  tps.keyFeatures         = row.key_features;
"""
#internal_role
internal_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:InternalRole {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ir.name                = row.node_name,
  ir.nodeType            = row.node_type,
  ir.definition          = row.definition,
  ir.officialDescription = row.official_description,
  ir.applicableTo        = row.applicable_to,
  ir.organizationOwner   = row.organization_owner,
  ir.version             = row.version,
  ir.status              = row.status,
  ir.keyFeatures         = row.key_features,
"""
#Incident_response
incident_response = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (in:IncidentResponse {id: row.node_id , industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  in.name                = row.node_name,
  in.nodeType            = row.node_type,
  in.definition          = row.definition,
  in.officialDescription = row.official_description,
  in.applicableTo        = row.applicable_to,
  in.organizationOwner   = row.organization_owner,
  in.version             = row.version,
  in.status              = row.status,
  in.keyFeatures         = row.key_features;
  """
#Training 
training = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Training {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  t.name                = row.node_name,
  t.nodeType            = row.node_type,
  t.definition          = row.definition,
  t.officialDescription = row.official_description,
  t.applicableTo        = row.applicable_to,
  t.organizationOwner   = row.organization_owner,
  t.version             = row.version,
  t.status              = row.status,
  t.keyFeatures         = row.key_features;
"""
#Breach Response procedure
breach_response_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (brp:BreachResponseProcedure {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  brp.name                = row.node_name,
  brp.nodeType            = row.node_type,
  brp.definition          = row.definition,
  brp.officialDescription = row.official_description,
  brp.applicableTo        = row.applicable_to,
  brp.organizationOwner   = row.organization_owner,
  brp.version             = row.version,
  brp.status              = row.status,
  brp.keyFeatures         = row.key_features;
"""
#Enforcement mechanisms
enforcement_mechanisms = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:EnforcementMechanisms {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  e.name                = row.node_name,
  e.nodeType            = row.node_type,
  e.definition          = row.definition,
  e.officialDescription = row.official_description,
  e.applicableTo        = row.applicable_to,
  e.organizationOwner   = row.organization_owner,
  e.version             = row.version,
  e.status              = row.status,
  e.keyFeatures         = row.key_features;
"""
#vendor evaluation
vendor_evaluation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ve:VendorEvaluation {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ve.name                = row.node_name,
  ve.nodeType            = row.node_type,
  ve.definition          = row.definition,
  ve.officialDescription = row.official_description,
  ve.applicableTo        = row.applicable_to,
  ve.organizationOwner   = row.organization_owner,
  ve.version             = row.version,
  ve.status              = row.status,
  ve.keyFeatures         = row.key_features;
"""
#Employee personal
employee_personal = """
MERGE (ep:EmployeePersonnel {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ep.name                = row.node_name,
  ep.nodeType            = row.node_type,
  ep.definition          = row.definition,
  ep.officialDescription = row.official_description,
  ep.applicableTo        = row.applicable_to,
  ep.organizationOwner   = row.organization_owner,
  ep.version             = row.version,
  ep.status              = row.status,
  ep.keyFeatures         = row.key_features;
  """
#Compliance Audit
compliance_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ca:ComplianceArtifact {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ca.name                = row.node_name,
  ca.nodeType            = row.node_type,
  ca.definition          = row.definition,
  ca.officialDescription = row.official_description,
  ca.applicableTo        = row.applicable_to,
  ca.organizationOwner   = row.organization_owner,
  ca.version             = row.version,
  ca.status              = row.status,
  ca.keyFeatures         = row.key_features;
"""

#Affiliate
affiliate = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Affiliate {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  a.name                = row.node_name,
  a.nodeType            = row.node_type,
  a.definition          = row.definition,
  a.officialDescription = row.official_description,
  a.applicableTo        = row.applicable_to,
  a.organizationOwner   = row.organization_owner,
  a.version             = row.version,
  a.status              = row.status,
  a.keyFeatures         = row.key_features;
"""
#NewMedia
new_media = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (nm:NewMedia {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  nm.name                = row.node_name,
  nm.nodeType            = row.node_type,
  nm.definition          = row.definition,
  nm.officialDescription = row.official_description,
  nm.applicableTo        = row.applicable_to,
  nm.organizationOwner   = row.organization_owner,
  nm.version             = row.version,
  nm.status              = row.status,
  nm.keyFeatures         = row.key_features;
"""
# Law enforcement
law_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (le:LawEnforcement {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  le.name                = row.node_name,
  le.nodeType            = row.node_type,
  le.definition          = row.definition,
  le.officialDescription = row.official_description,
  le.applicableTo        = row.applicable_to,
  le.organizationOwner   = row.organization_owner,
  le.version             = row.version,
  le.status              = row.status,
  le.keyFeatures         = row.key_features;
"""
# Identity Protection
identity_protection = """
MERGE (ip:IdentityProtection {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ip.name                = row.node_name,
  ip.nodeType            = row.node_type,
  ip.definition          = row.definition,
  ip.officialDescription = row.official_description,
  ip.applicableTo        = row.applicable_to,
  ip.organizationOwner   = row.organization_owner,
  ip.version             = row.version,
  ip.status              = row.status,
  ip.keyFeatures         = row.key_features;
"""

# Background check agency
background_check_agency = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bca:BackgroundCheckAgency {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  bca.name                = row.node_name,
  bca.nodeType            = row.node_type,
  bca.definition          = row.definition,
  bca.officialDescription = row.official_description,
  bca.applicableTo        = row.applicable_to,
  bca.organizationOwner   = row.organization_owner,
  bca.version             = row.version,
  bca.status              = row.status,
  bca.keyFeatures         = row.key_features;
"""
# Service provider Agreement
service_provider_agreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (spa:ServiceProviderAgreement {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  spa.name                = row.node_name,
  spa.nodeType            = row.node_type,
  spa.definition          = row.definition,
  spa.officialDescription = row.official_description,
  spa.applicableTo        = row.applicable_to,
  spa.organizationOwner   = row.organization_owner,
  spa.version             = row.version,
  spa.status              = row.status,
  spa.keyFeatures         = row.key_features;
"""

#Pretexting Prevention Procedure
pretexting_prevention_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pp:PretextingPreventionProcedure {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  pp.name                = row.node_name,
  pp.nodeType            = row.node_type,
  pp.definition          = row.definition,
  pp.officialDescription = row.official_description,
  pp.applicableTo        = row.applicable_to,
  pp.organizationOwner   = row.organization_owner,
  pp.version             = row.version,
  pp.status              = row.status,
  pp.keyFeatures         = row.key_features;
"""
# Access Control List
access_control_list = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (acl:AccessControlList {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  acl.name                = row.node_name,
  acl.nodeType            = row.node_type,
  acl.definition          = row.definition,
  acl.officialDescription = row.official_description,
  acl.applicableTo        = row.applicable_to,
  acl.organizationOwner   = row.organization_owner,
  acl.version             = row.version,
  acl.status              = row.status,
  acl.keyFeatures         = row.key_features;
"""
# Breach-Notification-Record
breach_notification_record = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bn:BreachNotificationRecord {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  bn.name                = row.node_name,
  bn.nodeType            = row.node_type,
  bn.definition          = row.definition,
  bn.officialDescription = row.official_description,
  bn.applicableTo        = row.applicable_to,
  bn.organizationOwner   = row.organization_owner,
  bn.version             = row.version,
  bn.status              = row.status,
  bn.keyFeatures         = row.key_features;
"""
# Non-Affiliated-Third-Party
non_affiliated_third_party = """
MERGE (ntp:NonAffiliatedThirdParty {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ntp.name                = row.node_name,
  ntp.nodeType            = row.node_type,
  ntp.definition          = row.definition,
  ntp.officialDescription = row.official_description,
  ntp.applicableTo        = row.applicable_to,
  ntp.organizationOwner   = row.organization_owner,
  ntp.version             = row.version,
  ntp.status              = row.status,
  ntp.keyFeatures         = row.key_features;
"""
#Threat-Intelligence-Provider
threat_intelligence_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ti:ThreatIntelligenceProvider {id: row.node_id, industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  ti.name                = row.node_name,
  ti.nodeType            = row.node_type,
  ti.definition          = row.definition,
  ti.officialDescription = row.official_description,
  ti.applicableTo        = row.applicable_to,
  ti.organizationOwner   = row.organization_owner,
  ti.version             = row.version,
  ti.status              = row.status,
  ti.keyFeatures         = row.key_features;
"""


#Regulation → standard
regulation_standard = """
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Standard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (i)-[:REGULATION_HAS_STANDARD}]->(s);
"""
# Standard -> requirement 
standard_requirement = """
MATCH (s:Standard{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (s)-[:STANDARD_HAS_REQUIREMENT]->(req);
"""
# Requirement -> domain
requirement_domain = """
MATCH (req:Requirement {industry_standard_regulation_id: 'GLBA 1999'})
MATCH (d:Domain {industry_standard_regulation_id: 'GLBA 1999'})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_DOMAIN]->(d);
"""
# Standard -> Domain
standard_domain = """
MATCH (s:Standard{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (d:Domain{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (s)-[:STANDARD_APPLIES_TO_DOMAIN]->(d);
"""
# Regulator -> financial_institution
regulator_financial_institution = """
MATCH (r:Regulator{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REGULATOR_HAS_FINANCIAL_INSTITUTION]->(fi);
"""
# Regulator ->Enforcement_Mechanism
regulator_enforcement_mechanisms = """
MATCH (r:Regulator{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (e:EnforcementMechanisms{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REGULATOR_HAS_ENFORCEMENT_ACTION]->(e);
"""
# Enforecemt -> financial_institution
enforcement_financial_institution = """
MATCH (e:EnforcementMechanisms{industry_standard_regulation_id : 'GLBA 1999'})
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (e)-[:ENFORCEMENT_HAS_FINANCIAL_INSTITUTION]->(fi);
"""
# Fiancial Institution -> consumer_customer
financial_institution_consumer_consumer = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (c:ConsumerCustomer{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FINANCIAL_INSTITUTION_HAS_CONSUMER_CUSTOMER]->(c);
"""
# Consumer_customer -> NPI
consumer_consumer_npi = """
MATCH (c:ConsumerCustomer{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (n:NPI{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (c)-[:CONSUMER_CUSTOMER_HAS_NPI]->(n);
"""
# Requirement -> NPI
requirement_npi = """
MATCH (req:Requirement {industry_standard_regulation_id: 'GLBA 1999'})
MATCH (n:NPI{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_NPI]->(n);
"""
# Safeguard -> NPI
safeguard_npi = """
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (n:NPI{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (s)-[:SAFEGUARD_PROTECTS_NPI]->(n);
"""
# Internal Role -> Infosec program
internal_role_infosec_program ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ir)-[:INTERNAL_ROLE_HAS_INFOSEC_PROGRAM]->(isp);
"""
# Internal Role -> RiskAssessment
internal_role_risk_assessment ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ra:RiskAssessment{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ir)-[:INTERNAL_ROLE_HAS_RISK_ASSESSMENT]->(ra);  
"""
# Internal Role -> Incident Response
internal_role_incident_response ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (in:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ir)-[:INTERNAL_ROLE_HAS_INCIDENT_RESPONSE]->(in);
"""
# Internal Role -> Training
internal_role_training ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ir)-[:INTERNAL_ROLE_RESPONSIBLE_FOR_TRAINING]->(t);
"""
# Employee Personnel -> Internal Role
employee_personnel_internal_role ="""
MATCH (ep:EmployeePersonnel{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ep)-[:EMPLOYEE_PLAYS_INTERNAL_ROLE]->(ir);
"""
# Employee Personnel -> InfosecProgram
employee_personnel_infosec ="""
MATCH (ep:EmployeePersonnel{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ep)-[:EMPLOYEE_PART_OF_INFOSEC_PROGRAM]->(isp);
"""
#Privacy_notice -> Requirement
privacy_notice_requirement = """
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pn)-[:PRIVACY_NOTICE_APPLIES_TO_REQUIREMENT]->(req);
"""
# Privacy_notice -> NPI
privacy_notice_npi = """
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (n:NPI{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pn)-[:PRIVACY_NOTICE_COVERS_TO_NPI]->(n);
"""
# Privacy_notice -> Consumer_customer
privacy_notice_consumer_customer = """
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (c:ConsumerCustomer{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pn)-[:PRIVACY_NOTICE_COVERS_TO_CONSUMER_CUSTOMER]->(c);
"""
# Affiliate -> Privacy_notice
affiliate_privacy_notice = """
MATCH (a:Affiliate{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (a)-[:AFFILIATE_HAS_PRIVACY_NOTICE]->(pn);
"""
#NonAffiliatedThirdParty -> Privacy_notice
non_affiliated_third_party_privacy_notice = """
MATCH (ntp:NonAffiliatedThirdParty{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (n)-[:NON_AFFILIATED_THIRD_PARTY_HAS_PRIVACY_NOTICE]->(pn);
"""
# Infosec_program -> Requirement
infosec_program_requirement = """
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (isp)-[:INFOSEC_PROGRAM_HAS_REQUIREMENT]->(req);
"""
# Risk Assessment -> Infosec_program
risk_assessment_infosec_program = """
MATCH (ra:RiskAssessment{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ra)-[:RISK_ASSESSMENT_HAS_INFOSEC_PROGRAM]->(isp);
"""

# Safeguard -> Requirement
safeguard_requirement = """
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (s)-[:SAFEGUARD_DERIVED_FROM_REQUIREMENT]->(r);
"""

# Safeguard -> RiskAssessment
safeguard_risk_assessment = """
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ra:RiskAssessment{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (s)-[:SAFEGUARD_ADDRESSES_RISK_IDENTIFIED_IN]->(ra);
"""
# Training -> Requirement
training_requirement = """
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (t)-[:TRAINING_SUPPORTS_REQUIREMENT]->(req);
"""

# Training -> Safeguard
training_safeguard = """
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (t)-[:TRAINING_COVERS_SAFEGUARD]->(s);
"""

# Training -> InternalRole
training_internal_role = """
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (t)-[:TRAINING_TARGETS_ROLE]->(ir);
"""

# Training -> InfoSecProgram
training_infosec_program = """
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (t)-[:TRAINING_SUPPORTS_PROGRAM]->(isp);
"""
# FinancialInstitution -> ThirdPartyService
financial_institution_third_party_service = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (tps:ThirdPartyService{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FINANCIAL_INSTITUTION_USES_SERVICE_PROVIDER]->(tps);
"""

# FinancialInstitution -> VendorEvaluation
financial_institution_vendor_evaluation = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ve:VendorEvaluation{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FINANCIAL_ENGAGES_VENDOR]->(ve);
"""

# VendorEvaluation -> ThirdPartyService
vendor_evaluation_third_party_service = """
MATCH (ve:VendorEvaluation{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (tps:ThirdPartyService{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ve)-[:VENDOR_EVALUATES_THIRD_PARTY_SERVICE]->(tps);
"""
# ThirdPartyService -> ServiceProviderAgreement
third_party_service_spa = """
MATCH (tps:ThirdPartyService{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (spa:ServiceProviderAgreement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (tps)-[:THIRD_PARTY_SERVICE_GOVERNED_BY_SERVICE_PROVIDER]->(spa);
"""
# ServiceProviderAgreement -> BackgroundCheckAgency
spa_background_check_agency = """
MATCH (spa:ServiceProviderAgreement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (spa)-[:SERVICE_PROVIDER_AGREEMENT_COVERS_VENDOR]->(bca);
"""

# NonAffiliatedThirdParty -> ThirdPartyService
non_affiliated_third_party_tps = """
MATCH (ntp:NonAffiliatedThirdParty{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (tps:ThirdPartyService{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ntp)-[:NON_AFFILIATED_THIRD_PARTY_USES_INCLUDES_PROVIDER]->(tps);
"""
# NonAffiliatedThirdParty -> BackgroundCheckAgency
non_affiliated_third_party_bca = """
MATCH (ntp:NonAffiliatedThirdParty{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ntp)-[:NON_AFFILIATED_THIRD_PARTY_INCLUDES_PROVIDER]->(bca);
"""

# FinancialInstitution -> Affiliate
financial_institution_affiliate = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (a:Affiliate{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FIANICAL_INSTITUTION_HAS_AFFILIATE]->(a);
"""

# Affiliate -> Requirement (sharing rules)
affiliate_requirement = """
MATCH (a:Affiliate{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (a)-[:AFFILIATE_SHARES_INFORMATION_UNDER_RULES]->(req);
"""

# Affiliate -> PrivacyNotice (opt-out context)
affiliate_privacy_notice_optout = """
MATCH (a:Affiliate{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (a)-[:AFFILIATE_NOTICED_OF_PRIVACY_NOTICE]->(pn);
"""
# NonAffiliatedThirdParty -> PrivacyNotice (opt-out)
non_affiliated_third_party_privacy_notice_optout = """
MATCH (ntp:NonAffiliatedThirdParty{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ntp)-[:NON_AFFILIATED_THIRD_PARTY_NOTICED_OF_PRIVACY_NOTICE]->(pn);
"""

# FinancialInstitution -> BackgroundCheckAgency
financial_institution_background_check_agency = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FIANICAL_INSTITUTION_USES_BACKGROUND_CHECK_PROVIDER]->(bca);
"""

# EmployeePersonnel -> BackgroundCheckAgency
employee_personnel_background_check_agency = """
MATCH (ep:EmployeePersonnel{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ep)-[:EMPLOYEE_PERSONNEL_ENFORCED_BY_BACKGROUND]->(bca);
"""

# ServiceProviderAgreement -> BackgroundCheckAgency (governance)
spa_governs_background_check_agency = """
MATCH (spa:ServiceProviderAgreement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (spa)-[:SPA_GOVERNS_BACKGROUND_CHECK_PROVIDER]->(bca);
"""

# BackgroundCheckAgency -> Requirement
background_check_agency_requirement = """
MATCH (bca:BackgroundCheckAgency{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (bca)-[:BACKGROUND_CHECK_AGENCY_SUBJECT_TO_REQUIREMENT]->(req);
"""

# FinancialInstitution -> LawEnforcement
financial_institution_law_enforcement = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (le:LawEnforcement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FINANCIAL_INSTITUTION_ENFORCED_BY_LAW]->(le);
"""

# IncidentResponse -> LawEnforcement
incident_response_law_enforcement = """
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (le:LawEnforcement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (irsp)-[:INCIDENT_RESPONSE_ENFORCED_BY_LAW]->(le);
"""

# LawEnforcement -> Requirement (exceptions)
law_enforcement_requirement = """
MATCH (le:LawEnforcement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (le)-[:LAW_ENFORECEMENT_HAS_REQUIREMENT]->(req);
"""

# Enforcement -> LawEnforcement
enforcement_law_enforcement = """
MATCH (e:Enforcement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (le:LawEnforcement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (e)-[:ENFORCEMENT_ENFORCED_BY_LAW]->(le);
"""

# IncidentResponse -> InfoSecProgram
incident_response_infosec_program = """
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (irsp)-[:INCIDENT_RESPONSE_PART_OF_PROGRAM]->(isp);
"""

# IncidentResponse -> BreachResponseProcedure
incident_response_breach_response_procedure = """
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (brp:BreachResponseProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (irsp)-[:INCIDENT_RESPONSE_USES_PROCEDURE]->(brp);
"""

# IncidentResponse -> BreachNotificationRecord
incident_response_breach_notification_record = """
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bn:BreachNotificationRecord{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (irsp)-[:INCIDENT_RESPONSE_USES_CREATES_RECORD]->(bn);
"""

# BreachNotificationRecord -> BreachResponseProcedure
breach_notification_record_breach_response_procedure = """
MATCH (bn:BreachNotificationRecord{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (brp:BreachResponseProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (bn)-[:BREACH_NOTIFICATION_USES_PROCEDURE]->(brp);
"""
# IncidentResponse -> NPI
incident_response_npi = """
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (n:NPI{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (irsp)-[:INCIDENT_RESPONSE_PROTECTS_DATA_CATEGORY]->(n);
"""

# BreachNotificationRecord -> IdentityProtection
breach_notification_record_identity_protection = """
MATCH (bn:BreachNotificationRecord{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ip:IdentityProtection{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (bn)-[:BREACH_NOTIFICATION_TRIGGERS_IDENTITY_PROTECTION]->(ip);
"""

# IdentityProtection -> ConsumerCustomer
identity_protection_consumer_customer = """
MATCH (ip:IdentityProtection{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (c:ConsumerCustomer{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ip)-[:IDENTITY_APPLIES_TO_CUSTOMER_TYPE]->(c);
"""

# IdentityProtection -> IncidentResponse
identity_protection_incident_response = """
MATCH (ip:IdentityProtection{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ip)-[:IDENTITY_RESPONDS_TO_INCIDENT]->(irsp);
"""

# IdentityProtection -> Requirement
identity_protection_requirement = """
MATCH (ip:IdentityProtection{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ip)-[:IDENTITY_PROTECTION_IMPLEMENTS_REQUIREMENT]->(req);
"""

# AccessControlList -> Safeguard
access_control_list_safeguard = """
MATCH (acl:AccessControlList{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (acl)-[:ACCESS_CONTROL_SUPPORTS_SAFEGUARD]->(s);
"""

# AccessControlList -> InfoSecProgram
access_control_list_infosec_program = """
MATCH (acl:AccessControlList{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (acl)-[:ACESS_CONTROL_IMPLEMENTED_IN_PROGRAM]->(isp);
"""

# AccessControlList -> Requirement
access_control_list_requirement = """
MATCH (acl:AccessControlList{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (acl)-[:ACCESS_CONTROL_ENFORCES_REQUIREMENT]->(req);
"""

# InternalRole -> AccessControlList
internal_role_access_control_list = """
MATCH (ir:InternalRole{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (acl:AccessControlList{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ir)-[:INTERNAL_ROLE_USES_ACCESS_CONTROL]->(acl);
"""

# PretextingPreventionProcedure -> InfoSecProgram
pretexting_prevention_infosec_program = """
MATCH (pp:PretextingPreventionProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pp)-[:PRETEXTING_PART_OF_PROGRAM]->(isp);
"""

# PretextingPreventionProcedure -> ConsumerCustomer
pretexting_prevention_consumer_customer = """
MATCH (pp:PretextingPreventionProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (c:ConsumerCustomer{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pp)-[:PRETEXTING_PROTECTS_INTERACTIONS_WITH]->(c);
"""

# PretextingPreventionProcedure -> Requirement
pretexting_prevention_requirement = """
MATCH (pp:PretextingPreventionProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (pp)-[:PRETEXTING_PREVENTION_IMPLEMENTS_REQUIREMENT]->(req);
"""

# Training -> PretextingPreventionProcedure
training_pretexting_prevention_procedure = """
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pp:PretextingPreventionProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (t)-[:TRAINING_COVERS_PRETEXTING_PROCEDURE]->(pp);
"""

# NewMedia -> PrivacyNotice
new_media_privacy_notice = """
MATCH (nm:NewMedia{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pn:PrivacyNotice{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (nm)-[:NEW_MEDIA_COVERS_PRIVACY_NOTICE]->(pn);
"""

# NewMedia -> IdentityProtection
new_media_identity_protection = """
MATCH (nm:NewMedia{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ip:IdentityProtection{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (nm)-[:NEW_MEDIA_USES_IDENTITY]->(ip);
"""

# NewMedia -> PretextingPreventionProcedure
new_media_pretexting_prevention_procedure = """
MATCH (nm:NewMedia{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pp:PretextingPreventionProcedure{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (nm)-[:NEW_MEDIA_SUBJECT_TO_PRETEXTING_CONTROLS]->(pp);
"""

# FinancialInstitution -> ThreatIntelligenceProvider
financial_institution_threat_intel = """
MATCH (fi:FinancialInstitution{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ti:ThreatIntelligenceProvider{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (fi)-[:FINANCIAL_INSTITUTION_USES_THREAT_INTEL_]->(ti);
"""

# ThreatIntelligenceProvider -> RiskAssessment
threat_intel_risk_assessment = """
MATCH (ti:ThreatIntelligenceProvider{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ra:RiskAssessment{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ti)-[:THREAT_INTELLIGENCE_PROVIDER_INFORMS_RISK_ASSESSMENT]->(ra);
"""

# ThreatIntelligenceProvider -> Safeguard
threat_intel_safeguard = """
MATCH (ti:ThreatIntelligenceProvider{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ti)-[:THREAT_INTELLIGENCE_PROVIDER_INFORMS_SAFEGUARD]->(s);
"""

# ThreatIntelligenceProvider -> IncidentResponse
threat_intel_incident_response = """
MATCH (ti:ThreatIntelligenceProvider{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (irsp:IncidentResponse{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ti)-[:THREAT_INTELLIGENCE_PROVIDER_INFORMS_INCIDENT_RESPONSE]->(irsp);
"""

# ComplianceArtifact -> Requirement
compliance_artifact_requirement = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (req:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_APPLIES_TO_REQUIREMENTS]->(req);
"""

# ComplianceArtifact -> InfoSecProgram
compliance_artifact_infosec_program = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (isp:InfoSecProgram{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_DOCUMENTS_PROGRAM]->(isp);
"""

# ComplianceArtifact -> Safeguard
compliance_artifact_safeguard = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_DOCUMENTS_SAFEGUARD]->(s);
"""

# ComplianceArtifact -> Training
compliance_artifact_training = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (t:Training{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_DOCUMENTS_TRAINING]->(t);
"""

# ComplianceArtifact -> VendorEvaluation
compliance_artifact_vendor_evaluation = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ve:VendorEvaluation{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_DOCUMENTS_VENDOR_EVALUATION]->(ve);
"""

# ComplianceArtifact -> BreachNotificationRecord
compliance_artifact_breach_notification_record = """
MATCH (ca:ComplianceArtifact{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (bn:BreachNotificationRecord{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ca)-[:COMPLIANCES_ARTIFACT_DOCUMENTS_BREACH_RECORD]->(bn);
"""


import os
import time
import logging
import json
import sys
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading graph structure...")

client.query(regulation)
time.sleep(2)

client.query(standard)
time.sleep(2)

client.query(requirement)
time.sleep(2)

client.query(domain)
time.sleep(2)

client.query(breach_notification_record)
time.sleep(2)

client.query(non_affiliated_third_party)
time.sleep(2)

client.query(threat_intelligence_provider)
time.sleep(2)

client.query(regulator)
time.sleep(2)

client.query(financial_institution)
time.sleep(2)

client.query(safeguard)
time.sleep(2)

client.query(infosec_program)
time.sleep(2)

client.query(training)
time.sleep(2)

client.query(internal_role)
time.sleep(2)

client.query(privacy_notice)
time.sleep(2)

client.query(affiliate)
time.sleep(2)

client.query(vendor_evaluation)
time.sleep(2)

client.query(third_party_service)
time.sleep(2)

client.query(background_check_agency)
time.sleep(2)

client.query(law_enforcement)
time.sleep(2)

client.query(incident_response)
time.sleep(2)

client.query(breach_response_procedure)
time.sleep(2)

client.query(identity_protection)
time.sleep(2)

client.query(access_control_list)
time.sleep(2)

client.query(pretexting_prevention_procedure)
time.sleep(2)

client.query(new_media)
time.sleep(2)

client.query(compliance_artifact)
time.sleep(2)

client.query(employee_personnel)
time.sleep(2)

client.query(consumer_customer)
time.sleep(2)

client.query(NPI)
time.sleep(2)

client.query(regulation_standard)
time.sleep(2)


 
logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:IndustryStandardAndRegulation)-[*]->()
WITH path
UNWIND nodes(path) AS n
UNWIND relationships(path) AS r
WITH collect(DISTINCT n) AS uniqueNodes, collect(DISTINCT r) AS uniqueRels

RETURN {
  nodes: [n IN uniqueNodes | n {
    .*,
    id: elementId(n),
    labels: labels(n),
    mainLabel: head(labels(n))
  }],
  rels: [r IN uniqueRels | r {
    .*,
    id: elementId(r),
    type: type(r),
    from: elementId(startNode(r)),
    to: elementId(endNode(r))
  }]
} AS graph_data""")

res = res[-1]['graph_data']

import json
with open('glba.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to glba.json")

client.close()

