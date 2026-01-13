# Create PCIDSS Standard Node
from sys import intern


industry_standard_regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:IndustryStandardAndRegulation {industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  s.name =  row.name,
  s.version = row.version,
  s.publication_date = date(row.publication_date),
  s.retirement_date = date(row.retirement_date),
  s.effective_date = date(row.effective_date),
  s.mandatory_date_future = date(row.mandatory_date_future),
  s.type = row.revision_type;
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
  e.criticality = row.criticality;
"""
# Cardholder Data Nodes 
card_holder_data ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:CardholderData {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  d.name = row.node_name,
  d.data_element = row.data_element,
  d.category = row.pci_official_category,
  d.definition = row.definition,
  d.official_pci_description = row.official_pci_description,
  d.storage_allowed = row.storage_allowed,
  d.encryption_required = row.encryption_required,
  d.masking_requirement = row.masking_requirement,
  d.deletion_requirement = row.deletion_requirement,
  d.official_regulation_reference = row.official_regulation_reference,
  d.criticality = row.criticality;
"""
# CDE Environment Nodes 
cde_environment ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:CDEComponent {cde_component_id: row.cde_component_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  c.type = row.component_type,
  c.description = row.official_description,
  c.in_scope_for_pci = row.in_scope_for_pci,
  c.protection_requirements = row.protection_requirements,
  c.connectivity_to_cde = row.connectivity_to_cde,
  c.monitoring_requirements = row.monitoring_requirements,
  c.vulnerability_scanning = row.vulnerability_scanning,
  c.network_segmentation = row.network_segmentation,
  c.encryption_required = row.encryption_required,
  c.physical_access_control = row.physical_access_control,
  c.systems = row.examples_of_systems;
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
MERGE (sc:SystemComponent {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  sc.name = row.node_name,
  sc.type = row.component_type,
  sc.definition = row.definition,
  sc.in_scope_for_pci = row.in_scope_for_pci,
  sc.security_requirements = row.security_requirements,
  sc.monitoring_requirements = row.monitoring_requirements,
  sc.examples = row.examples,
  sc.update_frequency = row.update_frequency,
  sc.pci_requirement_mapping = row.pci_requirement_mapping,
  sc.criticality = row.criticality;
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
  ir.criticality = row.criticality;
"""
# Artifact Nodes
artifact ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Artifact {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  a.name           = row.node_name,
  a.type       = row.artifact_type,
  a.definition          = row.definition,
  a.pci_dss_requirement = row.pci_dss_requirement,
  a.purpose_and_use     = row.purpose_and_use,
  a.retention_period    = row.retention_period,
  a.owner               = row.owner,
  a.verification_method = row.verification_method,
  a.criticality         = row.criticality,
  a.document_frequency  = row.document_frequency,
  a.digital_or_physical = row.digital_or_physical;
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
  pb.fraud_prevention = row.fraud_prevention;
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
MERGE (ti:ThreatIntelligence {node_id: row.node_id})
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
#REGULATORY AND LAW ENFORCEMENT NODES
regulatory_and_law_enforcement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rle:RegulatoryLawEnforcement {node_id: row.node_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
ON CREATE SET
  rle.type = row.organization_type,
  rle.role_in_ecosystem = row.role_in_ecosystem,
  rle.definition = row.official_definition,
  rle.primary_responsibilities = row.primary_responsibilities,
  rle.enforcement_authority = row.enforcement_authority,
  rle.jurisdiction = row.jurisdiction,
  rle.investigation_capabilities = row.investigation_capabilities,
  rle.notification_requirements = row.notification_requirements,
  rle.cooperation_requirements = row.cooperation_requirements,
  rle.data_requests = row.data_requests,
  rle.prosecution_authority = row.prosecution_authority,
  rle.international_coordination = row.international_coordination,
  rle.incident_response_role = row.incident_response_role,
  rle.victim_support = row.victim_support,
  rle.public_reporting = row.public_reporting,
  rle.contact_information = row.contact_information,
  rle.response_time = row.response_time,
  rle.key_statutes = row.key_statutes,
  rle.evidence_requirements = row.evidence_requirements;
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








# 1. PUBLISHES (Organization -> Standard) 
pcidss_publishes ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (o:Organization {name: row.source_name, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (s:IndustryStandardAndRegulation {name: row.target_name, version: row.target_version})
MERGE (o)-[:ORGANIZATION_PUBLISHES_STANDARD]->(s);
"""
# 2. HAS_GROUP (Standard -> RequirementGroup) 
pcidss_has_group ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:IndustryStandardAndRegulation {version: row.source_standard_version})
MATCH (rg:RequirementGroup {group_id: row.target_group_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (s)-[:INDUSTRY_STANDARD_REGULATION_HAS_REQUIREMENT_GROUP]->(rg);
"""

# 3. HAS_REQUIREMENT (RequirementGroup -> Requirement) 
pcidss_has_requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rg:RequirementGroup {group_id: row.source_group_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (r:Requirement {req_id: toInteger(row.target_req_id), industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (rg)-[:REQUIREMENT_GROUP_HAS_REQUIREMENT]->(r);
"""
# 4. HAS_SUB_REQUIREMENT (Requirement -> SubRequirement) 
pcidss_has_sub_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {req_id: toInteger(row.source_req_id), industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (sr:SubRequirement {req_id: row.target_subreq_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (r)-[:REQUIREMENT_HAS_SUB_REQUIREMENT]->(sr);
"""
# 5. HAS_DEFINED_APPROACH (SubRequirement -> DefinedApproach) 
pcidss_has_defined_approach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (da:DefinedApproach {req_id: row.target_defined_approach_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[:SUB_REQUIREMENT_HAS_DEFINED_APPROACH]->(da);
"""

# 6. HAS_TEST (DefinedApproach -> TestingProcedure) 
pcidss_has_test ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (da:DefinedApproach {req_id: row.source_defined_approach_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (tp:TestingProcedure {test_id: row.target_test_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (da)-[:DEFINED_APPROACH_TESTS_TESTING_PROCEDURE]->(tp);
"""

# 7. HAS_CUSTOMIZED_OBJECTIVE (SubRequirement -> CustomizedApproachObjective) 
pcidss_has_customized_objective ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cao:CustomizedApproachObjective {req_id: row.target_customized_objective_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[:SUB_REQUIREMENT_HAS_CUSTOMIZED_OBJECTIVE]->(cao);
"""
# 8. HAS_GUIDANCE (SubRequirement -> Guidance) 
pcidss_has_guidance = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (g:Guidance {guidance_id: row.target_guidance_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sr)-[:SUB_REQUIREMENT_HAS_GUIDANCE]->(g);
"""

# 9. REQUIRES_TRA (CustomizedApproachObjective -> TargetedRiskAnalysis) 
pcidss_requires_tra = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cao:CustomizedApproachObjective {req_id: row.source_customized_objective_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (tra:TargetedRiskAnalysis {tra_id: row.target_tra_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cao)-[:REQUIRES_TARGETED_RISK_ANALYSIS]->(tra);
"""

# 10. VALIDATES (TargetedRiskAnalysis -> CustomizedControl) 
pcidss_validates ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (tra:TargetedRiskAnalysis {tra_id: row.source_tra_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cc:CustomizedControl {control_id: row.target_control_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (tra)-[:VALIDATES_CUSTOMIZED_CONTROL]->(cc);
"""

# 11. ADDRESSES (CustomizedControl -> CustomizedApproachObjective) 
pcidss_addresses ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (cc:CustomizedControl {control_id: row.source_control_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MATCH (cao:CustomizedApproachObjective {req_id: row.target_customized_objective_id, industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (cc)-[:ADDRESSES_CUSTOMIZED_APPROACH_OBJECTIVE]->(cao);
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

client.query(industry_standard_regulation.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_standard.csv"))
time.sleep(2)

client.query(organization.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_organization.csv"))
time.sleep(2)

client.query(requirement_group.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_requirement_group.csv"))
time.sleep(2)


client.query(requirement.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_requirement.csv"))
time.sleep(2)

client.query(sub_requirement.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_subrequirement.csv"))
time.sleep(2)

client.query(defined_approach.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_defined_approach.csv"))
time.sleep(2)

client.query(testing_procedure.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_testing_procedure.csv"))
time.sleep(2)

client.query(customized_approach_objective.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_customized_approach_objective.csv"))
time.sleep(2)

client.query(target_risk_analysis.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_targeted_risk_analysis.csv"))
time.sleep(2)

client.query(customized_control.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_customized_control.csv"))
time.sleep(2)

client.query(guidance.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/nodes_guidance.csv"))
time.sleep(2)

client.query(pcidss_publishes.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_publishes.csv"))
time.sleep(2)

client.query(pcidss_has_group.replace('$file_path',   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_group.csv"))
time.sleep(2)

client.query(pcidss_has_requirement.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_requirement.csv"))
time.sleep(2)

client.query(pcidss_has_sub_requirement.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_sub_requirement.csv"))
time.sleep(2)

client.query(pcidss_has_defined_approach.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_defined_approach.csv"))
time.sleep(2)

client.query(pcidss_has_test.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_test.csv"))
time.sleep(2)

client.query(pcidss_has_customized_objective.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_customized_objective.csv"))
time.sleep(2)

client.query(pcidss_has_guidance.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_has_guidance.csv"))
time.sleep(2)

client.query(pcidss_requires_tra.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_requires_tra.csv"))
time.sleep(2)

client.query(pcidss_validates.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_validates.csv"))
time.sleep(2)

client.query(pcidss_addresses.replace('$file_path',  "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/PCI%20-%20DSS/relationships_addresses.csv"))
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
with open('pci-dss.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to pci-dss.json")


client.close()

