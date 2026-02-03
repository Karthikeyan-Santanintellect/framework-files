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
control_CIS = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (cis:CISControl {control_id: trim(row.cis_control_id), IS_frameworks_standard_id: 'CIS CONTROLS 8.1'})
MERGE (sc)-[:CONTROL_MAPS_CIS]->(cis);
"""
#3a.control->iso_27001
control_ISO27001= """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (iso1:ISO27001 {control_id: trim(row.iso_control_id), IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (sc)-[:CONTROL_MAPS_ISO27001]->(iso1);
"""

#4a.control->iso
control_ISO27002 = """
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
MATCH (glba:GLBA {control_id: trim(row.glba_section_id), industry_standard_regulation_id: 'GLBA 1999'})
MERGE (sc)-[:CONTROL_MAPS_GLBA]->(glba);
"""

#11a.control-> Nerc_CIP
control_nerc_cip = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (nerc:NERCCIP {requirement_id: trim(row.nerc_cip_requirement_id), industry_standard_regulation_id: 'NERC_CIP'})
MERGE (sc)-[:CONTROL_MAPS_NERC_CIP]->(nerc);
"""

#13a.control-> PCIDSS
control_pci_dss = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (pci:PCIDSS{control_id: trim(row.pci_dss_node_id), industry_standard_regulation_id: 'PCI-DSS 4.0'})
MERGE (sc)-[:CONTROL_MAPS_PCI_DSS]->(pci);
"""
#control->TISAX
control_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (tisax:TISAX {control_id: trim(row.tisax_reference_id), industry_standard_regulation_id: 'TISAX 6.0'})
MERGE (sc)-[:CONTROL_MAPS_TISAX]->(tisax);
"""
#17a.control->CPA
control_cpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (cpa:CPA {control_id: trim(row.cpa_section_id), industry_standard_regulation_id: 'CPA 1.0'})
MERGE (sc)-[:CONTROL_MAPS_CPA]->(cpa);
"""
#18a.control->DORA
control_dora = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (dora:DORA {control_id: trim(row.dora_article_id), industry_standard_regulation_id: 'DORA 2022/2554'})
MERGE (sc)-[:CONTROL_MAPS_DORA]->(dora);
"""
# control -> DPDPA
control_dpdpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (dpdpa:DPDPA {control_id: trim(row.dpdpa_section_id), industry_standard_regulation_id: 'DPDPA 1.0'})
MERGE (sc)-[:CONTROL_MAPS_DPDPA]->(dpdpa);
"""
# control -> GDPR
control_gdpr = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (gdpr:GDPR {control_id: trim(row.gdpr_article_id), industry_standard_regulation_id: 'GDPR 2016/679'})
MERGE (sc)-[:CONTROL_MAPS_GDPR]->(gdpr);
"""
# Control -> NY SHIELD
control_ny_shield= """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (ny:NYShield {control_id: trim(row.section_id), industry_standard_regulation_id: 'NY_SHIELD 1.0'})
MERGE (sc)-[:CONTROL_MAPS_NY_SHIELD]->(ny);
"""
# Control -> NIS 2
control_nis2 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sc:SCFControl {control_id: trim(row.scf_control_id)})
MATCH (nis2:NIS2Directive {control_id: trim(row.nis2_article_id), industry_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (sc)-[:CONTROL_MAPS_NIS2]->(nis2);
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

client.query(control_CSF.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20NIST%20CSF.csv"))
time.sleep(2)

client.query(control_CIS.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20CIS%20Controls.csv"))
time.sleep(2)

client.query(control_ISO27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20ISO27001.csv"))
time.sleep(2)

client.query(control_ISO27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Controls%20ISO27002.csv"))
time.sleep(2)


client.query(control_nist_pmf_1_0.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20PMF%201.0.csv"))
time.sleep(2)


client.query(control_nist_ai_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NIST%20AI%20RMF.csv"))
time.sleep(2)


client.query(control_glba.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20GLBA.csv"))
time.sleep(2)


client.query(control_nerc_cip.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NERC_CIP.csv"))
time.sleep(2)

client.query(control_pci_dss.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20PCIDSS.csv"))
time.sleep(2)

client.query(control_tisax.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20TISAX.csv"))
time.sleep(2)


client.query(control_cpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20CPA.csv"))
time.sleep(2)

client.query(control_dora.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20DORA.csv"))
time.sleep(2)

client.query(control_dpdpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20DPDPA.csv"))
time.sleep(2)

client.query(control_gdpr.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20GDPR.csv"))
time.sleep(2)

client.query(control_ny_shield.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NY%20SHEILD.csv"))
time.sleep(2)

client.query(control_nis2.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF%20Control%20NIS%202.csv"))
time.sleep(2)



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
