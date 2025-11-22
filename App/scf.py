#Load Framework
framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {name: row.name, version: row.version})
ON CREATE SET
    f.release_date = date(row.release_date),
    f.control_count = toInteger(row.control_count),
    f.url = row.url,
    f.status = row.status,
    f.created_at = datetime();
"""
#Load Domain 
domain ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.name,
    d.description = row.description;
"""

#Load Controls
controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id})
ON CREATE SET 
    c.control_name = row.control_name,
    c.control_text = row.control_text,
    c.domain_identifier = row.domain_identifier,
    c.pptdf_scope = row.pptdf_scope,
    c.control_question = row.control_question,
    c.relative_weighting = toInteger(row.relative_weighting),
    c.nist_csf_function = row.nist_csf_function,
    c.is_new_control = row.is_new_control,
    c.is_mcr = row.is_mcr,
    c.is_dsr = row.is_dsr,
    c.control_type = row.control_type;
"""
#Load External Controls
external_controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ec:ExternalControl {
    control_id: row.control_id,
    source_framework: row.source_framework,
    source_framework_version: row.source_framework_version
})
ON CREATE SET 
    ec.control_name = row.control_name,
    ec.control_text = row.control_text,
    ec.source_framework_full_name = row.source_framework_full_name,
    ec.control_type = row.control_type;
"""     

#Create Framework→Domain Relationships
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {name: row.framework_name, version: row.framework_version})
MATCH (d:Domain {identifier: row.domain_identifier})
MERGE (f)-[r:CONTAINS_DOMAIN]->(d);
"""
#Create Domain -> controls Relationships
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (d:Domain {identifier: row.domain_identifier})
MATCH (c:Control {control_id: row.control_id})
MERGE (d)-[r:CONTAINS_CONTROL]->(c);
"""
#Create CONTROL MAPS_TO EXTERNALCONTROL
control_external_control="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {control_id: row.scf_control_id})
MATCH (ec:ExternalControl {
    control_id: row.external_control_id,
    source_framework: row.external_framework,
    source_framework_version: row.external_framework_version
})
MERGE (c)-[r:MAPS_TO]->(ec)
ON CREATE SET 
    r.relationship_type = row.relationship_type,
    r.strength = row.strength,
    r.justification = row.justification,
    r.date_established = date(row.date_established),
    r.notes = row.notes,
    r.scf_control_name = row.scf_control_name,
    r.scf_domain = row.scf_domain,
    r.external_framework_full_name = row.external_framework_full_name;
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


client.query(framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_framework_simplified.csv"))
time.sleep(2)

client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_domains_simplified.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_controls_simplified.csv"))
time.sleep(2)

client.query(external_controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_external_controls_simplified.csv"))
time.sleep(2)

client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_framework_domain_relationships.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_domain_control_relationships.csv"))
time.sleep(2)


client.query(control_external_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF_New/neo4j_maps_to_relationships.csv"))
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
with open('scf.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(res, default=str))

client.close()
