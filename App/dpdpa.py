#Regulation
regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:RegionalStandardAndRegulation {
  regional_standard_regulation_id: row.regulation_id
})
ON CREATE SET
  reg.name = row.name,
  reg.citation = row.citation,
  reg.version = row.version,
  reg.status = row.status,
  reg.effective_date = row.effective_date,
  reg.jurisdiction = row.jurisdiction,
  reg.description = row.description;
"""
#Chapter
chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {regional_standard_regulation_id:'DPDPA 1.0', chapter_id: row.chapter_id})
ON CREATE SET 
  c.number = toInteger(row.chapter_number),
  c.name = row.title,
  c.description = row.description;
"""
#Section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {regional_standard_regulation_id:'DPDPA 1.0', section_id: row.section_id})
ON CREATE SET 
  sec.number = row.section_number,
  sec.chapter_id = row.chapter_id,
  sec.name = row.title;
"""
#Requirement
requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
ON CREATE SET 
  req.section_id = row.section_id,
  req.text = row.requirement_text,
  req.type = row.requirement_type,
  req.priority = row.priority,
  req.status = row.status;
"""
#role
role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_regulation_id:'DPDPA 1.0', role_id: row.role_id})
ON CREATE SET 
  ro.name = row.name,
  ro.description = row.description,
  ro.category = row.category;
"""
#datacategory
datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id:'DPDPA 1.0', data_id: row.data_id})
ON CREATE SET 
  dc.name = row.name,
  dc.description = row.description,
  dc.category = row.category,
  dc.definition_section = row.definition_section,
  dc.requires_consent = row.requires_consent;
"""
#safeguard
safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_regulation_id:'DPDPA 1.0', safeguard_id: row.safeguard_id})
ON CREATE SET 
  sg.name = row.name,
  sg.description = row.description,
  sg.type = row.type,
  sg.applies_to_section = row.applies_to_section;
"""
#event_type
event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id:'DPDPA 1.0', event_type_id: row.event_type_id})
ON CREATE SET 
  et.name = row.name,
  et.description = row.description,
  et.deadline = row.deadline,
  et.extendable = row.extendable,
  et.extension_period = row.extension_period,
  et.cost = row.cost;
"""
#policy
policy ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {regional_standard_regulation_id:'DPDPA 1.0', policy_id: row.policy_id})
ON CREATE SET 
  pol.name = row.name,
  pol.description = row.description,
  pol.owner = row.owner,
  pol.version = row.version,
  pol.effective_date = date(row.effective_date);
"""
#control
control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
ON CREATE SET 
  co.name = row.name,
  co.category = row.category,
  co.owner = row.owner,
  co.description = row.description;
"""
#system
system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
ON CREATE SET 
  sys.name = row.name,
  sys.type = row.type,
  sys.description = row.description,
  sys.category = row.category,
  sys.personal_data = row.holds_personal_data,
  sys.sensitive_data = row.holds_sensitive_data,
  sys.processing_activities = row.processing_activities;
"""
#process
process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
ON CREATE SET 
  pr.name = row.name,
  pr.description = row.description,
  pr.owner = row.owner,
  pr.frequency = row.frequency,
  pr.deadline = row.deadline;
"""
#enforcement_action
enforcement_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
ON CREATE SET 
  ea.name = row.name,
  ea.description = row.description,
  ea.type = row.type,
  ea.authority = row.authority,
  ea.level = row.severity_level,
  ea.applicable_section = row.applicable_section;
"""
#DataPrincipal
data_principal = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DataPrincipal {
  regional_standard_regulation_id: 'DPDPA 1.0',
  data_principal_id: row.data_principal_id
})
ON CREATE SET
  dp.name = row.name,
  dp.description = row.description;
"""
#DataFiduciary
data_fiduciary = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (df:DataFiduciary {
  regional_standard_regulation_id: 'DPDPA 1.0',
  data_fiduciary_id: row.data_fiduciary_id
})
ON CREATE SET
  df.name = row.name,
  df.description = row.description,
  df.category = row.category;
"""
#DataProcessor
data_processor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DataProcessor {
  regional_standard_regulation_id: 'DPDPA 1.0',
  data_processor_id: row.data_processor_id
})
ON CREATE SET
  dp.name = row.name,
  dp.description = row.description;
"""
#DataProtectionBoard(DPB)
data_protection_board = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (b:DataProtectionBoard {
  regional_standard_regulation_id: 'DPDPA 1.0',
  board_id: row.board_id
})
ON CREATE SET
  b.name = row.name,
  b.description = row.description;
"""
#Right (DPDPA data principal rights)
right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Right {
  regional_standard_regulation_id: 'DPDPA 1.0',
  right_id: row.right_id
})
ON CREATE SET
  r.name = row.name,
  r.section_id = row.section_id;
"""
# LegalBasis (lawful grounds for processing)
legal_basis = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lb:LegalBasis {
  regional_standard_regulation_id: 'DPDPA 1.0',
  legal_basis_id: row.legal_basis_id
})
ON CREATE SET
  lb.name = row.name,
  lb.description = row.description;
"""
#ProcessingActivity
processing_activity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {
  regional_standard_regulation_id: 'DPDPA 1.0',
  processing_id: row.processing_id
})
ON CREATE SET
  pa.name = row.name,
  pa.category = row.category,        
  pa.description = row.description;
"""
# Consent
consent = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Consent {
  regional_standard_regulation_id: 'DPDPA 1.0',
  consent_id: row.consent_id
})
ON CREATE SET
  c.name = row.name,
  c.description = row.description;
"""
# Exemption
exemption = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:Exemption {
  regional_standard_regulation_id: 'DPDPA 1.0',
  exemption_id: row.exemption_id
})
ON CREATE SET
  ex.name = row.name,
  ex.description = row.description,
  ex.section_id = row.section_id;
"""
#Complaint (grievance)
complaint = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cm:Complaint {
  regional_standard_regulation_id: 'DPDPA 1.0',
  complaint_id: row.complaint_id
})
ON CREATE SET
  cm.channel = row.channel,
  cm.description = row.description;
"""

# Significant Data Fiduciary (SDF)
significant_data_fiduciary = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sdf:SignificantDataFiduciary {
  regional_standard_regulation_id: 'DPDPA 1.0',
  sdf_id: row.sdf_id
})
ON CREATE SET
  sdf.name = row.name,
  sdf.notification_criteria = row.criteria, 
  sdf.notification_date = row.notification_date;
"""

# Consent Manager
consent_manager = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cm:ConsentManager {
  regional_standard_regulation_id: 'DPDPA 1.0',
  consent_manager_id: row.consent_manager_id
})
ON CREATE SET
  cm.name = row.name,
  cm.registration_number = row.registration_number,
  cm.technical_standard = row.technical_standard;
"""

# Nominee
nominee = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (n:Nominee {
  regional_standard_regulation_id: 'DPDPA 1.0',
  nominee_id: row.nominee_id
})
ON CREATE SET
  n.name = row.name,
  n.relationship_type = row.relationship_type,
  n.rights_scope = "Posthumous/Incapacity";
"""

# Independent Data Auditor
independent_auditor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ida:IndependentDataAuditor {
  regional_standard_regulation_id: 'DPDPA 1.0',
  auditor_id: row.auditor_id
})
ON CREATE SET
  ida.name = row.name,
  ida.accreditation = row.accreditation;
"""

# Notice 
notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (not:Notice {
  regional_standard_regulation_id: 'DPDPA 1.0',
  notice_id: row.notice_id
})
ON CREATE SET
  not.content_summary = row.content,
  not.languages_available = row.languages; 
"""

# Breach Notification
breach_notification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bn:BreachNotification {
  regional_standard_regulation_id: 'DPDPA 1.0',
  notification_id: row.notification_id
})
ON CREATE SET
  bn.trigger_event = "Personal Data Breach",
  bn.recipient_type = row.recipient_type,
  bn.deadline = "As prescribed";
"""

# Duty (of Data Principal)
duty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Duty {
  regional_standard_regulation_id: 'DPDPA 1.0',
  duty_id: row.duty_id
})
ON CREATE SET
  d.name = row.name,
  d.description = row.description, // e.g., "Do not file frivolous grievance"
  d.penalty_for_breach = "₹10,000";
"""



#Relationships
regulation_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: row.regulation_id})
MATCH (c:Chapter {regional_standard_regulation_id: 'DPDPA 1.0', chapter_id: row.chapter_id})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_CHAPTER]->(c);
"""

chapter_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {regional_standard_regulation_id: 'DPDPA 1.0', chapter_id: row.chapter_id})
MATCH (sec:Section {regional_standard_regulation_id:'DPDPA 1.0', section_id: row.section_id})
MERGE (c)-[:CHAPTER_HAS_SECTION]->(sec);
"""
section_right = """
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sec)-[:SECTION_ESTABLISHES_RIGHT]->(r);
"""


section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0', section_id: row.section_id})
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0', requirement_id: row.requirement_id})
MERGE (sec)-[:SECTION_HAS_REQUIREMENT]->(req);
"""

requirement_roles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (ro:Role {regional_standard_regulation_id:'DPDPA 1.0', role_id: row.role_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_ROLES]->(ro);
"""

requirement_datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (dc:DataCategory {regional_standard_regulation_id:'DPDPA 1.0', data_id: row.data_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_DATACATEGORY]->(dc);
"""

requirement_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (sg:Safeguard {regional_standard_regulation_id:'DPDPA 1.0', safeguard_id: row.safeguard_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_SAFEGUARD]->(sg);
"""

requirement_event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (et:EventType {regional_standard_regulation_id:'DPDPA 1.0', event_type_id: row.event_type_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_EVENTTYPE]->(et);
"""

requirement_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (pol:Policy {regional_standard_regulation_id:'DPDPA 1.0', policy_id: row.policy_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_POLICY]->(pol);
"""

requirement_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_CONTROL]->(co);
"""

control_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
MATCH (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
MERGE (co)-[:CONTROLS_CONTROLS_SYSTEM]->(sys);
"""

requirement_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_PROCESS]->(pr);
"""

process_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
MATCH (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
MERGE (pr)-[:PROCESSES_PROCESSES_SYSTEM]->(sys);
"""

enforcement_action_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
MATCH (req:Requirement {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    requirement_id: row.requirement_id
})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_REQUIREMENTS]->(req);
"""

enforcement_action_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
MATCH (ro:Role {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    role_id: row.role_id
})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_ROLES]->(ro);
"""


requirement_right = """
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (req)-[:REQUIREMENT_SUPPORTS_RIGHT]->(r);
"""
role_right ="""
MATCH (ro:Role {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (ro)-[:ROLE_HAS_RIGHT]->(r);
"""
data_principal_right ="""
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_HAS_RIGHT]->(r);
"""
data_fiduciary_data_principal ="""
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_OWES_DUTY_TO_DATA_PRINCIPAL]->(dp);
"""
data_fiduciary_data_processor ="""
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dpr:DataProcessor {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_OWES_DUTY_TO_DATA_PROCESSOR]->(dpr);
"""
data_protection_board_enforcement_action ="""
MATCH (b:DataProtectionBoard {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (b)-[:DATA_PROTECTION_BOARD_OWES_DUTY_TO_ENFORCEMENT_ACTION]->(ea);
"""

data_principal_complaint ="""
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (cm:Complaint {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_FILES_COMPLAINT]->(cm);
"""
complaint_data_protection_board ="""
MATCH (cm:Complaint {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (b:DataProtectionBoard {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (cm)-[:COMPLAINT_RECEIVED_BY_DATA_PROTECTION_BOARD]->(b);
"""
requirement_processing_activity ="""
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (req)-[:REQUIREMENT_REGULATES_PROCESSING]->(pa);
"""
processing_activity_data_category ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pa)-[:PROCESSING_USES_DATACATEGORY]->(dc);
"""
processing_activity_legal_basis ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (lb:LegalBasis {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pa)-[:PROCESSING_ACTIVATES_LEGAL_BASIS]->(lb);
"""
process_processing_activity ="""
MATCH (pr:Process {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pr)-[:PROCESS_INCLUDES_ACTIVITY]->(pa);
"""
processing_activity_system ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (sys:System {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pa)-[:ACTIVITY_EXECUTED_ON_SYSTEM]->(sys);
"""
data_principal_consent ="""
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (c:Consent {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_GIVES_CONSENT]->(c);
"""
consent_processing_activity ="""
MATCH (c:Consent {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (c)-[:CONSENT_PROVIDES_PROCESSING]->(pa);
"""
exemption_section ="""
MATCH (ex:Exemption {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (ex)-[:EXEMPTION_DEFINED_IN_SECTION]->(sec);
"""
processing_activity_exemption ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pa)-[:PROCESSING_EXEMPT_UNDER_EXEMPTION]->(ex);
"""
section_legal_basis ="""
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (lb:LegalBasis {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sec)-[:SECTION_DEFINES_LEGAL_BASIS]->(lb);
"""

requirement_consent ="""
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (c:Consent {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (req)-[:REQUIREMENT_REQUIRES_CONSENT]->(c);
"""
requirement_legal_basis ="""
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (lb:LegalBasis {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (req)-[:REQUIREMENT_REQUIRES_LEGAL_BASIS]->(lb);
"""

data_fiduciary_processing_activity ="""
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_CONDUCTS_PROCESSING]->(pa);
"""
data_processor_processing_activity ="""
MATCH (dpr:DataProcessor {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dpr)-[:DATA_PROCESSOR_PERFORMS_PROCESSING]->(pa);
"""
role_requirement ="""
MATCH (ro:Role {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (ro)-[:ROLE_IMPLEMENTS_REQUIREMENT]->(req);
"""

section_exemption ="""
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sec)-[:SECTION_PROVIDES_EXEMPTION]->(ex);
"""

requirement_exemption ="""
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (req)-[:REQUIREMENT_SUBJECT_TO_EXEMPTION]->(ex);
"""
enforcement_action_section ="""
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (ea)-[:ENFORCEMENT_APPLIES_TO_SECTION]->(sec);
"""

data_protection_board_right ="""
MATCH (b:DataProtectionBoard {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (b)-[:BOARD_ENFORCES_RIGHT]->(r);
"""

chapter_exemption ="""
MATCH (c:Chapter {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (c)-[:CHAPTER_DEFINES_EXEMPTION]->(ex);
"""

system_datacategory ="""
MATCH (sys:System {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sys)-[:SYSTEM_STORES_DATACATEGORY]->(dc);
"""

control_processing_activity ="""
MATCH (co:Control {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (co)-[:CONTROL_PROTECTS_PROCESSING]->(pa);
"""
safeguard_processing_activity ="""
MATCH (sg:Safeguard {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sg)-[:SAFEGUARD_PROTECTS_PROCESSING]->(pa);
"""
policy_processing_activity ="""
MATCH (pol:Policy {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pol)-[:POLICY_GOVERNS_PROCESSING]->(pa);
"""
processing_activity_right ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (pa)-[:PROCESSING_SUBJECT_TO_RIGHT]->(r);
"""
#  Data Fiduciary to Significant Data Fiduciary (Designation)
fiduciary_is_sdf = """
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (sdf:SignificantDataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_DESIGNATED_SIGNIFICANT]->(sdf);
"""

# SDF Appoints Independent Auditor
sdf_appoints_auditor = """
MATCH (sdf:SignificantDataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ida:IndependentDataAuditor {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sdf)-[:SIGNIFICANT_DATA_FIDUCIARY_APPOINTED_INDEPENDENT_AUDITOR]->(ida);
"""

# Independent Auditor Audits System
auditor_audits_system = """
MATCH (ida:IndependentDataAuditor {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (sys:System {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (ida)-[:INDEPENDENT_AUDITOR_CONDUCTS_SYSTEM_AUDITS]->(sys);
"""
# Fiduciary Issues Notice
fiduciary_issues_notice = """
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (not:Notice {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_ISSUES_NOTICE]->(not);
"""

# Notice Precedes and Validates Consent
notice_precedes_consent = """
MATCH (not:Notice {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (c:Consent {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (not)-[:NOTICE_MUST_PRECEDE_AND_VALIDATE_CONSENT]->(c);
"""

# Data Principal Manages Consent through Manager
principal_uses_manager = """
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (cm:ConsentManager {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_MANAGES_CONSENT_MANAGER]->(cm);
"""

# Consent Manager Facilitates Consent for Fiduciary
manager_links_fiduciary = """
MATCH (cm:ConsentManager {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (cm)-[:CONSENT_MANAGER_FACILITATES_CONSENT_FOR_FIDUCIARY]->(df);
"""

# Data Principal Nominates Successor
principal_nominates = """
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (n:Nominee {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_NOMINATES_SUCCESSOR]->(n);
"""

# Nominee Exercises Right (on behalf of Principal)
nominee_exercises_right = """
MATCH (n:Nominee {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (r:Right {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (n)-[:NOMINEE_EXERCISES_RIGHT]->(r);
"""

# Data Principal Must Adhere to Duty
principal_owes_duty = """
MATCH (dp:DataPrincipal {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (d:Duty {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (dp)-[:DATA_PRINCIPAL_MUST_ADHERE_TO_DUTY]->(d);
"""

# Fiduciary Triggers Breach Notification
fiduciary_reports_breach = """
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (bn:BreachNotification {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_TRIGGERS_NOTIFICATION]->(bn);
"""

# Breach Notification Intimated to Board
breach_sent_to_board = """
MATCH (bn:BreachNotification {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dpb:DataProtectionBoard {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (bn)-[:BREACH_NOTIFICATION_INTIMATED_TO_DATA_PROTECTION_BOARD]->(dpb);
"""

# Violation of Duty Triggers Enforcement Action
duty_violation_penalty = """
MATCH (d:Duty {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (d)-[:DUTY_VIOLATION_TRIGGERS_PENALTY]->(ea);
"""
# Fiduciary Engages Processor (Contractual)
fiduciary_engages_processor = """
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (dpr:DataProcessor {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (df)-[:DATA_FIDUCIARY_ENGAGES_UNDER_DATA_PROCESSOR]->(dpr);
"""

# Complaint Initially Lodged with Fiduciary
complaint_fiduciary = """
MATCH (cm:Complaint {regional_standard_regulation_id: 'DPDPA 1.0'})
MATCH (df:DataFiduciary {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (cm)-[:COMPLAINT_INITIALLY_LODGED_WITH_FIDUCIARY]->(df);
"""
regulation_event_type = """
MATCH (orphan:EventType) 
WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DPDPA 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_EVENT_TYPE]->(orphan);
"""

import sys
import os
import time
import logging
import json
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    client.close()
    sys.exit(1)

logger.info("Loading graph structure...")

client.query(regulation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Regulation_Node.csv"))
time.sleep(2)

client.query(chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Chapters.csv"))
time.sleep(2)

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Sections.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirements.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Roles.csv"))
time.sleep(2)

client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_DataCategories.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Safeguards.csv"))
time.sleep(2)

client.query(event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Event%20Types.csv"))
time.sleep(2)

client.query(policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Policies.csv"))
time.sleep(2)

client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Controls.csv"))
time.sleep(2)

client.query(system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Systems.csv"))
time.sleep(2)

client.query(process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Processes.csv"))
time.sleep(2)

client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction.csv"))
time.sleep(2)

client.query(data_principal.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DataPrincipal.csv"))
time.sleep(2)

client.query(data_fiduciary.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DataFiduciary.csv"))
time.sleep(2)

client.query(data_processor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DataProcessor.csv"))
time.sleep(2)

client.query(data_protection_board.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DataProtectionBoard.csv"))
time.sleep(2)

client.query(right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/Right.csv"))
time.sleep(2)

client.query(legal_basis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/LegalBasis.csv"))
time.sleep(2) 

client.query(processing_activity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/ProcessingActivity.csv"))
time.sleep(2)

client.query(consent.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/Consent.csv"))
time.sleep(2)

client.query(exemption.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/Exemption.csv"))
time.sleep(2)

client.query(complaint.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/Complaint.csv"))
time.sleep(2)

client.query(significant_data_fiduciary.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Significant%20Data%20Fiduciary.csv"))
time.sleep(2)

client.query(consent_manager.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Consent%20Manager.csv"))
time.sleep(2)

client.query(nominee.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Nominee.csv"))
time.sleep(2)

client.query(independent_auditor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Independent%20Auditor.csv"))
time.sleep(2)

client.query(notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Notice.csv"))
time.sleep(2)

client.query(breach_notification.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Breach%20Notification.csv"))
time.sleep(2)

client.query(duty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Duty.csv"))
time.sleep(2)


#Relationship
client.query(regulation_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Regulation_Chapter_Relationship_FIXED.csv"))
time.sleep(2)

client.query(chapter_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA-Chap-Sec-Rel.csv"))
time.sleep(2)

client.query(section_right)
time.sleep(2)

client.query(section_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA-Sec-Req-Rel.csv"))
time.sleep(2)

                                        
client.query(requirement_roles.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Roles.csv"))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Data.csv"))
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Safeguards.csv"))
time.sleep(2)

client.query(requirement_event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA%20-%20Requirements%20Event%20Type.csv"))
time.sleep(2)

client.query(requirement_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Controls.csv"))
time.sleep(2)


client.query(requirement_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Policies.csv"))
time.sleep(2)

client.query(control_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Control_Systems.csv"))
time.sleep(2)

client.query(requirement_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Processes.csv"))
time.sleep(2)

client.query(process_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Process_Systems.csv"))
time.sleep(2)

client.query(enforcement_action_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction_Requirement_Relationship.csv"))
time.sleep(2)

client.query(enforcement_action_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction_Role_Relationship.csv"))
time.sleep(2)

client.query(requirement_right)
time.sleep(2)

client.query(role_right)
time.sleep(2)

client.query(data_principal_right)
time.sleep(2)

client.query(data_fiduciary_data_principal)
time.sleep(2)

client.query(data_fiduciary_data_processor)
time.sleep(2)

client.query(data_protection_board_enforcement_action)
time.sleep(2)

client.query(data_principal_complaint)
time.sleep(2)

client.query(complaint_data_protection_board)
time.sleep(2)

client.query(requirement_processing_activity)
time.sleep(2)

client.query(processing_activity_data_category)
time.sleep(2)

client.query(processing_activity_legal_basis)
time.sleep(2)

client.query(process_processing_activity)
time.sleep(2)

client.query(processing_activity_system)
time.sleep(2)

client.query(data_principal_consent)
time.sleep(2)

client.query(consent_processing_activity)
time.sleep(2)

client.query(exemption_section)
time.sleep(2)

client.query(processing_activity_exemption)
time.sleep(2)

client.query(section_legal_basis)
time.sleep(2)

client.query(requirement_consent)
time.sleep(2)

client.query(requirement_legal_basis)
time.sleep(2)

client.query(data_fiduciary_processing_activity)
time.sleep(2)

client.query(data_processor_processing_activity)
time.sleep(2)

client.query(role_requirement)
time.sleep(2)

client.query(section_exemption)
time.sleep(2)

client.query(requirement_exemption)
time.sleep(2)

client.query(enforcement_action_section)
time.sleep(2)

client.query(data_protection_board_right)
time.sleep(2)

client.query(chapter_exemption) 
time.sleep(2)

client.query(system_datacategory)
time.sleep(2)

client.query(control_processing_activity)
time.sleep(2)

client.query(safeguard_processing_activity)
time.sleep(2)

client.query(policy_processing_activity)
time.sleep(2)

client.query(processing_activity_right)
time.sleep(2)

client.query(fiduciary_is_sdf)
time.sleep(2)

client.query(sdf_appoints_auditor)
time.sleep(2)

client.query(auditor_audits_system)
time.sleep(2)

client.query(fiduciary_issues_notice)
time.sleep(2)

client.query(notice_precedes_consent)
time.sleep(2)

client.query(principal_uses_manager)
time.sleep(2)

client.query(manager_links_fiduciary)
time.sleep(2)

client.query(principal_nominates)
time.sleep(2)

client.query(nominee_exercises_right)
time.sleep(2)

client.query(principal_owes_duty)
time.sleep(2)

client.query(fiduciary_reports_breach)
time.sleep(2)

client.query(breach_sent_to_board)
time.sleep(2)

client.query(duty_violation_penalty)
time.sleep(2)

client.query(fiduciary_engages_processor)
time.sleep(2)

client.query(complaint_fiduciary)
time.sleep(2)

client.query(regulation_event_type)
time.sleep(2)




logger.info("Graph structure loaded successfully.")

query = """
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
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
} AS graph_data
"""

results = client.query(query)

if results and len(results) > 0:
    graph_data = results[0]['graph_data']
    
    import json
    with open('dpdpa.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to dpdpa.json")
else:
    logger.error("No data returned from the query.")

client.close()