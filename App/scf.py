
# Create Constraints (Fixed syntax for Neo4j 5.x)
constraint_framework = """
CREATE CONSTRAINT framework_unique IF NOT EXISTS 
FOR (f:Framework) REQUIRE (f.name, f.version) IS NODE KEY
"""

constraint_domain = """
CREATE CONSTRAINT domain_unique IF NOT EXISTS 
FOR (d:Domain) REQUIRE d.identifier IS NODE KEY
"""

constraint_control = """
CREATE CONSTRAINT control_unique IF NOT EXISTS 
FOR (c:Control) REQUIRE c.control_id IS NODE KEY
"""

constraint_ext = """
CREATE CONSTRAINT external_control_unique IF NOT EXISTS 
FOR (ec:ExternalControl) REQUIRE (ec.control_id, ec.source_framework, ec.source_framework_version) IS NODE KEY
"""

# Load Framework
framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {name: row.name, version: row.version})
ON CREATE SET
    f.release_date = date(row.release_date),
    f.control_count = toInteger(row.control_count),
    f.url = row.url,
    f.status = row.status,
    f.created_at = datetime()
"""

# Load Domain 
domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.name,
    d.description = row.description,
    d.created_at = datetime()
"""

# Load Controls
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.control_id IS NOT NULL AND trim(row.control_id) <> ''
CALL {
    WITH row
    MERGE (c:Control {control_id: trim(row.control_id)})
    ON CREATE SET 
        c.control_name = row.control_name,
        c.control_text = row.control_text,
        c.domain_identifier = trim(row.domain_identifier),
        c.pptdf_scope = row.pptdf_scope,
        c.control_question = row.control_question,
        c.relative_weighting = toInteger(row.relative_weighting),
        c.nist_csf_function = row.nist_csf_function,
        c.is_new_control = toBoolean(row.is_new_control),
        c.is_mcr = toBoolean(row.is_mcr),
        c.is_dsr = toBoolean(row.is_dsr),
        c.control_type = row.control_type,
        c.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

# Load External Controls (Added validation for composite key)
external_controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.control_id IS NOT NULL AND trim(row.control_id) <> ''
    AND row.source_framework IS NOT NULL AND trim(row.source_framework) <> ''
    AND row.source_framework_version IS NOT NULL AND trim(row.source_framework_version) <> ''
CALL {
    WITH row
    MERGE (ec:ExternalControl {
        control_id: trim(row.control_id),
        source_framework: trim(row.source_framework),
        source_framework_version: trim(row.source_framework_version)
    })
    ON CREATE SET 
        ec.control_name = row.control_name,
        ec.control_text = row.control_text,
        ec.source_framework_full_name = row.source_framework_full_name,
        ec.control_type = row.control_type,
        ec.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

# Create Framework→Domain Relationships (Added validation)
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.framework_name IS NOT NULL AND row.domain_identifier IS NOT NULL
CALL {
    WITH row
    MATCH (f:Framework {name: row.framework_name, version: row.framework_version})
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MERGE (f)-[r:CONTAINS_DOMAIN]->(d)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

# Create Domain → Controls Relationships
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.domain_identifier IS NOT NULL AND row.control_id IS NOT NULL
    AND trim(row.domain_identifier) <> '' AND trim(row.control_id) <> ''
CALL {
    WITH row
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MATCH (c:Control {control_id: trim(row.control_id)})
    MERGE (d)-[r:CONTAINS_CONTROL]->(c)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

# Create CONTROL MAPS_TO EXTERNALCONTROL (Added validation)
control_external_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.scf_control_id IS NOT NULL AND row.external_control_id IS NOT NULL
    AND trim(row.scf_control_id) <> '' AND trim(row.external_control_id) <> ''
    AND row.external_framework IS NOT NULL AND trim(row.external_framework) <> ''
    AND row.external_framework_version IS NOT NULL AND trim(row.external_framework_version) <> ''
CALL {
    WITH row
    MATCH (c:Control {control_id: trim(row.scf_control_id)})
    MATCH (ec:ExternalControl {
        control_id: trim(row.external_control_id),
        source_framework: trim(row.external_framework),
        source_framework_version: trim(row.external_framework_version)
    })
    MERGE (c)-[r:MAPS_TO_EXTERNAL_CONTROL]->(ec)
    ON CREATE SET 
        r.relationship_type = row.relationship_type,
        r.strength = row.strength,
        r.justification = row.justification,
        r.date_established = date(row.date_established),
        r.notes = row.notes,
        r.scf_control_name = row.scf_control_name,
        r.scf_domain = row.scf_domain,
        r.external_framework_full_name = row.external_framework_full_name,
        r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
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

logger.info("Loading graph structure...")


client.query(framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_framework_simplified.csv"))
time.sleep(2)

client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domains_simplified.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_controls_simplified.csv"))
time.sleep(2)

client.query(external_controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_external_controls_simplified.csv"))
time.sleep(2)

client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_framework_domain_relationships.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domain_control_relationships.csv"))
time.sleep(2)


client.query(control_external_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_maps_to_relationships.csv"))
time.sleep(2)


# Export graph data
logger.info("\nExporting graph data to scf.json...")
res = client.query("""
MATCH path = (:Framework)-[*]->()
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
    logger.error(f"✗ Export query failed: {res}")
elif res and len(res) > 0:
    graph_data = res[0].get('graph_data', res[0])
    
    # Rename MAPS_TO to MAPS_TO_EXTERNAL_CONTROL in JSON
    renamed_count = 0
    if 'links' in graph_data:
        for link in graph_data['links']:
            if link.get('type') == 'MAPS_TO':
                link['type'] = 'MAPS_TO_EXTERNAL_CONTROL'
                renamed_count += 1
        
        if renamed_count > 0:
            logger.info(f"✓ Renamed {renamed_count} MAPS_TO → MAPS_TO_EXTERNAL_CONTROL relationships")
    
    with open('scf.json', 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=2, default=str, ensure_ascii=False)
    
    node_count = len(graph_data.get('nodes', []))
    link_count = len(graph_data.get('links', []))
    logger.info(f"✓ Exported {node_count} nodes and {link_count} relationships")
    logger.info(f"✓ Graph data saved to: scf.json")
else:
    logger.warning("⚠ No data returned from export query")
client.close()