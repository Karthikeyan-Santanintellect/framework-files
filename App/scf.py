# 1. Load Framework Node (Run Once)
IS_framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "SCF-2025.4"})
ON CREATE SET
    f.name = "Secure Controls Framework",
    f.full_name = "Secure Controls Framework",
    f.version = "2025.4",
    f.publication_date = date("2025-12-29"),
    f.status = "Active",
    f.url = "https://securecontrolsframework.com/",
    f.description = "A comprehensive cybersecurity and data privacy control framework organized into multiple domains.";
"""

# 2. Load Domains
domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (scd:SCFDomain {identifier: row.identifier, IS_frameworks_standard_id: "SCF-2025.4"})
ON CREATE SET 
    scd.name = row.name,
    scd.description = row.description;
"""

# 3. Load Controls
SCF_controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sc:SCFControl {id: row.control_id, IS_frameworks_standard_id: "SCF-2025.4"})
ON CREATE SET 
    sc.name = row.control_name,
    sc.description = row.control_text,
    sc.question = row.control_question,
    sc.scope = row.pptdf_scope,
    sc.weighting = toInteger(row.relative_weighting),
    sc.nist_function = row.nist_csf_function,
    sc.type = row.control_type;
"""

# 4. Framework -> Domain Relationship 
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "SCF-2025.4"})
MATCH (scd:SCFDomain {identifier: row.domain_identifier, IS_frameworks_standard_id: "SCF-2025.4"})
MERGE (f)-[:IS_FRAMEWORKS_STANDARD_CONTAINS_DOMAIN]->(scd);
"""

# 5. Domain -> Control Relationship 
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (scd:SCFDomain {identifier: row.domain_identifier, IS_frameworks_standard_id: "SCF-2025.4"})
MATCH (sc:SCFControl {id: row.control_id, IS_frameworks_standard_id: "SCF-2025.4"})
MERGE (scd)-[:SCF_DOMAIN_CONTAINS_CONTROL]->(sc);
"""

# Control -> NIST CSF 
control_nist_csf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (nist)
    WHERE nist.id = row.nist_csf_id 
      AND nist.IS_frameworks_standard_id = 'NIST_CSF_2.0'
      AND (nist:Category OR nist:Subcategory OR nist:Function)
    MERGE (sc)-[:SCF_CONTROL_MAPS_NIST_CSF]->(nist)
} IN TRANSACTIONS OF 500 ROWS;
"""
# Control -> CIS Controls 8.1
control_cis = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (cis:Control {control_id: row.cis_control_id})
    WHERE cis.IS_frameworks_standard_id = 'CIS CONTROLS 8.1'
    MERGE (sc)-[:SCF_CONTROL_MAPS_CIS]->(cis)
} IN TRANSACTIONS OF 500 ROWS;
"""



# Control -> ISO 27001:2022
control_iso_27001 ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (iso1:Control {control_id: row.iso_control_id})
    WHERE iso1.IS_frameworks_standard_id = 'ISO27001_2022'
    MERGE (sc)-[:SCF_CONTROL_MAPS_ISO27001]->(iso1)
    } IN TRANSACTIONS OF 500 ROWS;
"""

#Control -> ISO 27002:2022
control_iso_27002 ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (iso2:Control {control_id: row.iso_control_id})
    WHERE iso2.IS_frameworks_standard_id = 'ISO27002_2022'
    MERGE (sc)-[:SCF_CONTROL_MAPS_ISO27002]->(iso2)
    } IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> NIST PMF 1.0
control_nist_pmf_1_0 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (pmf:Subcategory {subcategory_id: row.nist_pmf_1_0_id})
    WHERE pmf.IS_frameworks_standard_id = 'NIST_PMF_1.0'
    MERGE (sc)-[:SCF_CONTROL_MAPS_NIST_PMF_1]->(pmf)
    } IN TRANSACTIONS OF 500 ROWS;
"""

# 8a. Control -> NIST AI RMF #
control_nist_ai_rmf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (airmf)
    WHERE airmf.IS_frameworks_standard_id = 'NIST_AI_RMF_1.0'
      AND airmf:Function OR airmf:Category OR airmf:Subcategory
    MERGE (sc)-[:SCF_CONTROL_MAPS_NIST_AI_RMF]->(airmf)
} IN TRANSACTIONS OF 500 ROWS;
"""



# 9a. Control -> GLBA 
control_glba = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (glba:Section {section_id: row.glba_section_id})
    WHERE glba.industry_standard_regulation_id = 'GLBA 1999'
    MERGE (sc)-[:SCF_CONTROL_MAPS_GLBA]->(glba)
} IN TRANSACTIONS OF 500 ROWS;
"""
# 11a. Control -> NERC CIP 
control_nerc_cip = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (nerc:Requirement {requirement_id: row.nerc_cip_requirement_id})
    WHERE nerc.industry_standard_regulation_id = 'NERC_CIP'
    MERGE (sc)-[:SCF_CONTROL_MAPS_NERC_CIP]->(nerc)
} IN TRANSACTIONS OF 500 ROWS;
"""

# 13a. Control -> PCI DSS 
control_pci_dss = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (pci:Requirement {node_id: row.pci_dss_node_id})
    WHERE pci.industry_standard_regulation_id = 'PCI-DSS 4.0'
    MERGE (sc)-[:SCF_CONTROL_MAPS_PCI_DSS]->(pci)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> TISAX 
control_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (tisax:Requirement {requirement_id: row.tisax_reference_id})
    WHERE tisax.industry_standard_regulation_id = 'TISAX 6.0'
    MERGE (sc)-[:SCF_CONTROL_MAPS_TISAX]->(tisax)
} IN TRANSACTIONS OF 500 ROWS;
"""
# 17a. Control -> CPA 
control_cpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (cpa:Section {section_id: row.cpa_section_id})
    WHERE cpa.regional_standard_regulation_id = 'CPA 1.0'
    MERGE (sc)-[:SCF_CONTROL_MAPS_CPA]->(cpa)
} IN TRANSACTIONS OF 500 ROWS;
"""

# 18a. Control -> DORA 
control_dora = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (dora:Article {id: row.dora_article_id})
    WHERE dora.regional_standard_regulation_id = 'DORA 2022/2554'
    MERGE (sc)-[:SCF_CONTROL_MAPS_DORA]->(dora)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> DPDPA 
control_dpdpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (dpdpa:Section {section_id: row.dpdpa_section_id})
    WHERE dpdpa.regional_standard_regulation_id = 'DPDPA 1.0' 
    MERGE (sc)-[:SCF_CONTROL_MAPS_DPDPA]->(dpdpa)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> GDPR 
control_gdpr = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (gdpr:Article {Node_ID: row.gdpr_article_id})
    WHERE gdpr.regional_standard_regulation_id = 'GDPR 2016/679'
    MERGE (sc)-[:SCF_CONTROL_MAPS_GDPR]->(gdpr)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> NY SHIELD 
control_ny_shield = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (nys:Section {section_id: row.section_id})
    WHERE nys.regional_standard_regulation_id = 'NY SHIELD 1.0'
    MERGE (sc)-[:SCF_CONTROL_MAPS_NY_SHIELD]->(nys)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> NIS 2 #
control_nis2 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL {
    WITH row
    MATCH (sc:SCFControl {id: row.scf_control_id})
    MATCH (nis2:Article {id: row.nis2_article_id})
    WHERE nis2.regional_standard_regulation_id = 'NIS2-EU-2022-2555'
    MERGE (sc)-[:SCF_CONTROL_MAPS_NIS2]->(nis2)
} IN TRANSACTIONS OF 500 ROWS;
"""

# Control -> HIPAA #
control_hipaa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {id: row.scf_control_id})
MATCH (std:Standard {id: row.hipaa_standard_id})
WHERE std.industry_standard_regulation_id = 'HIPAA 1996'
MERGE (sc)-[:SCF_CONTROL_MAPS_HIPAA]->(std);
"""


import os
from pydoc import cli
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

client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Domains.csv"))
time.sleep(2)

client.query(SCF_controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls.csv"))
time.sleep(2)


# Relationships
client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Framework%20Domain.csv"))
time.sleep(2)

# client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Domain%20Control.csv"))
# time.sleep(2)

# client.query(control_nist_csf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20NIST%20CSF.csv"))
# time.sleep(2)


# client.query(control_cis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20CIS%20Controls.csv"))
# time.sleep(2)

# client.query(control_iso_27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20ISO27001.csv"))
# time.sleep(2)

# client.query(control_iso_27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20ISO27002.csv"))
# time.sleep(2)


# client.query(control_nist_pmf_1_0.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20PMF%201.0.csv"))
# time.sleep(2)

# client.query(control_nist_ai_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NIST%20AI%20RMF.csv"))
# time.sleep(2)

# client.query(control_glba.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20GLBA.csv"))
# time.sleep(2)

# client.query(control_nerc_cip.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NERC_CIP.csv"))
# time.sleep(2)

# client.query(control_pci_dss.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20PCIDSS.csv"))
# time.sleep(2)

# client.query(control_tisax.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20TISAX.csv"))
# time.sleep(2)


# client.query(control_cpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20CPA.csv"))
# time.sleep(2)

# client.query(control_dora.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20DORA.csv"))
# time.sleep(2)

# client.query(control_dpdpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20DPDPA.csv"))
# time.sleep(2)

# client.query(control_gdpr.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20GDPR.csv"))
# time.sleep(2)

client.query(control_ny_shield.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NY%20SHEILD.csv"))
time.sleep(2)

# client.query(control_nis2.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NIS%202.csv"))
# time.sleep(2)

# client.query(control_hipaa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20HIPAA.csv"))
# time.sleep(2)

logger.info("Graph structure loaded successfully.")

query = """
MATCH (n)
WHERE size(labels(n)) > 0
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
    with open('scf.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to scf.json")
else:
    logger.error("No data returned from the query.")

client.close()
