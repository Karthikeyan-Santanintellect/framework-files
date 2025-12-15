#Regulation 
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'TDPSA'})
ON CREATE SET
    reg.name = "Texas Data Privacy and Security Act ",
    reg.version = "2023",
    reg.status = "Active",
    reg.jurisdiction = "Texas, United States",
    reg.effective_date = date("2024-07-01"),
    reg.enactment_date = date("2023-06-18"),
    reg.description = "Comprehensive state consumer data privacy law that regulates the collection, use, processing, and sale of personal data of Texas residents. Grants consumers rights to access, correct, delete, and port their personal data, and to opt-out of targeted advertising, data sales, and profiling. Requires businesses to obtain consent for processing sensitive data and conduct data protection assessments for high-risk processing activities.";
"""

#Business_entity
business_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (be:BusinessEntity {regional_standard_regulation_id: 'TDPSA', entity_id: row.entity_id})
ON CREATE SET
    be.legal_name = row.legal_name,
    be.entity_type = row.entity_type,
    be.industry_classification = row.industry_classification,
    be.employee_count = toInteger(row.employee_count),
    be.annual_revenue = toFloat(row.annual_revenue),
    be.sba_small_business_status = toBoolean(row.sba_small_business_status),
    be.gdpr_tdpsa_compliance_status = toBoolean(row.gdpr_tdpsa_compliance_status),
    be.data_controller_designation = toBoolean(row.data_controller_designation),
    be.data_processor_designation = toBoolean(row.data_processor_designation),
    be.registration_date = date(row.registration_date),
    be.headquarters_location = row.headquarters_location,
    be.texas_operations_presence = toBoolean(row.texas_operations_presence),
    be.personal_data_processing = toBoolean(row.personal_data_processing),
    be.sensitive_data_processing = toBoolean(row.sensitive_data_processing),
    be.children_data_processing = toBoolean(row.children_data_processing),
    be.targeted_advertising_processing = toBoolean(row.targeted_advertising_processing),
    be.personal_data_sale = toBoolean(row.personal_data_sale),
    be.profiling_processing = toBoolean(row.profiling_processing),
    be.last_compliance_audit_date = date(row.last_compliance_audit_date),
    be.compliance_status = row.compliance_status,
    be.designated_compliance_officer = row.designated_compliance_officer
ON MATCH SET
    be.last_compliance_audit_date = date(row.last_compliance_audit_date),
    be.compliance_status = row.compliance_status,
    be.employee_count = toInteger(row.employee_count),
    be.annual_revenue = toFloat(row.annual_revenue),
    be.gdpr_tdpsa_compliance_status = toBoolean(row.gdpr_tdpsa_compliance_status);
"""

#Consumer 
consumer = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Consumer {regional_standard_regulation_id: 'TDPSA', consumer_id: row.consumer_id})
ON CREATE SET
    c.texas_residency_status = toBoolean(row.texas_residency_status),
    c.age_group = row.age_group,
    c.known_child_status = toBoolean(row.known_child_status),
    c.parental_consent_obtained = toBoolean(row.parental_consent_obtained),
    c.contact_email = row.contact_email,
    c.contact_phone = row.contact_phone,
    c.request_history_count = toInteger(row.request_history_count),
    c.last_request_date = date(row.last_request_date),
    c.request_types = row.request_types,
    c.opt_out_status = toBoolean(row.opt_out_status),
    c.universal_opt_out_signal_status = toBoolean(row.universal_opt_out_signal_status),
    c.opt_out_categories = row.opt_out_categories,
    c.data_breach_affected = toBoolean(row.data_breach_affected),
    c.breach_notification_date = CASE WHEN row.breach_notification_date = '' THEN null ELSE date(row.breach_notification_date) END,
    c.dispute_status = toBoolean(row.dispute_status),
    c.dispute_type = row.dispute_type,
    c.discrimination_complaint = toBoolean(row.discrimination_complaint),
    c.right_to_access = toBoolean(row.right_to_access),
    c.right_to_correct = toBoolean(row.right_to_correct),
    c.right_to_delete = toBoolean(row.right_to_delete),
    c.right_to_portability = toBoolean(row.right_to_portability),
    c.right_to_appeal = toBoolean(row.right_to_appeal),
    c.compliance_requirement_met = toBoolean(row.compliance_requirement_met),
    c.last_interaction_date = date(row.last_interaction_date),
    c.response_received = toBoolean(row.response_received),
    c.satisfaction_rating = toInteger(row.satisfaction_rating),
    c.has_legal_representative = toBoolean(row.has_legal_representative),
    c.record_created_date = date(row.record_created_date),
    c.record_updated_date = date(row.record_updated_date),
    c.account_status = row.account_status;
"""

#Personal_data
personal_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pd:PersonalData {regional_standard_regulation_id: 'TDPSA', data_id: row.data_id})
ON CREATE SET
    pd.data_category = row.data_category,
    pd.classification_level = row.classification_level,
    pd.is_sensitive_data = toBoolean(row.is_sensitive_data),
    pd.collection_method = row.collection_method,
    pd.collection_purpose = row.collection_purpose,
    pd.disclosed_to_consumer = toBoolean(row.disclosed_to_consumer),
    pd.processing_purpose = row.processing_purpose,
    pd.compatible_with_disclosed = toBoolean(row.compatible_with_disclosed),
    pd.consent_required = toBoolean(row.consent_required),
    pd.consent_obtained = toBoolean(row.consent_obtained),
    pd.consent_date = CASE WHEN row.consent_date = '' THEN null ELSE datetime(row.consent_date) END,
    pd.retention_period_days = toInteger(row.retention_period_days),
    pd.third_party_sharing = toBoolean(row.third_party_sharing),
    pd.third_party_categories = split(row.third_party_categories, ','),
    pd.security_classification = row.security_classification;
"""

#Sensitive_data 
sensitive_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sd:SensitiveData {regional_standard_regulation_id: 'TDPSA', sensitive_id: row.sensitive_id})
ON CREATE SET
    sd.data_type = row.data_type,
    sd.description = row.description,
    sd.protection_level = row.protection_level,
    sd.encryption_required = toBoolean(row.encryption_required),
    sd.access_restricted = toBoolean(row.access_restricted),
    sd.audit_frequency_months = toInteger(row.audit_frequency_months),
    sd.parental_consent_for_children = toBoolean(row.parental_consent_for_children),
    sd.usage_restrictions = row.usage_restrictions,
    sd.sale_permitted = toBoolean(row.sale_permitted),
    sd.sale_notice_provided = toBoolean(row.sale_notice_provided),
    sd.location_radius_feet = toInteger(row.location_radius_feet),
    sd.processing_justified = toBoolean(row.processing_justified),
    sd.risk_assessment_conducted = toBoolean(row.risk_assessment_conducted),
    sd.risk_level = row.risk_level;
"""

#Datacategory 
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id: 'TDPSA', category_id: row.category_id})
ON CREATE SET
    dc.category_name = row.category_name,
    dc.category_code = row.category_code,
    dc.description = row.description,
    dc.requires_consent = toBoolean(row.requires_consent),
    dc.gdpr_equivalent = row.gdpr_equivalent,
    dc.special_handling_required = toBoolean(row.special_handling_required),
    dc.examples = row.examples,
    dc.consumer_visibility = toBoolean(row.consumer_visibility),
    dc.retention_guidance_months = toInteger(row.retention_guidance_months),
    dc.audit_frequency_months = toInteger(row.audit_frequency_months);
"""

#processing_activity 
processing_activity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {regional_standard_regulation_id: 'TDPSA', activity_id: row.activity_id})
ON CREATE SET
    pa.activity_name = row.activity_name,
    pa.processing_type = row.processing_type,
    pa.description = row.description,
    pa.disclosed_purpose = row.disclosed_purpose,
    pa.compatible_purpose = toBoolean(row.compatible_purpose),
    pa.data_categories_involved = split(row.data_categories_involved, ';'),
    pa.consumer_notice_provided = toBoolean(row.consumer_notice_provided),
    pa.consent_required = toBoolean(row.consent_required),
    pa.consent_obtained = toBoolean(row.consent_obtained),
    pa.dpa_required = toBoolean(row.dpa_required),
    pa.dpa_completed = toBoolean(row.dpa_completed),
    pa.risk_level = row.risk_level,
    pa.increased_risk_of_harm = toBoolean(row.increased_risk_of_harm),
    pa.processor_involved = toBoolean(row.processor_involved),
    pa.processor_contract_signed = toBoolean(row.processor_contract_signed),
    pa.data_retention_days = toInteger(row.data_retention_days),
    pa.deletion_process_established = toBoolean(row.deletion_process_established),
    pa.compliance_status = row.compliance_status;
"""
#consent
consent = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Consent {regional_standard_regulation_id: 'TDPSA', consent_id: row.consent_id})
ON CREATE SET
    co.consent_timestamp = datetime(row.consent_timestamp),
    co.affirmative_action_taken = toBoolean(row.affirmative_action_taken),
    co.consent_type = row.consent_type,
    co.consent_valid = toBoolean(row.consent_valid),
    co.dark_pattern_used = toBoolean(row.dark_pattern_used),
    co.consent_method = row.consent_method,
    co.scope_of_consent = row.scope_of_consent,
    co.expiration_date = CASE 
        WHEN row.expiration_date = '' OR row.expiration_date IS NULL 
        THEN null 
        ELSE date(row.expiration_date) 
    END,
    co.revocation_allowed = toBoolean(row.revocation_allowed),
    co.revocation_method = [method IN split(row.revocation_method, ';') | trim(method)],
    co.renewal_needed = toBoolean(row.renewal_needed),
    co.renewal_date = CASE 
        WHEN row.renewal_date = '' OR row.renewal_date IS NULL 
        THEN null 
        ELSE date(row.renewal_date) 
    END,
    co.compliance_with_coppa = toBoolean(row.compliance_with_coppa),
    co.parental_verification_completed = toBoolean(row.parental_verification_completed),
    co.freely_given = toBoolean(row.freely_given),
    co.specific = toBoolean(row.specific),
    co.informed = toBoolean(row.informed),
    co.consumer_can_withdraw = toBoolean(row.consumer_can_withdraw);
"""



#privacy_notice 
privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PrivacyNotice {regional_standard_regulation_id: 'TDPSA', notice_id: row.notice_id})
ON CREATE SET
    pn.notice_version = row.notice_version,
    pn.effective_date = date(row.effective_date),
    pn.last_updated_date = date(row.last_updated_date),
    pn.notice_format = row.notice_format,
    pn.notice_accessibility = toBoolean(row.notice_accessibility),
    pn.notice_clarity = row.notice_clarity,
    pn.categories_disclosed = toBoolean(row.categories_disclosed),
    pn.purposes_disclosed = toBoolean(row.purposes_disclosed),
    pn.third_party_sharing_disclosed = toBoolean(row.third_party_sharing_disclosed),
    pn.third_party_categories_disclosed = toBoolean(row.third_party_categories_disclosed),
    pn.consumer_rights_explained = toBoolean(row.consumer_rights_explained),
    pn.appeal_process_described = toBoolean(row.appeal_process_described),
    pn.request_submission_methods = toBoolean(row.request_submission_methods),
    pn.sensitive_data_notice_included = toBoolean(row.sensitive_data_notice_included),
    pn.sensitive_data_sale_notice = row.sensitive_data_sale_notice,
    pn.biometric_data_sale_notice = row.biometric_data_sale_notice,
    pn.targeted_advertising_notice = toBoolean(row.targeted_advertising_notice),
    pn.opt_out_mechanism_described = toBoolean(row.opt_out_mechanism_described),
    pn.universal_opt_out_supported = toBoolean(row.universal_opt_out_supported),
    pn.consumer_request_deadline = toInteger(row.consumer_request_deadline),
    pn.extension_possibility_explained = toBoolean(row.extension_possibility_explained),
    pn.free_requests_explained = toBoolean(row.free_requests_explained),
    pn.language_versions = row.language_versions,
    pn.compliance_verified = toBoolean(row.compliance_verified),
    pn.last_compliance_review_date = date(row.last_compliance_review_date);
"""

#Data_protection_assessment 
data_protection_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpa:DataProtectionAssessment {regional_standard_regulation_id: 'TDPSA', assessment_id: row.assessment_id})
ON CREATE SET
    dpa.assessment_type = row.assessment_type,
    dpa.assessment_date = date(row.assessment_date),
    dpa.assigned_to = row.assigned_to,
    dpa.processing_activity_ref = row.processing_activity_ref,
    dpa.scope_description = row.scope_description,
    dpa.benefits_identified = row.benefits_identified,
    dpa.risks_identified = row.risks_identified,
    dpa.unfair_treatment_risk = toBoolean(row.unfair_treatment_risk),
    dpa.disparate_impact_risk = toBoolean(row.disparate_iconsumer_requestmpact_risk),
    dpa.financial_harm_risk = toBoolean(row.financial_harm_risk),
    dpa.physical_harm_risk = toBoolean(row.physical_harm_risk),
    dpa.reputation_harm_risk = toBoolean(row.reputation_harm_risk),
    dpa.seclusion_intrusion_risk = toBoolean(row.seclusion_intrusion_risk),
    dpa.substantial_injury_risk = toBoolean(row.substantial_injury_risk),
    dpa.deidentification_used = toBoolean(row.deidentification_used),
    dpa.consumer_expectations_considered = toBoolean(row.consumer_expectations_considered),
    dpa.processing_context_considered = toBoolean(row.processing_context_considered),
    dpa.relationship_considered = toBoolean(row.relationship_considered),
    dpa.mitigating_safeguards_identified = row.mitigating_safeguards_identified,
    dpa.safeguards_sufficient = toBoolean(row.safeguards_sufficient),
    dpa.overall_risk_assessment = row.overall_risk_assessment,
    dpa.recommendations = row.recommendations,
    dpa.remediation_required = toBoolean(row.remediation_required),
    dpa.remediation_deadline = CASE 
        WHEN row.remediation_deadline = '' OR row.remediation_deadline IS NULL 
        THEN null 
        ELSE date(row.remediation_deadline) 
    END,
    dpa.attorney_general_accessible = toBoolean(row.attorney_general_accessible),
    dpa.assessment_documentation_complete = toBoolean(row.assessment_documentation_complete),
    dpa.compliant_with_other_laws = toBoolean(row.compliant_with_other_laws);
"""

#consumer_request
consumer_request = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cr:ConsumerRequest {regional_standard_regulation_id: 'TDPSA', request_id: row.request_id})
ON CREATE SET
    cr.request_type = row.request_type,
    cr.request_submission_date = datetime(row.request_submission_date),
    cr.submission_method = row.submission_method,
    cr.consumer_identification = row.consumer_identification,
    cr.authorized_agent_status = toBoolean(row.authorized_agent_status),
    cr.agent_authorization_verified = toBoolean(row.agent_authorization_verified),
    cr.authentication_method = row.authentication_method,
    cr.authentication_successful = toBoolean(row.authentication_successful),
    cr.authentication_date = date(row.authentication_date),
    cr.processing_status = row.processing_status,
    cr.response_deadline = date(row.response_deadline),
    cr.extension_needed = toBoolean(row.extension_needed),
    cr.extension_date = CASE 
        WHEN row.extension_date = '' OR row.extension_date IS NULL 
        THEN null 
        ELSE date(row.extension_date) 
    END,
    cr.response_date = CASE 
        WHEN row.response_date = '' OR row.response_date IS NULL 
        THEN null 
        ELSE date(row.response_date) 
    END,
    cr.response_method = CASE 
        WHEN row.response_method = '' OR row.response_method IS NULL 
        THEN null 
        ELSE row.response_method 
    END,
    cr.free_request_count = toInteger(row.free_request_count),
    cr.fee_charged = toBoolean(row.fee_charged),
    cr.completion_status = CASE 
        WHEN row.completion_status = '' OR row.completion_status IS NULL 
        THEN null 
        ELSE toBoolean(row.completion_status) 
    END,
    cr.consumer_satisfied = CASE 
        WHEN row.consumer_satisfied = '' OR row.consumer_satisfied IS NULL 
        THEN null 
        ELSE toBoolean(row.consumer_satisfied) 
    END,
    cr.appeal_submitted = toBoolean(row.appeal_submitted),
    cr.appeal_deadline = CASE 
        WHEN row.appeal_deadline = '' OR row.appeal_deadline IS NULL 
        THEN null 
        ELSE date(row.appeal_deadline) 
    END;
"""



#Data_processor 
data_processor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dp:DataProcessor {regional_standard_regulation_id: 'TDPSA', processor_id: row.processor_id})
ON CREATE SET
    dp.processor_name = row.processor_name,
    dp.processor_type = row.processor_type,
    dp.contract_signed_date = date(row.contract_signed_date),
    dp.contract_status = row.contract_status,
    dp.processing_instructions_provided = toBoolean(row.processing_instructions_provided),
    dp.instruction_clarity = row.instruction_clarity,
    dp.purpose_nature_agreed = row.purpose_nature_agreed,
    dp.data_types_processed = row.data_types_processed,
    dp.processing_duration_months = toInteger(row.processing_duration_months),
    dp.rights_obligations_documented = toBoolean(row.rights_obligations_documented),
    dp.confidentiality_required = toBoolean(row.confidentiality_required),
    dp.confidentiality_enforcement = toBoolean(row.confidentiality_enforcement),
    dp.subprocessor_prohibition = toBoolean(row.subprocessor_prohibition),
    dp.subprocessor_contracts_conforming = toBoolean(row.subprocessor_contracts_conforming),
    dp.data_deletion_required = toBoolean(row.data_deletion_required),
    dp.data_return_required = toBoolean(row.data_return_required),
    dp.compliance_cooperation = toBoolean(row.compliance_cooperation),
    dp.assessment_allowed = toBoolean(row.assessment_allowed),
    dp.audit_frequency_months = toInteger(row.audit_frequency_months),
    dp.information_provision_commitment = toBoolean(row.information_provision_commitment),
    dp.processor_reliability = row.processor_reliability,
    dp.security_certifications = row.security_certifications,
    dp.prior_breach_history = toBoolean(row.prior_breach_history),
    dp.last_security_audit_date = date(row.last_security_audit_date),
    dp.suspension_reason = CASE 
        WHEN row.suspension_reason = '' OR row.suspension_reason IS NULL 
        THEN null 
        ELSE row.suspension_reason 
    END,
    dp.termination_date = CASE 
        WHEN row.termination_date = '' OR row.termination_date IS NULL 
        THEN null 
        ELSE date(row.termination_date) 
    END,
    dp.data_legacy_period_days = toInteger(row.data_legacy_period_days);
"""

#Data_breach 
data_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (db:DataBreach {regional_standard_regulation_id: 'TDPSA', breach_id: row.breach_id})
ON CREATE SET
    db.discovery_date = datetime(row.discovery_date),
    db.occurrence_date = datetime(row.occurrence_date),
    db.notification_deadline_date = date(row.notification_deadline_date),
    db.notification_completed_date = date(row.notification_completed_date),
    db.breach_type = row.breach_type,
    db.cause_description = row.cause_description,
    db.affected_consumer_count = toInteger(row.affected_consumer_count),
    db.data_types_compromised = row.data_types_compromised,
    db.sensitive_data_compromised = toBoolean(row.sensitive_data_compromised),
    db.encryption_status_bypassed = toBoolean(row.encryption_status_bypassed),
    db.investigation_status = row.investigation_status,
    db.investigation_completion_date = date(row.investigation_completion_date),
    db.notification_method = row.notification_method,
    db.credit_monitoring_offered = toBoolean(row.credit_monitoring_offered),
    db.system_hardening_date = date(row.system_hardening_date),
    db.regulatory_notification_required = toBoolean(row.regulatory_notification_required),
    db.attorney_general_notified = toBoolean(row.attorney_general_notified),
    db.notification_letter_filed = toBoolean(row.notification_letter_filed),
    db.cost_incurred = toFloat(row.cost_incurred),
    db.legal_action_threatened = toBoolean(row.legal_action_threatened),
    db.class_action_filed = toBoolean(row.class_action_filed),
    db.consent_decree_issued = toBoolean(row.consent_decree_issued),
    db.fines_imposed = toFloat(row.fines_imposed),
    db.public_disclosure_required = toBoolean(row.public_disclosure_required),
    db.lessons_learned = row.lessons_learned;
"""

#opt_out_mechanism
opt_out_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (om:OptOutMechanism {regional_standard_regulation_id: 'TDPSA', optout_id: row.optout_id})
ON CREATE SET
    om.optout_type = row.optout_type,
    om.optout_method = row.optout_method,
    om.optout_request_date = datetime(row.optout_request_date),
    om.optout_effective_date = date(row.optout_effective_date),
    om.universal_opt_out_signal = toBoolean(row.universal_opt_out_signal),
    om.signal_type = CASE 
        WHEN row.signal_type = '' OR row.signal_type IS NULL OR row.signal_type = 'None'
        THEN null 
        ELSE row.signal_type 
    END,
    om.signal_verified = toBoolean(row.signal_verified),
    om.commercial_reasonableness = toBoolean(row.commercial_reasonableness),
    om.optout_confirmation_provided = toBoolean(row.optout_confirmation_provided),
    om.optout_scope_explained = row.optout_scope_explained,
    om.optout_duration = row.optout_duration,
    om.optout_revocation_allowed = toBoolean(row.optout_revocation_allowed),
    om.revocation_method = row.revocation_method,
    om.enforcement_status = toBoolean(row.enforcement_status),
    om.violation_date = CASE 
        WHEN row.violation_date = '' OR row.violation_date IS NULL 
        THEN null 
        ELSE date(row.violation_date) 
    END,
    om.violation_description = CASE 
        WHEN row.violation_description = '' OR row.violation_description IS NULL 
        THEN null 
        ELSE row.violation_description 
    END,
    om.consumer_notification_sent = toBoolean(row.consumer_notification_sent),
    om.remediation_completed = toBoolean(row.remediation_completed),
    om.remediation_date = CASE 
        WHEN row.remediation_date = '' OR row.remediation_date IS NULL 
        THEN null 
        ELSE date(row.remediation_date) 
    END;
"""


#Compliance audit 
compliance_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ca:ComplianceAudit {regional_standard_regulation_id: 'TDPSA', audit_id: row.audit_id})
ON CREATE SET
    ca.audit_type = row.audit_type,
    ca.audit_start_date = date(row.audit_start_date),
    ca.audit_completion_date = date(row.audit_completion_date),
    ca.audit_scope = row.audit_scope,
    ca.conducted_by = row.conducted_by,
    ca.focus_areas = row.focus_areas,
    ca.audit_results = row.audit_results,
    ca.tdpsa_compliance_checked = toBoolean(row.tdpsa_compliance_checked),
    ca.findings_count = toInteger(row.findings_count),
    ca.critical_findings = toInteger(row.critical_findings),
    ca.major_findings = toInteger(row.major_findings),
    ca.minor_findings = toInteger(row.minor_findings),
    ca.findings_summary = row.findings_summary,
    ca.risk_assessment_conducted = toBoolean(row.risk_assessment_conducted),
    ca.identified_risks = row.identified_risks,
    ca.remediation_recommended = toBoolean(row.remediation_recommended),
    ca.remediation_plan_deadline = CASE 
        WHEN row.remediation_plan_deadline = '' OR row.remediation_plan_deadline IS NULL 
        THEN null 
        ELSE date(row.remediation_plan_deadline) 
    END,
    ca.remediation_plan_submitted = toBoolean(row.remediation_plan_submitted),
    ca.remediation_plan_accepted = toBoolean(row.remediation_plan_accepted),
    ca.remediation_completion_date = CASE 
        WHEN row.remediation_completion_date = '' OR row.remediation_completion_date IS NULL 
        THEN null 
        ELSE date(row.remediation_completion_date) 
    END,
    ca.full_compliance_achieved = toBoolean(row.full_compliance_achieved),
    ca.repeat_violations = toBoolean(row.repeat_violations),
    ca.audit_report_filed = toBoolean(row.audit_report_filed),
    ca.regulatory_follow_up_required = toBoolean(row.regulatory_follow_up_required),
    ca.continuous_monitoring_implemented = toBoolean(row.continuous_monitoring_implemented),
    ca.next_audit_date = date(row.next_audit_date);
"""

#Process_consumer_rel
process_consumer_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:Consumer {consumer_id: row.target_consumer_id})
MERGE (source)-[r:PROCESSES_CONSUMER_DATA {
    source_id: row.source_entity_id,
    target_id: row.target_consumer_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.relationship_start_date = date(row.relationship_start_date),
    r.relationship_status = row.relationship_status,
    r.data_processing_scope = split(row.data_processing_scope, ';'),
    r.legal_basis = row.legal_basis,
    r.processing_established = toBoolean(row.processing_established),
    r.consent_obtained = toBoolean(row.consent_obtained),
    r.consent_date = CASE 
        WHEN row.consent_date = '' OR row.consent_date IS NULL 
        THEN null 
        ELSE date(row.consent_date) 
    END;
"""

#collects_personal_data
collects_personal_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:PersonalData {data_id: row.target_data_id})
MERGE (source)-[r:COLLECTS_PERSONAL_DATA {
    source_id: row.source_entity_id,
    target_id: row.target_data_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.collection_date = date(row.collection_date),
    r.collection_method = row.collection_method,
    r.frequency = row.frequency,
    r.disclosed_purpose = row.disclosed_purpose,
    r.purpose_legitimate = toBoolean(row.purpose_legitimate),
    r.minimization_applied = toBoolean(row.minimization_applied);
"""

#Process_sensitive_data
process_sensitive_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:SensitiveData {sensitive_id: row.target_sensitive_id})
MERGE (source)-[r:PROCESSES_SENSITIVE_DATA {
    source_id: row.source_entity_id,
    target_id: row.target_sensitive_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.processing_start_date = date(row.processing_start_date),
    r.explicit_consent_obtained = date(row.explicit_consent_obtained),
    r.consent_scope = row.consent_scope,
    r.protection_level_applied = row.protection_level_applied,
    r.encryption_enabled = toBoolean(row.encryption_enabled),
    r.access_restrictions = row.access_restrictions,
    r.audit_frequency_months = toInteger(row.audit_frequency_months);
"""

#obtains_consent_data - FIXED: Target should be Consent, not Consumer
obtains_consent_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:Consent {consent_id: row.target_consent_id})
MERGE (source)-[r:OBTAINS_CONSENT {
    source_id: row.source_entity_id,
    target_id: row.target_consent_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.consent_request_date = date(row.consent_request_date),
    r.consent_granted_date = date(row.consent_granted_date),
    r.consent_type = row.consent_type,
    r.dark_pattern_avoided = toBoolean(row.dark_pattern_avoided),
    r.freely_given = toBoolean(row.freely_given),
    r.specific_purpose_consented = row.specific_purpose_consented,
    r.consent_valid = toBoolean(row.consent_valid);
"""

#Conducts_processing_activity - FIXED: Renamed variable
conducts_processing_activity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:ProcessingActivity {activity_id: row.target_activity_id})
MERGE (source)-[r:CONDUCTS_PROCESSING_ACTIVITY {
    source_id: row.source_entity_id,
    target_id: row.target_activity_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.activity_start_date = date(row.activity_start_date),
    r.activity_end_date = CASE WHEN row.activity_end_date = '' THEN null ELSE date(row.activity_end_date) END,
    r.disclosed_to_consumer = toBoolean(row.disclosed_to_consumer),
    r.consent_required = toBoolean(row.consent_required),
    r.consent_obtained = toBoolean(row.consent_obtained),
    r.dpa_completed = toBoolean(row.dpa_completed),
    r.compliance_status = row.compliance_status;
"""

#requires_data_protection_assessment - FIXED: Changed dpa_id to assessment_id
requires_data_protection_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:ProcessingActivity {activity_id: row.source_activity_id})
MATCH (target:DataProtectionAssessment {assessment_id: row.target_dpa_id})
MERGE (source)-[r:REQUIRES_DATA_PROTECTION_ASSESSMENT {
    source_id: row.source_activity_id,
    target_id: row.target_dpa_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.assessment_requirement_date = date(row.assessment_requirement_date),
    r.assessment_type = row.assessment_type,
    r.assessment_required_reason = row.assessment_required_reason,
    r.assessment_completed = toBoolean(row.assessment_completed),
    r.assessment_date = CASE WHEN row.assessment_date = '' THEN null ELSE date(row.assessment_date) END,
    r.risk_identified = toBoolean(row.risk_identified),
    r.risk_level = row.risk_level;
"""

#respond_consumer_request
respond_consumer_request = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:ConsumerRequest {request_id: row.target_request_id})
MERGE (source)-[r:RESPONDS_TO_CONSUMER_REQUEST {
    source_id: row.source_entity_id,
    target_id: row.target_request_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.response_deadline = date(row.response_deadline),
    r.response_date = CASE WHEN row.response_date = '' THEN null ELSE date(row.response_date) END,
    r.response_method = row.response_method,
    r.extension_requested = toBoolean(row.extension_requested),
    r.extension_granted = toBoolean(row.extension_granted),
    r.extended_deadline = CASE WHEN row.extended_deadline = '' THEN null ELSE date(row.extended_deadline) END,
    r.request_fulfilled = toBoolean(row.request_fulfilled);
"""

#uses_data_processor
uses_data_processor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:DataProcessor {processor_id: row.target_processor_id})
MERGE (source)-[r:USES_DATA_PROCESSOR {
    source_id: row.source_entity_id,
    target_id: row.target_processor_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.contract_date = date(row.contract_date),
    r.contract_effective_date = date(row.contract_effective_date),
    r.contract_status = row.contract_status,
    r.processing_instructions_clear = toBoolean(row.processing_instructions_clear),
    r.confidentiality_binding = toBoolean(row.confidentiality_binding),
    r.tdpsa_compliant_contract = toBoolean(row.tdpsa_compliant_contract),
    r.subprocessor_agreement_required = toBoolean(row.subprocessor_agreement_required),
    r.audit_rights_included = toBoolean(row.audit_rights_included);
"""

#offers_privacy_notice
offers_privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:PrivacyNotice {notice_id: row.target_notice_id})
MERGE (source)-[r:OFFERS_PRIVACY_NOTICE {
    source_id: row.source_entity_id,
    target_id: row.target_notice_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.notice_date = date(row.notice_date),
    r.notice_version = row.notice_version,
    r.notice_accessible = toBoolean(row.notice_accessible),
    r.notice_clear = toBoolean(row.notice_clear),
    r.all_required_elements = toBoolean(row.all_required_elements),
    r.consumer_acknowledged = toBoolean(row.consumer_acknowledged),
    r.acknowledgment_date = CASE WHEN row.acknowledgment_date = '' THEN null ELSE date(row.acknowledgment_date) END;
"""

#PROVIDES_OPT_OUT_MECHANISM
provides_opt_out_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:OptOutMechanism {mechanism_id: row.target_mechanism_id})
MERGE (source)-[r:PROVIDES_OPT_OUT_MECHANISM {
    source_id: row.source_entity_id,
    target_id: row.target_mechanism_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.mechanism_implementation_date = date(row.mechanism_implementation_date),
    r.mechanism_types = row.mechanism_types,
    r.consumer_friendly = toBoolean(row.consumer_friendly),
    r.easy_to_use = toBoolean(row.easy_to_use),
    r.universal_opt_out_supported = toBoolean(row.universal_opt_out_supported),
    r.gpc_support_enabled = CASE WHEN row.gpc_support_enabled = '' THEN null ELSE date(row.gpc_support_enabled) END,
    r.merchant_reasonableness_standard = toBoolean(row.merchant_reasonableness_standard);
"""

#EXPERIENCES_DATA_BREACH
experiences_data_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:Consumer {consumer_id: row.source_consumer_id})
MATCH (target:DataBreach {breach_id: row.target_breach_id})
MERGE (source)-[r:EXPERIENCES_DATA_BREACH {
    source_id: row.source_consumer_id,
    target_id: row.target_breach_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.breach_date = date(row.breach_date),
    r.notification_sent_date = CASE WHEN row.notification_sent_date = '' THEN null ELSE date(row.notification_sent_date) END,
    r.data_compromised = row.data_compromised,
    r.financial_impact = toFloat(row.financial_impact),
    r.identity_theft_risk = toBoolean(row.identity_theft_risk),
    r.credit_monitoring_offered = toBoolean(row.credit_monitoring_offered),
    r.legal_action_status = row.legal_action_status;
"""

#UNDERGOES_COMPLIANCE_AUDIT
undergoes_compliance_audit = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {entity_id: row.source_entity_id})
MATCH (target:ComplianceAudit {audit_id: row.target_audit_id})
MERGE (source)-[r:UNDERGOES_COMPLIANCE_AUDIT {
    source_id: row.source_entity_id,
    target_id: row.target_audit_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.audit_initiation_date = date(row.audit_initiation_date),
    r.audit_start_date = date(row.audit_start_date),
    r.audit_completion_date = date(row.audit_completion_date),
    r.audit_type = row.audit_type,
    r.findings_count = toInteger(row.findings_count),
    r.remediation_required = toBoolean(row.remediation_required),
    r.remediation_deadline = CASE WHEN row.remediation_deadline = '' THEN null ELSE date(row.remediation_deadline) END,
    r.compliance_achieved = toBoolean(row.compliance_achieved);
"""

#EXERCISES_CONSUMER_RIGHT
exercises_consumer_right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:Consumer {consumer_id: row.source_consumer_id})
MATCH (target:ConsumerRequest {request_id: row.target_request_id})
MERGE (source)-[r:EXERCISES_CONSUMER_RIGHT {
    source_id: row.source_consumer_id,
    target_id: row.target_request_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.request_date = date(row.request_date),
    r.right_exercised = row.right_exercised,
    r.request_authenticated = toBoolean(row.request_authenticated),
    r.request_fulfilled = toBoolean(row.request_fulfilled),
    r.fulfillment_date = CASE WHEN row.fulfillment_date = '' THEN null ELSE date(row.fulfillment_date) END,
    r.free_request_used = toBoolean(row.free_request_used),
    r.fee_charged = toBoolean(row.fee_charged),
    r.appeal_available = toBoolean(row.appeal_available);
"""
#personal_data_belongs_to_category
personal_data_belongs_to_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:PersonalData {regional_standard_regulation_id: 'TDPSA', data_id: row.source_data_id})
MATCH (target:DataCategory {regional_standard_regulation_id: 'TDPSA', category_id: row.target_category_id})
MERGE (source)-[r:BELONGS_TO_CATEGORY {
    source_id: row.source_data_id,
    target_id: row.target_category_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.classification_date = date(row.classification_date),
    r.primary_category = toBoolean(row.primary_category);
"""

#sensitive_data_belongs_to_category
sensitive_data_belongs_to_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:SensitiveData {regional_standard_regulation_id: 'TDPSA', sensitive_id: row.source_sensitive_id})
MATCH (target:DataCategory {regional_standard_regulation_id: 'TDPSA', category_id: row.target_category_id})
MERGE (source)-[r:BELONGS_TO_CATEGORY {
    source_id: row.source_sensitive_id,
    target_id: row.target_category_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.classification_date = date(row.classification_date),
    r.sensitive_category_type = row.sensitive_category_type;
"""

#governed_by
governed_by = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:BusinessEntity {regional_standard_regulation_id: 'TDPSA', entity_id: row.source_entity_id})
MATCH (target:RegionalStandardAndRegulation {regional_standard_regulation_id: row.target_regulation_id})
MERGE (source)-[r:GOVERNED_BY {
    source_id: row.source_entity_id,
    target_id: row.target_regulation_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.compliance_start_date = date(row.compliance_start_date),
    r.jurisdiction = row.jurisdiction,
    r.mandatory = toBoolean(row.mandatory);
"""
# Personal data belongs to category
personal_data_belongs_to_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (source:PersonalData {regional_standard_regulation_id: 'TDPSA', data_id: row.source_data_id})
MATCH (target:DataCategory {regional_standard_regulation_id: 'TDPSA', category_id: row.target_category_id})
MERGE (source)-[r:BELONGS_TO_CATEGORY {
    source_id: row.source_data_id,
    target_id: row.target_category_id
}]->(target)
ON CREATE SET
    r.relationship_type = row.relationship_type,
    r.classification_date = date(row.classification_date),
    r.primary_category = toBoolean(row.primary_category);
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

client.query(business_entity.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_BusinessEntity_nodes.csv'))
time.sleep(2)

client.query(consumer.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_Consumer_nodes.csv'))
time.sleep(2)

client.query(personal_data.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_PersonalData_nodes.csv'))
time.sleep(2)

client.query(sensitive_data.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_SensitiveData_nodes.csv'))
time.sleep(2)

client.query(data_category.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_DATACATEGORY.csv'))
time.sleep(2)

client.query(processing_activity.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_ProcessingActivity_nodes.csv'))
time.sleep(2)

client.query(consent.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_Consent.csv'))
time.sleep(2)

client.query(privacy_notice.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_PrivacyNotice_nodes.csv'))
time.sleep(2)

client.query(data_protection_assessment.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_DataProtectionAssessment_nodes.csv'))
time.sleep(2)

client.query(consumer_request.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_ConsumerRequest.csv'))
time.sleep(2)

client.query(data_processor.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_DataProcessor_nodes.csv'))
time.sleep(2)

client.query(data_breach.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_DataBreach.csv'))
time.sleep(2)

client.query(opt_out_mechanism.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_OptOutMechanism_nodes.csv'))
time.sleep(2)

client.query(compliance_audit.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_ComplianceAudit_nodes.csv'))
time.sleep(2)

client.query(process_consumer_rel.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_PROCESSES_CONSUMER_DATA_relationships.csv'))
time.sleep(2)

client.query(collects_personal_data.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_COLLECTS_PERSONAL_DATA_relationships.csv'))
time.sleep(2)

client.query(process_sensitive_data.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_PROCESSES_SENSITIVE_DATA_relationships.csv'))
time.sleep(2)

client.query(obtains_consent_data.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_OBTAINS_CONSENT_relationships.csv'))
time.sleep(2)

client.query(conducts_processing_activity.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_CONDUCTS_PROCESSING_ACTIVITY_relationships.csv'))
time.sleep(2)

client.query(requires_data_protection_assessment.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_REQUIRES_DATA_PROTECTION_ASSESSMENT_relationships.csv'))
time.sleep(2)

client.query(respond_consumer_request.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_RESPONDS_TO_CONSUMER_REQUEST_relationships.csv'))
time.sleep(2)

client.query(uses_data_processor.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_USES_DATA_PROCESSOR_relationships.csv'))
time.sleep(2)

client.query(offers_privacy_notice.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_OFFERS_PRIVACY_NOTICE_relationships.csv'))
time.sleep(2)

client.query(provides_opt_out_mechanism.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_PROVIDES_OPT_OUT_MECHANISM_relationships.csv'))
time.sleep(2)

client.query(experiences_data_breach.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_EXPERIENCES_DATA_BREACH_relationships.csv'))
time.sleep(2)

client.query(undergoes_compliance_audit.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_UNDERGOES_COMPLIANCE_AUDIT_relationships.csv'))
time.sleep(2)

client.query(exercises_consumer_right.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_EXERCISES_CONSUMER_RIGHT_relationships.csv'))
time.sleep(2)

client.query(personal_data_belongs_to_category.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_BELONGS_TO_CATEGORY_PersonalData.csv'))
time.sleep(2)

client.query(sensitive_data_belongs_to_category.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_BELONGS_TO_CATEGORY_SensitiveData.csv'))
time.sleep(2)

client.query(governed_by.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/TDPSA/TDPSA_GOVERNED_BY_relationships.csv'))
time.sleep(2)


logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:RegionalStandardAndRegulation)-[*]-()
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
with open('tdpsa.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to tdpsa.json")

client.close()