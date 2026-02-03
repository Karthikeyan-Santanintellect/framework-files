# Regulation
regulation = """
MERGE (r:IndustryStandardAndRegulation {industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  r.name = "Health Information Technology for Economic and Clinical Health Act",
  r.version = "2009",
  r.enactment_date = date("2009-02-17"),
  r.description = "U.S. legislation to promote the adoption and meaningful use of health information technology.";
"""
#title
title = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Title {
    industry_standard_regulation_id: "HITECH_ACT_2009",
    title_id: row.title_id
})
ON CREATE SET
    t.name = row.name,
    t.description = row.description,
    t.enactment_date = date(row.enactment_date),
    t.jurisdiction = row.jurisdiction,
    t.authority = row.authority,
    t.status = row.status,
    t.parent_framework = row.parent_framework,
    t.short_name = row.short_name;
"""
#subtitle
subtitle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subtitle {
    industry_standard_regulation_id: "HITECH_ACT_2009",
    subtitle_id: row.subtitle_id
})
ON CREATE SET
    s.title_id = row.title_id,
    s.name = row.name,
    s.description = row.description,
    s.enactment_date = date(row.enactment_date),
    s.jurisdiction = row.jurisdiction,
    s.authority = row.authority,
    s.status = row.status,
    s.parent_framework = row.parent_framework,
    s.short_name = row.short_name,
    s.key_concepts = row.key_concepts;
"""
#section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  section_id: row.section_id
})
ON CREATE SET
  sec.subtitle_id     = row.subtitle_id,
  sec.full_citation   = row.full_citation,
  sec.heading         = row.heading,
  sec.description     = row.description,
  sec.content_summary = row.content_summary,
  sec.key_concepts    = row.key_concepts,
  sec.enacted_date    = date(row.enacted_date),
  sec.jurisdiction    = row.jurisdiction,
  sec.authority       = row.authority,
  sec.status          = row.status,
  sec.parent_framework= row.parent_framework,
  sec.short_name      = row.short_name;
"""
#requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  requirement_id: row.requirement_id
})
ON CREATE SET
  req.section_id = row.section_id,
  req.subtitle_id = row.subtitle_id,
  req.heading = row.heading,
  req.description = row.description,
  req.requirement_type = row.requirement_type,
  req.implementation_scope = row.implementation_scope,
  req.responsible_entity = row.responsible_entity,
  req.compliance_timeline = row.compliance_timeline,
  req.verification_method = row.verification_method,
  req.domain_covered = row.domain_covered,
  req.priority = row.priority,
  req.status = row.status,
  req.key_controls = row.key_controls,
  req.related_sections = row.related_sections;
"""
#role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (role:Role {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  role_id: row.role_id
})
ON CREATE SET
  role.role_name = row.role_name,
  role.organization_type = row.organization_type,
  role.description = row.description,
  role.primary_responsibilities = row.primary_responsibilities,
  role.authority_source = row.authority_source,
  role.regulatory_scope = row.regulatory_scope,
  role.compliance_obligations = row.compliance_obligations,
  role.enforcement_authority = row.enforcement_authority,
  role.domains_covered = row.domains_covered,
  role.examples = row.examples,
  role.key_stakeholders = row.key_stakeholders,
  role.priority_level = row.priority_level,
  role.status = row.status;
"""
#data_category
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cat:DataCategory {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  data_category_id: row.data_category_id
})
ON CREATE SET
  cat.data_category_name = row.data_category_name,
  cat.parent_category = row.parent_category,
  cat.description = row.description,
  cat.regulatory_definition = row.regulatory_definition,
  cat.classification_level = row.classification_level,
  cat.protection_requirements = row.protection_requirements,
  cat.breach_notification_required = row.breach_notification_required,
  cat.minimum_safeguards = row.minimum_safeguards,
  cat.handling_restrictions = row.handling_restrictions,
  cat.retention_requirements = row.retention_requirements,
  cat.disposal_requirements = row.disposal_requirements,
  cat.domains_covered = row.domains_covered,
  cat.applicable_sections = row.applicable_sections,
  cat.examples = row.examples,
  cat.key_identifiers = row.key_identifiers,
  cat.compliance_obligations = row.compliance_obligations,
  cat.enforcement_authority = row.enforcement_authority,
  cat.priority_level = row.priority_level,
  cat.status = row.status;
"""
#safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  safeguard_id: row.safeguard_id
})
ON CREATE SET
  sg.safeguard_type = row.safeguard_type,
  sg.safeguard_category = row.safeguard_category,
  sg.safeguard_name = row.safeguard_name,
  sg.description = row.description,
  sg.regulatory_basis = row.regulatory_basis,
  sg.implementation_scope = row.implementation_scope,
  sg.responsible_entity = row.responsible_entity,
  sg.technical_details = row.technical_details,
  sg.compliance_testing = row.compliance_testing,
  sg.effectiveness_metrics = row.effectiveness_metrics,
  sg.related_requirements = row.related_requirements,
  sg.domains_covered = row.domains_covered,
  sg.applicable_sections = row.applicable_sections,
  sg.success_criteria = row.success_criteria,
  sg.failure_consequences = row.failure_consequences,
  sg.enforcement_authority = row.enforcement_authority,
  sg.priority_level = row.priority_level,
  sg.status = row.status;
"""
#event_type
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (evt:EventType {
  industry_standard_regulation_id: "HITECH_ACT_2009",
  event_type_id: row.event_type_id
})
ON CREATE SET
  evt.event_type_category = row.event_type_category,
  evt.event_type_name = row.event_type_name,
  evt.description = row.description,
  evt.regulatory_definition = row.regulatory_definition,
  evt.classification_level = row.classification_level,
  evt.data_categories_affected = row.data_categories_affected,
  evt.typical_causes = row.typical_causes,
  evt.detection_methods = row.detection_methods,
  evt.investigation_scope = row.investigation_scope,
  evt.notification_required = row.notification_required,
  evt.notification_timeline = row.notification_timeline,
  evt.notification_recipients = row.notification_recipients,
  evt.risk_assessment_criteria = row.risk_assessment_criteria,
  evt.remediation_requirements = row.remediation_requirements,
  evt.documentation_requirements = row.documentation_requirements,
  evt.enforcement_authority = row.enforcement_authority,
  evt.penalty_tier = row.penalty_tier,
  evt.related_requirements = row.related_requirements,
  evt.domains_covered = row.domains_covered,
  evt.applicable_sections = row.applicable_sections,
  evt.success_criteria = row.success_criteria,
  evt.failure_consequences = row.failure_consequences,
  evt.priority_level = row.priority_level,
  evt.status = row.status;
"""
#enforcement_action
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {enforcement_action_id: row.enforcement_action_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  ea.enforcement_category = row.enforcement_category,
  ea.enforcement_type = row.enforcement_type,
  ea.enforcement_authority = row.enforcement_authority,
  ea.authority_agency = row.authority_agency,
  ea.description = row.description,
  ea.regulatory_basis = row.regulatory_basis,
  ea.applicable_to = row.applicable_to,
  ea.trigger_conditions = row.trigger_conditions,
  ea.initiation_process = row.initiation_process,
  ea.investigation_scope = row.investigation_scope,
  ea.documentation_requirements = row.documentation_requirements,
  ea.monetary_penalties = row.monetary_penalties,
  ea.penalty_tier = row.penalty_tier,
  ea.corrective_action_required = row.corrective_action_required,
  ea.timeline_for_action = row.timeline_for_action,
  ea.notification_process = row.notification_process,
  ea.appeal_process = row.appeal_process,
  ea.precedent_cases = row.precedent_cases,
  ea.related_hitech_sections = row.related_hitech_sections,
  ea.domains_covered = row.domains_covered,
  ea.applicable_regulations = row.applicable_regulations,
  ea.enforcement_frequency = row.enforcement_frequency,
  ea.success_metrics = row.success_metrics,
  ea.failure_consequences = row.failure_consequences,
  ea.priority_level = row.priority_level,
  ea.status = row.status;
"""
#incentive_program
incentive_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ip:IncentiveProgram {program_id: row.program_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  ip.program_category = row.program_category,
  ip.program_name = row.program_name,
  ip.program_type = row.program_type,
  ip.payer = row.payer,
  ip.administrator = row.administrator,
  ip.title_reference = row.title_reference,
  ip.description = row.description,
  ip.regulatory_basis = row.regulatory_basis,
  ip.eligible_entities = row.eligible_entities,
  ip.participation_requirements = row.participation_requirements,
  ip.incentive_amount = row.incentive_amount,
  ip.payment_structure = row.payment_structure,
  ip.timeline_start = row.timeline_start,
  ip.timeline_end = row.timeline_end,
  ip.meaningful_use_requirement = row.meaningful_use_requirement,
  ip.certified_ehr_requirement = row.certified_ehr_requirement,
  ip.functional_requirements = row.functional_requirements,
  ip.clinical_objectives = row.clinical_objectives,
  ip.administrative_objectives = row.administrative_objectives,
  ip.interoperability_objectives = row.interoperability_objectives,
  ip.payment_phases = row.payment_phases,
  ip.phase_1_timeline = row.phase_1_timeline,
  ip.phase_2_timeline = row.phase_2_timeline,
  ip.phase_3_timeline = row.phase_3_timeline,
  ip.documentation_requirements = row.documentation_requirements,
  ip.reporting_requirements = row.reporting_requirements,
  ip.compliance_monitoring = row.compliance_monitoring,
  ip.audit_procedures = row.audit_procedures,
  ip.success_metrics = row.success_metrics,
  ip.failure_consequences = row.failure_consequences,
  ip.program_evolution = row.program_evolution,
  ip.related_programs = row.related_programs,
  ip.priority_level = row.priority_level,
  ip.status = row.status;
"""
#meaningful_use_criterion
meaningful_use_criterion = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (muc:MeaningfulUseCriterion {criterion_id: row.criterion_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  muc.criterion_category = row.criterion_category,
  muc.criterion_name = row.criterion_name,
  muc.stage = row.stage,
  muc.program_id = row.program_id,
  muc.program_name = row.program_name,
  muc.criterion_type = row.criterion_type,
  muc.description = row.description,
  muc.regulatory_basis = row.regulatory_basis,
  muc.applicable_entities = row.applicable_entities,
  muc.measurement_approach = row.measurement_approach,
  muc.threshold_percentage = row.threshold_percentage,
  muc.core_requirement = row.core_requirement,
  muc.optional_requirement = row.optional_requirement,
  muc.clinical_objective = row.clinical_objective,
  muc.administrative_objective = row.administrative_objective,
  muc.interoperability_objective = row.interoperability_objective,
  muc.ehr_functionality_required = row.ehr_functionality_required,
  muc.data_elements_involved = row.data_elements_involved,
  muc.implementation_timeline = row.implementation_timeline,
  muc.documentation_requirements = row.documentation_requirements,
  muc.reporting_requirements = row.reporting_requirements,
  muc.compliance_verification = row.compliance_verification,
  muc.audit_procedures = row.audit_procedures,
  muc.success_metrics = row.success_metrics,
  muc.failure_consequences = row.failure_consequences,
  muc.related_measures = row.related_measures,
  muc.priority_level = row.priority_level,
  muc.status = row.status;
"""
#implementation_spec
implementation_spec = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (is:ImplementationSpec {impl_id: row.impl_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  is.impl_category = row.impl_category,
  is.impl_name = row.impl_name,
  is.impl_type = row.impl_type,
  is.owner_department = row.owner_department,
  is.related_requirement = row.related_requirement,
  is.description = row.description,
  is.regulatory_basis = row.regulatory_basis,
  is.applicable_entities = row.applicable_entities,
  is.implementation_scope = row.implementation_scope,
  is.technical_components = row.technical_components,
  is.functional_requirements = row.functional_requirements,
  is.data_handling_procedures = row.data_handling_procedures,
  is.security_measures = row.security_measures,
  is.privacy_controls = row.privacy_controls,
  is.audit_mechanisms = row.audit_mechanisms,
  is.testing_procedures = row.testing_procedures,
  is.documentation_standards = row.documentation_standards,
  is.training_requirements = row.training_requirements,
  is.deployment_approach = row.deployment_approach,
  is.timeline_phase = row.timeline_phase,
  is.go_live_readiness = row.go_live_readiness,
  is.success_criteria = row.success_criteria,
  is.failure_indicators = row.failure_indicators,
  is.rollback_procedures = row.rollback_procedures,
  is.lessons_learned = row.lessons_learned,
  is.priority_level = row.priority_level,
  is.status = row.status,
  is.related_policies = row.related_policies;
"""
#policy
policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {policy_id: row.policy_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  pol.policy_category = row.policy_category,
  pol.policy_name = row.policy_name,
  pol.policy_type = row.policy_type,
  pol.policy_owner = row.policy_owner,
  pol.regulatory_basis = row.regulatory_basis,
  pol.description = row.description,
  pol.scope = row.scope,
  pol.applicability = row.applicability,
  pol.key_objectives = row.key_objectives,
  pol.policy_framework = row.policy_framework,
  pol.core_requirements = row.core_requirements,
  pol.enforcement_mechanisms = row.enforcement_mechanisms,
  pol.compliance_procedures = row.compliance_procedures,
  pol.documentation_requirements = row.documentation_requirements,
  pol.training_requirements = row.training_requirements,
  pol.review_frequency = row.review_frequency,
  pol.approval_authority = row.approval_authority,
  pol.effective_date = row.effective_date,
  pol.last_updated = row.last_updated,
  pol.version_number = row.version_number,
  pol.related_regulations = row.related_regulations,
  pol.related_procedures = row.related_procedures,
  pol.related_standards = row.related_standards,
  pol.implementation_status = row.implementation_status,
  pol.oversight_body = row.oversight_body,
  pol.penalties_for_non_compliance = row.penalties_for_non_compliance,
  pol.exceptions_or_waivers = row.exceptions_or_waivers,
  pol.revision_history = row.revision_history,
  pol.related_policies = row.related_policies,
  pol.priority_level = row.priority_level,
  pol.status = row.status;
"""
#control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  c.control_name = row.control_name,
  c.control_category = row.control_category,
  c.control_type = row.control_type,
  c.safeguard_type = row.safeguard_type,
  c.related_requirement_ids = row.related_requirement_ids,
  c.related_policy_ids = row.related_policy_ids,
  c.related_impl_ids = row.related_impl_ids,
  c.description = row.description,
  c.primary_objective = row.primary_objective,
  c.threats_mitigated = row.threats_mitigated,
  c.data_categories_protected = row.data_categories_protected,
  c.systems_in_scope = row.systems_in_scope,
  c.processes_in_scope = row.processes_in_scope,
  c.implementation_guidance = row.implementation_guidance,
  c.monitoring_mechanisms = row.monitoring_mechanisms,
  c.owner_role = row.owner_role,
  c.responsible_department = row.responsible_department,
  c.priority_level = row.priority_level,
  c.status = row.status;
"""
#system
system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:System {system_id: row.system_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  s.system_name = row.system_name,
  s.system_category = row.system_category,
  s.system_type = row.system_type,
  s.primary_owner = row.primary_owner,
  s.supporting_owner = row.supporting_owner,
  s.description = row.description,
  s.business_function = row.business_function,
  s.phi_ehr_access = row.phi_ehr_access,
  s.data_classification = row.data_classification,
  s.criticality_level = row.criticality_level,
  s.environment_type = row.environment_type,
  s.technology_stack = row.technology_stack,
  s.deployment_model = row.deployment_model,
  s.encryption_status = row.encryption_status,
  s.backup_status = row.backup_status,
  s.audit_logging_enabled = row.audit_logging_enabled,
  s.vendor_name = row.vendor_name,
  s.version = row.version,
  s.go_live_date = row.go_live_date,
  s.last_security_audit = row.last_security_audit,
  s.compliance_certifications = row.compliance_certifications,
  s.related_controls = row.related_controls,
  s.related_policies = row.related_policies,
  s.incident_history = row.incident_history,
  s.maintenance_windows = row.maintenance_windows,
  s.support_contact = row.support_contact,
  s.disaster_recovery_plan = row.disaster_recovery_plan,
  s.backup_location = row.backup_location,
  s.status = row.status;
"""
#process
process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:Process {process_id: row.process_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  po.process_name = row.process_name,
  po.process_category = row.process_category,
  po.process_type = row.process_type,
  po.owner_role = row.owner_role,
  po.supporting_owner = row.supporting_owner,
  po.description = row.description,
  po.business_objective = row.business_objective,
  po.scope = row.scope,
  po.key_activities = row.key_activities,
  po.related_policies = row.related_policies,
  po.related_controls = row.related_controls,
  po.related_systems = row.related_systems,
  po.related_data_categories = row.related_data_categories,
  po.required_roles = row.required_roles,
  po.training_requirements = row.training_requirements,
  po.compliance_basis = row.compliance_basis,
  po.risk_mitigation = row.risk_mitigation,
  po.metrics_tracked = row.metrics_tracked,
  po.incident_history = row.incident_history,
  po.automation_status = row.automation_status,
  po.frequency_type = row.frequency_type,
  po.sla_hours = row.sla_hours,
  po.documentation_level = row.documentation_level,
  po.status = row.status;
"""
#external_framework_requirement
external_framework_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:FrameworkRequirement {framework_requirement_id: row.framework_requirement_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  f.framework_name = row.framework_name,
  f.framework_category = row.framework_category,
  f.framework_type = row.framework_type,
  f.issuing_organization = row.issuing_organization,
  f.regulatory_authority = row.regulatory_authority,
  f.requirement_description = row.requirement_description,
  f.applicability_scope = row.applicability_scope,
  f.hipaa_alignment = row.hipaa_alignment,
  f.hitech_alignment = row.hitech_alignment,
  f.related_hitech_sections = row.related_hitech_sections,
  f.related_policies = row.related_policies,
  f.related_controls = row.related_controls,
  f.related_processes = row.related_processes,
  f.data_categories_covered = row.data_categories_covered,
  f.systems_affected = row.systems_affected,
  f.compliance_status = row.compliance_status,
  f.certification_required = row.certification_required,
  f.audit_frequency = row.audit_frequency,
  f.audit_type = row.audit_type,
  f.enforcement_mechanism = row.enforcement_mechanism,
  f.penalties_for_non_compliance = row.penalties_for_non_compliance,
  f.implementation_guidance = row.implementation_guidance,
  f.best_practices = row.best_practices,
  f.current_compliance_level = row.current_compliance_level,
  f.gap_analysis = row.gap_analysis,
  f.remediation_plan = row.remediation_plan,
  f.remediation_timeline = row.remediation_timeline,
  f.responsible_owner = row.responsible_owner,
  f.supporting_teams = row.supporting_teams,
  f.framework_version = row.framework_version,
  f.effective_date = row.effective_date,
  f.next_review_date = row.next_review_date,
  f.documentation_level = row.documentation_level,
  f.status = row.status;
"""
#organization
organization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:Organization {
  organization_id: row.organization_id,
  industry_standard_regulation_id: "HITECH_ACT_2009"
})
ON CREATE SET
  o.name = row.name,
  o.org_type = row.org_type,
  o.description = row.description,
  o.npi_code = row.npi_code,
  o.location = row.location,
  o.status = "Active";
"""

#contract
contract = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Contract {
  contract_id: row.contract_id,
  industry_standard_regulation_id: "HITECH_ACT_2009"
})
ON CREATE SET
  c.name = row.name,
  c.contract_type = row.contract_type,
  c.effective_date = date(row.effective_date),
  c.expiration_date = date(row.expiration_date),
  c.key_clauses = row.key_clauses,
  c.status = "Active";
"""

#violation_tier
violation_tier = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vt:ViolationTier {
  tier_id: row.tier_id,
  industry_standard_regulation_id: "HITECH_ACT_2009"
})
ON CREATE SET
  vt.name = row.name,
  vt.culpability_level = row.culpability_level,
  vt.min_penalty_per_violation = toInteger(row.min_penalty_per_violation),
  vt.max_penalty_per_violation = toInteger(row.max_penalty_per_violation),
  vt.annual_cap = toInteger(row.annual_cap),
  vt.description = row.description;
"""

#breach_risk_assessment
breach_risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bra:BreachRiskAssessment {
  assessment_id: row.assessment_id,
  industry_standard_regulation_id: "HITECH_ACT_2009"
})
ON CREATE SET
  bra.name = row.name,
  bra.description = row.description,
  bra.factor_nature_of_phi = row.factor_1,
  bra.factor_unauthorized_person = row.factor_2,
  bra.factor_acquired_viewed = row.factor_3,
  bra.factor_mitigation = row.factor_4;
"""

#certified_ehr_technology
certified_ehr_technology = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ce:CertifiedEHRTechnology {
  tech_id: row.tech_id,
  industry_standard_regulation_id: "HITECH_ACT_2009"
})
ON CREATE SET
  ce.name = row.name,
  ce.edition = row.edition,
  ce.certification_body = row.certification_body,
  ce.mandate_year = row.mandate_year,
  ce.functional_requirements = row.functional_requirements;
"""

# Relationships
#regulation_title_rel
regulation_title_rel = """
MATCH (r:IndustryStandardAndRegulation {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (t:Title {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (r)-[:REGULATION_CONTAINS_TITLES]->(t);
"""
#title_sub_rel
title_subtitle_rel = """
MATCH (t:Title {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (s:Subtitle {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (t)-[:TITLE_CONTAINS_SUBTITLES]->(s);
"""
#subtitle_section_rel
subtitle_section_rel = """
MATCH (s:Subtitle {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sec:Section {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (t)-[:TITLE_CONTAINS_SUBTITLES]->(s);
"""
#section_requirement_rel
section_requirement_rel = """
MATCH (sec:Section {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (sec)-[:SECTION_HAS_REQUIREMENTS]->(rq);
"""
#requirement_role_rel
requirement_role_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (r:Role {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_REQUIRES_ROLE]->(r);
"""
#requirement_data_category_rel
requirement_data_category_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (d:DataCategory {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_INCLUDES_DATA_CATEGORY]->(d);
"""
#requirement_safeguard_rel
requirement_safeguard_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sg:Safeguard {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg);
"""
#requirement_event_type_rel
requirement_event_type_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (et:EventType {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE]->(et);
"""
#requirement_policy_rel
requirement_policy_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (pol:Policy {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(pol);
"""
#requirement_control_rel
requirement_control_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (c:Control {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(c);
"""
#control_system_rel
control_system_rel = """
MATCH (c:Control {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sy:System {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (c)-[:CONTROL_IMPLEMENTED_IN_SYSTEM]->(sy);
"""
#requirement_process_rel
requirement_process_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (p:Process {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_IMPACTS_PROCESS]->(p);
"""
#title_incentive_program_rel
title_incentive_program_rel = """
MATCH (t:Title {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (ip:IncentiveProgram {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (t)-[:TITLE_ESTABLISHED_INCENTIVE_PROGRAM]->(ip);
"""
#incentive_program_meaningful_use_criterion_rel
incentive_program_meaningful_use_criterion_rel = """
MATCH (ip:IncentiveProgram {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (m:MeaningfulUseCriterion {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (ip)-[:INCENTIVE_PROGRAM_USES_MEANINGFUL_USE_CRITERION]->(m);
"""
#requirement_meaningful_use_criterion_rel
requirement_meaningful_use_criterion_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (m:MeaningfulUseCriterion {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_DRIVES_MEANINGFUL_USE_CRITERION]->(m);
"""
#requirement_enforcement_action_rel
requirement_enforcement_action_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (e:EnforcementAction {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_SUBJECT_TO_ENFORCEMENT_ACTION]->(e);
"""
#section_enforcement_action_rel
section_enforcement_action_rel = """
MATCH (sec:Section {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (e:EnforcementAction {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (sec)-[:SECTION_SUBJECT_TO_ENFORCEMENT_ACTION]->(e);
"""
#requirements_implementation_spec_rel
requirements_implementation_spec_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (i:ImplementationSpec {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_HAS_IMPLEMENTATION_SPEC]->(i);
"""
#implementation_spec_control_rel
implementation_spec_control_rel = """
MATCH (i:ImplementationSpec {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (c:Control {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (i)-[:IMPLEMENTATION_SPEC_INCLUDES_CONTROL]->(c);
"""
#policy_control_rel
policy_control_rel = """
MATCH (pol:Policy {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (c:Control {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (pol)-[:POLICY_ENFORCES_CONTROL]->(c);
"""
#process_system_rel
process_system_rel = """
MATCH (po:Process {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sy:System {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (po)-[:PROCESS_INVOLVES_SYSTEM]->(sy);
"""
#requirement_external_framework_requirements_rel
requirement_external_framework_requirements_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (f:FrameworkRequirement {framework_requirement_id: "FRAMEWORK-HIPAA-PRIVACY",industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_MAPS_TO_EXTERNAL_FRAMEWORK_REQUIREMENT]->(f);
"""
#organization_role_rel
organization_role_rel = """
UNWIND [
  {source: "ORG-CE-001", target: "COVERED_ENTITY", desc: "General Mercy acts as Covered Entity"},
  {source: "ORG-BA-001", target: "BUSINESS_ASSOCIATE", desc: "CloudVault acts as Business Associate"},
  {source: "ORG-SUB-001", target: "SUBCONTRACTOR", desc: "SecureAudit acts as Subcontractor"}
] AS row
MATCH (o:Organization {organization_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (r:Role {role_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (o)-[rel:ORGANIZATION_PLAYS_ROLE]->(r)
SET rel.description = row.desc;
"""

#organization_contract_rel
organization_contract_rel = """
UNWIND [
  {source: "ORG-CE-001", target: "CTR-BAA-2024", type: "ORGANIZATION_SIGNS_CONTRACT", desc: "Hospital signs BAA with Vendor"},
  {source: "ORG-BA-001", target: "CTR-BAA-2024", type: "ORGANIZATION_BOUND_BY_CONTRACT", desc: "Vendor bound by BAA terms"},
  {source: "ORG-BA-001", target: "CTR-SUB-2024", type: "ORGANIZATION_SIGNS_CONTRACT", desc: "Vendor signs Subcontract"},
  {source: "ORG-SUB-001", target: "CTR-SUB-2024", type: "ORGANIZATION_BOUND_BY_CONTRACT", desc: "Subcontractor bound by terms"}
] AS row
MATCH (o:Organization {organization_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (c:Contract {contract_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
FOREACH (_ IN CASE WHEN row.type = 'ORGANIZATION_SIGNS_CONTRACT' THEN [1] ELSE [] END |
   MERGE (o)-[r1:ORGANIZATION_SIGNS_CONTRACT]->(c) 
   SET r1.description = row.desc
)
FOREACH (_ IN CASE WHEN row.type = 'ORGANIZATION_BOUND_BY_CONTRACT' THEN [1] ELSE [] END |
   MERGE (o)-[r2:ORGANIZATION_BOUND_BY_CONTRACT]->(c) 
   SET r2.description = row.desc
);
"""


#contract_requirement_rel
contract_requirement_rel = """
UNWIND [
  {source: "CTR-BAA-2024", target: "HITECH-13404-R1", desc: "BAA enforces breach notification"}
] AS row
MATCH (c:Contract {contract_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (req:Requirement {requirement_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (c)-[rel:CONTRACT_REQUIRES_REQUIREMENT]->(req)
SET rel.description = row.desc;
"""

#violation_tier_section_rel#
violation_tier_section_rel = """
UNWIND [
  {source: "TIER-1", target: "13410", desc: "Tier 1 defined in Enforcement section"}
] AS row
MATCH (vt:ViolationTier {tier_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sec:Section {section_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (vt)-[rel:VIOLATION_TIER_DEFINES_SECTION]->(sec)
SET rel.description = row.desc;
"""
#violation_tier_enforcement_rel
violation_tier_enforcement_rel = """
UNWIND [
  {source: "TIER-4", target: "EA-CIVIL-OCR-P1", desc: "Tier 4 triggers max penalty"}
] AS row
MATCH (vt:ViolationTier {tier_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (ea:EnforcementAction {enforcement_action_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (vt)-[rel:VIOLATION_TIER_TRIGGERS_ENFORCEMENT]->(ea)
SET rel.description = row.desc;
"""



#breach_risk_assessment_event_rel
breach_risk_assessment_event_rel = """
UNWIND [
  {source: "BRA-4FACTOR", target: "BREACH", desc: "Assessment evaluates breach event"}
] AS row
MATCH (bra:BreachRiskAssessment {assessment_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (evt:EventType {event_type_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (bra)-[rel:BREACH_EVALUATES_EVENT]->(evt)
SET rel.description = row.desc;
"""
#breach_risk_assessment_safeguard_rel
breach_risk_assessment_safeguard_rel = """
UNWIND [
  {source: "BRA-4FACTOR", target: "SG-A-RISK-ASSESSMENT", desc: "Assessment supports risk management"}
] AS row
MATCH (bra:BreachRiskAssessment {assessment_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sg:Safeguard {safeguard_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (bra)-[rel:BREACH_RISK_ASSESSMENT_MITIGATES_RISK]->(sg)
SET rel.description = row.desc;
"""

#ehr_tech_rel
ehr_tech_rel = """
UNWIND [
  {source: "CEHRT-2015", target: "MU3-HIE-EXCHANGE", desc: "Tech supports Stage 3 criteria"}
] AS row
MATCH (ce:CertifiedEHRTechnology {tech_id: row.source, industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (muc:MeaningfulUseCriterion {criterion_id: row.target, industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (ce)-[rel:CERTIFIED_IN_MEANINGFUL_SUPPORTS_CRITERION]->(muc)
SET rel.description = row.desc;
"""
# Link HITECH Regulation to all Certified Tech
hitech_rel_ehr_tech_framework = """
MATCH (framework:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITECH_ACT_2009'})
MATCH (ce:CertifiedEHRTechnology)
WHERE NOT (framework)-[:REGULATION_CERTIFIES_TECH]->(ce)
MERGE (framework)-[:REGULATION_CERTIFIES_TECH]->(ce);
"""
# Link HITECH Regulation to all Organizations
hitech_rel_organization_framework = """
MATCH (framework:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITECH_ACT_2009'})
MATCH (o:Organization)
WHERE NOT (framework)-[:REGULATION_GOVERNS_ORGANIZATION]->(o)
MERGE (framework)-[:REGULATION_GOVERNS_ORGANIZATION]->(o);
"""
# Link HITECH Regulation to all Violation Tiers
hitech_rel_violation_tier_framework = """
MATCH (framework:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITECH_ACT_2009'})
MATCH (vt:ViolationTier)
WHERE NOT (framework)-[:REGULATION_DEFINES_PENALTY_TIER]->(vt)
MERGE (framework)-[:REGULATION_DEFINES_PENALTY_TIER]->(vt);
"""
# Link HITECH Regulation to all Roles
hitech_rel_roles_framework = """
MATCH (framework:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITECH_ACT_2009'})
MATCH (r:Role)
WHERE NOT (framework)-[:REGULATION_DEFINES_ROLE]->(r)
MERGE (framework)-[:REGULATION_DEFINES_ROLE]->(r);
"""
# Link HITECH Regulation to all Frameworks
#hitech_rel_framework_framework
hitech_rel_framework_framework = """
MATCH (framework:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITECH_ACT_2009'})
MATCH (f:FrameworkRequirement)
WHERE NOT (framework)-[:REGULATION_DEFINES_FRAMEWORK_REQUIREMENT]->(f)
MERGE (framework)-[:REGULATION_DEFINES_FRAMEWORK_REQUIREMENT]->(f);
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

client.query(regulation)
time.sleep(2)

client.query(title.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Titles.csv'))
time.sleep(2)

client.query(subtitle.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Subtitles.csv'))
time.sleep(2)

client.query(section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Sections.csv'))
time.sleep(2)

client.query(requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH%20-%20Requirements.csv'))
time.sleep(2)

client.query(role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Roles.csv'))
time.sleep(2)

client.query(data_category.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_DataCategories.csv'))
time.sleep(2)

client.query(safeguard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Safeguards.csv'))
time.sleep(2)

client.query(event_type.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_EventTypes.csv'))
time.sleep(2)

client.query(enforcement_action.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_EnforcementActions.csv'))
time.sleep(2)

client.query(incentive_program.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_IncentivePrograms.csv'))
time.sleep(2)

client.query(meaningful_use_criterion.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_MeaningfulUseCriteria.csv'))
time.sleep(2)

client.query(implementation_spec.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_ImplementationSpecs.csv'))
time.sleep(2)

client.query(policy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Policies.csv'))
time.sleep(2)

client.query(control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Controls.csv'))
time.sleep(2)

client.query(system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Systems.csv'))
time.sleep(2)


client.query(process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Processes.csv'))
time.sleep(2)

client.query(external_framework_requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_ExternalFrameworkRequirements.csv'))  
time.sleep(2)

client.query(organization.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/organization.csv"))
time.sleep(2)

client.query(contract.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/contract.csv"))
time.sleep(2)

client.query(violation_tier.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/violation_tier.csv"))
time.sleep(2)

client.query(breach_risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/breach_risk_assessment.csv"))
time.sleep(2)

client.query(certified_ehr_technology.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH%20-%20Certified%20EHR.csv"))
time.sleep(2)

#Relationships
client.query(regulation_title_rel)
time.sleep(2)

client.query(title_subtitle_rel)
time.sleep(2)

client.query(subtitle_section_rel)
time.sleep(2)   

client.query(section_requirement_rel)
time.sleep(2)

client.query(requirement_role_rel)
time.sleep(2)

client.query(requirement_data_category_rel)
time.sleep(2)   

client.query(requirement_safeguard_rel)
time.sleep(2)   

client.query(requirement_event_type_rel)    
time.sleep(2)   

client.query(requirement_policy_rel)    
time.sleep(2)

client.query(requirement_control_rel)
time.sleep(2)   

client.query(control_system_rel)
time.sleep(2)

client.query(requirement_process_rel)
time.sleep(2)

client.query(title_incentive_program_rel)
time.sleep(2)

client.query(incentive_program_meaningful_use_criterion_rel)
time.sleep(2)

client.query(requirement_meaningful_use_criterion_rel)
time.sleep(2)

client.query(requirement_enforcement_action_rel)
time.sleep(2)


client.query(section_enforcement_action_rel)
time.sleep(2)


client.query(requirements_implementation_spec_rel)
time.sleep(2)


client.query(implementation_spec_control_rel)
time.sleep(2)


client.query(policy_control_rel)
time.sleep(2)


client.query(process_system_rel)
time.sleep(2)


client.query(requirement_external_framework_requirements_rel)
time.sleep(2)


client.query(organization_role_rel)
time.sleep(2)

client.query(organization_contract_rel)
time.sleep(2)

client.query(contract_requirement_rel)
time.sleep(2)

client.query(violation_tier_section_rel)
time.sleep(2)

client.query(violation_tier_enforcement_rel)
time.sleep(2)

client.query(breach_risk_assessment_event_rel)
time.sleep(2)

client.query(breach_risk_assessment_safeguard_rel)
time.sleep(2)

client.query(ehr_tech_rel)
time.sleep(2)

client.query(hitech_rel_ehr_tech_framework)
time.sleep(2)

client.query(hitech_rel_organization_framework)
time.sleep(2)

client.query(hitech_rel_violation_tier_framework)
time.sleep(2)

client.query(hitech_rel_roles_framework)
time.sleep(2)

client.query(hitech_rel_framework_framework)
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
    with open('hitech.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to hitech.json")
else:
    logger.error("No data returned from the query.")

client.close()











