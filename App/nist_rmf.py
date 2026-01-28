# nist_rmf.py

# UPDATED: Constraints are now composite to ensure uniqueness within a framework.
constraints = """
CREATE CONSTRAINT rmf_framework_id_unique IF NOT EXISTS FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_frameworks_standard_id IS UNIQUE;
CREATE CONSTRAINT rmf_step_id_unique IF NOT EXISTS FOR (s:Step) REQUIRE (s.IS_frameworks_standard_id, s.step_id) IS UNIQUE;
CREATE CONSTRAINT rmf_family_id_unique IF NOT EXISTS FOR (cf:ControlFamily) REQUIRE (cf.IS_frameworks_standard_id, cf.family_id) IS UNIQUE;
CREATE CONSTRAINT rmf_control_id_unique IF NOT EXISTS FOR (c:Control) REQUIRE (c.IS_frameworks_standard_id, c.control_id) IS UNIQUE;
CREATE CONSTRAINT rmf_role_id_unique IF NOT EXISTS FOR (r:Role) REQUIRE (r.IS_frameworks_standard_id, r.role_id) IS UNIQUE;
CREATE CONSTRAINT rmf_system_id_unique IF NOT EXISTS FOR (sys:System) REQUIRE (sys.IS_frameworks_standard_id, sys.system_id) IS UNIQUE;
"""

indexes = """
CREATE INDEX rmf_step_number_index IF NOT EXISTS FOR (s:Step) ON (s.step_number);
CREATE INDEX rmf_system_categorization_index IF NOT EXISTS FOR (sys:System) ON (sys.categorization);
CREATE INDEX rmf_authorization_status_index IF NOT EXISTS FOR (sys:System) ON (sys.authorization_status);
CREATE INDEX rmf_control_category_index IF NOT EXISTS FOR (cf:ControlFamily) ON (cf.control_category);
"""

# UPDATED: Using MERGE to prevent duplicates.
framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
ON CREATE SET
    f.name = 'NIST Risk Management Framework',
    f.version = '5.2',
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
MERGE (s:Step {IS_frameworks_standard_id: 'NIST_RMF_5.2', step_id: row.step_id})
ON CREATE SET
    s.name = row.step_name,
    s.description = row.step_description;
"""

# UPDATED: Using MERGE and adding framework_id.
control_families = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:ControlFamily {IS_frameworks_standard_id: 'NIST_RMF_5.2', family_id: row.family_id})
ON CREATE SET
    cf.name = row.family_name,
    cf.description = row.family_description,
    cf.nist_publication = 'NIST SP 800-53 Rev 5';
"""

# UPDATED: Using MERGE and adding framework_id.
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {IS_frameworks_standard_id: 'NIST_RMF_5.2', control_id: row.control_id})
ON CREATE SET
    c.family_id = row.family_id,
    c.name = row.control_name,
    c.description = row.control_text;
"""

# UPDATED: Using MERGE and adding framework_id.
roles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Role {IS_frameworks_standard_id: 'NIST_RMF_5.2', role_id: row.role_id})
ON CREATE SET
    r.name = row.role_name,
    r.description = row.role_description;
"""

# UPDATED: Using MERGE and adding framework_id.
systems = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System {IS_frameworks_standard_id: 'NIST_RMF_5.2', system_id: row.system_id})
ON CREATE SET
    sys.name = row.system_name,
    sys.type = row.system_type,
    sys.categorization = row.categorization,
    sys.authorization_status = row.authorization_status,
    sys.ato_date = row.ato_date,
    sys.ato_expiration = row.ato_expiration;
"""

# UPDATED: Scoped MATCH to framework_id.
framework_standard_step_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MATCH (s:Step {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (f)-[:FRAMEWORK_CONTAINS_STEP]->(s);
"""

# UPDATED: Scoped MATCH and changed CREATE to MERGE.
framework_standard_control_family_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MATCH (cf:ControlFamily {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (f)-[:FRAMEWORK_REFERENCES_CONTROL_FAMILY]->(cf);
"""

# UPDATED: Scoped MATCH to framework_id.
control_family_control_rel = """
MATCH (cf:ControlFamily {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
WITH cf
MATCH (c:Control {IS_frameworks_standard_id: 'NIST_RMF_5.2', family_id: cf.family_id})
MERGE (cf)-[:CONTROL_FAMILY_INCLUDES_CONTROL]->(c);
"""

# UPDATED: Scoped MATCH to framework_id.
role_step_rel = """
MATCH (r:Role {IS_frameworks_standard_id: 'NIST_RMF_5.2', role_id: 'AO'})
MATCH (s:Step {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
WHERE s.step_id IN ['step_2', 'step_3', 'step_6', 'step_7']
MERGE (r)-[:ROLE_INVOLVED_IN_STEP {involvement_type: 'Decision_Making'}]->(s);
"""

# UPDATED: Scoped MATCH and changed CREATE to MERGE.
control_system_rel = """
MATCH (c:Control {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MATCH (sys:System {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (c)-[:CONTROL_USES_SYSTEM]->(sys);
"""

# Framework -> Roles
framework_roles_rel = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MATCH (r:Role {IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (f)-[:FRAMEWORK_DEFINES_ROLE]->(r)
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

client.query(steps.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/NIST%20RMF%20-%20Steps.csv"))
time.sleep(2)
logger.info('Steps')

client.query(control_families.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/NIST%20RMF%20-%20Control%20Families.csv"))
time.sleep(2)
logger.info('Control Families')

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/NIST%20RMF%20-%20Security%20Controls.csv"))
time.sleep(2)
logger.info('Controls')

client.query(roles.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/NIST%20RMF%20-%20Roles.csv"))
time.sleep(2)
logger.info('Roles')


client.query(systems.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20RMF/NIST%20RMF%20-%20systems.csv"))
time.sleep(2)
logger.info('Systems')

# Relationships
logger.info("Creating relationships...")
client.query(framework_standard_step_rel)
time.sleep(2)

client.query(framework_standard_control_family_rel)
time.sleep(2)

client.query(control_family_control_rel)
time.sleep(2)

client.query(role_step_rel)
time.sleep(2)

client.query(control_system_rel)
time.sleep(2)

client.query(framework_roles_rel)
time.sleep(2)


logger.info("Graph structure loaded successfully.")

query = """
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
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
} AS graph_data
"""

results = client.query(query)

if results and len(results) > 0:
    graph_data = results[0]['graph_data']
    
    import json
    with open('nist_rmf.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to nist_rmf.json")
else:
    logger.error("No data returned from the query.")

client.close()