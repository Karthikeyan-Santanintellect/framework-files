# iso27001.py

# UPDATED: Constraints are now composite, requiring IDs to be unique within a framework.
constraints = """
CREATE CONSTRAINT framework_id_unique FOR (f:Framework) REQUIRE f.framework_id IS UNIQUE;
CREATE CONSTRAINT clause_framework_composite_unique FOR (c:Clause) REQUIRE (c.framework_id, c.clause_id) IS UNIQUE;
CREATE CONSTRAINT control_framework_composite_unique FOR (ctrl:Control) REQUIRE (ctrl.framework_id, ctrl.control_id) IS UNIQUE;
CREATE CONSTRAINT requirement_framework_composite_unique FOR (r:Requirement) REQUIRE (r.framework_id, r.requirement_id) IS UNIQUE;
CREATE CONSTRAINT category_framework_composite_unique FOR (cc:ControlCategory) REQUIRE (cc.framework_id, cc.category_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX clause_title_index FOR (c:Clause) ON (c.title);
CREATE INDEX control_name_index FOR (ctrl:Control) ON (ctrl.control_name);
CREATE INDEX control_category_index FOR (ctrl:Control) ON (ctrl.category);
"""

# UPDATED: Using MERGE to prevent errors on re-runs.
framework = """
MERGE (f:Framework {framework_id: 'ISO27001_2022'})
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
MERGE (cc:ControlCategory {framework_id: 'ISO27001_2022', category_id: row.category_id})
ON CREATE SET
    cc.category_name = row.category_name,
    cc.control_range = row.control_range,
    cc.control_count = toInteger(row.control_count);
"""

# UPDATED: Added framework_id and switched to MERGE.
clauses = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Clause {framework_id: 'ISO27001_2022', clause_id: row.clause_id})
ON CREATE SET
    c.title = row.title,
    c.description = row.description,
    c.category = row.category,
    c.parent_clause = CASE WHEN row.parent_clause <> '' THEN row.parent_clause ELSE null END;
"""

# UPDATED: Added framework_id and switched to MERGE.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {framework_id: 'ISO27001_2022', control_id: row.control_id})
ON CREATE SET
    ctrl.control_name = row.control_name,
    ctrl.category = row.category,
    ctrl.category_name = row.category_name,
    ctrl.legacy_mapping = row.legacy_mapping,
    ctrl.is_new = CASE WHEN row.is_new = 'Yes' THEN true ELSE false END,
    ctrl.full_description = row.full_description;
"""

# UPDATED: Added framework_id and switched to MERGE. Attribute combination is the key.
attributes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Attribute {framework_id: 'ISO27001_2022', attribute_type: row.attribute_type, attribute_value: row.attribute_value})
ON CREATE SET
    a.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Requirement {framework_id: 'ISO27001_2022', requirement_id: row.requirement_id})
ON CREATE SET
    r.clause_id = row.clause_id,
    r.requirement_text = row.requirement_text,
    r.requirement_type = row.requirement_type;
"""

# No changes needed here, as the MATCH is already specific.
framework_clauses = """
MATCH (f:Framework {framework_id: 'ISO27001_2022'})
MATCH (c:Clause {framework_id: 'ISO27001_2022', category: 'main_clause'})
MERGE (f)-[:CONTAINS]->(c);
"""

# UPDATED: Scoped MATCH to framework_id for precision.
clause_subclauses = """
MATCH (main:Clause {framework_id: 'ISO27001_2022', category: 'main_clause'})
MATCH (sub:Clause {framework_id: 'ISO27001_2022', category: 'subclause'})
WHERE sub.parent_clause = main.clause_id
MERGE (main)-[:CONTAINS]->(sub);
"""

# UPDATED: Scoped MATCH to framework_id.
framework_control_category = """
MATCH (f:Framework {framework_id: 'ISO27001_2022'})
MATCH (cat:ControlCategory {framework_id: 'ISO27001_2022'})
MERGE (f)-[:CONTAINS]->(cat);
"""

# UPDATED: Scoped MATCH to framework_id. Note the spelling fix for 'control'.
control_categories_control = """
MATCH (cat:ControlCategory {framework_id: 'ISO27001_2022'})
MATCH (ctrl:Control {framework_id: 'ISO27001_2022'})
WHERE cat.category_id = ctrl.category
MERGE (cat)-[:CONTAINS]->(ctrl);
"""

# UPDATED: Scoped MATCH to framework_id.
clause_requirements = """
MATCH (c:Clause {framework_id: 'ISO27001_2022'})
MATCH (r:Requirement {framework_id: 'ISO27001_2022'})
WHERE c.clause_id = r.clause_id
MERGE (c)-[:REQUIRES]->(r);
"""
# ... (rest of the python script remains the same)s

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

client.query(control_categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/iso27001_control_categories.csv'))
time.sleep(2)

client.query(clauses.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/iso27001_clauses.csv'))
time.sleep(2)

client.query(controls.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/iso27001_controls.csv'))
time.sleep(2)

client.query(attributes.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/iso27001_attributes.csv'))
time.sleep(2)

client.query(requirements.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027001/iso27001_requirements.csv'))
time.sleep(2)

client.query(framework_clauses)
time.sleep(2)

client.query(clause_subclauses)
time.sleep(2)

client.query(framework_control_category)
time.sleep(2)

client.query(control_categories_control)
time.sleep(2)

client.query(clause_requirements)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

res=client.query("""MATCH path = (:Framework)-[*]->()
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

import json
with open('iso27001.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(res, default=str))

client.close()