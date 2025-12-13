#Regulation
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'TDPSA'})
ON CREATE SET
    reg.name = "Texas Data Privacy and Security Act ",
    reg.version = "2023",
    reg.effective_date = date("2022-01-01"),
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







    




