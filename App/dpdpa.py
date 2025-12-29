#Regulation
regulation = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:RegionalStandardAndRegulation {
  regional_standard_regulation_id: 'DPDPA 1.0', 
  regulation_id: row.regulation_id})
ON CREATE SET
  reg.name = row.name,
  reg.citation = row.citation,
  reg.version = row.version,
  reg.status = row.status,
  reg.effective_date = row.effective_date,  
  reg.jurisdiction = row.jurisdiction,
  reg.description = row.description
RETURN count(reg) AS regulations_created;
"""
#Chapter
chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {regional_standard_regulation_id:'DPDPA 1.0', chapter_id: row.chapter_id})
ON CREATE SET 
  c.number = toInteger(row.chapter_number),
  c.name = row.title,
  c.description = row.description;
"""
#Section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {regional_standard_regulation_id:'DPDPA 1.0', section_id: row.section_id})
ON CREATE SET 
  sec.number = row.section_number,
  sec.chapter_id = row.chapter_id,
  sec.name = row.title;
"""
#Requirement
requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
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
MERGE (ro:Role {regional_standard_regulation_id:'DPDPA 1.0', role_id: row.role_id})
ON CREATE SET 
  ro.name = row.name,
  ro.description = row.description,
  ro.category = row.category;
"""
#datacategory
datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id:'DPDPA 1.0', data_id: row.data_id})
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
MERGE (sg:Safeguard {regional_standard_regulation_id:'DPDPA 1.0', safeguard_id: row.safeguard_id})
ON CREATE SET 
  sg.name = row.name,
  sg.description = row.description,
  sg.type = row.type,
  sg.applies_to_section = row.applies_to_section;
"""
#event_type
event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id:'DPDPA 1.0', event_type_id: row.event_type_id})
ON CREATE SET 
  et.name = row.name,
  et.description = row.description,
  et.deadline = row.deadline,
  et.extendable = row.extendable,
  et.extension_period = row.extension_period,
  et.cost = row.cost;
"""
#policy
policy ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {regional_standard_regulation_id:'DPDPA 1.0', policy_id: row.policy_id})
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
MERGE (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
ON CREATE SET 
  co.name = row.name,
  co.category = row.category,
  co.owner = row.owner,
  co.description = row.description;
"""
#system
system ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
ON CREATE SET 
  sys.name = row.name,
  sys.type = row.type,
  sys.description = row.description,
  sys.category = row.category,
  sys.personal_data = row.holds_personal_data,
  sys.sensitive_data = row.holds_sensitive_data,
  sys.processing_activities = row.processing_activities;
"""
#process
process ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
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
MERGE (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
ON CREATE SET 
  ea.name = row.name,
  ea.description = row.description,
  ea.type = row.type,
  ea.authority = row.authority,
  ea.level = row.severity_level,
  ea.applicable_section = row.applicable_section;
"""
regulation_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DPDPA 1.0', regulation_id: row.regulation_id})
MATCH (c:Chapter {regional_standard_regulation_id: 'DPDPA 1.0', chapter_id: row.chapter_id})
MERGE (reg)-[:REGIONAL_REGULATION_HAS_CHAPTER]->(c);
"""

chapter_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {regional_standard_regulation_id: 'DPDPA 1.0', chapter_id: row.chapter_id})
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0', section_id: row.section_id})
MERGE (c)-[:CHAPTER_HAS_SECTION]->(sec);
"""

section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {regional_standard_regulation_id: 'DPDPA 1.0', section_id: row.section_id})
MATCH (req:Requirement {regional_standard_regulation_id: 'DPDPA 1.0', requirement_id: row.requirement_id})
MERGE (sec)-[:SECTION_HAS_REQUIREMENT]->(req);
"""

requirement_roles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (ro:Role {regional_standard_regulation_id:'DPDPA 1.0', role_id: row.role_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_ROLES]->(ro);
"""

requirement_datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (dc:DataCategory {regional_standard_regulation_id:'DPDPA 1.0', data_id: row.data_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_DATACATEGORY]->(dc);
"""

requirement_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (sg:Safeguard {regional_standard_regulation_id:'DPDPA 1.0', safeguard_id: row.safeguard_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_SAFEGUARD]->(sg);
"""

requirement_event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (et:EventType {regional_standard_regulation_id:'DPDPA 1.0', event_type_id: row.event_type_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_EVENTTYPE]->(et);
"""

requirement_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (pol:Policy {regional_standard_regulation_id:'DPDPA 1.0', policy_id: row.policy_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_POLICY]->(pol);
"""

requirement_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_CONTROL]->(co);
"""

control_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:Control {regional_standard_regulation_id:'DPDPA 1.0', control_id: row.control_id})
MATCH (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
MERGE (co)-[:CONTROLS_CONTROLS_SYSTEM]->(sys);
"""

requirement_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:Requirement {regional_standard_regulation_id:'DPDPA 1.0', requirement_id: row.requirement_id})
MATCH (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
MERGE (req)-[:REQUIREMENTS_REQUIRES_PROCESS]->(pr);
"""

process_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pr:Process {regional_standard_regulation_id:'DPDPA 1.0', process_id: row.process_id})
MATCH (sys:System {regional_standard_regulation_id:'DPDPA 1.0', system_id: row.system_id})
MERGE (pr)-[:PROCESSES_PROCESSES_SYSTEM]->(sys);
"""

enforcement_action_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
MATCH (req:Requirement {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    requirement_id: row.requirement_id
})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_REQUIREMENTS]->(req);
"""

enforcement_action_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
MATCH (ro:Role {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    role_id: row.role_id
})
MERGE (ea)-[:ENFORCEMENTACTIONS_CARRIES_PENALTIES_ROLES]->(ro);
"""

enforcement_action_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    enforcement_action_id: row.enforcement_action_id
})
MATCH (sec:Section {
    regional_standard_regulation_id: 'DPDPA 1.0', 
    section_id: row.section_id
})
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

client.query(regulation.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Regulation_Node.csv"))
time.sleep(2)

client.query(chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Chapters.csv"))
time.sleep(2)

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Sections.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirements.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Roles.csv"))
time.sleep(2)

client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_DataCategories.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Safeguards.csv"))
time.sleep(2)

client.query(event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EventTypes.csv"))
time.sleep(2)

client.query(policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Policies.csv"))
time.sleep(2)

client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Controls.csv"))
time.sleep(2)

client.query(system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Systems.csv"))
time.sleep(2)

client.query(process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Processes.csv"))
time.sleep(2)

client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction.csv"))
time.sleep(2)

client.query(regulation_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Regulation_Chapter_Relationship_FIXED.csv"))
time.sleep(2)

client.query(chapter_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA-Chap-Sec-Rel.csv"))
time.sleep(2)

client.query(section_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA-Sec-Req-Rel.csv"))
time.sleep(2)
                                        
client.query(requirement_roles.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Roles.csv"))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Data.csv"))
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Safeguards.csv"))
time.sleep(2)

client.query(requirement_event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Events.csv"))
time.sleep(2)

client.query(requirement_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Controls.csv"))
time.sleep(2)


client.query(requirement_policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Policies.csv"))
time.sleep(2)

client.query(control_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Control_Systems.csv"))
time.sleep(2)

client.query(requirement_process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Requirement_Processes.csv"))
time.sleep(2)

client.query(process_system.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_Process_Systems.csv"))
time.sleep(2)

client.query(enforcement_action_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction_Requirement_Relationship.csv"))
time.sleep(2)

client.query(enforcement_action_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction_Role_Relationship.csv"))
time.sleep(2)

client.query(enforcement_action_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DPDPA/DPDPA_EnforcementAction_Section_Relationship.csv"))
time.sleep(2)




logger.info("Graph structure loaded successfully.")

export_query = """
MATCH (n)
OPTIONAL MATCH (n)-[r]->(m)
WITH collect(DISTINCT n) AS uniqueNodes, collect(DISTINCT r) AS uniqueRels
RETURN {
  nodes: [n IN uniqueNodes | n {
    .*,
    id: elementId(n),
    labels: labels(n),
    mainLabel: head(labels(n))
  }],
  rels: [r IN uniqueRels WHERE r IS NOT NULL | r {
    .*,
    id: elementId(r),
    type: type(r),
    from: elementId(startNode(r)),
    to: elementId(endNode(r))
  }]
} AS graph_data
"""

try:
    res = client.query(export_query)

    if res and len(res) > 0:
        graph_data = res[0]['graph_data']
        
        # Write to JSON
        with open('dpdpa.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(graph_data, default=str, indent=2))
        
        node_count = len(graph_data.get('nodes', []))
        rel_count = len(graph_data.get('rels', []))
        
        logger.info(f"✓ Exported graph data to dpdpa.json")
        logger.info(f"  └─ Nodes: {node_count}")
        logger.info(f"  └─ Relationships: {rel_count}")
    else:
        logger.warning("Query returned no results")
        # Try alternate query if primary fails
        logger.info("Attempting alternate query...")
        alt_query = "MATCH (n) RETURN count(n) as nodes; MATCH ()-[r]->() RETURN count(r) as rels"
        res_alt = client.query(alt_query)
        logger.info(f"Database stats: {res_alt}")

except Exception as e:
    logger.error(f"Failed to export graph: {str(e)}")

client.close()
logger.info("\n✓ Import complete!")

