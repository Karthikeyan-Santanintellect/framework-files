# Create PCIDSS Standard Nodes
industry_standard_regulation = """
MERGE (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  i.name = 'Payment Card Industry Data Security Standard',
  i.version = '4.0.1',
  i.publication_date = '2024-03-31',
  i.retirement_date = '2027-03-31',
  i.effective_date = '2024-03-31',
  i.type = 'Major Revision',
  i.status = 'Active',
  i.description = 'The Payment Card Industry Data Security Standard (PCI DSS) v4.0.1 is a comprehensive global security standard developed by the PCI Security Standards Council to protect cardholder data and reduce payment fraud.';
"""
#Standard Nodes
standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Standard {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  s.name = row.node_name,
  s.type = row.node_type,
  s.definition = row.definition,
  s.description = row.official_description,
  s.applicable_to = row.applicable_to,
  s.owner = row.organization_owner,
  s.version = row.version,
  s.status = row.status,
  s.key_features = row.key_features;
"""
#Requirement Nodes
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Requirement {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  r.name = row.node_name,
  r.number = row.requirement_number,
  r.standard_id = row.standard_id,
  r.title = row.official_title,
  r.description = row.official_description,
  r.purpose_and_intent = row.purpose_and_intent,
  r.key_implementation_requirements = row.key_implementation_requirements,
  r.sub_requirements = row.sub_requirements,
  r.testing_guidance = row.testing_guidance,
  r.applies_to_entity_type = row.applies_to_entity_type,
  r.criticality = row.criticality,
  r.pci_requirement_reference = row.pci_requirement_reference;
"""
#  Strategic Objective Nodes
strategic_objective ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:StrategicObjective {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  o.number = row.objective_number,
  o.name = row.node_name,
  o.definition = row.definition,
  o.official_pci_description = row.official_pci_description,
  o.pci_requirements_mapped = row.pci_requirements_mapped,
  o.implementation_focus = row.implementation_focus,
  o.business_value = row.business_value,
  o.criticality = row.criticality,
  o.iso_27001_alignment = row.iso_27001_alignment;
"""
# Responsible Entity Nodes 
responsible_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:ResponsibleEntity {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  e.name = row.node_name,
  e.type = row.entity_type,
  e.definition = row.definition,
  e.pci_dss_definition = row.pci_dss_definition,
  e.compliance_level = row.compliance_level,
  e.transaction_threshold = row.transaction_threshold,
  e.assessment_type = row.assessment_type,
  e.compliance_requirements = row.compliance_requirements,
  e.applicable_standards = row.applicable_standards,
  e.criticality = row.criticality,
  e.created_at = timestamp()
ON MATCH SET
  e.updated_at = timestamp()
RETURN COUNT(e) AS responsible_entities_loaded
"""
# Cardholder Data Nodes 
card_holder_data ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cd:CardholderData {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  cd.name = row.node_name,
  cd.data_element = row.data_element,
  cd.category = row.pci_official_category,
  cd.definition = row.definition,
  cd.official_pci_description = row.official_pci_description,
  cd.storage_allowed = row.storage_allowed,
  cd.encryption_required = row.encryption_required,
  cd.masking_requirement = row.masking_requirement,
  cd.deletion_requirement = row.deletion_requirement,
  cd.official_regulation_reference = row.official_regulation_reference,
  cd.criticality = row.criticality;
"""
# CDE Environment Nodes 
cde_environment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cde:CDEComponent {cde_component_id: row.cde_component_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  cde.type = row.component_type,
  cde.description = row.official_description,
  cde.in_scope_for_pci = row.in_scope_for_pci,
  cde.protection_requirements = row.protection_requirements,
  cde.connectivity_to_cde = row.connectivity_to_cde,
  cde.monitoring_requirements = row.monitoring_requirements,
  cde.vulnerability_scanning = row.vulnerability_scanning,
  cde.network_segmentation = row.network_segmentation,
  cde.encryption_required = row.encryption_required,
  cde.physical_access_control = row.physical_access_control,
  cde.systems = row.examples_of_systems;
"""
# Security Control Nodes 
security_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:SecurityControl {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  sc.name = row.node_name,
  sc.control_id = row.control_id,
  sc.standard_id = row.standard_id,
  sc.category = row.control_category,
  sc.definition = row.definition,
  sc.official_description = row.official_description,
  sc.implementation_guidance = row.implementation_guidance,
  sc.verification_method = row.verification_method,
  sc.applies_to = row.applies_to,
  sc.criticality = row.criticality,
  sc.pci_requirement_mapping = row.pci_requirement_mapping,
  sc.iso_27001_mapping = row.iso_27001_mapping;
"""
# System Component Nodes
system_component ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sysc:SystemComponent {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  sysc.name = row.node_name,
  sysc.type = row.component_type,
  sysc.definition = row.definition,
  sysc.in_scope_for_pci = row.in_scope_for_pci,
  sysc.security_requirements = row.security_requirements,
  sysc.monitoring_requirements = row.monitoring_requirements,
  sysc.examples = row.examples,
  sysc.update_frequency = row.update_frequency,
  sysc.pci_requirement_mapping = row.pci_requirement_mapping,
  sysc.criticality = row.criticality,
  sysc.created_at = timestamp()
ON MATCH SET
  sysc.updated_at = timestamp()
RETURN COUNT(sysc) AS system_components_loaded
"""
# Internal Role Nodes 
internal_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:InternalRole {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ir.name = row.node_name,
  ir.title = row.role_title,
  ir.department = row.department,
  ir.responsibility_summary = row.responsibility_summary,
  ir.pci_dss_responsibilities = row.pci_dss_responsibilities,
  ir.required_qualifications = row.required_qualifications,
  ir.training_requirements = row.training_requirements,
  ir.key_functions = row.key_functions,
  ir.pci_requirement_mapping = row.pci_requirement_mapping,
  ir.criticality = row.criticality,
  ir.created_at = timestamp()
ON MATCH SET
  ir.updated_at = timestamp()
RETURN COUNT(ir) AS internal_roles_loaded
"""
# Artifact Nodes
artifact ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Artifact {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  a.name = row.node_name,
  a.type = row.artifact_type,
  a.definition = row.definition,
  a.pci_dss_requirement = row.pci_dss_requirement,
  a.purpose_and_use = row.purpose_and_use,
  a.retention_period = row.retention_period,
  a.owner = row.owner,
  a.verification_method = row.verification_method,
  a.criticality = row.criticality,
  a.document_frequency = row.document_frequency,
  a.digital_or_physical = row.digital_or_physical,
  a.created_at = timestamp()
ON MATCH SET
  a.updated_at = timestamp()
RETURN COUNT(a) AS artifacts_loaded
"""
#Payment Brand Nodes
payment_brand ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pb:PaymentBrand {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  pb.name = row.payment_brand_name,
  pb.official_full_name = row.official_full_name,
  pb.headquarters_location = row.headquarters_location,
  pb.founded_year = row.founded_year,
  pb.market_coverage = row.market_coverage,
  pb.accepted_merchants_worldwide = row.accepted_merchants_worldwide,
  pb.transaction_volume_annual = row.transaction_volume_annual,
  pb.network_type = row.network_type,
  pb.card_types_supported = row.card_types_supported,
  pb.geographic_focus = row.geographic_focus,
  pb.regional_dominance = row.regional_dominance,
  pb.pci_dss_compliance = row.pci_dss_compliance,
  pb.security_standards = row.security_standards,
  pb.data_protection_requirements = row.data_protection_requirements,
  pb.fraud_prevention = row.fraud_prevention,
  pb.created_at = timestamp()
ON MATCH SET
  pb.updated_at = timestamp()
RETURN COUNT(pb) AS payment_brands_loaded
"""

# Acquiring Bank Nodes
acquiring_bank ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ab:AcquiringBank {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ab.type = row.organization_type,
  ab.role_in_ecosystem = row.role_in_ecosystem,
  ab.definition = row.official_definition,
  ab.primary_responsibilities = row.primary_responsibilities,
  ab.secondary_responsibilities = row.secondary_responsibilities,
  ab.pci_dss_requirements = row.pci_dss_requirements,
  ab.relationship_to_merchants = row.relationship_to_merchants,
  ab.relationship_to_service_providers = row.relationship_to_service_providers,
  ab.relationship_to_card_networks = row.relationship_to_card_networks,
  ab.typical_transaction_volume = row.typical_transaction_volume,
  ab.geographic_scope = row.geographic_scope,
  ab.regulatory_authority = row.regulatory_authority,
  ab.compliance_enforcement = row.compliance_enforcement,
  ab.data_requirements = row.data_requirements,
  ab.communication_protocols = row.communication_protocols,
  ab.incident_response_role = row.incident_response_role,
  ab.annual_assessment_requirements = row.annual_assessment_requirements,
  ab.certification_requirements = row.certification_requirements,
  ab.professional_standards = row.professional_standards,
  ab.liability_coverage = row.liability_coverage,
  ab.examples_global = row.examples_global,
  ab.key_selection_criteria = row.key_selection_criteria;
  """

#Service Provider Nodes
service_provider ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:ServiceProvider {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  sp.type = row.organization_type,
  sp.role_in_ecosystem = row.role_in_ecosystem,
  sp.official_definition = row.official_definition,
  sp.primary_responsibilities = row.primary_responsibilities,
  sp.secondary_responsibilities = row.secondary_responsibilities,
  sp.pci_dss_requirements = row.pci_dss_requirements,
  sp.relationship_to_merchants = row.relationship_to_merchants,
  sp.relationship_to_processors = row.relationship_to_processors,
  sp.relationship_to_acquirers = row.relationship_to_acquirers,
  sp.typical_service_scope = row.typical_service_scope,
  sp.geographic_scope = row.geographic_scope,
  sp.regulatory_authority = row.regulatory_authority,
  sp.compliance_enforcement = row.compliance_enforcement,
  sp.data_requirements = row.data_requirements,
  sp.communication_protocols = row.communication_protocols,
  sp.incident_response_role = row.incident_response_role,
  sp.annual_assessment_requirements = row.annual_assessment_requirements,
  sp.certification_requirements = row.certification_requirements,
  sp.professional_standards = row.professional_standards,
  sp.liability_coverage = row.liability_coverage,
  sp.examples_global = row.examples_global,
  sp.key_selection_criteria = row.key_selection_criteria;
"""
# Approved Scanning Vendor (ASV) Nodes
approved_scanning_vendor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (asv:ApprovedScanningVendor {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  asv.type = row.organization_type,
  asv.role_in_ecosystem = row.role_in_ecosystem,
  asv.official_definition = row.official_definition,
  asv.primary_responsibilities = row.primary_responsibilities,
  asv.secondary_responsibilities = row.secondary_responsibilities,
  asv.pci_dss_requirements = row.pci_dss_requirements,
  asv.relationship_to_entities = row.relationship_to_entities,
  asv.service_scope = row.service_scope,                              
  asv.geographic_scope = row.geographic_scope,
  asv.regulatory_authority = row.regulatory_authority,
  asv.compliance_enforcement = row.compliance_enforcement,
  asv.deliverables = row.deliverables,
  asv.communication_protocols = row.communication_protocols,
  asv.scan_frequency = row.scan_frequency,
  asv.support = row.remediation_support,
  asv.certification_requirements = row.certification_requirements,
  asv.professional_standards = row.professional_standards,
  asv.liability_coverage = row.liability_coverage,
  asv.approved_vendor_list = row.approved_vendor_list,
  asv.key_selection_criteria = row.key_selection_criteria;
"""
# Qualified Security Assessor (QSA) Nodes
qualified_security_assessor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (qsa:QualifiedSecurityAssessor {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  qsa.type = row.organization_type,
  qsa.role_in_ecosystem = row.role_in_ecosystem,
  qsa.official_definition = row.official_definition,
  qsa.primary_responsibilities = row.primary_responsibilities,
  qsa.secondary_responsibilities = row.secondary_responsibilities,
  qsa.pci_dss_requirements = row.pci_dss_requirements,
  qsa.relationship_to_entities = row.relationship_to_entities,
  qsa.service_scope = row.service_scope,
  qsa.geographic_scope = row.geographic_scope,
  qsa.regulatory_authority = row.regulatory_authority,
  qsa.compliance_enforcement = row.compliance_enforcement,
  qsa.deliverables = row.deliverables,
  qsa.communication_protocols = row.communication_protocols,
  qsa.assessment_frequency = row.assessment_frequency,
  qsa.certification_requirements = row.certification_requirements,
  qsa.professional_standards = row.professional_standards,
  qsa.liability_coverage = row.liability_coverage,
  qsa.approved_assessor_list = row.approved_assessor_list,
  qsa.key_selection_criteria = row.key_selection_criteria;
"""
#Threat Intelligence Nodes
threat_intelligence ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ti:ThreatIntelligence {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ti.type = row.organization_type,
  ti.role_in_ecosystem = row.role_in_ecosystem,
  ti.definition = row.official_definition,
  ti.primary_responsibilities = row.primary_responsibilities,
  ti.secondary_responsibilities = row.secondary_responsibilities,
  ti.information_shared = row.information_shared,
  ti.participation_model = row.participation_model,
  ti.geographic_scope = row.geographic_scope,
  ti.member_benefits = row.member_benefits,
  ti.communication_channels = row.communication_channels,
  ti.real_time_alerting = row.real_time_alerting,
  ti.incident_coordination = row.incident_coordination,
  ti.threat_analysis_capabilities = row.threat_analysis_capabilities,
  ti.reporting_frequency = row.reporting_frequency,
  ti.membership_requirements = row.membership_requirements,
  ti.confidentiality_protocols = row.confidentiality_protocols,
  ti.cost_structure = row.cost_structure,
  ti.integration_capabilities = row.integration_capabilities,
  ti.key_use_cases = row.key_use_cases;
"""
#Regulatory body
regulatory_body ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rb:RegulatoryBody {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  rb.type = row.organization_type,
  rb.role_in_ecosystem = row.role_in_ecosystem,
  rb.official_definition = row.official_definition,
  rb.primary_responsibilities = row.primary_responsibilities,
  rb.secondary_responsibilities = row.secondary_responsibilities,
  rb.enforcement_authority = row.enforcement_authority,
  rb.jurisdiction = row.jurisdiction,
  rb.regulatory_mandate = row.regulatory_mandate,
  rb.standards_developed = row.standards_developed,
  rb.compliance_monitoring = row.compliance_monitoring,
  rb.penalty_authority = row.penalty_authority,
  rb.investigation_authority = row.investigation_authority,
  rb.reporting_requirements = row.reporting_requirements,
  rb.coordination_mechanisms = row.coordination_mechanisms,
  rb.member_organizations = row.member_organizations,
  rb.assessment_programs = row.assessment_programs,
  rb.certification_programs = row.certification_programs,
  rb.guidance_publications = row.guidance_publications,
  rb.incident_notification = row.incident_notification,
  rb.international_reach = row.international_reach,
  rb.funding_model = row.funding_model,
  rb.governance_structure = row.governance_structure,
  rb.public_reporting = row.public_reporting,
  rb.contact_information = row.contact_information,
  rb.key_selection_criteria = row.key_selection_criteria;
"""
# Law enforcement Nodes
law_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (le:LawEnforcementAgency {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  le.type = row.organization_type,
  le.role_in_ecosystem = row.role_in_ecosystem,
  le.official_definition = row.official_definition,
  le.primary_responsibilities = row.primary_responsibilities,
  le.secondary_responsibilities = row.secondary_responsibilities,
  le.enforcement_authority = row.enforcement_authority,
  le.jurisdiction = row.jurisdiction,
  le.investigation_capabilities = row.investigation_capabilities,
  le.notification_requirements = row.notification_requirements,
  le.cooperation_requirements = row.cooperation_requirements,
  le.data_requests = row.data_requests,
  le.prosecution_authority = row.prosecution_authority,
  le.international_coordination = row.international_coordination,
  le.incident_response_role = row.incident_response_role,
  le.victim_support = row.victim_support,
  le.public_reporting = row.public_reporting,
  le.contact_information = row.contact_information,
  le.response_time = row.response_time,
  le.key_statutes = row.key_statutes,
  le.evidence_requirements = row.evidence_requirements,
  le.cyber_forensics_capability = row.cyber_forensics_capability,
  le.threat_intelligence_sharing = row.threat_intelligence_sharing,
  le.cross_border_authority = row.cross_border_authority,
  le.liaison_relationships = row.liaison_relationships,
  le.training_resources = row.training_resources,
  le.key_selection_criteria = row.key_selection_criteria;
  """

#Third-Party Assessor nodes
third_party_assessor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tpa:ThirdPartyAssessor {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  tpa.type = row.organization_type,
  tpa.role_in_ecosystem = row.role_in_ecosystem,
  tpa.definition = row.official_definition,
  tpa.primary_responsibilities = row.primary_responsibilities,
  tpa.secondary_responsibilities = row.secondary_responsibilities,
  tpa.assessment_frameworks = row.assessment_frameworks,
  tpa.relationship_to_entities = row.relationship_to_entities,
  tpa.service_scope = row.service_scope,
  tpa.geographic_scope = row.geographic_scope,
  tpa.regulatory_authority = row.regulatory_authority,
  tpa.compliance_enforcement = row.compliance_enforcement,
  tpa.deliverables = row.deliverables,
  tpa.communication_protocols = row.communication_protocols,
  tpa.assessment_frequency = row.assessment_frequency,
  tpa.certification_requirements = row.certification_requirements,
  tpa.professional_standards = row.professional_standards,
  tpa.liability_coverage = row.liability_coverage,
  tpa.independence_requirements = row.independence_requirements,
  tpa.accreditation_bodies = row.accreditation_bodies,
  tpa.quality_assurance = row.quality_assurance,
  tpa.continuing_education = row.continuing_education,
  tpa.typical_engagement_duration = row.typical_engagement_duration,
  tpa.cost_structure = row.cost_structure,
  tpa.examples_global = row.examples_global,
  tpa.key_selection_criteria = row.key_selection_criteria;
"""

# Sub-Requirement Nodes
sub_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sr:SubRequirement {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  sr.sub_requirement_id = row.sub_requirement_id,
  sr.requirement_reference = row.requirement_reference,
  sr.title = row.title,
  sr.description = row.description,
  sr.obligation_type = row.obligation_type,
  sr.risk_area = row.risk_area,
  sr.criticality = row.criticality;
"""

# Testing Procedure Nodes
testing_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tp:TestingProcedure {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  tp.procedure_id = row.procedure_id,
  tp.sub_requirement_reference = row.sub_requirement_reference,
  tp.description = row.description,
  tp.method_type = row.method_type,
  tp.evidence_required = row.evidence_required;
"""

# Merchant Level Nodes
merchant_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ml:MerchantLevel {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ml.level = row.level,
  ml.criteria = row.criteria,
  ml.validation_requirements = row.validation_requirements;
"""

# Assessment Instrument Nodes
assessment_instrument = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ai:AssessmentInstrument {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ai.name = row.name,
  ai.description = row.description,
  ai.target_audience = row.target_audience;
"""

# Data State Nodes
data_state = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ds:DataState {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  ds.state_name = row.state_name,
  ds.description = row.description,
  ds.primary_requirement_ref = row.primary_requirement_ref;
"""

# Authentication Factor Nodes
authentication_factor = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (af:AuthenticationFactor {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  af.factor_name = row.factor_name,
  af.category = row.category,
  af.examples = row.examples;
"""
# Compensating Control Nodes
compensating_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:CompensatingControl {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  cc.name = row.name,
  cc.description = row.description,
  cc.validity_period = row.validity_period;
"""

#Relaitonships
#  INDUSTRY REGULATION  TO STANDRAD
industry_standard_regulation_standard = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (i)-[rel:INDUSTRY_REGULATION_HAS_STANDARD]->(s);
"""
# STANDARD TO STRATEGIC OBJECTIVES
standard_strategic_objective="""
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (o:StrategicObjective {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (s)-[rel:STANDARD_HAS_STRATEGIC_OBJECTIVE]->(o);
"""
# STRATEGIC OBJECTIVE TO REQUIREMENTS
strategic_objective_requirement ="""
MATCH (o:StrategicObjective {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (o)-[rel:STRATEGIC_OBJECTIVE_CONTAINS_REQUIREMENT]->(r);
"""
# REQUIREMENT TO STANDARD 
requirement_standard="""
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (r)-[:REQUIREMENT_HAS_STANDARD]->(s);
"""
#REQUIREMENT TO STRATEGIC OBJECTIVE
requirement_strategic_objective = """
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (o:StrategicObjective {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (r)-[rel:REQUIREMENT_SUPPORTS_OBJECTIVE]->(o);
"""
# REQUIREMENTS REQUIRE SECURITY CONTROLS 
requirement_security_control ="""
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (r)-[rel:REQUIREMENT_REQUIRES_CONTROL]->(sc);
"""
# SECURITY CONTROLS PROTECT DATA
security_control_data_protection =  """
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE sc.category IN ['Data Protection', 'Encryption', 'Access Control']
   OR sc.name CONTAINS 'Encryption'
   OR sc.name CONTAINS 'Tokenization'
   OR sc.name CONTAINS 'Masking'
MERGE (sc)-[rel:SECURITY_CONTROL_PROTECTS_CARDHOLDER_DATA]->(cd);
"""
# SECURITY CONTROLS SECURE COMPONENTS
security_control_components = """
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sysc:SystemComponent {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE sc.category IN ['Technical', 'Network', 'Physical']
   OR sysc.pci_requirement_mapping CONTAINS sc.pci_requirement_mapping
MERGE (sc)-[rel:SECURITY_CONTROL_USES_SYSTEM_COMPONENT]->(sysc);
"""
# CARDHOLDER DATA STORED IN SYSTEMS
card_holder_data_systems ="""
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sysc:SystemComponent {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cd)-[rel:CARD_HOLDER_DATA_STORED_IN_SYSTEM_COMPONENT]->(sysc);
"""
# CARDHOLDER DATA ENCRYPTED WITH KEYS
card_holder_data_encryption ="""
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cd)-[rel:CARD_HOLDER_DATA_ENCRYPTED_WITH_SECURITY_CONTROL]->(sc);
"""
# CARDHOLDER DATA TRANSMITTED VIA CHANNELS
card_holder_data_channels ="""
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cde:CDEComponent {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cd)-[rel:CARD_HOLDER_DATA_TRANSMITTED_CDE_COMPONENT]->(cde);
"""
# 13. CARDHOLDER DATA PROTECTED BY ENCRYPTION
card_holder_data_protection ="""
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cd)-[rel:CARD_HOLDER_DATA_PROTECTED_BY_SECURITY_CONTROL]->(sc);
"""
#  CDE contains system components
cde_system_components ="""
MATCH (cde:CDEComponent{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sysc:SystemComponent{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cde)-[rel:CDE_CONTAINS_SYSTEM_COMPONENT]->(sysc);
"""
# System component has configuration
system_component_configuration ="""
MATCH (sysc:SystemComponent{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sysc)-[rel:SYSTEM_COMPONENT_HAS_SECURITY_CONTROL]->(sc);
"""
# Internal_control to SecurityControl
internal_control_security_control ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ir)-[rel:INTERNAL_ROLE_REQUIRES_SECURITY_CONTROL]->(sc);
"""

# Internal_control to card_holder
internal_control_card_holder ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cd:CardholderData{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ir)-[rel:INTERNAL_ROLE_ACQUIRES_CARD_HOLDER]->(cd);
"""
# Internal_control to requirement
internal_control_requirement ="""
MATCH (ir:InternalRole{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ir)-[rel:INTERNAL_ROLE_REQUIRES_REQUIREMENT]->(r);
"""
# Internal_control to Artifact
internal_control_artifact = """
MATCH (ir:InternalRole{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (a:Artifact{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ir)-[rel:INTERNAL_ROLE_LOGGED_IN_ARTIFACT]->(a);
"""
# CDE to Requirement
CDE_requirement ="""
MATCH (cde:CDEComponent{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cde)-[rel:CDE_REQUIRES_REQUIREMENT]->(r);
"""
# securitycontrol to artifact
security_control_artifact = """
MATCH (sc:SecurityControl{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (a:Artifact{industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sc)-[rel:SECURITY_CONTROL_LOGGED_IN_ARTIFACTS]->(a);
"""

# INTERNAL ROLE ASSIGNED TO ENTITY
internal_role_entity ="""
MATCH (ir:InternalRole {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ir)-[rel:INTERNAL_ROLE_WORKS_FOR_ENTITY]->(e);
"""
# SERVICE PROVIDER ACCESSES CARDHOLDER DATA
service_provider_card_holder ="""
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sp)-[rel:SERVICE_PROVIDER_ACCESSES_CARD_HOLDER]->(cd);
"""
#SERVICE PROVIDER MUST IMPLEMENT CONTROLS
service_provider_controls ="""
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sp)-[rel:SERVICE_PROVIDER_MUST_IMPLEMENT_SECURITY_CONTROL]->(sc);
"""
# SERVICE PROVIDER SUBJECT TO REQUIREMENTS
service_provider_requirements ="""
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sp)-[rel:SERVICE_PROVIDER_SUBJECT_TO_REQUIREMENT]->(r);
"""
#SERVICE PROVIDER CERTIFIED BY NETWORK
service_provider_network ="""
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (pb:PaymentBrand {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sp)-[rel:SERVICE_PROVIDER_CERTIFIED_BY_PAYMENT_BRAND]->(pb);
"""
#ACQUIRING BANK REGULATES SERVICE PROVIDER
service_provider_regulatory ="""
MATCH (ab:AcquiringBank {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ab)-[rel:ACQUIRING_BANK_REGULATES_SERVICE_PROVIDER]->(sp);
"""
#PAYMENT BRAND ENFORCES REQUIREMENT
service_provider_requirement ="""
MATCH (pb:PaymentBrand {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (pb)-[rel:PAYMENT_BRAND_ENFORCES_REQUIREMENT]->(r);
"""
#ACQUIRING BANK ENFORCES MERCHANT COMPLIANCE
acquiring_bank_compliance ="""
MATCH (ab:AcquiringBank {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ab)-[rel:ACQUIRING_BANK_ENFORCES_COMPLIANCE]->(e);
"""
#ACQUIRING BANK OPERATES ON NETWORK
acquiring_bank_payment_bank ="""
MATCH (ab:AcquiringBank {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (pb:PaymentBrand {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ab)-[rel:ACQUIRING_BANK_OPERATES_ON_NETWORK]->(pb);
"""
#QSA CONDUCTS ASSESSMENT
qsa_conducts_assessment ="""
MATCH (qsa:QualifiedSecurityAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (qsa)-[rel:QSA_CONDUCTS_ASSESSMENT]->(e);
"""
#ASV PERFORMS VULNERABILITY SCAN
asv_vulnerability_scan ="""
MATCH (asv:ApprovedScanningVendor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (asv)-[rel:ASV_PERFORMS_VULNERABILITY_SCAN]->(e);
"""
# QSA ASSESSES REQUIREMENT
qsa_assesses_requirement ="""
MATCH (qsa:QualifiedSecurityAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (qsa)-[rel:QSA_ASSESSES_REQUIREMENT]->(r);
"""
#ASV VALIDATES CONTROL
asv_security_control ="""
MATCH (asv:ApprovedScanningVendor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (asv)-[rel:ASV_VALIDATES_CONTROL]->(sc);
"""
#artifact to requirement
artifact_requirement ="""
MATCH (a:Artifact {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (a)-[rel:ARTIFACT_REQUIRES_REQUIREMENT]->(r);
"""
# QSA to artifact
qsa_artifact ="""
MATCH (qsa:QualifiedSecurityAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (a:Artifact {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (qsa)-[rel:QSA_CONDUCTS_ASSESSMENT]->(a);
"""
# ASV to artifact
asv_artifact ="""
MATCH (asv:ApprovedScanningVendor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (a:Artifact {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (asv)-[rel:ASV_HAS_ARTIFACT]->(a);
"""
# ARTIFACT MAINTAINED BY ROLE
artifact_role ="""
MATCH (a:Artifact {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (ir:InternalRole {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (a)-[rel:ARTIFACT_MAINTAINED_BY_INTERNAL_ROLE]->(ir);
"""
# REGULATORY BODY DEVELOPS STANDARD
regulatory_body_standard ="""
MATCH (rb:RegulatoryBody {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (rb)-[rel:REGULATORY_BODY_DEVELOPS_STANDARD]->(s);
"""

# REGULATORY BODY QUALIFIES QSA
regulatory_body_qsa = """
MATCH (rb:RegulatoryBody {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (qsa:QualifiedSecurityAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (rb)-[rel:REGULATORY_BODY_QUALIFIES_SECURITY_ASSESSOR]->(qsa);
"""
#  REGULATORY BODY APPROVES ASV
regulatory_body_asv ="""
MATCH (rb:RegulatoryBody {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (asv:ApprovedScanningVendor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (rb)-[rel:REGULATORY_BODY_APPROVES_SCANNING_VENDOR]->(asv);
"""
# REGULATORY BODY ENFORCES RESPONSIBLE_ENTITY
regulatory_body_responsible_entity ="""
MATCH (rb:RegulatoryBody {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (rb)-[rel:REGULATORY_BODY_ENFORCES_ENTITY]->(e);
"""
#LAW ENFORCEMENT INVESTIGATES BREACH
law_enforcement_investigates_breach ="""
MATCH (le:LawEnforcementAgency {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (le)-[rel:LAW_ENFORCEMENT_INVESTIGATES_ENTITY]->(e);
"""
# ENTITY REPORTS BREACH TO LAW ENFORCEMENT
law_enforcement_reports_breach ="""
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (le:LawEnforcementAgency {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (e)-[rel:RESPONSIBLE_ENTITY_REPORTS_BREACH]->(le);
"""
#  THREAT INTELLIGENCE INFORMS CONTROLS
threat_intelligence_controls ="""
MATCH (ti:ThreatIntelligence {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ti)-[rel:THREAT_INTELLIGENCE_FORMS_CONTROL]->(sc);
"""
# THREAT INTELLIGENCE SUPPORTS STANDARD
threat_intelligence_standard ="""
MATCH (ti:ThreatIntelligence {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ti)-[rel:THREAT_INTELLIGENCE_SUPPORTS_STANDARD]->(s);
"""
# ENTITY SUBSCRIBES TO THREAT INTELLIGENCE
responsible_entity_threat_intelligence ="""
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (ti:ThreatIntelligence {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (e)-[rel:RESPONSIBLE_ENTITY_SUBSCRIBES_TO_THREAT_INTELLIGENCE]->(ti);
"""

#THIRD-PARTY ASSESSOR VALIDATES STANDARD
third_party_assessor_standard ="""
MATCH (tpa:ThirdPartyAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:Standard {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (tpa)-[rel:ENTITY_VALIDATES_STANDARD]->(s);
"""
#THIRD-PARTY ASSESSOR ASSESSES CONTROL
third_party_assessor_control ="""
MATCH (tpa:ThirdPartyAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (tpa)-[rel:ENTITY_ASSESSES_CONTROL]->(sc);
"""
# ENTITY ENGAGES THIRD-PARTY ASSESSOR
responsible_entity_third_party_assessor ="""
MATCH (e:ResponsibleEntity {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (tpa:ThirdPartyAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (e)-[rel:ENTITY_ENGAGES_ASSESSOR]->(tpa);
"""
# THIRD-PARTY ASSESSOR GENERATES ARTIFACT
third_party_assessor_artifact = """
MATCH (tpa:ThirdPartyAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (a:Artifact {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (tpa)-[rel:THIRD_PARTY_ASSESSOR_GENERATES_ARTIFACT]->(a);
"""
# THIRD-PARTY ASSESSOR VALIDATES REQUIREMENT
third_party_assessor_requirement = """
MATCH (tpa:ThirdPartyAssessor {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (tpa)-[rel:THIRDPARTY_ASSESSOR_VALIDATES_REQUIREMENT]->(r);
"""
# Requirement Contains Sub-Requirement Relationship
requirement_sub_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {number: row.parent_req_number, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sr:SubRequirement {node_id: row.sub_req_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (r)-[rel:REQUIREMENT_CONTAINS_SUB_REQUIREMENT]->(sr);
"""
# Sub-Requirement Verified By Procedure Relationship
sub_requirement_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {node_id: row.sub_req_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (tp:TestingProcedure {node_id: row.testing_proc_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[rel:SUB_REQUIREMENT_VERIFIED_BY_PROCEDURE]->(tp);
"""
# Merchant Level to Assessment Instrument Relationships
merchant_assessment_relationships = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ml:MerchantLevel {node_id: row.merchant_level_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (ai:AssessmentInstrument {node_id: row.assessment_instrument_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (ml)-[:MERCHANT_LEVEL_REQUIRES_ASSESSMENT_TYPE]->(ai);
"""

# SubRequirement to Compensating Control Relationships
compensating_relationships = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {node_id: row.sub_req_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cc:CompensatingControl {node_id: row.compensating_control_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[:SUB_REQUIREMENT_MITIGATED_BY_COMPENSATING_CONTROL]->(cc);
"""
# Security Control implements SubRequirement
control_subreq_relationships = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {node_id: row.sub_req_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {node_id: row.control_node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sc)-[:SECURITY_CONTROL_IMPLEMENTS_SUB_REQUIREMENT]->(sr);
"""
# SubRequirement to Authentication Factor Relationships
auth_factor_relationships = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (af:AuthenticationFactor {node_id: row.auth_factor_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sr:SubRequirement {node_id: row.sub_req_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[:SUB_REQUIREMENT_MANDATES_AUTHENTICATION_FACTOR]->(af);
"""

# ResponsibleEntity (Merchant) to Merchant Level Relationships
entity_level_relationships = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (e:ResponsibleEntity {type: row.entity_type, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (ml:MerchantLevel {node_id: row.level_node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (e)-[:RESPONSIBLE_ENTITY_CLASSIFIED_AS_LEVEL]->(ml);
"""
# Security Control Protects Data State Relationship
security_control_data_state = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ds:DataState {node_id: row.data_state_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE sc.name CONTAINS row.control_keyword
MERGE (sc)-[rel:SECURITY_CONTROL_PROTECTS_DATA_STATE]->(ds);
"""
# Cardholder Data Exists In State Relationship
cardholder_data_exists_in_state = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ds:DataState {node_id: row.data_state_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE cd.node_id = row.cardholder_node_id 
   OR (row.cardholder_node_id IS NULL AND cd.name CONTAINS 'PAN')
MERGE (cd)-[rel:CARDHOLDER_DATA_EXISTS_IN_STATE]->(ds);
"""
sub_req_orphan = """
MATCH (sr:SubRequirement) WHERE NOT EXISTS ((sr)--())
MATCH (r:Requirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE sr.parent_requirement_ref = toString(r.number)
MERGE (r)-[:REQUIREMENT_CONTAINS_SUB_REQUIREMENT]->(sr);
"""
test_proc_orphan = """
MATCH (tp:TestingProcedure) WHERE NOT EXISTS ((tp)--())
MATCH (sr:SubRequirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE tp.procedure_id CONTAINS sr.sub_requirement_id
MERGE (sr)-[:SUB_REQUIREMENT_VERIFIED_BY_PROCEDURE]->(tp);
"""
merchant_level_orphan = """
MATCH (ml:MerchantLevel) WHERE NOT EXISTS ((ml)--())
MATCH (e:ResponsibleEntity {type: 'Merchant', industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (e)-[:RESPONSIBLE_ENTITY_CLASSIFIED_AS_LEVEL]->(ml);
"""
assessment_orphan = """
MATCH (ai:AssessmentInstrument) WHERE NOT EXISTS ((ai)--())
MATCH (ml:MerchantLevel {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE (ml.level = 'Level 1' AND ai.name CONTAINS 'ROC')
   OR (ml.level <> 'Level 1' AND ai.name CONTAINS 'SAQ')
MERGE (ml)-[:MERCHANT_LEVEL_REQUIRES_ASSESSMENT_TYPE]->(ai);
"""
compensating_orphan = """
MATCH (cc:CompensatingControl) WHERE NOT EXISTS ((cc)--())
MATCH (sr:SubRequirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE (cc.name CONTAINS 'Legacy' AND sr.title CONTAINS 'Malware')
   OR (cc.name CONTAINS 'Legacy' AND sr.title CONTAINS 'Software')
   OR (cc.name CONTAINS 'Wifi' AND sr.title CONTAINS 'Diagrams')
MERGE (sr)-[:SUB_REQUIREMENT_MITIGATED_BY_COMPENSATING_CONTROL]->(cc);
"""
auth_factor_orphan = """
MATCH (af:AuthenticationFactor) WHERE NOT EXISTS ((af)--())
MATCH (sr:SubRequirement {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE sr.sub_requirement_id = '8.3.6'
MERGE (sr)-[:SUB_REQUIREMENT_MANDATES_AUTHENTICATION_FACTOR]->(af);
"""
data_state_orphan = """
MATCH (ds:DataState) WHERE NOT EXISTS ((ds)--())
MATCH (sc:SecurityControl {industry_standard_regulation_id: 'PCI-DSS 4.0'})
WHERE (ds.state_name = 'Data At Rest' AND sc.name CONTAINS 'Encryption')
   OR (ds.state_name = 'Data In Transit' AND sc.name CONTAINS 'TLS')
   OR (ds.state_name = 'Data In Use' AND sc.name CONTAINS 'Antivirus')
MERGE (sc)-[:SECURITY_CONTROL_PROTECTS_DATA_STATE]->(ds)
WITH ds
MATCH (cd:CardholderData {industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cd)-[:CARDHOLDER_DATA_EXISTS_IN_STATE]->(ds);
"""


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
    os._exit(1)

logger.info("Loading graph structure...")

client.query(industry_standard_regulation)
time.sleep(2)

client.query(standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/standard.csv"))
time.sleep(2)

client.query(strategic_objective.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Strategic-Objective-Nodes.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/requirement.csv"))
time.sleep(2)

client.query(responsible_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Responsible_entity.csv"))
time.sleep(2)

client.query(card_holder_data.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Card_holder_data.csv"))
time.sleep(2)

client.query(cde_environment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/CDE_environment.csv"))
time.sleep(2)

client.query(security_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Security_controls.csv"))
time.sleep(2)

client.query(system_component.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/System-Components-Data.csv"))
time.sleep(2)

client.query(internal_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Internal-Roles-DATA.csv"))
time.sleep(2)

client.query(artifact.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Artifacts-DATA.csv"))
time.sleep(2)

client.query(payment_brand.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Payment_brand.csv"))
time.sleep(2)

client.query(acquiring_bank.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Acquiring_bank.csv"))
time.sleep(2)

client.query(service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Service_provider.csv"))
time.sleep(2)

client.query(approved_scanning_vendor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/ASV.csv"))
time.sleep(2)

client.query(qualified_security_assessor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/QSA.csv"))
time.sleep(2)

client.query(threat_intelligence.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Threat_intelligence.csv"))
time.sleep(2)

client.query(law_enforcement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/law_enforcement_agencies.csv"))
time.sleep(2)

client.query(regulatory_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/regulatory_bodies.csv"))
time.sleep(2)

client.query(third_party_assessor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/Third_party_asseror.csv"))
time.sleep(2)

client.query(sub_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Sub%20Requirements.csv"))
time.sleep(2)

client.query(testing_procedure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Testing%20Procedure.csv"))
time.sleep(2)

client.query(merchant_level.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Merchant%20Level.csv"))
time.sleep(2)

client.query(assessment_instrument.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Assessment%20Instruments.csv"))
time.sleep(2)

client.query(data_state.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Data%20State.csv"))
time.sleep(2)

client.query(authentication_factor.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Autentication%20Factor.csv"))
time.sleep(2)

client.query(compensating_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Compenstating%20Control.csv"))
time.sleep(2)


#Relationships
client.query(industry_standard_regulation_standard)
time.sleep(2)

client.query(standard_strategic_objective)
time.sleep(2)

client.query(strategic_objective_requirement)
time.sleep(2)

client.query(requirement_standard)
time.sleep(2)

client.query(requirement_strategic_objective)
time.sleep(2)

client.query(requirement_security_control)
time.sleep(2)

client.query(security_control_data_protection)
time.sleep(2)

client.query(security_control_components)
time.sleep(2)

client.query(card_holder_data_systems)
time.sleep(2)

client.query(card_holder_data_encryption)
time.sleep(2)

client.query(card_holder_data_channels)
time.sleep(2)

client.query(card_holder_data_protection)
time.sleep(2)

client.query(cde_system_components)
time.sleep(2)

client.query(system_component_configuration)
time.sleep(2)

client.query(internal_control_security_control)
time.sleep(2)

client.query(internal_control_card_holder)
time.sleep(2)

client.query(internal_control_requirement)
time.sleep(2)

client.query(internal_control_artifact)
time.sleep(2)

client.query(CDE_requirement)
time.sleep(2)

client.query(security_control_artifact)
time.sleep(2)

client.query(internal_role_entity)
time.sleep(2)

client.query(service_provider_card_holder)
time.sleep(2)

client.query(service_provider_controls)
time.sleep(2)

client.query(service_provider_requirements)
time.sleep(2)

client.query(service_provider_network)
time.sleep(2)

client.query(service_provider_regulatory)
time.sleep(2)

client.query(service_provider_requirement)
time.sleep(2)

client.query(acquiring_bank_compliance)
time.sleep(2)

client.query(acquiring_bank_payment_bank)
time.sleep(2)

client.query(qsa_conducts_assessment)
time.sleep(2)

client.query(asv_vulnerability_scan)
time.sleep(2)

client.query(qsa_assesses_requirement)
time.sleep(2)

client.query(asv_security_control)
time.sleep(2)

client.query(artifact_requirement)
time.sleep(2)

client.query(qsa_artifact)
time.sleep(2)

client.query(asv_artifact)
time.sleep(2)

client.query(artifact_role)
time.sleep(2)

client.query(regulatory_body_standard)
time.sleep(2)

client.query(regulatory_body_qsa)
time.sleep(2)

client.query(regulatory_body_asv)
time.sleep(2)

client.query(regulatory_body_responsible_entity)
time.sleep(2)

client.query(law_enforcement_investigates_breach)
time.sleep(2)

client.query(law_enforcement_reports_breach)
time.sleep(2)

client.query(threat_intelligence_controls)
time.sleep(2)

client.query(threat_intelligence_standard)
time.sleep(2)

client.query(responsible_entity_threat_intelligence)
time.sleep(2)

client.query(third_party_assessor_standard)
time.sleep(2)

client.query(third_party_assessor_control)
time.sleep(2)

client.query(responsible_entity_third_party_assessor)
time.sleep(2)

client.query(third_party_assessor_artifact)
time.sleep(2)

client.query(third_party_assessor_requirement)
time.sleep(2)

client.query(requirement_sub_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Requirements%20Sub%20Requirements.csv"))
time.sleep(2)

client.query(sub_requirement_procedure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Sub%20Requirements%20Testing%20Procedure.csv"))
time.sleep(2)

client.query(merchant_assessment_relationships.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Merchant%20Level%20Assement%20Instrument.csv"))
time.sleep(2)

client.query(compensating_relationships.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Sub%20Requirements%20Compensating%20Control.csv"))
time.sleep(2)

client.query(control_subreq_relationships.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Security%20Control%20Sub%20Requirements.csv"))
time.sleep(2)

client.query(cardholder_data_exists_in_state.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20CardHolder%20Data%20State.csv"))
time.sleep(2)

client.query(security_control_data_state.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Security%20Control%20Data%20State.csv"))
time.sleep(2)

client.query(auth_factor_relationships.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Sub%20Requirement%20Authentication%20Factor.csv"))
time.sleep(2)

client.query(entity_level_relationships.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/PCIDSS%20-%20Responsible%20Entity%20Merchant%20Level.csv"))
time.sleep(2)

client.query(sub_req_orphan)
time.sleep(2)

client.query(test_proc_orphan)
time.sleep(2)

client.query(merchant_level_orphan)
time.sleep(2)

client.query(assessment_orphan)
time.sleep(2)

client.query(compensating_orphan)
time.sleep(2)

client.query(auth_factor_orphan)
time.sleep(2)

client.query(data_state_orphan)
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
    with open('pcidss.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to pcidss.json")
else:
    logger.error("No data returned from the query.")

client.close()

