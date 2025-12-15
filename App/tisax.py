#Regulation
from sys import audit


regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'TISAX'})
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
MERGE (org:Organization {regional_standard_regulation_id: 'TISAX', organization_id: row.organization_id})
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
MERGE (ass:Assessment {regional_standard_regulation_id: 'TISAX', assessment_id: row.assessment_id})
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
MERGE (al:AssessmentLevel {regional_standard_regulation_id: 'TISAX', assessment_level_id: row.assessment_level_id})
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
MERGE (ao:AssessmentObjective {regional_standard_regulation_id: 'TISAX', assessment_objective_id: row.assessment_objective_id})
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
MERGE (ap:AuditProvider {regional_standard_regulation_id: 'TISAX', audit_provider_id: row.audit_provider_id})
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
MERGE (ic:ISA_catalogue {regional_standard_regulation_id: 'TISAX', isa_catalogue_id: row.isa_catalogue_id})
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
MERGE (cq:ControlQuestion {regional_standard_regulation_id: 'TISAX', control_question_id: row.question_id})
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
MERGE (po:ProtectionObject {regional_standard_regulation_id: 'TISAX', protection_object_id: row.object_id})
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