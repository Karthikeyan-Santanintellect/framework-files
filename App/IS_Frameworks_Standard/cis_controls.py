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
MERGE (c:Control {control_id: row.control_id})
ON CREATE SET
  c.name = row.name,
  c.description = row.description;
"""

#Load Safeguards
safeguards ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Safeguard {safeguard_id: row.safeguard_id})
ON CREATE SET
  s.description = row.description,
  s.version = row.version;
"""
#Load Asset class
asset_class ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(a:AssetClass{name:row.name})
ON CREATE SET
    a.description = row.description;
"""
#Load Security function
security_function ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(sf:SecurityFunction{name:row.name})
ON CREATE SET
    sf.source = row.source;
"""
# Load IMPLEMENTATION GROUP 
implementation_group ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(ig:ImplementationGroup {name: row.name})
ON CREATE SET
  ig.description = row.description,
  ig.safeguard_count = toInteger(row.safeguard_count);
"""
#Load  GOVERNING BODY NODE 
governing_body ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (gb:GoverningBody {name: row.name})
ON CREATE SET
  gb.alias = row.alias,
  gb.type = row.type,
  gb.mission = row.mission;
"""

# 1.CREATE FRAMEWORK -> GOVERNING BODY RELATIONSHIPS 
framework_and_standard_governing_body ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: row.from_node_id}) 
MATCH (gb:GoverningBody {name: row.to_node_id})
MERGE (f)-[:FRAMEWORK_PUBLISHED_BY_GOVERNING_BODY]->(gb);
"""
# 2.CREATE FRAMEWORK -> CONTROL RELATIONSHIPS 
framework_and_standard_control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: row.from_node_id})
MATCH (c:Control {control_id: row.to_node_id})
MERGE (f)-[:FRAMEWORK_HAS_CONTROL]->(c);
"""
# 3. CREATE CONTROL -> SAFEGUARD RELATIONSHIPS 
control_safeguard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {control_id: row.from_node_id})
MATCH (s:Safeguard {safeguard_id: row.to_node_id})
MERGE (c)-[:CONTROL_HAS_SAFEGUARD]->(s);
"""
# 4. CREATE SAFEGUARD -> IMPLEMENTATION GROUP RELATIONSHIPS 
safeguard_implementation_group ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (ig:ImplementationGroup {name: row.to_node_id})
MERGE (s)-[:SAFEGUARD_BELONGS_TO_IMPLEMENTATION_GROUP]->(ig);
"""

# 5. CREATE SAFEGUARD -> ASSET CLASS RELATIONSHIPS 
safeguard_asset_class ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (ac:AssetClass {name: row.to_node_id})
MERGE (s)-[:SAGEGUARD_APPLIES_TO_ASSET_CLASS]->(ac);
"""

# 6. CREATE SAFEGUARD -> SECURITY FUNCTION RELATIONSHIPS 
safeguard_security_function ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (sf:SecurityFunction {name: row.to_node_id})
MERGE (s)-[:SAFEGUARD_MAPS_TO_SECURITY_FUNCTION]->(sf);
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

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_controls.csv"))
time.sleep(2)

client.query(safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_safeguards.csv"))
time.sleep(2)

client.query(asset_class.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_asset_class.csv"))
time.sleep(2)

client.query(security_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_security_function.csv"))
time.sleep(2)

client.query(implementation_group.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_implementation_group.csv"))
time.sleep(2)

client.query(governing_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/nodes_governing_body.csv"))
time.sleep(2)

client.query(framework_and_standard_governing_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_framework_to_governing_body_CORRECTED.csv"))
time.sleep(2)

client.query(framework_and_standard_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_framework_to_control_CORRECTED.csv"))
time.sleep(2)

client.query(control_safeguard.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_control_to_safeguard.csv"))
time.sleep(2)


client.query(safeguard_implementation_group.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_safeguard_to_implementation_group.csv"))
time.sleep(2)

client.query(safeguard_asset_class.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_safeguard_to_asset_class.csv"))
time.sleep(2)

client.query(safeguard_security_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/CIS%20Controls/relations_safeguard_to_security_function.csv"))
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


