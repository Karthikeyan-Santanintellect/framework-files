# iso27002.py

# UPDATED: Constraints are now composite, requiring IDs to be unique within a framework.
constraints = """
CREATE CONSTRAINT framework_id_unique FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT category_framework_composite_unique FOR (c:Category) REQUIRE (c.IS_frameworks_standard_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT control_framework_composite_unique FOR (ctrl:Control) REQUIRE (ctrl.IS_frameworks_standard_id, ctrl.control_id) IS UNIQUE;
CREATE CONSTRAINT attribute_framework_composite_unique FOR (a:Attribute) REQUIRE (a.IS_frameworks_standard_id, a.attribute_id) IS UNIQUE;
CREATE CONSTRAINT guideline_framework_composite_unique FOR (g:Guideline) REQUIRE (g.IS_frameworks_standard_id, g.guideline_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX control_name_index FOR (ctrl:Control) ON (ctrl.control_name);
CREATE INDEX control_category_index FOR (ctrl:Control) ON (ctrl.category_id);
CREATE INDEX attribute_type_index FOR (a:Attribute) ON (a.attribute_type);
CREATE INDEX organization_industry_index FOR (o:Organization) ON (o.industry);
CREATE INDEX control_new_index FOR (ctrl:Control) ON (ctrl.is_new);
"""

# UPDATED: Switched to MERGE.
framework_standard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: row.framework_id})
ON CREATE SET
    f.name = row.name,
    f.full_name = row.full_name,
    f.version = row.version,
    f.publication_date = date(row.publication_date),
    f.status = row.status,
    f.total_controls = toInteger(row.total_controls),
    f.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ControlCategory {category_id: row.category_id, IS_frameworks_standard_id: 'ISO27002_2022'})
ON CREATE SET
    cc.name = row.category_name,
    cc.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id, IS_frameworks_standard_id: 'ISO27002_2022'})
SET
    c.name = row.control_name,
    c.purpose = row.purpose,
    c.category_code = row.category_code,
    c.legacy_mapping = row.legacy_mapping,
    c.is_new = row.is_new;
"""

# UPDATED: Added framework_id and switched to MERGE.
attributes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Attribute {
    IS_frameworks_standard_id: 'ISO27002_2022', 
    type: row.attribute_type, 
    value: row.attribute_value
})
ON CREATE SET
    a.description = row.description;
"""


# UPDATED: Added framework_id and switched to MERGE.
guidelines = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (g:Guideline {guideline_id: row.guideline_id, IS_frameworks_standard_id: 'ISO27002_2022'})
SET
    g.control_id = row.control_id,
    g.text = row.guideline_text,
    g.type = row.guideline_type;
"""

# UPDATED: Scoped MATCH to framework_id.
framework_standard_category_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (cc:ControlCategory {IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CONTROL_CATEGORY]->(cc);
"""

# Clear this framework's relationships before rebuilding so a re-run replaces the
# edge set instead of leaving the old (cartesian) edges in place.
clear_relationships = """
MATCH (a {IS_frameworks_standard_id: 'ISO27002_2022'})-[r]-(b {IS_frameworks_standard_id: 'ISO27002_2022'})
DELETE r;
"""

# Each control carries its category_code (e.g. control 5.1 -> category 5); join on
# it rather than linking every category to every control.
category_control_rel = """
MATCH (cc:ControlCategory {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022'})
WHERE ctrl.category_code = cc.category_id
MERGE (cc)-[:CONTROL_CATEGORY_CONTAINS_CONTROL]->(ctrl);
"""

# Each guideline carries the control_id it elaborates; join on it rather than
# linking every control to every guideline.
control_guideline_rel = """
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (guide:Guideline {IS_frameworks_standard_id: 'ISO27002_2022'})
WHERE guide.control_id = ctrl.control_id
MERGE (ctrl)-[:CONTROL_HAS_GUIDELINE]->(guide);
"""

# The attribute CSV is the ISO 27002 attribute taxonomy with no per-control
# mapping, so attach the taxonomy to the framework (as ISO 27001 does) rather
# than joining every control to every attribute.
framework_attribute_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (a:Attribute {IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_ATTRIBUTES]->(a);
"""

# ... (rest of the python script remains the same)


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

client.query(framework_standard.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027002/iso27002_framework.csv'))
time.sleep(2)

client.query(categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027002/ISO%2027002%20-%20Categories.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027002/ISO%2027002%20-%20Controls.csv"))
time.sleep(2)

client.query(attributes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027002/ISO%2027002%20-%20Attributes.csv"))
time.sleep(2)

client.query(guidelines.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027002/ISO%2027002%20-%20Guidelines.csv"))
time.sleep(2)

client.query(clear_relationships)
time.sleep(2)

client.query(framework_standard_category_rel)
time.sleep(2)

client.query(category_control_rel)
time.sleep(2)

client.query(control_guideline_rel)
time.sleep(2)

client.query(framework_attribute_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH (n {IS_frameworks_standard_id: 'ISO27002_2022'})
OPTIONAL MATCH (n)-[r]-(m {IS_frameworks_standard_id: 'ISO27002_2022'})
WITH collect(DISTINCT n) AS uniqueNodes, collect(DISTINCT r) AS uniqueRels
RETURN {
  nodes: [n IN uniqueNodes | n {
    .*,
    id: elementId(n),
    labels: labels(n),
    mainLabel: head(labels(n))
  }],
  rels: [r IN uniqueRels WHERE r IS NOT NULL | r {
    .*,
    id: elementId(r),
    type: type(r),
    from: elementId(startNode(r)),
    to: elementId(endNode(r))
  }]
} AS graph_data""")

res = res[-1]['graph_data']

import json
with open('iso-27002.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to iso-27002.json")


client.close()