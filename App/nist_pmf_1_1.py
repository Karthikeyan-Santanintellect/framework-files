# nist_pmf_1_1.py

# UPDATED: Constraints are now composite to ensure uniqueness within a ISFrameworksAndStandard.
constraints = """
CREATE CONSTRAINT pmf_11_ISFrameworksAndStandard_id_unique IF NOT EXISTS FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT pmf_11_function_id_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.IS_frameworks_standard_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_category_id_unique IF NOT EXISTS FOR (c:Category) REQUIRE (c.IS_frameworks_standard_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_subcategory_id_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.IS_frameworks_standard_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_objective_id_unique IF NOT EXISTS FOR (po:PrivacyObjective) REQUIRE (po.IS_frameworks_standard_id, po.objective_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_tier_id_unique IF NOT EXISTS FOR (it:ImplementationTier) REQUIRE (it.IS_frameworks_standard_id, it.tier_id) IS UNIQUE;
"""

indexes = """
// Create comprehensive performance indexes
CREATE INDEX pmf_11_function_foundational IF NOT EXISTS FOR (fn:Function) ON (fn.is_foundational, fn.function_id);
CREATE INDEX pmf_11_tier_maturity IF NOT EXISTS FOR (it:ImplementationTier) ON (it.tier_number, it.maturity_level);
CREATE INDEX pmf_11_ai_risk_impact IF NOT EXISTS FOR (apr:AIPrivacyRisk) ON (apr.impact_level, apr.likelihood);
CREATE INDEX pmf_11_org_v11_adoption IF NOT EXISTS FOR (o:Organization) ON (o.v11_adoption_date, o.ai_governance_committee);
"""

# UPDATED: Using MERGE to prevent duplicates.
IS_frameworks_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
SET
    f.name = 'NIST Privacy Framework 1.1',
    f.full_name = 'A Tool for Improving Privacy through Enterprise Risk Management - Version 1.1',
    f.version = '1.1',
    f.publication = 'NIST CSWP 01112025',
    f.publication_date = date('2025-01-11'),
    f.status = 'Active',
    f.purpose = 'Enhance privacy engineering practices supporting privacy by design concepts in AI systems';
"""


# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {function_id: row.Function_ID, IS_frameworks_standard_id: 'NIST_PMF_1.1'})
ON CREATE SET 
    fn.name = row.Function_Name,
    fn.definition = row.Function_Definition;
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {category_id: row.category_id, IS_frameworks_standard_id: 'NIST_PMF_1.1'})
ON CREATE SET  
    c.function_id = row.function_id,
    c.name = row.category_name,
    c.subcategory_count = row.subcategory_count,
    c.description = row.category_description;
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {subcategory_id: row.Subcategory_Code, IS_frameworks_standard_id: 'NIST_PMF_1.1' })
ON CREATE SET 
    s.category_id = row.Category_Code,
    s.function_id = row.Function_Code,
    s.description = row.Subcategory_Description;
"""


# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
implementation_tiers = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:ImplementationTier { tier_id: row.tier_id, IS_frameworks_standard_id: 'NIST_PMF_1.1' })
ON CREATE SET 
    t.name = row.tier_name,
    t.tier_number = row.tier_number,
    t.maturity_level = row.maturity_level,
    t.risk_management_process = row.privacy_risk_management,
    t.integrated_risk_program = row.integrated_risk_program,
    t.ecosystem_relationships = row.ecosystem_relationships,
    t.workforce = row.workforce,
    t.v11_updates = row.v11_updates;
"""


# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
objectives = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:PrivacyObjective {IS_frameworks_standard_id: 'NIST_PMF_1.1', objective_id: row.objective_id})
ON CREATE SET
    po.name = row.objective_name,
    po.definition = row.objective_definition,
    po.related_functions = split(row.related_functions, ','),
    po.engineering_focus = split(row.engineering_focus, ','),
    po.v11_updates = row.v11_updates;
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
framework_standard_function_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
WHERE fn.function_id IN ['ID-P', 'GV-P', 'CT-P', 'CM-P', 'PR-P']
MERGE (f)-[:FRAMEWORK_STANDARD_HAS_FUNCTION]->(fn);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_category_rel = """
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORY]->(c);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
category_subcategory_rel = """
MATCH (c:Category {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MATCH (s:Subcategory {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CATEGORY_HAS_SUBCATEGORY]->(s);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_objective_rel = """
MATCH (fn:Function {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MATCH (po:PrivacyObjective {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
WHERE fn.function_id IN po.related_functions
MERGE (fn)-[:FUNCTION_SUPPORTS_OBJECTIVE]->(po);
"""
# Function Tiers
framework_tiers_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MATCH (t:ImplementationTier {IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MERGE (f)-[:FRAMEWORK_DEFINES_TIER]->(t)
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

client.query(IS_frameworks_standard)
time.sleep(2)
logger.info('ISFrameworksAndStandard')

client.query(functions.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/NIST%20PMF%201.1%20-%20Functions.csv"))
time.sleep(2)
logger.info('Function')

client.query(categories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/NIST%20PMF%201.1%20-%20Categories.csv"))
time.sleep(2)
logger.info('Category')

client.query(subcategories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/NIST%20PMF%201.1%20-%20Subcategories.csv"))
time.sleep(2)
logger.info('Subcategory')

client.query(objectives.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/NIST%20PMF%201.1%20-%20Objectives.csv"))
time.sleep(2)
logger.info('Objective')


client.query(implementation_tiers.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/NIST%20PMF%201.1%20-%20Tiers.csv"))
time.sleep(2)
logger.info('ImplementationTier')


logger.info("Creating relationships...")

client.query(framework_standard_function_rel)
time.sleep(2)

client.query(function_category_rel)
time.sleep(2)

client.query(category_subcategory_rel)
time.sleep(2)

client.query(framework_tiers_rel)
time.sleep(2)

client.query(function_objective_rel)
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
with open('nist_pmf_1_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist_pmf_1_1.json")


client.close()
