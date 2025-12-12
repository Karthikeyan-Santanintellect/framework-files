#Regulations
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'CPRA'})
ON CREATE SET 
    reg.name = "California Privacy Rights Act",
    reg.version ="2.0 (Amends CCPA)",
    reg.base_regulation ="California Consumer Privacy Act (CCPA)",
    reg.codificatiom ="California Civil Code Title 1.81.5",
    reg.effective_date =date("2023-01-01"),
    reg.status = "Active",
    reg.description ="The CPRA is a ballot initiative that amends the CCPA, creating new consumer rights, establishing the CPPA, and strengthening enforcement.";
"""
#section
section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Section {regional_standard_regulation_id: 'CPRA',section_id: row.section_id})
ON CREATE SET 
    s.heading = row.heading;
"""
#requirement
requirement="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rq:Requirement {regional_standard_regulation_id: 'CPRA',requirement_id: row.requirement_id})
ON CREATE SET 
    rq.section_id = row.section_id,
    rq.text = row.text,
    rq.type = row.type;
"""
#role
role ="""
LOAD CSV WITH HEADERS FROM '$file_ path' AS row
MERGE (ro:Role {regional_standard_regulation_id: 'CPRA',role_id: row.role_id})
ON CREATE SET 
    ro.name = row.name,
    ro.description = row.description;
"""
#datacategory
datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_regulation_id: 'CPRA',data_id: row.data_id})
ON CREATE SET
    dc.name = row.name,
    dc.sensitivity = row.sensitivity;
"""
#right
right ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Right {regional_standard_regulation_id: 'CPRA',right_id: row.right_id})
ON CREATE SET 
    r.section_id = row.section_id,
    r.name = row.name;
"""
#safeguard
safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_regulation_id: 'CPRA',safeguard_id: row.safeguard_id})
ON CREATE SET 
    sg.type = row.type,
    sg.description = row.description;
"""
#event_type
event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_regulation_id: 'CPRA',event_type_id: row.event_type_id})
ON CREATE SET   
    et.name = row.name,
    et.description = row.description;
"""
#enforcement_action
enforcement_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_regulation_id: 'CPRA',enforcement_id: row.enforcement_id})
ON CREATE SET 
    ea.authority = row.authority,
    ea.max_penalty = row.max_penalty,
    ea.description = row.description;
"""
#control
control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control {regional_standard_regulation_id: 'CPRA',control_id: row.control_id})
ON CREATE SET 
    co.name = row.name,
    co.category = row.category;
"""

#Requirement_roles
requirement_role ="""
LOAD CSV WITH HEADERS FROM '$file_ path' AS row
MATCH (rq:Requirement {requirement_id: row.from_id})
MATCH (r:Role {role_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_ASSIGNED_TO_ROLE]->(ro);
"""
#Requirement_datacategory
requirement_datacategory ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {requirement_id: row.from_id})
MATCH (dc:DataCategory {data_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_INCLUDES_DATA_CATEGORY]->(dc);
"""
#role_rights
role_right ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ro:Role {role_id: row.from_id})
MATCH (r:Right {right_id: row.to_id})
MERGE (ro)-[:ROLE_HAS_RIGHT]->(r);
"""
#requirement_role
requirement_role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {requirement_id: row.from_id})
MATCH (ro:Role {role_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_MANDATES_CONTRACT_WITH_ROLE]->(ro);
"""
#requirement_events
requirement_event ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {requirement_id: row.from_id})
MATCH (et:EventType {event_type_id: row.to_id})
MERGE (rq)-[:REQUIREMENT_TRIGGERS_ON_EVENT_TYPE]->(et);
"""
#requirement_control
requirement_control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {requirement_id: row.from_id})
MATCH (co:Control {control_id: row.to_id})
MERGE (rq)-[:IMPLEMENTED_BY_CONTROL]->(co);
"""
#enforcement_requirements
enforcement_requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ea:EnforcementAction {enforcement_id: row.from_id})
MATCH (rq:Requirement {requirement_id: row.to_id})
MERGE (ea)-[:ENFORCEMENT_CARRIES_PENALTY_ON_REQUIREMENT]->(rq);
"""
#requirement_sections
requirement_section ="""
MATCH (rq:Requirement{regional_standard_regulation_id: 'CPRA'}
MATCH (s:Section{regional_standard_regulation_id: 'CPRA'}
MERGE (s)-[:DEFINES_REQUIREMENT]->(rq);
"""
#regional_sections
regulation_section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation{regional_standard_regulation_id: row.from_id}
MATCH (s:Section{regional_standard_regulation_id: row.to_id}
MERGE (reg)-[:DEFINES_SECTION]->(s);
"""
#right_section
right_section ="""
MATCH (r:Right{regional_standard_regulation_id: 'CPRA'}
MATCH (s:Section{regional_standard_regulation_id: 'CPRA'}
MERGE (r)-[:DEFINES_SECTION]->(s);
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

client.query(section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/2_chapter_nodes.csv"))
time.sleep(2)

client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/3_section_nodes.csv"))
time.sleep(2)

client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/article_node.csv"))
time.sleep(2)

client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/5_recital_nodes.csv"))
time.sleep(2)

client.query(right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/12_paragraph_nodes.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/13_subparagraph_nodes.csv"))
time.sleep(2)

client.query(event_type.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/14_legislative_action_nodes.csv"))
time.sleep(2)

client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/15_concept_nodes_COMPLETE.csv"))
time.sleep(2)

client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/1_framework_nodes_CORRECTED.csv"))
time.sleep(2)


client.query(requirement_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/7_relationships_regulation_to_recital.csv"))
time.sleep(2)

client.query(requirement_datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/8_relationships_chapter_to_section.csv"))
time.sleep(2)

client.query(role_right.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/9_relationships_chapter_to_article.csv"))
time.sleep(2)

client.query(requirement_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/10_relationships_section_to_article.csv"))
time.sleep(2)

client.query(requirement_event.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/11_relationships_article_to_recital.csv"))
time.sleep(2)

client.query(requirement_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/17_relationships_article_to_paragraph.csv"))
time.sleep(2)

client.query(enforcement_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/23_relationships_recital_to_paragraph_CLEANED.csv"))
time.sleep(2)

client.query(requirement_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/18_relationships_paragraph_to_subparagraph.csv"))
time.sleep(2)

client.query(regulation_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/19_relationships_regulation_to_legislative_action.csv"))
time.sleep(2)

client.query(right_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/20_relationships_regulation_to_framework_CORRECTED.csv"))
time.sleep(2)


logger.info("Graph structure loaded successfully.")

output_filename = "cpra.json"

res = client.query("""
    MATCH path = (:RegionalStandardAndRegulation)-[*]-()
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
      links: [r IN uniqueRels | r {
        .*,
        id: elementId(r),     
        type: type(r),         
        source: elementId(startNode(r)), 
        target: elementId(endNode(r)) 
      }]
    } AS graph_data
""")

if isinstance(res, str):
    logger.error(f"✗ Export query failed: {res}")
    client.close()
    sys.exit(1)

if not res or len(res) == 0:
    logger.warning(" No data returned from export query")
    client.close()
    sys.exit(1)

graph_data = res[0].get('graph_data', res[0])

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, default=str, ensure_ascii=False)

node_count = len(graph_data.get('nodes', []))
link_count = len(graph_data.get('links', []))

logger.info(f" Exported {node_count} nodes and {link_count} relationships")
logger.info(f" Graph data saved to: {output_filename}") 

client.close()





