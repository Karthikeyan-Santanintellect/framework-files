# 1. INITIALIZE THE FRAMEWORK NODE
framework_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO42001_2023'})
ON CREATE SET
    f.name = 'ISO/IEC 42001:2023',
    f.version = '2023',
    f.publication_date = date('2023-12-01'),
    f.status = 'Active',
    f.description = 'Information technology - Artificial intelligence - Management system';
"""

# 2. LOAD CONTROL CATEGORIES (From control_categories.csv)
control_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ControlCategory {IS_frameworks_standard_id: 'ISO42001_2023', category_id: row.category_id})
ON CREATE SET
    cc.name = row.category_name,
    cc.range = row.control_range,
    cc.description = row.description,   
    cc.control_count = toInteger(row.control_count);
"""

# 3. LOAD CLAUSES & SUBCLAUSES (From clauses.csv)
clauses = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Clause {IS_frameworks_standard_id: 'ISO42001_2023', clause_id: row.clause_id})
ON CREATE SET
    c.name = row.clause_name,
    c.description = row.description,
    c.category = row.category,
    c.parent_clause = CASE WHEN row.parent_clause <> '' THEN row.parent_clause ELSE null END;
"""

# 4. LOAD CONTROLS (From controls.csv)
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {IS_frameworks_standard_id: 'ISO42001_2023', control_id: row.control_id})
ON CREATE SET
    ctrl.name = row.control_name,
    ctrl.category = row.category,
    ctrl.category_name = row.category_name,
    ctrl.legacy_mapping = row.legacy_mapping,
    ctrl.is_new = CASE WHEN row.is_new = 'Yes' THEN true ELSE false END,
    ctrl.full_description = row.full_description;
"""

# 5. LOAD ATTRIBUTES / ENTITIES (From attributes.csv)
attributes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Attribute {IS_frameworks_standard_id: 'ISO42001_2023', attribute_type: row.attribute_type, attribute_value: row.attribute_value})
ON CREATE SET
    a.description = row.description;
"""

# 6. LOAD REQUIREMENTS / SHALL STATEMENTS (From requirements.csv)
requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Requirement {IS_frameworks_standard_id: 'ISO42001_2023', requirement_id: row.requirement_id})
ON CREATE SET
    r.clause_id = row.clause_id,
    r.text = row.requirement_text,
    r.type = row.requirement_type;
"""
# RELATIONSHIP BUILDERS (Execute these AFTER loading nodes)

# 7. CONNECT FRAMEWORK TO MAIN CLAUSES
framework_standard_clauses = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO42001_2023', category: 'main_clause'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CLAUSES]->(c);
"""

# 8. CONNECT MAIN CLAUSES TO SUBCLAUSES
clause_subclauses = """
MATCH (main:Clause {IS_frameworks_standard_id: 'ISO42001_2023', category: 'main_clause'})
MATCH (sub:Clause {IS_frameworks_standard_id: 'ISO42001_2023', category: 'subclause'})
WHERE sub.parent_clause = main.clause_id
MERGE (main)-[:CLAUSE_CONTAINS_SUBCLAUSES]->(sub);
"""

# 9. CONNECT FRAMEWORK TO CONTROL CATEGORIES (Annex A mapping)
framework_standard_control_category = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (cat:ControlCategory {IS_frameworks_standard_id: 'ISO42001_2023'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CONTROL_CATEGORY]->(cat);
"""

# 10. CONNECT CONTROL CATEGORIES TO INDIVIDUAL CONTROLS
control_categories_control = """
MATCH (cat:ControlCategory {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO42001_2023'})
WHERE cat.category_id = ctrl.category
MERGE (cat)-[:CONTROL_CATEGORIES_CONTAINS_CONTROL]->(ctrl);
"""

# 11. CONNECT CLAUSES TO THEIR MANDATORY REQUIREMENTS ("Shall" statements)
clause_requirements = """
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (r:Requirement {IS_frameworks_standard_id: 'ISO42001_2023'})
MERGE (c)-[:CLAUSE_REQUIRES_REQUIREMENT]->(r);
"""
clause_controls = """
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO42001_2023'})
MERGE (c)-[:CLAUSE_REQUIRES_CONTROL]->(ctrl);
"""

control_attributes = """
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO42001_2023'})
MATCH (a:Attribute {IS_frameworks_standard_id: 'ISO42001_2023'})
MERGE (ctrl)-[:CONTROL_HAS_ATTRIBUTE]->(a);
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

client.query(framework_standard)
time.sleep(2)

client.query(control_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2042001/control_categories.csv"))
time.sleep(2)

client.query(clauses.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2042001/clauses.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2042001/controls.csv"))
time.sleep(2)

client.query(attributes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2042001/attributes.csv"))
time.sleep(2)

client.query(requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2042001/requirements.csv"))
time.sleep(2)


logger.info("Creating relationships...")

client.query(framework_standard_clauses)
time.sleep(2)

client.query(clause_subclauses)
time.sleep(2)

client.query(framework_standard_control_category)
time.sleep(2)

client.query(control_categories_control)
time.sleep(2)

client.query(clause_requirements)
time.sleep(2)

client.query(clause_controls)
time.sleep(2)

client.query(control_attributes)
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
with open('iso-42001.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to iso-42001.json")

client.close()