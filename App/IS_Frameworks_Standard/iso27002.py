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
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: row."ISO27002_2022"})
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
MERGE (c:Category {IS_frameworks_standard_id: 'ISO27002_2022', category_id: row.category_id})
ON CREATE SET
    c.code = row.category_code,
    c.name = row.category_name,
    c.count = toInteger(row.control_count),
    c.range = row.control_range,
    c.description = row.description;
"""

# UPDATED: Added framework_id and switched to MERGE.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022', control_id: row.control_id})
ON CREATE SET
    ctrl.name = row.control_name,
    ctrl.purpose = row.purpose,
    ctrl.category_id = row.category_id,
    ctrl.category_code = row.category_code,
    ctrl.legacy_mapping = row.legacy_mapping,
    ctrl.is_new = CASE WHEN row.is_new = 'Yes' THEN true ELSE false END,
    ctrl.implementation_guidance = row.implementation_guidance,
    ctrl.description = row.control_description;
"""

# UPDATED: Added framework_id and switched to MERGE.
attributes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Attribute {IS_frameworks_standard_id: 'ISO27002_2022', attribute_id: row.attribute_id})
ON CREATE SET
    a.type = row.attribute_type,
    a.value = row.attribute_value,
    a.description = row.attribute_description,
    a.usage_context = row.usage_context;
"""

# UPDATED: Added framework_id and switched to MERGE.
guidelines = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (g:Guideline {IS_frameworks_standard_id: 'ISO27002_2022', guideline_id: row.guideline_id})
ON CREATE SET
    g.control_id = row.control_id,
    g.type = row.guideline_type,
    g.text = row.guideline_text,
    g.implementation_considerations = row.implementation_considerations,
    g.measurement_criteria = row.measurement_criteria;
"""

# UPDATED: Scoped MATCH to framework_id.
framework_standard_category_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (c:Category {IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CATEGORY]->(c);
"""

# UPDATED: Scoped MATCH to framework_id.
category_control_rel = """
MATCH (cat:Category {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022'})
WHERE cat.category_id = ctrl.category_id
MERGE (cat)-[:CATEGORY_CONTAINS_CONTROL]->(ctrl);
"""

# UPDATED: Scoped MATCH to framework_id.
control_guideline_rel = """
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022'})
MATCH (guide:Guideline {IS_frameworks_standard_id: 'ISO27002_2022'})
WHERE ctrl.control_id = guide.control_id
MERGE (ctrl)-[:CONTROL_HAS_GUIDELINE]->(guide);
"""

# UPDATED: Scoped MATCH to framework_id.
control_attribute_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27002_2022', control_id: row.control_id})
MATCH (attr:Attribute {IS_frameworks_standard_id: 'ISO27002_2022', attribute_id: row.attribute_id})
MERGE (ctrl)-[:CONTROL_HAS_ATTRIBUTE {relevance: row.relevance}]->(attr);
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

client.query(framework_standard.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_framework.csv'))
time.sleep(2)

client.query(categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_categories.csv'))
time.sleep(2)

client.query(controls.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_controls.csv'))
time.sleep(2)

client.query(attributes.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_attributes.csv'))
time.sleep(2)

client.query(guidelines.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_guidelines.csv'))
time.sleep(2)

client.query(framework_standard_category_rel)
time.sleep(2)

client.query(category_control_rel)
time.sleep(2)

client.query(control_guideline_rel)
time.sleep(2)

client.query(control_attribute_rel.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/ISO%2027002/iso27002_control_attributes.csv'))

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
with open('iso-27002.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to iso-27002.json")


client.close()