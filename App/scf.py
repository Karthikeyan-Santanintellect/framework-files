# Load Framework
IS_framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {IS_frameworks_standard_id: "SCF-2025.4"})
ON CREATE SET
    f.name = "Secure Controls Framework",
    f.full_name = "Secure Controls Framework",
    f.version = "2025.4",
    f.publication_date = date("2025-12-29"),
    f.status = "Active",
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
    d.description = row.description;
"""
# Load Controls
SCF_controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:SCFControl {id: row.control_id})
ON CREATE SET 
    c.name = row.control_name,
    c.description = row.control_text,
    c.question = row.control_question,
    c.scope = row.pptdf_scope,
    c.weighting = row.relative_weighting,
    c.nist_function = row.nist_csf_function,
    c.type = row.control_type;
"""

# Create Framework→Domain Relationships
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {name: row.framework_name, version: row.framework_version})
WITH f, row
MATCH (d:Domain {id: row.domain_identifier})
MERGE (f)-[:SCF_HAS_DOMAIN]->(d);
"""


# Create Domain → Controls Relationships
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (d:Domain {id: row.domain_identifier})
MATCH (c:Control {id: row.control_id})
MERGE (d)-[:DOMAIN_CONTAINS_CONTROL]->(c);
"""

#1a.control -> CSF 
control_CSF ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (csf:NISTCSF {function_id: row.nist_csf_2_0_id, IS_frameworks_standard_id: 'NIST_CSF_2.0'})
MERGE (sc)-[:CONTROL_MAPS_CSF]->(csf);
"""

# Control -> CIS 
control_cis = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (cis:CISControl {control_id: trim(row.cis_control_id), IS_frameworks_standard_id: 'CIS CONTROLS 8.1'})
MERGE (sc)-[:CONTROL_MAPS_CIS]->(cis);
"""
#3a.control->iso_27001
control_iso27001= """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (iso1:ISO27001 {control_id: trim(row.iso_control_id), IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (sc)-[:CONTROL_MAPS_ISO27001]->(iso1);
"""

#4a.control->iso
control_iso27002 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (iso2:ISO27002 {control_id: trim(row.iso_control_id), IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (sc)-[:CONTROL_MAPS_ISO27002]->(iso2);
"""
#5a.control->pmf_1
control_nist_pmf_1_0 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (pmf1:NISTPMF {control_id: trim(row.nist_pmf_1_0_id), IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (sc)-[:CONTROL_MAPS_NIST_PMF_1_0]->(pmf1);
"""
#6a.control->pmf_1.1
control_nist_pmf_1_1 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (pmf11:NISTPMF {control_id: trim(row.nist_pmf_id), IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MERGE (sc)-[:CONTROL_MAPS_NIST_PMF_1_1]->(pmf11);
"""
#7a.control->NIST_RMF
control_nist_rmf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (rmf:NISTRMF {control_id: trim(row.nist_rmf_control_id), IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (sc)-[:CONTROL_MAPS_NIST_RMF]->(rmf);
"""
#8c.control->nist_ai_rmf
control_nist_ai_rmf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (airmf:NISTAIRMF {control_id: trim(row.nist_ai_rmf_id), IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MERGE (sc)-[:CONTROL_MAPS_NIST_AI_RMF]->(airmf);
"""
#9a.controls->GLBA
control_glba = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (glba:GLBA {control_id: trim(row.glba_section_id), IS_frameworks_standard_id: 'GLBA 1999'})
MERGE (sc)-[:CONTROL_MAPS_GLBA]->(glba);
"""

#10a.control->Hippa
control_hipaa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (hipaa:HIPAA {standard_id: trim(row.hipaa_standard_id), IS_frameworks_standard_id: 'HIPAA 1996'})
MERGE (sc)-[:CONTROL_MAPS_HIPAA]->(hipaa);
"""

#11a.control-> Nerc_CIP
control_nerc_cip = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (nerc:NERCCIP {requirement_id: trim(row.nerc_cip_requirement_id), IS_frameworks_standard_id: 'NERC_CIP'})
MERGE (sc)-[:CONTROL_MAPS_NERC_CIP]->(nerc);
"""

#13a.control-> PCIDSS
control_pci_dss = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (pci:PCIDSS{control_id: trim(row.pci_dss_node_id), IS_frameworks_standard_id: 'PCI-DSS 4.0'})
MERGE (sc)-[:CONTROL_MAPS_PCI_DSS]->(pci);
"""
#control->TISAX
control_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (tisax:TISAX {control_id: trim(row.tisax_reference_id), IS_frameworks_standard_id: 'TISAX 6.0'})
MERGE (sc)-[:CONTROL_MAPS_TISAX]->(tisax);
"""
#16a.control->cpra_sections
control_cpra_sections = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.CPRA_Section IS NOT NULL AND trim(row.CPRA_Section) <> ''
MATCH (scf:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (section:Section {
    section_id: trim(row.CPRA_Section),
    regional_standard_regulation_id: 'CPRA 2.0'
})
MERGE (scf)-[:HAS_EXTERNAL_CONTROLS]->(section)
RETURN count(*) AS relationships_created;
"""
#17a.control->dpdpa_sections
control_dpdpa_sections = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.dpdpa_section_id IS NOT NULL AND trim(row.dpdpa_section_id) <> ''
MATCH (scf:SCFControl {control_id: trim(row.scf_control_code)})
MATCH (sec:Section {
    section_id: trim(row.dpdpa_section_id),
    regional_standard_regulation_id: 'DPDPA 1.0'
})
MERGE (scf)-[:HAS_EXTERNAL_CONTROLS]->(sec)
RETURN count(*) AS relationships_created;
"""
#18a.control->gdpr_articles
control_gdpr_articles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (scf:SCFControl {control_id: row.scf_control_code})
MATCH (art:Article {
    Node_ID: row.gdpr_article_id,
    regional_standard_regulation_id: 'GDPR 2016/679'
})
MERGE (scf)-[:HAS_EXTERNAL_CONTROLS]->(art);
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

client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Framework%20Domain.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Domain%20Control.csv"))
time.sleep(2)

client.query(control_CSF_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_CSF_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_CSF_subcategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
time.sleep(2)

client.query(control_cis_controls_id.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-CIS-Controls-Mapping.csv"))
time.sleep(2)

client.query(control_cis_controls_name.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-CIS-Controls-Mapping.csv"))
time.sleep(2)

client.query(control_iso_27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27001-Mapping.csv"))
time.sleep(2)

client.query(control_iso_27001_clause.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27001-Mapping.csv"))
time.sleep(2)

client.query(control_iso_27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27002-Mapping.csv"))
time.sleep(2)

client.query(control_iso_27002_clause.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27002-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1_1_functions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1_1_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
time.sleep(2)

client.query(control_pmf_1_1_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
time.sleep(2)

client.query(control_nist_rmf_step.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_RMF-Mapping.csv"))
time.sleep(2)

client.query(control_nist_ai_rmf_functions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
time.sleep(2)

client.query(control_nist_ai_rmf_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
time.sleep(2)

client.query(control_nist_ai_rmf_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
time.sleep(2)


client.query(control_glba_sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-GLBA-Mapping.csv"))
time.sleep(2)

client.query(control_glba_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-GLBA-Mapping.csv"))
time.sleep(2)

client.query(control_hipaa_rules.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HIPAA-Mapping.csv"))
time.sleep(2)

client.query(control_hipaa_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HIPAA-Mapping.csv"))
time.sleep(2)

client.query(control_hitech_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HITECH-Mapping.csv"))
time.sleep(2)

client.query(control_hitrust.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HITRUST-Mapping.csv"))
time.sleep(2)

client.query(control_pcidss_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)


client.query(control_pcidss_sub_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)

client.query(control_nerc_cip.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NERC-CIP-Mapping.csv"))
time.sleep(2)

client.query(control_tisax.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-TISAX-Mapping.csv"))
time.sleep(2)


client.query(control_cpra_sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-CPRA-Mapping.csv"))
time.sleep(2)

client.query(control_dpdpa_sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-DPDPA-Mapping.csv"))
time.sleep(2)

client.query(control_gdpr_articles.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-GDPR-Mapping-Complete.csv"))
time.sleep(2)





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