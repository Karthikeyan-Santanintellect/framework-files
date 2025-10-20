# nist_pmf_1.py

# UPDATED: Using MERGE to prevent duplicates.
framework = """
// Load NIST Privacy Framework 1.0
MERGE (f:Framework {framework_id: 'NIST_PRIVACY_2020'})
ON CREATE SET
    f.name = 'NIST Privacy Framework',
    f.full_title = 'A Tool for Improving Privacy through Enterprise Risk Management',
    f.version = '1.0',
    f.publication = 'NIST CSWP 01162020',
    f.publication_date = date('2020-01-16'),
    f.total_functions = 5,
    f.total_categories = 18,
    f.total_subcategories = 12,
    f.status = 'Active',
    f.purpose = 'Enable better privacy engineering practices that support privacy by design concepts';
"""

# UPDATED: Using MERGE and adding framework_id.
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {framework_id: 'NIST_PRIVACY_2020', function_id: row.function_id})
ON CREATE SET
    fn.name = row.function_name,
    fn.definition = row.function_definition,
    fn.primary_focus = row.primary_focus,
    fn.key_activities = split(row.key_activities, ','),
    fn.is_foundational = CASE WHEN row.is_foundational = 'True' THEN true ELSE false END;
"""

# UPDATED: Using MERGE and adding framework_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {framework_id: 'NIST_PRIVACY_2020', category_id: row.category_id})
ON CREATE SET
    c.function_id = row.function_id,
    c.name = row.category_name,
    c.definition = row.category_definition;
"""

# UPDATED: Using MERGE and adding framework_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {framework_id: 'NIST_PRIVACY_2020', subcategory_id: row.`Sub-Category`})
ON CREATE SET
    s.function_id = row.Function,
    s.category_id = row.Category,
    s.name = row.subcategory_name;
"""

framework_functions_rel = """
MATCH (f:Framework {framework_id: 'NIST_PRIVACY_2020'})
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_2020'})
MERGE (f)-[:CONTAINS]->(fn);
"""

function_categories_rel = """
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_2020'})
MATCH (c:Category {framework_id: 'NIST_PRIVACY_2020'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:HAS_CATEGORY]->(c);
"""

category_subcategories_rel = """
MATCH (c:Category {framework_id: 'NIST_PRIVACY_2020'})
MATCH (s:Subcategory {framework_id: 'NIST_PRIVACY_2020'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CONTAINS]->(s);
"""

import os
import time
import logging
from app import Neo4jConnect

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

client.query(functions.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/functions.csv'))
time.sleep(2)
logger.info('Function')

client.query(categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/categories.csv'))
time.sleep(2)
logger.info('Category')

client.query(subcategories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/subcategories.csv'))
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
