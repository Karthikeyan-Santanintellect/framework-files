#Industry_standard_regulation
industry_standard_regulation ="""
MERGE (r:IndustryStandardAndRegulation {industry_standard_regulation_id: "NERC_CIP"})
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
MERGE (org:Organization {industry_standard_regulation_id: 'NERC_CIP', organization_id: row.organization_id})
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
MERGE (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP', system_id: row.system_id})
ON CREATE SET
    bs.name = row.system_name,
    bs.type = row.system_type,
    bs.impact_level = row.impact_level,
    bs.critical_function = row.critical_function,
    bs.location = row.location;
    bs.connected_assets_count = row.connected_assets_count,
    bs.operates_in_esop = row.operates_in_esop,
    bs.backup_recovery_capability = row.backup_recovery_capability
    bs.mean_time_to_recovery = row.mean_time_to_recovery;
"""
#CIPStandard
CIPStandard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:CIPStandard {industry_standard_regulation_id: 'NERC_CIP', standard_id: row.standard_id})
ON CREATE SET
    cs.version = row.version,
    cs.title = row.title,
    cs.release_date = date(row.release_date),
    cs.effective_date = date(row.effective_date),
    cs.control_areas = row.control_areas;
"""
#ElectronicSecurityPerimeter
ElectronicSecurityPerimeter ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (es:ElectronicSecurityPerimeter {industry_standard_regulation_id: 'NERC_CIP', perimeter_id: row.perimeter_id})
ON CREATE SET
    es.name = row.name,
    es.perimeter_type = row.perimeter_type,
    es.access_point_count = row.access_point_count,
    es.monitored_systems_count = row.monitored_systems_count,
    es.logging_enabled = row.logging_enabled,
    es.intrusion_detection_active = row.intrusion_detection_active,
    es.air_gapped = row.air_gapped;
"""
#Asset
Asset ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Asset {industry_standard_regulation_id: 'NERC_CIP', asset_id: row.asset_id})
ON CREATE SET
    a.asset_name = row.asset_name,
    a.asset_type = row.asset_type,
    a.location = row.location,
    a.criticality_level = row.criticality_level,
    a.operational_status = row.operational_status,
    a.last_maintenance_date = date(row.last_maintenance_date),
    a.backup_asset_id = row.backup_asset_id;
"""
#CyberThreat
CyberThreat ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:CyberThreat {industry_standard_regulation_id: 'NERC_CIP', threat_id: row.threat_id})
ON CREATE SET
    ct.name = row.threat_name,
    ct.threat_category = row.threat_category,
    ct.severity_level = row.severity_level,
    ct.affected_systems_count = row.affected_systems_count,
    ct.description = row.threat_description,
    ct.attack_vector = row.attack_vector,
    ct.remediation_status = row.remediation_status;
"""
#AccessPoint
AccessPoint ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AccessPoint {industry_standard_regulation_id: 'NERC_CIP', access_point_id: row.access_point_id})
ON CREATE SET
    ap.point_name = row.point_name,
    ap.access_type = row.access_type,
    ap.protected_system_id = row.protected_system_id,
    ap.access_control_method = row.access_control_method,
    ap.authentication_required = row.authentication_required,
    ap.approval_process = row.approval_process,
    ap.monitoring_active = row.monitoring_active;
"""
#CriticalFacility
CriticalFacility ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:CriticalFacility {industry_standard_regulation_id: 'NERC_CIP', facility_id: row.facility_id})
ON CREATE SET
    cf.name = row.facility_name,
    cf.type = row.facility_type,
    cf.location = row.location,
    cf.criticality_rating = row.criticality_rating,
    cf.backup_facility_id = row.backup_facility_id,
    cf.physical_security_level = row.physical_security_level,
    cf.cctv_monitoring_active = row.cctv_monitoring_active;
"""
#IncidentResponse
IncidentResponse ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:IncidentResponse {industry_standard_regulation_id: 'NERC_CIP', incident_id: row.response_plan_id})
ON CREATE SET
    ir.plan_name = row.plan_name,
    ir.incident_category = row.incident_category,
    ir.response_team_size = row.response_team_size,
    ir.response_time_minutes = row.response_time_minutes,
    ir.last_drill_date = date(row.last_drill_date),
    ir.nerc_notification_required = row.nerc_notification_required;
"""
#VulnerabilityManagement
VulnerabilityManagement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (vm:VulnerabilityManagement {industry_standard_regulation_id: 'NERC_CIP', vulnerability_id: row.vuln_mgmt_id})
ON CREATE SET
    vm.name = row.program_name
    vm.responsible_team = row.responsible_team,
    vm.scan_frequency = row.scan_frequency,
    vm.open_vulnerabilities_critical = row.open_vulnerabilities_critical
    vm.patch_management_process = row.patch_management_process;
"""
#Relationships
#organization_bes
organization_bes_rel = """
MATCH (org:Organization {industry_standard_regulation_id: 'NERC_CIP',row.source_organization_id})
MATCH (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP',row.target_system_id})
MERGE (org) -[r:ORGANIZATION_OWNS_BES_CYBER_SYSTEM{relationship_type: row.relationship_type}]-> (bs)
ON CREATE SET
    r.ownership_start_date = date(row.ownership_start_date),
    r.operational_responsibility = row.operational_responsibility,
    r.maintenance_responsibility = row.maintenance_responsibility,
    r.security_responsibility = row.security_responsibility;
"""
#IMPLEMENTS_CIP_STANDARD
implements_cip_standard_rel = """
MATCH (bs:BESCyberSystem {industry_standard_regulation_id: 'NERC_CIP',row.source_system_id})
MATCH (cs:CIPStandard {industry_standard_regulation_id: 'NERC_CIP',row.target_standard_id})























"""


 

    
























 




 



 

 

