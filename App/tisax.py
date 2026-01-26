#Regulation
regulation = """
MERGE (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 6.0'})
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
MERGE (org:Organization {industry_standard_regulation_id: 'TISAX 6.0', organization_id: row.organization_id})
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
MERGE (ass:Assessment {industry_standard_regulation_id: 'TISAX 6.0', assessment_id: row.assessment_id})
ON CREATE SET
  ass.start_date             = date(row.start_date),
  ass.completion_date        = date(row.completion_date),
  ass.planned_duration_days  = row.planned_duration_days,
  ass.level       = row.assessment_level,
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
MERGE (al:AssessmentLevel {industry_standard_regulation_id: 'TISAX 6.0', assessment_level_id: row.level_id})
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
MERGE (ao:AssessmentObjective {industry_standard_regulation_id: 'TISAX 6.0', assessment_objective_id: row.objective_id})
ON CREATE SET
  ao.name                   = row.name,
  ao.category               = row.category,
  ao.description            = row.description,
  ao.ref      = row.isa_catalogue_ref,
  ao.count = row.control_questions_count,
  ao.level      = row.criticality_level,
  ao.risk_area              = row.risk_area,
  ao.version   = row.requirements_version,
  ao.standards      = row.related_standards,
  ao.evidence_types_required = row.evidence_types_required,
  ao.typical_effort_hours   = row.typical_effort_hours;
"""
#audit_provider
audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AuditProvider {industry_standard_regulation_id: 'TISAX 6.0', audit_provider_id: row.provider_id})
ON CREATE SET
  ap.name                         = row.provider_name,
  ap.number                       = row.registration_number,
  ap.status                       = row.accreditation_status,
  ap.date                         = date(row.accreditation_date),
  ap.expiry                       = date(row.accreditation_expiry),
  ap.levels  = row.supported_assessment_levels,
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
MERGE (ic:ISACatalogue {industry_standard_regulation_id: 'TISAX 6.0', isa_catalogue_id: row.catalogue_id})
ON CREATE SET
  ic.name                    = row.name,
  ic.type                    = row.type,
  ic.version                 = row.version,
  ic.release_date            = date(row.release_date),
  ic.last_updated            = date(row.last_updated),
  ic.total_control_questions = row.total_control_questions,
  ic.categories  = row.requirement_categories,
  ic.scope_coverage          = row.scope_coverage,
  ic.levels   = row.maturity_model_levels,
  ic.alignment_with_standards = row.alignment_with_standards,
  ic.geographic_applicability = row.geographic_applicability,
  ic.language_support        = row.language_support,
  ic.url       = row.documentation_url;
"""
#control_question
control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cq:ControlQuestion {industry_standard_regulation_id: 'TISAX 6.0', control_question_id: row.question_id})
ON CREATE SET
  cq.number         = row.sequence_number,
  cq.text           = row.question_text,
  cq.category       = row.question_category,
  cq.criticality             = row.criticality,
  cq.applies_to_al1          = row.applies_to_al1,
  cq.applies_to_al2          = row.applies_to_al2,
  cq.applies_to_al3          = row.applies_to_al3,
  cq.types = row.expected_evidence_types,
  cq.levels         = row.maturity_levels,
  cq.options = row.typical_response_options,
  cq.guidance_url            = row.guidance_url,
  cq.last_revision_date      = row.last_revision_date,
  cq.ids     = row.related_control_ids;
"""
#Protection Object
protection_object = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:ProtectionObject {industry_standard_regulation_id: 'TISAX 6.0', protection_object_id: row.object_id})
ON CREATE SET
  po.name                       = row.name,
  po.type                       = row.type,
  po.classification             = row.classification,
  po.level           = row.protection_level,
  po.is_sensitive               = row.is_sensitive,
  po.contained  = row.data_categories_contained,
  po.department           = row.owner_department,
  po.criticality_to_business    = row.criticality_to_business,
  po.location                   = row.location,
  po.last_date       = date(row.last_assessment_date),
  po.implemented = row.protection_controls_implemented,
  po.remaining_risk             = row.remaining_risk;
"""
#Participant
participant = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:Participant {industry_standard_regulation_id: 'TISAX 6.0', participant_id: row.participant_id})
ON CREATE SET
  pa.name               = row.organization_name,
  pa.type                = row.participant_type,
  pa.joining_date                    = date(row.joining_date),
  pa.level  = row.assessment_result_access_level,
  pa.status             = row.data_sharing_status,
  pa.relationship            = row.trusted_relationship,
  pa.shared_count        = row.shared_assessments_count,
  pa.received_count      = row.received_assessments_count,
  pa.exchange_count       = row.exchange_agreements_count,
  pa.last_exchange_date              = date(row.last_exchange_date),
  pa.incidents_reported      = row.quality_incidents_reported;
"""
#Assessment_result
assessment_result = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:AssessmentResult {industry_standard_regulation_id: 'TISAX 6.0', assessment_result_id: row.result_id})
ON CREATE SET
  ar.certification_date            = date(row.certification_date),
  ar.start_date               = date(row.validity_start),
  ar.end_date               = date(row.validity_end),
  ar.level_achieved     = row.assessment_level_achieved,
  ar.overall_compliance_percentage = row.overall_compliance_percentage,
  ar.findings_critical_count       = row.findings_critical_count,
  ar.findings_major_count          = row.findings_major_count,
  ar.findings_minor_count          = row.findings_minor_count,
  ar.findings_observations_count   = row.findings_observations_count,
  ar.non_conformities              = row.non_conformities,
  ar.corrective_actions_required   = row.corrective_actions_required,
  ar.status                  = row.label_status,
  ar.validity_months         = row.label_validity_months,
  ar.name                  = row.auditor_name,
  ar.sign_off_date         = date(row.auditor_sign_off_date),
  ar.confidentiality_level         = row.confidentiality_level,
  ar.result_documentation_url      = row.result_documentation_url,
  ar.issuing_body                  = row.issuing_body;
"""

#Exchange_node
exchange_node = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:TisaxExchange {industry_standard_regulation_id: 'TISAX 6.0', exchange_id: row.exchange_id})
ON CREATE SET
  ex.name        = row.name,
  ex.description = row.description,
  ex.operator    = row.operator,
  ex.status      = row.status;
"""

#Control_category
control_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ControlCategory {industry_standard_regulation_id: 'TISAX 6.0', category_id: row.category_id})
ON CREATE SET
  cc.name = row.name,
  cc.description = row.description,
  cc.code = row.code,
  cc.display_order = toInteger(row.display_order),
  cc.focus_area = row.focus_area,
  cc.is_new_in_v6 = toBoolean(row.is_new_in_v6),
  cc.total_controls = toInteger(row.total_controls_count);
"""

#Role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rl:Role {industry_standard_regulation_id: 'TISAX 6.0', role_id: row.role_id})
ON CREATE SET
  rl.title               = row.role_title,
  rl.description         = row.description,
  rl.responsibilities    = row.key_responsibilities,
  rl.qualification_reqs  = row.qualification_requirements,
  rl.is_mandatory        = toBoolean(row.is_mandatory),
  rl.reporting_line      = row.reporting_line,
  rl.typical_department  = row.typical_department;
"""

#Security_policy
security_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:SecurityPolicy {industry_standard_regulation_id: 'TISAX 6.0', policy_id: row.policy_id})
ON CREATE SET
  sp.title               = row.title,
  sp.type                = row.policy_type,
  sp.description         = row.description,
  sp.version             = row.version,
  sp.last_review_date    = date(row.last_review_date),
  sp.next_review_date    = date(row.next_review_date),
  sp.approval_status     = row.approval_status,
  sp.enforcement_level   = row.enforcement_level,
  sp.iso_reference       = row.iso_27001_reference,
  sp.document_url        = row.document_url;
"""

#Data_category
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {industry_standard_regulation_id: 'TISAX 6.0', data_category_id: row.data_category_id})
ON CREATE SET
  dc.name                = row.name,
  dc.description     = row.description,
  dc.classification      = row.default_classification,
  dc.is_personal_data    = toBoolean(row.is_personal_data),
  dc.is_prototype_data   = toBoolean(row.is_prototype_data),
  dc.retention_period    = row.typical_retention_period,
  dc.handling_reqs       = row.handling_requirements,
  dc.encryption_req      = toBoolean(row.encryption_required);
"""

#Assessment_phase
assessment_phase = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (aph:AssessmentPhase {industry_standard_regulation_id: 'TISAX 6.0', phase_id: row.phase_id})
ON CREATE SET
  aph.name               = row.name,
  aph.description        = row.description,
  aph.sequence_order     = toInteger(row.sequence_order),
  aph.typical_duration   = row.typical_duration_weeks,
  aph.required_inputs    = row.required_inputs,
  aph.deliverables       = row.expected_deliverables,
  aph.is_mandatory       = toBoolean(row.is_mandatory),
  aph.owner              = row.process_owner;
"""

#Finding
finding = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fd:Finding {industry_standard_regulation_id: 'TISAX 6.0', finding_id: row.finding_id})
ON CREATE SET
  fd.type                = row.finding_type,
  fd.description         = row.description,
  fd.severity            = row.severity_level,
  fd.date_identified     = date(row.date_identified),
  fd.auditor_comment     = row.auditor_comment,
  fd.status              = row.status,
  fd.remediation_deadline = date(row.remediation_deadline),
  fd.root_cause          = row.root_cause_analysis,
  fd.evidence_ref        = row.evidence_reference;
"""

#Relationships
#REGISTERS_IN_TISAX
registers_in_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: row.target_tisax})
MATCH (org:Organization {organization_id: row.source_organization_id})
MERGE (reg)-[r:REGISTERS_IN_TISAX]->(org)
ON CREATE SET
  r.type                   = row.relationship_type,
  r.registration_date      = row.registration_date,
  r.initial_al_target      = row.initial_al_target,
  r.scope_declaration      = row.scope_declaration,
  r.terms_acceptance_date  = row.terms_acceptance_date,
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
MERGE (pa)-[r:PARTICIPANT_SHARES_RESULTS {type: row.relationship_type}]->(tp)
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
#result_of_assessment
result_of_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:AssessmentResult {assessment_result_id: row.source_result_id})
MATCH (ass:Assessment {assessment_id: row.target_assessment_id})
MERGE (ar)-[r:ASSESSMENT_RESULT_OF_ASSESSMENT {type: row.relationship_type}]->(ass)
ON CREATE SET
  r.result_date        = date(row.result_date),
  r.final_status       = row.final_status,
  r.certification_body = row.certification_body;
"""
# Participant → IndustryStandardAndRegulation (TISAX)
participant_to_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pa:Participant {participant_id: row.source_participant_id})
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: row.target_regulation_id})
MERGE (pa)-[r:PARTICIPANT_PARTICIPATES_IN_TISAX]->(reg)
ON CREATE SET
  r.type                    = row.relationship_type,
  r.registration_date       = row.registration_date,
  r.participation_status    = row.participation_status,
  r.agreement_signed_date   = row.agreement_signed_date;
"""
#ISA -> control_question
ISA_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ic:ISACatalogue {isa_catalogue_id: row.source_catalogue_id})
MATCH (cq:ControlQuestion {control_question_id: row.target_question_id})
MERGE (ic)-[r:ISA_CONTROLS_CONTROL_QUESTION {type: row.relationship_type}]->(cq)
ON CREATE SET
  r.inclusion_date = row.inclusion_date,
  r.applicability_level = row.applicability_level,
  r.question_order = row.question_order,
  r.question_weight = row.question_weight,
  r.response_required = row.response_required;
"""

#Isa_catalogue_has_category#
isa_catalogue_has_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ic:ISACatalogue {isa_catalogue_id: row.source_catalogue_id})
MATCH (cc:ControlCategory {category_id: row.target_category_id})
MERGE (ic)-[r:ISA_CATALOGUE_HAS_CATEGORY {type: row.relationship_type}]->(cc)
ON CREATE SET
  r.inclusion_date = date(row.inclusion_date),
  r.is_mandatory   = toBoolean(row.is_mandatory);
"""

#Organization_assigns_role
organization_assigns_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {organization_id: row.source_organization_id})
MATCH (rl:Role {role_id: row.target_role_id})
MERGE (org)-[r:ORGANISATION_ASSIGNS_ROLE {type: row.relationship_type}]->(rl)
ON CREATE SET
  r.assignee_name   = row.assignee_name,
  r.assignment_date = date(row.assignment_date);
"""

#Organization_establishes_policy
organization_establishes_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {organization_id: row.source_organization_id})
MATCH (sp:SecurityPolicy {policy_id: row.target_policy_id})
MERGE (org)-[r:ORGANISATION_ESTABLISHES_POLICY {type: row.relationship_type}]->(sp)
ON CREATE SET
  r.establishment_date = date(row.establishment_date),
  r.owner_role_id      = row.owner_role_id;
"""

#Protection_object_classified_as
protection_object_classified_as = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (po:ProtectionObject {protection_object_id: row.source_object_id})
MATCH (dc:DataCategory {data_category_id: row.target_category_id})
MERGE (po)-[r:PROTECTION_OBJECT_CLASSIFIED_AS_DATA_CATEGORY {type: row.relationship_type}]->(dc)
ON CREATE SET
  r.classification_date = date(row.classification_date),
  r.volume_estimate     = row.volume_estimate;
"""

#Assessment_includes_phase#
assessment_includes_phase = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ass:Assessment {assessment_id: row.source_assessment_id})
MATCH (aph:AssessmentPhase {phase_id: row.target_phase_id})
MERGE (ass)-[r:ASSESSMENT_INCLUDES_PHASE {type: row.relationship_type}]->(aph)
ON CREATE SET
  r.start_date = date(row.start_date),
  r.end_date   = date(row.end_date),
  r.status     = row.status;
"""

#Assessment_result_contains_finding#
assessment_result_contains_finding = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:AssessmentResult {assessment_result_id: row.source_result_id})
MATCH (fd:Finding {finding_id: row.target_finding_id})
MERGE (ar)-[r:ASSESSMENT_RESULT_CONTAINS_FINDING {type: row.relationship_type}]->(fd)
ON CREATE SET
  r.impact_on_label     = row.impact_on_label,
  r.verification_method = row.verification_method;
"""
#Orphan_assessment_phase
orphan_assessment_phase = """
MATCH (orphan:AssessmentPhase) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 6.0'})
MERGE (reg)-[:TISAX_PRESCRIBES_PHASE]->(orphan);
"""

#Orphan_audit_provider
orphan_audit_provider = """
MATCH (orphan:AuditProvider) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 6.0'})
MERGE (reg)-[:TISAX_ACCREDITS_PROVIDER]->(orphan);
"""

#Orphan_data_category
orphan_data_category = """
MATCH (orphan:DataCategory) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 6.0'})
MERGE (reg)-[:TISAX_PROTECTS_DATA_CATEGORY]->(orphan);
"""

#Orphan_role
orphan_role = """
MATCH (orphan:Role) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 6.0'})
MERGE (reg)-[:TISAX_DEFINES_ROLE]->(orphan);
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
client.query(control_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/control_categories.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/roles.csv"))
time.sleep(2)

client.query(security_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/security_policies.csv"))
time.sleep(2)

client.query(data_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/data_categories.csv"))
time.sleep(2)

client.query(assessment_phase.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/assessment_phases.csv"))
time.sleep(2)

client.query(finding.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/findings.csv"))
time.sleep(2)

#Relationships
client.query(registers_in_tisax.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_REGISTERS_IN_TISAX_relationships.csv'))
time.sleep(2)

client.query(undergoes_assessment.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_UNDERGOES_ASSESSMENT_relationships.csv'))  

client.query(selects_assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_SELECTS_ASSESSMENT_LEVEL_relationships.csv'))
time.sleep(2)

client.query(chooses_audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_Organisation_Chooses_AuditProvider_relationships.csv'))
time.sleep(2)

client.query(subject_to_isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ISA_CATALOGUE_relationships.csv'))
time.sleep(2)   

client.query(contains_assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_CONTAINS_ASSESSMENT_OBJECTIVE_relationships.csv'))
time.sleep(2)

client.query(protects_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_PROTECTS_OBJECT_relationships.csv'))
time.sleep(2)

client.query(answers_control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ANSWERS_FULLY_UNIQUE_relationships.csv'))
time.sleep(2)   

client.query(meets_criteria.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_MEETS_CRITERIA_relationships.csv'))
time.sleep(2)   

client.query(shares_results_with.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_SHARES_RESULTS_WITH_relationships.csv'))    
time.sleep(2)   

client.query(participates_in_exchange.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_PARTICIPATES_IN_EXCHANGE_relationships.csv'))    
time.sleep(2)

client.query(result_of_assessment.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_RESULT_OF_ASSESSMENT_relationships.csv'))
time.sleep(2)

client.query(participant_to_tisax.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_PARTICIPANT_REGISTERS_IN_TISAX_relationships.csv'))
time.sleep(2)

client.query(ISA_control.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX_ISA_CONTAINS_QUESTIONS.csv'))
time.sleep(2)

client.query(isa_catalogue_has_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX%20-%20ISA%20Catalogue%20Control%20Category.csv"))
time.sleep(2)

client.query(organization_assigns_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/rel_org_assigns_role.csv"))
time.sleep(2)

client.query(organization_establishes_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/rel_org_establishes_policy.csv"))
time.sleep(2)

client.query(protection_object_classified_as.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/rel_object_classified_as.csv"))
time.sleep(2)

client.query(assessment_includes_phase.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX%20-%20Assesment%20Assesment%20Phase.csv"))
time.sleep(2)

client.query(assessment_result_contains_finding.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TISAX/TISAX%20-%20Assement%20Result%20Findings.csv"))
time.sleep(2)
 
client.query(orphan_assessment_phase)
time.sleep(2)

client.query(orphan_audit_provider)
time.sleep(2)

client.query(orphan_data_category)
time.sleep(2)

client.query(orphan_role)
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
    with open('tisax.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to tisax.json")
else:
    logger.error("No data returned from the query.")

client.close()
