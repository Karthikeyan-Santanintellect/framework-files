#Regulation

regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(reg:RegionalStandardAndRegulation {regional_standard_regulation_id: "VCDPA 2023"})
ON CREATE SET
  reg.name = row.name,
  reg.citation =row.citation,
  reg.version = row.version,
  reg.status = row.status,
  reg.effective_date = row.effective_date,
  reg.jurisdiction = row.jurisdiction,
  reg.description = row.description;
"""

#title
title = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Title {
    regional_standard_regulation_id: 'VCDPA 2023',
    title_id: row.title_id
})
ON CREATE SET
    t.number = row.title_number,
    t.name = row.name,
    t.citation = row.citation,
    t.description = row.description;
"""
#chapter
chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ch:Chapter {
    regional_standard_regulation_id: 'VCDPA 2023',
    chapter_id: row.chapter_id
})
ON CREATE SET
    ch.number = row.chapter_number,
    ch.name = row.name,
    ch.citation = row.citation,
    ch.description = row.description;
"""

#section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {
    regional_standard_regulation_id: 'VCDPA 2023',
    section_id: row.section_id
})
ON CREATE SET
    sec.full_citation = row.full_citation,
    sec.heading = row.heading,
    sec.text = row.text,
    sec.topic = row.topic;
"""
#subsection
subsection = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sub:Subsection {
    regional_standard_regulation_id: 'VCDPA 2023',
    subsection_id: row.subsection_id
})
ON CREATE SET
    sub.section_id = row.section_id,
    sub.label = row.label,          
    sub.text = row.text;
"""


#Requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
ON CREATE SET
    req.section_id = row.section_id,
    req.text = row.requirement_text,
    req.type = row.requirement_type,
    req.priority = row.priority,
    req.status = row.status,
    req.deadline = row.deadline,
    req.extendable = CASE WHEN row.extendable = 'Yes' THEN true ELSE false END,
    req.extension_period = row.extension_period;
"""
#Role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.role_id})
ON CREATE SET
    ro.name = row.name,
    ro.description = row.description,
    ro.threshold = row.threshold;
"""

#Data Category
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id: 'VCDPA 2023', data_id: row.data_id})
ON CREATE SET
    dc.type = row.category_type,
    dc.name = row.name,
    dc.description = row.description,
    dc.definition_section = row.definition_section,
    dc.requires_consent = CASE WHEN row.requires_consent = 'Yes' THEN true ELSE false END;
"""
#Event_Type
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id: 'VCDPA 2023', event_type_id: row.event_type_id})
ON CREATE SET
    et.name = row.name,
    et.description = row.description,
    et.deadline = row.deadline,
    et.extendable = CASE WHEN row.extendable = 'Yes' THEN true ELSE false END,
    et.extension_period = row.extension_period,
    et.cost = row.cost;
"""
#Safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_regulation_id: 'VCDPA 2023', safeguard_id: row.safeguard_id})
ON CREATE SET
    sg.name = row.name,
    sg.description = row.description,
    sg.type = row.type,
    sg.applies_to = row.applies_to_section;
"""
#enforcement_action
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_regulation_id: 'VCDPA 2023', enforcement_id: row.enforcement_id})
ON CREATE SET
    ea.type = row.type,
    ea.authority = row.authority,
    ea.violation_amount = row.violation_amount,
    ea.description = row.description,
    ea.section = row.section,
    ea.cure_period = row.cure_period,
    ea.private_right_of_action = CASE WHEN row.private_right_of_action = 'Yes' THEN true ELSE false END;
"""
#data_protection_assessment
data_protection_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023', dpa_id: row.dpa_id})
ON CREATE SET
    dpa.trigger = row.trigger,
    dpa.description = row.description,
    dpa.section = row.section,
    dpa.required_elements = row.required_elements;
"""
#implementation_spec
implementation_spec = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ispec:ImplementationSpec {regional_standard_regulation_id: 'VCDPA 2023', impl_id: row.impl_id})
ON CREATE SET
    ispec.requirement_id = row.requirement_id,
    ispec.name = row.name,
    ispec.description = row.description,
    ispec.owner = row.owner;
"""
#policy
policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {regional_standard_regulation_id: 'VCDPA 2023', policy_id: row.policy_id})
ON CREATE SET
    pol.name = row.name,
    pol.description = row.description,
    pol.owner = row.owner,
    pol.version = row.version,
    pol.effective_date = row.effective_date;
"""
#control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_regulation_id: 'VCDPA 2023', control_id: row.control_id})
ON CREATE SET
    co.name = row.name,
    co.description = row.description,
    co.category = row.category,
    co.owner = row.owner;
"""
#system
system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sy:System {regional_standard_regulation_id: 'VCDPA 2023', system_id: row.system_id})
ON CREATE SET
    sy.name = row.name,
    sy.type = row.type,
    sy.description = row.description,
    sy.owner = row.owner,
    sy.personal_data = CASE WHEN row.holds_personal_data = 'Yes' THEN true ELSE false END,
    sy.sensitive_data = CASE WHEN row.holds_sensitive_data = 'Yes' THEN true ELSE false END,
    sy.activities = row.processing_activities;
"""
#process
process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pro:Process {regional_standard_regulation_id: 'VCDPA 2023', process_id: row.process_id})
ON CREATE SET
    pro.name = row.name,
    pro.description = row.description,
    pro.owner = row.owner,
    pro.frequency = row.frequency,
    pro.deadline = row.deadline;
"""
#External Framework Requirements
External_Framework_Requirements ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (efr:ExternalFrameworkRequirement {regional_standard_regulation_id: 'VCDPA 2023', external_id: row.external_id})
ON CREATE SET
    efr.source_framework = row.source_framework,
    efr.text = row.text;
"""
#threshold
Threshold = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (th:Threshold {regional_standard_regulation_id: 'VCDPA 2023', threshold_id: row.threshold_id})
ON CREATE SET
    th.type = row.type,
    th.name = row.name,
    th.description = row.description,
    th.condition = row.condition,
    th.section = row.section;
"""
#Exemption
Exemption ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:Exemption {regional_standard_regulation_id: 'VCDPA 2023', exemption_id: row.exemption_id})
ON CREATE SET
    ex.type = row.type,
    ex.name = row.name,
    ex.description = row.description,
    ex.section = row.section;
"""
#definition
definition = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (def:Definition {
    regional_standard_regulation_id: 'VCDPA 2023',
    definition_id: row.definition_id
})
ON CREATE SET
    def.term = row.term,
    def.text = row.text,
    def.section_id = row.section_id;
"""
#consumer
consumer = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Consumer {
    regional_standard_regulation_id: 'VCDPA 2023',
    consumer_id: row.consumer_id
})
ON CREATE SET
    c.description = row.description,
    c.scope = row.scope;   
"""

#controller
controller = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Controller {
    regional_standard_regulation_id: 'VCDPA 2023',
    controller_id: row.controller_id
})
ON CREATE SET
    ctrl.name = row.name,
    ctrl.description = row.description,
    ctrl.industry = row.industry;
"""
#processor
processor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (proc:Processor {
    regional_standard_regulation_id: 'VCDPA 2023',
    processor_id: row.processor_id
})
ON CREATE SET
    proc.name = row.name,
    proc.description = row.description,
    proc.services = row.services;
"""
#third party
third_party = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tp:ThirdParty {
    regional_standard_regulation_id: 'VCDPA 2023',
    third_party_id: row.third_party_id
})
ON CREATE SET
    tp.name = row.name,
    tp.description = row.description;
"""
#attorney general
attorney_general = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ag:AttorneyGeneral {
    regional_standard_regulation_id: 'VCDPA 2023',
    ag_id: row.ag_id
})
ON CREATE SET
    ag.name = row.name,
    ag.jurisdiction = row.jurisdiction,
    ag.description = row.description;
"""
#employee
employee = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:Employee {
    regional_standard_regulation_id: 'VCDPA 2023',
    employee_id: row.employee_id
})
ON CREATE SET
    e.description = row.description;
"""
#commercial_entity
commercial_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ce:CommercialEntity {
    regional_standard_regulation_id: 'VCDPA 2023',
    entity_id: row.entity_id
})
ON CREATE SET
    ce.description = row.description;
"""
#right 
right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Right {
    regional_standard_regulation_id: 'VCDPA 2023',
    right_id: row.right_id
})
ON CREATE SET
    r.name = row.name,                
    r.description = row.description,
    r.section_id = row.section_id;    
"""
#personal data
personal_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pd:PersonalData {
    regional_standard_regulation_id: 'VCDPA 2023',
    personal_data_id: row.personal_data_id
})
ON CREATE SET
    pd.name = row.name,
    pd.description = row.description;
"""

#sensitive data
sensitive_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sd:SensitiveData {
    regional_standard_regulation_id: 'VCDPA 2023',
    sensitive_data_id: row.sensitive_data_id
})
ON CREATE SET
    sd.name = row.name,
    sd.description = row.description;
"""

#sensitive category
sensitive_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:SensitiveCategory {
    regional_standard_regulation_id: 'VCDPA 2023',
    sensitive_category_id: row.sensitive_category_id
})
ON CREATE SET
    sc.name = row.name,
    sc.description = row.description;
"""
#deidentified_data
deidentified_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dd:DeidentifiedData {
    regional_standard_regulation_id: 'VCDPA 2023',
    deid_id: row.deid_id
})
ON CREATE SET
    dd.description = row.description;
"""
#public_data
public_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pub:PubliclyAvailableInformation {
    regional_standard_regulation_id: 'VCDPA 2023',
    public_id: row.public_id
})
ON CREATE SET
    pub.description = row.description;
"""
#processing_activity
processing_activity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {
    regional_standard_regulation_id: 'VCDPA 2023',
    processing_id: row.processing_id
})
ON CREATE SET
    pa.name = row.name,
    pa.type = row.type,             
    pa.description = row.description;
"""

#privacy notice
privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PrivacyNotice {
    regional_standard_regulation_id: 'VCDPA 2023',
    notice_id: row.notice_id
})
ON CREATE SET
    pn.name = row.name,
    pn.description = row.description,
    pn.section_id = row.section_id;
"""

#consent
consent = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (con:Consent {
    regional_standard_regulation_id: 'VCDPA 2023',
    consent_id: row.consent_id
})
ON CREATE SET
    con.type = row.type,        
    con.description = row.description;
"""
#opt_in_consent
opt_in_consent = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oc:OptInConsent {
    regional_standard_regulation_id: 'VCDPA 2023',
    optin_id: row.optin_id
})
ON CREATE SET
    oc.description = row.description;
"""
#security_measures
security_measures = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sm:SecurityMeasures {
    regional_standard_regulation_id: 'VCDPA 2023',
    security_id: row.security_id
})
ON CREATE SET
    sm.description = row.description,
    sm.section_id = row.section_id;
"""
#rights_request_process
rights_request_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rrp:RightsRequestProcess {
    regional_standard_regulation_id: 'VCDPA 2023',
    process_id: row.process_id
})
ON CREATE SET
    rrp.name = row.name,
    rrp.description = row.description;
"""
#duty 
duty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (du:Duty {
    regional_standard_regulation_id: 'VCDPA 2023',
    duty_id: row.duty_id
})
ON CREATE SET
    du.type = row.type,          
    du.description = row.description;
"""
#opt_out_mechanism
opt_out_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oom:OptOutMechanism {
    regional_standard_regulation_id: 'VCDPA 2023',
    mechanism_id: row.mechanism_id
})
ON CREATE SET
    oom.name = row.name,
    oom.description = row.description;
"""
#violation_notice
violation_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vn:ViolationNotice {
    regional_standard_regulation_id: 'VCDPA 2023',
    notice_id: row.notice_id
})
ON CREATE SET
    vn.description = row.description;
"""
#civil_penalty
civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cp:CivilPenalty {
    regional_standard_regulation_id: 'VCDPA 2023',
    penalty_id: row.penalty_id
})
ON CREATE SET
    cp.amount = row.amount,
    cp.description = row.description;
"""

#civil_investigative_demand
civil_investigative_demand = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cid:CivilInvestigativeDemand {
    regional_standard_regulation_id: 'VCDPA 2023',
    cid_id: row.cid_id
})
ON CREATE SET
    cid.description = row.description;
"""
#injunction
injunction = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (inj:Injunction {
    regional_standard_regulation_id: 'VCDPA 2023',
    injunction_id: row.injunction_id
})
ON CREATE SET
    inj.description = row.description;
"""

#cure_period 
cure_period = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cpd:CurePeriod {
    regional_standard_regulation_id: 'VCDPA 2023',
    cure_id: row.cure_id
})
ON CREATE SET
    cpd.duration = row.duration,       
    cpd.description = row.description;
"""

#Data_processing_agreement
data_processing_agreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpaa:DataProcessingAgreement {
    regional_standard_regulation_id: 'VCDPA 2023',
    contract_id: row.contract_id
})
ON CREATE SET
    dpaa.name = row.name,
    dpaa.effective_date = row.effective_date,
    dpaa.status = row.status,
    dpaa.required_terms = row.required_terms; 
"""
#AppealMechanism
appeal_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (am:AppealMechanism {
    regional_standard_regulation_id: 'VCDPA 2023', 
    appeal_id: row.appeal_id
})
ON CREATE SET 
    am.process_name = row.process_name,
    am.timeline = row.timeline, 
    am.escalation_authority = row.escalation_authority;
"""
# DenialReason
denial_reason = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dr:DenialReason {
    regional_standard_regulation_id: 'VCDPA 2023',
    reason_id: row.reason_id
})
ON CREATE SET
    dr.description = row.description, 
    dr.legal_basis = row.legal_basis;
"""
# risk
risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rk:Risk {
    regional_standard_regulation_id: 'VCDPA 2023',
    risk_id: row.risk_id
})
ON CREATE SET
    rk.name = row.name, 
    rk.severity = row.severity,
    rk.description = row.description;
"""

# Benefit
benefit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (b:Benefit {
    regional_standard_regulation_id: 'VCDPA 2023',
    benefit_id: row.benefit_id
})
ON CREATE SET
    b.name = row.name,
    b.recipient = row.recipient; 
"""
# DarkPattern
dark_pattern = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DarkPattern {
    regional_standard_regulation_id: 'VCDPA 2023', 
    pattern_id: row.pattern_id
})
ON CREATE SET 
    dp.name = row.name, 
    dp.description = row.description,
    dp.effect = row.effect;
"""
# CureStatement
cure_statement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:CureStatement {
    regional_standard_regulation_id: 'VCDPA 2023', 
    statement_id: row.statement_id
})
ON CREATE SET 
    cs.required_content = row.required_content, 
    cs.submission_target = row.submission_target;
"""

# Child (Subtype of Consumer)
child = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (chl:Child {
    regional_standard_regulation_id: 'VCDPA 2023', 
    child_id: row.child_id
})
ON CREATE SET 
    chl.age_threshold = row.age_threshold,
    chl.coppa_trigger = CASE WHEN toLower(row.coppa_trigger) = 'true' THEN true ELSE false END,
    chl.description = row.description;
"""

# Affilate
affilate = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (aff:Affiliate {regional_standard_regulation_id: 'VCDPA 2023', affiliate_id: row.affiliate_id})
ON CREATE SET 
    aff.name = row.name, 
    aff.relationship = row.relationship;
"""
# Department
department = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dept:Department {regional_standard_regulation_id: 'VCDPA 2023', dept_id: row.dept_id})
ON CREATE SET 
    dept.name = row.name, 
    dept.owner = row.owner; 
"""
# Sub_Processor
sub_processor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (subp:Subprocessor {regional_standard_regulation_id: 'VCDPA 2023', sub_id: row.sub_id})
ON CREATE SET 
    subp.name = row.name, 
    subp.service_type = row.service_type;
"""

# Exempted_purpose
exempted_purpose = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ep:ExemptedPurpose {regional_standard_regulation_id: 'VCDPA 2023', purpose_id: row.purpose_id})
ON CREATE SET 
    ep.description = row.description;
"""
# Pseudonymous_data
pseudonymous_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (psd:PseudonymousData {regional_standard_regulation_id: 'VCDPA 2023', pseudo_id: row.pseudo_id})
ON CREATE SET 
    psd.controls = row.controls;
"""
# Authentication_method
authenication_method = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (auth:AuthenticationMethod {regional_standard_regulation_id: 'VCDPA 2023', auth_id: row.auth_id})
ON CREATE SET 
    auth.type = row.type;
"""
# DPA Trigger
dpa_trigger = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (trig:DPATrigger {regional_standard_regulation_id: 'VCDPA 2023', trigger_id: row.trigger_id})
ON CREATE SET 
    trig.condition = row.condition; 
"""





# Relationships 
#Regulation → Section
regulation_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: row.regulation_id})
MATCH (sec:Section {regional_standard_regulation_id: row.regulation_id, section_id: row.section_id})
MERGE (reg)-[:REGULATION_HAS_SECTION]->(sec);
"""

#Section → Requirement
section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023',section_id : row.section_id})
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MERGE (sec)-[:SECTION_HAS_REQUIREMENT]->(req);
"""
#Requirement → Role
requirement_role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (ro:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.role_id})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_ROLE {applicability: row.applicability}]->(ro);
"""
#Requirement → DataCategory
requirement_datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'VCDPA 2023', data_id: row.data_id})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_DATA {scope: row.scope}]->(dc);
"""
#Requirement → EventType
requirement_event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (et:EventType {regional_standard_regulation_id: 'VCDPA 2023', event_type_id: row.event_type_id})
MERGE (req)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE {trigger_condition: row.trigger_condition}]->(et);
"""
#Role → ThresholdDefinition
role_threshold ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ro:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.role_id})
MATCH (th:Threshold {regional_standard_regulation_id: 'VCDPA 2023', threshold_id: row.threshold_id})
MERGE (ro)-[:ROLE_MEETS_THRESHOLD {status: row.status}]->(th);
"""
#Role → Exemption
role_exemption ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ro:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.role_id})
MATCH (ex:Exemption {regional_standard_regulation_id: 'VCDPA 2023', exemption_id: row.exemption_id})
MERGE (ro)-[:ROLE_QUALIFIES_FOR_EXEMPTION {exemption_type: row.exemption_type}]->(ex);
"""
#Requirement → Safeguard
requirement_safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (sg:Safeguard {regional_standard_regulation_id: 'VCDPA 2023', safeguard_id: row.safeguard_id})
MERGE (req)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg);
"""
#Requirement → Policy
requirement_policy ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (pol:Policy {regional_standard_regulation_id: 'VCDPA 2023', policy_id: row.policy_id})
MERGE (req)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(pol);
"""
#Requirement → Control
requirement_control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (co:Control {regional_standard_regulation_id: 'VCDPA 2023', control_id: row.control_id})
MERGE (req)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co);
"""
#Control → System
control_system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:Control {regional_standard_regulation_id: 'VCDPA 2023', control_id: row.control_id})
MATCH (sy:System {regional_standard_regulation_id: 'VCDPA 2023', system_id: row.system_id})
MERGE (co)-[:CONTROL_IMPLEMENTED_IN_SYSTEM]->(sy);
"""
#Requirement → Process
requirement_process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (pro:Process {regional_standard_regulation_id: 'VCDPA 2023', process_id: row.process_id})
MERGE (req)-[:REQUIREMENT_IMPACTS_PROCESS]->(pro);
"""
#Process → System
process_system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pro:Process {regional_standard_regulation_id: 'VCDPA 2023', process_id: row.process_id})
MATCH (sy:System {regional_standard_regulation_id: 'VCDPA 2023', system_id: row.system_id})
MERGE (pro)-[:PROCESS_SUPPORTED_BY_SYSTEM]->(sy);
"""
#Requirement → DataProtectionAssessment
requirement_dataprotectionassessment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023', dpa_id: row.dpa_id})
MERGE (req)-[:REQUIREMENT_REQUIRES_DATA_PROTECTION_ASSESSMENT {trigger: row.trigger}]->(dpa);
"""
#DPA → Systems
dpa_systems = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023', dpa_id: row.dpa_id})
MATCH (sy:System {regional_standard_regulation_id: 'VCDPA 2023', system_id: row.system_id})
MERGE (dpa)-[:DATA_PROTECTION_ASSESSMENT_APPLIES_SYSTEM]->(sy);
"""
#DPA → Processes
dpa_process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023', dpa_id: row.dpa_id})
MATCH (pro:Process {regional_standard_regulation_id: 'VCDPA 2023', process_id: row.process_id})
MERGE (dpa)-[:DATA_PROTECTION_ASSESSMENT_ASSESSES_PROCESS]->(pro);
"""
#Requirement → EnforcementAction
requirement_enforcementaction = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.requirement_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'VCDPA 2023', enforcement_id: row.enforcement_id})
MERGE (req)-[:REQUIREMENT_ENFORCED_BY_ENFORCEMENT_ACTION]->(ea);
"""
#EnforcementAction → Role
enforcement_action_role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'VCDPA 2023', enforcement_id: row.enforcement_id})
MATCH (ro:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.role_id})
MERGE (ea)-[:ENFORCEMENT_ACTION_APPLIES_TO_ROLE {applicability: row.applicability}]->(ro);
"""
#Section → EnforcementAction
section_enforcement_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023',section_id : row.section_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'VCDPA 2023', enforcement_id: row.enforcement_id})
MERGE (sec)-[:SECTION_DEFINES_ENFORCEMENT_ACTION]->(ea);
"""
#Processor–Controller Relationships
processor_controller = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (proc:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.processor_role_id})
MATCH (ctrl:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.controller_role_id})
MERGE (proc)-[:PROCESSES_ON_BEHALF_OF_CONTROLLER {
  relationship_type: row.relationship_type,
  contractual_basis: row.contractual_basis,
  description: row.description
}]->(ctrl);
"""
#Processor ENGAGES_SUBCONTRACTOR Processor
processor_subcontractor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (proc:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.processor_role_id})
MATCH (subproc:Role {regional_standard_regulation_id: 'VCDPA 2023', role_id: row.subcontractor_role_id})
MERGE (proc)-[:PROCESSOR_ENGAGES_SUBCONTRACTOR {
  authorization_type: row.authorization_type,
  notification_required: row.notification_required,
  description: row.description
}]->(subproc);
"""
#Cross‑Framework Mapping
requirement_external_frameworks ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id: 'VCDPA 2023', requirement_id: row.source_requirement_id})
MATCH (efr:ExternalFrameworkRequirement {regional_standard_regulation_id: 'VCDPA 2023', external_id: row.target_requirement_id})
MERGE (req)-[r:REQUIREMENT_MAPPED_TO_EXTERNAL_FRAMEWORK]->(efr)
ON CREATE SET
    r.source_framework = row.source_framework,
    r.target_framework = row.target_framework,
    r.strength = row.strength,
    r.justification = row.justification,
    r.mapping_type = row.mapping_type;
"""

# Regulation → Title
regulation_title = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (t:Title {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (reg)-[:REGULATION_HAS_TITLE]->(t);
"""

# Title → Chapter
title_chapter = """
MATCH (t:Title {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (ch:Chapter {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (t)-[:TITLE_HAS_CHAPTER]->(ch);
"""

# Chapter → Section
chapter_section_rel = """
MATCH (ch:Chapter {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ch)-[:CHAPTER_HAS_SECTION]->(sec);
"""

# Section → Subsection
section_subsection_rel = """
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (sub:Subsection {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sec)-[:SECTION_HAS_SUBSECTION]->(sub);
"""

# Section → Definition
section_definition_rel = """
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (def:Definition {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sec)-[:SECTION_DEFINES_TERM]->(def);
"""

# Section → Right
section_right_rel = """
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (r:Right {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sec)-[:SECTION_ESTABLISHES_RIGHT]->(r);
"""

# Section → DataProtectionAssessment
section_dpa_rel = """
MATCH (sec:Section {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sec)-[:SECTION_MANDATES_DPA]->(dpa);
"""

# Consumer → Right
consumer_right = """
MATCH (c:Consumer {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (r:Right {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (c)-[:CONSUMER_HAS_RIGHT]->(r);
"""

# Controller → Consumer (Duty)
controller_consumer_duty = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (c:Consumer {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:OWES_DUTY_TO_CONSUMER]->(c);
"""

# Controller → Threshold
controller_threshold = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (th:Threshold {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:CONTROLLER_MEETS_THRESHOLD]->(th);
"""

# Controller → Processor
controller_processor = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (proc:Processor {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:ENGAGES_PROCESSOR]->(proc);
"""

# Controller excludes Employee context
controller_excludes_context = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (e:Employee {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:EXCLUDES_EMPLOYEE_CONTEXT]->(e);
"""

# SensitiveData → PersonalData (Subtype)
sensitive_subtype_of_personal = """
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (pd:PersonalData {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sd)-[:SUBTYPE_OF_PERSONAL_DATA]->(pd);
"""

# SensitiveData → SensitiveCategory
sensitive_includes_category_rel = """
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (sc:SensitiveCategory {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sd)-[:INCLUDES_SENSITIVE_CATEGORY]->(sc);
"""

# SensitiveData → OptInConsent
sensitive_requires_consent_rel = """
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (oc:OptInConsent {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (sd)-[:REQUIRES_OPT_IN_CONSENT]->(oc);
"""

# Controller → ProcessingActivity
controller_processing = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:CONDUCTS_PROCESSING]->(pa);
"""

# ProcessingActivity → DataCategory
processing_operates_on_data = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pa)-[:PROCESSING_OPERATES_ON_DATACATEGORY]->(dc);
"""

# ProcessingActivity → Right (subject to)
processing_subject_to_right = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (r:Right {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pa)-[:PROCESSING_SUBJECT_TO_RIGHT]->(r);
"""

# ProcessingActivity → DataProtectionAssessment
processing_requires_dpa = """
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pa)-[:PROCESSING_REQUIRES_DPA]->(dpa);
"""

# Controller → PrivacyNotice
controller_privacy_notice = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (pn:PrivacyNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:CONTROLLER_PUBLISHES_PRIVACY_NOTICE]->(pn);
"""

# PrivacyNotice → DataCategory
privacy_notice_discloses_datacategory = """
MATCH (pn:PrivacyNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pn)-[:PRIVACY_NOTICE_DISCLOSES_DATACATEGORY]->(dc);
"""

# PrivacyNotice → OptOutMechanism
privacy_notice_optout_mechanism = """
MATCH (pn:PrivacyNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (oom:OptOutMechanism {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pn)-[:PRIVACY_NOTICE_INCLUDES_OPTOUT_MECHANISM]->(oom);
"""

# Controller → OptInConsent
controller_must_obtain_optin = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (oc:OptInConsent {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:CONTROLLER_MUST_OBTAIN_OPTIN_CONSENT]->(oc);
"""

# AttorneyGeneral → Regulation
ag_enforces_regulation = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ENFORCES_REGULATION]->(reg);
"""

# AttorneyGeneral → ViolationNotice
ag_issues_violation_notice = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (vn:ViolationNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ISSUES_VIOLATION_NOTICE]->(vn);
"""

# ViolationNotice → CurePeriod
violation_triggers_cure = """
MATCH (vn:ViolationNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (cpd:CurePeriod {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (vn)-[:VIOLATION_TRIGGERS_CURE_PERIOD]->(cpd);
"""

# AttorneyGeneral → CivilPenalty
ag_seeks_penalty = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (cp:CivilPenalty {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ATTORNEY_GENERAL_CAN_SEEK_CIVIL_PENALTY]->(cp);
"""

# AttorneyGeneral → CivilInvestigativeDemand
ag_can_issue_cid = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (cid:CivilInvestigativeDemand {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ATTORNEY_GENERAL_CAN_ISSUE_CID]->(cid);
"""

# AttorneyGeneral → Injunction
ag_can_seek_injunction = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (inj:Injunction {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ATTORNEY_GENERAL_CAN_SEEK_INJUNCTION]->(inj);
"""

# AttorneyGeneral → DataProtectionAssessment
violation_requests_dpa = """
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ag)-[:ATTORNEY_GENERAL_REQUESTS_DPA_FROM_CONTROLLER]->(dpa);
"""

# Controller -> Contract
controller_contract = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpaa:DataProcessingAgreement {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:CONTROLLER_ESTABLISHES_AGREEMENT]->(dpaa);
"""
# Processor -> Contract
processor_contract = """
MATCH (proc:Processor {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpaa:DataProcessingAgreement {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (proc)-[:PROCESSOR_ESTABLISHES_AGREEMENT]->(dpaa);
"""
# Processor -> Subprocessor
processor_subprocessor = """
MATCH (proc:Processor {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (subp:Subprocessor {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (proc)-[:PROCESSOR_ENGAGES_SUBPROCESSOR {flow_down_obligations: true}]->(subp);
"""
# Affiliate -> Controller
affiliate_controller = """
MATCH (ctrl:Controller {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (aff:Affiliate {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (ctrl)-[:AFFILIATE_CONTROLS_CONTROLLER]->(aff);
"""
#RightsRequestProcess -> AppealMechanism
rights_request_mechanism = """
MATCH (rrp:RightsRequestProcess {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (am:AppealMechanism {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (rrp)-[:RIGHTS_REQUEST_INCLUDES_APPEAL_MECHANISM]->(am);
"""
#AppealMechanism -> DenialReason
appeal_mechanism_denial_reason = """
MATCH (am:AppealMechanism {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dr:DenialReason {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (am)-[:APPEAL_MECHANISM_REVIEWS_DENIAL_REASON]->(dr);
"""
# RightsRequestProcess -> AuthenticationMethod
rights_request_authentication_method = """
MATCH (rrp:RightsRequestProcess {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (auth:AuthenticationMethod {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (rrp)-[:RIGHTS_REQUEST_REQUIRES_AUTHENTICATION]->(auth);
"""
#DPA -> Risk
dpa_risk = """
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (rk:Risk {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (dpa)-[:DATA_PROTECTION_ASSESSMENT_EVALUATES_RISK]->(rk);
"""
# DPA -> Benefit
dpa_benefit = """
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (b:Benefit {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (dpa)-[:DATA_PROTECTION_ASSESSMENT_EVALUATES_BENEFIT]->(b);
"""
# DPATrigger -> DPA
dpa_dpa_trigger = """
MATCH (trig:DPATrigger {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (trig)-[:DPA_TRIGGERS]->(dpa);
"""
# DarkPattern -> Consent
dark_pattern_consent = """
MATCH (dp:DarkPattern {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (con:Consent {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (dp)-[:DARK_PATTERN_INVALIDATES_CONSENT]->(con);
"""
# child_implies_sensitive
child_implies_sensitive = """
MATCH (chl:Child {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (chl)-[:CHILD_IMPLIES_SENSITIVE_DATA]->(sd);
"""
# PseudonymousData -> ExemptedPurpose
pseudonymous_exempted_purpose = """
MATCH (psd:PseudonymousData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (ep:ExemptedPurpose {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (psd)-[:PSEUDONYMOUS_DATA_EXEMPTED_FOR_PURPOSE]->(ep);
"""
# ViolationNotice -> CureStatement
violation_notice_cure_statement = """
MATCH (vn:ViolationNotice {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (cs:CureStatement {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (vn)-[:VIOLATION_NOTICE_RESOLVED_BY_CURE_STATEMENT]->(cs);
"""
#CureStatement -> AttorneyGeneral
cure_statement_attorney_general = """
MATCH (cs:CureStatement {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (ag:AttorneyGeneral {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (cs)-[:CURE_STATEMENT_SUBMITTED_TO_ATTORNEY_GENERAL]->(ag);
"""

# Department -> ProcessingActivity
department_processing_activity = """
MATCH (dept:Department {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (dept)-[:DEPARTMENT_RESPONSIBLE_FOR_ACTIVITY]->(pa);
"""
# Department -> SecurityMeasures
department_security_measures = """
MATCH (dept:Department {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (sm:SecurityMeasures {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (dept)-[:DEPARTMENT_IMPLEMENTS_SAFEGUARDS]->(sm);
"""
# PersonalData -> DeidentifiedData
personal_data_deidentified_data = """
MATCH (pd:PersonalData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (dd:DeidentifiedData {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pd)-[:PERSONAL_DATA_DEIDENTIFIES_DATA]->(dd);
"""
# PersonalData -> PubliclyAvailableInformation
personal_data_publicly_available_information = """
MATCH (pd:PersonalData {regional_standard_regulation_id: 'VCDPA 2023'})
MATCH (pub:PubliclyAvailableInformation {regional_standard_regulation_id: 'VCDPA 2023'})
MERGE (pd)-[:PERSONAL_DATA_EXCLUDES_PUBLIC_INFORMATION]->(pub);
"""




import os
from pydoc import cli
import re
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

client.query(regulation.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Regulation_Node.csv'))
time.sleep(2)

client.query(title.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Title.csv"))
time.sleep(2)

client.query(section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Sections.csv'))
time.sleep(2)

client.query(subsection.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Subsection.csv"))
time.sleep(2)


client.query(requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirements.csv'))
time.sleep(2)

client.query(role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Roles.csv'))
time.sleep(2)


client.query(data_category.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_DataCategories.csv'))
time.sleep(2)

client.query(event_type.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_EventTypes.csv'))
time.sleep(2)

client.query(safeguard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Safeguards.csv'))
time.sleep(2)

client.query(enforcement_action.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_EnforcementActions_Filled.csv'))
time.sleep(2)

client.query(data_protection_assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_DataProtectionAssessments.csv'))
time.sleep(2)

client.query(implementation_spec.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_ImplementationSpecs.csv'))
time.sleep(2)

client.query(policy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Policies.csv'))
time.sleep(2)

client.query(control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Controls.csv'))
time.sleep(2)

client.query(system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Systems.csv'))
time.sleep(2)

client.query(process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Processes.csv'))
time.sleep(2)

client.query(External_Framework_Requirements.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_ExternalFrameworkRequirements.csv'))  
time.sleep(2)

client.query(Threshold.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Thresholds.csv'))
time.sleep(2)

client.query(Exemption.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Exemptions.csv'))
time.sleep(2)

client.query(definition.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Definition.csv"))
time.sleep(2)

client.query(right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Right.csv"))
time.sleep(2)

client.query(consumer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Consumer.csv"))
time.sleep(2)

client.query(duty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Duty.csv"))
time.sleep(2)

client.query(employee.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Employee.csv"))
time.sleep(2)

client.query(sensitive_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/SensitiveData.csv"))
time.sleep(2)

client.query(personal_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/PersonalData.csv"))
time.sleep(2)

client.query(sensitive_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/SensitiveCategory.csv"))
time.sleep(2)

client.query(opt_in_consent.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/OptInConsent.csv"))
time.sleep(2)

client.query(processing_activity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/ProcessingActivity.csv"))
time.sleep(2)

client.query(privacy_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/PrivacyNotice.csv"))
time.sleep(2)

client.query(cure_period.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/CurePeriod.csv"))
time.sleep(2)

client.query(civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/CivilPenalty.csv"))
time.sleep(2)

client.query(civil_investigative_demand.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/CivilInvestigativeDemand.csv"))
time.sleep(2)

client.query(injunction.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Injunction.csv"))
time.sleep(2)

client.query(controller.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Controller.csv"))
time.sleep(2)

client.query(processor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Processor.csv"))
time.sleep(2)

client.query(attorney_general.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/AttorneyGeneral.csv"))
time.sleep(2)

client.query(violation_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/ViolationNotice.csv"))
time.sleep(2)

client.query(chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Chapter.csv"))
time.sleep(2)

client.query(commercial_entity.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/CommercialEntity.csv"))
time.sleep(2)

client.query(deidentified_data.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/DeidentifiedData.csv"))
time.sleep(2)

client.query(public_data.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/PubliclyAvailableInformation.csv"))
time.sleep(2)

client.query(rights_request_process.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/RightsRequestProcess.csv"))
time.sleep(2)

client.query(security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/SecurityMeasures.csv"))
time.sleep(2)

client.query(consent.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/Consent.csv"))
time.sleep(2)

client.query(data_processing_agreement.replace('$file_path', ""))
time.sleep(2)

client.query(appeal_mechanism.replace('$file_path',""))
time.sleep(2)

client.query(denial_reason.replace('$file_path',""))
time.sleep(2)

client.query(risk.replace('$file_path',""))
time.sleep(2)

client.query(benefit.replace('$file_path',""))
time.sleep(2)

client.query(dark_pattern.replace('$file_path',""))
time.sleep(2)

client.query(cure_statement.replace('$file_path',""))
time.sleep(2)

client.query(child.replace('$file_path',""))
time.sleep(2)

client.query(affilate.replace('$file_path',""))
time.sleep(2)

client.query(department.replace('$file_path',""))
time.sleep(2)

client.query(sub_processor.replace('$file_path',""))
time.sleep(2)

client.query(exempted_purpose.replace('$file_path',""))
time.sleep(2)

client.query(pseudonymous_data.replace('$file_path',""))
time.sleep(2)

client.query(authenication_method.replace('$file_path',""))
time.sleep(2)

client.query(dpa_trigger.replace('$file_path',""))
time.sleep(2)











#Relationships
client.query(regulation_section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Regulation_Section_Relationship.csv'))
time.sleep(2)

client.query(section_requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Section_Requirements.csv'))
time.sleep(2)

client.query(requirement_role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Roles.csv'))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Data.csv'))
time.sleep(2)   

client.query(requirement_event_type.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Events.csv'))
time.sleep(2)   

client.query(role_threshold.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Role_Thresholds.csv'))    
time.sleep(2)   

client.query(role_exemption.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Role_Exemptions.csv'))    
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Safeguards.csv'))
time.sleep(2)   

client.query(requirement_policy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Policies.csv'))
time.sleep(2)

client.query(requirement_control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Controls.csv'))
time.sleep(2)

client.query(control_system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Control_Systems.csv'))
time.sleep(2)

client.query(requirement_process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Processes.csv'))
time.sleep(2)

client.query(process_system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Process_Systems.csv'))
time.sleep(2)

client.query(requirement_dataprotectionassessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_DPAs.csv'))
time.sleep(2)

client.query(dpa_systems.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_DPA_Systems.csv'))
time.sleep(2)

client.query(dpa_process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_DPA_Processes.csv'))
time.sleep(2)

client.query(requirement_enforcementaction.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_Enforcement.csv'))
time.sleep(2)

client.query(enforcement_action_role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_EnforcementAction_Roles.csv'))
time.sleep(2)

client.query(section_enforcement_action.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Section_Enforcement.csv'))
time.sleep(2)

client.query(processor_controller.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Processor_Controller.csv'))
time.sleep(2)   

client.query(processor_subcontractor.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Processor_Subcontractor.csv'))
time.sleep(2)  

client.query(requirement_external_frameworks.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/VCDPA/VCDPA_Requirement_ExternalFramework_Mapping.csv'))
time.sleep(2)  

client.query(regulation_title)
time.sleep(2)

client.query(title_chapter)
time.sleep(2)

client.query(chapter_section_rel)
time.sleep(2)

client.query(section_subsection_rel)
time.sleep(2)

client.query(section_definition_rel)
time.sleep(2)

client.query(section_right_rel)
time.sleep(2)

client.query(section_dpa_rel)
time.sleep(2)

client.query(consumer_right)
time.sleep(2)

client.query(controller_consumer_duty)
time.sleep(2)

client.query(controller_threshold)
time.sleep(2)

client.query(controller_processor)
time.sleep(2)

client.query(controller_excludes_context)
time.sleep(2)

client.query(sensitive_subtype_of_personal)
time.sleep(2)

client.query(sensitive_includes_category_rel)
time.sleep(2)

client.query(sensitive_requires_consent_rel)
time.sleep(2)

client.query(controller_processing)
time.sleep(2)

client.query(processing_operates_on_data)
time.sleep(2)

client.query(processing_subject_to_right)
time.sleep(2)

client.query(processing_requires_dpa)
time.sleep(2)

client.query(controller_privacy_notice)
time.sleep(2)

client.query(privacy_notice_discloses_datacategory)
time.sleep(2)

client.query(privacy_notice_optout_mechanism)
time.sleep(2)

client.query(controller_must_obtain_optin)
time.sleep(2)

client.query(ag_enforces_regulation)
time.sleep(2)

client.query(ag_issues_violation_notice)
time.sleep(2)

client.query(violation_triggers_cure)
time.sleep(2)

client.query(ag_seeks_penalty)
time.sleep(2)

client.query(ag_can_issue_cid)
time.sleep(2)

client.query(ag_can_seek_injunction)
time.sleep(2)

client.query(violation_requests_dpa)
time.sleep(2)

client.query(controller_contract)
time.sleep(2)

client.query(processor_contract)
time.sleep(2)

client.query(processor_subprocessor)
time.sleep(2)

client.query(affiliate_controller)
time.sleep(2)

client.query(rights_request_mechanism)
time.sleep(2)

client.query(appeal_mechanism_denial_reason)
time.sleep(2)

client.query(rights_request_authentication_method)
time.sleep(2)

client.query(dpa_risk)
time.sleep(2)

client.query(dpa_benefit)
time.sleep(2)

client.query(dpa_dpa_trigger)
time.sleep(2)

client.query(dark_pattern_consent)
time.sleep(2)

client.query(child_implies_sensitive)
time.sleep(2)

client.query(pseudonymous_exempted_purpose)
time.sleep(2)

client.query(violation_notice_cure_statement)
time.sleep(2)

client.query(cure_statement_attorney_general)
time.sleep(2)

client.query(department_processing_activity)
time.sleep(2)

client.query(department_security_measures)
time.sleep(2)

client.query(personal_data_deidentified_data)
time.sleep(2)

client.query(personal_data_publicly_available_information)
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
    with open('vcdpa.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to vcdpa.json")
else:
    logger.error("No data returned from the query.")

client.close()

















