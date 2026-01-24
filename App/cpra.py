# Regulation Node
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPRA 2.0'})
ON CREATE SET 
    reg.name = "California Privacy Rights Act",
    reg.version = "2.0 (Amends CCPA)",
    reg.base_regulation = "California Consumer Privacy Act (CCPA)",
    reg.codification = "California Civil Code Title 1.81.5",
    reg.effective_date = date("2023-01-01"),
    reg.status = "Active",
    reg.description = "The CPRA is a ballot initiative that amends the CCPA, creating new consumer rights, establishing the CPPA, and strengthening enforcement.";
"""

# Title
title = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Title {regional_standard_regulation_id: 'CPRA 2.0', title_id: row.title_id})
ON CREATE SET
  t.title_number = row.title_number,    
  t.name = row.name,                    
  t.legal_citation = row.legal_citation;
"""
# Subdivison
subdivision = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sd:Subdivision {regional_standard_regulation_id: 'CPRA 2.0', subdivision_id: row.subdivision_id})
ON CREATE SET
  sd.section_id = row.section_id,      
  sd.name = row.name,                   
  sd.text = row.text;
"""

# Paragaph
paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph {regional_standard_regulation_id: 'CPRA 2.0', paragraph_id: row.paragraph_id})
ON CREATE SET
  p.subdivision_id = row.subdivision_id,
  p.text = row.text;
"""

# Consumer 
consumer = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Consumer {regional_standard_regulation_id: 'CPRA 2.0', consumer_id: row.consumer_id})
ON CREATE SET
  c.description = row.description;
"""

# Business 
business = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (b:Business {regional_standard_regulation_id: 'CPRA 2.0', business_id: row.business_id})
ON CREATE SET
  b.definition = row.definition;
"""
# Service_provider
service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:ServiceProvider {regional_standard_regulation_id: 'CPRA 2.0', service_provider_id: row.service_provider_id})
ON CREATE SET
  sp.definition = row.definition;
"""

# Contractor
contractor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:Contractor {regional_standard_regulation_id: 'CPRA 2.0', contractor_id: row.contractor_id})
ON CREATE SET
  ct.definition = row.definition;
"""
# Third_party
third_party = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tp:ThirdParty {regional_standard_regulation_id: 'CPRA 2.0', third_party_id: row.third_party_id})
ON CREATE SET
  tp.definition = row.definition;
"""
# Threshold
threshold = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (th:Threshold {regional_standard_regulation_id: 'CPRA 2.0', threshold_id: row.threshold_id})
ON CREATE SET
  th.type = row.type,         
  th.value = row.value;        
"""
# CPPA (enforcement authority)
cppa = """
MERGE (a:EnforcementAuthority {regional_standard_regulation_id: 'CPRA 2.0', authority_id: 'CPPA'})
ON CREATE SET
  a.name = 'California Privacy Protection Agency',
  a.type = 'AdministrativeRegulator';
"""
# PI 
pi_roots = """
MERGE (pi:PersonalInformation {regional_standard_regulation_id: 'CPRA 2.0', data_root_id: 'PI'})
ON CREATE SET 
    pi.name = 'Personal Information';
"""
# SPI
SPI = """
MERGE (spi:SensitivePersonalInformation {regional_standard_regulation_id: 'CPRA 2.0', data_root_id: 'SPI'})
ON CREATE SET spi.name = 'Sensitive Personal Information';
"""
# PI Categories A–K
pi_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pc:PICategory {regional_standard_regulation_id: 'CPRA 2.0', pi_category_id: row.pi_category_id})
ON CREATE SET
  pc.code = row.code,         
  pc.name = row.name,
  pc.examples = row.examples;
"""

# SPI Categories 1A–2C
spi_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:SPICategory {regional_standard_regulation_id: 'CPRA 2.0', spi_category_id: row.spi_category_id})
ON CREATE SET
  sc.code = row.code,          
  sc.name = row.name,
  sc.text = row.text;
"""


# Section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.section_id})
ON CREATE SET 
    s.heading = row.heading;
"""

# Requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.requirement_id})
ON CREATE SET 
    rq.section_id = row.section_id,
    rq.text = row.text,
    rq.type = row.type;
"""

# Role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.role_id})
ON CREATE SET 
    ro.name = row.name,
    ro.description = row.description;
"""

# DataCategory
datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id: 'CPRA 2.0', data_id: row.data_id})
ON CREATE SET
    dc.name = row.name,
    dc.sensitivity = row.sensitivity;
"""

# Right
right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.right_id})
ON CREATE SET 
    r.section_id = row.section_id,
    r.name = row.name;
"""

# Safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_regulation_id: 'CPRA 2.0', safeguard_id: row.safeguard_id})
ON CREATE SET 
    sg.type = row.type,
    sg.description = row.description;
"""

# EventType
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id: 'CPRA 2.0', event_type_id: row.event_type_id})
ON CREATE SET   
    et.name = row.name,
    et.description = row.description;
"""

# EnforcementAction
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.enforcement_id})
ON CREATE SET 
    ea.authority = row.authority,
    ea.max_penalty = row.max_penalty,
    ea.description = row.description;
"""

# Control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_regulation_id: 'CPRA 2.0', control_id: row.control_id})
ON CREATE SET 
    co.name = row.name,
    co.category = row.category;
"""
# ProcessingActivity
processing_activity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0', processing_id: row.processing_id})
ON CREATE SET
  pa.name = row.name,             
  pa.type = row.type,              
  pa.description = row.description;
"""
# BusinessPurpose 
business_purpose = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bp:BusinessPurpose {regional_standard_regulation_id: 'CPRA 2.0', purpose_id: row.purpose_id})
ON CREATE SET
  bp.code = row.code,            
  bp.name = row.name,
  bp.text = row.text;
"""

# NoticeAtCollection
notice_at_collection = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (n:NoticeAtCollection {regional_standard_regulation_id: 'CPRA 2.0', notice_id: row.notice_id})
ON CREATE SET
  n.description = row.description;
"""

# PrivacyPolicy
privacy_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pp:PrivacyPolicy {regional_standard_regulation_id: 'CPRA 2.0', policy_id: row.policy_id})
ON CREATE SET
  pp.name = row.name,
  pp.version = row.version,
  pp.url = row.url;
"""

# RiskAssessment
risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ra:RiskAssessment {regional_standard_regulation_id: 'CPRA 2.0', risk_assessment_id: row.risk_assessment_id})
ON CREATE SET
  ra.regulation_ref = row.regulation_ref,     
  ra.description = row.description;
"""

# CybersecurityAudit
cybersecurity_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ca:CybersecurityAudit {regional_standard_regulation_id: 'CPRA 2.0', audit_id: row.audit_id})
ON CREATE SET
  ca.regulation_ref = row.regulation_ref,    
  ca.description = row.description;
"""

# OptOutLink & OptOutPreferenceSignal
optout_link = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ol:OptOutLink {regional_standard_regulation_id: 'CPRA 2.0', optout_link_id: row.optout_link_id})
ON CREATE SET
  ol.text = row.text;
"""

# OptOut Signal
optout_signal = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (os:OptOutPreferenceSignal {regional_standard_regulation_id: 'CPRA 2.0', signal_id: row.signal_id})
ON CREATE SET
  os.name = row.name,              
  os.description = row.description;
"""

# AdministrativeFine
administrative_fine = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (af:AdministrativeFine {regional_standard_regulation_id: 'CPRA 2.0', fine_id: row.fine_id})
ON CREATE SET
  af.standard_amount = row.standard_amount,
  af.intentional_amount = row.intentional_amount,
  af.minor_amount = row.minor_amount;
"""

# DataBreach
data_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (db:DataBreach {regional_standard_regulation_id: 'CPRA 2.0', breach_id: row.breach_id})
ON CREATE SET
  db.scope = row.scope,
  db.damages_range = row.damages_range;
"""

# Consumer Request (Transactional Ticket)
consumer_request = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cr:ConsumerRequest {regional_standard_regulation_id: 'CPRA 2.0', request_id: row.request_id})
ON CREATE SET 
    cr.received_date = row.received_date,
    cr.due_date = row.due_date,
    cr.status = row.status,    
    cr.type = row.type,         
    cr.days_open = row.days_open;
"""
# Verification_method
verification_method = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vm:VerificationMethod {regional_standard_regulation_id: 'CPRA 2.0', method_id: row.method_id})
ON CREATE SET 
    vm.name = row.name,                 
    vm.assurance_level = row.level;     
"""
# Denial Reason (For audit trails)
denial_reason = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dr:DenialReason {regional_standard_regulation_id: 'CPRA 2.0', reason_id: row.reason_id})
ON CREATE SET 
    dr.code = row.code,                
    dr.description = row.description;  
"""
# Exemption (Why a right was denied)
exemption = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:Exemption {regional_standard_regulation_id: 'CPRA 2.0', exemption_id: row.exemption_id})
ON CREATE SET 
    ex.name = row.name,                 
    ex.scope = row.scope,              
    ex.legal_citation = row.citation;
"""

# Retention Schedule (Specific retention rules)
retention_schedule = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rs:RetentionSchedule {regional_standard_regulation_id: 'CPRA 2.0', retention_id: row.retention_id})
ON CREATE SET 
    rs.period_days = row.period_days,
    rs.trigger_event = row.trigger,     
    rs.justification = row.justification;
"""

# Commercial Purpose (Triggers "Sale/Sharing")
commercial_purpose = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cp:CommercialPurpose {regional_standard_regulation_id: 'CPRA 2.0', purpose_id: row.purpose_id})
ON CREATE SET 
    cp.name = row.name,                
    cp.triggers_opt_out = true;
"""

# Contract Clause (Statutory requirements for Service Providers)
contract_clause = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ContractClause {regional_standard_regulation_id: 'CPRA 2.0', clause_id: row.clause_id})
ON CREATE SET 
    cc.name = row.name,                
    cc.mandatory_text = row.text;
"""

# Automated Decision Making (ADMT)
admt = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (admt:ADMT {regional_standard_regulation_id: 'CPRA 2.0', system_id: row.system_id})
ON CREATE SET 
    admt.name = row.name,
    admt.logic = row.logic_summary,
    admt.impact = row.impact_description;
"""

# Transparency Report (Annual Metrics)
transparency_report = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tr:TransparencyReport {regional_standard_regulation_id: 'CPRA 2.0', report_year: row.year})
ON CREATE SET 
    tr.received_count = row.received,
    tr.denied_count = row.denied,
    tr.mean_response_time = row.response_time;
"""


# RELATIONSHIPS
# Regulation to Section
regulation_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.to_id})
MERGE (reg)-[:REGIONAL_REGULATION_DEFINES_SECTION]->(s);
"""

# Section to Subdivison
section_subdivision = """
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (sd:Subdivision{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (s)-[:SECTION_DEFINES_SUBDIVISION]->(sd);
"""


# Section to Requirement
section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.to_id})
MERGE (s)-[:SECTION_DEFINES_REQUIREMENT]->(rq);
"""

# Section to Right
section_right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.to_id})
MERGE (s)-[:SECTION_ESTABLISHES_RIGHT]->(r);
"""

# Section to EnforcementAction
section_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.to_id})
MERGE (s)-[:SECTION_PRESCRIBES_PENALTY]->(ea);
"""

# Requirement to DataCategory
requirement_datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'CPRA 2.0', data_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_REGULATES_USE_OF_DATA_CATEGORY]->(dc);
"""

# Requirement to Safeguard
requirement_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (sg:Safeguard {regional_standard_regulation_id: 'CPRA 2.0', safeguard_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg);
"""

# Requirement to EventType
requirement_event = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (et:EventType {regional_standard_regulation_id: 'CPRA 2.0', event_type_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_TRIGGERS_ON_EVENT_TYPE]->(et);
"""

# Requirement to Control
requirement_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (co:Control {regional_standard_regulation_id: 'CPRA 2.0', control_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co);
"""

# Requirement to EnforcementAction
requirement_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_CARRIES_PENALTY_ON_ENFORCEMENT]->(ea);
"""

# Role to Right
role_right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.from_id})
MATCH (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.to_id})
MERGE (ro)-[:ROLE_HAS_RIGHT]->(r);
"""

# Contract Requirements
requirement_contract = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_MANDATES_CONTRACT_WITH_ROLE]->(ro);
"""
# Subdivision to paragraph
subdivision_paragraph = """
MATCH (sd:Subdivision {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (p:Paragraph {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (sd)-[:SUBDIVISION_CONTAINS_PARAGRAPH]->(p);
"""
# Business to Threshold
business_threshold = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (th:Threshold{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_MEETS_THRESHOLD]->(th);
"""
# Consumer to right
consumer_right = """
MATCH (c:Consumer{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (r:Right{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (c)-[:CONSUMER_HAS_RIGHT]->(r);
"""
# Business to consumer
business_consumer = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (c:Consumer{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_OWES_DUTY_TO_CONSUMER]->(c);
"""
# Business to serviceprovider
business_service_provider = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (sp:ServiceProvider{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_ENGAGES_SERVICE_PROVIDER]->(sp);
"""
# Business to contractor
business_contractor ="""
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ct:Contractor{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_ENGAGES_CONTRACTOR]->(ct);
"""
# Business to thirdparty
business_thirdparty ="""
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (tp:ThirdParty{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_ENGAGES_THIRD_PARTY]->(tp);    
"""

# EnforcementAuthority to Business
enforcement_authority_business = """
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_ENGAGES_BUSINESS]->(b);
"""
# EnforcementAuthority to serviceprovider
enforcement_authority_service_provider = """
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (sp:ServiceProvider{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_ENGAGES_SERVICE_PROVIDER]->(sp);
"""

# EnforcementAuthority to contractor
enforcement_authority_contractor = """
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ct:Contractor{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_ENGAGES_CONTRACTOR]->(ct);
"""

# PersonalInformation to PIcategory
personal_information_pi_category = """
MATCH (pi:PersonalInformation{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pc:PICategory{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pi)-[:PERSONAL_INFORMATION_HAS_CATEGORY]->(pc);
"""

# SensitivePersonalInformation to SPIcategory
sensitive_personal_information_spi_category = """
MATCH (spi:SensitivePersonalInformation{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (sc:SPICategory{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (spi)-[:SENSITIVE_PERSONAL_INFORMATION_HAS_CATEGORY]->(sc);
"""

# SPI to right
sensitive_personal_information_right = """
MATCH (spi:SensitivePersonalInformation{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (r:Right{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (spi)-[:SENSITIVE_PERSONAL_INFORMATION_HAS_RIGHT]->(r);
"""
# Business to ProcessingActivity
business_processing_activity = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pa:ProcessingActivity{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_CONDUCTS_PROCESSING_ACTIVITY]->(pa);
"""

# ProcessingActivity to BusinessPurpose
processing_activity_business_purpose = """
MATCH (pa:ProcessingActivity{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (bp:BusinessPurpose{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_USES_BUSINESS_PURPOSE]->(bp);
"""

#Business to NoticeAtCollection
business_notice_at_collection = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (n:NoticeAtCollection{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_NOTICE_AT_COLLECTION]->(n);
"""

#Business to PrivacyPolicy
business_privacy_policy ="""
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pp:PrivacyPolicy{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_PRIVACY_POLICY]->(pp);
"""

# Business to RiskAssessment
business_risk_assessment = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ra:RiskAssessment{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_RISK_ASSESSMENT]->(ra);
"""
# PrivacyPolicy to ProcessingActivity
privacy_policy_processing_activity = """
MATCH (pp:PrivacyPolicy{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pa:ProcessingActivity{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pp)-[:PRIVACY_POLICY_USES_PROCESSING_ACTIVITY]->(pa);
"""
# Business to cybersecurity_audit
business_cybersecurity_audit = """
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ca:CybersecurityAudit{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_CYBERSECURITY_AUDIT]->(ca);
"""
# Business to optout_link
business_optout_link ="""
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ol:OptOutLink{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_OPT_OUT_LINK]->(ol);
"""
# Business to optout_signal
business_optout_signal ="""
MATCH (b:Business{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (os:OptOutPreferenceSignal{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_REQUIRES_OPT_OUT_SIGNAL]->(os);
"""
# Enforcement Authority to Administrative_fine
business_administrative_fine = """
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (af:AdministrativeFine{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_ADMINISTRATIVE_FINE]->(af);
"""
# Enforcement Authority to Risk_Assessment
enforcement_authority_risk_assessment = """
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ra:RiskAssessment{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_RECEIVES_SUBMISSIONS]->(ra);
"""
# Enforcement Authority to Cybersecurity_audit
enforcement_authority_cybersecurity_audit ="""
MATCH (a:EnforcementAuthority{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ca:CybersecurityAudit{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (a)-[:ENFORCEMENT_SUPERVISES_RECEIVES_CERTIFICATIONS]->(ca);
"""

# Consumer to Databreach
consumer_data_breach = """
MATCH (c:Consumer{regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (db:DataBreach{regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (c)-[:CONSUMER_HAS_DATA_BREACH]->(db);
"""
# Consumer -> Request
consumer_initiates_request = """
MATCH (c:Consumer {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (cr:ConsumerRequest {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (c)-[:CONSUMER_INITIATES_REQUEST]->(cr);
"""

# Request -> Right (What did they ask for?)
request_invokes_right = """
MATCH (cr:ConsumerRequest {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (r:Right {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (cr)-[:CONSUMER_REQUESTS_INVOKES_RIGHT]->(r);
"""

# Request -> Verification (How did we check?)
request_verified_by = """
MATCH (cr:ConsumerRequest {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (vm:VerificationMethod {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (cr)-[:CONSUMER_REQUESTS_VERIFIED_BY_VERIFICATION_METHOD]->(vm);
"""

# Request -> Denial Reason (Why did we say no?)
request_denied_because = """
MATCH (cr:ConsumerRequest {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (dr:DenialReason {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (cr)-[:CONSUMER_REQUESTS_DENIED_DUE_TO_DENIAL_REASON]->(dr);
"""

# Data Category -> Retention Schedule
pi_category_retention = """
MATCH (pc:PICategory {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (rs:RetentionSchedule {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pc)-[:PI_CATEGORY_HAS_RETENTION_SCHEDULE]->(rs);
"""

# Business -> Exemption (Entity Level)
business_claims_exemption = """
MATCH (b:Business {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_CLAIMS_ENTITY_EXEMPTION]->(ex);
"""

# Data Category -> Exemption (Data Level)
data_falls_under_exemption = """
MATCH (pc:PICategory {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ex:Exemption {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pc)-[:PI_CATEGORY_FALLS_UNDER_EXEMPTION]->(ex);
"""

# Processing Activity -> Commercial Purpose (Sale/Share Trigger)
activity_commercial_purpose = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (cp:CommercialPurpose {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_SERVES_COMMERCIAL_PURPOSE]->(cp);
"""

# Commercial Purpose -> Opt-Out Link
commercial_purpose_link = """
MATCH (cp:CommercialPurpose {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ol:OptOutLink {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (cp)-[:COMMERCIAL_PURPOSE_REQUIRES_LINK]->(ol);
"""

# Service Provider -> Contract Clause
sp_bound_by_clause = """
MATCH (sp:ServiceProvider {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (cc:ContractClause {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (sp)-[:SERVICE_PROVIDER_BOUND_BY_CONTRACT_CLAUSE]->(cc);
"""

# Business -> Transparency Report
business_transparency = """
MATCH (b:Business {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (tr:TransparencyReport {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_PUBLISHES_METRICS]->(tr);
"""
# Title to Section 
title_section = """
MATCH (t:Title {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (t)-[:TITLE_CONTAINS_SECTION]->(s);
"""
# Processing Activity to PI Category 
processing_activity_pi = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pc:PICategory {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_PROCESSES_DATA]->(pc);
"""

# Processing Activity to SPI Category 
processing_activity_spi = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (sc:SPICategory {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_PROCESSES_SENSITIVE_DATA]->(sc);
"""

# Business to ADMT
business_admt = """
MATCH (b:Business {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (admt:ADMT {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_USES_ADMT]->(admt);
"""

# ADMT to Risk Assessment 
admt_risk_assessment = """
MATCH (admt:ADMT {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ra:RiskAssessment {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (admt)-[:ADMT_REQUIRES_RISK_ASSESSMENT]->(ra);
"""

# ADMT to Processing Activity
admt_processing = """
MATCH (admt:ADMT {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (admt)-[:ADMT_AUTOMATES_ACTIVITY]->(pa);
"""

# Contractor to Contract Clause
contractor_clause = """
MATCH (ct:Contractor {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (cc:ContractClause {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (ct)-[:CONTRACTOR_BOUND_BY_CLAUSE]->(cc);
"""

# Processing Activity to Third Party 
activity_third_party = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (tp:ThirdParty {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_TRANSFERS_TO]->(tp);
"""
# Business to Data Breach
business_breach = """
MATCH (b:Business {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (db:DataBreach {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (b)-[:BUSINESS_EXPERIENCED_BREACH]->(db);
"""

# Data Breach to PI Category (Impact Analysis)
breach_pi = """
MATCH (db:DataBreach {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (pc:PICategory {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (db)-[:DATA_BREACH_COMPROMISED_CATEGORY]->(pc);
"""

# Enforcement Authority to Breach (Notification)
authority_breach = """
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (db:DataBreach {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (ea)-[:AUTHORITY_NOTIFIED_OF_BREACH]->(db);
"""

# Consumer to Opt-Out Signal
consumer_signal = """
MATCH (c:Consumer {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (os:OptOutPreferenceSignal {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (c)-[:CONSUMER_USES_SIGNAL]->(os);
"""
# Processing Activity to Risk Assessment
activity_risk = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (ra:RiskAssessment {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (pa)-[:HIGH_RISK_ACTIVITY_TRIGGERS_ASSESSMENT]->(ra);
"""
# Enforcement Action to Fine Value
action_fine = """
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (af:AdministrativeFine {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (ea)-[:ENFORCEMENT_ACTION_IMPOSES_FINE]->(af);
"""
# Regulation to Threshold
regulation_threshold = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPRA 2.0'})
MATCH (th:Threshold {regional_standard_regulation_id: 'CPRA 2.0'})
MERGE (reg)-[:REGULATION_DEFINES_THRESHOLD]->(th);
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

client.query(regulation)
time.sleep(2)

client.query(title.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Title.csv"))
time.sleep(2)

client.query(subdivision.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Subdivision.csv"))
time.sleep(2)

client.query(paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Paragraph.csv"))
time.sleep(2)

client.query(consumer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Consumer.csv"))
time.sleep(2)

client.query(business.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Business.csv"))
time.sleep(2)

client.query(service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/ServiceProvider.csv"))
time.sleep(2)

client.query(contractor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Contractor.csv"))
time.sleep(2)

client.query(third_party.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/ThirdParty.csv"))
time.sleep(2)

client.query(threshold.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Threshold.csv"))
time.sleep(2)

client.query(cppa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/EnforcementAuthority.csv"))
time.sleep(2)

client.query(pi_roots.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/DataRoot.csv"))
time.sleep(2)

client.query(SPI.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/DataRoot.csv"))
time.sleep(2)

client.query(pi_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/PICategory.csv"))
time.sleep(2)

client.query(spi_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/SPICategory.csv"))
time.sleep(2)

                                 

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Sections.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirements.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Roles_Corrected.csv"))
time.sleep(2)

client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_DataCategories.csv"))
time.sleep(2)

client.query(right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Rights_Corrected.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Safeguards.csv"))
time.sleep(2)

client.query(event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_EventTypes_Corrected.csv"))
time.sleep(2)

client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPPA_EnforcementActions.csv"))
time.sleep(2)

client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Controls.csv"))
time.sleep(2)

client.query(processing_activity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/ProcessingActivity.csv"))
time.sleep(2)

client.query(business_purpose.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/BusinessPurpose.csv"))
time.sleep(2)   

client.query(notice_at_collection.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/NoticeAtCollection.csv"))
time.sleep(2)

client.query(privacy_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/PrivacyPolicy.csv"))
time.sleep(2)

client.query(risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/RiskAssessment.csv"))
time.sleep(2)

client.query(cybersecurity_audit.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CybersecurityAudit.csv"))
time.sleep(2)

client.query(optout_link.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/OptOutLink.csv"))
time.sleep(2)

client.query(optout_signal.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/OptOutPreferenceSignal.csv"))
time.sleep(2)

client.query(administrative_fine.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/AdministrativeFine.csv"))
time.sleep(2)

client.query(data_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/DataBreach.csv"))
time.sleep(2)

client.query(consumer_request.replace('$file_path',""))
time.sleep(2)

client.query(verification_method.replace('$file_path',""))
time.sleep(2)

client.query(denial_reason.replace('$file_path',""))
time.sleep(2)

client.query(retention_schedule.replace('$file_path',""))
time.sleep(2)

client.query(exemption.replace('$file_path',""))
time.sleep(2)

client.query(commercial_purpose.replace('$file_path',""))
time.sleep(2)

client.query(contract_clause.replace('$file_path',""))
time.sleep(2)

client.query(transparency_report.replace('$file_path',""))
time.sleep(2)



#Relationships
client.query(regulation_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Regulation_Sections.csv"))
time.sleep(2)

client.query(section_subdivision)
time.sleep(2)

client.query(section_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Requirements.csv"))
time.sleep(2)

client.query(section_right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Rights.csv"))
time.sleep(2)

client.query(section_enforcement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Enforcement.csv"))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Data.csv"))
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Safeguards.csv"))
time.sleep(2)

client.query(requirement_event.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Events_Updated.csv"))
time.sleep(2)

client.query(requirement_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Controls.csv"))
time.sleep(2)


client.query(requirement_enforcement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Enforcement_Links.csv"))
time.sleep(2)

client.query(role_right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Role_Rights.csv"))
time.sleep(2)

client.query(requirement_contract.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Contract_Corrected.csv"))
time.sleep(2)

client.query(subdivision_paragraph)
time.sleep(2)

client.query(business_threshold)
time.sleep(2)

client.query(consumer_right)
time.sleep(2)

client.query(business_consumer)
time.sleep(2)

client.query(business_service_provider)
time.sleep(2)

client.query(business_contractor)
time.sleep(2)

client.query(business_thirdparty)
time.sleep(2)

client.query(enforcement_authority_business)
time.sleep(2)

client.query(enforcement_authority_service_provider)
time.sleep(2)

client.query(enforcement_authority_contractor)
time.sleep(2)

client.query(personal_information_pi_category)
time.sleep(2)

client.query(sensitive_personal_information_spi_category)
time.sleep(2)

client.query(sensitive_personal_information_right)
time.sleep(2)

client.query(business_processing_activity)
time.sleep(2)

client.query(processing_activity_business_purpose)
time.sleep(2)

client.query(business_notice_at_collection)
time.sleep(2)

client.query(business_privacy_policy)
time.sleep(2)

client.query(business_risk_assessment)
time.sleep(2)

client.query(privacy_policy_processing_activity)
time.sleep(2)

client.query(business_cybersecurity_audit)
time.sleep(2)

client.query(business_optout_link)
time.sleep(2)

client.query(business_optout_signal)
time.sleep(2)

client.query(business_administrative_fine)
time.sleep(2)

client.query(enforcement_authority_risk_assessment)
time.sleep(2)

client.query(enforcement_authority_cybersecurity_audit)
time.sleep(2)

client.query(consumer_data_breach)
time.sleep(2)

client.query(consumer_initiates_request)
time.sleep(2)

client.query(request_invokes_right)
time.sleep(2)

client.query(request_verified_by)
time.sleep(2)

client.query(request_denied_because)
time.sleep(2)

client.query(pi_category_retention)
time.sleep(2)

client.query(business_claims_exemption)
time.sleep(2)

client.query(data_falls_under_exemption)
time.sleep(2)

client.query(activity_commercial_purpose)
time.sleep(2)

client.query(commercial_purpose_link)
time.sleep(2)

client.query(sp_bound_by_clause)
time.sleep(2)

client.query(business_transparency)
time.sleep(2)

client.query(title_section)
time.sleep(2)

client.query(processing_activity_pi)
time.sleep(2)

client.query(processing_activity_spi)
time.sleep(2)

client.query(business_admt)
time.sleep(2)

client.query(admt_risk_assessment)
time.sleep(2)

client.query(admt_processing)
time.sleep(2)

client.query(contractor_clause)
time.sleep(2)

client.query(activity_third_party)
time.sleep(2)

client.query(business_breach)
time.sleep(2)

client.query(breach_pi)
time.sleep(2)

client.query(authority_breach)
time.sleep(2)

client.query(consumer_signal)
time.sleep(2)

client.query(activity_risk)
time.sleep(2)

client.query(action_fine)
time.sleep(2)

client.query(regulation_threshold)
time.sleep(2)


logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:RegionalStandardAndRegulation)-[*]->()
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
with open('cpra.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to cpra.json")


client.close()





