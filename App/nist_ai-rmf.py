# nist_ai-rmf.py

# UPDATED: Constraints are now composite to ensure uniqueness within a framework.
constraints = """
// Create all unique constraints for data integrity
CREATE CONSTRAINT ai_rmf_framework_id_unique IF NOT EXISTS FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT ai_rmf_function_id_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.IS_frameworks_standard_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_category_id_unique IF NOT EXISTS FOR (c:Category) REQUIRE (c.IS_frameworks_standard_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_subcategory_id_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.IS_frameworks_standard_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_characteristic_id_unique IF NOT EXISTS FOR (tc:TrustworthyCharacteristic) REQUIRE (tc.IS_frameworks_standard_id, tc.characteristic_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_lifecycle_stage_id_unique IF NOT EXISTS FOR (ls:LifecycleStage) REQUIRE (ls.IS_frameworks_standard_id, ls.stage_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_risk_type_id_unique IF NOT EXISTS FOR (rt:RiskType) REQUIRE (rt.IS_frameworks_standard_id, rt.risk_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_ai_system_id_unique IF NOT EXISTS FOR (ai:AISystem) REQUIRE (ai.IS_frameworks_standard_id, ai.system_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_org_id_unique IF NOT EXISTS FOR (o:Organization) REQUIRE (o.IS_frameworks_standard_id, o.org_id) IS UNIQUE;
CREATE CONSTRAINT ai_rmf_stakeholder_id_unique IF NOT EXISTS FOR (sh:Stakeholder) REQUIRE (sh.IS_frameworks_standard_id, sh.stakeholder_id) IS UNIQUE;
"""

indexes = """
// Create comprehensive performance indexes
CREATE INDEX ai_rmf_function_cross_cutting_stage IF NOT EXISTS FOR (fn:Function) ON (fn.is_cross_cutting, fn.lifecycle_stage);
CREATE INDEX ai_rmf_subcategory_function_category IF NOT EXISTS FOR (s:Subcategory) ON (s.function_id, s.category_id);
CREATE INDEX ai_rmf_ai_system_risk_implementation IF NOT EXISTS FOR (ai:AISystem) ON (ai.risk_level, ai.ai_rmf_implementation);
CREATE INDEX ai_rmf_org_adoption_maturity IF NOT EXISTS FOR (o:Organization) ON (o.ai_rmf_adoption, o.implementation_maturity);
"""

# UPDATED: Using MERGE to prevent duplicates.
framework_and_standards = """
// Load NIST AI RMF Framework
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
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
MERGE (fn:Function {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0', function_id: row.Function_ID})
ON CREATE SET
    fn.name = row.Function,
    fn.definition = row.Function_Description;
"""

# UPDATED: Using MERGE and adding framework_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0', category_id: row.Category_ID})
ON CREATE SET
    c.function_id = row.Function_ID,
    c.name = row.Category;
"""

# UPDATED: Using MERGE and adding framework_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0', subcategory_id: row.Subcategory_ID})
ON CREATE SET
    s.function_id = row.Function_ID,
    s.category_id = row.Category_ID,
    s.name = row.Subcategory;
"""

framework_functions_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MERGE (f)-[:FRAMEWORK_CONTAINS_FUNCTIONS]->(fn);
"""

function_categories_rel = """
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORY]->(c);
"""

category_subcategories_rel = """
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MATCH (s:Subcategory {IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
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

client.query(framework_and_standards)
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
with open('nist-ai-rmf.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist-ai-rmf.json")


client.close()
