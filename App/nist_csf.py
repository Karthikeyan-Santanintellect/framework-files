# nist_csf.py

# CORRECTED: Standardized constraints to use 'IS_frameworks_standard_id' consistently.
constraints = """
CREATE CONSTRAINT nist_IS_frameworks_standard_id IF NOT EXISTS FOR (f:Framework) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT nist_function_composite_id IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.IS_frameworks_standard_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT nist_category_composite_id IF NOT EXISTS FOR (c:Category) REQUIRE (c.IS_frameworks_standard_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT nist_subcategory_composite_id IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.IS_frameworks_standard_id, s.subcategory_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX nist_function_name IF NOT EXISTS FOR (fn:Function) ON (fn.name);
CREATE INDEX nist_category_name IF NOT EXISTS FOR (c:Category) ON (c.name);
"""

# CORRECTED: Changed property from 'id' to 'IS_frameworks_standard_id' for consistency.
IS_framework_and_standards = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "NIST_CSF_2.0"})
ON CREATE SET
  f.name = "NIST Cybersecurity Framework 2.0",
  f.version = "2.0",
  f.publication_date = date("2024-02-26"),
  f.description = "Framework for managing cybersecurity risks";
"""

functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {function_id: row.Function_Code, IS_frameworks_standard_id: "NIST_CSF_2.0"})
ON CREATE SET
  fn.name = row.Function,
  fn.description = row.Function_Description;
"""

# CORRECTED: Used '=' instead of ':' for property assignment in SET clause.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {category_id: row.Category_Code, IS_frameworks_standard_id: "NIST_CSF_2.0"})
ON CREATE SET
  c.function_id = row.Function_Code,
  c.name = row.Category,
  c.description = row.Category_Description;
"""

# CORRECTED: Used '=' instead of ':' for property assignment in SET clause.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:Subcategory {id: row.Subcategory_Code, IS_frameworks_standard_id: "NIST_CSF_2.0"})
ON CREATE SET
  sc.category_id = row.Category_Code,
  sc.description = row.Subcategory_Description,
  sc.example = row.Implementation_Example;
"""

# No changes needed here, as it now correctly matches the 'IS_frameworks_standard_id' property.
framework_and_standard_functions_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MERGE (f)-[:FRAMEWORK_CONTAINS_FUNCTIONS]->(fn);
"""


function_categories_rel = """
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORIES]->(c);
"""

category_subcategories_rel = """
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MATCH (s:Subcategory {IS_frameworks_standard_id: 'NIST_CSF_2.0'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CATEGORY_CONTAINS_SUBCATEGORIES]->(s);
"""


import os
import time
import logging
import json
import sys
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)
    

logger.info("Loading graph structure...")

client.query(IS_framework_and_standards)
time.sleep(2)
logger.info('ISFrameworksAndStandard')

client.query(functions.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20CSF%202.0/functions.csv'))
time.sleep(2)
logger.info('Function')

client.query(categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20CSF%202.0/categories.csv'))
time.sleep(2)
logger.info('Category')

client.query(subcategories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20CSF%202.0/subcategories.csv'))
time.sleep(2)
logger.info('Subcategory')

logger.info("Creating relationships...")
client.query(framework_and_standard_functions_rel)
time.sleep(2)

client.query(function_categories_rel)
time.sleep(2)

client.query(category_subcategories_rel)
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
with open('nist_csf.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist_csf.json")


client.close()
