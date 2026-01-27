# Create HITRUST Standard Node
industry_standard_regulation = """
MERGE (s:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITRUST 11.6.0'})
ON CREATE SET
    s.name = "Health Information Trust Alliance",
    s.version = "11.6.0",
    s.publication_date = date("2025-08-22"),
    s.type = "Industrial",
    s.description = "It integrates multiple standards, such as HIPAA, ISO, and PCI, into a single, comprehensive framework to safeguard sensitive data";
"""



# Load HITRUST Category
hitrust_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Category {industry_standard_regulation_id: 'HITRUST 11.6.0', category_id: row.id})
ON CREATE SET
    c.number = toInteger(row.number),
    c.name = row.name,
    c.description = row.description;
"""

# Load HITRUST Control
hitrust_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctrl:Control {industry_standard_regulation_id: 'HITRUST 11.6.0', control_id: row.id})
ON CREATE SET
    ctrl.name = row.name,
    ctrl.category_id = row.category_id,
    ctrl.description = row.description;
"""

# Load HITRUST Control_objective
hitrust_control_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:ControlObjective {industry_standard_regulation_id: 'HITRUST 11.6.0', objective_id: row.id})
ON CREATE SET
    co.control_id = row.control_id,
    co.description = row.text;
"""

# Load HITRUST Control_specification
hitrust_control_specification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cs:ControlSpecification {industry_standard_regulation_id: 'HITRUST 11.6.0', specification_id: row.id})
ON CREATE SET
    cs.control_id = row.control_id,
    cs.description = row.text;
"""
# Load Assurance Levels
hitrust_assurance_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (al:AssuranceLevel {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.level})
ON CREATE SET al.description = row.description;
"""

#Load Implementation Requirements
hitrust_requirement_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:ImplementationRequirement {industry_standard_regulation_id: 'HITRUST 11.6.0', requirement_id: row.id})
ON CREATE SET 
    req.control_id = row.control_id,
    req.level = row.level,
    req.description = row.text;
"""

#Load Assessment Procedures
hitrust_procedure_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AssessmentProcedure {industry_standard_regulation_id: 'HITRUST 11.6.0', procedure_id: row.id})
ON CREATE SET 
    ap.method = row.method, 
    ap.description = row.description;
"""

#Load Healthcare Data Categories
hitrust_data_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:HealthcareDataCategory {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.name})
ON CREATE SET 
    d.type = row.type, 
    d.is_sensitive = toBoolean(row.is_sensitive);
"""

#Load Risks & Threats
hitrust_risk_threat_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:HealthcareThreat {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.threat_name})
ON CREATE SET 
  t.category = row.threat_category,
  t.risk_name = row.risk_name,
  t.description = row.risk_description;
"""

#Load Roles & Organization
hitrust_role_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rl:Role {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.role_name})
ON CREATE SET rl.primary_responsibility = row.responsibility;
"""

#Load Regulations
hitrust_regulation_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:Regulation {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.rule_name})
ON CREATE SET reg.cfr_reference = row.cfr;
"""

#Load Ecosystem
hitrust_ecosystem_nodes = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ba:BusinessAssociate {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.name})
ON CREATE SET ba.type = row.type;
"""


#Relationships
# Create CONTAINS relationships (standard -> category)
hitrust_standard_category_rel = """
MATCH (s:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HITRUST 11.6.0'})
MATCH (c:Category {industry_standard_regulation_id: 'HITRUST 11.6.0'})
MERGE (s)-[:INDUSTRY_STANDARD_CONTAINS_CATEGORY]->(c);
"""

# Create HAS_CONTROL relationships (Category -> Control)
hitrust_category_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Category {industry_standard_regulation_id: 'HITRUST 11.6.0', category_id: row.start_id})
MATCH (ctrl:Control {industry_standard_regulation_id: 'HITRUST 11.6.0', control_id: row.end_id})
MERGE (c)-[:CATEGORY_HAS_CONTROL]->(ctrl);
"""

# Create HAS_OBJECTIVE relationships (Control -> ControlObjective)
hitrust_control_ControlObjective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {industry_standard_regulation_id: 'HITRUST 11.6.0', control_id: row.start_id})
MATCH (co:ControlObjective {industry_standard_regulation_id: 'HITRUST 11.6.0', objective_id: row.end_id})
MERGE (ctrl)-[:CONTROL_HAS_CONTROL_OBJECTIVE]->(co);
"""

# Create HAS_SPECIFICATION relationships (ControlObjective -> ControlSpecification)
hitrust_ControlObjective_specification = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:ControlObjective {industry_standard_regulation_id: 'HITRUST 11.6.0', objective_id: row.start_id})
MATCH (cs:ControlSpecification {industry_standard_regulation_id: 'HITRUST 11.6.0', specification_id: row.end_id})
MERGE (co)-[:CONTROL_OBJECTIVE_HAS_SPECIFICATION]->(cs);
"""
# Link Framework to Assurance Levels 
hitrust_framework_assurance_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:IndustryStandardAndRegulation {industry_standard_regulation_id: row.framework_id})
MATCH (al:AssuranceLevel {industry_standard_regulation_id: row.framework_id, name: row.assurance_level})
MERGE (s)-[:INDUSTRY_STANDARD_REGULATION_DEFINES_ASSURANCE_LEVEL]->(al);
"""
# Link Controls to Implementation Requirements#
hitrust_rel_control_has_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {industry_standard_regulation_id: 'HITRUST 11.6.0', control_id: row.control_id})
MATCH (req:ImplementationRequirement {industry_standard_regulation_id: 'HITRUST 11.6.0', requirement_id: row.requirement_id})
MERGE (ctrl)-[:CONTROL_HAS_REQUIREMENT]->(req);
"""
hitrust_rel_requirement_assurance_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:ImplementationRequirement {industry_standard_regulation_id: 'HITRUST 11.6.0', requirement_id: row.requirement_id})
MATCH (al:AssuranceLevel {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.assurance_level})
MERGE (req)-[:REQUIREMENT_DEFINES_ASSURANCE_LEVEL]->(al);
"""

# Link Requirements to Procedures
hitrust_requirement_procedure_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (req:ImplementationRequirement {industry_standard_regulation_id: 'HITRUST 11.6.0', requirement_id: row.requirement_id})
MATCH (ap:AssessmentProcedure {industry_standard_regulation_id: 'HITRUST 11.6.0', procedure_id: row.procedure_id})
MERGE (req)-[:REQUIREMENT_ASSESSED_BY_PROCEDURE]->(ap);
"""

# Link Data Categories to Framework
hitrust_framework_data_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:IndustryStandardAndRegulation {industry_standard_regulation_id: row.framework_id})
MATCH (d:HealthcareDataCategory {industry_standard_regulation_id: row.framework_id, name: row.data_name})
MERGE (s)-[:INDUSTRY_STANDARD_REGULATION_PROTECTS_DATA_ASSET]->(d);
"""


# Link Threats to Data Targets
hitrust_rel_threat_target = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (t:HealthcareThreat {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.threat_name})
MATCH (d:HealthcareDataCategory {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.target_data})
MERGE (t)-[:THREAT_TARGETS_DATA_CATEGORY]->(d);
"""

# Create Organization and Link Roles#
hitrust_org_structure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:HealthcareOrganization {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.org_name})
MATCH (rl:Role {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.role_name})
MERGE (org)-[:ORGANIZATION_APPOINTS_ROLES]->(rl);
"""
# Link Framework to Regulations
hitrust_framework_regulation_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:IndustryStandardAndRegulation {industry_standard_regulation_id: row.framework_id})
MATCH (reg:Regulation {industry_standard_regulation_id: row.framework_id, name: row.rule_name})
MERGE (s)-[:INDUSTRY_STANDARD_REGULATION_HARMONIZES_REGULATION]->(reg);
"""


# Link Org to Ecosystem#
hitrust_org_ecosystem_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (org:HealthcareOrganization {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.org_name})
MATCH (ba:BusinessAssociate {industry_standard_regulation_id: 'HITRUST 11.6.0', name: row.ba_name})
MERGE (org)-[:ORGANIZATION_ENGAGES_BUSINESS_ASSOCIATE]->(ba);
"""
# Map HITRUST Controls to NIST CSF Subcategories#
hitrust_controls_nist_CSF_subcategories = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ctrl:Control {
  industry_standard_regulation_id: 'HITRUST 11.6.0'
})
WHERE ctrl.control_id = row.start_id OR ctrl.control_id = replace(row.start_id, 'HITRUST-', '')
MATCH (sc:Subcategory {
  id: row.end_id,
  IS_framework_standard_id: 'NIST_CSF_2.0'
})

MERGE (ctrl)-[:CONTROLS_MAPS_TO_SUBCATEGORIES {
  mapping_type: row.mapping_type,
  confidence: row.confidence,
  rationale: row.rationale,
  source_document_id: row.source_document_id,
  created_date: row.created_date
}]->(sc);
"""


import os
import time
import logging
from app import Neo4jConnect
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading graph structure...")

client.query(industry_standard_regulation)
time.sleep(2)


client.query(hitrust_category.replace('$file_path',
                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Category.csv"))
time.sleep(2)

client.query(hitrust_control.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Control.csv"))
time.sleep(2)

client.query(hitrust_control_objective.replace('$file_path',
                                               "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlObjective.csv"))
time.sleep(2)

client.query(hitrust_control_specification.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlSpecification.csv"))
time.sleep(2)

client.query(hitrust_assurance_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_assurance_levels.csv"))
time.sleep(2)

client.query(hitrust_requirement_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_implementation_requirements.csv"))
time.sleep(2)

client.query(hitrust_procedure_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_assessment_procedures.csv"))
time.sleep(2)

client.query(hitrust_data_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_data_categories.csv"))
time.sleep(2)

client.query(hitrust_risk_threat_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_risks_threats.csv"))
time.sleep(2)

client.query(hitrust_role_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_roles.csv"))
time.sleep(2)

client.query(hitrust_regulation_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_regulations.csv"))
time.sleep(2)

client.query(hitrust_ecosystem_nodes.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/hitrust_ecosystem.csv"))
time.sleep(2)



#Relationships
client.query(hitrust_standard_category_rel)
time.sleep(2)

client.query(hitrust_category_control.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_CONTROL.csv"))
time.sleep(2)

client.query(hitrust_control_ControlObjective.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_OBJECTIVE.csv"))
time.sleep(2)

client.query(hitrust_ControlObjective_specification.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_SPECIFICATION.csv"))
time.sleep(2)

client.query(hitrust_controls_nist_CSF_subcategories.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST%20-%20CSF%20Subcategory%20Mapping.csv"))
time.sleep(2)

client.query(hitrust_framework_assurance_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_framework_assurance.csv"))
time.sleep(2)

client.query(hitrust_rel_control_has_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST%20-%20Control%20Requirements.csv"))
time.sleep(2)

client.query(hitrust_rel_requirement_assurance_level.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST%20-%20Requirment%20Assurance%20Level.csv"))
time.sleep(2)


client.query(hitrust_requirement_procedure_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST%20-%20Requirements%20Procedure.csv"))
time.sleep(2)

client.query(hitrust_framework_data_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_framework_data.csv"))
time.sleep(2)

client.query(hitrust_rel_threat_target.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_threat_target.csv"))
time.sleep(2)

client.query(hitrust_org_structure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_org_roles.csv"))
time.sleep(2)

client.query(hitrust_framework_regulation_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_framework_reg.csv"))
time.sleep(2)

client.query(hitrust_org_ecosystem_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/rel_org_ecosystem.csv"))
time.sleep(2)


logger.info("Graph structure loaded successfully.")

query = """
MATCH (n)
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
    with open('hitrust.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to hitrust.json")
else:
    logger.error("No data returned from the query.")

client.close()

