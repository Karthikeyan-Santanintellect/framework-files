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

#Title
title ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Title {title_id: row.title_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    t.number = row.title_number,
    t.name = row.title_name,
    t.citation = row.legal_citation,
    t.jurisdiction = row.jurisdiction;
"""
# Article
article ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Article {article_id: row.article_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    a.number = row.article_number,
    a.name = row.article_name,
    a.citation = row.legal_citation,
    a.jurisdiction = row.jurisdiction,
    a.parent_title_id = row.parent_title_id;
  """
# Part
part ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Part {node_id: row.node_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET   
    p.number = row.part_number,
    p.name = row.part_name,
    p.citation = row.legal_citation,
    p.effective_date = row.effective_date,
    p.parent_article_id = row.parent_article_id;
"""
# Section
section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Section {section_id: row.section_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    s.number = row.section_number,
    s.name = row.section_name,
    s.type = row.section_type,
    s.citation = row.legal_citation,
    s.summary = row.summary,
    s.key_provisions = row.key_provisions,
    s.parent_part_id = row.parent_part_id;
"""
#Rule
rule ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ru:Rule {rule_id: row.rule_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
    ru.number = row.rule_number,
    ru.name = row.rule_name,
    ru.requirement = row.rule_requirement,
    ru.effective_date = row.effective_date,
    ru.authority = row.regulatory_authority,
    ru.parent_section_id = row.parent_section_id;
"""
#Definition
definition ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Definition {definition_id: row.definition_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    d.term = row.term,
    d.text = row.definition_text,
    d.citation = row.legal_citation,
    d.cross_references = row.cross_references,
    d.defined_by_section_id = row.defined_by_section_id;
  """
#Consumer Rights
consumer_rights ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:ConsumerRight {
  node_id: row.node_id,
  regional_standard_regulation_id: row.regional_standard_regulation_id
})
ON CREATE SET
  ct.name = row.right_name,
  ct.type = row.right_type,
  ct.legal_citation = row.legal_citation,
  ct.right_description = row.right_description,
  ct.response_deadline_days = row.response_deadline_days,
  ct.extension_allowed_days = row.extension_allowed_days,
  ct.no_account_required = row.no_account_required,
  ct.no_cost_to_consumer = row.no_cost_to_consumer,
  ct.max_free_requests_per_year = row.max_free_requests_per_year,
  ct.appeal_process_required = row.appeal_process_required,
  ct.ag_notification_required_if_denied = row.ag_notification_required_if_denied,
  ct.established_by_section_id = row.established_by_section_id;
"""
#Opt-Out Rights
opt_out_rights ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oor:OptOutRight {
  node_id: row.node_id,
  regional_standard_regulation_id: row.regional_standard_regulation_id
})
ON CREATE SET
  oor.type = row.opt_out_type,
  oor.description = row.opt_out_description,
  oor.legal_citation = row.legal_citation,
  oor.uoom_applicable =  row.uoom_applicable,
  oor.response_timeframe = row.response_timeframe,
  oor.parent_consumer_right_id = row.parent_consumer_right_id;
  """
#Controller Duties
controller_duties = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cld:ControllerDuty {node_id: row.node_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  cld.name = row.duty_name,
  cld.type = row.duty_type,
  cld.legal_citation = row.legal_citation,
  cld.description = row.duty_description,
  cld.mandatory = row.mandatory,
  cld.applicable_to = row.applicable_to,
  cld.penalty_for_violation = row.penalty_for_violation,
  cld.imposed_by_section_or_rule_id = row.imposed_by_section_or_rule_id;
"""
#Enforcement Authority
enforcement_authority ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAuthority {authority_id: row.authority_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    ea.name = row.authority_name,
    ea.type = row.authority_type,
    ea.jurisdiction = row.jurisdiction,
    ea.citation = row.legal_citation,
    ea.powers = row.enforcement_powers,
    ea.contact = row.contact_info,
    ea.cure_period_status = row.cure_period_status;
  """
#Civil Penalty
civil_penalty ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cp:CivilPenalty {
  node_id: row.node_id,
  regional_standard_regulation_id: row.regional_standard_regulation_id
})
ON CREATE SET
  cp.penalty_name = row.penalty_name,
  cp.max_amount_per_violation = row.max_amount_per_violation,
  cp.currency = row.currency,
  cp.legal_citation = row.legal_citation,
  cp.penalty_framework = row.penalty_framework,
  cp.seekable_by = row.seekable_by,
  cp.discretionary_cure_period = row.discretionary_cure_period,
  cp.mandatory_cure_period_ended = row.mandatory_cure_period_ended;
  """
#Applicability Threshold
applicability_threshold ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (at:ApplicabilityThreshold {
  node_id: row.node_id,
  regional_standard_regulation_id: row.regional_standard_regulation_id
})
ON CREATE SET
  at.name = row.threshold_name,
  at.type = row.threshold_type,
  at.consumer_count_threshold = toInteger(row.consumer_count_threshold),
  at.revenue_condition = row.revenue_condition,
  at.legal_citation = row.legal_citation,
  at.applicability_test = row.applicability_test,
  at.defined_by_section_id = row.defined_by_section_id;
"""
#Data Processing Agreement Template
data_processing_agreement_template ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpt:DataProcessingAgreementTemplate {dpa_template_id: row.dpa_template_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    dpt.name = row.dpa_name,
    dpt.citation = row.legal_citation,
    dpt.mandatory_terms = row.mandatory_terms,
    dpt.type = row.contract_type,
    dpt.enforceable = row.enforceable,
    dpt.defined_by_section_id = row.defined_by_section_id;
"""
#Universal Opt-Out Mechanism
universal_opt_out_mechanism ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (uoom:UniversalOptOutMechanism {uoom_id: row.uoom_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    uoom.name = row.uoom_name,
    uoom.type = row.mechanism_type,
    uoom.technical_standard = row.technical_standard,
    uoom.examples = row.examples,
    uoom.mandatory_date = row.mandatory_compliance_date,
    uoom.citation = row.legal_citation,
    uoom.applicable_activities = row.applicable_activities,
    uoom.response_timeframe = row.response_timeframe,
    uoom.account_required = row.account_required,
    uoom.single_request = row.single_request_mechanism,
    uoom.defined_by_rule_id = row.defined_by_rule_id;
  """
#De-identified Data
de_identified_data ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dd:DeidentifiedData {deidentified_data_id: row.node_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    dd.name = row.data_class_name,
    dd.citation = row.legal_citation,
    dd.cpa_status = row.cpa_coverage_status,
    dd.definition = row.definition,
    dd.technical_requirements = row.technical_requirements,
    dd.organizational_requirements = row.organizational_requirements,
    dd.defined_by_section_id = row.defined_by_section_id;
  """
#Third Party
third_party ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tp:ThirdParty {third_party_id: row.third_party_id, regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET 
    tp.name = row.actor_name,
    tp.citation = row.legal_citation,
    tp.definition = row.definition,
    tp.relationships = row.relationships_to_other_actors,
    tp.obligations = row.cpa_direct_obligations,
    tp.controller_liability = row.controller_liability,
    tp.defined_by_section_id = row.defined_by_section_id;
  """


#consent node
consent ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cd:ConsentRecord {consent_id: row.consent_id,regional_standard_regulation_id: 'CPA 1.0'})
ON CREATE SET
  cd.type = row.consent_type,
  cd.date = row.consent_date,
  cd.method = row.consent_method,
  cd.status = row.consent_status,
  cd.expiration_date = row.consent_expiration_date,
  cd.last_refresh_date = row.last_refresh_date,
  cd.refresh_required = row.refresh_required,
  cd.specificity_level = row.specificity_level,
  cd.informed_status = row.informed_status,
  cd.freely_given = row.freely_given,
  cd.unambiguous_agreement = row.unambiguous_agreement,
  cd.dark_pattern_used = row.dark_pattern_used,
  cd.withdrawal_date = row.withdrawal_date,
  cd.consent_proof_documentation = row.consent_proof_documentation;
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
MERGE (sd:SensitiveData {
  node_id: row.node_id,
  regional_standard_regulation_id: row.regional_standard_regulation_id
})
ON CREATE SET
  sd.name = row.category_name,
  sd.description = row.category_description,
  sd.legal_citation = row.legal_citation,
  sd.consent_required = row.consent_required,
  sd.parental_consent_age_threshold = row.parental_consent_age_threshold,
  sd.specific_consent_needed = row.specific_consent_needed,
  sd.classification_level = row.classification_level,
  sd.processing_restrictions = row.processing_restrictions,
  sd.security_requirements = row.security_requirements;
"""

#Relationships

#Regulation → Title
regulation_title ="""
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (t:Title {title_id: 'TITLE-6', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (reg)-[:REGULATION_HAS_TITLE]->(t);
"""
#Title → Article
title_article ="""
MATCH (t:Title {title_id: 'TITLE-6', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (a:Article {article_id: 'ARTICLE-1', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (t)-[:TITLE_CONTAINS_ARTICLE]->(a);
"""
#Article → Part
article_part = """
MATCH (a:Article {article_id: 'ARTICLE-1', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (p:Part {node_id: 'PART-13', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (a)-[:ARTICLE_CONTAINS_PART]->(p);
"""
#Part → Sections
part_section ="""
MATCH (p:Part {node_id: 'PART-13', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (s:Section {regional_standard_regulation_id: 'CPA 1.0'})
WHERE s.section_id IN ['SECTION-6-1-1301', 'SECTION-6-1-1302', 'SECTION-6-1-1303', 
                          'SECTION-6-1-1304', 'SECTION-6-1-1305', 'SECTION-6-1-1306',
                          'SECTION-6-1-1307', 'SECTION-6-1-1308', 'SECTION-6-1-1309',
                          'SECTION-6-1-1310', 'SECTION-6-1-1311', 'SECTION-6-1-1312', 'SECTION-6-1-1313']
MERGE (p)-[:PART_CONTAINS_SECTION]->(s);
"""
#Regulation → Rules
regulation_rule ="""
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ru:Rule {regional_standard_regulation_id: 'CPA 1.0'})
WHERE ru.rule_id IN ['RULE-5-01', 'RULE-6-02', 'RULE-7-03', 'RULE-8-01']
MERGE (reg)-[:REGULATION_GOVERNED_BY_RULE]->(ru);
"""
#Sections → Rules
section_rule ="""
UNWIND [
  {s:'SECTION-6-1-1306', ru:'RULE-5-01'},
  {s:'SECTION-6-1-1305', ru:'RULE-6-02'},
  {s:'SECTION-6-1-1308', ru:'RULE-7-03'},
  {s:'SECTION-6-1-1308', ru:'RULE-8-01'}
] AS pair
MATCH (s:Section {section_id: pair.s, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (r:Rule {rule_id: pair.ru, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_IMPLEMENTED_BY_RULE]->(r);
"""
# Section → Definitions
section_definition ="""
UNWIND [
  'DEF-PERSONAL-DATA',
  'DEF-SENSITIVE-DATA',
  'DEF-SALE',
  'DEF-CONTROLLER',
  'DEF-PROCESSOR',
  'DEF-CONSUMER',
  'DEF-TARGETED-ADVERTISING',
  'DEF-PROFILING',
  'DEF-CONSENT',
  'DEF-DEIDENTIFIED-DATA',
  'DEF-PROCESS',
  'DEF-THIRD-PARTY',
  'DEF-UOOM'
] AS def_id
MATCH (s:Section {section_id: 'SECTION-6-1-1303', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (d:Definition {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_DEFINES_DEFINITION]->(d);
"""

# Section → Consumer Rights
section_consumer_rights ="""
UNWIND [
  'RIGHT-ACCESS',
  'RIGHT-CORRECT',
  'RIGHT-DELETE',
  'RIGHT-PORTABILITY',
  'RIGHT-OPT-OUT'
] AS right_id
MATCH (s:Section {section_id: 'SECTION-6-1-1306', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ct:ConsumerRight {node_id: right_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_GRANTS_RIGHT]->(ct);
"""
# Consumer Right -> Opt Out Right 
consumer_right_opt_out_right ="""
UNWIND [
  'OPT-OUT-TARGETED-ADS',
  'OPT-OUT-SALE',
  'OPT-OUT-PROFILING'
] AS oor_id
MATCH (cr:ConsumerRight {node_id: 'RIGHT-OPT-OUT', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (oor:OptOutRight {node_id: oor_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (cr)-[:CONSUMER_RIGHT_INCLUDES_OPT_OUT_RIGHT]->(oor);
"""
# Consumer Request -> Consumer Right
consumer_request_consumer_right ="""
WITH [
  {request_id: 'REQ-001', node_id: 'RIGHT-ACCESS'},
  {request_id: 'REQ-003', node_id: 'RIGHT-CORRECT'},
  {request_id: 'REQ-002', node_id: 'RIGHT-DELETE'},
  {request_id: 'REQ-004', node_id: 'RIGHT-PORTABILITY'},
  {request_id: 'REQ-005', node_id: 'RIGHT-OPT-OUT'},
  {request_id: 'REQ-006', node_id: 'RIGHT-ACCESS'}
] AS mappings

UNWIND mappings AS mapping

MATCH (cr:ConsumerRequest {request_id: mapping.request_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ct:ConsumerRight {node_id: mapping.node_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (cr)-[:CONSUMER_REQUEST_EXERCISES_RIGHT]->(ct);
"""

#OptOutMechanism → OptOutRight
opt_out_mechanism_opt_out_right ="""
WITH [
  {mechanism_id: 'OPTOUT-001', right_node_id: 'OPT-OUT-SALE'},
  {mechanism_id: 'OPTOUT-002', right_node_id: 'OPT-OUT-TARGETED-ADS'},
  {mechanism_id: 'OPTOUT-003', right_node_id: 'OPT-OUT-PROFILING'}
] AS mappings

UNWIND mappings AS mapping

MATCH (oom:OptOutMechanism {
  mechanism_id: mapping.mechanism_id, 
  regional_standard_regulation_id: 'CPA 1.0'
})
MATCH (oor:OptOutRight {
  node_id: mapping.right_node_id,
  regional_standard_regulation_id: 'CPA 1.0'
})
MERGE (oom)-[:OPT_OUT_MECHANISM_ENABLES_OPT_OUT_RIGHT]->(oor);
"""
# Section → ControllerDuty
section_controller_duty ="""
UNWIND [
  {s:'SECTION-6-1-1305', cld:'DUTY-PROVIDE-NOTICE'},
  {s:'SECTION-6-1-1306', cld:'DUTY-HONOR-OPT-OUT'},
  {s:'SECTION-6-1-1306', cld:'DUTY-RESPOND-RIGHTS-REQUESTS'},
  {s:'SECTION-6-1-1308', cld:'DUTY-MINIMIZATION'},
  {s:'SECTION-6-1-1308', cld:'DUTY-AVOID-SECONDARY-USE'},
  {s:'SECTION-6-1-1308', cld:'DUTY-OBTAIN-CONSENT'}
] AS pair
MATCH (s:Section {section_id: pair.s, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cld:ControllerDuty {node_id: pair.cld, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_IMPOSES_DUTY]->(cld);
"""

#  Regulation → EnforcementAuthority
regulation_enforcement_authority ="""
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'CPA 1.0'})
WHERE ea.authority_id IN ['AG-001', 'AG-002']
MERGE (reg)-[:REGULATION_ENFORCED_BY_ENFORCEMENT_AUTHORITY]->(ea);
"""
# EnforcementAuthority → CivilPenalty
enforcement_authority_civil_penalty ="""
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cp:CivilPenalty {node_id: 'PENALTY-001', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (ea)-[:ENFORCEMENT_AUTHORITY_CAN_IMPOSE_PENALTY]->(cp);
"""
#Section  → EnforcementAuthority
section_enforcement_authority ="""
MATCH (s:Section {section_id: 'SECTION-6-1-1311', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_GRANTS_AUTHORITY]->(ea);
"""
#Section  → CivilPenalty
section_civil_penalty = """
MATCH (s:Section {section_id: 'SECTION-6-1-1311', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cp:CivilPenalty {node_id: 'PENALTY-001', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_ESTABLISHES_PENALTY]->(cp);
"""

# Section  → ApplicabilityThreshold
section_applicability_threshold ="""
MATCH (s:Section {section_id: 'SECTION-6-1-1302', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (at:ApplicabilityThreshold {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_DEFINES_THRESHOLD]->(at);
"""
# Section → DPA Template
section_dpa_template ="""
MATCH (s:Section {section_id: 'SECTION-6-1-1302', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dpt:DataProcessingAgreementTemplate {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_REQUIRES_DPA_TEMPLATE]->(dpt);
"""
# DataProcessor → DPA Template
data_processor_dpa_template ="""
MATCH (dp:DataProcessor {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dpt:DataProcessingAgreementTemplate {dpa_template_id: 'DPA-TEMPLATE-001', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (dp)-[:SECTION_BOUND_BY_DPA_TEMPLATE]->(dpt);
"""
# Rule → UniversalOptOutMechanism
rule_universal_opt_out_mechanism ="""
MATCH (ru:Rule {rule_id: 'RULE-5-01', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (uoom:UniversalOptOutMechanism {uoom_id: 'UOOM-001', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (ru)-[:RULE_REQUIRES_UOOM]->(uoom);
"""
# UniversalOptOutMechanism → Right to Opt Out
universal_opt_out_mechanism_right_to_opt_out ="""
MATCH (uoom:UniversalOptOutMechanism {uoom_id: 'UOOM-001', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (ct:ConsumerRight {node_id: 'RIGHT-OPT-OUT', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (uoom)-[:UNIVERSAL_OPT_OUT_MECHANISM_ENABLES_RIGHT]->(ct);
"""

#DeidentifiedData → Definition
deidentified_definition ="""
MATCH (dd:DeidentifiedData {
  deidentified_data_id: 'DEIDENT-001',   
  regional_standard_regulation_id: 'CPA 1.0'
})
MATCH (d:Definition {
  definition_id: 'DEF-DEIDENTIFIED',
  regional_standard_regulation_id: 'CPA 1.0'
})
MERGE (dd)-[:DATA_DEFINED_BY_DEFINITION]->(d);
"""
#ThirdParty → Definition
third_party_definition ="""
MATCH (tp:ThirdParty {third_party_id:'THIRD-PARTY-001', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (d:Definition {definition_id:'DEF-THIRD-PARTY', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (tp)-[:THIRD_PARTY_DEFINES_DEFINITION]->(d);
"""
#Section  → SensitiveData 
section_sensitive_data ="""
MATCH (s:Section {section_id: 'SECTION-6-1-1304', regional_standard_regulation_id: 'CPA 1.0'})
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (s)-[:SECTION_REQUIRES_CONSENT_FOR_SENSITIVE_DATA]->(sd);
"""

#ProcessingActivity → SensitiveData
processing_activity_sensitive_data ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_PROCESSES_SENSITIVE_DATA]->(sd); 
"""
#ConsentRecord → SensitiveData
consent_record_sensitive_data ="""
MATCH (cd:ConsentRecord {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (sd:SensitiveData {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (cd)-[:CONSENT_RECORD_GRANTS_CONSENT_FOR_SENSITIVE_DATA]->(sd);  
"""

#consumer -> consumer Right
consumer_right ="""
MATCH (c:Consumer {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cr:ConsumerRight {regional_standard_regulation_id: 'CPA 1.0'})
MERGE (c)-[:CONSUMER_HAS_RIGHT]->(cr);
"""
#ProcessingActivity → DPA (REQUIRES_DPA)
processing_activity_dpa ="""
WITH [
  {activity_id: 'ACT-002', dpa_id: 'DPA-001'},
  {activity_id: 'ACT-003', dpa_id: 'DPA-002'},
  {activity_id: 'ACT-004', dpa_id: 'DPA-003'},
  {activity_id: 'ACT-006', dpa_id: 'DPA-004'},
  {activity_id: 'ACT-002', dpa_id: 'DPA-005'}
] AS mappings
UNWIND mappings AS mapping
MATCH (pa:ProcessingActivity {activity_id: mapping.activity_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (dpa:DataProtectionAssessment {dpa_id: mapping.dpa_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (pa)-[:PROCESSING_ACTIVITY_REQUIRES_DPA]->(dpa);
"""
#DataBreach → Section
data_breach_section ="""
MATCH (db:DataBreachIncident {regional_standard_regulation_id: 'CPA 1.0'})
MATCH (s:Section {section_id: 'SECTION-6-1-1308', regional_standard_regulation_id: 'CPA 1.0'})
MERGE (db)-[:DATA_BREACH_OCCURRED_IN_SECTION]->(s);
"""
##Consumer → PersonalData
consumer_personal_data ="""
WITH [
  {data_id: 'PD-001', consumer_id: 'CON-001'},
  {data_id: 'PD-002', consumer_id: 'CON-001'},
  {data_id: 'PD-003', consumer_id: 'CON-001'},
  {data_id: 'PD-004', consumer_id: 'CON-001'},
  {data_id: 'PD-005', consumer_id: 'CON-001'},
  {data_id: 'PD-006', consumer_id: 'CON-001'},
  {data_id: 'PD-007', consumer_id: 'CON-002'},
  {data_id: 'PD-008', consumer_id: 'CON-001'}
] AS mappings
UNWIND mappings AS mapping
MATCH (cons:Consumer {consumer_id: mapping.consumer_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (pd:PersonalDataRecord {data_id: mapping.data_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (cons)-[:CONSUMER_OWNS_PERSONAL_DATA]->(pd);
"""
#PrivacyNotice → ConsumerRight
privacy_notice_consumer_right ="""
WITH [
  {notice_id: 'NOTICE-001', node_ids: ['RIGHT-ACCESS', 'RIGHT-DELETE', 'RIGHT-CORRECT', 'RIGHT-PORTABILITY', 'RIGHT-OPT-OUT']},
  {notice_id: 'NOTICE-002', node_ids: ['RIGHT-OPT-OUT']},
  {notice_id: 'NOTICE-003', node_ids: ['RIGHT-OPT-OUT']},
  {notice_id: 'NOTICE-004', node_ids: ['RIGHT-DELETE']}
] AS mappings
UNWIND mappings AS mapping
UNWIND mapping.node_ids AS node_id
MATCH (pn:PrivacyNotice {notice_id: mapping.notice_id, regional_standard_regulation_id: 'CPA 1.0'})
MATCH (cr:ConsumerRight {node_id: node_id, regional_standard_regulation_id: 'CPA 1.0'})
MERGE (pn)-[:PRIVACY_NOTICE_DISCLOSES_RIGHT]->(cr);
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

client.query(title.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Title_nodes.csv"))
time.sleep(2)

client.query(article.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Article_nodes.csv"))
time.sleep(2)

client.query(part.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Part_nodes.csv"))
time.sleep(2)

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Section_nodes.csv"))
time.sleep(2)

client.query(rule.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Rule_nodes.csv"))
time.sleep(2)

client.query(definition.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Definition_nodes.csv"))
time.sleep(2)

client.query(consumer_rights.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ConsumerRight_CORRECTED.csv"))
time.sleep(2)

client.query(opt_out_rights.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_OptOutRight_CORRECTED.csv"))
time.sleep(2)

client.query(controller_duties.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ControllerDuty_CORRECTED.csv"))
time.sleep(2)

client.query(enforcement_authority.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_EnforcementAuthority_nodes.csv"))
time.sleep(2)

client.query(civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_CivilPenalty_CORRECTED.csv"))
time.sleep(2)

client.query(applicability_threshold.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ApplicabilityThreshold_CORRECTED.csv"))
time.sleep(2)

client.query(data_processing_agreement_template.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataProcessingAgreementTemplate_nodes.csv"))
time.sleep(2)

client.query(universal_opt_out_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_UniversalOptOutMechanism_nodes.csv"))
time.sleep(2)

client.query(de_identified_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DeidentifiedData_nodes.csv"))
time.sleep(2)

client.query(third_party.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ThirdParty_nodes.csv"))
time.sleep(2)



client.query(consent.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Consent_nodes.csv"))
time.sleep(2)

client.query(consumer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_Consumer_nodes.csv"))
time.sleep(2)

client.query(consumer_request.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_ConsumerRequest_nodes.csv"))
time.sleep(2)

client.query(data_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_DataBreach_nodes.csv"))
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

client.query(sensitive_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPA/CPA_SensitiveData_Complete.csv"))
time.sleep(2)


#Relationships
client.query(regulation_title)
time.sleep(2)

client.query(title_article)
time.sleep(2)

client.query(article_part)
time.sleep(2)

client.query(part_section)
time.sleep(2)

client.query(regulation_rule)
time.sleep(2)

client.query(section_rule)
time.sleep(2)

client.query(section_definition)
time.sleep(2)

client.query(section_consumer_rights)
time.sleep(2)

client.query(consumer_right_opt_out_right)
time.sleep(2)

client.query(consumer_request_consumer_right)
time.sleep(2)

client.query(opt_out_mechanism_opt_out_right)
time.sleep(2)

client.query(section_controller_duty)
time.sleep(2)


client.query(regulation_enforcement_authority)
time.sleep(2)

client.query(enforcement_authority_civil_penalty)
time.sleep(2)

client.query(section_enforcement_authority)
time.sleep(2)

client.query(section_civil_penalty)
time.sleep(2)


client.query(section_applicability_threshold)
time.sleep(2)

client.query(section_dpa_template)
time.sleep(2)


client.query(data_processor_dpa_template)
time.sleep(2)

client.query(rule_universal_opt_out_mechanism)
time.sleep(2)

client.query(universal_opt_out_mechanism_right_to_opt_out)
time.sleep(2)

client.query(deidentified_definition)
time.sleep(2)

client.query(third_party_definition)
time.sleep(2)


client.query(section_sensitive_data)
time.sleep(2)

client.query(processing_activity_sensitive_data)
time.sleep(2)

client.query(consent_record_sensitive_data)
time.sleep(2)

client.query(consumer_right)
time.sleep(2)

client.query(processing_activity_dpa)
time.sleep(2)



client.query(data_breach_section)
time.sleep(2)

client.query(consumer_personal_data)
time.sleep(2)

client.query(privacy_notice_consumer_right)
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
    with open('cpa.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to cpa.json")
else:
    logger.error("No data returned from the query.")

client.close()
