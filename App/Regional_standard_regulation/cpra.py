# Regulation Node
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPRA 2.0'})
ON CREATE SET 
    reg.name = "California Privacy Rights Act",
    reg.version = "2.0 (Amends CCPA)",
    reg.base_regulation = "California Consumer Privacy Act (CCPA)",
    reg.codification = "California Civil Code Title 1.81.5",
    reg.effective_date = date("2023-01-01"),
    reg.status = "Active",
    reg.description = "The CPRA is a ballot initiative that amends the CCPA, creating new consumer rights, establishing the CPPA, and strengthening enforcement.";
"""

# Section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.section_id})
ON CREATE SET 
    s.heading = row.heading;
"""

# Requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.requirement_id})
ON CREATE SET 
    rq.section_id = row.section_id,
    rq.text = row.text,
    rq.type = row.type;
"""

# Role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.role_id})
ON CREATE SET 
    ro.name = row.name,
    ro.description = row.description;
"""

# DataCategory
datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id: 'CPRA 2.0', data_id: row.data_id})
ON CREATE SET
    dc.name = row.name,
    dc.sensitivity = row.sensitivity;
"""

# Right
right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.right_id})
ON CREATE SET 
    r.section_id = row.section_id,
    r.name = row.name;
"""

# Safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_regulation_id: 'CPRA 2.0', safeguard_id: row.safeguard_id})
ON CREATE SET 
    sg.type = row.type,
    sg.description = row.description;
"""

# EventType
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id: 'CPRA 2.0', event_type_id: row.event_type_id})
ON CREATE SET   
    et.name = row.name,
    et.description = row.description;
"""

# EnforcementAction
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.enforcement_id})
ON CREATE SET 
    ea.authority = row.authority,
    ea.max_penalty = row.max_penalty,
    ea.description = row.description;
"""

# Control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_regulation_id: 'CPRA 2.0', control_id: row.control_id})
ON CREATE SET 
    co.name = row.name,
    co.category = row.category;
"""

# RELATIONSHIPS

# Regulation to Section
regulation_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: row.from_id})
MATCH (s:Section {regional_standard_regulation_id: 'CPRA', section_id: row.to_id})
MERGE (reg)-[:REGIONAL_REGULATION_DEFINES_SECTION]->(s);
"""

# Section to Requirement
section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.to_id})
MERGE (s)-[:SECTION_DEFINES_REQUIREMENT]->(rq);
"""

# Section to Right
section_right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.to_id})
MERGE (s)-[:SECTION_ESTABLISHES_RIGHT]->(r);
"""

# Section to EnforcementAction
section_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {regional_standard_regulation_id: 'CPRA 2.0', section_id: row.from_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.to_id})
MERGE (s)-[:SECTION_PRESCRIBES_PENALTY]->(ea);
"""

# Requirement to DataCategory
requirement_datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'CPRA 2.0', data_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_REGULATES_USE_OF_DATA_CATEGORY]->(dc);
"""

# Requirement to Safeguard
requirement_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (sg:Safeguard {regional_standard_regulation_id: 'CPRA 2.0', safeguard_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg);
"""

# Requirement to EventType
requirement_event = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (et:EventType {regional_standard_regulation_id: 'CPRA 2.0', event_type_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_TRIGGERS_ON_EVENT_TYPE]->(et);
"""

# Requirement to Control
requirement_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (co:Control {regional_standard_regulation_id: 'CPRA 2.0', control_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co);
"""

# Requirement to EnforcementAction
requirement_enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA 2.0', enforcement_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_CARRIES_PENALTY_ON_ENFORCEMENT]->(ea);
"""

# Role to Right
role_right = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.from_id})
MATCH (r:Right {regional_standard_regulation_id: 'CPRA 2.0', right_id: row.to_id})
MERGE (ro)-[:ROLE_HAS_RIGHT]->(r);
"""

# Contract Requirements
requirement_contract = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {regional_standard_regulation_id: 'CPRA 2.0', requirement_id: row.from_id})
MATCH (ro:Role {regional_standard_regulation_id: 'CPRA 2.0', role_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_MANDATES_CONTRACT_WITH_ROLE]->(ro);
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





