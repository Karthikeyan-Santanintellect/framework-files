# Create SEC Regulation Node
regional_standard_and_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    reg.name = "SEC Cybersecurity Disclosure Rules",
    reg.version = "2023",
    reg.authority = "U.S. Securities and Exchange Commission",
    reg.effective_date = date("2023-09-05"),
    reg.jurisdiction = "United States",
    reg.type = "Federal Regulation",
    reg.description = "Rules requiring public companies to disclose material cybersecurity incidents and annual cybersecurity risk management, strategy, and governance.";
"""

# Create Disclosure Category Node
sec_disclosure_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cat:Category {categoryId: row.categoryId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    cat.name = row.name,
    cat.description = row.description,
    cat.frequency = row.frequency;
"""

# Create Disclosure Requirement Node
sec_disclosure_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {reqId: row.reqId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    req.title = row.title,
    req.category = row.category,
    req.description = row.description;
"""

# Create Regulatory Form Node
sec_regulatory_form = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rf:RegulatoryForm {formId: row.formId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    rf.name = row.name,
    rf.description = row.description,
    rf.filingDeadline = row.filingDeadline;
"""

# Create Filing Timeline Node
sec_filing_timeline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ft:FilingTimeline {timelineId: row.timelineId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    ft.name = row.name,
    ft.duration = row.duration,
    ft.triggerEvent = row.triggerEvent;
"""

# Create Delay Provision Node
sec_delay_provision = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DelayProvision {provisionId: row.provisionId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    dp.reason = row.reason,
    dp.maxDelayDays = row.maxDelayDays,
    dp.approver = row.approver;
"""

# Create Regulated Entity Node
sec_regulated_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (re:RegulatedEntity {entityType: row.entityType, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    re.description = row.description,
    re.complianceDate = row.complianceDate;
"""

# Create Governance Body Node
sec_governance_body = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (gb:GovernanceBody {governanceId: row.governanceId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    gb.name = row.committeeName,
    gb.type = "Board Committee",
    gb.primaryResponsibility = row.primaryResponsibility;
"""

# Create Board Committee Type Node
sec_board_committee_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bct:BoardCommitteeType {typeId: row.typeId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    bct.name = row.name,
    bct.focusArea = row.focusArea;
"""

# Create Management Role Node
sec_management_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mgr:ManagementRole {roleId: row.roleId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    mgr.title = row.roleTitle,
    mgr.function = row.function,
    mgr.reportingLine = row.reportingLine;
"""

# Create External Actor Node
sec_external_actor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:ExternalActor {name: row.name, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    ea.role = row.role,
    ea.category = row.category;
"""

# Create Cybersecurity Incident Node
sec_cybersecurity_incident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ci:CybersecurityIncident {incidentId: row.incidentId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    ci.description = row.description,
    ci.detectionDate = row.detectionDate;
"""

# Create Material Cybersecurity Incident Node
sec_material_cybersecurity_incident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mci:MaterialCybersecurityIncident {incidentId: row.incidentId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    mci.materialityDate = row.materialityDate,
    mci.disclosureStatus = row.disclosureStatus;
"""

# Create Information System Node
sec_information_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (is:InformationSystem {systemId: row.systemId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    is.systemType = row.systemType,
    is.description = row.description,
    is.owner = row.owner;
"""

# Create Incident Type Node
sec_incident_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (it:IncidentType {typeId: row.typeId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    it.name = row.name,
    it.definition = row.definition;
"""

# Create Impact Category Node
sec_impact_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ic:ImpactCategory {categoryId: row.categoryId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    ic.name = row.name,
    ic.description = row.description;
"""

# Create Risk Management Process Node
sec_risk_management_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rmp:RiskManagementProcess {processId: row.processId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    rmp.name = row.processName,
    rmp.description = row.description;
"""

# Create Cybersecurity Framework Node (External Standards)
sec_cybersecurity_framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:CybersecurityFramework {frameworkNodeId: row.frameworkNodeId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    cf.name = row.standardName,
    cf.description = row.description;
"""

# Create Security Control Node
sec_security_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:SecurityControl {controlId: row.controlId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    sc.name = row.name,
    sc.type = row.type,
    sc.description = row.description;
"""

# Create Expertise Node
sec_expertise = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (exp:Expertise {expertiseId: row.expertiseId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    exp.name = row.certName,
    exp.issuer = row.issuer,
    exp.domain = row.domain;
"""

# Create Board Oversight Process Node
sec_board_oversight_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bop:BoardOversightProcess {processId: row.processId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    bop.name = row.name,
    bop.frequency = row.frequency,
    bop.description = row.description;
"""

# Create Filing Event Node
sec_filing_event = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fe:FilingEvent {eventId: row.eventId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    fe.type = row.type,
    fe.description = row.description,
    fe.trigger = row.trigger;
"""

# Create XBRL Tagging Node
sec_xbrl_tagging = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (xbrl:XBRLTagging {xbrlId: row.xbrlId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    xbrl.taxonomy = row.taxonomy,
    xbrl.format = row.format,
    xbrl.effectiveDate = row.effectiveDate;
"""

# Create Compliance Deadline Node
sec_compliance_deadline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tl:ComplianceDeadline {deadlineId: row.deadlineId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    tl.description = row.description,
    tl.date = row.date;
"""

# Create Exemption Node
sec_exemption = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:Exemption {exemptionId: row.exemptionId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    ex.name = row.name,
    ex.description = row.description,
    ex.duration = row.duration;
"""

# Create Materiality Determination Node
sec_materiality_determination = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (md:MaterialityDetermination {determinationId: row.determinationId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    md.outcome = row.outcome,
    md.date = date(row.date),
    md.justification = row.justification;
"""

# Create Assessment Standard Node (Materiality)
sec_assessment_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (std:AssessmentStandard {standardId: row.standardId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    std.name = row.standardName,
    std.legalSource = row.legalSource,
    std.definition = row.definition;
"""

# Create Quantitative Factor Node
sec_quantitative_factor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (qtf:QuantitativeFactor {factorId: row.factorId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    qtf.name = row.factorName,
    qtf.metricType = row.metricType;
"""

# Create Qualitative Factor Node
sec_qualitative_factor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (qlf:QualitativeFactor {factorId: row.factorId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    qlf.name = row.factorName,
    qlf.riskCategory = row.riskCategory;
""" 

# Create Assessment Team Node
sec_assessment_team = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (at:AssessmentTeam {teamId: row.teamId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    at.name = row.name,
    at.primaryRole = row.primaryRole;
"""
 # Create Third-Party Service Provider Node
sec_third_party_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tpsp:ThirdPartyServiceProvider {providerId: row.providerId, regional_standard_regulation_id: 'SEC-2023'})
ON CREATE SET 
    tpsp.name = row.name,
    tpsp.serviceType = row.serviceType,
    tpsp.accessLevel = row.accessLevel;
"""


# Relationships

# Regulation → Disclosure Category
regulation_disclosure_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (cat:Category {categoryId: row.categoryId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_CATEGORY {order: row.order}]->(cat);
"""

# Regulation → Disclosure Requirement
regulation_disclosure_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (req:Requirement {reqId: row.reqId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_REQUIREMENT {order: row.order}]->(req);
"""

# Requirement → Regulatory Form
requirement_regulatory_form = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {reqId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (rf:RegulatoryForm {formId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (req)-[:REQUIREMENT_IMPLEMENTED_VIA_FORM]->(rf);
"""

# Regulatory Form → Filing Timeline
regulatory_form_timeline = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rf:RegulatoryForm {formId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (ft:FilingTimeline {timelineId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (rf)-[:FORM_FOLLOWS_TIMELINE]->(ft);
"""

# Regulatory Form → Delay Provision
regulatory_form_delay = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rf:RegulatoryForm {formId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (dp:DelayProvision {provisionId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (rf)-[:FORM_MAY_BE_DELAYED_BY_PROVISION]->(dp);
"""

# Regulatory Form → XBRL Tagging
regulatory_form_xbrl = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rf:RegulatoryForm {formId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (xbrl:XBRLTagging {xbrlId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (rf)-[:FORM_REQUIRES_XBRL_TAGGING]->(xbrl);
"""

# Regulated Entity → Regulation (Subject To)
regulated_entity_regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_SUBJECT_TO_REGULATION]->(reg);
"""

# Regulated Entity → Exemption
regulated_entity_exemption = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (ex:Exemption {exemptionId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_QUALIFIES_FOR_EXEMPTION]->(ex);
"""

# Governance Body → Board Committee Type
governance_body_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (gb:GovernanceBody {governanceId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (bct:BoardCommitteeType {typeId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (gb)-[:GOVERNANCE_BODY_IS_TYPE_OF_BOARD_COMMITTEE]->(bct);
"""

# Management Role → Governance Body (Reports To)
management_role_governance_body = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (mgr:ManagementRole {roleId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (gb:GovernanceBody {governanceId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (mgr)-[:MANAGEMENT_ROLE_REPORTS_TO_GOVERNANCE_BODY]->(gb);
"""

# Management Role → Expertise
management_role_expertise = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (mgr:ManagementRole {roleId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (exp:Expertise {expertiseId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (mgr)-[:MANAGEMENT_ROLE_POSSESSES_EXPERTISE]->(exp);
"""

# Assessment Team → Management Role (Composed Of)
assessment_team_management_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (at:AssessmentTeam {teamId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (mgr:ManagementRole {roleId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (at)-[:ASSESSMENT_TEAM_INCLUDES_ROLE]->(mgr);
"""

# Regulated Entity → Information System
regulated_entity_information_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (is:InformationSystem {systemId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_OWNS_OR_USES_SYSTEM]->(is);
"""

# Requirement → Risk Management Process
requirement_risk_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row 
MATCH (req:Requirement {reqId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (rmp:RiskManagementProcess {processId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (req)-[:REQUIREMENT_GOVERNS_RISK_PROCESS]->(rmp);
"""

# Risk Management Process → Cybersecurity Framework
risk_process_framework = """ 
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rmp:RiskManagementProcess {processId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (cf:CybersecurityFramework {frameworkNodeId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (rmp)-[:RISK_PROCESS_ALIGNS_WITH_FRAMEWORK]->(cf);
"""

# Risk Management Process → Security Control
risk_process_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rmp:RiskManagementProcess {processId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (sc:SecurityControl {controlId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (rmp)-[:RISK_PROCESS_IMPLEMENTS_CONTROL]->(sc);
"""

# Governance Body → Board Oversight Process
governance_body_oversight = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (gb:GovernanceBody {governanceId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (bop:BoardOversightProcess {processId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (gb)-[:GOVERNANCE_BODY_EXECUTES_OVERSIGHT]->(bop);
"""

# Cybersecurity Incident → Incident Type
incident_incident_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ci:CybersecurityIncident {incidentId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (it:IncidentType {typeId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (ci)-[:CYBERSECURITY_INCIDENT_HAS_TYPE]->(it);
"""

# Cybersecurity Incident → Information System
incident_information_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ci:CybersecurityIncident {incidentId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (is:InformationSystem {systemId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (ci)-[:CYBERSECURITY_INCIDENT_AFFECTS_SYSTEM]->(is);
"""

# Cybersecurity Incident → Impact Category
incident_impact_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ci:CybersecurityIncident {incidentId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (ic:ImpactCategory {categoryId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (ci)-[:CYBERSECURITY_INCIDENT_CAUSES_IMPACT]->(ic);
"""

# Materiality Determination → Cybersecurity Incident
materiality_determination_incident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (md:MaterialityDetermination {determinationId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (ci:CybersecurityIncident {incidentId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (md)-[:MATERIALITY_DETERMINATION_EVALUATES_INCIDENT]->(ci);
"""

# Materiality Determination → Assessment Standard
materiality_determination_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (md:MaterialityDetermination {determinationId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (std:AssessmentStandard {standardId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (md)-[:MATERIALITY_DETERMINATION_APPLIES_STANDARD]->(std);
"""

# Assessment Standard → Quantitative Factor
assessment_standard_quantitative = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (std:AssessmentStandard {standardId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (qtf:QuantitativeFactor {factorId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (std)-[:ASSESSMENT_STANDARD_CONSIDERS_QUANTITATIVE_FACTOR]->(qtf);
"""

# Assessment Standard → Qualitative Factor
assessment_standard_qualitative = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (std:AssessmentStandard {standardId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (qlf:QualitativeFactor {factorId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (std)-[:ASSESSMENT_STANDARD_CONSIDERS_QUALITATIVE_FACTOR]->(qlf);
"""

# Assessment Team → Materiality Determination
assessment_team_determination = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (at:AssessmentTeam {teamId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (md:MaterialityDetermination {determinationId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (at)-[:ASSESSMENT_TEAM_CONDUCTS_DETERMINATION]->(md);
"""

# Materiality Determination → Material Cybersecurity Incident (Outcome)
determination_material_incident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (md:MaterialityDetermination {determinationId: row.sourceId, regional_standard_regulation_id: 'SEC-2023'})
MATCH (mci:MaterialCybersecurityIncident {incidentId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (md)-[:MATERIALITY_DETERMINATION_RESULTED_IN_MATERIAL_INCIDENT]->(mci);
"""
# Regulated Entity to its Governance Body (Board)
regulated_entity_governace = """  
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.entityType}) 
MATCH (gb:GovernanceBody {governanceId: row.governanceId})
MERGE (re)-[:REGULATED_ENTITY_ESTABLISHES_GOVERNANCE_STRUCTURE]->(gb);
"""
# Regulated Entity to Key Management Roles
regulated_entity_management_roles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.entityType})
MATCH (mgr:ManagementRole {roleId: row.roleId})   
MERGE (re)-[:REGULATED_ENTITY_KEY_APPOINTS_MANAGEMENT_ROLE]->(mgr);
"""
# Regulated Entity to Assessment Teams
regulated_entity_assessment_teams = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.entityType})
MATCH (at:AssessmentTeam {teamId: row.teamId})   
MERGE (re)-[:REGULATED_ENTITY_RESIGNATES_ASSESSMENT_TEAM]->(at);
"""
# Regulated Entity to the Processes
regulated_entity_risk_management_processes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row   
MATCH (re:RegulatedEntity {entityType: row.entityType})
MATCH (rmp:RiskManagementProcess {processId: row.processId})
MERGE (re)-[:REGULATED_ENTITY_IMPLEMENTS_RISK_PROCESS]->(rmp);
"""
# Regulated Entity to its specific Compliance Deadlines
regulated_entity_compliance_deadlines = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row  
MATCH (re:RegulatedEntity {entityType: row.entityType})
MATCH (cd:ComplianceDeadline {deadlineId: row.deadlineId})
MERGE (re)-[:REGULATED_ENTITY_MUST_COMPLY_BY_DATE]->(cd);
"""
# Anchor Incident Types to the Regulation
regulation_incident_types = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (it:IncidentType {regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGULATION_DEFINES_RECOGNIZED_INCIDENT_TYPE]->(it);
"""
# Anchor Impact Categories to the Regulation
regulation_impact_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (ic:ImpactCategory{targetId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGULATION_DEFINES_MATERIALITY_IMPACT_FACTOR]->(ic);
"""
# Anchor Professional Expertise Requirements to the Regulation
regulation_expertise_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (exp:Expertise{targetId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGULATION_RECOGNIZES_PROFESSIONAL_CREDENTIAL]->(exp);
"""

#Anchor Assessment Standards (Reasonable Investor) to the Regulation
regulation_assessment_standards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MATCH (std:AssessmentStandard{standardId: row.standardId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGULATION_ESTABLISHES_LEGAL_STANDARD]->(std);
"""
# Regulated Entity -> Filing Event (Data Driven)
regulated_entity_filing_event = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {regional_standard_regulation_id: 'SEC-2023'})
MATCH (fe:FilingEvent{targetId: row.targetId, regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_SUBMITS_FILING]->(fe);
"""
 # Filing Event -> Regulatory Form (Data Driven)
filing_event_form = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (fe:FilingEvent {eventId: row.eventId})
MATCH (rf:RegulatoryForm {formId: row.formId})
MERGE (fe)-[:REGULATORY_FILING_UTILIZES_FORM]->(rf);  
"""
# Third-Party Service Provider Relationships
regulated_entity_third_party_service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (re:RegulatedEntity {entityType: row.entityType})  
MATCH (tpsp:ThirdPartyServiceProvider {providerId: row.providerId})
MERGE (re)-[:REGULATED_ENTITY_ENGAGES_SERVICE_PROVIDER {
    oversight_level: row.oversightLevel,
    contractual_audit_rights: row.auditRights
}]->(tpsp);
"""
# Management Role -> External Actor
management_role_external_actor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (mgr:ManagementRole {roleId: row.roleId})
MATCH (ea:ExternalActor {name: row.actorName})   
MERGE (mgr)-[:MANAGEMENT_INTERACTS_WITH_EXTERNAL_ACTOR {
    context: row.context,
    frequency: row.frequency
}]->(ea);
"""
# Regulation -> Board commitee
regulation_board_committee = """
MATCH (orphan:BoardCommitteeType)WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_BOARD_COMMITTEE]->(orphan);
"""
# Regulated Entity -> Filling Event
entity_filing_event = """
MATCH (orphan:FilingEvent)WHERE NOT EXISTS ((orphan)--())
MATCH (re:RegulatedEntity {regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_SUBMITS_FILING]->(orphan);
"""

# Regulation -> Regulated Entity
regulation_regulated_entity = """
MATCH (orphan:RegulatedEntity)WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_REGULATED_ENTITY]->(orphan);
"""
# Regulated Entity -> Management Roles
entity_management_roles = """
MATCH (orphan:ManagementRole)WHERE NOT EXISTS ((orphan)--())
MATCH (re:RegulatedEntity {regional_standard_regulation_id: 'SEC-2023'})
MERGE (re)-[:REGULATED_ENTITY_KEY_APPOINTS_MANAGEMENT_ROLE]->(orphan);
"""
# Regulated Entity -> Risk Management
entity_risk_management = """
MATCH (orphan:RiskManagementProcess)WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'SEC-2023'})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_RISK_MANAGEMENT_PROCESS]->(orphan);
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

client.query(regional_standard_and_regulation)
time.sleep(2)

client.query(sec_disclosure_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Disclosure%20Category.csv"))
time.sleep(2)


client.query(sec_disclosure_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Disclosure%20Requirement.csv"))
time.sleep(2)


client.query(sec_regulatory_form.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulatory%20Form.csv"))
time.sleep(2)

client.query(sec_filing_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Filing%20Timeline.csv"))
time.sleep(2)

client.query(sec_delay_provision.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Delay%20Provision.csv"))
time.sleep(2)

client.query(sec_regulated_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulated%20Entity.csv"))
time.sleep(2)

client.query(sec_governance_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Governance%20Body.csv"))
time.sleep(2)

client.query(sec_board_committee_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Board%20Committee%20Type.csv"))
time.sleep(2)

client.query(sec_management_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Management%20Role.csv"))
time.sleep(2)


client.query(sec_external_actor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20External%20Actor.csv"))
time.sleep(2)


client.query(sec_cybersecurity_incident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Cybersecurity%20Incident.csv"))
time.sleep(2)

client.query(sec_material_cybersecurity_incident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Material%20Cybersecurity%20Incident.csv"))
time.sleep(2)


client.query(sec_information_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Information%20System.csv"))
time.sleep(2)


client.query(sec_incident_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Incident%20Type.csv"))
time.sleep(2)


client.query(sec_impact_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Impact%20Category.csv"))
time.sleep(2)

client.query(sec_risk_management_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Risk%20Management%20Process.csv"))
time.sleep(2)

client.query(sec_cybersecurity_framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Cybersecurity%20Framework.csv"))
time.sleep(2)

client.query(sec_security_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Security%20Control.csv"))
time.sleep(2)

client.query(sec_expertise.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Expertise.csv"))
time.sleep(2)


client.query(sec_board_oversight_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Board%20Oversight%20Process.csv"))
time.sleep(2)

client.query(sec_filing_event.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Filing%20Event.csv"))
time.sleep(2)


client.query(sec_xbrl_tagging.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20XBRL%20Tagging.csv"))
time.sleep(2)


client.query(sec_compliance_deadline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Compliance%20Deadline.csv"))
time.sleep(2)


client.query(sec_exemption.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Exemption.csv"))
time.sleep(2)


client.query(sec_materiality_determination.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Materiality%20Determination.csv"))
time.sleep(2)


client.query(sec_assessment_standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Assessment%20Standard.csv"))
time.sleep(2)


client.query(sec_quantitative_factor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Quantitative%20Factor.csv"))
time.sleep(2)
                                        

client.query(sec_qualitative_factor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Qualitative%20Factor.csv"))
time.sleep(2)


client.query(sec_assessment_team.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Assessment%20Team.csv"))
time.sleep(2)

client.query(sec_third_party_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Third%20Party%20Service%20Provider.csv"))
time.sleep(2)


# Relationships
client.query(regulation_disclosure_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20Disclosure%20Category%20Rel.csv"))
time.sleep(2)

client.query(regulation_disclosure_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20Requirements%20Rel.csv"))
time.sleep(2)

client.query(requirement_regulatory_form.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Requirement%20RegulatoryForm%20Relationship.csv"))
time.sleep(2)


client.query(regulatory_form_timeline.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulatory%20Form%20Filling%20Relationship.csv"))
time.sleep(2)

client.query(regulatory_form_delay.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulatory%20Form%20Delay%20Provison.csv"))
time.sleep(2)

client.query(regulatory_form_xbrl.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatoryForm%20XBRLTagging%20Relationship.csv"))
time.sleep(2)

client.query(regulated_entity_regulation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulatory%20Entity%20Regulation.csv"))
time.sleep(2)

client.query(regulated_entity_exemption.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulatory%20Entity%20Exemption.csv"))
time.sleep(2)

client.query(governance_body_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Governance%20Body%20Board%20Commitee%20.csv"))
time.sleep(2)


client.query(management_role_governance_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-ManagementRole%20GovernanceBody%20Relationship.csv"))
time.sleep(2)


client.query(management_role_expertise.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20ManagementRole%20Expertise.csv"))
time.sleep(2)


client.query(assessment_team_management_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20AssessmentTeam%20ManagementRole.csv"))
time.sleep(2)


client.query(regulated_entity_information_system.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20InformationSystem%20Relationship.csv"))
time.sleep(2)


client.query(requirement_risk_process.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Requirement%20RiskManagementProcess%20Relationship.csv"))
time.sleep(2)


client.query(risk_process_framework.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RiskProcess%20CybersecurityFramework%20Relationship.csv"))
time.sleep(2)

client.query(risk_process_control.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RiskProcess%20SecurityControl%20Relatioship.csv"))
time.sleep(2)


client.query(governance_body_oversight.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20GovernanceBody%20BoardOversightProcess%20Relationship.csv"))
time.sleep(2)


client.query(incident_incident_type.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20CybersecurityIncident_IncidentType%20Relationship.csv"))
time.sleep(2)

client.query(incident_information_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20CybersecurityIncident_InformationSystem%20Relationship.csv"))
time.sleep(2)

client.query(incident_impact_category.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20CybersecurityIncident_ImpactCategory%20Relationship.csv"))
time.sleep(2)


client.query(materiality_determination_incident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20MaterialityDetermination%20MaterialIncident.csv"))
time.sleep(2)


client.query(materiality_determination_standard.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20MaterialityDetermination_AssessmentStandard%20Relationship.csv"))
time.sleep(2)

client.query(assessment_standard_quantitative.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20AssessmentStandard_QuantitativeFactor%20Relationship.csv"))
time.sleep(2)

client.query(assessment_standard_qualitative.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20AssessmentStandard%20QualitativeFactor%20Relationship.csv"))
time.sleep(2)

client.query(assessment_team_determination.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20AssessmentTeam%20MaterialityDetermination%20Rel.csv"))
time.sleep(2)

client.query(determination_material_incident.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20MaterialityDetermination%20MaterialIncident.csv"))
time.sleep(2)


client.query(regulation_incident_types.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20Incident%20Type.csv"))
time.sleep(2)

client.query(regulation_impact_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20ImpactCategory.csv"))
time.sleep(2)

client.query(regulation_expertise_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20Expertise.csv"))
time.sleep(2)

client.query(regulation_assessment_standards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20Regulation%20AssessmentStandard.csv"))
time.sleep(2)

client.query(regulated_entity_filing_event.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20%20FilingEvent.csv"))
time.sleep(2)

client.query(filing_event_form.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20FilingEvent%20RegulatoryForm.csv"))
time.sleep(2)

client.query(regulated_entity_governace.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20GovernanceStructure.csv"))
time.sleep(2)

client.query(regulated_entity_management_roles.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20ManagementRole.csv"))
time.sleep(2)

client.query(regulated_entity_assessment_teams.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20AssessmentTeam.csv"))
time.sleep(2)

client.query(regulated_entity_risk_management_processes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20RiskProcess.csv"))
time.sleep(2)

client.query(regulated_entity_compliance_deadlines.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20ComplianceDeadline.csv"))
time.sleep(2)


client.query(regulated_entity_third_party_service_provider.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20RegulatedEntity%20ThirdPartyProvider.csv"))
time.sleep(2)


client.query(management_role_external_actor.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SEC/SEC%20-%20ManagementRole%20ExternalActor.csv"))
time.sleep(2)

client.query(regulation_regulated_entity)
time.sleep(2)

client.query(regulation_board_committee)
time.sleep(2)

client.query(entity_filing_event)
time.sleep(2)

client.query(entity_management_roles)
time.sleep(2)

client.query(regulation_regulated_entity)
time.sleep(2)

client.query(entity_risk_management)
time.sleep(2)


logger.info("Graph structure loaded successfully.")

query = """
MATCH (n)
OPTIONAL MATCH (n)-[r]->()
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
    with open('sec.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to sec.json")
else:
    logger.error("No data returned from the query.")

client.close()

