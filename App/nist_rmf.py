# nist_rmf.py

# UPDATED: Constraints are now composite to ensure uniqueness within a framework.
constraints = """
CREATE CONSTRAINT rmf_framework_id_unique IF NOT EXISTS FOR (f:FrameworkAndStandard) REQUIRE f.framework_standard_id IS UNIQUE;
CREATE CONSTRAINT rmf_step_id_unique IF NOT EXISTS FOR (s:Step) REQUIRE (s.framework_standard_id, s.step_id) IS UNIQUE;
CREATE CONSTRAINT rmf_family_id_unique IF NOT EXISTS FOR (cf:ControlFamily) REQUIRE (cf.framework_standard_id, cf.family_id) IS UNIQUE;
CREATE CONSTRAINT rmf_control_id_unique IF NOT EXISTS FOR (c:Control) REQUIRE (c.framework_standard_id, c.control_id) IS UNIQUE;
CREATE CONSTRAINT rmf_role_id_unique IF NOT EXISTS FOR (r:Role) REQUIRE (r.framework_standard_id, r.role_id) IS UNIQUE;
CREATE CONSTRAINT rmf_system_id_unique IF NOT EXISTS FOR (sys:System) REQUIRE (sys.framework_standard_id, sys.system_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX rmf_step_number_index IF NOT EXISTS FOR (s:Step) ON (s.step_number);
CREATE INDEX rmf_system_categorization_index IF NOT EXISTS FOR (sys:System) ON (sys.categorization);
CREATE INDEX rmf_authorization_status_index IF NOT EXISTS FOR (sys:System) ON (sys.authorization_status);
CREATE INDEX rmf_control_category_index IF NOT EXISTS FOR (cf:ControlFamily) ON (cf.control_category);
"""

# UPDATED: Using MERGE to prevent duplicates.
framework_and_standard = """
MERGE (f:FrameworkAndStandard {framework_standard_id: 'NIST_RMF_2018'})
ON CREATE SET
    f.name = 'NIST Risk Management Framework',
    f.publication = 'NIST SP 800-37 Revision 2',
    f.publication_date = date('2018-12-20'),
    f.total_steps = 7,
    f.total_control_families = 20,
    f.total_controls = 1000,
    f.status = 'Active',
    f.scope = 'Federal Information Systems and Organizations';
"""

# UPDATED: Using MERGE and adding framework_id.
steps = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Step {framework_standard_id: 'NIST_RMF_2018', step_id: row.step_id})
ON CREATE SET
    s.step_number = toInteger(row.step_number),
    s.step_name = row.step_name,
    s.objective = row.objective,
    s.is_new_in_rev2 = CASE WHEN row.is_new_in_rev2 = 'True' THEN true ELSE false END,
    s.step_description = row.step_description;
"""

# UPDATED: Using MERGE and adding framework_id.
control_families = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:ControlFamily {framework_standard_id: 'NIST_RMF_2018', family_id: row.family_id})
ON CREATE SET
    cf.family_name = row.family_name,
    cf.control_count = toInteger(row.control_count),
    cf.family_description = row.family_description,
    cf.control_category = row.control_category,
    cf.nist_publication = 'NIST SP 800-53 Rev 5';
"""

# UPDATED: Using MERGE and adding framework_id.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {framework_standard_id: 'NIST_RMF_2018', control_id: row.`Control Identifier`})
ON CREATE SET
    c.family_id = row.`Family`,
    c.name = row.`Control Name`,
    c.description = row.`Control`,
    c.related_controls = split(row.`Related Controls`, ',');
"""

# UPDATED: Using MERGE and adding framework_id.
roles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Role {framework_standard_id: 'NIST_RMF_2018', role_id: row.role_id})
ON CREATE SET
    r.role_title = row.role_title,
    r.role_description = row.role_description,
    r.role_type = row.role_type,
    r.decision_authority = row.decision_authority;
"""

# UPDATED: Using MERGE and adding framework_id.
systems = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System {framework_standard_id: 'NIST_RMF_2018', system_id: row.system_id})
ON CREATE SET
    sys.system_name = row.system_name,
    sys.system_type = row.system_type,
    sys.categorization = row.categorization,
    sys.authorization_status = row.authorization_status,
    sys.ato_date = CASE WHEN row.ato_date IS NOT NULL THEN date(row.ato_date) ELSE null END,
    sys.ato_expiration = CASE WHEN row.ato_expiration IS NOT NULL THEN date(row.ato_expiration) ELSE null END;
"""

# UPDATED: Scoped MATCH to framework_id.
framework_standard_step_rel = """
MATCH (f:FrameworkAndStandard {framework_standard_id: 'NIST_RMF_2018'})
MATCH (s:Step {framework_standard_id: 'NIST_RMF_2018'})
MERGE (f)-[:FRAMEWORK_CONTAINS_STEP]->(s);
"""

# UPDATED: Scoped MATCH to framework_id.
step_step_rel = """
MATCH (s1:Step {framework_standard_id: 'NIST_RMF_2018'}), (s2:Step {framework_standard_id: 'NIST_RMF_2018'})
WHERE s2.step_number = s1.step_number + 1
MERGE (s1)-[:STEP_PRECEDES_STEP]->(s2);
"""

# UPDATED: Scoped MATCH and changed CREATE to MERGE.
framework_standard_control_family_rel = """
MATCH (f:FrameworkAndStandard {framework_standard_id: 'NIST_RMF_2018'})
MATCH (cf:ControlFamily {framework_standard_id: 'NIST_RMF_2018'})
MERGE (f)-[:FRAMEWORK_REFERENCES_CONTROL_FAMILY]->(cf);
"""

# UPDATED: Scoped MATCH to framework_id.
control_family_control_rel = """
MATCH (cf:ControlFamily {framework_standard_id: 'NIST_RMF_2018'}), (c:Control {framework_standard_id: 'NIST_RMF_2018'})
WHERE cf.family_id = c.family_id
MERGE (cf)-[:CONTROL_FAMILY_INCLUDES_CONTROL]->(c);
"""

# UPDATED: Scoped MATCH to framework_id.
role_step_rel = """
MATCH (r:Role {framework_standard_id: 'NIST_RMF_2018', role_id: 'authorizing_official'})
MATCH (s:Step {framework_standard_id: 'NIST_RMF_2018'})
WHERE s.step_id IN ['2_categorize', '3_select', '6_authorize', '7_monitor']
MERGE (r)-[:ROLE_INVOLVED_IN_STEP {involvement_type: 'Decision_Making'}]->(s);
"""

# UPDATED: Scoped MATCH and changed CREATE to MERGE.
system_control_rel = """
MATCH (sys:System {framework_standard_id: 'NIST_RMF_2018'})
MATCH (c:Control {framework_standard_id: 'NIST_RMF_2018'})
WHERE c.baseline CONTAINS sys.categorization
MERGE (sys)-[:SYSTEM_IMPLEMENTS_CONTROLS {implementation_status: 'Required'}]->(c);
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
logger.info('Framework')

client.query(steps.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/nist_rmf_steps.csv'))
time.sleep(2)
logger.info('Steps')

client.query(control_families.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/nist_control_families.csv'))
time.sleep(2)
logger.info('Control Families')

client.query(controls.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/nist_security_contorls.csv'))
time.sleep(2)
logger.info('Controls')

client.query(roles.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/nist_rmf_roles.csv'))
time.sleep(2)
logger.info('Roles')

logger.info("Creating relationships...")
client.query(framework_standard_step_rel)
time.sleep(2)

client.query(framework_standard_control_family_rel)
time.sleep(2)

client.query(step_step_rel)
time.sleep(2)

client.query(control_family_control_rel)
time.sleep(2)

client.query(role_step_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

output_filename = "nist_rmf.json"

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
