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
MERGE (p:Policy {policy_id: row.policy_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  p.policy_category = row.policy_category,
  p.policy_name = row.policy_name,
  p.policy_type = row.policy_type,
  p.policy_owner = row.policy_owner,
  p.regulatory_basis = row.regulatory_basis,
  p.description = row.description,
  p.scope = row.scope,
  p.applicability = row.applicability,
  p.key_objectives = row.key_objectives,
  p.policy_framework = row.policy_framework,
  p.core_requirements = row.core_requirements,
  p.enforcement_mechanisms = row.enforcement_mechanisms,
  p.compliance_procedures = row.compliance_procedures,
  p.documentation_requirements = row.documentation_requirements,
  p.training_requirements = row.training_requirements,
  p.review_frequency = row.review_frequency,
  p.approval_authority = row.approval_authority,
  p.effective_date = row.effective_date,
  p.last_updated = row.last_updated,
  p.version_number = row.version_number,
  p.related_regulations = row.related_regulations,
  p.related_procedures = row.related_procedures,
  p.related_standards = row.related_standards,
  p.implementation_status = row.implementation_status,
  p.oversight_body = row.oversight_body,
  p.penalties_for_non_compliance = row.penalties_for_non_compliance,
  p.exceptions_or_waivers = row.exceptions_or_waivers,
  p.revision_history = row.revision_history,
  p.related_policies = row.related_policies,
  p.priority_level = row.priority_level,
  p.status = row.status;
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
MERGE (p:Process {process_id: row.process_id,industry_standard_regulation_id: "HITECH_ACT_2009"})
ON CREATE SET
  p.process_name = row.process_name,
  p.process_category = row.process_category,
  p.process_type = row.process_type,
  p.owner_role = row.owner_role,
  p.supporting_owner = row.supporting_owner,
  p.description = row.description,
  p.business_objective = row.business_objective,
  p.scope = row.scope,
  p.key_activities = row.key_activities,
  p.related_policies = row.related_policies,
  p.related_controls = row.related_controls,
  p.related_systems = row.related_systems,
  p.related_data_categories = row.related_data_categories,
  p.required_roles = row.required_roles,
  p.training_requirements = row.training_requirements,
  p.compliance_basis = row.compliance_basis,
  p.risk_mitigation = row.risk_mitigation,
  p.metrics_tracked = row.metrics_tracked,
  p.incident_history = row.incident_history,
  p.automation_status = row.automation_status,
  p.frequency_type = row.frequency_type,
  p.sla_hours = row.sla_hours,
  p.documentation_level = row.documentation_level,
  p.status = row.status;
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
MATCH (po:Policy {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (rq)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(po);
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
MATCH (po:Policy {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (c:Control {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (po)-[:POLICY_ENFORCES_CONTROL]->(c);
"""
#process_system_rel
process_system_rel = """
MATCH (p:Process {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (sy:System {industry_standard_regulation_id: "HITECH_ACT_2009"})
MERGE (p)-[:PROCESS_INVOLVES_SYSTEM]->(sy);
"""
#requirement_external_framework_requirements_rel
requirement_external_framework_requirements_rel = """
MATCH (rq:Requirement {industry_standard_regulation_id: "HITECH_ACT_2009"})
MATCH (efr:ExternalFrameworkRequirement {framework_requirement_id: "FRAMEWORK-HIPAA-PRIVACY"})
MERGE (rq)-[:REQUIREMENT_MAPS_TO_EXTERNAL_FRAMEWORK_REQUIREMENT]->(efr);
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

client.query(requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirements.csv'))
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

client.query(regulation_title_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Regulation_Titles.csv'))
time.sleep(2)

client.query(title_subtitle_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Title_Subtitles.csv'))
time.sleep(2)

client.query(subtitle_section_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Subtitle_Sections.csv'))
time.sleep(2)   

client.query(section_requirement_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Section_Requirements.csv'))
time.sleep(2)

client.query(requirement_role_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Roles.csv'))
time.sleep(2)

client.query(requirement_data_category_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Data.csv'))
time.sleep(2)   

client.query(requirement_safeguard_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Safeguards.csv'))
time.sleep(2)   

client.query(requirement_event_type_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Events.csv'))    
time.sleep(2)   

client.query(requirement_policy_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Policies.csv'))    
time.sleep(2)

client.query(requirement_control_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Controls.csv'))
time.sleep(2)   

client.query(control_system_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Control_Systems.csv'))
time.sleep(2)

client.query(requirement_process_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Processes.csv'))
time.sleep(2)

client.query(title_incentive_program_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Title_IncentivePrograms.csv'))
time.sleep(2)

client.query(incentive_program_meaningful_use_criterion_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_IncentiveProgram_MeaningfulUseCriteria.csv'))
time.sleep(2)

client.query(requirement_meaningful_use_criterion_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_MeaningfulUseCriteria.csv'))
time.sleep(2)

client.query(requirement_enforcement_action_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Enforcement.csv'))
time.sleep(2)

client.query(section_enforcement_action_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Section_Enforcement.csv'))
time.sleep(2)

client.query(requirements_implementation_spec_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_ImplementationSpecs.csv'))
time.sleep(2)

client.query(implementation_spec_control_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_ImplementationSpec_Controls.csv'))
time.sleep(2)

client.query(policy_control_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Policy_Controls.csv'))
time.sleep(2)

client.query(process_system_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Process_Systems.csv'))
time.sleep(2)

client.query(requirement_external_framework_requirements_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITECH/HITECH_Requirement_Mapping.csv'))
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
with open('hitech.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to hitech.json")


client.close()










