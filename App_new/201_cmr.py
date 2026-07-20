# Regulation 
regional_standard_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET
    reg.name = "Standards for the Protection of Personal Information of Residents of the Commonwealth",
    reg.citation = "201 CMR 17.00",
    reg.version = "17.00",
    reg.effective_date = date("2010-03-01"),
    reg.type = "State Regulation",
    reg.jurisdiction = "Massachusetts, USA",
    reg.description = "Establishes minimum standards to be met in connection with the safeguarding of personal information of Massachusetts residents contained in both paper and electronic records to prevent identity theft and fraud.";
"""
# Person Node
person = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Person {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    p.node_label = row.node_label,
    p.entity_type = row.entity_type,
    p.legal_definition = row.legal_definition,
    p.primary_duty = row.primary_duty;
"""
# Resident Node
resident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Resident {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    r.node_label = row.node_label,
    r.jurisdiction = row.jurisdiction,
    r.relationship_to_data = row.relationship_to_data;
"""
# Service Provider Node
service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Resident {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    r.node_label = row.node_label,
    r.jurisdiction = row.jurisdiction,
    r.relationship_to_data = row.relationship_to_data;
"""
# Employee Node
employee = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:Employee {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    e.node_label = row.node_label,
    e.scope = row.scope,
    e.training_requirements = row.training_requirements,
    e.access_restrictions = row.access_restrictions;
"""
# Security Policies
security_policies = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:SecurityPolicy {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    sp.node_label = row.node_label,
    sp.policy_scope = row.policy_scope,
    sp.enforcement = row.enforcement;
"""
# Terminated Employee
terminated_employee = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (te:TerminatedEmployee {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    te.node_label = row.node_label,
    te.mandatory_action = row.mandatory_action,
    te.security_program_requirement = row.security_program_requirement;
"""
# Personal Information Node
personal_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pi:PersonalInformation {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    pi.node_label = row.node_label,
    pi.data_elements = row.data_elements,
    pi.exemptions = row.exemptions,
    pi.encryption_mandates = row.encryption_mandates;
"""
# Record Node
record = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Record {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    r.node_label = row.node_label,
    r.physical_form = row.physical_form,
    r.legal_definition = row.legal_definition,
    r.storage_safeguards = row.storage_safeguards;
"""
# Information Security Program Node
information_security_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (wisp:InformationSecurityProgram {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    wisp.node_label = row.node_label,
    wisp.format_requirement = row.format_requirement,
    wisp.risk_factors = row.risk_factors,
    wisp.mandatory_components = row.mandatory_components;
"""
# Portable Devices Node
portable_devices = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pd:PortableDevice {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    pd.node_label = row.node_label,
    pd.device_types = row.device_types,
    pd.encryption_mandate = row.encryption_mandate;
"""
# Breach of Security Node
breach_of_security = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (b:BreachOfSecurity {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    b.node_label = row.node_label,
    b.legal_definition = row.legal_definition,
    b.good_faith_exception = row.good_faith_exception,
    b.mandatory_actions = row.mandatory_actions;
"""
# Computer System Node
computer_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:ComputerSystem {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    cs.node_label = row.node_label,
    cs.scope = row.scope,
    cs.access_control_measures = row.access_control_measures,
    cs.monitoring_requirements = row.monitoring_requirements;
"""
# Wireless System Node
wireless_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ws:WirelessSystem {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    ws.node_label = row.node_label,
    ws.inclusion = row.inclusion,
    ws.encryption_mandate = row.encryption_mandate;
"""
# User Authentication Node
user_authentication = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ua:UserAuthentication {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    ua.node_label = row.node_label,
    ua.approved_methods = row.approved_methods,
    ua.password_security = row.password_security,
    ua.access_blocking = row.access_blocking;
"""

# System Security 
system_security = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ssa:SystemSecurityAgentSoftware {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    ssa.node_label = row.node_label,
    ssa.mandatory_components = row.mandatory_components,
    ssa.update_standards = row.update_standards;
"""
# Public Networks Node
public_networks = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PublicNetwork {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    pn.node_label = row.node_label,
    pn.network_types = row.network_types,
    pn.encryption_mandate = row.encryption_mandate;
"""
# Firewall Protection Node
firewall_protection = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fw:FirewallProtection {node_id: row.node_id, regional_standard_regulation_id: '201 CMR 17.00'})
ON CREATE SET 
    fw.node_label = row.node_label,
    fw.system_applicability = row.system_applicability,
    fw.maintenance_standards = row.maintenance_standards;
"""

# Relationships 

# Regulation to Information Security Program
reg_to_isp = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (isp:InformationSecurityProgram {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (reg)-[:REGULATION_HAS_INFORMATION_SECURITY_PROGRAM]->(isp);
"""

# Person to Personal Information
person_licenses_pi = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_OWNS_PERSONAL_INFORMATION]->(pi);
"""

# Personal Information to Resident
pi_resident = """
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (r:Resident {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (pi)-[:PERSONAL_INFORMATION_RELATES_TO_RESIDENT]->(r);
"""

# Person to Information Security Program
person_isp = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (isp:InformationSecurityProgram {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_DEVELOPS_AND_MAINTAINS_INFORMATION_SECURITY_PROGRAM]->(isp);
"""

# Information Security Program to Security Policies
isp_security_policies = """
MATCH (isp:InformationSecurityProgram {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (sp:SecurityPolicy {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (isp)-[:INFORMATION_SECURITY_PROGRAM_INCLUDES_SECURITY_POLICY]->(sp);
"""

# Person to Service Provider
person_service_provider = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (sp:ServiceProvider {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_OVERSEES_SERVICE_PROVIDER]->(sp);
"""

# Service Provider to Personal Information
service_provider_access_pi = """
MATCH (sp:ServiceProvider {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (sp)-[:SERVICE_PROVIDER_PERMITTED_ACCESS_TO_PERSONAL_INFORMATION]->(pi);
"""

# Person to Employee (Trains)
person_employee = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (e:Employee {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_TRAINS_EMPLOYEE]->(e);
"""

# Person to Employee (Disciplines)
person_imposes_disciplinary_measures_employee = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (e:Employee {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_IMPOSES_DISCIPLINARY_MEASURES_ON_EMPLOYEE]->(e);
"""

# Person to Terminated Employee
person_terminated_employee = """
MATCH (p:Person {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (te:TerminatedEmployee {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (p)-[:PERSON_PREVENTS_ACCESS_BY_TERMINATED_EMPLOYEE]->(te);
"""

# Information Security Program to Records
isp_records = """
MATCH (isp:InformationSecurityProgram {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (r:Record {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (isp)-[:INFORMATION_SECURITY_PROGRAM_PROTECTS_RECORDS]->(r);
"""

# Portable Devices to Personal Information (Stores)
portable_devices_pi = """
MATCH (pd:PortableDevice {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (pd)-[:PORTABLE_DEVICE_STORES_PERSONAL_INFORMATION]->(pi);
"""

# Public Networks to Personal Information (Transmits)
public_networks_pi = """
MATCH (pn:PublicNetwork {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (pn)-[:PUBLIC_NETWORK_TRANSMITS_PERSONAL_INFORMATION]->(pi);
"""

# Wireless System to Personal Information (Transmits)
wireless_system_pi = """
MATCH (ws:WirelessSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (ws)-[:WIRELESS_SYSTEM_TRANSMITS_PERSONAL_INFORMATION]->(pi);
"""

# Computer System to User Authentication
computer_system_user_authentication = """
MATCH (cs:ComputerSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (ua:UserAuthentication {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (cs)-[:COMPUTER_SYSTEM_REQUIRES_USER_AUTHENTICATION]->(ua);
"""

# Portable Devices Requires Encryption
portable_devices_encryption = """
MATCH (pd:PortableDevice {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (pd)-[:PORTABLE_DEVICE_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION]->(pi);
"""

# Public Networks Requires Encryption
public_networks_encryption = """
MATCH (pn:PublicNetwork {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (pn)-[:PUBLIC_NETWORK_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION]->(pi);
"""

# Wireless System Requires Encryption
wireless_system_encryption = """
MATCH (ws:WirelessSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (ws)-[:WIRELESS_SYSTEM_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION]->(pi);
"""

# Computer System Requires Firewall Protection
computer_system_firewall = """
MATCH (cs:ComputerSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (fw:FirewallProtection {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (cs)-[:COMPUTER_SYSTEM_REQUIRES_FIREWALL_PROTECTION]->(fw);
"""

# Computer System Requires System Security Agent Software
computer_system_system_security = """
MATCH (cs:ComputerSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (ssa:SystemSecurityAgentSoftware {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (cs)-[:COMPUTER_SYSTEM_REQUIRES_SYSTEM_SECURITY_AGENT_SOFTWARE]->(ssa);
"""

# Information Security Program to Computer System
isp_computer_system = """
MATCH (isp:InformationSecurityProgram {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (cs:ComputerSystem {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (isp)-[:INFORMATION_SECURITY_PROGRAM_ESTABLISHES_SECURITY_FOR_COMPUTER_SYSTEM]->(cs);
"""
# Breach of Security compromises Personal Information
breach_compromises_pi = """
MATCH (b:BreachOfSecurity {regional_standard_regulation_id: '201 CMR 17.00'})
MATCH (pi:PersonalInformation {regional_standard_regulation_id: '201 CMR 17.00'})
MERGE (b)-[:BREACH_OF_SECURITY_COMPROMISES_PERSONAL_INFORMATION]->(pi);
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

client.query(regional_standard_regulation)
time.sleep(2)

client.query(person.replace('$file_path',""))
time.sleep(2)

client.query(resident.replace('$file_path',""))
time.sleep(2)

client.query(service_provider.replace('$file_path',""))
time.sleep(2)

client.query(employee.replace('$file_path',""))
time.sleep(2)

client.query(security_policies.replace('$file_path',""))
time.sleep(2)

client.query(terminated_employee.replace('$file_path',""))
time.sleep(2)

client.query(personal_information.replace('$file_path',""))
time.sleep(2)

client.query(record.replace('$file_path',""))
time.sleep(2)

client.query(information_security_program.replace('$file_path',""))
time.sleep(2)

client.query(portable_devices.replace('$file_path',""))
time.sleep(2)

client.query(breach_of_security.replace('$file_path',""))
time.sleep(2)

client.query(computer_system.replace('$file_path',""))
time.sleep(2)

client.query(wireless_system.replace('$file_path',""))
time.sleep(2)

client.query(user_authentication.replace('$file_path',""))
time.sleep(2)

client.query(system_security.replace('$file_path',""))
time.sleep(2)

client.query(public_networks.replace('$file_path',""))
time.sleep(2)

client.query(firewall_protection.replace('$file_path',""))
time.sleep(2)                                        

# Relationships
client.query(reg_to_isp)
time.sleep(2)

client.query(person_licenses_pi)
time.sleep(2)

client.query(pi_resident)
time.sleep(2)

client.query(person_isp)
time.sleep(2)

client.query(isp_security_policies)
time.sleep(2)

client.query(person_service_provider)
time.sleep(2)

client.query(service_provider_access_pi)
time.sleep(2)

client.query(person_employee)
time.sleep(2)

client.query(person_imposes_disciplinary_measures_employee)
time.sleep(2)

client.query(person_terminated_employee)
time.sleep(2)

client.query(isp_records)
time.sleep(2)

client.query(portable_devices_pi)
time.sleep(2)

client.query(public_networks_pi)
time.sleep(2)

client.query(wireless_system_pi)
time.sleep(2)

client.query(computer_system_user_authentication)
time.sleep(2)

client.query(portable_devices_encryption)
time.sleep(2)

client.query(public_networks_encryption)
time.sleep(2)

client.query(wireless_system_encryption)
time.sleep(2)

client.query(computer_system_firewall)
time.sleep(2)

client.query(computer_system_system_security)
time.sleep(2)

client.query(isp_computer_system)
time.sleep(2)

client.query(breach_compromises_pi)
time.sleep(2)


logger.info("Graph structure loaded successfully.")

cleanup_query = """
MATCH (n)
WHERE size(labels(n)) = 0
DETACH DELETE n
"""

logger.info("Cleaning up ghost nodes (nodes with no labels)...")
client.query(cleanup_query)
logger.info("✓ Ghost nodes removed from database.")

query = """
MATCH (n)
WHERE size(labels(n)) > 0
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
    with open('201_cmr.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to 201_cmr.json")
else:
    logger.error("No data returned from the query.")

client.close()