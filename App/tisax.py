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
  ass.on_site_required       = row.on_sitr_required,
  ass.documentation_reviewed = row.documentation_reviewed;
"""
#assessment_level
assessment_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (al:AssessmentLevel {industry_standard_regulation_id: 'TISAX', assessment_level_id: row.assessment_level_id})
ON CREATE SET
  al.name                        = row.name,
  al.description                 = row.description,
  al.protection_level            = row.protection_level,
  al.data_protection_needs       = row.data_protection_needs,
  al.isa_catalogue_required      = row.isa_catalogue_required,
  al.external_audit_required     = row.external_audit_required,
  al.self_assessment_allowed     = row.self_assessment_allowed
  al.requires_on_site_visit      = row.requires_on_site_visit,
  al.typical_scope_size          = row.typical_scope_size,
  al.costs_implications          = row.costs_implications,
  al.certification_validity_years = toInteger(row.certification_validity_years);
"""
#Assessment_objective
assessment_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ao:AssessmentObjective {industry_standard_regulation_id: 'TISAX', assessment_objective_id: row.assessment_objective_id})
ON CREATE SET
  obj.name                   = row.name,
  obj.category               = row.category,
  obj.description            = row.description,
  obj.isa_catalogue_ref      = row.isa_catalogue_ref,
  obj.control_questions_count = toInteger(row.control_questions_count),
  obj.criticality_level      = row.criticality_level,
  obj.risk_area              = row.risk_area,
  obj.requirements_version   = row.requirements_version,
  obj.related_standards      = row.related_standards,
  obj.evidence_types_required = row.evidence_types_required,
  obj.typical_effort_hours   = toInteger(row.typical_effort_hours);
"""
#audit_provider
audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AuditProvider {industry_standard_regulation_id: 'TISAX', audit_provider_id: row.audit_provider_id})
ON CREATE SET
  ap.provider_name                = row.provider_name,
  ap.registration_number          = row.registration_number,
  ap.accreditation_status         = row.accreditation_status,
  ap.accreditation_date           = date(row.accreditation_date),
  ap.accreditation_expiry         = date(row.accreditation_expiry),
  ap.supported_assessment_levels  = row.supported_assessment_levels,
  ap.geographic_coverage          = row.geographic_coverage,
  ap.industry_specialization      = row.industry_specialization,
  ap.max_concurrent_assessments   = toInteger(row.max_concurrent_assessments),
  ap.average_audit_duration_days  = toInteger(row.average_audit_duration_days),
  ap.certification_count          = toInteger(row.certification_count),
  ap.quality_rating               = toFloat(row.quality_rating),
  ap.contact_person               = row.contact_person,
  ap.website                      = row.website;
"""
#ISA_catalogue
isa_catalogue = """ 
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ic:ISA_catalogue {industry_standard_regulation_id: 'TISAX', isa_catalogue_id: row.isa_catalogue_id})
ON CREATE SET
  cat.name                    = row.name,
  cat.type                    = row.type,
  cat.version                 = row.version,
  cat.release_date            = date(row.release_date),
  cat.last_updated            = date(row.last_updated),
  cat.total_control_questions = toInteger(row.total_control_questions),
  cat.requirement_categories  = row.requirement_categories,
  cat.scope_coverage          = row.scope_coverage,
  cat.maturity_model_levels   = row.maturity_model_levels,
  cat.alignment_with_standards = row.alignment_with_standards,
  cat.geographic_applicability = row.geographic_applicability,
  cat.language_support        = row.language_support,
  cat.documentation_url       = row.documentation_url;
"""
#control_question
control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cq:ControlQuestion {industry_standard_regulation_id: 'TISAX', control_question_id: row.question_id})
ON CREATE SET
  cq.sequence_number         = toInteger(row.sequence_number),
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
  cq.last_revision_date      = date(row.last_revision_date),
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
  p.organization_name               = row.organization_name,
  p.participant_type                = row.participant_type,
  p.joining_date                    = date(row.joining_date),
  p.assessment_result_access_level  = row.assessment_result_access_level,
  p.data_sharing_status             = row.data_sharing_status,
  p.trusted_relationship            = row.trusted_relationship,
  p.shared_assessments_count        = toInteger(row.shared_assessments_count),
  p.received_assessments_count      = toInteger(row.received_assessments_count),
  p.exchange_agreements_count       = toInteger(row.exchange_agreements_count),
  p.last_exchange_date              = date(row.last_exchange_date),
  p.quality_incidents_reported      = toInteger(row.quality_incidents_reported);
"""
#Assessment_result
assessment_result = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:AssessmentResult {industry_standard_regulation_id: 'TISAX', assessment_result_id: row.result_id})
ON CREATE SET
  res.certification_date            = date(row.certification_date),
  res.validity_start                = date(row.validity_start),
  res.validity_end                  = date(row.validity_end),
  res.assessment_level_achieved     = toInteger(row.assessment_level_achieved),
  res.overall_compliance_percentage = toFloat(row.overall_compliance_percentage),
  res.findings_critical_count       = toInteger(row.findings_critical_count),
  res.findings_major_count          = toInteger(row.findings_major_count),
  res.findings_minor_count          = toInteger(row.findings_minor_count),
  res.findings_observations_count   = toInteger(row.findings_observations_count),
  res.non_conformities              = toInteger(row.non_conformities),
  res.corrective_actions_required   = row.corrective_actions_required,
  res.label_status                  = row.label_status,
  res.label_validity_months         = toInteger(row.label_validity_months),
  res.auditor_name                  = row.auditor_name,
  res.auditor_sign_off_date         = date(row.auditor_sign_off_date),
  res.confidentiality_level         = row.confidentiality_level,
  res.result_documentation_url      = row.result_documentation_url,
  res.issuing_body                  = row.issuing_body;
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
MATCH (org:TisaxOrganization {
  organization_id: row.source_organization_id
})
MATCH (tisax:IndustryStandardAndRegulation {
  industry_standard_regulation_id: row.target_tisax
})
MERGE (org)-[r:REGISTERS_IN_TISAX {
  type: row.relationship_type
}]->(tisax)
ON CREATE SET
  r.registration_date      = date(row.registration_date),
  r.initial_al_target      = toInteger(row.initial_al_target),
  r.scope_declaration      = row.scope_declaration,
  r.terms_acceptance_date  = date(row.terms_acceptance_date),
  r.registration_number    = row.registration_number;
"""
#UNDERGOES_ASSESSMENT
undergoes_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:TisaxOrganization {
  organization_id: row.source_organization_id
})
MATCH (ass:TisaxAssessment {
  assessment_id: row.target_assessment_id
})
MERGE (org)-[r:UNDERGOES_ASSESSMENT {
  type: row.relationship_type
}]->(ass)
ON CREATE SET
  r.assessment_start        = date(row.assessment_start),
  r.scheduled_completion    = date(row.scheduled_completion),
  r.budget_allocated        = toInteger(row.budget_allocated),
  r.scope_agreed            = row.scope_agreed,
  r.internal_resource_hours = toInteger(row.internal_resource_hours);
"""
#SELECTS_ASSESSMENT_LEVEL
selects_assessment_level ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:TisaxOrganization {
  organization_id: row.source_organization_id
})
MATCH (al:TisaxAssessmentLevel {
  level_id: toInteger(row.target_level_id)
})
MERGE (org)-[r:SELECTS_ASSESSMENT_LEVEL {
  type: row.relationship_type
}]->(al)
ON CREATE SET
  r.selection_date              = date(row.selection_date),
  r.justification               = row.justification,
  r.data_protection_justification = row.data_protection_justification,
  r.approved_by                 = row.approved_by,
  r.is_upgrade_from_previous    = row.is_upgrade_from_previous;
"""
#CHOOSES_AUDIT_PROVIDER
chooses_audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:TisaxOrganization {
  organization_id: row.source_organization_id
})
MATCH (ap:TisaxAuditProvider {
  provider_id: row.target_provider_id
})
MERGE (org)-[r:CHOOSES_AUDIT_PROVIDER {
  type: row.relationship_type
}]->(ap)
ON CREATE SET
  r.selection_date          = date(row.selection_date),
  r.criteria_considered     = row.criteria_considered,
  r.contract_start_date     = date(row.contract_start_date),
  r.contract_end_date       = date(row.contract_end_date),
  r.budget_agreed           = toInteger(row.budget_agreed),
  r.primary_auditor_assigned = row.primary_auditor_assigned;
"""
#SUBJECT_TO_ISA_CATALOGUE
subject_to_isa_catalogue = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:TisaxAssessment {
  assessment_id: row.source_assessment_id
})
MATCH (cat:TisaxISACatalogue {
  catalogue_id: row.target_catalogue_id
})
MERGE (ass)-[r:SUBJECT_TO_ISA_CATALOGUE {
  type: row.relationship_type
}]->(cat)
ON CREATE SET
  r.applicability_date                 = date(row.applicability_date),
  r.catalogue_version_used             = row.catalogue_version_used,
  r.control_questions_applicable_count = toInteger(row.control_questions_applicable_count),
  r.exemptions_claimed                 = row.exemptions_claimed,
  r.exemption_justification            = row.exemption_justification;
"""
#CONTAINS_ASSESSMENT_OBJECTIVE
contains_assessment_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:TisaxAssessment {
  assessment_id: row.source_assessment_id
})
MATCH (obj:TisaxAssessmentObjective {
  objective_id: row.target_objective_id
})
MERGE (ass)-[r:CONTAINS_ASSESSMENT_OBJECTIVE {
  type: row.relationship_type
}]->(obj)
ON CREATE SET
  r.inclusion_date   = date(row.inclusion_date),
  r.priority_order   = toInteger(row.priority_order),
  r.estimated_hours  = toInteger(row.estimated_hours),
  r.weight_percentage = toFloat(row.weight_percentage),
  r.pass_fail_criteria = row.pass_fail_criteria;
"""
#PROTECTS_OBJECT
protects_object = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:TisaxAssessment {
  assessment_id: row.source_assessment_id
})
MATCH (po:TisaxProtectionObject {
  object_id: row.target_object_id
})
MERGE (ass)-[r:PROTECTS_OBJECT {
  type: row.relationship_type
}]->(po)
ON CREATE SET
  r.inclusion_date          = date(row.inclusion_date),
  r.current_protection_level = row.current_protection_level,
  r.target_protection_level  = row.target_protection_level,
  r.identified_gaps          = row.identified_gaps;
"""
#ANSWERS_CONTROL_QUESTION
answers_control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:TisaxOrganization {
  organization_id: row.source_organization_id
})
MATCH (cq:TisaxControlQuestion {
  question_id: row.target_question_id
})
MERGE (org)-[r:ANSWERS_CONTROL_QUESTION {
  type: row.relationship_type
}]->(cq)
ON CREATE SET
  r.response_date            = date(row.response_date),
  r.answer_status            = row.answer_status,
  r.maturity_level_achieved  = toInteger(row.maturity_level_achieved),
  r.evidence_provided        = row.evidence_provided,
  r.remediation_required     = row.remediation_required ,
  r.remediation_due_date     = row.remediation_due_date;
"""
#MEETS_CRITERIA
meets_criteria = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:TisaxAssessment {
  assessment_id: row.source_assessment_id
})
MATCH (obj:TisaxAssessmentObjective {
  objective_id: row.target_objective_id
})
MERGE (ass)-[r:MEETS_CRITERIA {
  type: row.relationship_type
}]->(obj)
ON CREATE SET
  r.verification_date       = date(row.verification_date),
  r.confidence_level        = toFloat(row.confidence_level),
  r.evidence_types_reviewed = row.evidence_types_reviewed,
  r.auditor_notes           = row.auditor_notes;
"""
#SHARES_RESULTS_WITH
shares_results_with = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (src:TisaxParticipant {
  participant_id: row.source_participant_id
})
MATCH (tgt:TisaxParticipant {
  participant_id: row.target_participant_id
})
MATCH (res:TisaxAssessmentResult {
  result_id: row.result_id_shared
})
MERGE (src)-[r:SHARES_RESULTS_WITH {
  type: row.relationship_type
}]->(tgt)
ON CREATE SET
  r.sharing_date                 = date(row.sharing_date),
  r.shared_by                    = row.shared_by,
  r.confidentiality_level_granted = row.confidentiality_level_granted,
  r.result_id_shared             = res.result_id,
  r.expires_date                 = date(row.expires_date),
  r.consent_obtained             = row.consent_obtained;
  """

#PARTICIPATES_IN_EXCHANGE
participates_in_exchange = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (p:TisaxParticipant {
  participant_id: row.source_participant_id
})
MATCH (ex:TisaxExchange {
  exchange_id: row.target_tisax_exchange
})
MERGE (p)-[r:PARTICIPATES_IN_EXCHANGE {
  type: row.relationship_type
}]->(ex)
ON CREATE SET
  r.participation_start_date = date(row.participation_start_date),
  r.participation_status     = row.participation_status,
  r.agreement_signed_date    = date(row.agreement_signed_date);
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

client.query(organization.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Rule_nodes.csv'))
time.sleep(2)

client.query(assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Section_nodes.csv'))
time.sleep(2)

client.query(assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Requirement_nodes.csv'))
time.sleep(2)

client.query(assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Role_nodes.csv'))
time.sleep(2)

client.query(audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_DataCategory_nodes.csv'))
time.sleep(2)

client.query(isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_EventType_nodes.csv'))
time.sleep(2)

client.query(control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Safeguard_nodes.csv'))
time.sleep(2)

client.query(protection_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_EnforcementAction_nodes.csv'))
time.sleep(2)

client.query(participant.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Policy_nodes.csv'))
time.sleep(2)

client.query(assessment_result.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Control_nodes.csv'))
time.sleep(2)

client.query(exchange_node.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_System_nodes.csv'))
time.sleep(2)

#Relationships
client.query(registers_in_tisax.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Process_nodes.csv'))
time.sleep(2)

client.query(undergoes_assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASRULE_relationships.csv'))  

client.query(selects_assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASSECTION_relationships.csv'))
time.sleep(2)

client.query(chooses_audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASREQUIREMENT_relationships.csv'))
time.sleep(2)

client.query(subject_to_isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_APPLIESTOROLE_relationships.csv'))
time.sleep(2)   

client.query(contains_assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_APPLIESTODATA_relationships.csv'))
time.sleep(2)

client.query(protects_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_TRIGGERSEVENTTYPE_relationships.csv'))
time.sleep(2)

client.query(answers_control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_REQUIRESSAFEGUARD_relationships.csv'))
time.sleep(2)   

client.query(meets_criteria.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_SUPPORTEDBYPOLICY_relationships.csv'))
time.sleep(2)   

client.query(shares_results_with.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_IMPLEMENTEDBYCONTROL_relationships.csv'))    
time.sleep(2)   

client.query(participates_in_exchange.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_IMPLEMENTEDINSYSTEM_relationships.csv'))    
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
with open('tisax.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to tisax.json")

client.close()
