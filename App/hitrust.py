# Create HITRUST Standard Node
standard = """
MERGE (s:Standard {standard_id: 'HITRUST'})
ON CREATE SET
    s.standard_name = "Health Information Trust Alliance",
    s.version = "11.6.0",
    s.publication_date = date("2025-08-22"),
    s.type = "Industrial",
    s.description = "It integrates multiple standards, such as HIPAA, ISO, and PCI, into a single, comprehensive framework to safeguard sensitive data";
"""

# Load HITRUST Category
hitrust_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {standard_id: 'HITRUST', category_id: row.id})
ON CREATE SET
    c.number = toInteger(row.number),
    c.name = row.name,
    c.description = row.description;
"""
# Load HITRUST Control
hitrust_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {standard_id: 'HITRUST', control_id: row.id})
ON CREATE SET
    ctrl.name = row.name,
    ctrl.category_id = row.category_id,
    ctrl.description = row.description;
"""
# Load HITRUST Control_objective
hitrust_control_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:ControlObjective {standard_id: 'HITRUST', objective_id: row.id})
ON CREATE SET
    co.control_id = row.control_id,
    co.description = row.text;
"""
# Load HITRUST Control_specification
hitrust_control_specification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:ControlSpecification {standard_id: 'HITRUST', specification_id: row.id})
ON CREATE SET
    cs.control_id = row.control_id,
    cs.description = row.text;
"""

# Create CONTAINS relationships (standard -> category)
hitrust_standard_category_rel = """
MATCH (s:Standard {standard_id: 'HITRUST'})
MATCH (c:Category {standard_id: 'HITRUST'})
MERGE (s)-[:CONTAINS]->(c);
"""

#  Create HAS_CONTROL relationships (Category -> Control)
hitrust_category_control = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Category {standard_id: 'HITRUST', category_id: row.start_id})
MATCH (ctrl:Control {standard_id: 'HITRUST', control_id: row.end_id})
MERGE (c)-[:HAS_CONTROL]->(ctrl);
"""
# Create HAS_OBJECTIVE relationships (Control -> ControlObjective)
hitrust_control_ControlObjective = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {standard_id: 'HITRUST', control_id: row.start_id})
MATCH (co:ControlObjective {standard_id: 'HITRUST', objective_id: row.end_id})
MERGE (ctrl)-[:HAS_OBJECTIVE]->(co);
"""
# Create HAS_SPECIFICATION relationships (Controlobjective -> ControlSpecification)
hitrust_ControlObjective_specification = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:ControlObjective {standard_id: 'HITRUST', objective_id: row.start_id})
MATCH (cs:ControlSpecification {standard_id: 'HITRUST', specification_id: row.end_id})
MERGE (co)-[:HAS_SPECIFICATION]->(cs);
"""
# Create MAPS_TO relationships (Controls -> CSF Subcategories)
hitrust_controls_maps_nist_CSF = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {standard_id: 'HITRUST', control_id: row.start_id})
MATCH (sc:Subcategory {framework_id: 'NIST_CSF_2.0',subcategory_id: row.end_id})
MERGE (ctrl)-[:MAPS_TO]->(sc);
"""

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

client.query(standard)
time.sleep(2)

client.query(hitrust_category.replace('$file_path',
                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Category.csv"))
time.sleep(2)

client.query(hitrust_control.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Control.csv"))
time.sleep(2)

client.query(hitrust_control_objective.replace('$file_path',
                                               "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlObjective.csv"))
time.sleep(2)

client.query(hitrust_control_specification.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlSpecification.csv"))
time.sleep(2)

client.query(hitrust_standard_category_rel)
time.sleep(2)

client.query(hitrust_category_control.replace('$file_path',
                                              "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_CONTROL.csv"))
time.sleep(2)

client.query(hitrust_control_ControlObjective.replace('$file_path',
                                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_OBJECTIVE.csv"))
time.sleep(2)

client.query(hitrust_ControlObjective_specification.replace('$file_path',
                                                            "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_SPECIFICATION.csv"))
time.sleep(2)

client.query(hitrust_controls_maps_nist_CSF.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

logger.info("Graph structure loaded successfully.")

res=client.query("""MATCH path = (:Standard)-[*]->()
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
with open('hitrust.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(res, default=str))

client.close()
