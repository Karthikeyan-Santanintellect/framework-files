#Industry_standard_regulation
industry_standard_regulation ="""
MERGE (i:IndustryStandardAndRegulation {industry_standard_regulation_id: "NERC_CIP"})
ON CREATE SET
  i.name = "NERC Critical Infrastructure Protection",
  i.version = "NERC CIP Version 5 / V6+",
  i.enactment_date = date("2008-01-17"),
  i.effective_date = date("2016-07-01"),
  i.jurisdiction = "North America (Bulk Electric System)",
  i.status = "Active",
  i.description = "A set of mandatory cybersecurity standards enforced by the North American Electric Reliability Corporation (NERC) to secure the Bulk Electric System (BES). It requires entities to identify critical assets and apply controls for electronic and physical security, personnel training, incident response, and recovery to ensure the reliability of the North American power grid.";
"""
#standard Node
standard ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (std:Standard {industry_standard_regulation_id: 'NERC_CIP', standard_id: row.node_id})
ON CREATE SET
  std.number                          = row.standard_number,
  std.full_number                     = row.standard_full_number,
  std.name                            = row.standard_name,
  std.version_current                 = row.version_current,
  std.effective_date                  = row.effective_date,
  std.purpose                         = row.purpose,
  std.applicability                   = row.applicability,
  std.status                          = row.status,
  std.requirement_count               = row.requirement_count,
  std.part_count                      = row.part_count,
  std.measure_count                   = row.measure_count,
  std.vrf_levels                      = row.vrf_levels,
  std.source_document                 = row.source_document;
"""
#Requirement Node
requirement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', requirement_id: row.requirement_id})
ON CREATE SET
  req.requirement_number              = row.requirement_number,
  req.standard_id                     = row.standard_id,
  req.title                           = row.requirement_title,
  req.description                     = row.requirement_description,
  req.violation_risk_factor           = row.vrf,
  req.time_horizon                    = row.time_horizon,
  req.compliance_measure              = row.measure,
  req.parts_count                     = row.parts_count,
  req.vsl_lower                       = row.vsl_lower,
  req.vsl_moderate                    = row.vsl_moderate,
  req.vsl_high                        = row.vsl_high,
  req.vsl_severe                      = row.vsl_severe,
  req.applicability_statement         = row.applicability,
  req.source_document                 = row.source_document;
"""

#requirement_part
requirement_part ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rp:RequirementPart {industry_standard_regulation_id: 'NERC_CIP', requirement_part_id: row.requirement_part_id})
ON CREATE SET
  rp.requirement_id                   = row.requirement_id,
  rp.standard_id                      = row.standard_id,
  rp.part_number                      = row.part_number,
  rp.description                      = row.part_description,
  rp.applicable_systems               = row.applicable_systems,
  rp.compliance_measure               = row.measure,
  rp.source_document                  = row.source_document;
"""
#Domain
domain ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dom:Domain {industry_standard_regulation_id: 'NERC_CIP', domain_id: row.domain_id})
ON CREATE SET
  dom.name                            = row.domain_name,
  dom.category                        = row.domain_category,
  dom.description                     = row.description,
  dom.cip_standards_covered           = row.cip_standards_covered,
  dom.key_controls                    = row.key_controls,
  dom.applicable_entities             = row.applicable_entities,
  dom.risk_focus                      = row.risk_focus;
"""
#Role (Internal Roles)
roles ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {
  industry_standard_regulation_id: 'NERC_CIP',
  role_id: row.internal_role_id
})
ON CREATE SET
  ro.name                = row.role_name,
  ro.category            = row.role_category,
  ro.organization_level  = row.organization_level,
  ro.responsible_for     = row.responsible_for,
  ro.required_training   = row.required_training,
  ro.required_clearance  = row.required_clearance,
  ro.access_level        = row.access_level,
  ro.accountability      = row.accountability,
  ro.cip_requirement     = row.cip_requirement,
  ro.titles      = row.example_titles;
"""

#Artifact
artifact ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (art:Artifact {
  industry_standard_regulation_id: 'NERC_CIP',
  artifact_id: row.artifact_id
})
ON CREATE SET
  art.name                  = row.artifact_name,
  art.type                  = row.artifact_type,
  art.category              = row.artifact_category,
  art.evidence_category     = row.evidence_category,
  art.related_standard      = row.related_standard,
  art.related_requirement   = row.related_requirement,
  art.description           = row.description,
  art.retention_period      = row.retention_period,
  art.storage_location      = row.storage_location,
  art.access_control        = row.access_control,
  art.confidentiality_level = row.confidentiality_level,
  art.cip_evidence_level    = row.cip_evidence_level,
  art.responsible_party     = row.responsible_party,
  art.update_frequency      = row.update_frequency,
  art.bcsi_content          = row.bcsi_content;
  """
#regulator
regulator ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (reg:Regulator {
  industry_standard_regulation_id: 'NERC_CIP',
  regulator_id: row.regulator_id
})
ON CREATE SET
  reg.name                 = row.regulator_name,
  reg.type                 = row.regulator_type,
  reg.jurisdiction         = row.jurisdiction,
  reg.enforcement_authority= row.enforcement_authority,
  reg.primary_function     = row.primary_function,
  reg.regulated_entities   = row.regulated_entities,
  reg.compliance_oversight = row.compliance_oversight,
  reg.audit_authority      = row.audit_authority,
  reg.penalty_authority    = row.penalty_authority,
  reg.coordination_role    = row.coordination_role,
  reg.contact_method       = row.contact_method;
"""

















#Relationships
#IndustryStandardAndRegulation → Standard
# Framework relationships
regulation_standard_rel = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (i)-[:INDUSTRY_STANDARD_AND_REGULATION_HAS_STANDARD {relationship_type: 'Framework_Standard'}]->(std);
"""


# Standards hierarchy
standard_requirement = """
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', standard_id: std.standard_id})
MERGE (std)-[:STANDARD_CONTAINS_REQUIREMENT {relationship_type: 'Standard_Requirement'}]->(req);
"""

requirement_requirement_part = """
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (rp:RequirementPart {industry_standard_regulation_id: 'NERC_CIP', requirement_id: req.requirement_id})
MERGE (req)-[:REQUIREMENT_HAS_PART {relationship_type: 'Requirement_Part'}]->(rp);
"""

standard_domain = """
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (dom:Domain {industry_standard_regulation_id: 'NERC_CIP'})
WHERE dom.cip_standards_covered CONTAINS std.number
MERGE (std)-[:STANDARD_ADDRESSES_DOMAIN {relationship_type: 'Standard_Domain'}]->(dom);
"""

domain_requirement = """
MATCH (dom:Domain {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP'})
WHERE dom.cip_standards_covered CONTAINS req.standard_id
MERGE (dom)-[:DOMAIN_IMPLEMENTS_REQUIREMENT {relationship_type: 'Domain_Requirement'}]->(req);
"""










artifact_standard = """
MATCH (art:Artifact {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP', standard_id: art.related_standard})
MERGE (art)-[:ARTIFACT_EVIDENCES_STANDARD {relationship_type: 'Evidence_Standard'}]->(std);
"""

artifact_requirement = """
MATCH (art:Artifact {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (req:Requirement {industry_standard_regulation_id: 'NERC_CIP', requirement_id: art.related_requirement})
MERGE (art)-[:ARTIFACT_EVIDENCES_REQUIREMENT {relationship_type: 'Evidence_Requirement'}]->(req);
"""


regulator_standard = """
MATCH (reg:Regulator {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (reg)-[:REGULATOR_ENFORCES_STANDARD {relationship_type: 'Regulatory_Enforcement'}]->(std);
"""

# Roles are scoped to standards via the CSV's cip_requirement column; 'CIP-003 through CIP-014'
# denotes programme-wide accountability and therefore spans every standard.
role_standard = """
MATCH (ro:Role {industry_standard_regulation_id: 'NERC_CIP'})
MATCH (std:Standard {industry_standard_regulation_id: 'NERC_CIP'})
WHERE ro.cip_requirement CONTAINS std.standard_id OR ro.cip_requirement CONTAINS 'through'
MERGE (ro)-[:ROLE_ACCOUNTABLE_FOR_STANDARD {relationship_type: 'Role_Standard'}]->(std);
"""











orphan_domain = """
MATCH (orphan:Domain) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (reg)-[:NERC_CIP_GOVERNS_DOMAIN]->(orphan);
"""
orphan_requirement_part = """
MATCH (orphan:RequirementPart) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'NERC_CIP'})
MERGE (reg)-[:NERC_CIP_GOVERNS_REQUIREMENT_PART]->(orphan);
"""


import os
import re
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

#Nodes
client.query(industry_standard_regulation)
time.sleep(2)

client.query(standard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Standard.csv'))
time.sleep(2)

client.query(requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Requirement.csv'))
time.sleep(2)

client.query(requirement_part.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_RequirementPart.csv'))
time.sleep(2)

client.query(domain.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Domain.csv'))
time.sleep(2)

client.query(roles.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Role.csv'))
time.sleep(2)

client.query(artifact.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Artifact.csv'))
time.sleep(2)

client.query(regulator.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/NERC/nodes_Regulator.csv'))
time.sleep(2)


#Relationships
client.query(regulation_standard_rel)
time.sleep(2)

client.query(standard_requirement)
time.sleep(2)

client.query(requirement_requirement_part)
time.sleep(2)

client.query(standard_domain)
time.sleep(2)

client.query(domain_requirement)
time.sleep(2)


client.query(artifact_standard)
time.sleep(2)

client.query(artifact_requirement)
time.sleep(2)

client.query(regulator_standard)
time.sleep(2)

client.query(role_standard)
time.sleep(2)

client.query(orphan_domain)
time.sleep(2)

client.query(orphan_requirement_part)
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
    with open('nerc_cip.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to nerc_cip.json")
else:
    logger.error("No data returned from the query.")

client.close()




















 

    
























 




 



 

 

