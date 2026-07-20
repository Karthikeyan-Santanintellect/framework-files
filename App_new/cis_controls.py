#Load Framework
framework_and_standard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET
  f.name = row.name,
  f.version = row.version,
  f.publication_date = date('2022-10-25'),
  f.status = 'Active',
  f.description = row.description,
  f.total_controls = toInteger(row.total_controls),
  f.total_safeguards = toInteger(row.total_safeguards);
 """

# Load Controls
controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id,IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET
  c.name = row.name,
  c.description = row.description;
"""

#Load Safeguards
safeguards ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Safeguard {safeguard_id: row.safeguard_id,IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET 
    s.title = row.title,
    s.description = row.description;
"""
#Load Asset class
asset_class ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:AssetClass {name: row.name,IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET 
  a.description = row.description;
"""
#Load Security function
security_function ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sf:SecurityFunction {name: row.name,IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET 
    sf.source = row.source,
    sf.description = row.description;
"""
# Load IMPLEMENTATION GROUP 
implementation_group ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(ig:ImplementationGroup {name: row.name,IS_frameworks_standard_id : 'CIS CONTROLS 8.1'})
ON CREATE SET 
    ig.title = row.title,
    ig.description = row.description;
"""
# CREATE FRAMEWORK -> CONTROL RELATIONSHIPS 
framework_and_standard_control ="""
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'CIS CONTROLS 8.1'})
MATCH (c:Control {IS_frameworks_standard_id: 'CIS CONTROLS 8.1'})
MERGE (f)-[:FRAMEWORK_HAS_CONTROL]->(c);
"""
# CREATE CONTROL -> SAFEGUARD RELATIONSHIPS 
control_safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {control_id: row.from_node_id})
MATCH (s:Safeguard {safeguard_id: row.to_node_id})
MERGE (c)-[:CONTROL_HAS_SAFEGUARD]->(s);
"""
# CREATE SAFEGUARD -> IMPLEMENTATION GROUP RELATIONSHIPS 
safeguard_implementation_group ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (ig:ImplementationGroup {name: row.to_node_id})
MERGE (s)-[:SAFEGUARD_BELONGS_TO_IMPLEMENTATION_GROUP]->(ig);
"""

# CREATE SAFEGUARD -> ASSET CLASS RELATIONSHIPS 
safeguard_asset_class ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (ac:AssetClass {name: row.to_node_id})
MERGE (s)-[:SAFEGUARD_APPLIES_TO_ASSET]->(ac);
"""

# CREATE SAFEGUARD -> SECURITY FUNCTION RELATIONSHIPS 
safeguard_security_function ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (sf:SecurityFunction {name: row.to_node_id})
MERGE (s)-[:SAFEGUARD_MAPS_TO_SECURITY_FUNCTION]->(sf);
"""
# Framework -> Assets relationships
framework_assets_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'CIS CONTROLS 8.1'})
MATCH (a:AssetClass {IS_frameworks_standard_id: 'CIS CONTROLS 8.1'}) 
MERGE (f)-[:FRAMEWORK_CONTAINS_ASSET]->(a);
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

client.query(framework_and_standard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_framework.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Controls.csv"))
time.sleep(2)

client.query(safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Safeguard.csv"))
time.sleep(2)

client.query(asset_class.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Asset%20Class.csv"))
time.sleep(2)

client.query(security_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Security%20Functions.csv"))
time.sleep(2)

client.query(implementation_group.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Implementation%20Group.csv"))
time.sleep(2)


# Relationships

client.query(framework_and_standard_control)
time.sleep(2)

client.query(control_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Control%20-%20Control%20Safeguard.csv"))
time.sleep(2)

client.query(safeguard_implementation_group.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Controls%20-%20Safeguard%20Implementation.csv"))
time.sleep(2)

client.query(safeguard_asset_class.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Control%20-%20Safeguard%20Asset.csv"))
time.sleep(2)

client.query(safeguard_security_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/CIS%20Control%20-%20Safeguard%20Security%20Function.csv"))
time.sleep(2)

client.query(framework_assets_rel)
time.sleep(2)



logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:ISFrameworksAndStandard)-[*]->()
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
with open('cis-controls.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to cis-controls.json")


client.close()


