# nist_ai-rmf.py

# UPDATED: Constraints are now composite to ensure uniqueness within a framework.
constraints = """
// Create all unique constraints for data integrity
CREATE CONSTRAINT ai_rmf_framework_id_unique IF NOT EXISTS FOR (f:Framework) REQUIRE f.framework_id IS UNIQUE;
CREATE CONSTRAINT ai_rmf_function_id_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.framework_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_category_id_unique IF NOT EXISTS FOR (c:Category) REQUIRE (c.framework_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_subcategory_id_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.framework_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_characteristic_id_unique IF NOT EXISTS FOR (tc:TrustworthyCharacteristic) REQUIRE (tc.framework_id, tc.characteristic_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_lifecycle_stage_id_unique IF NOT EXISTS FOR (ls:LifecycleStage) REQUIRE (ls.framework_id, ls.stage_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_risk_type_id_unique IF NOT EXISTS FOR (rt:RiskType) REQUIRE (rt.framework_id, rt.risk_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_ai_system_id_unique IF NOT EXISTS FOR (ai:AISystem) REQUIRE (ai.framework_id, ai.system_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_org_id_unique IF NOT EXISTS FOR (o:Organization) REQUIRE (o.framework_id, o.org_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_stakeholder_id_unique IF NOT EXISTS FOR (sh:Stakeholder) REQUIRE (sh.framework_id, sh.stakeholder_id) IS UNIQUE;
"""

indexes = """
// Create comprehensive performance indexes
CREATE INDEX ai_rmf_function_cross_cutting_stage IF NOT EXISTS FOR (fn:Function) ON (fn.is_cross_cutting, fn.lifecycle_stage);
CREATE INDEX ai_rmf_subcategory_function_category IF NOT EXISTS FOR (s:Subcategory) ON (s.function_id, s.category_id);
CREATE INDEX ai_rmf_ai_system_risk_implementation IF NOT EXISTS FOR (ai:AISystem) ON (ai.risk_level, ai.ai_rmf_implementation);
CREATE INDEX ai_rmf_org_adoption_maturity IF NOT EXISTS FOR (o:Organization) ON (o.ai_rmf_adoption, o.implementation_maturity);
"""

# UPDATED: Using MERGE to prevent duplicates.
framework = """
// Load NIST AI RMF Framework
MERGE (f:Framework {framework_id: 'NIST_AI_RMF_2023'})
ON CREATE SET
    f.name = 'NIST AI Risk Management Framework',
    f.version = '1.0',
    f.publication = 'NIST AI 100-1',
    f.publication_date = date('2023-01-26'),
    f.total_functions = 4,
    f.total_categories = 19,
    f.total_subcategories = 77,
    f.trustworthy_ai_characteristics = 7,
    f.framework_type = 'Voluntary Framework';
"""

# UPDATED: Using MERGE and adding framework_id.
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {framework_id: 'NIST_AI_RMF_2023', function_id: row.Function_ID})
ON CREATE SET
    fn.function_name = row.Function,
    fn.function_definition = row.Function_Description;
"""

# UPDATED: Using MERGE and adding framework_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {framework_id: 'NIST_AI_RMF_2023', category_id: row.Category_ID})
ON CREATE SET
    c.function_id = row.Function_ID,
    c.name = row.Category;
"""

# UPDATED: Using MERGE and adding framework_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {framework_id: 'NIST_AI_RMF_2023', subcategory_id: row.Subcategory_ID})
ON CREATE SET
    s.function_id = row.Function_ID,
    s.category_id = row.Category_ID,
    s.name = row.Subcategory;
"""

framework_functions_rel = """
MATCH (f:Framework {framework_id: 'NIST_AI_RMF_2023'})
MATCH (fn:Function {framework_id: 'NIST_AI_RMF_2023'})
MERGE (f)-[:CONTAINS]->(fn);
"""

function_categories_rel = """
MATCH (fn:Function {framework_id: 'NIST_AI_RMF_2023'})
MATCH (c:Category {framework_id: 'NIST_AI_RMF_2023'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:HAS_CATEGORY]->(c);
"""

category_subcategories_rel = """
MATCH (c:Category {framework_id: 'NIST_AI_RMF_2023'})
MATCH (s:Subcategory {framework_id: 'NIST_AI_RMF_2023'})
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

client.query(functions.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_functions.csv'))
time.sleep(2)

client.query(categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_categories.csv'))
time.sleep(2)

client.query(subcategories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_subcategories.csv'))
time.sleep(2)

client.query(framework_functions_rel)
time.sleep(2)

client.query(function_categories_rel)
time.sleep(2)

client.query(category_subcategories_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

res=client.query("""MATCH path = (:Standard)-[*]->()
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
} AS graph_data""")

client.close()