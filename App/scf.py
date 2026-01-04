
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
SCF_controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.control_id IS NOT NULL AND trim(row.control_id) <> ''
CALL {
    WITH row
    MERGE (sc:SCFControl {control_id: trim(row.control_id)})
    ON CREATE SET 
        sc.control_name = row.control_name,
        sc.control_text = row.control_text,
        sc.domain_identifier = trim(row.domain_identifier),
        sc.pptdf_scope = row.pptdf_scope,
        sc.control_question = row.control_question,
        sc.relative_weighting = toInteger(row.relative_weighting),
        sc.nist_csf_function = row.nist_csf_function,
        sc.is_new_control = toBoolean(row.is_new_control),
        sc.is_mcr = toBoolean(row.is_mcr),
        sc.is_dsr = toBoolean(row.is_dsr),
        sc.control_type = row.control_type,
        sc.created_at = datetime()
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
    MATCH (sc:SCFControl {control_id: trim(row.control_id)})
    MERGE (d)-[r:DOMAIN_CONTAINS_CONTROL]->(sc)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS;
"""


# #1a.control -> CSF Function
# control_CSF_function ="""
# LOAD CSV WITH HEADERS FROM '$file_path' AS row
# MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
# MATCH (fn:Function {function_id: trim(row.NIST_CSF_Function), IS_frameworks_standard_id: 'NIST_CSF_2.0'})
# MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(fn);
# """
# #1b.control -> CSF Categories
# control_CSF_category = """
# LOAD CSV WITH HEADERS FROM '$file_path' AS row
# MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
# MATCH (cat:Category {category_id: trim(row.NIST_CSF_Category), IS_frameworks_standard_id: 'NIST_CSF_2.0'})
# MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cat);
# """
# #1c.control -> CSF Subcategories
# control_CSF_subcategory = """
# LOAD CSV WITH HEADERS FROM '$file_path' AS row
# MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
# MATCH (sub:Subcategory {subcategory_id: trim(row.NIST_CSF_Subcategory), IS_frameworks_standard_id: 'NIST_CSF_2.0'})
# MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(sub);
# """

#2a.control->cis_controls_number
control_cis_controls_id = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.CIS_Control_Id IS NOT NULL 
  AND trim(row.CIS_Control_Id) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (cis:Control {control_id: trim(row.CIS_Control_Id)})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cis)
RETURN count(*) AS relationships_created;
"""
#2b.control->cis_controls_title
control_cis_controls_name = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.CIS_Control_Name IS NOT NULL 
  AND trim(row.CIS_Control_Name) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (cis:Control {name: trim(row.CIS_Control_Name)})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cis)
RETURN count(*) AS relationships_created;
"""

#3a.control->iso_27001_controls
control_iso_27001 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.ISO27001_Control IS NOT NULL 
  AND trim(row.ISO27001_Control) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (iso:Control {control_id: trim(row.ISO27001_Control), IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(iso)
RETURN count(*) AS relationships_created;
"""
#3b.control->iso_27001_clause
control_iso_27001_clause = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.ISO27001_Clause IS NOT NULL 
  AND trim(row.ISO27001_Clause) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (isoc:Clause {clause_id: trim(row.ISO27001_Clause), IS_frameworks_standard_id: 'ISO27001_2022'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(isoc)
RETURN count(*) AS relationships_created;
"""
#4a.control->iso_27002_controls
control_iso_27002 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.ISO27002_Control IS NOT NULL 
  AND trim(row.ISO27002_Control) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (iso2:Control {control_id: trim(row.ISO27002_Control), IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(iso2)
RETURN count(*) AS relationships_created;
"""
#4b.control->iso_27002_clause
control_iso_27002_clause = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.ISO27002_Clause IS NOT NULL 
  AND trim(row.ISO27002_Clause) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (iso2c:Clause {clause_id: trim(row.ISO27002_Clause), IS_frameworks_standard_id: 'ISO27002_2022'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(iso2c)
RETURN count(*) AS relationships_created;
"""
#5a.control->pmf_1_functions
control_pmf_1 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_Function IS NOT NULL 
  AND trim(row.NIST_PMF_Function) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (f:Function {function_id: trim(row.NIST_PMF_Function), IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(f);
"""
#5b.control->pmf_1_categories
control_pmf_1_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_Category IS NOT NULL 
  AND trim(row.NIST_PMF_Category) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (cat:Category {category_id: trim(row.NIST_PMF_Category), IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cat);
"""
#5c.control->pmf_1_subcategories
control_pmf_1_subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_Subcategory IS NOT NULL 
  AND trim(row.NIST_PMF_Subcategory) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (sub:Subcategory {subcategory_id: trim(row.NIST_PMF_Subcategory), IS_frameworks_standard_id: 'NIST_PMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(sub);
"""
#6a.control->pmf_1.1_functions
control_pmf_1_1_functions= """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_1_1_Function IS NOT NULL 
  AND trim(row.NIST_PMF_1_1_Function) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (f:Function {function_id: trim(row.NIST_PMF_1_1_Function), IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(f);
"""
#6b.control->pmf_1.1_categories
control_pmf_1_1_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_1_1_Category IS NOT NULL 
  AND trim(row.NIST_PMF_1_1_Category) <> '' 
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control)})
MATCH (cat:Category {category_id: trim(row.NIST_PMF_1_1_Category), IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cat);
"""
#6c.control->pmf_1.1_subcategories
control_pmf_1_1_subcategories = """ 
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_PMF_1_1_Subcategory IS NOT NULL 
  AND trim(row.NIST_PMF_1_1_Subcategory) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control)})
MATCH (sub:Subcategory {subcategory_id: trim(row.NIST_PMF_1_1_Subcategory), IS_frameworks_standard_id: 'NIST_PMF_1.1'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(sub);
"""
#7a.control->NIST_RMF_controls
control_nist_rmf_step = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row 
WHERE row.NIST_RMF_Step_ID IS NOT NULL 
  AND trim(row.NIST_RMF_Step_ID) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (step:Step {step_id: trim(row.NIST_RMF_Step_ID), IS_frameworks_standard_id: 'NIST_RMF_5.2'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(step)
RETURN count(*) AS relationships_created;
"""

#8a.control->nist_ai_rmf_functions
control_nist_ai_rmf_functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_AI_RMF_Function IS NOT NULL 
  AND trim(row.NIST_AI_RMF_Function) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (f:Function {function_id: trim(row.NIST_AI_RMF_Function), IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(f)
RETURN count(*) AS relationships_created;
"""
#8b.control->nist_ai_rmf_categories
control_nist_ai_rmf_categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_AI_RMF_Category IS NOT NULL 
  AND trim(row.NIST_AI_RMF_Category) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (cat:Category {category_id: trim(row.NIST_AI_RMF_Category), IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(cat)
RETURN count(*) AS relationships_created;
"""
#8c.control->nist_ai_rmf_subcategories
control_nist_ai_rmf_subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.NIST_AI_RMF_SubCategory IS NOT NULL 
  AND trim(row.NIST_AI_RMF_SubCategory) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (subc:Subcategory {subcategory_id: trim(row.NIST_AI_RMF_SubCategory), IS_frameworks_standard_id: 'NIST_AI_RMF_1.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(subc)
RETURN count(*) AS relationships_created;
"""
#9a.controls->GLBA_sections
control_glba_sections = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.GLBA_Section IS NOT NULL  
  AND trim(row.GLBA_Section) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (sec:Section {section_id: trim(row.GLBA_Section), industry_standard_regulation_id: 'GLBA 1999'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(sec)
RETURN count(*) AS relationships_created;
"""
#9b.controls->GLBA_requirements
control_glba_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.GLBA_Requirement_ID IS NOT NULL  
  AND trim(row.GLBA_Requirement_ID) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (req:Requirement {requirement_id: trim(row.GLBA_Requirement_ID), industry_standard_regulation_id: 'GLBA 1999'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(req)
RETURN count(*) AS relationships_created;
"""

#10a.control->hippa_rules
control_hipaa_rules = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WHERE row.HIPAA_Rule IS NOT NULL AND trim(row.HIPAA_Rule) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (std:Standard {section: trim(row.HIPAA_Rule), industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sc)-[:STANDARD_MAPS_TO_MAPPING]->(std)
RETURN count(*) AS rules_linked;
"""
#10b.control->hipaa_safeguards
control_hipaa_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WHERE row.HIPAA_Requirement_ID IS NOT NULL AND trim(row.HIPAA_Requirement_ID) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (std:Standard {id: trim(row.HIPAA_Requirement_ID), industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sc)-[:STANDARD_MAPS_TO_MAPPING]->(std)
RETURN count(*) AS safeguards_linked;
"""

#11a.control->hitech_requirements
control_hitech_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.HITECH_Requirement_ID IS NOT NULL AND trim(row.HITECH_Requirement_ID) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (req:Requirement {requirement_id: trim(row.HITECH_Requirement_ID), industry_standard_regulation_id: 'HITECH_ACT_2009'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(req)
RETURN count(*) AS hitech_requirements_linked;
"""
#12a.control->hitrust
control_hitrust = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.HITRUST_Control_ID IS NOT NULL AND trim(row.HITRUST_Control_ID) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (hc:Control {control_id: trim(row.HITRUST_Control_ID), industry_standard_regulation_id: 'HITRUST 11.6.0'})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(hc)
RETURN count(*) AS hitrust_requirements_linked;
"""


#13a.control->pcidss_requirements
control_pcidss_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.PCI_DSS_Requirement IS NOT NULL AND trim(row.PCI_DSS_Requirement) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (r:Requirement {req_id: toInteger(trim(row.PCI_DSS_Requirement))})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(r)
RETURN count(*) as SCF_Requirement_Links_Created;
"""

#13b.control->pcidss_sub_requirements = """
control_pcidss_sub_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.PCI_DSS_Sub_Requirement IS NOT NULL AND trim(row.PCI_DSS_Sub_Requirement) <> ''
MATCH (sc:SCFControl {control_id: trim(row.SCF_Control_Code)})
MATCH (sr:SubRequirement {req_id: trim(row.PCI_DSS_Sub_Requirement)})
MERGE (sc)-[:HAS_EXTERNAL_CONTROLS]->(sr)
RETURN count(*) as SCF_SubRequirement_Links_Created;
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


client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domains_simplified.csv"))
time.sleep(2)

client.query(SCF_controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_controls_simplified.csv"))
time.sleep(2)


client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_framework_domain_relationships.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domain_control_relationships.csv"))
time.sleep(2)


# client.query(control_CSF_function.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
# time.sleep(2)

# client.query(control_CSF_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
# time.sleep(2)

# client.query(control_CSF_subcategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Actual_From_Excel.csv"))
# time.sleep(2)

# client.query(control_cis_controls_id.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-CIS-Controls-Mapping.csv"))
# time.sleep(2)

# client.query(control_cis_controls_name.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-CIS-Controls-Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27001-Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27001_clause.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27001-Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27002-Mapping.csv"))
# time.sleep(2)

# client.query(control_iso_27002_clause.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-ISO27002-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1_1_functions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1_1_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_pmf_1_1_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_PMF_1_1-Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_rmf_step.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST_RMF-Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_ai_rmf_functions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_ai_rmf_categories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
# time.sleep(2)

# client.query(control_nist_ai_rmf_subcategories.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-NIST-AI-RMF-Mapping.csv"))
# time.sleep(2)


# client.query(control_glba_sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-GLBA-Mapping.csv"))
# time.sleep(2)

# client.query(control_glba_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-GLBA-Mapping.csv"))
# time.sleep(2)

# client.query(control_hipaa_rules.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HIPAA-Mapping.csv"))
# time.sleep(2)

# client.query(control_hipaa_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HIPAA-Mapping.csv"))
# time.sleep(2)

# client.query(control_hitech_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HITECH-Mapping.csv"))
# time.sleep(2)

# client.query(control_hitrust.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-HITRUST-Mapping.csv"))
# time.sleep(2)

client.query(control_pcidss_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)


client.query(control_pcidss_sub_requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF-PCI-DSS-Mapping.csv"))
time.sleep(2)

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