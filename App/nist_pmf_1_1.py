# nist_pmf_1_1.py

# UPDATED: Constraints are now composite to ensure uniqueness within a ISFrameworksAndStandard.
constraints = """
CREATE CONSTRAINT pmf_11_ISFrameworksAndStandard_id_unique IF NOT EXISTS FOR (f:ISFrameworksAndStandard) REQUIRE f.IS_framework_standard_id IS UNIQUE;
CREATE CONSTRAINT pmf_11_function_id_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.IS_framework_standard_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_category_id_unique IF NOT EXISTS FOR (c:Category) REQUIRE (c.IS_framework_standard_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_subcategory_id_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.IS_framework_standard_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_objective_id_unique IF NOT EXISTS FOR (po:PrivacyObjective) REQUIRE (po.IS_framework_standard_id, po.objective_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_tier_id_unique IF NOT EXISTS FOR (it:ImplementationTier) REQUIRE (it.IS_framework_standard_id, it.tier_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_ai_risk_id_unique IF NOT EXISTS FOR (apr:AIPrivacyRisk) REQUIRE (apr.IS_framework_standard_id, apr.ai_risk_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_org_id_unique IF NOT EXISTS FOR (o:Organization) REQUIRE (o.IS_framework_standard_id, o.org_id) IS UNIQUE;
"""

indexes = """
// Create comprehensive performance indexes
CREATE INDEX pmf_11_function_foundational IF NOT EXISTS FOR (fn:Function) ON (fn.is_foundational, fn.function_id);
CREATE INDEX pmf_11_tier_maturity IF NOT EXISTS FOR (it:ImplementationTier) ON (it.tier_number, it.maturity_level);
CREATE INDEX pmf_11_ai_risk_impact IF NOT EXISTS FOR (apr:AIPrivacyRisk) ON (apr.impact_level, apr.likelihood);
CREATE INDEX pmf_11_org_v11_adoption IF NOT EXISTS FOR (o:Organization) ON (o.v11_adoption_date, o.ai_governance_committee);
"""

# UPDATED: Using MERGE to prevent duplicates.
IS_frameworks_standard = """
MERGE (f:ISFrameworksAndStandard {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
SET
    f.name = 'NIST Privacy Framework 1.1',
    f.full_title = 'A Tool for Improving Privacy through Enterprise Risk Management - Version 1.1',
    f.version = '1.1',
    f.publication = 'NIST CSWP 01112025',
    f.publication_date = date('2025-01-11'),
    f.status = 'Active',
    f.purpose = 'Enhance privacy engineering practices supporting privacy by design concepts in AI systems';
"""


# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', function_id: row.function_id})
ON CREATE SET
    fn.name = row.function_name,
    fn.definition = row.function_definition,
    fn.is_foundational = CASE WHEN row.is_foundational = 'True' THEN true ELSE false END,
    fn.v11_updates = row.v11_updates,
    fn.primary_focus = row.primary_focus,
    fn.key_activities = split(row.key_activities, ','),
    fn.supports_functions = split(row.supports_functions, ',');
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', category_id: row.category_id})
ON CREATE SET
    c.function_id = row.function_id,
    c.name = row.category_name,
    c.definition = row.category_definition,
    c.v11_updates = row.v11_updates;
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', subcategory_id: row.subcategory_id})
ON CREATE SET
    s.category_id = row.category_id,
    s.function_id = row.function_id,
    s.name = row.subcategory_name,
    s.type = row.subcategory_type,
    s.updates = row.v11_updates;
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
ai_privacy_risks = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (apr:AIPrivacyRisk {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', ai_risk_id: row.ai_risk_id})
ON CREATE SET
    apr.risk_name = row.risk_name,
    apr.risk_description = row.risk_description,
    apr.risk_category = row.risk_category,
    apr.impact_level = row.impact_level,
    apr.likelihood = row.likelihood,
    apr.affected_functions = split(row.affected_functions, ','),
    apr.mitigation_strategies = split(row.mitigation_strategies, ','),
    apr.v11_section = row.v11_section;

"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
implementation_tiers = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (it:ImplementationTier {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', tier_id: row.tier_id})
ON CREATE SET
    it.tier_name = row.tier_name,
    it.tier_number = toInteger(row.tier_number),
    it.maturity_level = row.maturity_level,
    it.privacy_risk_management = row.privacy_risk_management,
    it.v11_updates = row.v11_updates;
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
organization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:Organization {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', org_id: row.org_id})
ON CREATE SET
    o.org_name = row.org_name,
    o.industry = row.industry,
    o.sector = row.sector,
    o.size = row.size,
    o.employees = toInteger(row.employees),
    o.privacy_framework_version = row.privacy_framework_version,
    o.implementation_tier = row.implementation_tier,
    o.current_profile_maturity = row.current_profile_maturity,
    o.target_profile_maturity = row.target_profile_maturity,
    o.ai_system_count = toInteger(row.ai_system_count),
    o.data_processing_types = split(row.data_processing_types, ','),
    o.privacy_program_established = date(row.privacy_program_established),
    o.v11_adoption_date = date(row.v11_adoption_date),
    o.ai_governance_committee = CASE WHEN row.ai_governance_committee = 'True' THEN true ELSE false END,
    o.csf_integration = row.csf_integration,
    o.key_ai_privacy_focus = split(row.key_ai_privacy_focus, ',');
"""

# UPDATED: Using MERGE and adding ISFrameworksAndStandard_id.
objectives = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:PrivacyObjective {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', objective_id: row.objective_id})
ON CREATE SET
    po.objective_name = row.objective_name,
    po.objective_definition = row.objective_definition,
    po.related_functions = split(row.related_functions, ','),
    po.engineering_focus = split(row.engineering_focus, ','),
    po.v11_updates = row.v11_updates;
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
framework_standard_function_rel = """
MATCH (f:ISFrameworksAndStandard {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN ['ID-P', 'GV-P', 'CT-P', 'CM-P', 'PR-P']
MERGE (f)-[:FRAMEWORK_STANDARD_HAS_FUNCTION]->(fn);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_category_rel = """
MATCH (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (c:Category {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:FUNCTION_HAS_CATEGORY]->(c);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
category_subcategory_rel = """
MATCH (c:Category {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (s:Subcategory {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE c.category_id = s.category_id
MERGE (c)-[:CATEGORY_HAS_SUBCATEGORY]->(s);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_support_imp_function_rel = """
MATCH (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', is_foundational: true})
MATCH (nfn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025', is_foundational: false})
MERGE (fn)-[:FUNCTION_HAS_FOUNDATIONAL_SUPPORT {relationship_type: 'Foundational_Support', support_area: fn.primary_focus}]->(nfn);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_ai_risk_rel = """
MATCH (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (apr:AIPrivacyRisk {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN apr.affected_functions
MERGE (fn)-[:FUNCTION_ADDRESSES_AI_RISKS {address_type: 'AI_Privacy_Risk_Mitigation', v11_new_capability: true}]->(apr);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
function_objective_rel = """
MATCH (fn:Function {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (po:PrivacyObjective {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN po.related_functions
MERGE (fn)-[:FUNCTION_SUPPORTS_OBJECTIVE]->(po);
"""

# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
org_ai_risk_rel = """
MATCH (o:Organization {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (apr:AIPrivacyRisk {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MERGE (o)-[:ORGANIZATION_FACES_AI_RISKS]->(apr);
"""



# UPDATED: Scoped MATCH to ISFrameworksAndStandard_id.
org_tier_rel = """
MATCH (o:Organization {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
MATCH (it:ImplementationTier {IS_framework_standard_id: 'NIST_PRIVACY_11_2025'})
WHERE o.implementation_tier = it.tier_id
MERGE (o)-[:ORGANIZATION_HAS_TIER]->(it);
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

client.query(IS_frameworks_standard)
time.sleep(2)
logger.info('ISFrameworksAndStandard')

client.query(functions.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_functions.csv"))
time.sleep(2)
logger.info('Function')

client.query(categories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_categories.csv"))
time.sleep(2)
logger.info('Category')

client.query(subcategories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_subcategories.csv"))
time.sleep(2)
logger.info('Subcategory')

client.query(ai_privacy_risks.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_ai_risks.csv"))
time.sleep(2)
logger.info('AIPrivacyRisk')

client.query(objectives.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_objectives.csv"))
time.sleep(2)
logger.info('Objective')


client.query(organization.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_organizations.csv"))
time.sleep(2)
logger.info('Organization')


client.query(implementation_tiers.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.1/nist_privacy_framework_11_tiers.csv"))
time.sleep(2)
logger.info('ImplementationTier')





logger.info("Creating relationships...")
client.query(framework_standard_function_rel)
time.sleep(2)

client.query(function_category_rel)
time.sleep(2)

client.query(category_subcategory_rel)
time.sleep(2)

client.query(category_subcategory_rel)
time.sleep(2)

client.query(function_support_imp_function_rel)
time.sleep(2)

client.query(function_ai_risk_rel)
time.sleep(2)

client.query(function_objective_rel)
time.sleep(2)

client.query(org_ai_risk_rel)
time.sleep(2)

client.query(org_tier_rel)
time.sleep(2)



logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:ISFrameworksAndStandard)-[*]->()
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
  rels: [r IN uniqueRels | r {
    .*,
    id: elementId(r),
    type: type(r),
    from: elementId(startNode(r)),
    to: elementId(endNode(r))
  }]
} AS graph_data""")

res = res[-1]['graph_data']

import json
with open('nist_pmf_1_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist_pmf_1_1.json")


client.close()
