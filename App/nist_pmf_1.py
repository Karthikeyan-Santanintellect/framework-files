# nist_pmf_1.py
# nist_pmf_1.py - CONSTRAINTS

constraints_framework = """
CREATE CONSTRAINT pmf_10_framework_id_unique IF NOT EXISTS 
FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
"""

constraints_function = """
CREATE CONSTRAINT pmf_10_function_id_unique IF NOT EXISTS 
FOR (fn:Function) REQUIRE (fn.IS_frameworks_standard_id, fn.function_id) IS UNIQUE;
"""

constraints_category = """
CREATE CONSTRAINT pmf_10_category_id_unique IF NOT EXISTS 
FOR (c:Category) REQUIRE (c.IS_frameworks_standard_id, c.category_id) IS UNIQUE;
"""

constraints_subcategory = """
CREATE CONSTRAINT pmf_10_subcategory_id_unique IF NOT EXISTS 
FOR (s:Subcategory) REQUIRE (s.IS_frameworks_standard_id, s.subcategory_id) IS UNIQUE;
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

# ISFrameworksAndStandard
IS_framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
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
MERGE (fn:Function {function_id: row.Function_ID, IS_frameworks_standard_id: 'NIST_PMF_1.0'})
ON CREATE SET 
    fn.name = row.Function_Name,
    fn.definition = row.Function_Definition,
    fn.is_foundational = row.Is_Foundational;
"""

#categories
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {category_id: row.category_id, IS_frameworks_standard_id: 'NIST_PMF_1.0'})
ON CREATE SET  
    c.function_id = row.function_id,
    c.name = row.category_name,
    c.subcategory_count = toInteger(row.subcategory_count),
    c.description = row.category_description;
"""

#subcategories
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory { subcategory_id: row.Subcategory_Code, IS_frameworks_standard_id: 'NIST_PMF_1.0' })
ON CREATE SET 
    s.category_id = row.Category_Code,
    s.function_id = row.Function_Code,
    s.description = row.Subcategory_Description;
"""
# Tiers
tiers = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:ImplementationTier { tier_id: row.Tier_ID, IS_frameworks_standard_id: 'NIST_PMF_1.0' })
ON CREATE SET 
    t.name = row.Tier_Name,
    t.description = row.Tier_Description;
"""
# Term (Glossary)
terms = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Term { name: row.Term, IS_frameworks_standard_id: 'NIST_PMF_1.0' })
ON CREATE SET 
    t.definition = row.Definition;
"""

# Relationships
framework_standard_functions_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (f)-[:FRAMEWORK_CONTAINS_FUNCTIONS]->(fn)
RETURN count(*) as created;
"""

function_categories_rel = """
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORIES]->(c)
RETURN count(*) as created;
"""
category_subcategories_rel = """
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MATCH (s:Subcategory{ IS_frameworks_standard_id: 'NIST_PMF_1.0'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CATEGORY_CONTAINS_SUBCATEGORIES]->(s)
RETURN count(*) as created;
"""
# Framework -> Tiers
framework_tiers_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MATCH (t:ImplementationTier {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (f)-[:FRAMEWORK_DEFINES_TIER]->(t)
"""
# Framework -> Glossary Terms
framework_glossary_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MATCH (t:Term {IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (f)-[:FRAMEWORK_DEFINES_TERM]->(t)
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

client.query(IS_framework_and_standard)
time.sleep(2)
logger.info('ISFrameworksAndStandard')

client.query(functions.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/NIST%20PMF%201.0%20-%20Functions.csv"))
time.sleep(2)
logger.info('Functions')

client.query(categories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/NIST%20PMF%201.0%20-%20Categories.csv"))
time.sleep(2)
logger.info('Categories')

client.query(subcategories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/NIST%20PMF%201.0%20-%20Subcategories.csv"))
time.sleep(2)
logger.info('Subcategories')

client.query(tiers.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/NIST%20PMF%201.0%20-%20Tiers.csv"))
time.sleep(2)
logger.info('Tiers')

client.query(terms.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/NIST%20PMF%201.0%20-%20Term.csv"))
time.sleep(2)
logger.info('Terms')

# Relationships
logger.info("Creating relationships...")
client.query(framework_standard_functions_rel)
time.sleep(2)

client.query(function_categories_rel)
time.sleep(2)

client.query(category_subcategories_rel)
time.sleep(2)

client.query(framework_tiers_rel)
time.sleep(2)

client.query(framework_glossary_rel)
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
with open('nist_pmf_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist_pmf_1.json")


client.close()