# nist_pmf_1_1.py

# UPDATED: Constraints are now composite to ensure uniqueness within a framework.
constraints = """
CREATE CONSTRAINT pmf_11_framework_id_unique IF NOT EXISTS FOR (pf:PrivacyFramework) REQUIRE pf.framework_id IS UNIQUE;
CREATE CONSTRAINT pmf_11_function_id_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.framework_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_category_id_unique IF NOT EXISTS FOR (c:Category) REQUIRE (c.framework_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_subcategory_id_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.framework_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_objective_id_unique IF NOT EXISTS FOR (po:PrivacyObjective) REQUIRE (po.framework_id, po.objective_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_tier_id_unique IF NOT EXISTS FOR (it:ImplementationTier) REQUIRE (it.framework_id, it.tier_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_ai_risk_id_unique IF NOT EXISTS FOR (apr:AIPrivacyRisk) REQUIRE (apr.framework_id, apr.ai_risk_id) IS UNIQUE;
CREATE CONSTRAINT pmf_11_org_id_unique IF NOT EXISTS FOR (o:Organization) REQUIRE (o.framework_id, o.org_id) IS UNIQUE;
"""

indexes = """
// Create comprehensive performance indexes
CREATE INDEX pmf_11_function_foundational IF NOT EXISTS FOR (fn:Function) ON (fn.is_foundational, fn.function_id);
CREATE INDEX pmf_11_tier_maturity IF NOT EXISTS FOR (it:ImplementationTier) ON (it.tier_number, it.maturity_level);
CREATE INDEX pmf_11_ai_risk_impact IF NOT EXISTS FOR (apr:AIPrivacyRisk) ON (apr.impact_level, apr.likelihood);
CREATE INDEX pmf_11_org_v11_adoption IF NOT EXISTS FOR (o:Organization) ON (o.v11_adoption_date, o.ai_governance_committee);
"""

# UPDATED: Using MERGE to prevent duplicates.
framework = """
// Load NIST Privacy Framework 1.1
MERGE (pf:Framework {framework_id: 'NIST_PRIVACY_11_2025'})
ON CREATE SET
    pf.name = 'NIST Privacy Framework',
    pf.version = '1.1',
    pf.publication = 'NIST CSWP 40',
    pf.publication_date = date('2025-04-14'),
    pf.status = 'Initial Public Draft',
    pf.total_functions = 5,
    pf.total_categories = 19,
    pf.total_subcategories = 110,
    pf.key_updates = 'AI privacy risks, CSF 2.0 alignment, standalone governance',
    pf.alignment_frameworks = 'NIST Cybersecurity Framework 2.0, AI Risk Management Framework';
"""

# UPDATED: Using MERGE and adding framework_id.
functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fn:Function {framework_id: 'NIST_PRIVACY_11_2025', function_id: row.function_id})
ON CREATE SET
    fn.name = row.function_name,
    fn.definition = row.function_definition,
    fn.is_foundational = CASE WHEN row.is_foundational = 'True' THEN true ELSE false END,
    fn.v11_updates = row.v11_updates,
    fn.primary_focus = row.primary_focus,
    fn.key_activities = split(row.key_activities, ','),
    fn.supports_functions = split(row.supports_functions, ',');
"""

# UPDATED: Using MERGE and adding framework_id.
categories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {framework_id: 'NIST_PRIVACY_11_2025', category_id: row.category_id})
ON CREATE SET
    c.function_id = row.function_id,
    c.name = row.category_name,
    c.definition = row.category_definition,
    c.v11_updates = row.v11_updates;
"""

# UPDATED: Using MERGE and adding framework_id.
subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subcategory {framework_id: 'NIST_PRIVACY_11_2025', subcategory_id: row.`Sub-Category`})
ON CREATE SET
    s.category_id = row.Category,
    s.subcategory_name = row.subcategory_name;
"""

# UPDATED: Using MERGE and adding framework_id.
ai_privacy_risks = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (apr:AIPrivacyRisk {framework_id: 'NIST_PRIVACY_11_2025', ai_risk_id: row.ai_risk_id})
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

# UPDATED: Using MERGE and adding framework_id.
implementation_tiers = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (it:ImplementationTier {framework_id: 'NIST_PRIVACY_11_2025', tier_id: row.tier_id})
ON CREATE SET
    it.tier_name = row.tier_name,
    it.tier_number = toInteger(row.tier_number),
    it.maturity_level = row.maturity_level,
    it.privacy_risk_management = row.privacy_risk_management,
    it.v11_updates = row.v11_updates;
"""

# UPDATED: Using MERGE and adding framework_id.
organization = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:Organization {framework_id: 'NIST_PRIVACY_11_2025', org_id: row.org_id})
ON CREATE SET
    o.org_name = row.org_name,
    o.industry = row.industry,
    o.sectory = row.sectory,
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

# UPDATED: Using MERGE and adding framework_id.
objectives = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:PrivacyObjective {framework_id: 'NIST_PRIVACY_11_2025', objective_id: row.objective_id})
ON CREATE SET
    po.objective_name = row.objective_name,
    po.objective_definition = row.objective_definition,
    po.related_functions = split(row.related_functions, ','),
    po.engineering_focus = split(row.engineering_focus, ','),
    po.v11_updates = row.v11_updates;
"""

# UPDATED: Scoped MATCH to framework_id.
framework_function_rel = """
MATCH (pf:Framework {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN ['ID-P', 'GV-P', 'CT-P', 'CM-P', 'PR-P']
MERGE (pf)-[:HAS_FUNCTION]->(fn);
"""

# UPDATED: Scoped MATCH to framework_id.
function_category_rel = """
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (c:Category {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id = c.function_id
MERGE (fn)-[:HAS_CATEGORY]->(c);
"""

# UPDATED: Scoped MATCH to framework_id.
category_subcategory_rel = """
MATCH (c:Category {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (s:Subcategory {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE c.category_id = s.category_id
MERGE (c)-[:HAS_SUBCATEGORY]->(s);
"""

# UPDATED: Scoped MATCH to framework_id.
function_support_imp_function_rel = """
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_11_2025', is_foundational: true})
MATCH (nfn:Function {framework_id: 'NIST_PRIVACY_11_2025', is_foundational: false})
MERGE (fn)-[:FOUNDATIONAL_FOR {relationship_type: 'Foundational_Support', support_area: fn.primary_focus}]->(nfn);
"""

# UPDATED: Scoped MATCH to framework_id.
function_ai_risk_rel = """
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (apr:AIPrivacyRisk {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN apr.affected_functions
MERGE (fn)-[:ADDRESSES {address_type: 'AI_Privacy_Risk_Mitigation', v11_new_capability: true}]->(apr);
"""

# UPDATED: Scoped MATCH to framework_id.
function_objective_rel = """
MATCH (fn:Function {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (po:PrivacyObjective {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE fn.function_id IN po.related_functions
MERGE (fn)-[:SUPPORTS]->(po);
"""

# UPDATED: Scoped MATCH to framework_id.
org_ai_risk_rel = """
MATCH (o:Organization {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (apr:AIPrivacyRisk {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE o.ai_system_count > 0 AND (
    (o.industry = 'Healthcare' AND apr.ai_risk_id IN ['AI_BIAS_001', 'AI_PII_001']) OR
    (o.industry = 'Financial Services' AND apr.ai_risk_id IN ['AI_BIAS_001', 'AI_RECON_001']) OR
    apr.impact_level = 'High'
)
MERGE (o)-[:FACES {risk_exposure: 'Active_AI_Systems', ai_systems_count: o.ai_system_count}]->(apr);
"""

# UPDATED: Scoped MATCH to framework_id.
org_tier_rel = """
MATCH (o:Organization {framework_id: 'NIST_PRIVACY_11_2025'})
MATCH (it:ImplementationTier {framework_id: 'NIST_PRIVACY_11_2025'})
WHERE o.implementation_tier = it.tier_id
MERGE (o)-[:HAS_TIER]->(it);
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

client.query(framework)
time.sleep(2)
logger.info('Framework')

client.query(functions.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/functions.csv'))
time.sleep(2)
logger.info('Function')

client.query(categories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/categories.csv'))
time.sleep(2)
logger.info('Category')

client.query(subcategories.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20PMF%201.0/subcategories.csv'))
time.sleep(2)
logger.info('Subcategory')

logger.info("Creating relationships...")
client.query(framework_function_rel)
time.sleep(2)

client.query(function_category_rel)
time.sleep(2)

client.query(category_subcategory_rel)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

client.close()
