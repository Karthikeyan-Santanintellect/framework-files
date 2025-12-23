from neo4j import GraphDatabase
import json
import os
import time
import logging
from app import Neo4jConnect

# Load the JSON data
with open(r'D:\framework-files\Catalog\RiskCatalog.json') as f:
    json_data = json.load(f)

# Define the query
query = """
UNWIND $data AS row
MERGE (d:Domain {name: row.`DTOM Domain` , type: 'DTOM'})
MERGE (fd:FunctionalDomain {name: row.`DTOM Functional Domain`})
MERGE (d)-[:HAS_FUNCTIONAL_DOMAIN]->(fd)
MERGE (r:Risk {id: row.`Risk #`})
SET r.title = row.Risk, 
    r.description = row.`Description of Possible Risk Due To Control Deficiency`
MERGE (fd)-[:HAS_RISK]->(r)
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading graph structure...")

client.query(query, others={'data': json_data})

logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:Domain)-[*]->()
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

with open('risk_catalog.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to risk_catalog.json")

client.close()
