#Regulation
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_and_regulation_id: 'dpdpa_2023'})
ON CREATE SET 
  reg.name = 'Digital Personal Data Protection Act, 2023',
  reg.citation = 'Act No. 22 of 2023',
  reg.version = '1.0',
  reg.status = 'Active',
  reg.effective_date = '2023-08-04',
  reg.jurisdiction = 'India',
  reg.description = 'Comprehensive framework for processing digital personal data in India';
"""
#Chapter
chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {regional_standard_and_regulation_id:'dpdpa_2023', chapter_id: row.chapter_id})
ON CREATE SET 
  c.chapter_number = row.chapter_number,
  c.title = row.title,
  c.description = row.description;
"""
#Section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {regional_standard_and_regulation_id:'dpdpa_2023', section_id: row.section_id})
ON CREATE SET 
  sec.section_number = row.section_number,
  sec.chapter_id = row.chapter_id,
  sec.title = row.title;
"""
#Requirement
requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
ON CREATE SET 
  req.section_id = row.section_id,
  req.text = row.requirement_text,
  req.type = row.requirement_type,
  req.priority = row.priority,
  req.status = row.status;
"""
#role
role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_and_regulation_id:'dpdpa_2023', role_id: row.role_id})
ON CREATE SET 
  ro.name = row.name,
  ro.description = row.description,
  ro.category = row.category;
"""
#datacategory
datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_and_regulation_id:'dpdpa_2023', data_id: row.data_id})
ON CREATE SET 
  dc.name = row.name,
  dc.description = row.description,
  dc.category = row.category,
  dc.definition_section = row.definition_section,
  dc.requires_consent = row.requires_consent;
"""
#safeguard
safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_and_regulation_id:'dpdpa_2023', safeguard_id: row.safeguard_id})
ON CREATE SET 
  sg.name = row.name,
  sg.description = row.description,
  sg.type = row.type,
  sg.applies_to_section = row.applies_to_section;
"""
#event_type
event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_and_regulation_id:'dpdpa_2023', event_type_id: row.event_type_id})
ON CREATE SET 
  ett.name = row.name,
  et.description = row.description,
  et.deadline = row.deadline,
  et.extendable = row.extendable,
  et.extension_period = row.extension_period,
  et.cost = row.cost;
"""
#policy
policy ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {regional_standard_and_regulation_id:'dpdpa_2023', policy_id: row.policy_id})
ON CREATE SET 
  pol.name = row.name,
  pol.description = row.description,
  pol.owner = row.owner,
  pol.version = row.version,
  pol.effective_date = date(row.effective_date);
"""
#control
control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_and_regulation_id:'dpdpa_2023', control_id: row.control_id})
ON CREATE SET 
  co.name = row.name,
  co.category = row.category,
  co.owner = row.owner,
  co.description = row.description;
"""
#system
system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System {regional_standard_and_regulation_id:'dpdpa_2023', system_id: row.system_id})
ON CREATE SET 
  sys.name = row.name,
  sys.type = row.type,
  sys.description = row.description,
  sys.category = row.category,
  sys.holds_personal_data = row.holds_personal_data,
  sys.holds_sensitive_data = row.holds_sensitive_data,
  sys.processing_activities = row.processing_activities;
"""
#process
process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pr:Process {regional_standard_and_regulation_id:'dpdpa_2023', process_id: row.process_id})
ON CREATE SET 
  pr.name = row.name,
  pr.description = row.description,
  pr.owner = row.owner,
  pr.frequency = row.frequency,
  pr.deadline = row.deadline;
"""
#enforcement_action
enforcement_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_and_regulation_id:'dpdpa_2023', enforcement_id: row.enforcement_id})
ON CREATE SET 
 ea.name = row.name,
  ea.description = row.description,
  ea.type = row.type,
  ea.authority = row.authority,
  ea.severity_level = row.severity_level,
  ea.applicable_section = row.applicable_section;
"""
#requirement->roles
requirement_roles ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (ro:Role {regional_standard_and_regulation_id:'dpdpa_2023', role_id: row.role_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_ROLES]->(ro);
"""
#requirement->datacategory
requirement_datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (dc:DataCategory {regional_standard_and_regulation_id:'dpdpa_2023', data_id: row.data_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_DATACATEGORY]->(dc);
"""
#requirement->safeguard
requirement_safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (sg:Safeguard {regional_standard_and_regulation_id:'dpdpa_2023', safeguard_id: row.safeguard_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_SAFEGUARD]->(sg);
"""
#requirement->event_type
requirement_event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (et:EventType {regional_standard_and_regulation_id:'dpdpa_2023', event_type_id: row.event_type_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_EVENTTYPE]->(et);
"""
#requirement->policy
requirement_policy ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (pol:Policy {regional_standard_and_regulation_id:'dpdpa_2023', policy_id: row.policy_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_POLICY]->(pol);
"""
#requirement->control
requirement_control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_id})
MATCH (co:Control {regional_standard_and_regulation_id:'dpdpa_2023', control_id: row.control_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_CONTROL]->(co);
""" 
#control->system
control_system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:Control {regional_standard_and_regulation_id:'dpdpa_2023', control_id: row.control_id})
MATCH (sys:System {regional_standard_and_regulation_id:'dpdpa_2023', system_id: row.system_id})
MERGE (co)-[:CONTROLS_CONTROLS_SYSTEM]->(sys);
"""
#Requirement->process
requirement_process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_ id})
MATCH (pr:Process {regional_standard_and_regulation_id:'dpdpa_2023', process_id: row.process_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_PROCESS]->(pr);
"""
#process->system
process_system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pr:Process {regional_standard_and_regulation_id:'dpdpa_2023', process_id: row.process_id})
MATCH (sys:System {regional_standard_and_regulation_id:'dpdpa_2023', system_id: row.system_id})
MERGE (pr)-[:PROCESSES_PROCESSES_SYSTEM]->(sys);
"""
#enforcement_action->requirements
enforcement_action_requirements ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:enforcement_action {regional_standard_and_regulation_id:'dpdpa_2023', enforcement_id: row.enforcement_id})
MATCH (req:Requirement {regional_standard_and_regulation_id:'dpdpa_2023', requirement_id: row.requirement_ id})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_REQUIREMENTS]->(req);
"""
#enforcement_action->role
enforcement_action_role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:enforcement_action {regional_standard_and_regulation_id:'dpdpa_2023', enforcement_id: row.enforcement_id})
MATCH (ro:Role {regional_standard_and_regulation_id:'dpdpa_2023', role_id: row.role_id})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_ROLES]->(ro);
"""
#enforcement_action->section
enforcement_action_section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:enforcement_action {regional_standard_and_regulation_id:'dpdpa_2023', enforcement_id: row.enforcement_id})
MATCH (sec:Section {regional_standard_and_regulation_id:'dpdpa_2023', section_id: row.section_id})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_SECTION]->(sec);
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

client.query(regulation)
time.sleep(2)

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Sections.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirements.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Roles_Corrected.csv"))
time.sleep(2)

client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_DataCategories.csv"))
time.sleep(2)

client.query(right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Rights_Corrected.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Safeguards.csv"))
time.sleep(2)

client.query(event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_EventTypes_Corrected.csv"))
time.sleep(2)

client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPPA_EnforcementActions.csv"))
time.sleep(2)

client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Controls.csv"))
time.sleep(2)

client.query(regulation_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Regulation_Sections.csv"))
time.sleep(2)

client.query(section_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Requirements.csv"))
time.sleep(2)

client.query(section_right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Rights.csv"))
time.sleep(2)

client.query(section_enforcement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Section_Enforcement.csv"))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Data.csv"))
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Safeguards.csv"))
time.sleep(2)

client.query(requirement_event.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Events_Updated.csv"))
time.sleep(2)

client.query(requirement_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Controls.csv"))
time.sleep(2)


client.query(requirement_enforcement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Enforcement_Links.csv"))
time.sleep(2)

client.query(role_right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Role_Rights.csv"))
time.sleep(2)

client.query(requirement_contract.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/CPRA_Requirement_Contract_Corrected.csv"))
time.sleep(2)



logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:RegionalStandardAndRegulation)-[*]->()
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
with open('cpra.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to cpra.json")


client.close()

