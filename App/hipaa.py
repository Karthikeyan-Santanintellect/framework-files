

#industry_standard_and_regulation
industry_standard_and_regulation = """
MERGE(i:IndustryStandardAndRegulation{industry_standard_regulation_id:'HIPAA 1996'})
ON CREATE SET
    i.name='HIPAA',
    i.description='The Health Insurance Portability and Accountability Act (HIPAA) is a US regulation that sets standards for protecting sensitive patient health information.',
    i.url='https://www.hhs.gov/hipaa/index.html',
    i.abbreviation='Health Insurance Portability and Accountability Act',
    i.version='1996',
    i.published_date='1996-08-21',
    i.type='Regulation';
"""

# SUBGRAPH 1: LEGAL STRUCTURE & FRAMEWORK (4 NODES)
# 1.1 Load CFR Sections
cfr_sections ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cfr:CFRSection {cfr_section_id: row.cfr_section_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    cfr.cfr_part = row.cfr_part,
    cfr.cfr_subpart = row.cfr_subpart,
    cfr.cfr_section = row.cfr_section,
    cfr.title = row.title,
    cfr.description = row.description,
    cfr.legal_authority = row.legal_authority,
    cfr.url = row.url,
    cfr.full_citation = row.full_citation;
"""

# 1.2 Load Regulatory Standards
regulatory_standards ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rs:RegulatoryStandard {standard_id: row.standard_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    rs.title = row.title,
    rs.description = row.description,
    rs.standard_type = row.standard_type,
    rs.applicability_scope = row.applicability_scope,
    rs.cfr_citation = row.cfr_citation,
    rs.mandatory_status = row.mandatory_status,
    rs.parent_rule = row.parent_rule;
"""

# 1.3 Load Compliance Requirements
Compliance_Requirements ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cr:ComplianceRequirement {requirement_id: row.requirement_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    cr.description = row.description,
    cr.obligation_type = row.obligation_type,
    cr.applicable_entities = row.applicable_entities,
    cr.enforcement_basis = row.enforcement_basis,
    cr.cfr_citation = row.cfr_citation,
    cr.standard_id = row.standard_id,
    cr.mandatory = row.mandatory;
"""

# 1.4 Load Implementation Specifications
Implementation_Specifications ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (is:ImplementationSpecification {spec_id: row.spec_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    is.title = row.title,
    is.description = row.description,
    is.requirement_type = row.requirement_type,
    is.addressable = row.addressable,
    is.standard_id = row.standard_id,
    is.cfr_citation = row.cfr_citation,
    is.implementation_guidance = row.implementation_guidance;
"""

# SUBGRAPH 2: PROTECTED HEALTH INFORMATION (12 NODES)

# 2.1 Load Electronic PHI
Electronic_PHI ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ephi:ElectronicPHI {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ephi.name = row.name,
    ephi.description = row.description,
    ephi.storage_format = row.storage_format,
    ephi.transmission_method = row.transmission_method,
    ephi.encryption_required = row.encryption_required,
    ephi.sensitivity_level = row.sensitivity_level,
    ephi.cfr_citation = row.cfr_citation;
"""

# 2.2 Load PHI Categories
PHI_Categories ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pc:PHICategory {category_id: row.category_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pc.name = row.name,
    pc.description = row.description,
    pc.examples = row.examples,
    pc.sensitivity_level = row.sensitivity_level,
    pc.cfr_citation = row.cfr_citation
ON MATCH SET
    pc.description = row.description,
    pc.examples = row.examples;
"""

# 2.3 Load PHI Forms
PHI_Forms ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pf:PHIForm {form_id: row.form_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pf.name = row.name,
    pf.format = row.format,
    pf.description = row.description,
    pf.examples = row.examples,
    pf.cfr_citation = row.cfr_citation;
"""


# 2.4 Load PHI Locations
PHI_Locations ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pl:PHILocation {location_id: row.location_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pl.name = row.name,
    pl.location_type = row.location_type,
    pl.description = row.description,
    pl.security_requirements = row.security_requirements,
    pl.cfr_citation = row.cfr_citation;
"""

# 2.5 Load Sensitive Data Elements
sensitive_data_elements ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sde:SensitiveDataElement {element_id: row.element_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sde.name = row.name,
    sde.description = row.description,
    sde.data_type = row.data_type,
    sde.identifier_type = row.identifier_type,
    sde.protected = row.protected,
    sde.cfr_citation = row.cfr_citation;
"""

# 2.6 Load PHI Lifecycle
PHI_Lifecycle ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (plc:PHILifecycle {lifecycle_id: row.lifecycle_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    plc.stage_name = row.stage_name,
    plc.description = row.description,
    plc.safeguards_required = row.safeguards_required,
    plc.sequence_order = row.sequence_order,
    plc.cfr_citation = row.cfr_citation;
"""

# 2.7 Load Data Uses
data_uses ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (du:DataUse {use_id: row.use_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    du.name = row.name,
    du.description = row.description,
    du.use_type = row.use_type,
    du.authorization_required = row.authorization_required,
    du.permitted_without_authorization = row.permitted_without_authorization,
    du.cfr_citation = row.cfr_citation;
"""
# 2.8 Load Data Disclosures
data_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dd:DataDisclosure {disclosure_id: row.disclosure_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    dd.name = row.name,
    dd.description = row.description,
    dd.disclosure_type = row.disclosure_type,
    dd.recipient_type = row.recipient_type,
    dd.authorization_required = row.authorization_required,
    dd.cfr_citation = row.cfr_citation;
"""

# 2.9 Load Minimum Necessary
minimum_necessary = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mn:MinimumNecessary {principle_id: row.principle_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    mn.name = row.name,
    mn.description = row.description,
    mn.principle = row.principle,
    mn.exceptions = row.exceptions,
    mn.cfr_citation = row.cfr_citation,
    mn.applies_to = row.applies_to;
"""

# 2.10 Load De-Identified Health Information
de_indentified_health_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dhi:DeidentifiedHealthInfo {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    dhi.name = row.name,
    dhi.description = row.description,
    dhi.deidentification_method = row.deidentification_method,
    dhi.identifiers_removed_count = row.identifiers_removed_count,
    dhi.hipaa_protected = row.hipaa_protected,
    dhi.cfr_citation = row.cfr_citation;
"""

# 2.11 Load Limited Data Set
limited_data_set = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lds:LimitedDataSet {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    lds.name = row.name,
    lds.description = row.description,
    lds.permitted_uses = row.permitted_uses,
    lds.excluded_identifiers = row.excluded_identifiers,
    lds.requires_data_use_agreement = row.requires_data_use_agreement,
    lds.cfr_citation = row.cfr_citation;
"""

# 2.12 Load Data Use Agreement
data_use_agreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dua:DataUseAgreement {agreement_id: row.agreement_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    dua.name = row.name,
    dua.description = row.description,
    dua.required_provisions = row.required_provisions,
    dua.prohibitions = row.prohibitions,
    dua.cfr_citation = row.cfr_citation;
"""

# SUBGRAPH 3: PRIVACY RULE & INDIVIDUAL RIGHTS (10 NODES)

# 3.1 Load Individual Rights
individual_rights = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:IndividualRight {right_id: row.right_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ir.name = row.name,
    ir.description = row.description,
    ir.right_type = row.right_type,
    ir.cfr_citation = row.cfr_citation,
    ir.timeline_for_response = row.timeline_for_response,
    ir.fees_allowed = row.fees_allowed;
"""

# 3.2 Load Data Subjects
data_subjects = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ds:DataSubject {subject_id: row.subject_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ds.subject_type = row.subject_type,
    ds.description = row.description,
    ds.rights = row.rights,
    ds.cfr_citation = row.cfr_citation;
"""

# 3.3 Load Use and Disclosures
use_and_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ud:UseAndDisclosure {disclosure_id: row.disclosure_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ud.name = row.name,
    ud.use_disclosure_type = row.use_disclosure_type,
    ud.authorization_status = row.authorization_status,
    ud.permitted_use = row.permitted_use,
    ud.cfr_citation = row.cfr_citation,
    ud.conditions = row.conditions;
"""

# 3.4 Load Authorizations
authorizations = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (auth:Authorization {authorization_id: row.authorization_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    auth.description = row.description,
    auth.required_elements = row.required_elements,
    auth.expiration_rules = row.expiration_rules,
    auth.revocation_allowed = row.revocation_allowed,
    auth.cfr_citation = row.cfr_citation,
    auth.valid_for = row.valid_for;
"""

# 3.5 Load Lawful Basis
lawful_basis = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lb:LawfulBasis {basis_id: row.basis_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    lb.name = row.name,
    lb.basis_type = row.basis_type,
    lb.description = row.description,
    lb.legal_authority = row.legal_authority,
    lb.cfr_citation = row.cfr_citation;
"""

# 3.6 Load Patient Requests
patient_requests = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pr:PatientRequest {request_id: row.request_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pr.request_type = row.request_type,
    pr.description = row.description,
    pr.response_timeline = row.response_timeline,
    pr.fees_allowed = row.fees_allowed,
    pr.cfr_citation = row.cfr_citation;
"""
# 3.7 Load Privacy Complaints
privacy_complaints = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pcom:PrivacyComplaint {complaint_id: row.complaint_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pcom.complaint_type = row.complaint_type,
    pcom.description = row.description,
    pcom.filing_process = row.filing_process,
    pcom.investigation_required = row.investigation_required,
    pcom.cfr_citation = row.cfr_citation;
"""

# 3.8 Load Privacy Notices
privacy_notices = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PrivacyNotice {notice_id: row.notice_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    pn.name = row.name,
    pn.description = row.description,
    pn.required_content = row.required_content,
    pn.distribution_method = row.distribution_method,
    pn.cfr_citation = row.cfr_citation;
"""

# 3.9 Load Psychotherapy Notes
psychotherapy_notes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ptn:PsychotherapyNotes {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ptn.name = row.name,
    ptn.description = row.description,
    ptn.protection_level = row.protection_level,
    ptn.authorization_required = row.authorization_required,
    ptn.exceptions = row.exceptions,
    ptn.cfr_citation = row.cfr_citation;
"""

# 3.10 Load Marketing Authorizations
marketing_authorization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ma:MarketingAuthorization {authorization_id: row.authorization_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ma.name = row.name,
    ma.description = row.description,
    ma.remuneration_disclosure_required = row.remuneration_disclosure_required,
    ma.exceptions = row.exceptions,
    ma.cfr_citation = row.cfr_citation;
"""
# SUBGRAPH 4: SECURITY RULE & SAFEGUARDS (12 NODES)

# 4.1 Load Security Standards
security_standards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ss:SecurityStandard {standard_id: row.standard_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ss.title = row.title,
    ss.description = row.description,
    ss.standard_type = row.standard_type,
    ss.safeguard_category = row.safeguard_category,
    ss.required_addressable = row.required_addressable,
    ss.cfr_citation = row.cfr_citation;
"""

# 4.2 Load Administrative Safeguards
administrative_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (as:AdministrativeSafeguard {safeguard_id: row.safeguard_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    as.name = row.name,
    as.description = row.description,
    as.safeguard_type = row.safeguard_type,
    as.implementation_specifications = row.implementation_specifications,
    as.cfr_citation = row.cfr_citation,
    as.required_addressable = row.required_addressable;
"""

# 4.3 Load Physical Safeguards
physical_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ps:PhysicalSafeguard {safeguard_id: row.safeguard_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ps.name = row.name,
    ps.description = row.description,
    ps.safeguard_type = row.safeguard_type,
    ps.implementation_specifications = row.implementation_specifications,
    ps.cfr_citation = row.cfr_citation,
    ps.required_addressable = row.required_addressable;
"""

# 4.4 Load Technical Safeguards
technical_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ts:TechnicalSafeguard {safeguard_id: row.safeguard_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ts.name = row.name,
    ts.description = row.description,
    ts.safeguard_type = row.safeguard_type,
    ts.implementation_specifications = row.implementation_specifications,
    ts.cfr_citation = row.cfr_citation,
    ts.required_addressable = row.required_addressable;
"""

# 4.5 Load Security Measures
security_measures = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sm:SecurityMeasure {measure_id: row.measure_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sm.name = row.name,
    sm.description = row.description,
    sm.control_type = row.control_type,
    sm.technology_used = row.technology_used,
    sm.cfr_citation = row.cfr_citation;
"""

# 4.6 Load Risk Assessments
risk_assessments = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ra:RiskAssessment {assessment_id: row.assessment_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ra.name = row.name,
    ra.description = row.description,
    ra.frequency = row.frequency,
    ra.methodology = row.methodology,
    ra.cfr_citation = row.cfr_citation,
    ra.required = row.required;
"""

# 4.7 Load Security Incidents
security_incidents = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (si:SecurityIncident {incident_id: row.incident_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    si.incident_type = row.incident_type,
    si.description = row.description,
    si.severity = row.severity,
    si.response_required = row.response_required,
    si.cfr_citation = row.cfr_citation;
"""

# 4.8 Load Incident Response
Incident_Response ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:IncidentResponse {response_id: row.response_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ir.name = row.name,
    ir.description = row.description,
    ir.procedures = row.procedures,
    ir.timeline = row.timeline,
    ir.cfr_citation = row.cfr_citation;
"""

# 4.9 Load Security Vulnerabilities
security_vulnerabilities = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sv:SecurityVulnerability {vulnerability_id: row.vulnerability_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sv.name = row.name,
    sv.description = row.description,
    sv.vulnerability_type = row.vulnerability_type,
    sv.severity = row.severity,
    sv.cfr_citation = row.cfr_citation;
"""


# 4.10 Load Security Risks
security_risks = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sr:SecurityRisk {risk_id: row.risk_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sr.name = row.name,
    sr.description = row.description,
    sr.risk_level = row.risk_level,
    sr.mitigation_required = row.mitigation_required,
    sr.cfr_citation = row.cfr_citation;
"""

# 4.11 Load Contingency Planning
contingency_planning = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cp:ContingencyPlanning {plan_id: row.plan_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    cp.name = row.name,
    cp.description = row.description,
    cp.components = row.components,
    cp.testing_frequency = row.testing_frequency,
    cp.cfr_citation = row.cfr_citation;
"""

# 4.12 Load Workforce Security
workforce_security = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ws:WorkforceSecurity {security_id: row.security_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ws.name = row.name,
    ws.description = row.description,
    ws.components = row.components,
    ws.cfr_citation = row.cfr_citation;
"""

# SUBGRAPH 5: BREACH NOTIFICATION RULE (9 NODES)

# 5.1 Load Security Breaches
security_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sb:SecurityBreach {breach_id: row.breach_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sb.breach_type = row.breach_type,
    sb.description = row.description,
    sb.severity = row.severity,
    sb.affected_individuals_count = row.affected_individuals_count,
    sb.cfr_citation = row.cfr_citation;
"""

# 5.2 Load Breach Risk Assessments
breach_risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bra:BreachRiskAssessment {assessment_id: row.assessment_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    bra.factors_considered = row.factors_considered,
    bra.methodology = row.methodology,
    bra.determination = row.determination,
    bra.cfr_citation = row.cfr_citation;
"""

# 5.3 Load Breach Notification Process
breach_notification_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bnp:BreachNotificationProcess {process_id: row.process_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    bnp.name = row.name,
    bnp.description = row.description,
    bnp.timeline = row.timeline,
    bnp.notification_recipients = row.notification_recipients,
    bnp.cfr_citation = row.cfr_citation;
"""

# 5.4 Load Affected Individuals
affected_individuals = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ai:AffectedIndividual {individual_id: row.individual_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ai.notification_required = row.notification_required,
    ai.notification_method = row.notification_method,
    ai.notification_content = row.notification_content,
    ai.cfr_citation = row.cfr_citation;
"""

# 5.5 Load Notification Recipients
notification_receipients = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (nr:NotificationRecipient {recipient_id: row.recipient_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    nr.recipient_type = row.recipient_type,
    nr.notification_method = row.notification_method,
    nr.timeline = row.timeline,
    nr.cfr_citation = row.cfr_citation;
"""

# 5.6 Load Notification Content
notfication_content = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (nc:NotificationContent {content_id: row.content_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    nc.required_elements = row.required_elements,
    nc.description = row.description,
    nc.cfr_citation = row.cfr_citation;
"""

# 5.7 Load Breach Timelines
breach_timeline ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bt:BreachTimeline {timeline_id: row.timeline_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    bt.notification_deadline = row.notification_deadline,
    bt.discovery_date = row.discovery_date,
    bt.notification_date = row.notification_date,
    bt.cfr_citation = row.cfr_citation;
"""

# 5.8 Load Mitigation Services
mitigation_services ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ms:MitigationServices {service_id: row.service_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ms.service_type = row.service_type,
    ms.description = row.description,
    ms.duration = row.duration,
    ms.cost_bearer = row.cost_bearer,
    ms.cfr_citation = row.cfr_citation;
"""

# 5.9 Load Media Notifications
media_notifications = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mn:MediaNotification {notification_id: row.notification_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    mn.threshold = row.threshold,
    mn.media_types = row.media_types,
    mn.content_requirements = row.content_requirements,
    mn.cfr_citation = row.cfr_citation;
"""

# SUBGRAPH 6: COVERED ENTITIES & BUSINESS ASSOCIATES (9 NODES)

# 6.1 Load Covered Entities
Covered_Entities ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ce:CoveredEntity {entity_id: row.entity_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ce.entity_type = row.entity_type,
    ce.name = row.name,
    ce.description = row.description,
    ce.obligations = row.obligations,
    ce.cfr_citation = row.cfr_citation,
    ce.covered_if_criteria = row.covered_if_criteria;
"""

# 6.2 Load Business Associates
business_associates = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ba:BusinessAssociate {associate_id: row.associate_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ba.name = row.name,
    ba.description = row.description,
    ba.service_type = row.service_type,
    ba.obligations = row.obligations,
    ba.cfr_citation = row.cfr_citation,
    ba.must_implement = row.must_implement;
"""

# 6.3 Load Subcontractors
Subcontractors="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:Subcontractor {subcontractor_id: row.subcontractor_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sc.name = row.name,
    sc.description = row.description,
    sc.service_type = row.service_type,
    sc.obligations = row.obligations,
    sc.cfr_citation = row.cfr_citation;
"""

# 6.4 Load Business Associate Agreements
Business_Associate_Agreements ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (baa:BusinessAssociateAgreement {agreement_id: row.agreement_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    baa.required_provisions = row.required_provisions,
    baa.description = row.description,
    baa.cfr_citation = row.cfr_citation,
    baa.permitted_uses = row.permitted_uses,
    baa.prohibited_uses = row.prohibited_uses;
"""

# 6.5 Load Hybrid Entities
Hybrid_Entities ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (he:HybridEntity {entity_id: row.entity_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    he.name = row.name,
    he.description = row.description,
    he.healthcare_components = row.healthcare_components,
    he.non_covered_functions = row.non_covered_functions,
    he.cfr_citation = row.cfr_citation,
    he.requirement = row.requirement;
"""

# 6.6 Load OHCA
OHCA ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:OHCA {ohca_id: row.ohca_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    o.name = row.name,
    o.description = row.description,
    o.participating_entities = row.participating_entities,
    o.benefits = row.benefits,
    o.cfr_citation = row.cfr_citation,
    o.characteristics = row.characteristics;
"""

# 6.7 Load Healthcare Providers
Healthcare_Providers ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (hp:HealthcareProvider {provider_id: row.provider_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    hp.provider_type = row.provider_type,
    hp.name = row.name,
    hp.description = row.description,
    hp.covered_if = row.covered_if,
    hp.cfr_citation = row.cfr_citation;
"""

#6.8 Load Health Plans
Health_Plans ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (hpl:HealthPlan {plan_id: row.plan_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    hpl.plan_type = row.plan_type,
    hpl.name = row.name,
    hpl.description = row.description,
    hpl.covered_status = row.covered_status,
    hpl.cfr_citation = row.cfr_citation;
"""

# 6.9 Load Workforce Members
Workforce_Members ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (wm:WorkforceMember {member_id: row.member_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    wm.member_type = row.member_type,
    wm.description = row.description,
    wm.obligations = row.obligations,
    wm.training_required = row.training_required,
    wm.cfr_citation = row.cfr_citation;
"""


# SUBGRAPH 7: COMPLIANCE & ENFORCEMENT (10 NODES)


# 7.1 Load Compliance Programs
Compliance_Programs ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (comp:ComplianceProgram {program_id: row.program_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    comp.name = row.name,
    comp.description = row.description,
    comp.components = row.components,
    comp.monitoring_frequency = row.monitoring_frequency,
    comp.cfr_citation = row.cfr_citation;
"""

# 7.2 Load Compliance Audits
Compliance_Audits ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ca:ComplianceAudit {audit_id: row.audit_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ca.audit_type = row.audit_type,
    ca.description = row.description,
    ca.frequency = row.frequency,
    ca.scope = row.scope,
    ca.cfr_citation = row.cfr_citation;
"""
# 7.3 Load Compliance Violations
Compliance_Violations ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cv:ComplianceViolation {violation_id: row.violation_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    cv.violation_type = row.violation_type,
    cv.description = row.description,
    cv.severity = row.severity,
    cv.rule_violated = row.rule_violated,
    cv.cfr_citation = row.cfr_citation;
"""

#7.4 Load Violation Severities
Violation_Severities ="""
LOAD CSV WITH HEADERS FROM '$file_path_' AS row
MERGE (vs:ViolationSeverity {severity_id: row.severity_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    vs.severity_level = row.severity_level,
    vs.description = row.description,
    vs.penalty_range = row.penalty_range,
    vs.cfr_citation = row.cfr_citation;
"""

# 7.5 Load OCR Investigations
OCR_Investigations ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oi:OCRInvestigation {investigation_id: row.investigation_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    oi.description = row.description,
    oi.investigation_process = row.investigation_process,
    oi.authority = row.authority,
    oi.cfr_citation = row.cfr_citation;
"""

# 7.6 Load Enforcement Actions
Enforcement_Actions ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {action_id: row.action_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ea.action_type = row.action_type,
    ea.description = row.description,
    ea.authority = row.authority,
    ea.cfr_citation = row.cfr_citation;
"""

#7.7 Load Civil Penalties
Civil_Penalties ="""
LOAD CSV WITH HEADERS FROM '$file_path_cpen' AS row
MERGE (cpen:CivilPenalty {penalty_id: row.penalty_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    cpen.penalty_tier = row.penalty_tier,
    cpen.penalty_range = row.penalty_range,
    cpen.annual_maximum = row.annual_maximum,
    cpen.description = row.description,
    cpen.cfr_citation = row.cfr_citation;
"""

# 7.8 Load Criminal Penalties
Criminal_Penalties ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (crpen:CriminalPenalty {penalty_id: row.penalty_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    crpen.offense_type = row.offense_type,
    crpen.fine_amount = row.fine_amount,
    crpen.imprisonment_duration = row.imprisonment_duration,
    crpen.description = row.description,
    crpen.cfr_citation = row.cfr_citation;
"""


 #7.9 Load Corrective Action Plans
Corrective_Action_Plans="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (capl:CorrectiveActionPlan {plan_id: row.plan_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    capl.description = row.description,
    capl.required_actions = row.required_actions,
    capl.timeline = row.timeline,
    capl.monitoring = row.monitoring,
    capl.cfr_citation = row.cfr_citation;
"""
# 7.10 Load Regulators
Regulators="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:Regulator {regulator_id: row.regulator_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    reg.name = row.name,
    reg.authority = row.authority,
    reg.enforcement_powers = row.enforcement_powers,
    reg.investigation_process = row.investigation_process,
    reg.cfr_citation = row.cfr_citation;
"""



#Relationships
industry_standard_and_regulations_hipaa_standards_rel = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (s:Standard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_STANDARDS]->(s);
"""




hipaa_standard_subcategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cfr:CFRCitation {citation: row.cfr_citation, industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (CSF:NISTCSFSubcategory {subcategory_id: row.nist_subcategory_id, 
       IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MERGE (cfr)-[rel:ALIGNS_WITH_NIST_CSF_SUBCATEGORY {relationship_id: row.relationship_id}]->(CSF)
ON CREATE SET
    rel.hipaa_title = row.hipaa_title,
    rel.mapping_type = row.mapping_type,
    rel.confidence = row.confidence,
    rel.alignment_level = row.alignment_level,
    rel.mapping_rationale = row.mapping_rationale,
    rel.nist_function = row.nist_function,
    rel.nist_category = row.nist_category,
    rel.source_doc = row.source_doc,
    rel.source_section = row.source_section,
    rel.source_page = row.source_page,
    rel.created_date = row.created_date,
    rel.created_by = row.created_by;
"""



#IndustryStandardAndRegulation → CFRSection
industry_standard_and_regulation_cfr_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cfr:CFRSection {cfr_section_id: row.cfr_section_id})
MERGE (i)-[rel:INDUSTRY_STANDARD_AND_REGULATION_CONTAINS_CFR_SECTION {relationship_id: row.relationship_id}]->(cfr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

# CFRSection → RegulatoryStandard
cfr_section_regulatory_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cfr:CFRSection {cfr_section_id: row.cfr_section_id})
MATCH (rs:RegulatoryStandard {standard_id: row.standard_id})
MERGE (cfr)-[rel:CFR_CONTAINS_REGULATORY_STANDARD {relationship_id: row.relationship_id}]->(rs)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#RegulatoryStandard → ComplianceRequirement
regulatory_standard_compliance_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rs:RegulatoryStandard {standard_id: row.standard_id})
MATCH (cr:ComplianceRequirement {requirement_id: row.requirement_id})
MERGE (rs)-[rel:REGULATORY_STANDARD_HAS_COMPLIANCE_REQUIREMENT {relationship_id: row.relationship_id}]->(cr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceRequirement → ImplementationSpecification
compliance_requirement_implementation_specification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cr:ComplianceRequirement {requirement_id: row.requirement_id})
MATCH (is:ImplementationSpecification {spec_id: row.spec_id})
MERGE (cr)-[rel:COMPLIANCE_REQUIREMENT_SPECIFIED_BY_IMPLEMENTATION_SPECIFICATION {relationship_id: row.relationship_id}]->(is)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#RegulatoryStandard → ImplementationSpecification
regulatory_standard_implementation_spec ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rs:RegulatoryStandard {standard_id: row.standard_id})
MATCH (is:ImplementationSpecification {spec_id: row.spec_id})
MERGE (rs)-[rel:REGULATORY_STANDARD_SPECIFIED_BY_IMPLEMENTATION {relationship_id: row.relationship_id}]->(is)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ElectronicPHI → PHICategory
electronic_phi_phi_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MATCH (pc:PHICategory {category_id: row.category_id})
MERGE (ephi)-[rel:ELECTRONICPHI_CLASSIFIES_PHICATEGORY {relationship_id: row.relationship_id}]->(pc)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PHICategory → SensitiveDataElement
PHI_Categories_Sensitive_Data_Elements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pc:PHICategory {category_id: row.category_id})
MATCH (sde:SensitiveDataElement {element_id: row.element_id})
MERGE (pc)-[rel:PHICATEGORY_CONTAINS_ELEMENTS {relationship_id: row.relationship_id}]->(sde)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# ElectronicPHI → PHIForm
electronic_phi_phi_form = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MATCH (pf:PHIForm {form_id: row.form_id})
MERGE (ephi)-[rel:ELECTRONICPHI_CONTAINS_PHIFORM {relationship_id: row.relationship_id}]->(pf)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# ElectronicPHI → PHILocation
electronic_phi_phi_location = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MATCH (pl:PHILocation {location_id: row.location_id})
MERGE (ephi)-[rel:ELECTRONICPHI_CONTAINS_PHILOCATION {relationship_id: row.relationship_id}]->(pl)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ElectronicPHI → PHILifecycle
electronic_phi_phi_lifecycle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MATCH (plc:PHILifecycle {lifecycle_id: row.lifecycle_id})
MERGE (ephi)-[rel:ELECTRONICPHI_SUBJECT_TO_PHI_LIFECYCLE {relationship_id: row.relationship_id}]->(plc)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#DataUse → ElectronicPHI
data_use_electronic_phi = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (du:DataUse {use_id: row.use_id})
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MERGE (du)-[rel:DATAUSE_APPLIES_TO_ELECTRONICPHI {relationship_id: row.relationship_id}]->(ephi)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#DataDisclosure → ElectronicPHI
data_disclosure_electronic_phi = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dd:DataDisclosure {disclosure_id: row.disclosure_id})
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MERGE (dd)-[rel:DATA_DISCLOSURE_APPLIES_TO_ELECTRONIC_PHI {relationship_id: row.relationship_id}]->(ephi)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#MinimumNecessary → ElectronicPHI
minimum_necessary_electronic_phi = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (mn:MinimumNecessary {principle_id: row.principle_id})
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MERGE (ephi)-[rel:MINIMUM_NECESSARY_APPLIES_TO_ELECTRONIC_PHI {relationship_id: row.relationship_id}]->(mn)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#DeidentifiedHealthInfo → ElectronicPHI
deidentified_health_info_electronic_phi = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dhi:DeidentifiedHealthInfo {node_id: row.dhi_id})
MATCH (ephi:ElectronicPHI {node_id: row.ephi_id})
MERGE (dhi)-[rel:DEIDENTIFIED_HEALTH_INFO_APPLIES_TO_ELECTRONIC_PHI {relationship_id: row.relationship_id}]->(ephi)
ON CREATE SET
    rel.deidentification_method = row.deidentification_method,
    rel.created_date = row.created_date;
"""
#LimitedDataSet → DataUseAgreement
Limiteddataset_datauseagreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (lds:LimitedDataSet {node_id: row.lds_id})
MATCH (dua:DataUseAgreement {agreement_id: row.agreement_id})
MERGE (lds)-[rel:DATASET_REQUIRES_AGREEMENT {relationship_id: row.relationship_id}]->(dua)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PHILifecycle → ComplianceRequirement
phi_lifecycle_compliance_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (plc:PHILifecycle {lifecycle_id: row.lifecycle_id})
MATCH (cr:ComplianceRequirement {requirement_id: row.requirement_id})
MERGE (plc)-[rel:PHILIFECYCLE_REQUIRES_COMPLIANCE {relationship_id: row.relationship_id}]->(cr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#DataUseAgreement → DataUse
data_use_agreement_data_use = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dua:DataUseAgreement {agreement_id: row.agreement_id})
MATCH (du:DataUse {use_id: row.use_id})
MERGE (dua)-[rel:DATAUSEAGREEMENT_USES_DATA {relationship_id: row.relationship_id}]->(du)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#IndividualRight → DataSubject
individual_right_data_subject = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ir:IndividualRight {right_id: row.right_id})
MATCH (ds:DataSubject {subject_id: row.subject_id})
MERGE (ir)-[rel:EXERCISEDBY {relationship_id: row.relationship_id}]->(ds)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#UseAndDisclosure → Authorization
use_and_disclosure_authorization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ud:UseAndDisclosure {disclosure_id: row.disclosure_id})
MATCH (auth:Authorization {authorization_id: row.authorization_id})
MERGE (ud)-[rel:USEANDDISCLOSURE_REQUIRES_AUTHORIZATION {relationship_id: row.relationship_id}]->(auth)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#UseAndDisclosure → LawfulBasis
use_and_disclosure_lawful_basis = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ud:UseAndDisclosure {disclosure_id: row.disclosure_id})
MATCH (lb:LawfulBasis {basis_id: row.basis_id})
MERGE (ud)-[rel:USEANDDISCLOSURE_REQUIRES_LAWFUL_BASIS {relationship_id: row.relationship_id}]->(lb)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#DataSubject → PatientRequest
data_subject_patient_request = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ds:DataSubject {subject_id: row.subject_id})
MATCH (pr:PatientRequest {request_id: row.request_id})
MERGE (ds)-[rel:DATASUBJECT_REQUESTS_PATIENT_REQUEST {relationship_id: row.relationship_id}]->(pr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PatientRequest → ComplianceRequirement
patient_requests_compliance_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pr:PatientRequest {request_id: row.request_id})
MATCH (cr:ComplianceRequirement {requirement_id: row.requirement_id})
MERGE (pr)-[rel:PATIENTREQUEST_REQUIRES_COMPLIANCE_REQUIREMENT{relationship_id: row.relationship_id}]->(cr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PrivacyComplaint → PrivacyNotice
privacy_complaint_privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pcom:PrivacyComplaint {complaint_id: row.complaint_id})
MATCH (pn:PrivacyNotice {notice_id: row.notice_id})
MERGE (pcom)-[rel:PRIVACYCOMPLAINT_NEEDS_PRIVACYNOTICE {relationship_id: row.relationship_id}]->(pn)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PsychotherapyNotes → Authorization
psychotherapy_notes_authorization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ptn:PsychotherapyNotes {node_id: row.ptn_id})
MATCH (auth:Authorization {authorization_id: row.authorization_id})
MERGE (ptn)-[rel:PSYCHOTHERAPYNOTES_REQUIRES_AUTHORIZATION {relationship_id: row.relationship_id}]->(auth)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#MarketingAuthorization → UseAndDisclosure
marketing_authorization_use_and_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ma:MarketingAuthorization {authorization_id: row.marketing_auth_id})
MATCH (ud:UseAndDisclosure {disclosure_id: row.disclosure_id})
MERGE (ma)-[rel:MARKETINGAUTHORIZATION_REQUIRES_USE_AND_DISCLOSURE {relationship_id: row.relationship_id}]->(ud)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PrivacyNotice → UseAndDisclosure
privacy_notice_use_and_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pn:PrivacyNotice {notice_id: row.notice_id})
MATCH (ud:UseAndDisclosure {disclosure_id: row.disclosure_id})
MERGE (pn)-[rel:PRIVACYNOTICE_REQUIRES_USE_AND_DISCLOSUR {relationship_id: row.relationship_id}]->(ud)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#ndividualRight → RegulatoryStandard
individual_right_regulatory_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ir:IndividualRight {right_id: row.right_id})
MATCH (rs:RegulatoryStandard {standard_id: row.standard_id})
MERGE (ir)-[rel:INDIVIDUALRIGHT_REQUIRES_REGULATORY_STANDARD {relationship_id: row.relationship_id}]->(rs)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#SecurityStandard → AdministrativeSafeguard
security_standard_administrative_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ss:SecurityStandard {standard_id: row.standard_id})
MATCH (as:AdministrativeSafeguard {safeguard_id: row.safeguard_id})
MERGE (ss)-[rel:SECURITYSTANDARD_REQUIRES_ADMINISTRATIVE_SAFEGUARD {relationship_id: row.relationship_id}]->(as)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityStandard → PhysicalSafeguard
security_standard_physical_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ss:SecurityStandard {standard_id: row.standard_id})
MATCH (ps:PhysicalSafeguard {safeguard_id: row.safeguard_id})
MERGE (ss)-[rel:SECURITYSTANDARD_REQUIRES_PHYSICAL_SAFEGUARDS {relationship_id: row.relationship_id}]->(ps)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityStandard → TechnicalSafeguard
security_standard_technical_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ss:SecurityStandard {standard_id: row.standard_id})
MATCH (ts:TechnicalSafeguard {safeguard_id: row.safeguard_id})
MERGE (ss)-[rel:SECURITYSTANDARD_REQUIRES_TECHNICAL_SAFEGUARDS {relationship_id: row.relationship_id}]->(ts)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#AdministrativeSafeguard → SecurityMeasure
administrative_safeguards_security_measures = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (as:AdministrativeSafeguard {safeguard_id: row.safeguard_id})
MATCH (sm:SecurityMeasure {measure_id: row.measure_id})
MERGE (as)-[rel:IMPLEMENTEDVIA {relationship_id: row.relationship_id}]->(sm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#PhysicalSafeguard → SecurityMeasure
physical_safeguards_security_measures = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ps:PhysicalSafeguard {safeguard_id: row.safeguard_id})
MATCH (sm:SecurityMeasure {measure_id: row.measure_id})
MERGE (ps)-[rel:PHYSICAL_SAFEGUARD_MEETS_SECURITY_MEASURE {relationship_id: row.relationship_id}]->(sm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#TechnicalSafeguard → SecurityMeasure
technical_safeguards_security_measures = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ts:TechnicalSafeguard {safeguard_id: row.safeguard_id})
MATCH (sm:SecurityMeasure {measure_id: row.measure_id})
MERGE (ts)-[rel:TECHNICAL_SAFEGUARD_MEETS_SECURITY_MEASURE {relationship_id: row.relationship_id}]->(sm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#RiskAssessment → SecurityVulnerability
risk_assessment_security_vulnerability = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ra:RiskAssessment {assessment_id: row.assessment_id})
MATCH (sv:SecurityVulnerability {vulnerability_id: row.vulnerability_id})
MERGE (ra)-[rel:IRISKASSESSMENT_IDENTIFIES_SECURITY_VULNERABILITY {relationship_id: row.relationship_id}]->(sv)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityVulnerability → SecurityRisk
security_vulnerability_security_risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sv:SecurityVulnerability {vulnerability_id: row.vulnerability_id})
MATCH (sr:SecurityRisk {risk_id: row.risk_id})
MERGE (sv)-[rel:SECURITYVULNERABILITY_IDENTIFIES_SECURITY {relationship_id: row.relationship_id}]->(sr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#SecurityRisk → SecurityMeasure
security_risk_security_measure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SecurityRisk {risk_id: row.risk_id})
MATCH (sm:SecurityMeasure {measure_id: row.measure_id})
MERGE (sr)-[rel:SECURITYRISK_REQUIRES_SECURITY_MITIGATION {relationship_id: row.relationship_id}]->(sm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityIncident → IncidentResponse
security_incident_incident_response = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (si:SecurityIncident {incident_id: row.incident_id})
MATCH (ir:IncidentResponse {response_id: row.response_id})
MERGE (si)-[rel:SECURITYINCIDENT_TRIGGERS_INCIDENT_RESPONSE {relationship_id: row.relationship_id}]->(ir)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ContingencyPlanning → SecurityMeasure
Contingency_Planning_Security_Measure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cp:ContingencyPlanning {plan_id: row.plan_id})
MATCH (sm:SecurityMeasure {measure_id: row.measure_id})
MERGE (cp)-[rel:CONTINGENCYPLANNING_INVOLVES_SECURITY_MEASURES {relationship_id: row.relationship_id}]->(sm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#WorkforceSecurity → ComplianceRequirement
workforce_security_compliance_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ws:WorkforceSecurity {security_id: row.security_id})
MATCH (cr:ComplianceRequirement {requirement_id: row.requirement_id})
MERGE (ws)-[rel:WORKFORCESECURITY_REQUIRES_COMPLIANCE_REQUIREMENT {relationship_id: row.relationship_id}]->(cr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityBreach → BreachRiskAssessment
security_breach_breach_risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (bra:BreachRiskAssessment {assessment_id: row.assessment_id})
MERGE (sb)-[rel:SECURITYBREACH_IDENTIFIES_RISK_ASSESSMENT {relationship_id: row.relationship_id}]->(bra)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityBreach → BreachNotificationProcess
security_breach_breach_notification_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (bnp:BreachNotificationProcess {process_id: row.process_id})
MERGE (sb)-[rel:SECURITYBREACH_TRIGGERS_BREACH_NOTIFICATION_PROCESS {relationship_id: row.relationship_id}]->(bnp)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#BreachNotificationProcess → AffectedIndividual
breach_notification_process_affected_individual = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (bnp:BreachNotificationProcess {process_id: row.process_id})
MATCH (ai:AffectedIndividual {individual_id: row.individual_id})
MERGE (bnp)-[rel:BREACHNOTIFICATIONPROCESS_REQUIRES_AFFECTED_INDIVIDUALS {relationship_id: row.relationship_id}]->(ai)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#BreachNotificationProcess → NotificationRecipient
breach_notification_process_notification_recipient = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (bnp:BreachNotificationProcess {process_id: row.process_id})
MATCH (nr:NotificationRecipient {recipient_id: row.recipient_id})
MERGE (bnp)-[rel:BREACHNOTIFICATIONPROCESS_REQUIRES_NOTIFICATION_RECIPIENTS {relationship_id: row.relationship_id}]->(nr)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#NotificationRecipient → NotificationContent
notification_recipient_notification_content = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (nr:NotificationRecipient {recipient_id: row.recipient_id})
MATCH (nc:NotificationContent {content_id: row.content_id})
MERGE (nr)-[rel:NOTIFICATIONRECIPIENT_SENDS_NOTIFICATION_CONTENT {relationship_id: row.relationship_id}]->(nc)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# SecurityBreach → BreachTimeline
security_breach_breach_timeline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (bt:BreachTimeline {timeline_id: row.timeline_id})
MERGE (sb)-[rel:SECURITYBREACH_HAS_TIMELINE {relationship_id: row.relationship_id}]->(bt)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#SecurityBreach → MitigationServices
security_breach_mitigation_services = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (ms:MitigationServices {service_id: row.service_id})
MERGE (sb)-[rel:SECURITYBREACH_REQUIRES_MITIGATION_SERVICES {relationship_id: row.relationship_id}]->(ms)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# SecurityBreach → MediaNotification
security_breach_media_notification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (mn:MediaNotification {notification_id: row.notification_id})
MERGE (sb)-[rel:SECURITYBREACH_REQUIRES_MEDIA_NOTIFICATION_SERVICE {relationship_id: row.relationship_id}]->(mn)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#BreachNotificationProcess → BreachTimeline
breach_notification_process_breach_timeline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (bnp:BreachNotificationProcess {process_id: row.process_id})
MATCH (bt:BreachTimeline {timeline_id: row.timeline_id})
MERGE (bnp)-[rel:BREACHNOTIFICATIONPROCESS_HAS_TIMELINE {relationship_id: row.relationship_id}]->(bt)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#IndustryStandardAndRegulation → CoveredEntity
industry_standard_and_regulation_covered_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MERGE (i)-[rel:INDUSTRY_STANDARD_AND_REGULATES_COVERED_ENTITY {relationship_id: row.relationship_id}]->(ce)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → BusinessAssociate
covered_entity_business_associate = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (ba:BusinessAssociate {associate_id: row.associate_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_BUSINESS_ASSOCIATE {relationship_id: row.relationship_id}]->(ba)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → BusinessAssociateAgreement
covered_entity_business_associate_agreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (baa:BusinessAssociateAgreement {agreement_id: row.agreement_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_BUSINESS_ASSOCIATE_AGREEMENT_WITH_BUSINESS_ASSOCIATE_AGREEMENT{relationship_id: row.relationship_id}]->(baa)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#BusinessAssociate → BusinessAssociateAgreement
business_associate_business_associate_agreement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ba:BusinessAssociate {associate_id: row.associate_id})
MATCH (baa:BusinessAssociateAgreement {agreement_id: row.agreement_id})
MERGE (ba)-[rel:BUSINESS_ASSOCIATE_HAS_BUSINESS_ASSOCIATE_AGREEMENT_WITH_BUSINESS_AGREEMENT {relationship_id: row.relationship_id}]->(baa)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#BusinessAssociate → Subcontractor
business_associate_subcontractor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ba:BusinessAssociate {associate_id: row.associate_id})
MATCH (sc:Subcontractor {subcontractor_id: row.subcontractor_id})
MERGE (ba)-[rel:BUSINESS_ASSOCIATE_HAS_SUBCONTRACTOR{relationship_id: row.relationship_id}]->(sc)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → HybridEntity
covered_entity_hybrid_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (he:HybridEntity {entity_id: row.hybrid_entity_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HYBRID_ENTITY {relationship_id: row.relationship_id}]->(he)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → OHCA
covered_entity_ohca = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (o:OHCA {ohca_id: row.ohca_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_OHCA {relationship_id: row.relationship_id}]->(o)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#CoveredEntity → HealthcareProvider
covered_entity_healthcare_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (hp:HealthcareProvider {provider_id: row.provider_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HEALTHCARE_PROVIDER_WITH_HEALTHCARE {relationship_id: row.relationship_id}]->(hp)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# CoveredEntity → HealthPlan
covered_entity_health_plan = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (hpl:HealthPlan {plan_id: row.plan_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HEALTH_PLAN_WITH_HEALTH {relationship_id: row.relationship_id}]->(hpl)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → WorkforceMember
covered_entity_workforce_member = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (wm:WorkforceMember {member_id: row.member_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_WORKFORCE_MEMBER_WITH_WORKFORCE_MEMBER {relationship_id: row.relationship_id}]->(wm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → ComplianceProgram
covered_entity_compliance_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (comp:ComplianceProgram {program_id: row.program_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_COMPLIANCE_PROGRAM_WITH_COMPLIANCE_ {relationship_id: row.relationship_id}]->(comp)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceProgram → ComplianceAudit
compliance_program_compliance_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (comp:ComplianceProgram {program_id: row.program_id})
MATCH (ca:ComplianceAudit {audit_id: row.audit_id})
MERGE (comp)-[rel:COMPLIANCE_PROGRAM_HAS_COMPLIANCE_AUDIT_WITH_COMPLIAN {relationship_id: row.relationship_id}]->(ca)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceAudit → ComplianceViolation
compliance_audit_compliance_violation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ca:ComplianceAudit {audit_id: row.audit_id})
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MERGE (ca)-[rel:COMPLIANCE_AUDIT_HAS_COMPLIANCE_VIOLATION_WITH_VIOLATION {relationship_id: row.relationship_id}]->(cv)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → ViolationSeverity
compliance_violation_violation_severity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MATCH (vs:ViolationSeverity {severity_id: row.severity_id})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_HAS_VIOLATION_SEVERITY_WITH_SEVERITY {relationship_id: row.relationship_id}]->(vs)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → OCRInvestigation
compliance_violation_ocr_investigation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MATCH (oi:OCRInvestigation {investigation_id: row.investigation_id})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_HAS_OCR_INVESTIGATION_WITH_INVESTIGANTION {relationship_id: row.relationship_id}]->(oi)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#OCRInvestigation → EnforcementAction
ocr_investigation_enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (oi:OCRInvestigation {investigation_id: row.investigation_id})
MATCH (ea:EnforcementAction {action_id: row.action_id})
MERGE (oi)-[rel:OCR_INVESTIGATION_HAS_ENFORCEMENT_ACTION_WITH_ACTION {relationship_id: row.relationship_id}]->(ea)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CivilPenalty
enforcement_action_civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (cpen:CivilPenalty {penalty_id: row.penalty_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CIVIL_PENALTY_WITH_PENALTY {relationship_id: row.relationship_id}]->(cpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CriminalPenalty
enforcement_action_criminal_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (crpen:CriminalPenalty {penalty_id: row.penalty_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CRIMINAL_PENALTY_WITH_PENALTY {relationship_id: row.relationship_id}]->(crpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CorrectiveActionPlan
enforcement_action_corrective_action_plan = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (capl:CorrectiveActionPlan {plan_id: row.plan_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CORRECTIVE_ACTION_PLAN_WITH_PLAN {relationship_id: row.relationship_id}]->(capl)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#Regulator → EnforcementAction
regulator_enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulator {regulator_id: row.regulator_id})
MATCH (ea:EnforcementAction {action_id: row.action_id})
MERGE (reg)-[rel:REGULATOR_HAS_ENFORCEMENT_ACTION_WITH_ACTION {relationship_id: row.relationship_id}]->(ea)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ViolationSeverity → CivilPenalty
violation_severity_civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (vs:ViolationSeverity {severity_id: row.severity_id})
MATCH (cpen:CivilPenalty {penalty_id: row.penalty_id})
MERGE (vs)-[rel:DETERMINES {relationship_id: row.relationship_id}]->(cpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → RegulatoryStandard
compliance_violation_regulatory_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MATCH (rs:RegulatoryStandard {standard_id: row.standard_id})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_REQUIRES_REGULATORY_STANDARD {relationship_id: row.relationship_id}]->(rs)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""



import os
import time
import logging
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading graph structure...")

client.query(industry_standard_and_regulation)
time.sleep(2)

client.query(cfr_sections.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cfr_sections.csv'))
time.sleep(2)

client.query(regulatory_standards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulatory_standards.csv"))
time.sleep(2)

client.query(Compliance_Requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance_requirements.csv"))
time.sleep(2)

client.query(Implementation_Specifications.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/implementation_specs.csv"))
time.sleep(2)

client.query(Electronic_PHI.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/electronic_phi.csv"))
time.sleep(2)

client.query(PHI_Categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_categories.csv"))
time.sleep(2)

client.query(PHI_Forms.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_forms.csv"))
time.sleep(2)

client.query(PHI_Locations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_locations.csv"))
time.sleep(2)

client.query(PHI_Lifecycle.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_lifecycle.csv"))
time.sleep(2)

client.query(sensitive_data_elements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sensitive_data_elements.csv"))
time.sleep(2)

client.query(data_uses.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_uses.csv"))
time.sleep(2)

client.query(data_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_disclosures.csv"))
time.sleep(2)

client.query(minimum_necessary.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/minimum_necessary.csv"))
time.sleep(2)

client.query(de_indentified_health_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/deidentified_health_info.csv"))
time.sleep(2)

client.query(limited_data_set.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/limited_data_set.csv"))
time.sleep(2)

client.query(data_use_agreement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_use_agreement.csv"))
time.sleep(2)


client.query(individual_rights.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/individual_rights.csv"))
time.sleep(2)

client.query(data_subjects.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_subjects.csv"))
time.sleep(2)

client.query(use_and_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/use_and_disclosure.csv"))
time.sleep(2)

client.query(authorizations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/authorizations.csv"))
time.sleep(2)

client.query(lawful_basis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/lawful_basis.csv"))
time.sleep(2)

client.query(patient_requests.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/patient_requests.csv"))
time.sleep(2)

client.query(privacy_complaints.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/privacy_complaints.csv"))
time.sleep(2)

client.query(privacy_notices.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/privacy_notices.csv"))
time.sleep(2)

client.query(psychotherapy_notes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/psychotherapy_notes.csv"))
time.sleep(2)

client.query(marketing_authorization.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/marketing_authorizations.csv"))
time.sleep(2)

client.query(security_standards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_standards.csv"))
time.sleep(2)

client.query(administrative_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/administrative_safeguards.csv"))
time.sleep(2)

client.query(physical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/physical_safeguards.csv"))
time.sleep(2)

client.query(technical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/technical_safeguards.csv"))
time.sleep(2)

client.query(security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_measures.csv"))
time.sleep(2)

client.query(risk_assessments.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/risk_assessment.csv"))
time.sleep(2)

client.query(security_incidents.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_incidents.csv"))
time.sleep(2)

client.query(Incident_Response.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/incident_response.csv"))
time.sleep(2)

client.query(security_vulnerabilities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_vulnerabilities.csv"))
time.sleep(2)


client.query(security_risks.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security-risks.csv"))
time.sleep(2)

client.query(contingency_planning.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/contingency-planning.csv"))
time.sleep(2)

client.query(workforce_security.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/workforce-security.csv"))
time.sleep(2)


client.query(security_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security-breach.csv"))
time.sleep(2)

client.query(breach_risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-risk-assess.csv"))
time.sleep(2)


client.query(breach_notification_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-notif-process.csv"))
time.sleep(2)

client.query(affected_individuals.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/affected-individuals.csv"))
time.sleep(2)

client.query(notification_receipients.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/notif-recipients.csv"))
time.sleep(2)

client.query(notfication_content.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/notif-content.csv"))
time.sleep(2)

client.query(breach_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-timeline.csv"))
time.sleep(2)

client.query(mitigation_services.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/mitigation-services.csv"))
time.sleep(2)

client.query(media_notifications.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/media-notifications.csv"))
time.sleep(2)

client.query(Covered_Entities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/covered-entities.csv"))
time.sleep(2)

client.query(business_associates.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/business-associates.csv"))
time.sleep(2)

client.query(Subcontractors.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/subcontractors.csv"))
time.sleep(2)

client.query(Business_Associate_Agreements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/business-associates.csv"))
time.sleep(2)

client.query(Hybrid_Entities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hybrid-entities.csv"))
time.sleep(2)

client.query(OHCA.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ohca.csv"))
time.sleep(2)

client.query(Healthcare_Providers.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/healthcare-providers.csv"))
time.sleep(2)

client.query(Health_Plans.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/health-plans.csv"))
time.sleep(2)

client.query(Workforce_Members.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/workforce-members.csv"))
time.sleep(2)

client.query(Compliance_Programs.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-programs.csv"))
time.sleep(2)

client.query(Compliance_Audits.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-audits.csv"))
time.sleep(2)

client.query(Compliance_Violations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-violations.csv"))
time.sleep(2)

client.query(Violation_Severities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/violation-severities.csv"))
time.sleep(2)

client.query(OCR_Investigations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ocr-investigations.csv"))
time.sleep(2)

client.query(Enforcement_Actions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/enforcement-actions.csv"))
time.sleep(2)

client.query(Civil_Penalties.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/civil-penalties.csv"))
time.sleep(2)

client.query(Criminal_Penalties.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/criminal-penalties.csv"))
time.sleep(2)

client.query(Corrective_Action_Plans.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/corrective-action-plans.csv"))
time.sleep(2)

client.query(Regulators.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulators.csv"))
time.sleep(2)

#Relationships

client.query(industry_standard_and_regulations_hipaa_standards_rel)
time.sleep(2)

client.query(hipaa_standard_mapping_rel)
time.sleep(2)

client.query(mapping_subcategory_rel)
time.sleep(2)

client.query(industry_standard_and_regulation_cfr_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/isr-cfr-section.csv"))
time.sleep(2)


client.query(cfr_section_regulatory_standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cfr-reg-standard.csv"))
time.sleep(2)

client.query(regulatory_standard_compliance_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/reg-std-comp-req.csv"))
time.sleep(2)

client.query(compliance_requirement_implementation_specification.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/comp-req-impl-spec.csv"))
time.sleep(2)

client.query(regulatory_standard_implementation_spec.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/reg-std-impl-spec.csv"))
time.sleep(2)

client.query(electronic_phi_phi_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ephi-phi-category.csv"))
time.sleep(2)

client.query(PHI_Categories_Sensitive_Data_Elements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi-cat-sens-elem.csv"))
time.sleep(2)

client.query(electronic_phi_phi_form.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ephi-phi-form.csv"))
time.sleep(2)

client.query(electronic_phi_phi_location.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ephi-phi-location.csv"))
time.sleep(2)

client.query(electronic_phi_phi_lifecycle.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ephi-phi-lifecycle.csv"))
time.sleep(2)

client.query(data_use_electronic_phi.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/datause-ephi.csv"))
time.sleep(2)

client.query(data_disclosure_electronic_phi.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/datadisclosure-ephi.csv"))
time.sleep(2)

client.query(minimum_necessary_electronic_phi.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/minnecessary-ephi.csv"))
time.sleep(2)

client.query(deidentified_health_info_electronic_phi.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/deidentified-ephi.csv"))
time.sleep(2)

client.query(Limiteddataset_datauseagreement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/lds-dua.csv"))
time.sleep(2)

client.query(phi_lifecycle_compliance_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/philifecycle-compliance.csv"))
time.sleep(2)

client.query(data_use_agreement_data_use.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/dua-datause.csv"))
time.sleep(2)

client.query(individual_right_data_subject.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ir-regstd.csv"))
time.sleep(2)

client.query(use_and_disclosure_authorization.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ud-authorization.csv"))
time.sleep(2)

client.query(use_and_disclosure_lawful_basis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ud-lawfulbasis.csv"))
time.sleep(2)

client.query(data_subject_patient_request.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ds-patientrequest.csv"))
time.sleep(2)

client.query(patient_requests_compliance_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/pr-compliance.csv"))
time.sleep(2)

client.query(privacy_complaint_privacy_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/pc-privacynotice.csv"))
time.sleep(2)

client.query(privacy_notice_use_and_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/pn-ud.csv"))
time.sleep(2)

client.query(individual_right_regulatory_standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ir-regstd.csv"))
time.sleep(2)

client.query(security_standard_administrative_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ss-admin-safeguard.csv"))
time.sleep(2)

client.query(security_standard_physical_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ss-physical-safeguard.csv"))
time.sleep(2)

client.query(security_standard_technical_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ss-technical-safeguard.csv"))
time.sleep(2)

client.query(administrative_safeguards_security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/admin-safeguard-secmeasure.csv"))
time.sleep(2)

client.query(physical_safeguards_security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phys-safeguard-secmeasure.csv"))
time.sleep(2)

client.query(technical_safeguards_security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/tech-safeguard-secmeasure.csv"))
time.sleep(2)

client.query(risk_assessment_security_vulnerability.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ra-secvuln.csv"))
time.sleep(2)

client.query(security_vulnerability_security_risk.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sv-securityrisk.csv"))
time.sleep(2)

client.query(security_risk_security_measure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sr-secmeasure.csv"))
time.sleep(2)

client.query(security_incident_incident_response.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/si-incidentresponse.csv"))
time.sleep(2)

client.query(Contingency_Planning_Security_Measure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cp-secmeasure.csv"))
time.sleep(2)

client.query(workforce_security_compliance_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ws-compliance.csv"))
time.sleep(2)

client.query(security_breach_breach_risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-breachrisk.csv"))
time.sleep(2)

client.query(security_breach_breach_notification_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-media-notif.csv"))
time.sleep(2)

client.query(breach_notification_process_affected_individual.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/bnp-affected.csv"))
time.sleep(2)

client.query(breach_notification_process_notification_recipient.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/bnp-recipients.csv"))
time.sleep(2)

client.query(notification_recipient_notification_content.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/nr-notifcontent.csv"))
time.sleep(2)

client.query(security_breach_breach_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-timeline.csv"))
time.sleep(2)

client.query(security_breach_mitigation_services.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-mitigation.csv"))
time.sleep(2)

client.query(security_breach_media_notification.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-media-notif.csv"))
time.sleep(2)

client.query(breach_notification_process_breach_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-notif-process.csv"))
time.sleep(2)

client.query(covered_entity_hybrid_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-hybrid.csv"))
time.sleep(2)

client.query(covered_entity_ohca.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-ohca.csv"))
time.sleep(2)

client.query(covered_entity_healthcare_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-provider.csv"))
time.sleep(2)

client.query(covered_entity_health_plan.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-healthplan.csv"))
time.sleep(2)

client.query(covered_entity_workforce_member.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-workforce.csv"))
time.sleep(2)

client.query(covered_entity_compliance_program.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-compliance.csv"))
time.sleep(2)

client.query(compliance_program_compliance_audit.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cp-audit.csv"))
time.sleep(2)

client.query(compliance_audit_compliance_violation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ca-violation.csv"))
time.sleep(2)

client.query(compliance_violation_violation_severity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cv-severity.csv"))
time.sleep(2)

client.query(compliance_violation_ocr_investigation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cv-investigation.csv"))
time.sleep(2)

client.query(ocr_investigation_enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/oi-enforcement.csv"))
time.sleep(2)

client.query(enforcement_action_civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-civil-penalty.csv"))
time.sleep(2)

client.query(enforcement_action_criminal_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-criminal-penalty.csv"))
time.sleep(2)

client.query(enforcement_action_corrective_action_plan.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-corrective-action.csv"))
time.sleep(2)

client.query(regulator_enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulator-enforcement.csv"))
time.sleep(2)

client.query(violation_severity_civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/vs-civil-penalty.csv"))
time.sleep(2)

client.query(compliance_violation_regulatory_standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cv-regulatory-std.csv"))
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
with open('hipaa.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to hipaa.json")


client.close()
