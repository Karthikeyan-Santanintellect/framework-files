# ISO/IEC 27701 — Privacy Information Management System (PIMS)
# Loader for the ISO 27701 node/relationship CSVs into the Neo4j Aura instance.
#
# Source CSVs (branch: gautham, folder "ISO 27701/"):
#   Clauses.csv                    clause_id, clause_name, category_id
#   Annex.csv                      annex_id, title, type
#   Control Objective.csv          objective_id, title, description
#   Controls.csv                   control_id, objective_id, title, control_text
#   Implementation Guidance.csv    guidance_id, control_id, text
#   Actors.csv                     node_id, node_label, name, description
#   Assets & Data.csv              node_id, node_label, name, description
#   Logic Controls &Enforcement.csv node_id, node_label, name, description

BASE = "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/ISO%2027701"

FW_ID = "ISO27701_2025"

# ---------- NODES ----------

framework_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    f.name = 'ISO/IEC 27701:2025',
    f.full_name = 'Security techniques - Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management - Requirements and guidelines',
    f.version = '2025',
    f.status = 'Active',
    f.description = 'Privacy Information Management System (PIMS): requirements and guidance for establishing, implementing, maintaining and continually improving a PIMS as an extension to ISO/IEC 27001 and ISO/IEC 27002.';
"""

clauses = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Clause {clause_id: row.clause_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    c.name = row.clause_name,
    c.category_id = row.category_id;
"""

annexes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Annex {annex_id: row.annex_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    a.title = row.title,
    a.type = row.type;
"""

control_objectives = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:ControlObjective {objective_id: row.objective_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    o.title = row.title,
    o.description = row.description;
"""

controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {control_id: row.control_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    ctrl.objective_id = row.objective_id,
    ctrl.title = row.title,
    ctrl.control_text = row.control_text;
"""

guidance = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (g:Guideline {guideline_id: row.guidance_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    g.control_id = row.control_id,
    g.text = row.text;
"""

# Actors / Assets / Logic-and-enforcement nodes carry their intended semantic name
# in node_label; keep it as a property (a fixed structural label is used so the
# graph stays queryable without APOC dynamic labels).
actors = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Actor {node_id: row.node_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    a.node_label = row.node_label,
    a.name = row.name,
    a.description = row.description;
"""

assets = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Asset {node_id: row.node_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    d.node_label = row.node_label,
    d.name = row.name,
    d.description = row.description;
"""

logic_controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (l:LogicControl {node_id: row.node_id, IS_frameworks_standard_id: 'ISO27701_2025'})
ON CREATE SET
    l.node_label = row.node_label,
    l.name = row.name,
    l.description = row.description;
"""

# ---------- RELATIONSHIPS ----------

# Clear this framework's relationships before rebuilding (idempotent re-runs).
clear_relationships = """
MATCH (a {IS_frameworks_standard_id: 'ISO27701_2025'})-[r]-(b {IS_frameworks_standard_id: 'ISO27701_2025'})
DELETE r;
"""

framework_clauses = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (c:Clause {IS_frameworks_standard_id: 'ISO27701_2025'})
MERGE (f)-[:FRAMEWORK_CONTAINS_CLAUSES]->(c);
"""

# Clause hierarchy: a sub-clause carries category_id = its top-level clause number.
clause_hierarchy = """
MATCH (parent:Clause {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (child:Clause {IS_frameworks_standard_id: 'ISO27701_2025'})
WHERE child.category_id = parent.clause_id AND child.clause_id <> parent.clause_id
MERGE (parent)-[:CLAUSE_HAS_SUBCLAUSE]->(child);
"""

framework_annexes = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (a:Annex {IS_frameworks_standard_id: 'ISO27701_2025'})
MERGE (f)-[:FRAMEWORK_CONTAINS_ANNEX]->(a);
"""

# Annex A holds the PIMS control objectives (objective ids look like OBJ-A.1.2).
annex_objectives = """
MATCH (a:Annex {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (o:ControlObjective {IS_frameworks_standard_id: 'ISO27701_2025'})
WHERE o.objective_id STARTS WITH 'OBJ-' + a.annex_id + '.'
MERGE (a)-[:ANNEX_CONTAINS_OBJECTIVE]->(o);
"""

# Each control names the objective it fulfils.
objective_controls = """
MATCH (o:ControlObjective {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27701_2025'})
WHERE ctrl.objective_id = o.objective_id
MERGE (o)-[:OBJECTIVE_HAS_CONTROL]->(ctrl);
"""

# Each implementation-guidance item names the control it elaborates.
control_guidance = """
MATCH (ctrl:Control {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (g:Guideline {IS_frameworks_standard_id: 'ISO27701_2025'})
WHERE g.control_id = ctrl.control_id
MERGE (ctrl)-[:CONTROL_HAS_GUIDELINE]->(g);
"""

# Annex B is the implementation guidance annex (guidance ids look like B.1.2.2).
annex_guidance = """
MATCH (a:Annex {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (g:Guideline {IS_frameworks_standard_id: 'ISO27701_2025'})
WHERE g.guideline_id STARTS WITH a.annex_id + '.'
MERGE (a)-[:ANNEX_CONTAINS_GUIDELINE]->(g);
"""

framework_actors = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (a:Actor {IS_frameworks_standard_id: 'ISO27701_2025'})
MERGE (f)-[:FRAMEWORK_CONTAINS_ACTOR]->(a);
"""

framework_assets = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (d:Asset {IS_frameworks_standard_id: 'ISO27701_2025'})
MERGE (f)-[:FRAMEWORK_CONTAINS_ASSET]->(d);
"""

framework_logic = """
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: 'ISO27701_2025'})
MATCH (l:LogicControl {IS_frameworks_standard_id: 'ISO27701_2025'})
MERGE (f)-[:FRAMEWORK_CONTAINS_LOGIC_CONTROL]->(l);
"""


import os
import time
import logging
import json
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading ISO 27701 graph structure...")

client.query(framework_standard)
time.sleep(2)

client.query(clauses.replace('$file_path', BASE + "/ISO%2027701%20-%20Clauses.csv"))
time.sleep(2)

client.query(annexes.replace('$file_path', BASE + "/ISO%2027701%20-%20Annex.csv"))
time.sleep(2)

client.query(control_objectives.replace('$file_path', BASE + "/ISO%2027701%20-%20Control%20Objective.csv"))
time.sleep(2)

client.query(controls.replace('$file_path', BASE + "/ISO%2027701%20-%20Controls.csv"))
time.sleep(2)

client.query(guidance.replace('$file_path', BASE + "/ISO%2027701%20-%20Implementation%20Guidance.csv"))
time.sleep(2)

client.query(actors.replace('$file_path', BASE + "/ISO%2027701%20-%20Actors.csv"))
time.sleep(2)

client.query(assets.replace('$file_path', BASE + "/ISO%2027701%20-%20Assets%20%26%20Data.csv"))
time.sleep(2)

client.query(logic_controls.replace('$file_path', BASE + "/ISO%2027701%20-%20Logic%20Controls%20%26Enforcement.csv"))
time.sleep(2)

logger.info("Creating relationships...")

client.query(clear_relationships)
time.sleep(2)

client.query(framework_clauses)
time.sleep(2)

client.query(clause_hierarchy)
time.sleep(2)

client.query(framework_annexes)
time.sleep(2)

client.query(annex_objectives)
time.sleep(2)

client.query(objective_controls)
time.sleep(2)

client.query(control_guidance)
time.sleep(2)

client.query(annex_guidance)
time.sleep(2)

client.query(framework_actors)
time.sleep(2)

client.query(framework_assets)
time.sleep(2)

client.query(framework_logic)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH (n {IS_frameworks_standard_id: 'ISO27701_2025'})
OPTIONAL MATCH (n)-[r]-(m {IS_frameworks_standard_id: 'ISO27701_2025'})
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

with open('iso-27701.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info(f"✓ Exported {len(res['nodes'])} nodes and {len(res['rels'])} relationships to iso-27701.json")

client.close()
