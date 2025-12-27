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
#Organization Node
organization ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.organization_id})
ON CREATE SET
  org.name                    = row.name,
  org.type                    = row.entity_type,
  org.region                 = row.nerc_region,
  org.registration_date       = date(row.registration_date),
  org.compliance_status       = row.compliance_status,
  org.last_audit_date         = date(row.last_audit_date),
  org.next_audit_due          = date(row.next_audit_due),
  org.bes_asset_count  = row.bes_asset_count,
 org.ciso_name  = row.ciso_name,
 org.ciso_contact_email  = row.ciso_contact_email;
"""
#BESCyberSystem Node
BESCyberSystem ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP 5', system_id: row.system_id})
ON CREATE SET
    bs.name = row.system_name,
    bs.type = row.system_type,
    bs.impact_level = row.impact_level,
    bs.critical_function = row.critical_function,
    bs.location = row.location,
    bs.connected_assets_count = row.connected_assets_count,
    bs.operates_in_esop = row.operates_in_esop,
    bs.backup_recovery_capability = row.backup_recovery_capability,
    bs.mean_time_to_recovery = row.mean_time_to_recovery;
"""
#CIPStandard
CIPStandard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:CIPStandard {industry_standard_regulation_id: 'NERC_CIP 5', standard_id: row.standard_id})
ON CREATE SET
    cs.version = row.version,
    cs.name = row.title,
    cs.release_date = date(row.release_date),
    cs.effective_date = date(row.effective_date),
    cs.control_areas = row.control_areas;
"""
#ElectronicSecurityPerimeter
ElectronicSecurityPerimeter ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (es:ElectronicSecurityPerimeter {industry_standard_regulation_id: 'NERC_CIP 5', perimeter_id: row.perimeter_id})
ON CREATE SET
    es.name = row.name,
    es.type = row.perimeter_type,
    es.access_point_count = row.access_point_count,
    es.monitored_systems_count = row.monitored_systems_count,
    es.logging_enabled = row.logging_enabled,
    es.intrusion_detection_active = row.intrusion_detection_active,
    es.air_gapped = row.air_gapped;
"""
#Asset
Asset ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Asset {industry_standard_regulation_id: 'NERC_CIP 5', asset_id: row.asset_id})
ON CREATE SET
    a.name = row.asset_name,
    a.type = row.asset_type,
    a.location = row.location,
    a.criticality_level = row.criticality_level,
    a.operational_status = row.operational_status,
    a.last_maintenance_date = date(row.last_maintenance_date),
    a.backup_asset_id = row.backup_asset_id;
"""
#CyberThreat
CyberThreat ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:CyberThreat {industry_standard_regulation_id: 'NERC_CIP 5', threat_id: row.threat_id})
ON CREATE SET
    ct.name = row.threat_name,
    ct.category = row.threat_category,
    ct.severity_level = row.severity_level,
    ct.count = row.affected_systems_count,
    ct.description = row.threat_description,
    ct.attack_vector = row.attack_vector,
    ct.remediation_status = row.remediation_status;
"""
#AccessPoint
AccessPoint ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AccessPoint {industry_standard_regulation_id: 'NERC_CIP 5', access_point_id: row.access_point_id})
ON CREATE SET
    ap.name = row.point_name,
    ap.type = row.access_type,
    ap.protected_system_id = row.protected_system_id,
    ap.access_control_method = row.access_control_method,
    ap.authentication_required = row.authentication_required,
    ap.approval_process = row.approval_process,
    ap.monitoring_active = row.monitoring_active;
"""
#CriticalFacility
CriticalFacility ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:CriticalFacility {industry_standard_regulation_id: 'NERC_CIP 5', facility_id: row.facility_id})
ON CREATE SET
    cf.name = row.facility_name,
    cf.type = row.facility_type,
    cf.location = row.location,
    cf.rating = row.criticality_rating,
    cf.backup_facility_id = row.backup_facility_id,
    cf.level = row.physical_security_level,
    cf.cctv_monitoring_active = row.cctv_monitoring_active;
"""
#IncidentResponse
IncidentResponse ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:IncidentResponse {industry_standard_regulation_id: 'NERC_CIP 5', incident_id: row.response_plan_id})
ON CREATE SET
    ir.name = row.plan_name,
    ir.category = row.incident_category,
    ir.size = row.response_team_size,
    ir.time_minutes = row.response_time_minutes,
    ir.last_drill_date = date(row.last_drill_date),
    ir.nerc_notification_required = row.nerc_notification_required;
"""
#VulnerabilityManagement
VulnerabilityManagement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vm:VulnerabilityManagement {industry_standard_regulation_id: 'NERC_CIP 5', vulnerability_id: row.vuln_mgmt_id})
ON CREATE SET
    vm.name = row.program_name,
    vm.responsible_team = row.responsible_team,
    vm.scan_frequency = row.scan_frequency,
    vm.open_vulnerabilities_critical = row.open_vulnerabilities_critical,
    vm.patch_management_process = row.patch_management_process;
"""
#Relationships
#regulation -> organization
regulation_organization_rel = """
MATCH (r:IndustryStandardAndRegulation {industry_standard_regulation_id: "NERC_CIP 5"})
MATCH (o:Organization {industry_standard_regulation_id: 'NERC_CIP 5'})
MERGE (r)-[:REGULATION_GOVERNS_ORGANIZATION]->(o);
"""

# ORGANIZATION_OWNS_BES_CYBER_SYSTEM
organization_bes_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.source_organization_id})
MATCH (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP 5', system_id: row.target_system_id})
MERGE (org)-[r:ORGANIZATION_OWNS_BES_CYBER_SYSTEM {relationship_type: row.relationship_type}]->(bs)
ON CREATE SET
    r.ownership_start_date = date(row.ownership_start_date),
    r.operational_responsibility = row.operational_responsibility,
    r.maintenance_responsibility = row.maintenance_responsibility,
    r.security_responsibility = row.security_responsibility;
"""

# ORGANIZATION_IMPLEMENTS_CIP_STANDARD
implements_cip_standard_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.source_organization_id})
MATCH (cs:CIPStandard {industry_standard_regulation_id: 'NERC_CIP 5', standard_id: row.target_standard_id})
MERGE (org)-[r:ORGANIZATION_IMPLEMENTS_CIP_STANDARD {relationship_type: row.relationship_type}]->(cs)
ON CREATE SET
    r.implementation_date = date(row.implementation_date),
    r.compliance_level = row.compliance_level,
    r.compliance_percentage = row.compliance_percentage;
"""

# DEFINES_SECURITY_PERIMETER 
defines_security_perimeter_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP 5', system_id: row.source_system_id})
MATCH (es:ElectronicSecurityPerimeter {industry_standard_regulation_id: 'NERC_CIP 5', perimeter_id: row.target_perimeter_id})
MERGE (bs)-[r:BES_CYBER_SYSTEM_DEFINES_SECURITY_PERIMETER {relationship_type: row.relationship_type}]->(es)
ON CREATE SET
    r.definition_date = date(row.definition_date),
    r.documentation_reference = row.documentation_reference,
    r.reviewed_date = date(row.reviewed_date);
"""

# PROTECTS_CRITICAL_ASSET 
protects_critical_asset_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP 5', system_id: row.source_system_id})
MATCH (a:Asset {industry_standard_regulation_id: 'NERC_CIP 5', asset_id: row.target_asset_id})
MERGE (bs)-[r:BES_CYBER_SYSTEM_PROTECTS_CRITICAL_ASSET {relationship_type: row.relationship_type}]->(a)
ON CREATE SET
    r.protection_start_date = date(row.protection_start_date),
    r.protection_level = row.protection_level,
    r.effectiveness_rating = row.effectiveness_rating;
"""

# MANAGES_ACCESS_CONTROL
manages_access_control_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.source_organization_id})
MATCH (ap:AccessPoint {industry_standard_regulation_id: 'NERC_CIP 5', access_point_id: row.target_access_point_id})
MERGE (org)-[r:ORGANIZATION_MANAGES_ACCESS_CONTROL {relationship_type: row.relationship_type}]->(ap)
ON CREATE SET
    r.access_control_start_date = date(row.access_control_start_date),
    r.access_control_type = row.access_control_type,
    r.unauthorized_access_incidents = row.unauthorized_access_incidents;
"""



# RESPONDS_TO_INCIDENT 
responds_to_incident_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.source_organization_id})
MATCH (ir:IncidentResponse {industry_standard_regulation_id: 'NERC_CIP 5', incident_response_id: row.target_incident_id})
MERGE (org)-[r:ORGANIZATION_RESPONDS_TO_INCIDENT {relationship_type: row.relationship_type}]->(ir)
ON CREATE SET
    r.plan_effective_date = date(row.plan_effective_date),
    r.coverage_scope = row.coverage_scope,
    r.test_success_percentage = row.test_success_percentage;
"""

# MANAGES_VULNERABILITY
manages_vulnerability_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP 5', organization_id: row.source_organization_id})
MATCH (vm:VulnerabilityManagement {industry_standard_regulation_id: 'NERC_CIP 5', vulnerability_id: row.target_vuln_mgmt_id})
MERGE (org)-[r:ORGANIZATION_MANAGES_VULNERABILITY {relationship_type: row.relationship_type}]->(vm)
ON CREATE SET
    r.program_start_date = date(row.program_start_date),
    r.scanning_frequency = row.scanning_frequency,
    r.remediation_sla = row.remediation_sla,
    r.critical_unpatched_count = row.critical_unpatched_count;
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

client.query(responds_to_incident_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_RESPONDS_TO_INCIDENT_relationships.csv'))
time.sleep(2)

client.query(manages_vulnerability_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NERC/NERC_MANAGES_VULNERABILITY_relationships.csv'))
time.sleep(2)

 
logger.info("Graph structure loaded successfully.")

res = client.query("""
    MATCH path = (:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})-[*1..5]-()
    UNWIND nodes(path) as n
    UNWIND relationships(path) as r
    WITH collect(DISTINCT n) AS uniqueNodes, collect(DISTINCT r) AS uniqueRels
    RETURN {
      nodes: [node IN uniqueNodes | node {
        .*,
        id: elementId(node),
        labels: labels(node),
        mainLabel: head(labels(node))
      }],
      rels: [rel IN uniqueRels | rel {
        .*,
        id: elementId(rel),
        type: type(rel),
        from: elementId(startNode(rel)),
        to: elementId(endNode(rel))
      }]
    } AS graph_data
""")



graph = res[0]["graph_data"]   

import json
with open("nerc_cip.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(graph, default=str, indent=2))

logger.info("✓ Exported graph data to nerc_cip.json")
client.close()





















 

    
























 




 



 

 

