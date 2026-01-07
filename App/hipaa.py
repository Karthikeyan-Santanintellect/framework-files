# UPDATED: Using MERGE to prevent errors on re-runs.
#Industry Standard & Regulations: HIPAA
import re


industry_standard_and_regulations = """
MERGE(i:IndustryStandardAndRegulation{industry_standard_regulation_id:'HIPAA 1996'})
ON CREATE SET
    i.name='HIPAA',
    i.description='The Health Insurance Portability and Accountability Act (HIPAA) is a US regulation that sets standards for protecting sensitive patient health information.',
    i.url='https://www.hhs.gov/hipaa/index.html',
    i.abbreviation='Health Insurance Portability and Accountability Act',
    i.version='1996',
    i.published_date='1996-08-21',
    i.type='Regulation';
"""


hipaa_standards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Standard{standard_id: row.id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    s.title = row.title,
    s.safeguard_type = row.safeguard_type,
    s.type = row.standard_type,
    s.text = row.text,
    s.req_type = row.req_type,
    s.section = row.section,
    s.source_doc = row.source_doc,
    s.source_section = row.source_section;
"""

mappings = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (m:Mapping {mapping_id: row.hipaa_id + '_TO_' + row.csf_subcategory_id, industry_standard_regulation_id: "HIPAA 1996"})
ON CREATE SET
    m.type = row.mapping_type,
    m.confidence = row.confidence,
    m.rationale = row.rationale,
    m.source_doc = row.source_doc,
    m.source_section = row.source_section;
"""

#primary entity
primary_entity= """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Rule{rule_id: row.rule_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    r.name = row.name,
    r.cfr_citation = row.cfr_citation,
    r.cfr_parts = row.cfr_parts,
    r.description = row.description,
    r.long_description = row.long_description,
    r.type = row.type,
    r.rule_category = row.rule_category,
    r.enacted_date = row.enacted_date,
    r.effective_date = row.effective_date,
    r.last_amended_date = row.last_amended_date,
    r.applicable_entities = row.applicable_entities,
    r.primary_requirements = row.primary_requirements,
    r.authorization_required = row.authorization_required,
    r.minimum_necessary_applies = row.minimum_necessary_applies,
    r.documentation_required = row.documentation_required,
    r.audit_required = row.action_required,
    r.encryption_required = row.encryption_required,
    r.audit_logging_required =row.audit_logging_required,
    r.risk_assessment_frequency = row.risk_assessment_frequency,
    r.enforcement_authority = row.enforcement_authority,
    r.url = row.url,
    r.reference_url = row.reference_url,
    r.industry_standard_regulation_id = row.industry_standard_regulation_id,
    r.status = row.status,
    r.compliance_complexity = row.compliance_complexity,
    r.severity_rating = row.severity_rating;
  """
#data_protection_nodes
data_protection_nodes ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:DataProtectionNode{node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    d.name = row.name,
    d.description = row.description,
    d.node_type = row.node_type,
    d.category = row.category,
    d.type = row.type,
    d.sensitivity_level = row.sensitivity_level,
    d.regulated = row.regulated,
    d.properties_count = row.properties_count,
    d.cfr_citation = row.cfr_citation,
    d.parent_node = row.parent_node;
"""
#privacy_rule
privacy_rule ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:PrivacyRule{node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    p.name = row.name,
    p.description = row.description,
    p.node_type = row.node_type,
    p.category = row.category,
    p.type = row.type,
    p.properties_count = row.properties_count,
    p.regulated = row.regulated,
    p.cfr_citation = row.cfr_citation,
    p.sensitivity_level = row.sensitivity_level,
    p.parent_node = row.parent_node;
"""

#security_rule 
security_rule ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sr:SecurityRule{node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    sr.name = row.name,
    sr.description = row.description,
    sr.node_type = row.node_type,
    sr.category = row.category,
    sr.type = row.type,
    sr.properties_count = row.properties_count,
    sr.regulated = row.regulated,
    sr.cfr_citation = row.cfr_citation,
    sr.sensitivity_level = row.sensitivity_level,
    sr.parent_node = row.parent_node;
"""
#Breach_notifications
breach_notifications ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bn:BreachNotification{node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996})
ON CREATE SET
    bn.name = row.name,
    bn.description = row.description,
    bn.node_type = row.node_type,
    bn.category = row.category,
    bn.type = row.type,
    bn.properties_count = row.properties_count,
    bn.regulated = row.regulated,
    bn.cfr_citation = row.cfr_citation,
    bn.sensitivity_level = row.sensitivity_level,
    bn.parent_node = row.parent_node;
"""
#compliance_enforcement
compliance_enforcement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ce:ComplianceEnforcement{node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    ce.name = row.name,
    ce.description = row.description,
    ce.node_type = row.node_type,
    ce.category = row.category,
    ce.type = row.type,
    ce.properties_count = row.properties_count,
    ce.regulated = row.regulated,
    ce.cfr_citation = row.cfr_citation,
    ce.sensitivity_level = row.sensitivity_level,
    ce.parent_node = row.parent_node;
"""
#organizational_governance
organizational_governance ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (og:OrganizationalGovernance {node_id: row.node_id, industry_standard_regulation_id: 'HIPAA 1996'})
ON CREATE SET
    og.name = row.name,
    og.description = row.description,
    og.node_type = row.node_type,
    og.category = row.category,
    og.type = row.type,
    og.properties_count = row.properties_count,
    og.regulated = row.regulated,
    og.cfr_citation = row.cfr_citation,
    og.sensitivity_level = row.sensitivity_level,
    og.parent_node = row.parent_node;
"""


#Relationships
industry_standard_and_regulations_hipaa_standards_rel = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (s:Standard {industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_STANDARDS]->(s);
"""


# UPDATED: Scoped MATCH to framework_id for precision.
hipaa_parent_child_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.parent_id IS NOT NULL AND row.parent_id <> ''
MATCH (child:Standard {standard_id: row.id, industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (parent:Standard {standard_id: row.parent_id, industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (parent)-[:HIPAA_PARENT_CHILD_]->(child);
"""

hipaa_standard_mapping_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Standard {industry_standard_regulation_id: 'HIPAA 1996', standard_id: row.source_standard_id})
MATCH (m:Mapping {mapping_id: row.target_mapping_id})
MERGE (s)-[:STANDARD_MAPS_TO_MAPPING {relationship_type: row.relationship_type, mapping_type: row.mapping_type, confidence: row.confidence}]->(m);
"""

mapping_subcategory_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (m:Mapping {mapping_id: row.source_mapping_id})
MATCH (sc:Subcategory {id: row.target_subcategory_id, IS_framework_standard_id: 'NIST_CSF_2.0'})
MERGE (m)-[:MAPPING_TARGETS_SUB_CATEGORY]->(sc);
"""

regulation_privacy_rules = """
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pr:PrivacyRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:REGULATION_REGULATES_PRIVACY_RULE]->(pr);
"""
regulation_security_rules = """
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:REGULATION_CONTAINS_SECURITY_RULE]->(sr);
"""
regulation_breach_notifications = """
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (br:BreachNotificationRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:REGULATION_CONTAINS_BREACH_NOTIFICATION_RULE]->(br);
"""
regulation_compliance_enforcement = """
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ce:ComplianceEnforcementRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:REGULATION_CONTAINS_COMPLIANCE_ENFORCEMENT_RULE]->(ce);
"""
regulation_organizational_governance ="""
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (og:OrganizationalGovernanceRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (i)-[:REGULATION_CONTAINS_ORGANIZATIONAL_GOVERNANCE_RULE]->(og);
"""
privacy_security_rules = """
MATCH (p:PrivacyRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (p)-[:PRIVACY_RULE_REFERENCES_SECURITY_RULE]->(sr);
"""
security_rules_breach_notifications = """
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996})
MERGE (sr)-[:SECURITY_RULE_REFERENCES_BREACH_NOTIFICATION]->(bn);
"""

breach_notifications_compliance_enforcement = """
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (ce:ComplianceEnforcement{node_type: 'EnforcementAuthority', industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (bn)-[:BREACH_NOTIFICATION_REFERENCES_COMPLIANCE_ENFORCEMENT]->(ce);
"""
data_protection_privacy_rules ="""
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (pr:PrivacyRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (d)-[:DATA_PROTECTION_NODE_REFERENCES_PRIVACY_RULE]->(pr);
"""
data_protection_security_rules ="""
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (d)-[:DATA_PROTECTION_NODE_REFERENCES_SECURITY_RULE]->(sr);
"""
data_protection_breach_notifications ="""
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (d)-[:DATA_PROTECTION_NODE_REFERENCES_BREACH_NOTIFICATION]->(bn);
"""
privacy_rule_data_protection="""
MATCH (pr:PrivacyRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pr)-[:PRIVACY_RULE_REFERENCES_DATA_PROTECTION_NODE]->(d);
"""
privacy_rule_breach_notifications ="""
MATCH (pr:PrivacyRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (pr)-[:PRIVACY_RULE_REFERENCES_BREACH_NOTIFICATION]->(bn);
"""
security_rule_data_protection ="""
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sr)-[:SECURITY_RULE_REFERENCES_DATA_PROTECTION_NODE]->(d);
"""
security_rule_breach_notifications ="""
MATCH (sr:SecurityRule{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (sr)-[:SECURITY_RULE_REFERENCES_BREACH_NOTIFICATION]->(bn);
"""
breach_notifications_data_protection ="""
MATCH (bn:BreachNotification{industry_standard_regulation_id: 'HIPAA 1996'})
MATCH (d:DataProtectionNode{industry_standard_regulation_id: 'HIPAA 1996'})
MERGE (bn)-[:BREACH_NOTIFICATION_REFERENCES_DATA_PROTECTION_NODE]->(d);
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

client.query(industry_standard_and_regulations)
time.sleep(2)

client.query(hipaa_standards.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_standards.csv'))
time.sleep(2)

client.query(mappings.replace('$file_path','https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_csf_mappings.csv'))
time.sleep(2)

client.query(industry_standard_and_regulations_hipaa_standards_rel)
time.sleep(2)

client.query(hipaa_parent_child_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_standards.csv"))
time.sleep(2)

client.query(hipaa_standard_mapping_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/maps_to_relationships.csv"))
time.sleep(2)

client.query(mapping_subcategory_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/target_relationships.csv"))

logger.info("Graph structure loaded successfully.")

res = client.query("""MATCH path = (:IndustryStandardAndRegulation)-[*]->()
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
with open('hipaa.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to hipaa.json")


client.close()
