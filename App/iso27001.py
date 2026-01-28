# iso27001.py

# UPDATED: Constraints are now composite, requiring IDs to be unique within a framework.
from ctypes.macholib import framework


constraints = """
CREATE CONSTRAINT framework_id_unique FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT clause_framework_composite_unique FOR (c:Clause) REQUIRE (c.IS_frameworks_standard_id, c.clause_id) IS UNIQUE;
CREATE CONSTRAINT control_framework_composite_unique FOR (ctrl:Control) REQUIRE (ctrl.IS_frameworks_standard_id, ctrl.control_id) IS UNIQUE;
CREATE CONSTRAINT requirement_framework_composite_unique FOR (r:Requirement) REQUIRE (r.IS_frameworks_standard_id, r.requirement_id) IS UNIQUE;
CREATE CONSTRAINT category_framework_composite_unique FOR (cc:ControlCategory) REQUIRE (cc.IS_frameworks_standard_id, cc.category_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX clause_title_index FOR (c:Clause) ON (c.title);
CREATE INDEX control_name_index FOR (ctrl:Control) ON (ctrl.control_name);
CREATE INDEX control_category_index FOR (ctrl:Control) ON (ctrl.category);
"""

# UPDATED: Using MERGE to prevent errors on re-runs.
framework_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27001_2022'})
ON CREATE SET
    f.name = 'ISO/IEC 27001:2022',
    f.version = '2022',
    f.publication_date = date('2022-10-25'),
    f.status = 'Active',
    f.description = 'Information security, cybersecurity and privacy protection — Information security management systems — Requirements';
"""

# UPDATED: Added framework_id and switched to MERGE.
control_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ControlCategory {category_id: row.category_id, IS_frameworks_standard_id: 'ISO27001_2022'})
ON CREATE SET
    cc.name = row.category_name,
    cc.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
clauses = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cl:Clause {clause_id: row.clause_id, IS_frameworks_standard_id: 'ISO27001_2022'})
ON CREATE SET
    cl.title = row.title,
    cl.type = row.category,
    cl.parent_clause = row.parent_clause;
"""
# UPDATED: Added framework_id and switched to MERGE.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id, IS_frameworks_standard_id: 'ISO27001_2022'})
ON CREATE SET
    c.name = row.control_name,
    c.category_id = row.category_id;
"""

# UPDATED: Added framework_id and switched to MERGE. Attribute combination is the key.
attributes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Attribute {
    IS_frameworks_standard_id: 'ISO27001_2022', 
    type: row.attribute_type, 
    value: row.attribute_value
})
ON CREATE SET
    a.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Requirement {requirement_id: row.requirement_id, IS_frameworks_standard_id: 'ISO27001_2022'})
ON CREATE SET
    r.clause_id = row.clause_id,
    r.text = row.requirement_text;
"""

# No changes needed here, as the MATCH is already specific.
framework_standard_clauses = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27001_2022'})
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CLAUSES]->(c);
"""

# UPDATED: Scoped MATCH to framework_id.
framework_standard_control_category = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27001_2022'})
MATCH (cat:ControlCategory {IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CONTROL_CATEGORY]->(cat);
"""

# UPDATED: Scoped MATCH to framework_id. Note the spelling fix for 'control'.
control_categories_control = """
MATCH (cat:ControlCategory {IS_frameworks_standard_id: 'ISO27001_2022'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (cat)-[:CONTROL_CATEGORIES_CONTAINS_CONTROL]->(ctrl);
"""

# UPDATED: Scoped MATCH to framework_id.
clause_requirements = """
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO27001_2022'})
MATCH (r:Requirement {IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (c)-[:CLAUSE_REQUIRES_REQUIREMENT]->(r);
"""
# Framework -> Attributes relationships 
framework_attributes_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27001_2022'})
MATCH (a:Attribute {IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_ATTRIBUTES]->(a);
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

client.query(control_categories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/ISO%2027001%20-%20Control%20Categories.csv"))
time.sleep(2)

client.query(clauses.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/ISO%2027001%20-%20Clauses.csv"))
time.sleep(2)

client.query(controls.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/ISO%2027001%20-%20Controls.csv"))
time.sleep(2)

client.query(attributes.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/ISO%2027001%20-%20Attributes.csv"))
time.sleep(2)

client.query(requirements.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/ISO%2027001%20-%20Requirements.csv"))
time.sleep(2)


client.query(framework_standard_clauses)
time.sleep(2)


client.query(framework_standard_control_category)
time.sleep(2)

client.query(control_categories_control)
time.sleep(2)

client.query(clause_requirements)
time.sleep(2)

client.query(framework_attributes_rel)
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
with open('iso-27001.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to iso-27001.json")


client.close()