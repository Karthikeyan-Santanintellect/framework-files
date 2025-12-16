#Regulation
regulation = """
MERGE (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX'})
ON CREATE SET
    reg.name = "Trusted Information Security Assessment Exchange",
    reg.version = "VDA ISA 6 / TISAX",
    reg.status = "Active",
    reg.jurisdiction = "Automotive industry, primarily Europe",
    reg.effective_date = date("2024-04-01"),        
    reg.enactment_date = date("2017-01-01"),   
    reg.description = "Information security assessment and exchange scheme for the automotive industry, based on ISO/IEC 27001 and sector-specific requirements. Managed by the ENX Association and using the VDA Information Security Assessment (ISA) catalogue, it provides graded assessment levels and TISAX labels so manufacturers, suppliers, and service providers can demonstrate and share their information security maturity in a standardized way.";
"""
#organization 
organization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (org:Organization {industry_standard_regulation_id: 'TISAX', organization_id: row.organization_id})
ON CREATE SET
  org.name                      = row.name,
  org.type                      = row.type,
  org.location                  = row.location,
  org.industry_sector           = row.industry_sector,
  org.registration_date         = date(row.registration_date),
  org.assessment_status         = row.assessment_status,
  org.highest_al_current        = toInteger(row.highest_al_current),
  org.last_assessment_date      = date(row.last_assessment_date),
  org.certification_validity_end = row.certification_validity_end,
  org.contact_email             = row.contact_email,
  org.contact_phone             = row.contact_phone;
"""
#assessment
assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ass:Assessment {industry_standard_regulation_id: 'TISAX', assessment_id: row.assessment_id})
ON CREATE SET
  ass.start_date             = date(row.start_date),
  ass.completion_date        = date(row.completion_date),
  ass.planned_duration_days  = row.planned_duration_days,
  ass.assessment_level       = row.assessment_level,
  ass.status                 = row.status,
  ass.scope_description      = row.scope_description,
  ass.scope_type             = row.scope_type,
  ass.assessment_type        = row.assessment_type,
  ass.methodology            = row.methodology,
  ass.on_site_required       = row.on_site_required,
  ass.documentation_reviewed = row.documentation_reviewed;
"""
#assessment_level
assessment_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (al:AssessmentLevel {industry_standard_regulation_id: 'TISAX', assessment_level_id: row.level_id})
ON CREATE SET
  al.name                        = row.name,
  al.description                 = row.description,
  al.protection_level            = row.protection_level,
  al.data_protection_needs       = row.data_protection_needs,
  al.isa_catalogue_required      = row.isa_catalogue_required,
  al.external_audit_required     = row.external_audit_required,
  al.self_assessment_allowed     = row.self_assessment_allowed,
  al.requires_on_site_visit      = row.requires_on_site_visit,
  al.typical_scope_size          = row.typical_scope_size,
  al.costs_implications          = row.costs_implications,
  al.certification_validity_years = row.certification_validity_years;
"""
#Assessment_objective
assessment_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ao:AssessmentObjective {industry_standard_regulation_id: 'TISAX', assessment_objective_id: row.objective_id})
ON CREATE SET
  ao.name                   = row.name,
  ao.category               = row.category,
  ao.description            = row.description,
  ao.isa_catalogue_ref      = row.isa_catalogue_ref,
  ao.control_questions_count = row.control_questions_count,
  ao.criticality_level      = row.criticality_level,
  ao.risk_area              = row.risk_area,
  ao.requirements_version   = row.requirements_version,
  ao.related_standards      = row.related_standards,
  ao.evidence_types_required = row.evidence_types_required,
  ao.typical_effort_hours   = row.typical_effort_hours;
"""
#audit_provider
audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AuditProvider {industry_standard_regulation_id: 'TISAX', audit_provider_id: row.provider_id})
ON CREATE SET
  ap.provider_name                = row.provider_name,
  ap.registration_number          = row.registration_number,
  ap.accreditation_status         = row.accreditation_status,
  ap.accreditation_date           = date(row.accreditation_date),
  ap.accreditation_expiry         = date(row.accreditation_expiry),
  ap.supported_assessment_levels  = row.supported_assessment_levels,
  ap.geographic_coverage          = row.geographic_coverage,
  ap.industry_specialization      = row.industry_specialization,
  ap.max_concurrent_assessments   = row.max_concurrent_assessments,
  ap.average_audit_duration_days  = row.average_audit_duration_days,
  ap.certification_count          = row.certification_count,
  ap.quality_rating               = row.quality_rating,
  ap.contact_person               = row.contact_person,
  ap.website                      = row.website;
"""
#ISA_catalogue
isa_catalogue = """ 
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ic:ISACatalogue {industry_standard_regulation_id: 'TISAX', isa_catalogue_id: row.catalogue_id})
ON CREATE SET
  ic.name                    = row.name,
  ic.type                    = row.type,
  ic.version                 = row.version,
  ic.release_date            = date(row.release_date),
  ic.last_updated            = date(row.last_updated),
  ic.total_control_questions = row.total_control_questions,
  ic.requirement_categories  = row.requirement_categories,
  ic.scope_coverage          = row.scope_coverage,
  ic.maturity_model_levels   = row.maturity_model_levels,
  ic.alignment_with_standards = row.alignment_with_standards,
  ic.geographic_applicability = row.geographic_applicability,
  ic.language_support        = row.language_support,
  ic.documentation_url       = row.documentation_url;
"""
#control_question
control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cq:ControlQuestion {industry_standard_regulation_id: 'TISAX', control_question_id: row.question_id})
ON CREATE SET
  cq.sequence_number         = row.sequence_number,
  cq.question_text           = row.question_text,
  cq.question_category       = row.question_category,
  cq.criticality             = row.criticality,
  cq.applies_to_al1          = row.applies_to_al1,
  cq.applies_to_al2          = row.applies_to_al2,
  cq.applies_to_al3          = row.applies_to_al3,
  cq.expected_evidence_types = row.expected_evidence_types,
  cq.maturity_levels         = row.maturity_levels,
  cq.typical_response_options = row.typical_response_options,
  cq.guidance_url            = row.guidance_url,
  cq.last_revision_date      = row.last_revision_date,
  cq.related_control_ids     = row.related_control_ids;
"""
#Protection Object
protection_object = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:ProtectionObject {industry_standard_regulation_id: 'TISAX', protection_object_id: row.object_id})
ON CREATE SET
  po.name                       = row.name,
  po.type                       = row.type,
  po.classification             = row.classification,
  po.protection_level           = row.protection_level,
  po.is_sensitive               = row.is_sensitive,
  po.data_categories_contained  = row.data_categories_contained,
  po.owner_department           = row.owner_department,
  po.criticality_to_business    = row.criticality_to_business,
  po.location                   = row.location,
  po.last_assessment_date       = date(row.last_assessment_date),
  po.protection_controls_implemented = row.protection_controls_implemented,
  po.remaining_risk             = row.remaining_risk;
"""
#Participant
participant = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:Participant {industry_standard_regulation_id: 'TISAX', participant_id: row.participant_id})
ON CREATE SET
  pa.organization_name               = row.organization_name,
  pa.participant_type                = row.participant_type,
  pa.joining_date                    = date(row.joining_date),
  pa.assessment_result_access_level  = row.assessment_result_access_level,
  pa.data_sharing_status             = row.data_sharing_status,
  pa.trusted_relationship            = row.trusted_relationship,
  pa.shared_assessments_count        = row.shared_assessments_count,
  pa.received_assessments_count      = row.received_assessments_count,
  pa.exchange_agreements_count       = row.exchange_agreements_count,
  pa.last_exchange_date              = date(row.last_exchange_date),
  pa.quality_incidents_reported      = row.quality_incidents_reported;
"""
#Assessment_result
assessment_result = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:AssessmentResult {industry_standard_regulation_id: 'TISAX', assessment_result_id: row.result_id})
ON CREATE SET
  ar.certification_date            = date(row.certification_date),
  ar.validity_start                = date(row.validity_start),
  ar.validity_end                  = date(row.validity_end),
  ar.assessment_level_achieved     = row.assessment_level_achieved,
  ar.overall_compliance_percentage = row.overall_compliance_percentage,
  ar.findings_critical_count       = row.findings_critical_count,
  ar.findings_major_count          = row.findings_major_count,
  ar.findings_minor_count          = row.findings_minor_count,
  ar.findings_observations_count   = row.findings_observations_count,
  ar.non_conformities              = row.non_conformities,
  ar.corrective_actions_required   = row.corrective_actions_required,
  ar.label_status                  = row.label_status,
  ar.label_validity_months         = row.label_validity_months,
  ar.auditor_name                  = row.auditor_name,
  ar.auditor_sign_off_date         = date(row.auditor_sign_off_date),
  ar.confidentiality_level         = row.confidentiality_level,
  ar.result_documentation_url      = row.result_documentation_url,
  ar.issuing_body                  = row.issuing_body;
"""

#Exchange_node
exchange_node = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:TisaxExchange {industry_standard_regulation_id: 'TISAX',exchange_id: row.exchange_id})
ON CREATE SET
  ex.name        = row.name,
  ex.description = row.description,
  ex.operator    = row.operator,
  ex.status      = row.status;
"""
#Relationships
#REGISTERS_IN_TISAX
registers_in_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {
  organization_id: row.source_organization_id
})
MATCH (tisax:IndustryStandardAndRegulation {
  industry_standard_regulation_id: row.target_tisax
})
MERGE (tisax)-[r:ORGANISATION_REGISTERS_IN_TISAX {
  type: row.relationship_type
}]->(org)
ON CREATE SET
  r.registration_date      = date(row.registration_date),
  r.initial_al_target      = row.initial_al_target,
  r.scope_declaration      = row.scope_declaration,
  r.terms_acceptance_date  = date(row.terms_acceptance_date),
  r.registration_number    = row.registration_number;
"""
#UNDERGOES_ASSESSMENT
undergoes_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {
  organization_id: row.source_organization_id
})
MATCH (ass:Assessment {
  assessment_id: row.target_assessment_id
})
MERGE (org)-[r:ORGANISATION_UNDERGOES_ASSESSMENT {
  type: row.relationship_type
}]->(ass)
ON CREATE SET
  r.assessment_start        = row.assessment_start,
  r.scheduled_completion    = row.scheduled_completion,
  r.budget_allocated        = row.budget_allocated,
  r.scope_agreed            = row.scope_agreed,
  r.internal_resource_hours = row.internal_resource_hours;
"""
#SELECTS_ASSESSMENT_LEVEL
selects_assessment_level ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {organization_id: row.source_organization_id})
MATCH (al:AssessmentLevel {assessment_level_id: row.target_level_id})
MERGE (org)-[r:ORGANISATION_SELECTS_ASSESSMENT_LEVEL {type: row.relationship_type}]->(al)
ON CREATE SET
  r.selection_date              = row.selection_date,
  r.justification               = row.justification,
  r.data_protection_justification = row.data_protection_justification,
  r.approved_by                 = row.approved_by,
  r.is_upgrade_from_previous    = row.is_upgrade_from_previous;
"""
#CHOOSES_AUDIT_PROVIDER
chooses_audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {organization_id: row.source_organization_id})
MATCH (ap:AuditProvider {audit_provider_id: row.target_provider_id})
MERGE (org)-[r:ORGANISATION_CHOOSES_AUDIT_PROVIDER {type: row.relationship_type}]->(ap)
ON CREATE SET
  r.selection_date           = row.selection_date,
  r.criteria_considered      = row.criteria_considered,
  r.contract_start_date      = row.contract_start_date,
  r.contract_end_date        = row.contract_end_date,
  r.budget_agreed            = row.budget_agreed,
  r.primary_auditor_assigned = row.primary_auditor_assigned;
"""
#SUBJECT_TO_ISA_CATALOGUE
subject_to_isa_catalogue = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:Assessment {assessment_id: row.source_assessment_id})
MATCH (ic:ISACatalogue {isa_catalogue_id: row.target_catalogue_id})
MERGE (ass)-[r:ASSESSMENT_SUBJECT_TO_ISA_CATALOGUE {type: row.relationship_type}]->(ic)
ON CREATE SET
  r.applicability_date                 = row.applicability_date,
  r.catalogue_version_used             = row.catalogue_version_used,
  r.control_questions_applicable_count = row.control_questions_applicable_count,
  r.exemptions_claimed                 = row.exemptions_claimed,
  r.exemption_justification            = row.exemption_justification;
"""
#CONTAINS_ASSESSMENT_OBJECTIVE
contains_assessment_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:Assessment {assessment_id: row.source_assessment_id})
MATCH (ao:AssessmentObjective {assessment_objective_id: row.target_objective_id})
MERGE (ass)-[r:ASSESSMENT_CONTAINS_ASSESSMENT_OBJECTIVE {type: row.relationship_type}]->(ao)
ON CREATE SET
  r.inclusion_date    = row.inclusion_date,
  r.priority_order    = row.priority_order,
  r.estimated_hours   = row.estimated_hours,
  r.weight_percentage = row.weight_percentage,
  r.pass_fail_criteria = row.pass_fail_criteria;
  """
#PROTECTS_OBJECT
protects_object = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:Assessment {assessment_id: row.source_assessment_id})
MATCH (po:ProtectionObject {protection_object_id: row.target_object_id})
MERGE (ass)-[r:ASSESSMENT_PROTECTS_PROTECTION_OBJECT {type: row.relationship_type}]->(po)
ON CREATE SET
    r.inclusion_date = row.inclusion_date,
    r.current_protection_level = row.current_protection_level,
    r.target_protection_level = row.target_protection_level,
    r.identified_gaps = row.identified_gaps;
  """

#ANSWERS_CONTROL_QUESTION
answers_control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {organization_id: row.source_organization_id})
MATCH (cq:ControlQuestion {control_question_id: row.target_question_id})
MERGE (org)-[r:ORGANISATION_ANSWERS_CONTROL_QUESTION {type: row.relationship_type}]->(cq)
ON CREATE SET
  r.response_date           = row.response_date,
  r.answer_status           = row.answer_status,
  r.maturity_level_achieved = row.maturity_level_achieved,
  r.evidence_provided       = row.evidence_provided,
  r.remediation_required     = row.remediation_required ,
  r.remediation_due_date     = row.remediation_due_date;
"""
#MEETS_CRITERIA
meets_criteria = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:Assessment {assessment_id: row.source_assessment_id})
MATCH (ao:AssessmentObjective {assessment_objective_id: row.target_objective_id})
MERGE (ass)-[r:ASSESSMENT_MEETS_CRITERIA {type: row.relationship_type}]->(ao)
ON CREATE SET
  r.verification_date       = row.verification_date,
  r.confidence_level        = row.confidence_level,
  r.evidence_types_reviewed = row.evidence_types_reviewed,
  r.auditor_notes           = row.auditor_notes;
"""
#SHARES_RESULTS_WITH
shares_results_with = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pa:Participant {participant_id: row.source_participant_id})
MATCH (tp:Participant {participant_id: row.target_participant_id})
MERGE (pa)-[r:PARTICIPANT_SHARES_RESULTS_WITH {type: row.relationship_type}]->(tp)
ON CREATE SET
  r.sharing_date                 = row.sharing_date,
  r.shared_by                    = row.shared_by,
  r.confidentiality_level_granted = row.confidentiality_level_granted,
  r.result_id_shared             = row.result_id_shared,
  r.expires_date                 = row.expires_date,
  r.consent_obtained             = row.consent_obtained;
"""

#PARTICIPATES_IN_EXCHANGE
participates_in_exchange = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pa:Participant {participant_id: row.source_participant_id})
MATCH (ex:TisaxExchange {exchange_id: row.target_tisax_exchange})
MERGE (pa)-[r:PARTICIPANT_PARTICIPATES_IN_EXCHANGE {type: row.relationship_type}]->(ex)
ON CREATE SET
  r.participation_start_date = row.participation_start_date,
  r.participation_status     = row.participation_status,
  r.agreement_signed_date    = row.agreement_signed_date;
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

#Nodes
client.query(regulation)
time.sleep(2)

client.query(organization.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_Organization_nodes.csv'))
time.sleep(2)

client.query(assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_Assessment_nodes.csv'))
time.sleep(2)

client.query(assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_AssessmentLevel_nodes.csv'))
time.sleep(2)

client.query(assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_AssessmentObjective_nodes.csv'))
time.sleep(2)

client.query(audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_AuditProvider_nodes.csv'))
time.sleep(2)

client.query(isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ISACatalogue_nodes.csv'))
time.sleep(2)

client.query(control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ControlQuestion_nodes.csv'))
time.sleep(2)

client.query(protection_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ProtectionObject_nodes.csv'))
time.sleep(2)

client.query(participant.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_Participant_nodes.csv'))
time.sleep(2)

client.query(assessment_result.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_AssessmentResult_nodes.csv'))
time.sleep(2)

client.query(exchange_node.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_Exchange_nodes.csv'))
time.sleep(2)

#Relationships
client.query(registers_in_tisax.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_REGISTERS_IN_TISAX_relationships.csv'))
time.sleep(2)

client.query(undergoes_assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_UNDERGOES_ASSESSMENT_relationships.csv'))  

client.query(selects_assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_SELECTS_ASSESSMENT_LEVEL_relationships.csv'))
time.sleep(2)

client.query(chooses_audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_CHOOSES_AUDIT_PROVIDER_relationships.csv'))
time.sleep(2)

client.query(subject_to_isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_SUBJECT_TO_ISA_CATALOGUE_relationships.csv'))
time.sleep(2)   

client.query(contains_assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_CONTAINS_ASSESSMENT_OBJECTIVE_relationships.csv'))
time.sleep(2)

client.query(protects_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_PROTECTS_OBJECT_relationships.csv'))
time.sleep(2)

client.query(answers_control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ANSWERS_CONTROL_QUESTION_relationships.csv'))
time.sleep(2)   

client.query(meets_criteria.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_MEETS_CRITERIA_relationships.csv'))
time.sleep(2)   

client.query(shares_results_with.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_SHARES_RESULTS_WITH_relationships.csv'))    
time.sleep(2)   

client.query(participates_in_exchange.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_PARTICIPATES_IN_EXCHANGE_relationships.csv'))    
time.sleep(2)
 
logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:IndustryStandardAndRegulation)-[*]->()
WITH path
UNWIND nodes(path) AS n
UNWIND relationships(path) AS r
WITH collect(DISTINCT n) AS uniqueNodes,
     collect(DISTINCT r) AS uniqueRels
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


graph = res[0]["graph_data"]   

import json
with open("tisax.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(graph, default=str, indent=2))

logger.info("✓ Exported graph data to tisax.json")
client.close()