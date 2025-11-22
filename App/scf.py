#Load Framework
framework ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {framework_id : 'SCF 2025'})
ON CREATE SET
    f.name = row.name,
    f.version = row.version,
    f.release_date = date(row.release_date),
    f.control_count = toInteger(row.control_count),
    f.url = row.url,
    f.status = row.status,
    f.framework_type = 'SCF',
    f.created_at = datetime();
"""
#Load External Framework
external_framework ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework:ExternalFramework {name: row.framework_name, version: row.framework_version})
ON CREATE SET 
    f.full_name = row.framework_full_name,
    f.control_count = toInteger(row.control_count),
    f.framework_type = row.framework_type,
    f.status = row.status,
    f.created_at = datetime();
"""
#Load Domain 
domain ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.name,
    d.description = row.description,
    d.created_at = datetime();
"""

#Load Controls
controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control:SCFControl {control_id: row.control_id})
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
    c.control_type = 'SCF',
    c.created_at = datetime();
"""
#Load External Controls
external_controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control:ExternalControl {
    control_id: row.control_id,
    source_framework: row.source_framework,
    source_framework_version: row.source_framework_version
})
ON CREATE SET 
    c.control_name = row.control_name,
    c.control_text = row.control_text,
    c.source_framework_full_name = row.source_framework_full_name,
    c.control_type = 'External',
    c.created_at = datetime();
"""     

#Create Framework→Domain Relationships
framework_domain_rel ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework:SCFFramework {name: row.framework_name, version: row.framework_version})
MATCH (d:Domain {identifier: row.domain_identifier})
MERGE (f)-[r:CONTAINS_DOMAIN]->(d)
ON CREATE SET 
    r.created_at = datetime();
"""
#Create Domain→Control Relationships
domain_controls_rel="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (d:Domain {identifier: row.domain_identifier})
MATCH (c:Control:SCFControl {control_id: row.control_id})
MERGE (d)-[r:CONTAINS_CONTROL]->(c)
ON CREATE SET 
    r.created_at = datetime();
"""
#Create External Framework→Control Relationships
control_external_control_rel="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework:ExternalFramework {name: row.framework_name, version: row.framework_version})
MATCH (c:Control:ExternalControl {
    control_id: row.control_id,
    source_framework: row.framework_name,
    source_framework_version: row.framework_version
})
MERGE (f)-[r:CONTAINS_CONTROL]->(c)
ON CREATE SET 
    r.created_at = datetime();
"""
#Create Cross-Framework Mappings (STRM)
scf_external_control="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (scf:Control:SCFControl {control_id: row.scf_control_id})
MATCH (ext:Control:ExternalControl {
    control_id: row.external_control_id,
    source_framework: row.external_framework,
    source_framework_version: row.external_framework_version
})
MERGE (scf)-[r:MAPS_TO]->(ext)
ON CREATE SET 
    r.relationship_type = row.relationship_type,
    r.strength = row.strength,
    r.justification = row.justification,
    r.date_established = date(row.date_established),
    r.notes = row.notes,
    r.scf_control_name = row.scf_control_name,
    r.scf_domain = row.scf_domain,
    r.external_framework_full_name = row.external_framework_full_name,
    r.created_at = datetime();
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


client.query(framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/2_chapter_nodes.csv"))
time.sleep(2)

client.query(external_framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/3_section_nodes.csv"))
time.sleep(2)


client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/article_node.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/5_recital_nodes.csv"))
time.sleep(2)

client.query(external_controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/12_paragraph_nodes.csv"))
time.sleep(2)

client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/13_subparagraph_nodes.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/14_legislative_action_nodes.csv"))
time.sleep(2)


client.query(control_external_control_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/15_concept_nodes_CORRECTED.csv"))
time.sleep(2)

client.query(scf_external_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/1_framework_nodes_CORRECTED.csv"))
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
