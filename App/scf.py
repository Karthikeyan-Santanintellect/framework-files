
# Load Framework
IS_framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "SCF-2025.2.2"})
ON CREATE SET
    f.name = "Secure Controls Framework",
    f.full_name = "Secure Controls Framework",
    f.version = "2025.2.2",
    f.publication_date = date("2025-01-01"),
    f.status = "Active",
    f.total_controls = 1342,
    f.url = "https://securecontrolsframework.com/",
    f.description = "A comprehensive cybersecurity and data privacy control framework organized into multiple domains."
RETURN f;
"""

# Load Domain 
domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.name,
    d.description = row.description,
    d.created_at = datetime();
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
} IN TRANSACTIONS OF 500 ROWS;
"""



# Create Framework→Domain Relationships
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.domain_identifier IS NOT NULL
CALL {
    WITH row
    MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "SCF-2025.2.2"})
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MERGE (f)-[r:IS_FRAMEWORKS_AND_STANDARD_CONTAINS_DOMAIN]->(d)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS;
"""


# Create Domain → Controls Relationships
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.domain_identifier IS NOT NULL AND row.control_id IS NOT NULL
CALL {
    WITH row
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MATCH (c:Control {control_id: trim(row.control_id)})
    MERGE (d)-[r:DOMAIN_CONTAINS_CONTROL]->(c)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS;
"""


#1a.control -> CSF Function
control_CSF_function ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.NIST_CSF_Function IS NOT NULL 
  AND trim(row.NIST_CSF_Function) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:SCF_CONTROLS_MAPS_TO_EXTERNAL_CONTROLS {
    function_code: trim(row.NIST_CSF_Function),
    function_name: trim(row.NIST_CSF_Function),
    mapping_type: 'CSF_FUNCTION',
    framework: 'NIST_CSF_2.0',
    created_date: date()
}]->(m:ExternalControl {id: 'CSF_' + trim(row.NIST_CSF_Function), type: 'CSF_FUNCTION'})
RETURN count(rel) as relationships_created;
""" 
#1b.control -> CSF Categories
control_CSF_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.NIST_CSF_Category IS NOT NULL 
  AND trim(row.NIST_CSF_Category) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:SCF_CONTROLS_MAPS_TO_EXTERNAL_CONTROLS {
    category_code: trim(row.NIST_CSF_Category),
    mapping_type: 'CSF_CATEGORY',
    framework: 'NIST_CSF_2.0',
    created_date: date()
}]->(m:ExternalControl {id: 'CSF_' + trim(row.NIST_CSF_Category), type: 'CSF_CATEGORY'})
RETURN count(rel) as relationships_created;
"""
#1c.control -> CSF Subcategories
control_CSF_subcategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.NIST_CSF_Subcategory IS NOT NULL 
  AND trim(row.NIST_CSF_Subcategory) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:SCF_CONTROLS_MAPS_TO_EXTERNAL_CONTROLS {
    subcategory_code: trim(row.NIST_CSF_Subcategory),
    mapping_type: 'CSF_SUBCATEGORY',
    framework: 'NIST_CSF_2.0',
    created_date: date()
}]->(m:ExternalControl {id: 'CSF_' + trim(row.NIST_CSF_Subcategory), type: 'CSF_SUBCATEGORY'})
RETURN count(rel) as relationships_created;
"""
#2a.control -> PCIDSS - Requirements
control_pcidss_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.PCI_DSS_Requirement IS NOT NULL 
  AND trim(row.PCI_DSS_Requirement) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:SCF_CONTROLS_MAPS_TO_EXTERNAL_CONTROLS {
    requirement_code: trim(row.PCI_DSS_Requirement),
    mapping_type: 'PCI_DSS_REQUIREMENT',
    framework: 'PCI_DSS_4.0',
    created_date: date()
}]->(m:ExternalControl {id: 'PCI_' + trim(row.PCI_DSS_Requirement), type: 'PCI_REQUIREMENT'})
RETURN count(rel) as relationships_created;
"""
#2b.control -> PCIDSS - Sub_Requirements
control_pcidss_sub_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.PCI_DSS_Sub_Requirement IS NOT NULL 
  AND trim(row.PCI_DSS_Sub_Requirement) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:SCF_CONTROLS_MAPS_TO_EXTERNAL_CONTROLS {
    sub_requirement_code: trim(row.PCI_DSS_Sub_Requirement),
    mapping_type: 'PCI_DSS_SUB_REQUIREMENT',
    framework: 'PCI_DSS_4.0',
    created_date: date()
}]->(m:ExternalControl {id: 'PCI_' + trim(row.PCI_DSS_Sub_Requirement), type: 'PCI_SUB_REQUIREMENT'})
RETURN count(rel) as relationships_created;
"""
#3a.control->cis_controls_number
control_cis_controls_number = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.CIS_Control_Number IS NOT NULL 
  AND trim(row.CIS_Control_Number) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:MAPS_TO_CIS_CONTROL_NUMBER {
    cis_control_number: trim(row.CIS_Control_Number),
    cis_control_title: trim(row.CIS_Control_Title),
    mapping_type: 'CIS_CONTROL_NUMBER',
    framework: 'CIS_Controls_v8',
    created_date: date()
}]->(m:ExternalControl {id: 'CIS_' + trim(row.CIS_Control_Number), type: 'CIS_CONTROL'})
RETURN count(rel) as relationships_created;
"""
#3b.control->cis_controls_title
control_cis_controls_title = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.CIS_Control_Title IS NOT NULL 
  AND trim(row.CIS_Control_Title) <> ''
MATCH (c:Control {control_id: trim(row.SCF_Control_Code)})
CREATE (c)-[rel:MAPS_TO_CIS_CONTROL_TITLE {
    cis_control_number: trim(row.CIS_Control_Number),
    cis_control_title: trim(row.CIS_Control_Title),
    mapping_type: 'CIS_CONTROL_TITLE',
    framework: 'CIS_Controls_v8',
    created_date: date()
}]->(m:ExternalControl {id: 'CIS_TITLE_' + trim(row.CIS_Control_Title), type: 'CIS_CONTROL_TITLE'})
RETURN count(rel) as relationships_created;
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

# LOAD DATA

client.query(IS_framework_and_standard)
time.sleep(2)


client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domains_simplified.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_controls_simplified.csv"))
time.sleep(2)


client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_framework_domain_relationships.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domain_control_relationships.csv"))
time.sleep(2)


client.query(control_CSF_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_CSF_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_CSF_subcategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_pcidss_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)

client.query(control_pcidss_sub_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)

# client.query(control_hipaa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_HIPAA_Mapping.csv"))
# time.sleep(2)

# client.query(control_hitech.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_HITECH_Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_ISO27001_Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_ISO27002_Mapping.csv"))
# time.sleep(2)

# client.query(control_nerc_cip.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NERC_CIP_Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_ai_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_AI_RMF_Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_csf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_RMF_Mapping.csv"))
# time.sleep(2)

# client.query(control_pcidss.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_PCIDSS_Mapping.csv"))
# time.sleep(2)

# client.query(control_tdpsa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_TDPSA_Mapping.csv"))
# time.sleep(2)

# client.query(control_tisax.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_TISAX_Mapping.csv"))
# time.sleep(2)

# client.query(control_vcdpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_VCDPA_Mapping.csv"))
# time.sleep(2)


logger.info("Graph structure loaded successfully.")

res = client.query("""
    MATCH (n)
    WITH collect(DISTINCT n) AS allNodes
    MATCH ()-[r]-()
    WITH allNodes, collect(DISTINCT r) AS allRels
    RETURN {
      nodes: [node IN allNodes | node {
        .*,
        id: elementId(node),
        labels: labels(node),
        mainLabel: head(labels(node))
      }],
      rels: [rel IN allRels | rel {
        .*,
        id: elementId(rel),
        type: type(rel),
        from: elementId(startNode(rel)),
        to: elementId(endNode(rel))
      }]
    } AS graph_data
""")

import json

graph = None

try:
    # CASE 1: res is a list of dictionaries (Standard)
    if isinstance(res, list) and len(res) > 0 and isinstance(res[0], dict):
        graph = res[0].get("graph_data")

    # CASE 2: res is a list of strings (Needs JSON parsing)
    elif isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
        print("Detected string result, attempting to parse JSON...")
        try:
            parsed = json.loads(res[0])
            if isinstance(parsed, dict):
                graph = parsed.get("graph_data", parsed) 
        except json.JSONDecodeError:
            print("Error: Could not parse res[0] as JSON.")

    # CASE 3: res is a single dictionary
    elif isinstance(res, dict):
         graph = res.get("graph_data")

    if graph:
        with open("scf.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(graph, default=str, indent=2))
        logger.info("✓ Exported graph data to scf.json")
        
        # Print statistics
        if isinstance(graph, dict):
            num_nodes = len(graph.get("nodes", []))
            num_rels = len(graph.get("rels", []))
            logger.info(f"Graph exported: {num_nodes} nodes, {num_rels} relationships")
    else:
        logger.error("Failed to extract 'graph_data' from response.")

except Exception as e:
    logger.error(f"An error occurred during export: {e}")

client.close()