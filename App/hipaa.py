

#industry_standard_and_regulation
industry_standard_and_regulation = """
MERGE (i:IndustryStandardAndRegulation{industry_standard_regulation_id:'HIPAA 1996'})
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
cfr_sections = """
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
# cfr citation 
cfr_citation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cfrc:CFRCitation {citation: row.citation, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    cfrc.hipaa_title = row.hipaa_title,
    cfrc.full_citation = row.full_citation,
    cfrc.industry_standard_regulation_id = row.industry_standard_regulation_id;
"""

# 1.2 Load Regulatory Standards
regulatory_standards = """
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
Compliance_Requirements = """
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
MERGE (sbc:Subcontractor {subcontractor_id: row.subcontractor_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sbc.name = row.name,
    sbc.description = row.description,
    sbc.service_type = row.service_type,
    sbc.obligations = row.obligations,
    sbc.cfr_citation = row.cfr_citation;
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
LOAD CSV WITH HEADERS FROM '$file_path' AS row
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
LOAD CSV WITH HEADERS FROM '$file_path' AS row
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
# Designated officials
designated_officials = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (do:DesignatedOfficial {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    do.name = row.name,
    do.description = row.description,
    do.source_citation = row.source_citation_id;
"""
# Preemption conditions
preemption_conditions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pc:PreemptionCondition {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    pc.name = row.name,
    pc.description = row.description,
    pc.source_citation = row.source_citation_id;
"""
# Plan sponsors
plan_sponsors = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (psp:PlanSponsor {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    psp.name = row.name,
    psp.description = row.description,
    psp.source_citation = row.source_citation_id;
"""
# External receipients
external_recipients = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rec:ExternalRecipient {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    rec.name = row.name,
    rec.description = row.description,
    rec.source_citation = row.source_citation_id;
"""

# Standard 
standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (std:Standard {node_id: row.id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET 
    std.name = row.title,
    std.type = row.safeguard_type,
    std.standard_type = row.standard_type,
    std.text = row.text,
    std.req_type = row.req_type,
    std.parent_id = row.parent_id,
    std.section = row.section,
    std.source_doc = row.source_doc,
    std.source_section = row.source_section;
"""


#Relationships
industry_standard_and_regulations_hipaa_standards_rel = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_REGULATORY_STANDARD]->(rs);
"""

# CFRCitation → NIST_CSF_Subcategory
hipaa_nist_mapping = """
MATCH (cfrc:CFRCitation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sc:Subcategory {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MERGE (cfrc)-[:CFR_CITATIONS_MAPPED_WITH_NIST_CSF_SUBCATEGORY]->(sc);
"""
 
# IndustryStandardAndRegulation → CFRSection
industry_standard_and_regulation_cfr_section = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cfr:CFRSection {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:INDUSTRY_STANDARD_AND_REGULATION_CONTAINS_CFR_SECTION]->(cfr);
"""

# CFRSection → RegulatoryStandard
CFR_citation_regulatory_standard = """
MATCH (cfr:CFRSection {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (cfr)-[:CFR_CONTAINS_REGULATORY_STANDARD]->(rs);
"""

# RegulatoryStandard → ComplianceRequirement
regulatory_standard_compliance_requirement = """
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cr:ComplianceRequirement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (rs)-[:REGULATORY_STANDARD_HAS_COMPLIANCE_REQUIREMENT]->(cr);
"""

#ComplianceRequirement → ImplementationSpecification
Compliance_Requirements_Implementation_Specification = """
MATCH (cr:ComplianceRequirement {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (is:ImplementationSpecification {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (cr)-[:COMPLIANCE_REQUIREMENT_SPECIFIED_BY_IMPLEMENTATION_SPECIFICATION]->(is);
"""

# RegulatoryStandard → ImplementationSpecification
regulatory_standard_implementation_specification = """
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (is:ImplementationSpecification {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (rs)-[:REGULATORY_STANDARD_SPECIFIED_BY_IMPLEMENTATION]->(is);
"""

# ElectronicPHI → PHICategory
electronic_phi_phi_category = """
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pc:PHICategory {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ephi)-[:ELECTRONICPHI_CLASSIFIES_PHICATEGORY]->(pc);
"""

# PHICategory → SensitiveDataElement
phi_category_sensitive_data_element = """
MATCH (pc:PHICategory {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sde:SensitiveDataElement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pc)-[:PHICATEGORY_CONTAINS_ELEMENTS]->(sde);
"""

# ElectronicPHI → PHIForm
electronic_phi_phi_form = """
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pf:PHIForm {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ephi)-[:ELECTRONICPHI_CONTAINS_PHIFORM]->(pf);
"""

# ElectronicPHI → PHILocation
electronic_phi_phi_location = """
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pl:PHILocation {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ephi)-[:ELECTRONICPHI_CONTAINS_PHILOCATION]->(pl);
"""

# ElectronicPHI → PHILifecycle
electronic_phi_phi_lifecycle = """
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (plc:PHILifecycle {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ephi)-[:ELECTRONICPHI_SUBJECT_TO_PHI_LIFECYCLE]->(plc);
"""

# DataUse → ElectronicPHI
data_use_electronic_phi = """
MATCH (du:DataUse {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (du)-[:DATAUSE_APPLIES_TO_ELECTRONICPHI]->(ephi);
"""

# DataDisclosure → ElectronicPHI
data_disclosure_electronic_phi = """
MATCH (dd:DataDisclosure {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (dd)-[:DATA_DISCLOSURE_APPLIES_TO_ELECTRONIC_PHI]->(ephi);
"""

# MinimumNecessary → ElectronicPHI
minimum_necessary_electronic_phi = """
MATCH (mn:MinimumNecessary {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ephi)-[:MINIMUM_NECESSARY_APPLIES_TO_ELECTRONIC_PHI]->(mn);
"""

# DeidentifiedHealthInfo → ElectronicPHI
deidentified_health_info_electronic_phi = """
MATCH (dhi:DeidentifiedHealthInfo {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ephi:ElectronicPHI {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (dhi)-[:DEIDENTIFIED_HEALTH_INFO_APPLIES_TO_ELECTRONIC_PHI]->(ephi);
"""

# LimitedDataSet → DataUseAgreement
limited_data_set_data_use_agreement = """
MATCH (lds:LimitedDataSet {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (dua:DataUseAgreement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (lds)-[:DATASET_REQUIRES_AGREEMENT]->(dua);
"""
#PHILifecycle → ComplianceRequirement
phi_lifecycle_compliance_requirement = """
MATCH (plc:PHILifecycle {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cr:ComplianceRequirement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (plc)-[:PHI_LIFECYCLE_REQUIRES_COMPLIANCE_REQUIREMENT]->(cr);
"""
# DataUseAgreement → DataUse #
data_use_agreement_data_use = """
MATCH (dua:DataUseAgreement {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (du:DataUse {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (dua)-[:DATA_USE_AGREEMENT_USES_DATA]->(du);
"""
## IndividualRight → DataSubject #
individual_right_data_subject = """
MATCH (ir:IndividualRight {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ds:DataSubject {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ir)-[:INDIVIDUAL_RIGHT_REQUIRES_DATASUBJECT]->(ds);
"""
# UseAndDisclosure → Authorization #
use_and_disclosure_authorization = """
MATCH (ud:UseAndDisclosure {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (auth:Authorization {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ud)-[:USE_AND_DISCLOSURE_REQUIRES_AUTHORIZATION]->(auth);
"""
# DataSubject → PatientRequest #
data_subject_patient_request = """
MATCH (ds:DataSubject {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pr:PatientRequest {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ds)-[:DATASUBJECT_REQUESTS_PATIENT_REQUEST]->(pr);
"""
# PatientRequest → ComplianceRequirement #
patient_request_compliance_requirement = """
MATCH (pr:PatientRequest {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cr:ComplianceRequirement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pr)-[:PATIENT_REQUEST_REQUIRES_COMPLIANCE_REQUIREMENT]->(cr);
"""
# PrivacyComplaint → PrivacyNotice #
privacy_complaint_privacy_notice = """
MATCH (pcom:PrivacyComplaint {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pn:PrivacyNotice {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pcom)-[:PRIVACY_COMPLAINT_NEEDS_PRIVACY_NOTICE]->(pn);
"""
#PsychotherapyNotes → Authorization #
psychotherapy_notes_authorization = """
MATCH (pn:PsychotherapyNotes {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (auth:Authorization {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pn)-[rel:PSYCHO_THERAPY_NOTES_REQUIRES_AUTHORIZATION]->(auth);
"""
#MarketingAuthorization → UseAndDisclosure #
marketing_authorization_use_and_disclosure = """
MATCH (ma:MarketingAuthorization {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ud:UseAndDisclosure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ma)-[rel:MARKETING_AUTHORIZATION_REQUIRES_USE_AND_DISCLOSURE]->(ud);
"""
#PrivacyNotice → UseAndDisclosure #
privacy_notice_use_and_disclosure = """
MATCH (pn:PrivacyNotice {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ud:UseAndDisclosure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pn)-[rel:PRIVACY_NOTICE_REQUIRES_USE_AND_DISCLOSURE]->(ud);
"""

#ndividualRight → RegulatoryStandard #
individual_right_regulatory_standard = """
MATCH (ir:IndividualRight {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ir)-[rel:INDIVIDUAL_RIGHT_REQUIRES_REGULATORY_STANDARD]->(rs);
"""

#SecurityStandard → AdministrativeSafeguard #
security_standard_administrative_safeguard = """
MATCH(ss:SecurityStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH(as:AdministrativeSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ss)-[rel:SECURITY_STANDARD_REQUIRES_ADMINISTRATIVE_SAFEGUARDS]->(as);
"""
#SecurityStandard → PhysicalSafeguard #
security_standard_physical_safeguard = """
MATCH(ss:SecurityStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH(ps:PhysicalSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ss)-[rel:SECURITY_STANDARD_REQUIRES_PHYSICAL_SAFEGUARDS]->(ps);
"""
#SecurityStandard → TechnicalSafeguard #
security_standard_technical_safeguard = """
MATCH(ss:SecurityStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH(ts:TechnicalSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ss)-[rel:SECURITY_STANDARD_REQUIRES_TECHNICAL_SAFEGUARDS]->(ts);
"""
#AdministrativeSafeguard → SecurityMeasure #
administrative_safeguards_security_measures = """
MATCH (as:AdministrativeSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sm:SecurityMeasure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (as)-[rel:ADMINISTRATIVE_SAFEGUARD_MEETS_SECURITY_MEASURE]->(sm);
"""
#PhysicalSafeguard → SecurityMeasure #
physical_safeguards_security_measures = """
MATCH (ps:PhysicalSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sm:SecurityMeasure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ps)-[rel:PHYSICAL_SAFEGUARD_MEETS_SECURITY_MEASURE]->(sm);
"""
#TechnicalSafeguard → SecurityMeasure #
technical_safeguards_security_measures = """
MATCH (ts:TechnicalSafeguard {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sm:SecurityMeasure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ts)-[rel:TECHNICAL_SAFEGUARD_MEETS_SECURITY_MEASURE]->(sm);
"""
#RiskAssessment → SecurityVulnerability #
risk_assessment_security_vulnerability = """
MATCH (ra:RiskAssessment {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sv:SecurityVulnerability {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ra)-[rel:RISKASSESSMENT_HAS_SECURITY_VULNERABILITY]->(sv);
"""
#SecurityVulnerability → SecurityRisk #
security_vulnerability_security_risk = """
MATCH (sv:SecurityVulnerability {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sr:SecurityRisk {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sv)-[rel:SECURITY_VULNERABILITY_HAS_SECURITY_RISK]->(sr);
"""

#SecurityRisk → SecurityMeasure#
security_risk_security_measure = """
MATCH (sr:SecurityRisk {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sm:SecurityMeasure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sr)-[rel:SECURITY_RISK_REQUIRES_SECURITY_MEASURE]->(sm);
"""
#SecurityIncident → IncidentResponse #
security_incident_incident_response = """
MATCH (si:SecurityIncident {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ir:IncidentResponse {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (si)-[rel:SECURITY_INCIDENT_REQUIRES_INCIDENT_RESPONSE]->(ir);
"""
#ContingencyPlanning → SecurityMeasure #
Contingency_Planning_Security_Measure = """
MATCH (cp:ContingencyPlanning {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sm:SecurityMeasure {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (cp)-[rel:CONTINGENCY_PLANNING_REQUIRES_SECURITY_MEASURE]->(sm);
"""
#WorkforceSecurity → ComplianceRequirement 
workforce_security_compliance_requirement = """
MATCH (ws:WorkforceSecurity {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cr:ComplianceRequirement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ws)-[rel:WORK_FORCE_SECURITY_REQUIRES_COMPLIANCE_REQUIREMENT]->(cr);
"""
#SecurityBreach → BreachRiskAssessment #
security_breach_breach_risk_assessment = """
MATCH (sb:SecurityBreach {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (bra:BreachRiskAssessment {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sb)-[rel:SECURITY_BREACH_HAS_RISK_ASSESSMENT]->(bra);
"""

#NotificationRecipient → NotificationContent #
notification_recipient_notification_content = """
MATCH (nr:NotificationRecipient {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (nc:NotificationContent {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (nr)-[rel:NOTIFICATION_RECIPIENT_SENDS_NOTIFICATION_CONTENT]->(nc);
"""
# SecurityBreach → BreachTimeline
security_breach_breach_timeline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {breach_id: row.breach_id})
MATCH (bt:BreachTimeline {timeline_id: row.timeline_id})
MERGE (sb)-[rel:SECURITY_BREACH_HAS_TIMELINE {relationship_id: row.relationship_id}]->(bt)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""

#IndustryStandardAndRegulation → CoveredEntity #
industry_standard_and_regulation_covered_entity = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ce:CoveredEntity {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[rel:INDUSTRY_STANDARD_AND_REGULATION_INCLUDES_COVERED_ENTITY]->(ce);
"""

#CoveredEntity → BusinessAssociate #
covered_entity_business_associate = """
MATCH (ce:CoveredEntity {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ba:BusinessAssociate {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_BUSINESS_ASSOCIATE]->(ba);
"""
#CoveredEntity → BusinessAssociateAgreement #
covered_entity_business_associate_agreement = """
MATCH (ce:CoveredEntity {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (baa:BusinessAssociateAgreement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_BUSINESS_ASSOCIATE_AGREEMENT]->(baa);
"""
#BusinessAssociate → BusinessAssociateAgreement #
business_associate_business_associate_agreement = """
MATCH (ba:BusinessAssociate {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (baa:BusinessAssociateAgreement {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ba)-[rel:BUSINESS_ASSOCIATE_HAS_BUSINESS_ASSOCIATE_AGREEMENT]->(baa);
"""
#BusinessAssociate → Subcontractor #
business_associate_subcontractor = """
MATCH (ba:BusinessAssociate {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sbc:Subcontractor {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ba)-[rel:BUSINESS_ASSOCIATE_HAS_SUBCONTRACTOR]->(sbc);
"""
#CoveredEntity → HybridEntity #
covered_entity_hybrid_entity = """
MATCH (ce:CoveredEntity {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (he:HybridEntity {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HYBRID_ENTITY]->(he);
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
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HEALTHCARE_PROVIDER {relationship_id: row.relationship_id}]->(hp)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
# CoveredEntity → HealthPlan
covered_entity_health_plan = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (hpl:HealthPlan {plan_id: row.plan_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_HEALTH_PLAN {relationship_id: row.relationship_id}]->(hpl)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → WorkforceMember
covered_entity_workforce_member = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (wm:WorkforceMember {member_id: row.member_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_WORKFORCE_MEMBER {relationship_id: row.relationship_id}]->(wm)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#CoveredEntity → ComplianceProgram
covered_entity_compliance_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.entity_id})
MATCH (comp:ComplianceProgram {program_id: row.program_id})
MERGE (ce)-[rel:COVERED_ENTITY_HAS_COMPLIANCE_PROGRAM {relationship_id: row.relationship_id}]->(comp)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceProgram → ComplianceAudit
compliance_program_compliance_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (comp:ComplianceProgram {program_id: row.program_id})
MATCH (ca:ComplianceAudit {audit_id: row.audit_id})
MERGE (comp)-[rel:COMPLIANCE_PROGRAM_HAS_COMPLIANCE_AUDIT {relationship_id: row.relationship_id}]->(ca)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceAudit → ComplianceViolation
compliance_audit_compliance_violation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ca:ComplianceAudit {audit_id: row.audit_id})
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MERGE (ca)-[rel:COMPLIANCE_AUDIT_HAS_COMPLIANCE_VIOLATION {relationship_id: row.relationship_id}]->(cv)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → ViolationSeverity
compliance_violation_violation_severity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MATCH (vs:ViolationSeverity {severity_id: row.severity_id})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_HAS_VIOLATION_SEVERITY {relationship_id: row.relationship_id}]->(vs)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → OCRInvestigation
compliance_violation_ocr_investigation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cv:ComplianceViolation {violation_id: row.violation_id})
MATCH (oi:OCRInvestigation {investigation_id: row.investigation_id})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_HAS_OCR_INVESTIGATION {relationship_id: row.relationship_id}]->(oi)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#OCRInvestigation → EnforcementAction
ocr_investigation_enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (oi:OCRInvestigation {investigation_id: row.investigation_id})
MATCH (ea:EnforcementAction {action_id: row.action_id})
MERGE (oi)-[rel:OCR_INVESTIGATION_HAS_ENFORCEMENT_ACTION {relationship_id: row.relationship_id}]->(ea)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CivilPenalty
enforcement_action_civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (cpen:CivilPenalty {penalty_id: row.penalty_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CIVIL_PENALTY {relationship_id: row.relationship_id}]->(cpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CriminalPenalty
enforcement_action_criminal_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (crpen:CriminalPenalty {penalty_id: row.penalty_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CRIMINAL_PENALTY {relationship_id: row.relationship_id}]->(crpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#EnforcementAction → CorrectiveActionPlan
enforcement_action_corrective_action_plan = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {action_id: row.action_id})
MATCH (capl:CorrectiveActionPlan {plan_id: row.plan_id})
MERGE (ea)-[rel:ENFORCEMENT_ACTION_HAS_CORRECTIVE_ACTION_PLAN {relationship_id: row.relationship_id}]->(capl)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#Regulator → EnforcementAction
regulator_enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulator {regulator_id: row.regulator_id})
MATCH (ea:EnforcementAction {action_id: row.action_id})
MERGE (reg)-[rel:REGULATOR_HAS_ENFORCEMENT_ACTION {relationship_id: row.relationship_id}]->(ea)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ViolationSeverity → CivilPenalty
violation_severity_civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (vs:ViolationSeverity {severity_id: row.severity_id})
MATCH (cpen:CivilPenalty {penalty_id: row.penalty_id})
MERGE (vs)-[rel:VIOLATION_SEVERITY_HAS_CIVIL_PENALTY {relationship_id: row.relationship_id}]->(cpen)
ON CREATE SET
    rel.description = row.description,
    rel.created_date = row.created_date;
"""
#ComplianceViolation → RegulatoryStandard##
compliance_violation_regulatory_standard = """
MATCH (cv:ComplianceViolation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (rs:RegulatoryStandard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (cv)-[rel:COMPLIANCE_VIOLATION_VIOLATES_REGULATORY_STANDARD]->(rs);
"""

#CoveredEntity → Designatedofficial
covered_entity_designated_official = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.source_id,industry_standard_regulation_id: 'HIPAA 1996'}) 
MATCH (do:DesignatedOfficial {node_id: row.target_id,industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ce)-[rel:COVERED_ENTITY_DESIGNATES_DESIGNATED_OFFICIAL]->(do)
ON CREATE SET 
    rel.description = row.description,
    rel.citation = row.source_citation_id;
"""
# PreemptionCondition → IndustryStandardAndRegulation
preemption_condition_industry_standard_and_regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pc:PreemptionCondition {node_id: row.source_id,industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (hipaa:IndustryStandardAndRegulation {industry_standard_regulation_id: row.target_id,industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pc)-[rel:PREMPTION_CONDITION_REQUIRES_INDUSTRY_STANDARD_AND_REGULATION]->(hipaa)
ON CREATE SET 
    rel.description = row.description,
    rel.citation = row.source_citation_id;
"""
# HealthPlan → PlanSponsor 
health_plan_plan_sponsor = """
MATCH (hpl:HealthPlan{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (psp:PlanSponsor{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (hpl)-[:HEALTH_PLAN_HAS_PLAN_SPONSOR_INFO]->(psp);
"""
# CoveredEntity → ExternalRecipient
covered_entity_external_recipient = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ce:CoveredEntity {entity_id: row.source_id,industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (rec:ExternalRecipient {node_id: row.target_id,industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (ce)-[rel:COVERED_ENTITY_PERMITTED_EXTERNAL_RECIPIENT]->(rec)
ON CREATE SET 
    rel.description = row.description,
    rel.citation = row.source_citation_id;
"""
# Regulation defines EnforcementAction
regulation_defines_enforcement_action = """
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (cap:CorrectiveActionPlan)
WHERE NOT (reg)-[:REGULATION_DEFINES_CORRECTIVE_ACTION]->(cap)
MERGE (reg)-[:REGULATION_DEFINES_CORRECTIVE_ACTION]->(cap);
"""
# Regulation defines ViolationSeverity
regulation_defines_violation_severity = """
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (vs:ViolationSeverity)
WHERE NOT (reg)-[:REGULATION_DEFINES_SEVERITY_METRIC]->(vs)
MERGE (reg)-[:REGULATION_DEFINES_SEVERITY_METRIC]->(vs);
"""
# Regulation protects AffectedIndividual
regulation_protects_affected_individual = """
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ai:AffectedIndividual)
WHERE NOT (reg)-[:REGULATION_PROTECTS_INDIVIDUAL]->(ai)
MERGE (reg)-[:REGULATION_PROTECTS_INDIVIDUAL]->(ai);
"""
# Regulation establishes LawfulBasis
regulation_establishes_lawful_basis = """
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (lb:LawfulBasis)
WHERE NOT (reg)-[:REGULATION_ESTABLISHES_LAWFUL_BASIS]->(lb)
MERGE (reg)-[:REGULATION_ESTABLISHES_LAWFUL_BASIS]->(lb);
"""
# Regulation -> Standard
regulation_standard = """
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (std:Standard{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (reg)-[:REGULATION_DEFINES_STANDARD]->(std);
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

# client.query(cfr_sections.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cfr_sections.csv'))
# time.sleep(2)

# client.query(cfr_citation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20CFR%20Citation.csv"))
# time.sleep(2)


# client.query(regulatory_standards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulatory_standards.csv"))
# time.sleep(2)

# client.query(Compliance_Requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance_requirements.csv"))
# time.sleep(2)

# client.query(Implementation_Specifications.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/implementation_specs.csv"))
# time.sleep(2)

# client.query(Electronic_PHI.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/electronic_phi.csv"))
# time.sleep(2)

# client.query(PHI_Categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_categories.csv"))
# time.sleep(2)

# client.query(PHI_Forms.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_forms.csv"))
# time.sleep(2)

# client.query(PHI_Locations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_locations.csv"))
# time.sleep(2)

# client.query(PHI_Lifecycle.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/phi_lifecycle.csv"))
# time.sleep(2)

# client.query(sensitive_data_elements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sensitive_data_elements.csv"))
# time.sleep(2)

# client.query(data_uses.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_uses.csv"))
# time.sleep(2)

# client.query(data_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_disclosures.csv"))
# time.sleep(2)

# client.query(minimum_necessary.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/minimum_necessary.csv"))
# time.sleep(2)

# client.query(de_indentified_health_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/deidentified_health_info.csv"))
# time.sleep(2)

# client.query(limited_data_set.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/limited_data_set.csv"))
# time.sleep(2)

# client.query(data_use_agreement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_use_agreement.csv"))
# time.sleep(2)


# client.query(individual_rights.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/individual_rights.csv"))
# time.sleep(2)

# client.query(data_subjects.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/data_subjects.csv"))
# time.sleep(2)

# client.query(use_and_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/use_and_disclosure.csv"))
# time.sleep(2)

# client.query(authorizations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/authorizations.csv"))
# time.sleep(2)

# client.query(lawful_basis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/lawful_basis.csv"))
# time.sleep(2)

# client.query(patient_requests.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/patient_requests.csv"))
# time.sleep(2)

# client.query(privacy_complaints.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/privacy_complaints.csv"))
# time.sleep(2)

# client.query(privacy_notices.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/privacy_notices.csv"))
# time.sleep(2)

# client.query(psychotherapy_notes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/psychotherapy_notes.csv"))
# time.sleep(2)

# client.query(marketing_authorization.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/marketing_authorizations.csv"))
# time.sleep(2)

# client.query(security_standards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_standards.csv"))
# time.sleep(2)

# client.query(administrative_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/administrative_safeguards.csv"))
# time.sleep(2)

# client.query(physical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/physical_safeguards.csv"))
# time.sleep(2)

# client.query(technical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/technical_safeguards.csv"))
# time.sleep(2)

# client.query(security_measures.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_measures.csv"))
# time.sleep(2)

# client.query(risk_assessments.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/risk_assessment.csv"))
# time.sleep(2)

# client.query(security_incidents.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_incidents.csv"))
# time.sleep(2)

# client.query(Incident_Response.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/incident_response.csv"))
# time.sleep(2)

# client.query(security_vulnerabilities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security_vulnerabilities.csv"))
# time.sleep(2)


# client.query(security_risks.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security-risks.csv"))
# time.sleep(2)

# client.query(contingency_planning.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/contingency-planning.csv"))
# time.sleep(2)

# client.query(workforce_security.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/workforce-security.csv"))
# time.sleep(2)


# client.query(security_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/security-breach.csv"))
# time.sleep(2)

# client.query(breach_risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-risk-assess.csv"))
# time.sleep(2)


# client.query(affected_individuals.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/affected-individuals.csv"))
# time.sleep(2)

# client.query(notification_receipients.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/notif-recipients.csv"))
# time.sleep(2)

# client.query(notfication_content.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/notif-content.csv"))
# time.sleep(2)

# client.query(breach_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/breach-timeline.csv"))
# time.sleep(2)

# client.query(Covered_Entities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/covered-entities.csv"))
# time.sleep(2)

# client.query(business_associates.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/business-associates.csv"))
# time.sleep(2)

# client.query(Subcontractors.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/subcontractors.csv"))
# time.sleep(2)

# client.query(Business_Associate_Agreements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/BusinessAssociateAgreement.csv"))
# time.sleep(2)

# client.query(Hybrid_Entities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Hybrid%20Entities.csv"))
# time.sleep(2)

# client.query(OHCA.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ohca.csv"))
# time.sleep(2)

# client.query(Healthcare_Providers.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/healthcare-providers.csv"))
# time.sleep(2)

# client.query(Health_Plans.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/health-plans.csv"))
# time.sleep(2)

# client.query(Workforce_Members.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/workforce-members.csv"))
# time.sleep(2)

# client.query(Compliance_Programs.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-programs.csv"))
# time.sleep(2)

# client.query(Compliance_Audits.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-audits.csv"))
# time.sleep(2)

# client.query(Compliance_Violations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/compliance-violations.csv"))
# time.sleep(2)

# client.query(Violation_Severities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/violation-severities.csv"))
# time.sleep(2)

# client.query(OCR_Investigations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ocr-investigations.csv"))
# time.sleep(2)

# client.query(Enforcement_Actions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/enforcement-actions.csv"))
# time.sleep(2)

# client.query(Civil_Penalties.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/civil-penalties.csv"))
# time.sleep(2)

# client.query(Criminal_Penalties.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/criminal-penalties.csv"))
# time.sleep(2)

# client.query(Corrective_Action_Plans.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/corrective-action-plans.csv"))
# time.sleep(2)

# client.query(Regulators.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulators.csv"))
# time.sleep(2)

# client.query(designated_officials.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Designated%20Official.csv"))
# time.sleep(2)

# client.query(preemption_conditions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Preemption%20Condition.csv"))
# time.sleep(2)

# client.query(plan_sponsors.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Plan%20Sponser.csv"))
# time.sleep(2)

# client.query(external_recipients.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20External%20Receiptent.csv"))
# time.sleep(2)

client.query(standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_standards.csv"))
time.sleep(2)


#Relationships

# client.query(industry_standard_and_regulations_hipaa_standards_rel)
# time.sleep(2)

# client.query(hipaa_nist_mapping)
# time.sleep(2)

# client.query(industry_standard_and_regulation_cfr_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/isr-cfr-section.csv"))
# time.sleep(2)


# client.query(CFR_citation_regulatory_standard)
# time.sleep(2)

# client.query(regulatory_standard_compliance_requirement)
# time.sleep(2)

# client.query(Compliance_Requirements_Implementation_Specification)
# time.sleep(2)

# client.query(regulatory_standard_implementation_specification)
# time.sleep(2)

# client.query(electronic_phi_phi_category)
# time.sleep(2)

# client.query(phi_category_sensitive_data_element)
# time.sleep(2)

# client.query(electronic_phi_phi_form)
# time.sleep(2)

# client.query(electronic_phi_phi_location)
# time.sleep(2)

# client.query(electronic_phi_phi_lifecycle)
# time.sleep(2)


# client.query(data_use_electronic_phi)
# time.sleep(2)

# client.query(data_disclosure_electronic_phi)
# time.sleep(2)

# client.query(minimum_necessary_electronic_phi)
# time.sleep(2)

# client.query(deidentified_health_info_electronic_phi)
# time.sleep(2)

# client.query(limited_data_set_data_use_agreement)
# time.sleep(2)

# client.query(phi_lifecycle_compliance_requirement)
# time.sleep(2)

# client.query(data_use_agreement_data_use)
# time.sleep(2)

# client.query(individual_right_data_subject)
# time.sleep(2)

# client.query(use_and_disclosure_authorization)
# time.sleep(2)

# client.query(data_subject_patient_request)
# time.sleep(2)

# client.query(patient_request_compliance_requirement)
# time.sleep(2)

# client.query(privacy_complaint_privacy_notice)
# time.sleep(2)

# client.query(psychotherapy_notes_authorization)
# time.sleep(2)

# client.query(marketing_authorization_use_and_disclosure)
# time.sleep(2)

# client.query(privacy_notice_use_and_disclosure)
# time.sleep(2)

# client.query(individual_right_regulatory_standard)
# time.sleep(2)

# client.query(security_standard_administrative_safeguard)
# time.sleep(2)

# client.query(security_standard_physical_safeguard)
# time.sleep(2)

# client.query(security_standard_technical_safeguard)
# time.sleep(2)


# client.query(administrative_safeguards_security_measures)
# time.sleep(2)

# client.query(physical_safeguards_security_measures)
# time.sleep(2)

# client.query(technical_safeguards_security_measures)
# time.sleep(2)

# client.query(risk_assessment_security_vulnerability)
# time.sleep(2)


# client.query(security_vulnerability_security_risk)
# time.sleep(2)

# client.query(security_risk_security_measure)
# time.sleep(2)

# client.query(security_incident_incident_response)
# time.sleep(2)

# client.query(Contingency_Planning_Security_Measure)
# time.sleep(2)

# client.query(workforce_security_compliance_requirement)
# time.sleep(2)

# client.query(security_breach_breach_risk_assessment)
# time.sleep(2)

# client.query(notification_recipient_notification_content)
# time.sleep(2)

# client.query(security_breach_breach_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/sb-timeline.csv"))
# time.sleep(2)

# client.query(industry_standard_and_regulation_covered_entity)
# time.sleep(2)

# client.query(covered_entity_business_associate)
# time.sleep(2)

# client.query(covered_entity_business_associate_agreement)
# time.sleep(2)

# client.query(business_associate_business_associate_agreement)
# time.sleep(2)

# client.query(business_associate_subcontractor)
# time.sleep(2)

# client.query(covered_entity_hybrid_entity)
# time.sleep(2)

# client.query(covered_entity_ohca.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-ohca.csv"))
# time.sleep(2)

# client.query(covered_entity_healthcare_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-provider.csv"))
# time.sleep(2)

# client.query(covered_entity_health_plan.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-healthplan.csv"))
# time.sleep(2)

# client.query(covered_entity_workforce_member.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-workforce.csv"))
# time.sleep(2)

# client.query(covered_entity_compliance_program.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ce-compliance.csv"))
# time.sleep(2)

# client.query(compliance_program_compliance_audit.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cp-audit.csv"))
# time.sleep(2)

# client.query(compliance_audit_compliance_violation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ca-violation.csv"))
# time.sleep(2)

# client.query(compliance_violation_violation_severity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cv-severity.csv"))
# time.sleep(2)

# client.query(compliance_violation_ocr_investigation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/cv-investigation.csv"))
# time.sleep(2)

# client.query(ocr_investigation_enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/oi-enforcement.csv"))
# time.sleep(2)

# client.query(enforcement_action_civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-civil-penalty.csv"))
# time.sleep(2)

# client.query(enforcement_action_criminal_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-criminal-penalty.csv"))
# time.sleep(2)

# client.query(enforcement_action_corrective_action_plan.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/ea-corrective-action.csv"))
# time.sleep(2)

# client.query(regulator_enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/regulator-enforcement.csv"))
# time.sleep(2)

# client.query(violation_severity_civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/vs-civil-penalty.csv"))
# time.sleep(2)

# client.query(compliance_violation_regulatory_standard)
# time.sleep(2)

# client.query(covered_entity_designated_official.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Covered%20Entity%20Designated%20Officials.csv"))
# time.sleep(2)

# client.query(preemption_condition_industry_standard_and_regulation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Preemption%20Condition%20Regulation.csv"))
# time.sleep(2)

# client.query(health_plan_plan_sponsor)
# time.sleep(2)

# client.query(covered_entity_external_recipient.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/HIPAA%20-%20Covered%20Entity%20External%20Recipients.csv"))
# time.sleep(2)

# client.query(regulation_defines_enforcement_action)
# time.sleep(2)

# client.query(regulation_defines_violation_severity)
# time.sleep(2)

# client.query(regulation_protects_affected_individual)
# time.sleep(2)

# client.query(regulation_establishes_lawful_basis)
# time.sleep(2)

client.query(regulation_standard)
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
    with open('hipaa.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to hipaa.json")
else:
    logger.error("No data returned from the query.")

client.close()
