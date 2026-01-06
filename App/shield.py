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
MERGE (pi:PrivateInformation {info_id: row.info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET 
    pi.name = row.category_name,
    pi.type = row.category_type,
    pi.description = row.description,
    pi.sensitivity_level = row.sensitivity_level,
    pi.requires_combination_with_pi = row.requires_combination_with_pi,
    pi.examples = row.examples,
    pi.protection_level_required = row.protection_level_required,
    pi.breach_notification_required = row.breach_notification_required,
    pi.retention_guidance = row.retention_guidance;
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
MATCH (pi:PrivateInformation {info_id: row.target_private_information_id})
MERGE (dc)-[:DATA_CONTROLLER_OWNS_LICENSES_PRIVATE_INFORMATION]->(pi);
"""

#security_program_trainingemployee
security_program_training_employee ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (spg:SecurityProgram {program_id: row.source_program_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (et:EmployeeTraining {training_id: row.target_training_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (spg)-[:SECURITY_PROGRAM_PROVIDES_TRAINING_TO_EMPLOYEE]->(et);
"""
#data_breach_government_agency
data_breach_government_agency ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (br:DataBreach {breach_id: row.source_breach_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (agency:GovernmentAgency {agency_name: row.agency_name, regional_standard_regulation_id: 'NY SHIELD 1.0'})
CREATE (breach)-[r:DATA_BREACH_REPORTS_TO_GOVERNMENT_AGENCY {
    report_date: row.report_date,
    report_method: row.report_method,
    report_number: row.report_number,
    confirmation_received: row.confirmation_received,
    confirmation_date: row.confirmation_date
}]->(agency);
"""
#datacontroller_compilance_assessment
datacontroller_compliance_assessment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (dc:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (ca:ComplianceAssessment {assessment_id: row.target_assessment_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (dc)-[:DATA_CONTROLLER_UNDERGOES_COMPLIANCE_ASSESSMENT]->(ca);
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

client.query(data_controller.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataBreach_nodes.csv"))
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

client.query(data_breach_government_agency.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_REPORTS_TO_GOVERNMENT_relationships.csv"))
time.sleep(2)

client.query(datacontroller_compliance_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SHIELD/SHIELD_UNDERGOES_COMPLIANCE_ASSESSMENT_relationships.csv"))
time.sleep(2)



logger.info("Graph structure loaded successfully.")

output_filename = "shield.json"

res = client.query("""
    MATCH path = (:RegionalStandardAndRegulation)-[*]->()
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
      links: [r IN uniqueRels | r {
        .*,
        id: elementId(r),     
        type: type(r),         
        source: elementId(startNode(r)), 
        target: elementId(endNode(r)) 
      }]
    } AS graph_data
""")

if isinstance(res, str):
    logger.error(f"✗ Export query failed: {res}")
    client.close()
    sys.exit(1)

if not res or len(res) == 0:
    logger.warning(" No data returned from export query")
    client.close()
    sys.exit(1)

graph_data = res[0].get('graph_data', res[0])

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, default=str, ensure_ascii=False)

node_count = len(graph_data.get('nodes', []))
link_count = len(graph_data.get('links', []))

logger.info(f" Exported {node_count} nodes and {link_count} relationships")
logger.info(f" Graph data saved to: {output_filename}") 

client.close()








