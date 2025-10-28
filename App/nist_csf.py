# nist_csf.py

# CORRECTED: Standardized constraints to use 'framework_id' consistently.
constraints = """
CREATE CONSTRAINT nist_framework_id IF NOT EXISTS FOR (f:Framework) REQUIRE f.framework_id IS UNIQUE;
CREATE CONSTRAINT nist_function_composite_id IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.framework_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT nist_category_composite_id IF NOT EXISTS FOR (c:Category) REQUIRE (c.framework_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT nist_subcategory_composite_id IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.framework_id, s.subcategory_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX nist_function_name IF NOT EXISTS FOR (fn:Function) ON (fn.name);
CREATE INDEX nist_category_name IF NOT EXISTS FOR (c:Category) ON (c.name);
"""

# CORRECTED: Changed property from 'id' to 'framework_id' for consistency.
framework = """
MERGE (f:Framework {framework_id: "NIST_CSF_2.0"})
ON CREATE SET
  f.name = "NIST Cybersecurity Framework 2.0",
  f.version = "2.0",
  f.release_date = date("2024-02-26"),
  f.description = "Framework for managing cybersecurity risks";
"""

functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {function_id: row.Function_Code, framework_id: "NIST_CSF_2.0"})
ON CREATE SET
  fn.name = row.Function,
  fn.description = row.Function_Description;
"""

# CORRECTED: Used '=' instead of ':' for property assignment in SET clause.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {category_id: row.Category_Code, framework_id: "NIST_CSF_2.0"})
ON CREATE SET
  c.function_id = row.Function_Code,
  c.name = row.Category,
  c.description = row.Category_Description;
"""

# CORRECTED: Used '=' instead of ':' for property assignment in SET clause.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {subcategory_id: row.Subcategory, framework_id: "NIST_CSF_2.0"})
ON CREATE SET
  s.category_id = row.Category_Code,
  s.description = row.Subcategory_Description,
  s.example = row.Implementation_Example;
"""

# No changes needed here, as it now correctly matches the 'framework_id' property.
framework_functions_rel = """
MATCH (f:Framework {framework_id: 'NIST_CSF_2.0'})
MATCH (fn:Function {framework_id: 'NIST_CSF_2.0'})
MERGE (f)-[:CONTAINS]->(fn);
"""

function_categories_rel = """
MATCH (fn:Function {framework_id: 'NIST_CSF_2.0'})
MATCH (c:Category {framework_id: 'NIST_CSF_2.0'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:HAS_CATEGORY]->(c);
"""

category_subcategories_rel = """
MATCH (c:Category {framework_id: 'NIST_CSF_2.0'})
MATCH (s:Subcategory {framework_id: 'NIST_CSF_2.0'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CONTAINS]->(s);
"""


import os
import time
import logging
from App.app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)
    

logger.info("Loading graph structure...")

client.query(framework)
time.sleep(2)
logger.info('Framework')

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
client.query(framework_functions_rel)
time.sleep(2)

client.query(function_categories_rel)
time.sleep(2)

client.query(category_subcategories_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

client.close()