#Regional Standard and Regulation node
regional_standard_and_regulation ="""
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    reg.name = "Colorado Privacy Act",
    reg.version = "1.0",
    reg.base_regulation = "Colorado Consumer Protection Act",
    reg.codification = "Colorado Revised Statutes § 6-1-1303 through § 6-1-1313",
    reg.effective_date = date("2023-07-01"),
    reg.enactment_date = date("2021-07-07"),
    reg.enforcement_date = date("2023-07-01"),
    reg.status = "Active",
    reg.description = "The CPA is Colorado's comprehensive consumer privacy law that protects the privacy rights of Colorado residents, establishes controller and processor obligations, and grants enforcement authority to the Colorado Attorney General and District Attorneys.",
    reg.jurisdiction = "Colorado (State)";
"""
#consent node
consent ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:ConsentRecord {consent_id: row.consent_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  ct.type = row.consent_type,
  ct.date = row.consent_date,
  ct.method = row.consent_method,
  ct.status = row.consent_status,
  ct.expiration_date = row.consent_expiration_date,
  ct.last_refresh_date = row.last_refresh_date,
  ct.refresh_required = row.refresh_required,
  ct.specificity_level = row.specificity_level,
  ct.informed_status = row.informed_status,
  ct.freely_given = row.freely_given,
  ct.unambiguous_agreement = row.unambiguous_agreement,
  ct.dark_pattern_used = row.dark_pattern_used,
  ct.withdrawal_date = row.withdrawal_date,
  ct.consent_proof_documentation = row.consent_proof_documentation;
"""
#consumer node
consumer ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cons:Consumer {consumer_id: row.consumer_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  cons.status = row.consumer_status,
  cons.location_state = row.location_state,
  cons.is_minor = row.is_minor,
  cons.age_group = row.age_group,
  cons.status = row.consent_status,
  cons.opt_out_date = row.opt_out_date,
  cons.access_request_count = row.access_request_count,
  cons.deletion_request_count = row.deletion_request_count,
  cons.correction_request_count = row.correction_request_count,
  cons.portability_request_count = row.portability_request_count,
  cons.complaint_filed = row.complaint_filed,
  cons.has_sensitive_data = row.has_sensitive_data,
  cons.last_engagement_date = row.last_engagement_date,
  cons.total_rights_requests = row.total_rights_requests;
"""
#consumer request
consumer_request ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cr:ConsumerRequest {request_id: row.request_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  cr.type = row.request_type,
  cr.date = row.request_date,
  cr.status = row.request_status,
  cr.channel = row.request_channel,
  cr.verification_method = row.consumer_verification_method,
  cr.verified = row.consumer_verified,
  cr.date = row.verification_date,
  cr.response_deadline = row.response_deadline,
  cr.response_date = row.response_date,
  cr.response_status = row.response_status,
  cr.denial_reason = row.denial_reason,
  cr.data_format_requested = row.data_format_requested,
  cr.portable_format_provided = row.portable_format_provided,
  cr.estimated_cost = row.estimated_cost,
  cr.actual_cost_charged = row.actual_cost_charged,
  cr.appeal_submitted = row.appeal_submitted,
  cr.documentation_maintained = row.documentation_maintained,
  cr.response_time_days = row.response_time_days,
  cr.deadline_met = row.deadline_met;
"""
#data_breach node
data_breach ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (db:DataBreachIncident {breach_id: row.breach_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
   db.discovery_date = row.discovery_date,
  db.occurrence_date = row.occurrence_date,
  db.type = row.breach_type,
  db.scope = row.breach_scope,
  db.affected_consumer_count = row.affected_consumer_count,
  db.data_types_compromised = row.data_types_compromised,
  db.sensitive_data_involved = row.sensitive_data_involved,
  db.children_data_involved = row.children_data_involved,
  db.root_cause = row.root_cause,
  db.immediate_actions_taken = row.immediate_actions_taken,
  db.notification_status = row.notification_status,
  db.notification_date = row.notification_date,
  db.ag_notification_date = row.ag_notification_date,
  db.law_enforcement_involved = row.law_enforcement_involved,
  db.remediation_status = row.remediation_status,
  db.compensation_offered = row.compensation_offered,
  db.credit_monitoring_provided = row.credit_monitoring_provided,
  db.total_costs = row.total_costs,
  db.insurance_claim_filed = row.insurance_claim_filed,
  db.litigation_risk = row.litigation_risk,
  db.regulatory_penalty_amount = row.regulatory_penalty_amount,
  db.lessons_learned = row.lessons_learned,
  db.discovery_to_notification_days = row.discovery_to_notification_days,
  db.severity_score = row.severity_score;
"""
#data controller node
data_controller ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataController {controller_id: row.controller_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  dc.organization_name = row.organization_name,
  dc.type = row.controller_type,
  dc.location = row.location,
  dc.industry_sector = row.industry_sector,
  dc.registration_date = row.registration_date,
  dc.compliance_status = row.compliance_status,
  dc.annual_data_volume_consumers = row.annual_data_volume_consumers,
  dc.data_from_sale_revenue = row.data_from_sale_revenue,
  dc.privacy_officer_assigned = row.privacy_officer_assigned,
  dc.privacy_officer_contact = row.privacy_officer_contact,
  dc.privacy_policy_published_date = row.privacy_policy_published_date,
  dc.dpa_count = row.dpa_count,
  dc.subject_to_biometric_rules = row.subject_to_biometric_rules,
  dc.last_audit_date = row.last_audit_date,
  dc.months_since_registration = row.months_since_registration,
  dc.days_since_last_audit = row.days_since_last_audit,
  dc.meets_cpa_thresholds = row.meets_cpa_thresholds,
  dc.cpa_applicability =row.cpa_applicability,
  dc.compliance_risk_score = row.compliance_risk_score;
"""
#data processor node
data_processor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DataProcessor {processor_id: row.processor_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  dp.name = row.processor_name,
  dp.type = row.processor_type,
  dp.location = row.location,
  dp.certifications = row.certifications,
  dp.services = row.data_processing_services,
  dp.subprocessor_count = row.subprocessor_count,
  dp.max_data_records = row.max_data_records,
  dp.security_measures_implemented = row.security_measures_implemented,
  dp.breach_history = row.breach_history,
  dp.count = row.dpa_count,
  dp.audit_frequency = row.audit_frequency,
  dp.liability_insurance = row.liability_insurance,
  dp.gdpr_compliant = row.gdpr_compliant,
  dp.ccpa_compliant = row.ccpa_compliant,
  dp.contact_person = row.contact_person,
  dp.cpa_compliance_ready = row.cpa_compliance_ready,
  dp.risk_score = row.risk_score,
  dp.security_posture = row.security_posture;
"""
#data protection assessment node
data_protection_assessment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpa:DataProtectionAssessment {dpa_id: row.dpa_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  dpa.assessment_date = row.assessment_date,
  dpa.assessment_status = row.assessment_status,
  dpa.processing_activity_assessed = row.processing_activity_assessed,
  dpa.risk_level_overall = row.risk_level_overall,
  dpa.risk_identified = row.heightened_risk_identified,
  dpa.risk_description = row.heightened_risk_description,
  dpa.benefits_identified = row.benefits_identified,
  dpa.risks_identified = row.risks_identified,
  dpa.risk_mitigation_measures = row.risk_mitigation_measures,
  dpa.external_experts_engaged = row.external_experts_engaged,
  dpa.documentation_complete = row.documentation_complete,
  dpa.ag_request_received = row.ag_request_received,
  dpa.submission_date = row.ag_submission_date,
  dpa.remediation_required = row.remediation_required,
  dpa.deadline = row.remediation_deadline,
  dpa.review_date = row.effectiveness_review_date,
  dpa.due_date = row.annual_review_due_date,
  dpa.days_until_remediation = row.days_until_remediation,
  dpa.compliance_status =row.compliance_status,
  dpa.risk_severity = row.risk_severity,
  dpa.completeness =row.assessment_completeness;
"""
#opt-out mechanism node
opt_out_mechanism ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oom:OptOutMechanism {mechanism_id: row.mechanism_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
  oom.type = row.opt_out_type,
  oom.name = row.mechanism_name,
  oom.implementation_date = row.implementation_date,
  oom.method_type = row.method_type,
  oom.placement = row.clear_conspicuous_placement,
  oom.location = row.placement_location,
  oom.single_request_only = row.single_request_only,
  oom.no_account_required = row.no_account_required,
  oom.response_timeline = row.response_timeline,
  oom.technical_standard_compliant = row.technical_standard_compliant,
  oom.verified = row.effectiveness_verified,
  oom.consumer_count_ =row.consumer_count_opted_out,
  oom.request_tracking = row.opt_out_request_tracking,
  oom.retention = row.retention_of_opt_out_data,
  oom.audit_frequency = row.audit_frequency,
  oom.compliance_rate = row.compliance_rate,
  oom.months_since_implementation = row.months_since_implementation,
  oom.compliance_status = row.compliance_status,
  oom.effectiveness_score = row.effectiveness_score,
  oom.adoption_rate = row.adoption_rate,
  oom.enforcement_risk = row.enforcement_risk;
"""
#personal_data node
personal_data ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pd:PersonalDataRecord {data_id: row.data_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  pd.datatype = row.data_type,
  pd.category = row.data_category,
  pd.value_sample = row.data_value_sample,
  pd.is_sensitive = row.is_sensitive,
  pd.sensitivity_level = row.sensitivity_level,
  pd.collection_method = row.collection_method,
  pd.retention_days = row.retention_days,
  pd.is_required_for_service = row.is_required_for_service,
  pd.purpose = row.processing_purpose,
  pd.contains_pii = row.contains_pii,
  pd.encryption_status = row.encryption_status,
  pd.classification_date = row.classification_date,
  pd.months_since_classification = row.months_since_classification,
  pd.retention_compliant = row.retention_compliant,
  pd.security_posture = row.security_posture,
  pd.risk_score = row.risk_score,
  pd.breach_impact = row.breach_impact,
  pd.compliance_concern = row.compliance_concern;
"""
#privacy_notice node
privacy_notice ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PrivacyNotice {notice_id: row.notice_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  pn.type = row.notice_type,
  pn.publication_date = row.publication_date,
  pn.last_updated = row.last_updated,
  pn.distribution_method = row.distribution_method,
  pn.accessibility_level = row.accessibility_level,
  pn.data_collection = row.covers_data_collection,
  pn.data_use = row.covers_data_use,
  pn.data_sharing = row.covers_data_sharing,
  pn.consumer_rights = row.covers_consumer_rights,
  pn.sale_sharing = row.covers_sale_sharing,
  pn.profiling = row.covers_profiling,
  pn.covers_opt_out_mechanism = row.covers_opt_out_mechanism,
  pn.language_count = row.language_count,
  pn.languages_supported = row.languages_supported,
  pn.readability_score = row.readability_score,
  pn.compliance_status = row.compliance_status,
  pn.ag_review_date = row.ag_review_date,
  pn.revisions_required = row.revisions_required,
  pn.months_since_publication = row.months_since_publication,
  pn.months_since_update = row.months_since_update,
  pn.completeness_score = row.completeness_score,
  pn.transparency_level = row.transparency_level,
  pn.enforcement_risk = row.enforcement_risk,
  pn.accessibility = row.languages_supported;
"""
#processing_activity node
processing_activity ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {activity_id: row.activity_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  pa.name = row.activity_name,
  pa.type = row.activity_type,
  pa.purpose = row.processing_purpose,
  pa.legal_basis = row.legal_basis,
  pa.start_date = row.start_date,
  pa.end_date = row.end_date,
  pa.data_retention_period = row.data_retention_period,
  pa.frequency = row.frequency,
  pa.recipients_of_data = row.recipients_of_data,
  pa.cross_border_transfer = row.cross_border_transfer,
  pa.automated_decision_making = row.automated_decision_making,
  pa.profiling_involved = row.profiling_involved,
  pa.dpa_required = row.dpa_required,
  pa.high_risk_flag = row.high_risk_flag,
  pa.impact_assessment_status = row.impact_assessment_status,
  pa.months_active = row.months_active,
  pa.compliance_status = row.compliance_status,
  pa.risk_score = row.risk_score,
  pa.enforcement_priority = row.enforcement_priority,
  pa.consumer_transparency_required =row.consumer_transparency_required,
  pa.available = row.opt_out_available,
  pa.count = row.recipients_count;
"""
#sensitive_data node
sensitive_data ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sd:SensitiveData {data_id: row.sensitive_data_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  sd.type = row.sensitive_type,
  sd.definition = row.definition,
  sd.reference = row.regulation_reference,
  sd.required = row.consent_required,
  sd.parental_consent_required = row.parental_consent_required,
  sd.specific_consent_needed = row.specific_consent_needed,
  sd.retention_limits = row.retention_limits,
  sd.security_requirements = row.security_requirements,
  sd.audit_requirements = row.audit_requirements,
  sd.reporting_requirement = row.reporting_requirement,
  sd.annual_review_required = row.annual_review_required,
  sd.level = row.classification_level,
  sd.enforcement_priority = row.enforcement_priority,
  sd.breach_impact_severity = row.breach_impact_severity,
  sd.regulatory_frameworks = row.regulatory_frameworks,
  sd.compliance_complexity = row.compliance_complexity,
  sd.data_minimization_applicable = row.data_minimization_applicable,
  sd.purpose_limitation_required = row.purpose_limitation_required,
  sd.storage_limitation_required = row.storage_limitation_required,
  sd.integrity_confidentiality_required = row.integrity_confidentiality_required;
"""

#Relationships
#regulation_data_controller relationship
regulation_data_controller ="""
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dc:DataController {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (reg)-[:REGULATION_HAS_DATA_CONTROLLER]->(dc);
"""
#data_controller_consumer relationship
data_controller_consumer ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (consumer:Consumer {consumer_id: row.target_consumer_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_CONTROLS_CONSUMER]->(consumer);
"""
#data_controller_DataProtectionAssessment relationship
data_controller_dataProtectionAssessment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dpa:DataProtectionAssessment {dpa_id: row.target_dpa_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_DATA_PROTECTS_DATA_PROTECTION_ASSESSMENT]->(dpa);
"""
#data_controller_OptOutMechanism relationship
data_controller_optOutMechanism ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (oom:OptOutMechanism {mechanism_id: row.target_mechanism_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_FORCES_OPT_OUT_MECHANISM]->(oom);
"""
#data_controller_consent relationship
data_controller_consent ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ct:ConsentRecord {consent_id: row.target_consent_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_HAS_CONSENT_RECORD]->(ct);
"""

#data_controller_processingActivity relationship
data_controller_processingActivity ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (pa:ProcessingActivity {activity_id: row.target_activity_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_PROCESSING_ACTIVITY]->(pa);
"""
#data_controller_dataBreach relationship
data_controller_dataBreach ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (db:DataBreachIncident {breach_id: row.target_breach_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_BREACH_DATA_BREACH]->(db);
"""
#data_controller_consumerRequest relationship
data_controller_consumerRequest ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cr:ConsumerRequest {request_id: row.target_request_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_RESPONDS_TO_CONSUMER_REQUEST]->(cr);
"""
#data_controller_dataProcessor relationship
data_controller_dataProcessor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (controller:DataController {controller_id: row.source_controller_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dp:DataProcessor {processor_id: row.target_processor_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (controller)-[:DATA_CONTROLLER_PROCESSES_DATA_PROCESSOR]->(dp);
"""
#delete orphan relationships nodes
orphan_nodes_cleanup ="""
MATCH (n)
WHERE NOT (n)--()
DETACH DELETE n;
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

client.query(consent.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Consent_nodes.csv"))
time.sleep(2)

client.query(consumer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Consumer_nodes.csv"))
time.sleep(2)

client.query(consumer_request.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ConsumerRequest_nodes.csv"))
time.sleep(2)

client.query(data_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataBreach_nodes.csv"))
time.sleep(2)

client.query(data_controller.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataController_nodes.csv"))
time.sleep(2)

client.query(data_processor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataProcessor_nodes.csv"))
time.sleep(2)

client.query(data_protection_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataProtectionAssessment_nodes.csv"))
time.sleep(2)

client.query(opt_out_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_OptOutMechanism_nodes.csv"))
time.sleep(2)

client.query(personal_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_PersonalData_nodes.csv"))
time.sleep(2)

client.query(privacy_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_PrivacyNotice_nodes.csv"))
time.sleep(2)

client.query(processing_activity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ProcessingActivity_nodes.csv"))
time.sleep(2)

client.query(sensitive_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_SensitiveData_nodes.csv"))
time.sleep(2)

client.query(regulation_data_controller)
time.sleep(2)

client.query(data_controller_consumer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_COLLECTS_PERSONAL_DATA_relationships.csv"))
time.sleep(2)


client.query(data_controller_dataProtectionAssessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_CONDUCTS_DATA_PROTECTION_ASSESSMENT_relationships.csv"))
time.sleep(2)

client.query(data_controller_optOutMechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ENFORCES_OPT_OUT_relationships.csv"))
time.sleep(2)

client.query(data_controller_consent.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_OBTAINS_CONSENT_relationships.csv"))
time.sleep(2)

client.query(data_controller_processingActivity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_PROCESSES_PERSONAL_DATA_relationships.csv"))
time.sleep(2)

client.query(data_controller_dataBreach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_REPORTS_DATA_BREACH_relationships.csv"))
time.sleep(2)

client.query(data_controller_consumerRequest.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_RESPONDS_TO_REQUEST_relationships.csv"))
time.sleep(2)

client.query(data_controller_dataProcessor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_SHARES_WITH_PROCESSOR_relationships.csv"))
time.sleep(2)

#Orphan
client.query(orphan_nodes_cleanup)
time.sleep(2)


logger.info("Graph structure loaded successfully.")

output_filename = "cpa.json"

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