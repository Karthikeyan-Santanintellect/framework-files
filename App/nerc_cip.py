#Industry_standard_regulation
industry_standard_regulation ="""
MERGE (r:IndustryStandardAndRegulation {industry_standard_regulation_id: "NERC_CIP 5"})
ON CREATE SET
  r.name = "NERC Critical Infrastructure Protection",
  r.version = "NERC CIP Version 5 / V6+",
  r.enactment_date = date("2008-01-17"),
  r.effective_date = date("2016-07-01"),
  r.jurisdiction = "North America (Bulk Electric System)",
  r.status = "Active",
  r.description = "A set of mandatory cybersecurity standards enforced by the North American Electric Reliability Corporation (NERC) to secure the Bulk Electric System (BES). It requires entities to identify critical assets and apply controls for electronic and physical security, personnel training, incident response, and recovery to ensure the reliability of the North American power grid.";
"""
#standard Node
standard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (std:Standard {industry_standard_regulation_id: 'NERC_CIP', standard_id: row.standard_id})
ON CREATE SET
  std.number                          = row.standard_number,
  std.name                            = row.standard_name,
  std.version                         = row.version_current,
  std.effective_date                  = row.effective_date,
  std.ferc_order                      = row.ferc_order,
  std.purpose                         = row.standard_purpose,
  std.applicability_scope             = row.applicability_scope,
  std.key_compliance_domains          = row.key_compliance_domains,
  std.development_year                = row.development_year,
  std.last_updated                    = row.last_updated,
  std.violation_severity_levels       = row.violation_severity_levels,
  std.critical_requirements_count     = row.critical_requirements_count;
"""
#Requirement Node
requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', requirement_id: row.requirement_id})
ON CREATE SET
  req.requirement_number              = row.requirement_number,
  req.standard_id                     = row.standard_id,
  req.title                           = row.requirement_title,
  req.description                     = row.requirement_description,
  req.violation_severity_level        = row.violation_severity_level,
  req.applicability_statement         = row.applicability_statement,
  req.compliance_measure              = row.compliance_measure,
  req.evidence_type                   = row.evidence_type; 
"""

#requirement_part
requirement_part ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rp:RequirementPart {industry_standard_regulation_id: 'NERC_CIP', requirement_part_id: row.requirement_part_id})
ON CREATE SET
  rp.requirement_id                   = row.requirement_id,
  rp.part_number                      = row.part_number,
  rp.description                      = row.description,
  rp.applicability                    = row.applicability,
  rp.evidence                         = row.evidence;
"""
#Domain
domain ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dom:Domain {industry_standard_regulation_id: 'NERC_CIP', domain_id: row.domain_id})
ON CREATE SET
  dom.name                            = row.domain_name,
  dom.category                        = row.domain_category,
  dom.description                     = row.description,
  dom.cip_standards_covered           = row.cip_standards_covered,
  dom.key_controls                    = row.key_controls,
  dom.applicable_entities             = row.applicable_entities,
  dom.risk_focus                      = row.risk_focus;
"""
#organization
organization ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (org:Organization {industry_standard_regulation_id: 'NERC_CIP', organization_id: row.responsible_entity_id})
ON CREATE SET
  org.name                            = row.entity_name,
  org.type                            = row.entity_type,
  org.abbreviation                    = row.entity_abbreviation,
  org.region                          = row.nerc_region,
  org.registration_status             = row.registered_status,
  org.registration_date               = row.registration_date,
  org.compliance_status               = row.compliance_history,
  org.last_audit_date                 = row.last_audit_date,
  org.annual_revenue_usd              = row.annual_revenue_usd,
  org.employee_count                  = row.employee_count,
  org.high_impact_bcs_count           = row.high_impact_bcs_count,
  org.medium_impact_bcs_count         = row.medium_impact_bcs_count,
  org.low_impact_bcs_count            = row.low_impact_bcs_count,
  org.total_bcs_count                 = row.total_bcs_count,
  org.cip_program_maturity            = row.cip_program_maturity,
  org.audit_result                    = row.audit_result,
  org.compliance_officer_designated   = row.compliance_officer_designated,
  org.security_officer_designated     = row.security_officer_designated;
"""
#BES Cyber System
bes_cyber_system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP', bcs_id: row.bcs_id})
ON CREATE SET
  bcs.name                            = row.bcs_name,
  bcs.type                            = row.bcs_type,
  bcs.impact_rating                   = row.impact_rating,
  bcs.facility_id                     = row.facility_id,
  bcs.facility_name                   = row.facility_name,
  bcs.facility_type                   = row.facility_type,
  bcs.responsible_entity_id           = row.responsible_entity,
  bcs.classification_basis            = row.classification_basis,
  bcs.associated_functions            = row.associated_functions,
  bcs.cyber_assets_count              = row.cyber_assets_count,
  bcs.esp_id                          = row.esp_id,
  bcs.cip_applicability               = row.cip_applicability;
"""
#Bes_Cyber_asset
bes_cyber_asset ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bca:BESCyberAsset {industry_standard_regulation_id: 'NERC_CIP', bca_id: row.bca_id})
ON CREATE SET
  bca.name                            = row.bca_name,
  bca.asset_type                      = row.asset_type,
  bca.asset_category                  = row.asset_category,
  bca.manufacturer                    = row.manufacturer,
  bca.model                           = row.model,
  bca.bcs_id                          = row.bcs_id,
  bca.impact_rating                   = row.impact_rating,
  bca.function                        = row.function,
  bca.operating_system                = row.operating_system,
  bca.network_accessible              = row.network_accessible,
  bca.routable_protocol               = row.routable_protocol,
  bca.ports_services                  = row.ports_services,
  bca.authentication_method           = row.authentication_method,
  bca.location                        = row.location,
  bca.firmware_version                = row.firmware_version,
  bca.patch_level                     = row.patch_level;
"""
#ESP
esp="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (esp:ElectronicSecurityPerimeter {
  industry_standard_regulation_id: 'NERC_CIP',
  esp_id: row.esp_id
})
ON CREATE SET
  esp.name                 = row.esp_name,
  esp.type                 = row.esp_type,
  esp.facility_id          = row.facility_id,
  esp.facility_type        = row.facility_type,
  esp.impact_level         = row.impact_level,
  esp.description          = row.description,
  esp.perimeter_type       = row.perimeter_type,
  esp.boundary_definition  = row.boundary_definition,
  esp.protected_assets     = row.protected_assets,
  esp.access_control_type  = row.access_control_type,
  esp.monitoring_type      = row.monitoring_type;
"""
#psp
psp ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (psp:PhysicalSecurityPerimeter {
  industry_standard_regulation_id: 'NERC_CIP',
  psp_id: row.psp_id
})
ON CREATE SET
  psp.name                 = row.psp_name,
  psp.type                 = row.psp_type,
  psp.facility_id          = row.facility_id,
  psp.facility_type        = row.facility_type,
  psp.impact_level         = row.impact_level,
  psp.description          = row.description,
  psp.perimeter_type       = row.perimeter_type,
  psp.boundary_definition  = row.boundary_definition,
  psp.protected_assets     = row.protected_assets,
  psp.access_control_type  = row.access_control_type,
  psp.surveillance_type    = row.surveillance_type,
  psp.cip_014_critical     = row.cip_014_critical;
"""
#Role (Internal Roles)
roles ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (role:Role {
  industry_standard_regulation_id: 'NERC_CIP',
  role_id: row.internal_role_id
})
ON CREATE SET
  role.name                = row.role_name,
  role.category            = row.role_category,
  role.organization_level  = row.organization_level,
  role.responsible_for     = row.responsible_for,
  role.required_training   = row.required_training,
  role.required_clearance  = row.required_clearance,
  role.access_level        = row.access_level,
  role.accountability      = row.accountability,
  role.cip_requirement     = row.cip_requirement,
  role.titles      = row.example_titles;
"""

#Artifact
artifact ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (art:Artifact {
  industry_standard_regulation_id: 'NERC_CIP',
  artifact_id: row.artifact_id
})
ON CREATE SET
  art.name                  = row.artifact_name,
  art.type                  = row.artifact_type,
  art.category              = row.artifact_category,
  art.evidence_category     = row.evidence_category,
  art.related_standard      = row.related_standard,
  art.related_requirement   = row.related_requirement,
  art.description           = row.description,
  art.retention_period      = row.retention_period,
  art.storage_location      = row.storage_location,
  art.access_control        = row.access_control,
  art.confidentiality_level = row.confidentiality_level,
  art.cip_evidence_level    = row.cip_evidence_level,
  art.responsible_party     = row.responsible_party,
  art.update_frequency      = row.update_frequency,
  art.bcsi_content          = row.bcsi_content;
  """
#regulator
regulator ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:Regulator {
  industry_standard_regulation_id: 'NERC_CIP',
  regulator_id: row.regulator_id
})
ON CREATE SET
  reg.name                 = row.regulator_name,
  reg.type                 = row.regulator_type,
  reg.jurisdiction         = row.jurisdiction,
  reg.enforcement_authority= row.enforcement_authority,
  reg.primary_function     = row.primary_function,
  reg.regulated_entities   = row.regulated_entities,
  reg.compliance_oversight = row.compliance_oversight,
  reg.audit_authority      = row.audit_authority,
  reg.penalty_authority    = row.penalty_authority,
  reg.coordination_role    = row.coordination_role,
  reg.contact_method       = row.contact_method;
"""

#vendor
vendor ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vnd:Vendor {
  industry_standard_regulation_id: 'NERC_CIP',
  vendor_id: row.vendor_id
})
ON CREATE SET
  vnd.name                        = row.vendor_name,
  vnd.type                        = row.vendor_type,
  vnd.category                    = row.vendor_category,
  vnd.products_services           = row.products_services,
  vnd.served_industries           = row.served_industries,
  vnd.company_size                = row.company_size,
  vnd.headquarters_location       = row.headquarters_location,
  vnd.annual_revenue_range        = row.annual_revenue_range,
  vnd.cybersecurity_certifications= row.cybersecurity_certifications,
  vnd.cip_experience              = row.cip_experience,
  vnd.vendor_assessment_required  = row.vendor_assessment_required,
  vnd.notable_clients             = row.notable_clients,
  vnd.market_position             = row.market_position,
  vnd.supply_chain_risk           = row.supply_chain_risk;
"""
#ExternalNetwork
external_network ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (net:ExternalNetwork {
  industry_standard_regulation_id: 'NERC_CIP',
  network_id: row.external_network_id
})
ON CREATE SET
  net.name                       = row.network_name,
  net.type                       = row.network_type,
  net.category                   = row.network_category,
  net.owner_operator            = row.owner_operator,
  net.trust_level               = row.trust_level,
  net.connectivity_type         = row.connectivity_type,
  net.security_boundary         = row.security_boundary,
  net.typical_protocols         = row.typical_protocols,
  net.access_control_requirements = row.access_control_requirements,
  net.monitoring_requirements   = row.monitoring_requirements,
  net.data_classification       = row.data_classification,
  net.encryption_required       = row.encryption_required,
  net.risk_profile              = row.risk_profile;
"""
#ThreatIntelligence
threat_intelligence ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ti:ThreatIntelligence {
  industry_standard_regulation_id: 'NERC_CIP',
  threat_id: row.threat_intel_id
})
ON CREATE SET
  ti.name                 = row.source_name,
  ti.source_type          = row.source_type,
  ti.organization         = row.organization,
  ti.coverage_area        = row.coverage_area,
  ti.information_type     = row.information_type,
  ti.distribution_model   = row.distribution_model,
  ti.access_requirements  = row.access_requirements,
  ti.update_frequency     = row.update_frequency,
  ti.reliability_rating   = row.reliability_rating,
  ti.timeliness           = row.timeliness,
  ti.focus_sectors        = row.focus_sectors,
  ti.threat_categories    = row.threat_categories,
  ti.cost_model           = row.cost_model,
  ti.cip_relevance        = row.cip_relevance;
"""

#LawEnforcement
law_enforcement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (le:LawEnforcement {
  industry_standard_regulation_id: 'NERC_CIP',
  agency_id: row.law_enforcement_id
})
ON CREATE SET
  le.name                  = row.agency_name,
  le.type                  = row.agency_type,
  le.jurisdiction          = row.jurisdiction,
  le.primary_mission       = row.primary_mission,
  le.cip_coordination_role = row.cip_coordination_role,
  le.contact_method        = row.contact_method,
  le.response_capability   = row.response_capability,
  le.specialized_units     = row.specialized_units,
  le.authority_level       = row.authority_level,
  le.partnership_programs  = row.partnership_programs,
  le.response_time         = row.response_time;
"""
#Relationships
#IndustryStandardAndRegulation → Standard
regulation_standard_rel = """
MATCH (isr:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (isr)-[:INDUSTRY_STANDARD_AND_REGULATION_HAS_STANDARD {relationship_type: 'Framework_Standard'}]->(std);
"""
#IndustryStandardAndRegulation → Organization
regulation_organization_rel = """
MATCH (isr:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (isr)-[:INDUSTRY_STANDARD_AND_REGULATION_APPLIES_TO_ORGANIZATION {relationship_type: 'Framework_Entity'}]->(org);
"""
#standard-> requirement
standard_requirement = """
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', standard_id: std.standard_id})
MERGE (std)-[:STANDARD_CONTAINS_REQUIREMENT {relationship_type: 'Standard_Requirement'}]->(req);
"""
#requirement -> requirement part
requirement_requirement_part = """
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (rp:RequirementPart {industry_standard_regulation_id: 'NERC_CIP', requirement_id: req.requirement_id})
MERGE (req)-[:REQUIREMENT_HAS_PART {relationship_type: 'Requirement_Part'}]->(rp);
"""
#standard -> domain
standard_domain = """
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (dom:Domain {industry_standard_regulation_id: 'NERC_CIP'})
WHERE dom.cip_standards_covered CONTAINS std.number
MERGE (std)-[:STANDARD_ADDRESSES_DOMAIN {relationship_type: 'Standard_Domain'}]->(dom);
"""
#Doamin -> requirement
domain_requirement = """
MATCH (dom:Domain {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP'})
WHERE dom.cip_standards_covered CONTAINS req.standard_id
MERGE (dom)-[:DOMAIN_IMPLEMENTS_REQUIREMENT {relationship_type: 'Domain_Requirement'}]->(req);
"""

# ORGANIZATION_OWNS_BES_CYBER_SYSTEM
organization_bes_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP', responsible_entity_id: org.organization_id})
MERGE (org)-[:ORGANIZATION_OWNS_BES_CYBER_SYSTEM {relationship_type: 'Entity_BCS'}]->(bcs);
"""

# Organization → BESCyberSystem
organization_bcs_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP', responsible_entity_id: org.organization_id})
MERGE (org)-[:ORGANIZATION_OWNS_BES_CYBER_SYSTEM {relationship_type: 'Entity_BCS_Operation'}]->(bcs);
"""

# BESCyberSystem → BESCyberAsset
bes_cyber_asset_rel = """
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (bca:BESCyberAsset {industry_standard_regulation_id: 'NERC_CIP', bcs_id: bcs.bcs_id})
MERGE (bcs)-[:BES_CYBER_SYSTEM_CONTAINS_BES_CYBER_ASSET {relationship_type: 'BCS_Asset'}]->(bca);
"""

# BESCyberSystem → ElectronicSecurityPerimeter
bes_cyber_system_esp_rel = """
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (esp:ElectronicSecurityPerimeter {industry_standard_regulation_id: 'NERC_CIP', esp_id: bcs.esp_id})
MERGE (bcs)-[:BES_PROTECTED_BY_ELECTRONIC_SECURITY_PERIMETER {protection_type: 'Electronic', basis: 'CIP-005'}]->(esp);
"""

# BESCyberSystem → PhysicalSecurityPerimeter
bes_cyber_system_psp_rel = """
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (psp:PhysicalSecurityPerimeter {industry_standard_regulation_id: 'NERC_CIP', facility_id: bcs.facility_id})
MERGE (bcs)-[:BES_PROTECTED_BY_PHYSICAL_SECURITY_PERIMETER {protection_type: 'Physical', basis: 'CIP-006'}]->(psp);
"""
#BESCyberAsset → Vendor
manages_vulnerability_rel = """
MATCH (bca:BESCyberAsset {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (vnd:Vendor {industry_standard_regulation_id: 'NERC_CIP'})
WHERE bca.manufacturer = vnd.name
MERGE (bca)-[:BES_ASSET_MANUFACTURED_BY_VENDOR {relationship_type: 'Asset_Vendor'}]->(vnd);
"""
#Organization → Vendor
organization_vendor_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (vnd:Vendor {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_ENGAGES_VENDOR {relationship_type: 'Supply_Chain', basis: 'CIP-013'}]->(vnd);
"""
#Organization → Role
organization_role_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (role:Role {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_EMPLOYS_ROLE {relationship_type: 'Personnel', basis: 'CIP-004'}]->(role);
"""
#Organization → Artifact
organization_artifact_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (art:Artifact {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_MAINTAINS_ARTIFACT {relationship_type: 'Evidence_Management', basis: 'CIP-011'}]->(art);
"""
#Artifact → Standard
artifact_standard = """
MATCH (art:Artifact {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP', standard_id: art.related_standard})
MERGE (art)-[:ARTIFACT_EVIDENCES_STANDARD {relationship_type: 'Evidence_Standard'}]->(std);
"""
#Artifact → Requirement
artifact_requirement = """
MATCH (art:Artifact {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', requirement_id: art.related_requirement})
MERGE (art)-[:ARTIFACT_EVIDENCES_REQUIREMENT {relationship_type: 'Evidence_Requirement'}]->(req);
"""
#Organization → Regulator
organization_regulator = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (reg:Regulator {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_REGULATED_BY_REGULATOR {relationship_type: 'Oversight', enforcement: 'CMEP'}]->(reg);
"""
#Regulator → Standard
regulator_standard = """
MATCH (reg:Regulator {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (reg)-[:REGULATOR_REGULATES_STANDARD {relationship_type: 'Regulatory_Enforcement'}]->(std);
"""
#BESCyberSystem → ExternalNetwork
bes_cyber_system_external_network = """
MATCH (bcs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (net:ExternalNetwork {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (bcs)-[:BES_PROTECTED_BY_NETWORK {relationship_type: 'Network_Connection', basis: 'CIP-005'}]->(net);
"""
#Organization → ExternalNetwork
organization_external_network ="""
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (net:ExternalNetwork {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_USES_NETWORK {relationship_type: 'Network_Usage', basis: 'CIP-012'}]->(net);
"""
#Organization → ThreatIntelligence
organization_threat_intelligence = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (ti:ThreatIntelligence {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_MONITORS_THREAT_INTELLIGENCE {relationship_type: 'Threat_Monitoring', basis: 'CIP-015'}]->(ti);
"""
#BESCyberAsset → ThreatIntelligence
bes_cyber_asset_threat_intelligence = """
MATCH (bca:BESCyberAsset {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (ti:ThreatIntelligence {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (bca)-[:BES_ASSET_THREAT_INTELLIGENCE {relationship_type: 'Asset_Monitoring', basis: 'CIP-015'}]->(ti);
"""
#Organization → LawEnforcement
organization_law_enforcement = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (le:LawEnforcement {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (org)-[:ORGANIZATION_COORDINATES_LAW_ENFORCEMENT {relationship_type: 'Incident_Coordination', basis: 'CIP-008'}]->(le);
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
client.query(industry_standard_regulation)
time.sleep(2)

client.query(organization.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_Organization_nodes.csv'))
time.sleep(2)

client.query(BESCyberSystem.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_BESCyberSystem_nodes.csv'))
time.sleep(2)

client.query(CIPStandard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_CIPStandard_nodes.csv'))
time.sleep(2)

client.query(ElectronicSecurityPerimeter.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_ElectronicSecurityPerimeter_nodes.csv'))
time.sleep(2)

client.query(Asset.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_Asset_nodes.csv'))
time.sleep(2)

client.query(CyberThreat.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_CyberThreat_nodes.csv'))
time.sleep(2)

client.query(AccessPoint.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_AccessPoint_nodes.csv'))
time.sleep(2)

client.query(CriticalFacility.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_CriticalFacility_nodes.csv'))
time.sleep(2)

client.query(IncidentResponse.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_IncidentResponse_nodes.csv'))
time.sleep(2)

client.query(VulnerabilityManagement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_VulnerabilityManagement_nodes.csv'))
time.sleep(2)

#Relationships
client.query(regulation_organization_rel)
time.sleep(2)

client.query(organization_bes_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_OWNS_BES_CYBER_SYSTEM_relationships.csv'))
time.sleep(2)

client.query(implements_cip_standard_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_IMPLEMENTS_CIP_STANDARD_relationships.csv'))
time.sleep(2) 

client.query(defines_security_perimeter_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_DEFINES_SECURITY_PERIMETER_relationships.csv'))
time.sleep(2)

client.query(protects_critical_asset_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_PROTECTS_CRITICAL_ASSET_relationships.csv'))
time.sleep(2)

client.query(manages_access_control_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_MANAGES_ACCESS_CONTROL_relationships.csv'))
time.sleep(2)   


client.query(manages_vulnerability_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_MANAGES_VULNERABILITY_relationships.csv'))
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
with open('nerc_cip.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nerc_cip.json")


client.close()





















 

    
























 




 



 

 

