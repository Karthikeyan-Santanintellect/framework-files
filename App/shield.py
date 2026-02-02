#Regional Regulation 
regional_standard_and_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    reg.name = "New York Stop Hacks and Improve Electronic Data Security (SHIELD) Act",
    reg.version = "1.0",
    reg.base_regulation = "New York Information Security Breach and Notification Act",
    reg.codification = "New York General Business Law Article 39-F §§ 899-aa and 899-bb",
    reg.effective_date = date("2020-03-21"),
    reg.enactment_date = date("2019-07-25"),
    reg.enforcement_date = date("2020-03-21"),
    reg.status = "Active",
    reg.description = "The SHIELD Act is New York's data security and breach notification law that amends the state's Information Security Breach and Notification Act, expands the scope of 'private information', and requires any person or business that owns or licenses private information of New York residents to implement reasonable administrative, technical, and physical safeguards, enforced by the New York Attorney General.",
    reg.jurisdiction = "New York (State)";
"""

# Sections 
sections = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {section_id: row.section_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    sec.citation = row.official_citation,
    sec.heading = row.heading,
    sec.text = row.text;
"""
#Administrative Safeguards
administrative_safeguards = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sf:AdministrativeSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    sf.name = row.safeguard_name,
    sf.category = row.safeguard_category,
    sf.description = row.description,
    sf.status = row.implementation_status,
    sf.date = row.implementation_date,
    sf.responsible_person = row.responsible_person,
    sf.frequency_of_review = row.frequency_of_review,
    sf.last_review_date = row.last_review_date,
    sf.score = row.effectiveness_score,
    sf.compliance_with_shield = row.compliance_with_shield;
"""
#Compliance Assessment
compliance_assessment = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ass:ComplianceAssessment {assessment_id: row.assessment_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    ass.type = row.assessment_type,
    ass.date = row.assessment_date,
    ass.name = row.assessor_name,
    ass.organization = row.assessor_organization,
    ass.scope = row.scope,
    ass.compliant_areas = row.compliant_areas,
    ass.non_compliant_areas = row.non_compliant_areas,
    ass.gaps_identified_count = row.gaps_identified_count,
    ass.critical_gaps_count = row.critical_gaps_count,
    ass.remediation_plan_developed = row.remediation_plan_developed,
    ass.remediation_timeline = row.remediation_timeline,
    ass.reassessment_date = row.reassessment_date,
    ass.recommendation_count = row.recommendation_count,
    ass.overall_compliance_rating = row.overall_compliance_rating,
    ass.rating = row.risk_rating,
    ass.shield_compliance_result = row.shield_compliance_result;
"""
#data_breach
data_breach ="""
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (br:DataBreach {breach_id: row.breach_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    br.discovery_date = row.discovery_date,
    br.determination_date = row.breach_determination_date,
    br.deadline = row.notification_deadline,
    br.actual_notification_date = row.actual_notification_date,
    br.description = row.breach_description,
    br.vector = row.breach_vector,
    br.access = row.unauthorized_access,
    br.acquisition = row.unauthorized_acquisition,
    br.residents_count = row.affected_residents_count,
    br.individuals_count = row.affected_individuals_count,
    br.investigation_status = row.investigation_status,
    br.government_notification_status = row.government_notification_status,
    br.consumer_reporting_agency_notification = row.consumer_reporting_agency_notification,
    br.estimated_damages = row.estimated_damages,
    br.recovery_status = row.breach_recovery_status,
    br.root_cause_identified = row.root_cause_identified,
    br.remediation_completed = row.remediation_completed;
"""
#data_controller
data_controller = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataController {controller_id: row.controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    dc.name = row.entity_name,
    dc.type = row.entity_type,
    dc.business_size = row.business_size,
    dc.employee_count = row.employee_count,
    dc.annual_revenue = row.annual_revenue,
    dc.total_assets = row.total_assets,
    dc.nysag_regulated = row.nysag_regulated,
    dc.nysdfs_regulated = row.nysdfs_regulated,
    dc.hipaa_compliant = row.hipaa_compliant,
    dc.glba_compliant = row.glba_compliant,
    dc.state_jurisdiction = row.state_jurisdiction,
    dc.compliance_status = row.shield_compliance_status,
    dc.last_security_audit_date = row.last_security_audit_date,
    dc.security_program_coordinator = row.security_program_coordinator,
    dc.data_classification_implemented = row.data_classification_implemented,
    dc.contact_email = row.contact_email,
    dc.contact_phone = row.contact_phone;
"""
#Employee Training
employee_training = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EmployeeTraining {training_id: row.training_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    et.name = row.training_name,
    et.type = row.training_type,
    et.target_audience = row.target_audience,
    et.delivery_method = row.delivery_method,
    et.required_frequency = row.required_frequency,
    et.duration_hours = row.duration_hours,
    et.completion_tracking = row.completion_tracking,
    et.completion_rate = row.completion_rate,
    et.last_delivery_date = row.last_delivery_date,
    et.next_scheduled_date = row.next_scheduled_date,
    et.certification_earned = row.certification_earned,
    et.test_requirement = row.test_requirement,
    et.average_test_score = row.average_test_score,
    et.training_materials_available = row.training_materials_available,
    et.qualified = row.trainer_qualified,
    et.compliance_with_shield = row.compliance_with_shield,
    et.effectiveness_feedback_score = row.effectiveness_feedback_score;
"""
#Incident Response
incident_response = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:IncidentResponse {response_id: row.response_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    ir.breach_id = row.breach_associated_id,
    ir.response_step = row.response_step,
    ir.name = row.step_name,
    ir.type = row.step_type,
    ir.start_date = row.start_date,
    ir.completion_date = row.completion_date,
    ir.responsible_person = row.responsible_person,
    ir.responsible_team = row.responsible_team,
    ir.actions_taken = row.actions_taken,
    ir.status = row.status,
    ir.time_to_complete_hours = row.time_to_complete_hours,
    ir.notification_sent = row.notification_sent,
    ir.notification_date = row.notification_date;
"""
#Notification process
notification_process = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (np:NotificationProcess {notification_id: row.notification_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    np.breach_id = row.breach_associated_id,
    np.type = row.notification_type,
    np.planned_date = row.planned_date,
    np.actual_date = row.actual_date,
    np.deadline = row.deadline,
    np.on_schedule = row.on_schedule,
    np.days_to_notify = row.days_to_notify,
    np.method = row.method,
    np.recipients_count = row.recipients_count,
    np.notification_content_includes = row.notification_content_includes,
    np.credit_monitoring_offered = row.credit_monitoring_offered,
    np.government_agencies_notified = row.government_agencies_notified,
    np.regulatory_violation_risk = row.regulatory_violation_risk,
    np.penalty_exposure = row.penalty_exposure;
"""
#NY resident
ny_resident = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (nr:NYResident {resident_id: row.resident_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    nr.state = row.residence_state,
    nr.status = row.data_subject_status,
    nr.data_collection_date = row.data_collection_date,
    nr.last_interaction_date = row.last_interaction_date,
    nr.notification_received = row.notification_received,
    nr.count = row.affected_by_breach_count,
    nr.has_exercised_rights = row.has_exercised_rights,
    nr.consent_status = row.consent_status,
    nr.data_retention_status = row.data_retention_status;
"""
#security_policy
security_policy = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:SecurityPolicy {policy_id: row.policy_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    sp.name = row.policy_name,
    sp.type = row.policy_type,
    sp.description = row.description,
    sp.creation_date = row.creation_date,
    sp.last_revision_date = row.last_revision_date,
    sp.next_review_date = row.next_review_date,
    sp.version = row.version_number,
    sp.key_procedures = row.key_procedures,
    sp.acknowledgment_required = row.acknowledgment_required,
    sp.training_required = row.training_required,
    sp.regulatory_mandate = row.regulatory_mandate,
    sp.rating = row.effectiveness_rating,
    sp.accessible_to_all_staff = row.accessible_to_all_staff;
"""
#security_program
security_program = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (spg:SecurityProgram {program_id: row.program_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    spg.name = row.program_name,
    spg.establishment_date = row.establishment_date,
    spg.last_update_date = row.last_update_date,
    spg.coordinator = row.program_coordinator,
    spg.risk_assessment_frequency = row.risk_assessment_frequency,
    spg.last_risk_assessment_date = row.last_risk_assessment_date,
    spg.training_frequency = row.training_frequency,
    spg.employee_training_completion_rate = row.employee_training_completion_rate,
    spg.third_party_assessment_conducted = row.third_party_assessment_conducted,
    spg.documentation_complete = row.documentation_complete,
    spg.disaster_recovery_plan_exists = row.disaster_recovery_plan_exists,
    spg.incident_response_plan_exists = row.incident_response_plan_exists,
    spg.rating = row.program_effectiveness_rating;
"""

#security_provider
security_provider = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (spv:SecurityProvider {provider_id: row.provider_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    spv.name = row.provider_name,
    spv.type = row.provider_type,
    spv.services_provided = row.services_provided,
    spv.engagement_date = row.engagement_date,
    spv.contract_end_date = row.contract_end_date,
    spv.has_security_agreement = row.has_security_agreement,
    spv.data_security_clauses = row.agreement_includes_data_security_clauses,
    spv.breach_notification = row.agreement_includes_breach_notification,
    spv.audit_rights = row.agreement_includes_audit_rights,
    spv.data_deletion = row.agreement_includes_data_deletion,
    spv.access_level = row.access_level,
    spv.security_assessment_completed = row.security_assessment_completed,
    spv.security_assessment_date = row.security_assessment_date,
    spv.assessment_result = row.assessment_result,
    spv.compliance_certifications = row.compliance_certifications,
    spv.incident_history_count = row.incident_history_count,
    spv.last_incident_date = row.last_incident_date;   
"""
#technical_safeguards
technical_safeguards = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ts:TechnicalSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    ts.name = row.safeguard_name,
    ts.type = row.control_type,
    ts.description = row.description,
    ts.implementation_status = row.implementation_status,
    ts.implementation_date = row.implementation_date,
    ts.encryption_algorithm = row.encryption_algorithm,
    ts.encryption_scope = row.encryption_scope,
    ts.mfa_enabled = row.mfa_enabled,
    ts.mfa_coverage_percentage = row.mfa_coverage_percentage,
    ts.testing_frequency = row.testing_frequency,
    ts.last_testing_date = row.last_testing_date,
    ts.vulnerabilities_found_count = row.vulnerabilities_found_count,
    ts.critical_vulnerabilities_count = row.critical_vulnerabilities_count,
    ts.compliance_with_shield = row.compliance_with_shield;
"""
#private_information
private_information = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pvi:PrivateInformation {info_id: row.info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    pvi.name = row.category_name,
    pvi.type = row.category_type,
    pvi.description = row.description,
    pvi.sensitivity_level = row.sensitivity_level,
    pvi.requires_combination_with_pi = row.requires_combination_with_pi,
    pvi.examples = row.examples,
    pvi.protection_level_required = row.protection_level_required,
    pvi.breach_notification_required = row.breach_notification_required,
    pvi.retention_guidance = row.retention_guidance;
"""
#risk_assessment
risk_assesment ="""
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ra:RiskAssessment {assessment_id: row.assessment_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    ra.name = row.assessment_name,
    ra.type = row.assessment_type,
    ra.assessment_date = row.assessment_date,
    ra.completion_date = row.completion_date,
    ra.assessor_name = row.assessor_name,
    ra.scope = row.assessment_scope,
    ra.internal_risks_identified = row.internal_risks_identified,
    ra.external_risks_identified = row.external_risks_identified,
    ra.risk_level = row.risk_level,
    ra.risk_mitigation_plan_exists = row.risk_mitigation_plan_exists,
    ra.mitigation_deadline = row.mitigation_deadline,
    ra.last_review_date = row.last_review_date,
    ra.next_review_date = row.next_review_date;
"""
# Physical Safeguards
physical_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ps:PhysicalSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    ps.name = row.safeguard_name,
    ps.description = row.description,
    ps.implementation_status = row.implementation_status,
    ps.last_inspection_date = row.last_inspection_date,
    ps.secure_disposal_method = row.secure_disposal_method,
    ps.compliance_with_shield = row.compliance_with_shield;
"""
# Data Element Combinations
data_element_combination = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'DEC'
MERGE (dec:DataElementCombination {combination_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    dec.type = row.type,
    dec.elements = row.elements_list,
    dec.requires_name = row.requires_personal_name_boolean,
    dec.description = row.description;
"""
# Publicly Available Information
public_info_exclusion = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'PAI'
MERGE (pai:PubliclyAvailableInformation {exclusion_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    pai.name = row.type,
    pai.description = row.description;
"""
# Personal Information (Parent Node)
personal_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'PI'
MERGE (pi:PersonalInformation {type_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    pi.name = row.type,
    pi.description = row.description;
"""
# Regulatory Bodies
regulatory_bodies = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.authority_id <> 'SB_DEF_001'
MERGE (rb:RegulatoryBody {authority_id: row.authority_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    rb.name = row.name,
    rb.role = row.role,
    rb.jurisdiction = row.jurisdiction,
    rb.exclusive_enforcement = row.exclusive_enforcement;
"""
# Small Business Definition
small_business_def = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sb:SmallBusinessDefinition {definition_id: row.authority_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    sb.name = row.name,
    sb.description = row.description; 
"""
# Civil Penalties
civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cp:CivilPenalty {penalty_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    cp.name = row.name,
    cp.violation_type = row.violation_type,
    cp.amount_per_violation = row.amount,
    cp.cap_amount = row.cap_amount,
    cp.description = row.description;
"""
# Statute of Limitations
statute_of_limitations = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rule_id STARTS WITH 'SOL'
MERGE (sol:StatuteOfLimitations {rule_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    sol.name = row.name,
    sol.description = row.description;
"""
# Inadvertent Disclosure
inadvertent_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (id:InadvertentDisclosure {exception_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    id.name = row.name,
    id.description = row.description;
"""

# Unauthorized Access
unauthorized_access = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ua:UnauthorizedAccess {definition_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    ua.name = row.name,
    ua.description = row.description;
"""
# Compliant Regulated Entity 
compliant_regulated_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cre:CompliantRegulatedEntity {entity_id: row.entity_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    cre.regulation_type = row.regulation_type,
    cre.deemed_compliant_status = row.deemed_compliant_status,
    cre.validation_date = row.validation_date;
"""


#Relationships
#regulation_data_controller
regulation_data_controller = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_GOVERNS_DATA_CONTROLLER]->(dc);
"""
#data_controller_data_breach
data_controller_data_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (br:DataBreach {breach_id: row.target_breach_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_DETECTS_DATA_BREACH]->(br);
"""
#private_inforamtion_private_information
private_inforamtion_private_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (SourceInfo:PrivateInformation {info_id: row.source_info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (TargetInfo:PrivateInformation {info_id:row.target_info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (SourceInfo)-[:PRIVATE_INFORMATION_COMBINES_WITH_DATA_ELEMENT]->(TargetInfo);
"""

#security_program_administrative_safeguard
security_program_administrative_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (spg:SecurityProgram {program_id: row.source_program_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (sf:AdministrativeSafeguard {safeguard_id: row.target_safeguard_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (spg)-[:SECURITY_PROGRAM_APPLIES_SAFEGUARDS_TO_ADMINISTRATIVE_SAFEGUARD]->(sf);
"""
#security_program_risk_assessment
security_program_risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (spg:SecurityProgram {program_id: row.source_program_id})
MATCH (ra:RiskAssessment {assessment_id: row.target_assessment_id})
MERGE (spg)-[:SECURITY_PROGRAM_CONDUCTS_RISK_ASSESSMENT]->(ra);
"""
#datacontroller_securitypolicy
datacontroller_securitypolicy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (sp:SecurityPolicy {policy_id: row.target_policy_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_ENFORCES_SECURITY_POLICY]->(sp);
"""
#datacontroller_nyresident
datacontroller_nyresident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (nr:NYResident {resident_id: row.target_resident_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_HOLDS_PERSONAL_DATA_OF_NY_RESIDENT]->(nr);
"""
#datacontroller_security_program
datacontroller_security_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (spg:SecurityProgram {program_id: row.target_program_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_IMPLEMENTS_SECURITY_PROGRAM]->(spg);
"""
#datacontroller_service provider
datacontroller_service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (spv:SecurityProvider {provider_id: row.target_provider_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_IMPLEMENTS_SECURITY_PROVIDER]->(spv);
"""
#databreach_nyresident
databreach_nyresident="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (br:DataBreach {breach_id: row.source_breach_id})
MATCH (nr:NYResident {resident_id: row.target_resident_id})
MERGE (br)-[:DATA_BREACH_NOTIFIES_AFFECTED_INDIVIDUAL_NY_RESIDENT]->(nr);
"""
#datacontroller_privateinformation
datacontroller_private_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id})
MATCH (pvi:PrivateInformation {info_id: row.target_private_information_id})
MERGE (dc)-[:DATA_CONTROLLER_OWNS_LICENSES_PRIVATE_INFORMATION]->(pvi);
"""

#security_program_trainingemployee
security_program_training_employee ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (spg:SecurityProgram {program_id: row.source_program_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (et:EmployeeTraining {training_id: row.target_training_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (spg)-[:SECURITY_PROGRAM_PROVIDES_TRAINING_TO_EMPLOYEE]->(et);
"""

#datacontroller_compilance_assessment
datacontroller_compliance_assessment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (ca:ComplianceAssessment {assessment_id: row.target_assessment_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_UNDERGOES_COMPLIANCE_ASSESSMENT]->(ca);
"""

# Link Security Program to Physical Safeguards
security_program_physical_safeguards = """
MATCH (spg:SecurityProgram {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (ps:PhysicalSafeguard {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (spg)-[:SECURITY_PROGRAM_APPLIES_SAFEGUARDS_PHYSICAL_SAFEGUARD]->(ps);
"""
# Link Data Controller to Small Business Definition

datacontroller_small_business_definition = """
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (sb:SmallBusinessDefinition {definition_id: 'SB_DEF_001'})
MERGE (dc)-[:DATA_CONTROLLER_QUALIFIES_AS_SMALL_BUSINESS]->(sb);
"""
# Link Data Controller to Compliant Regulated Entity
datacontroller_compliant_regulated_entity = """
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (cre:CompliantRegulatedEntity {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_HAS_SAFE_HARBOR_STATUS]->(cre);
"""
# Link Attorney General to Civil Penalties
regulatory_bodies_civil_penalties = """
MATCH (rb:RegulatoryBody {authority_id: 'NY_AG'})
MATCH (cp:CivilPenalty {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (rb)-[:ATTORNEY_GENERAL_ENFORCES_PENALTY]->(cp);
"""

# Link Data Breach to Specific Regulatory Bodies (Notification Duty)
regulatory_bodies_data_breach = """
MATCH (br:DataBreach {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (rb:RegulatoryBody {regional_standard_regulation_id: 'NY SHIELD 1.0'})
WHERE rb.authority_id IN ['NY_AG', 'NY_DOS', 'NY_SP', 'CRA_001']
MERGE (br)-[:DATA_BREACH_MUST_NOTIFY_AUTHORITY]->(rb);
"""
# Link Private Information to Data Element Combinations (Triggers)
private_information_data_element_combination = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (dec:DataElementCombination {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pi)-[:PRIVACY_INFORMATION_DEFINED_BY_COMBINATION]->(dec);
"""

#Link Private Information to Parent Category (Personal Information)
personal_information_private_information = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (parent:PersonalInformation {type_id: 'PI-PARENT-001', regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pvi)-[:PRIVACY_INFORMATION_SUBTYPE_OF_PERSONAL_INFORMATION]->(parent);
"""

# Link Private Information to Publicly Available Information (Exclusion)
private_information_publicly_available_information = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (pai:PubliclyAvailableInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pvi)-[:PRIVACY_INFORMATION_EXCLUDES_DEFINITION]->(pai);
"""

# Link Data Breach to Unauthorized Access Definition
data_breach_unauthorized_access = """
MATCH (br:DataBreach {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (ua:UnauthorizedAccess {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (br)-[:DATA_BREACH_CLASSIFIED_AS_UNAUTHORIZED_ACCESS]->(ua);
"""

orphan_small_business = """
MATCH (orphan:SmallBusinessDefinition) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_statute_limitations = """
MATCH (orphan:StatuteOfLimitations) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_inadvertent_disclosure = """
MATCH (orphan:InadvertentDisclosure) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_technical_safeguard = """
MATCH (orphan:TechnicalSafeguard) WHERE NOT EXISTS ((orphan)--())
MATCH (spg:SecurityProgram {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (spg)-[:SECURITY_PROGRAM_APPLIES_SAFEGUARDS_TO_TECHNICAL]->(orphan);
"""
orphan_security_policy = """
MATCH (orphan:SecurityPolicy) WHERE NOT EXISTS ((orphan)--())
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_ENFORCES_SECURITY_POLICY]->(orphan);
"""
orphan_incident_response = """
MATCH (orphan:IncidentResponse) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_MANDATES_RESPONSE_PROCESS]->(orphan);
"""

orphan_notification_process = """
MATCH (orphan:NotificationProcess) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_MANDATES_RESPONSE_PROCESS]->(orphan);
"""
orphan_ny_resident = """
MATCH (orphan:NYResident) WHERE NOT EXISTS ((orphan)--())
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_HOLDS_PERSONAL_DATA_OF_NY_RESIDENT]->(orphan);
"""
# Data Controller -> Data Element Combination
datacontroller_data_element = """
MATCH (dc:DataController {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (dec:DataElementCombination {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_OWNS_LICENSES_DATA_ELEMENT]->(dec);
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



client.query(regional_standard_and_regulation)
time.sleep(2)

client.query(administrative_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_AdministrativeSafeguard_nodes.csv"))
time.sleep(2)

client.query(compliance_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_ComplianceAssessment_nodes.csv"))
time.sleep(2)

client.query(data_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_DataBreach_nodes.csv"))
time.sleep(2)

client.query(data_controller.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_DataController_nodes.csv"))
time.sleep(2)

client.query(employee_training.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_EmployeeTraining_nodes.csv"))
time.sleep(2)

client.query(incident_response.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_IncidentResponse_nodes.csv"))
time.sleep(2)

client.query(notification_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_NotificationProcess_nodes.csv"))
time.sleep(2)

client.query(ny_resident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_NYResident_nodes.csv"))
time.sleep(2)

client.query(security_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_SecurityPolicy_nodes.csv"))
time.sleep(2)

client.query(security_program.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_SecurityProgram_nodes.csv"))
time.sleep(2)

client.query(security_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_ServiceProvider_nodes.csv"))
time.sleep(2)

client.query(technical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_TechnicalSafeguard_nodes.csv"))
time.sleep(2)

client.query(private_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_PrivateInformation_nodes.csv"))
time.sleep(2)

client.query(risk_assesment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_RiskAssessment_nodes.csv"))
time.sleep(2)

client.query(physical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Physical%20Safeguard.csv"))
time.sleep(2)

client.query(data_element_combination.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(public_info_exclusion.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(personal_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(regulatory_bodies.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Entities.csv"))
time.sleep(2)

client.query(small_business_def.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Entities.csv"))
time.sleep(2)

client.query(civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(statute_of_limitations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(inadvertent_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(unauthorized_access.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(compliant_regulated_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD%20-%20Safe%20Harbor.csv"))
time.sleep(2)
                                              






#Relationships
client.query(regulation_data_controller)
time.sleep(2)

client.query(data_controller_data_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_DETECTS_DATA_BREACH_relationships.csv"))
time.sleep(2)

client.query(private_inforamtion_private_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_COMBINES_WITH_DATA_ELEMENT_relationships.csv"))
time.sleep(2)

client.query(security_program_administrative_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_AppliesSafeguards_Updated.csv"))
time.sleep(2)

client.query(security_program_risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_CONDUCTS_RISK_ASSESSMENT.csv"))
time.sleep(2)

client.query(datacontroller_securitypolicy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_ENFORCES_POLICY_relationships.csv"))
time.sleep(2)

client.query(datacontroller_nyresident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_HOLDS_PERSONAL_DATA_OF_relationships.csv"))
time.sleep(2)

client.query(datacontroller_security_program.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_IMPLEMENTS_SECURITY_PROGRAM_relationships.csv"))
time.sleep(2)

client.query(datacontroller_service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_MANAGES_THIRD_PARTY_relationships.csv"))
time.sleep(2)

client.query(databreach_nyresident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_NOTIFIES_AFFECTED_INDIVIDUAL_relationships.csv"))
time.sleep(2)

client.query(datacontroller_private_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_OwnsLicenses_Corrected.csv"))
time.sleep(2)

client.query(security_program_training_employee.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_PROVIDES_TRAINING_TO_relationships.csv"))
time.sleep(2)

client.query(datacontroller_compliance_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_UNDERGOES_COMPLIANCE_ASSESSMENT_relationships.csv"))
time.sleep(2)

client.query(security_program_physical_safeguards)
time.sleep(2)

client.query(datacontroller_small_business_definition)
time.sleep(2)

client.query(datacontroller_compliant_regulated_entity)
time.sleep(2)

client.query(regulatory_bodies_civil_penalties)
time.sleep(2)

client.query(regulatory_bodies_data_breach)
time.sleep(2)

client.query(private_information_data_element_combination)
time.sleep(2)

client.query(personal_information_private_information)
time.sleep(2)

client.query(private_information_publicly_available_information)
time.sleep(2)

client.query(data_breach_unauthorized_access)
time.sleep(2)   

client.query(orphan_small_business)
time.sleep(2)

client.query(orphan_statute_limitations)
time.sleep(2)

client.query(orphan_inadvertent_disclosure)
time.sleep(2)

client.query(orphan_technical_safeguard)
time.sleep(2)

client.query(orphan_security_policy)
time.sleep(2)

client.query(orphan_incident_response)
time.sleep(2)

client.query(orphan_notification_process)
time.sleep(2)

client.query(orphan_ny_resident)
time.sleep(2)

client.query(datacontroller_data_element)
time.sleep(2)




logger.info("Graph structure loaded successfully.")

cleanup_query = """
MATCH (n)
WHERE size(labels(n)) = 0
DETACH DELETE n
"""
cleanup_query = """
MATCH (n)
WHERE elementId(n) = '4:5ad33362-7a76-4561-94af-1b68b08b0d51:9321'
DETACH DELETE n
"""
client.query(cleanup_query)

logger.info("Cleaning up ghost nodes (nodes with no labels)...")
client.query(cleanup_query)
logger.info("✓ Ghost nodes removed from database.")

query = """
MATCH (n)
WHERE size(labels(n)) > 0
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
    with open('shield.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to shileld.json")
else:
    logger.error("No data returned from the query.")

client.close()








