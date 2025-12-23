from neo4j import GraphDatabase
import json
import os
import time
import logging
from app import Neo4jConnect

# Load the JSON data
with open(r'D:\framework-files\Catalog\ControlCatalog.json') as f:
    json_data = json.load(f)

# Define the query
query = """
UNWIND $data AS row

MERGE (d:Domain {name: row.`SCF Domain`})
MERGE (c:Control {id: row.`SCF #`})
ON CREATE SET 
    c.title = row.`SCF Control`,
    c.description = row.`Secure Controls Framework (SCF)\nControl Description`
ON MATCH SET 
    c.title = row.`SCF Control`,
    c.description = row.`Secure Controls Framework (SCF)\nControl Description`
MERGE (d)-[:HAS_CONTROL]->(c)

// CONDITIONAL CSF FUNCTION
FOREACH (ignoreMe IN CASE WHEN row.`NIST CSF\nFunction Grouping` IS NOT NULL THEN [1] ELSE [] END |
    MERGE (f:`CSF Function` {name: row.`NIST CSF\nFunction Grouping`})
    MERGE (c)-[:MAPS_TO_FUNCTION]->(f)
)

MERGE (w:Weighting {value: row.`Relative Control Weighting`})
MERGE (c)-[:HAS_WEIGHTING]->(w)

// CONDITIONAL SOLUTIONS
FOREACH (ignoreMe IN CASE WHEN row.`Possible Solutions & Considerations\nMedium Business (50-249 staff)\nBLS Firm Size Classes 5-6` IS NOT NULL THEN [1] ELSE [] END |
    MERGE (s_med:Solution {
        description: row.`Possible Solutions & Considerations\nMedium Business (50-249 staff)\nBLS Firm Size Classes 5-6`,
        size: "Medium Business"
    })
    MERGE (c)-[:HAS_POSSIBLE_SOLUTION]->(s_med)
)

FOREACH (ignoreMe IN CASE WHEN row.`Possible Solutions & Considerations\nLarge Business (250-999 staff)\nBLS Firm Size Classes 7-8` IS NOT NULL THEN [1] ELSE [] END |
    MERGE (s_large:Solution {
        description: row.`Possible Solutions & Considerations\nLarge Business (250-999 staff)\nBLS Firm Size Classes 7-8`,
        size: "Large Business"
    })
    MERGE (c)-[:HAS_POSSIBLE_SOLUTION]->(s_large)
)

FOREACH (ignoreMe IN CASE WHEN row.`Possible Solutions & Considerations\nEnterprise (> 1,000 staff)\nBLS Firm Size Class 9` IS NOT NULL THEN [1] ELSE [] END |
    MERGE (s_ent:Solution {
        description: row.`Possible Solutions & Considerations\nEnterprise (> 1,000 staff)\nBLS Firm Size Class 9`,
        size: "Enterprise"
    })
    MERGE (c)-[:HAS_POSSIBLE_SOLUTION]->(s_ent)
)
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    logger.error("Neo4j connection error: %s", health)
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

with open('control_catalog.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to control_catalog.json")

client.close()
