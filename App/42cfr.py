regulation = """
MERGE (r:Regulation {IS_frameworks_standard_id: '42_CFR_PART_2'})
ON CREATE SET
    r.name = '42 CFR Part 2',
    r.version = '2026 Edition',
    r.jurisdiction = 'US Federal',
    r.authority = 'Secretary of HHS',
    r.description = 'Confidentiality of Substance Use Disorder Patient Records';
"""

# UPDATED: Added framework_id and switched to MERGE. 
# Replaces 'control_categories' from ISO27001.
subparts = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sub:Subpart {IS_frameworks_standard_id: '42_CFR_PART_2', subpart_id: row.id})
ON CREATE SET
    sub.name = row.name,
    sub.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE. 
# Replaces 'clauses' from ISO27001.
sections = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {IS_frameworks_standard_id: '42_CFR_PART_2', section_id: row.id})
ON CREATE SET
    sec.name = row.name,
    sec.description = row.description,
    sec.subpart_id = row.subpart_id; 
"""

# UPDATED: Added framework_id and switched to MERGE. 
# Handing the Actors/Entities from the 42 CFR Graph.
entities = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:Entity {IS_frameworks_standard_id: '42_CFR_PART_2', entity_id: row.id})
ON CREATE SET
    e.label = row.label,
    e.name = row.name,
    e.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE. 
# Handling the Data/Records from the 42 CFR Graph.
assets = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Asset {IS_frameworks_standard_id: '42_CFR_PART_2', asset_id: row.id})
ON CREATE SET
    a.label = row.label,
    a.name = row.name,
    a.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE. 
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {IS_frameworks_standard_id: '42_CFR_PART_2', control_id: row.id})
ON CREATE SET
    c.label = row.label,
    c.name = row.name,
    c.description = row.description;
"""
# Relationships 
regulation_has_subparts = """
MATCH (reg:Regulation {regional_standard_regulation_id: '42_CFR_PART_2'})
MATCH (sub:Subpart {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (reg)-[:REGULATION_HAS_SUBPART]->(sub);
"""
subpart_contains_sections = """
MATCH (sub:Subpart {IS_frameworks_standard_id: '42_CFR_PART_2'})
MATCH (sec:Section {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (sub)-[:SUBPART_CONTAINS_SECTION]->(sec);
"""
entity_entity = """
MATCH (p2p:Entity {regional_standard_regulation_id: '42_CFR_PART_2'})
MATCH (pat:Entity {regional_standard_regulation_id: '42_CFR_PART_2'})
MERGE (p2p)-[:ENTITY_DIAGNOSES_PATIENT]->(pat);
"""
entity_control = """
MATCH (e:Entity {IS_frameworks_standard_id: '42_CFR_PART_2'})
MATCH (c:Control {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (e)-[:ENTITY_PROVIDES_CONTROL]->(c);
"""
entity_asset = """
MATCH (e:Entity {IS_frameworks_standard_id: '42_CFR_PART_2'})
MATCH (a:Asset {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (e)-[:ENTITY_HAS_ASSET]->(a); 
"""
asset_asset = """
MATCH (a1:Asset {IS_frameworks_standard_id: '42_CFR_PART_2'})
MATCH (a2:Asset {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (a1)-[:ASSET_RELATES_TO_ASSET]->(a2);
"""
control_asset = """
MATCH (c:Control {IS_frameworks_standard_id: '42_CFR_PART_2'})
MATCH (a:Asset {IS_frameworks_standard_id: '42_CFR_PART_2'})
MERGE (c)-[:CONTROL_MITIGATES_ASSET]->(a);
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

client.query(subparts.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Title.csv"))
time.sleep(2)

client.query(sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Subdivision.csv"))
time.sleep(2)

client.query(entities.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Paragraph.csv"))
time.sleep(2)

client.query(assets.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Consumer.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CPRA/Business.csv"))
time.sleep(2)

                                 
#Relationships
client.query(regulation_has_subparts)
time.sleep(2)

client.query(subpart_contains_sections)
time.sleep(2)

client.query(entity_entity)
time.sleep(2)

client.query(entity_control)
time.sleep(2)

client.query(entity_asset)
time.sleep(2)

client.query(asset_asset)
time.sleep(2)

client.query(control_asset)
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
    with open('42cfr.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to 42cfr.json")
else:
    logger.error("No data returned from the query.")

client.close()





