# nist_pmf_1.py
# nist_pmf_1.py - CONSTRAINTS

constraints_framework = """
CREATE CONSTRAINT pmf_10_framework_id_unique IF NOT EXISTS 
FOR (f:FrameworkAndStandard) REQUIRE f.framework_standard_id IS UNIQUE;
"""

constraints_function = """
CREATE CONSTRAINT pmf_10_function_id_unique IF NOT EXISTS 
FOR (fn:Function) REQUIRE (fn.framework_standard_id, fn.function_id) IS UNIQUE;
"""

constraints_category = """
CREATE CONSTRAINT pmf_10_category_id_unique IF NOT EXISTS 
FOR (c:Category) REQUIRE (c.framework_standard_id, c.category_id) IS UNIQUE;
"""

constraints_subcategory = """
CREATE CONSTRAINT pmf_10_subcategory_id_unique IF NOT EXISTS 
FOR (s:Subcategory) REQUIRE (s.framework_standard_id, s.subcategory_id) IS UNIQUE;
"""

# Indexes
index_function_foundational = """
CREATE INDEX pmf_10_function_foundational IF NOT EXISTS 
FOR (fn:Function) ON (fn.is_foundational);
"""

index_function_name = """
CREATE INDEX pmf_10_function_name IF NOT EXISTS 
FOR (fn:Function) ON (fn.name);
"""

index_category_function = """
CREATE INDEX pmf_10_category_function IF NOT EXISTS 
FOR (c:Category) ON (c.function_id);
"""

index_subcategory_category = """
CREATE INDEX pmf_10_subcategory_category IF NOT EXISTS 
FOR (s:Subcategory) ON (s.category_id);
"""

index_subcategory_type = """
CREATE INDEX pmf_10_subcategory_type IF NOT EXISTS 
FOR (s:Subcategory) ON (s.type);
"""

# FrameworkAndStandard
framework_and_standard = """
MERGE (f:FrameworkAndStandard {framework_standard_id: 'NIST_PRIVACY_2020'})
SET
    f.name = 'NIST Privacy Framework 1.0',
    f.full_title = 'A Tool for Improving Privacy through Enterprise Risk Management',
    f.version = '1.0',
    f.publication = 'NIST CSWP 01162020',
    f.publication_date = date('2020-01-16'),
    f.status = 'Active',
    f.purpose = 'Enable better privacy engineering practices that support privacy by design concepts'
RETURN f;
"""

# Functions
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {function_id: row.function_id, framework_standard_id: 'NIST_PRIVACY_2020'})
ON CREATE SET 
    fn.function_name = row.function_name,
    fn.function_definition = row.function_definition,
    fn.is_foundational = CASE row.is_foundational WHEN 'True' THEN true ELSE false END,
    fn.category_count = toInteger(row.category_count),
    fn.subcategory_count = toInteger(row.subcategory_count),
    fn.primary_focus = row.primary_focus,
    fn.key_activities = row.key_activities;

"""

#categories
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {category_id: row.category_id, framework_standard_id: 'NIST_PRIVACY_2020'})
ON CREATE SET  
    c.function_id = row.function_id,
    c.category_name = row.category_name,
    c.subcategory_count = toInteger(row.subcategory_count),
    c.category_description = row.category_description;
"""

#subcategories
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory { subcategory_id: row.`Sub-Category`, framework_standard_id: 'NIST_PRIVACY_2020' })
ON CREATE SET 
    s.category_id = row.Category,
    s.function_id = row.Function,
    s.subcategory_name = row.subcategory_name,
    s.subcategory_type = row.subcategory_type;
"""

# Relationships
framework_standard_functions_rel = """
MATCH (f:FrameworkAndStandard {framework_standard_id: 'NIST_PRIVACY_2020'})
MATCH (fn:Function {framework_standard_id: 'NIST_PRIVACY_2020'})
MERGE (f)-[:FRAMEWORK_CONTAINS_FUNCTIONS]->(fn)
RETURN count(*) as created;
"""

function_categories_rel = """
MATCH (fn:Function {framework_standard_id: 'NIST_PRIVACY_2020'})
MATCH (c:Category {framework_standard_id: 'NIST_PRIVACY_2020'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORIES]->(c)
RETURN count(*) as created;
"""
category_subcategories_rel = """
MATCH (c:Category {framework_standard_id: 'NIST_PRIVACY_2020'})
MATCH (s:Subcategory{ framework_standard_id: 'NIST_PRIVACY_2020'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CATEGORY_CONTAINS_SUBCATEGORIES]->(s)
RETURN count(*) as created;
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

client.query(framework_and_standard)
time.sleep(2)
logger.info('FrameworkAndStandard')

client.query(functions.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/functions.csv"))
time.sleep(2)
logger.info('Functions')

client.query(categories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/categories.csv"))
time.sleep(2)
logger.info('Categories')

client.query(subcategories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/subcategories.csv"))
time.sleep(2)
logger.info('Subcategories')

logger.info("Creating relationships...")
client.query(framework_standard_functions_rel)
time.sleep(2)

client.query(function_categories_rel)
time.sleep(2)

client.query(category_subcategories_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

output_filename = "nist_pmf_1.json"

res = client.query("""
    MATCH path = (:FrameworkAndStandard)-[*]->()
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
    logger.error(f" Export query failed: {res}")
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
