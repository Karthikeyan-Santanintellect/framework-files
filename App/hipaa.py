#industry_standard_and_regulation
industry_standard_and_regulation = """
MERGE (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    i.name = 'HIPAA',
    i.full_name = 'Health Insurance Portability and Accountability Act',
    i.description = 'The federal framework setting standards for protecting sensitive patient health information. This modernized version includes the HITECH Act, 2013 Omnibus Rule, 2024 Reproductive Health Care Privacy Rule, and 2026 42 CFR Part 2 (SUD) alignments.',
    i.url = 'https://www.hhs.gov/hipaa/index.html',
    i.version = 'Modernized 2026 Edition (Includes 2024 Final Rules)',
    i.original_published_date = '1996-08-21',
    i.latest_update_published = '2024-04-26', 
    i.type = 'Regulation';
"""
# Actors/Entities
actors = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Actor {actor_id: row.actor_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    a.actor_type = row.actor_type,
    a.description = row.description,
    a.applies_to = row.applies_to,
    a.role_category = row.role_category,
    a.framework = 'HIPAA 2026';
"""
# Data PHI Categories
data_PHI = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:PHIData {data_id: row.data_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    d.data_type = row.data_type,
    d.description = row.description,
    d.format = row.format,
    d.classification = row.classification,
    d.example_elements = row.example_elements,
    d.framework = 'HIPAA 2026';
"""
# Rules and Requirements
rules_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:HIPAARule {rule_id: row.rule_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    r.rule_name = row.rule_name,
    r.cfr_reference = row.cfr_reference,
    r.description = row.description,
    r.applicable_entities = row.applicable_entities,
    r.rule_type = row.rule_type,
    r.framework = 'HIPAA 2026';
"""
# Controls and Safeguards
controls_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Safeguard {control_id: row.control_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    c.control_type = row.control_type,
    c.control_name = row.control_name,
    c.description = row.description,
    c.category = row.category,
    c.implementation_type = row.implementation_type,
    c.framework = 'HIPAA 2026';
"""
# Security and risk
security_risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:SecurityRisk {security_id: row.security_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    s.node_type = row.node_type,
    s.description = row.description,
    s.related_to = row.related_to,
    s.priority = row.priority,
    s.framework = 'HIPAA 2026';
"""
# Breach and Management
breach_management = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (b:BreachManagement {breach_id: row.breach_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    b.node_type = row.node_type,
    b.description = row.description,
    b.trigger = row.trigger,
    b.timeline = row.timeline,
    b.framework = 'HIPAA 2026';
"""
# Organizational 
organizational = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (o:OrganizationalContext {context_id: row.context_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    o.node_type = row.node_type,
    o.description = row.description,
    o.example = row.example,
    o.impact = row.impact,
    o.framework = 'HIPAA 2026';
"""
# Enforcement
enforcement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:Enforcement {enf_id: row.enf_id, industry_standard_regulation_id: 'HIPAA 2026'})
ON CREATE SET
    e.node_type = row.node_type,
    e.description = row.description,
    e.severity = row.severity,
    e.penalty_range = row.penalty_range,
    e.framework = 'HIPAA 2026';
"""
# Relationships

# Framework to Rules
framework_to_rules = """
MATCH (f:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE r.rule_id IN ['R01', 'R02', 'R03', 'R04']
MERGE (f)-[:FRAMEWORK_CONTAINS_RULE]->(r);
"""

# Rules to Standards
rules_to_standards = """
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE r.rule_id IN ['R01', 'R02', 'R03']
MATCH (s:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'STD-00'})
MERGE (r)-[:RULE_HAS_STANDARD]->(s);
"""

# Standards to Specifications
standards_to_specifications = """
MATCH (s:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'STD-00'})
MATCH (spec:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'SPEC-00'})
MERGE (s)-[:STANDARD_INCLUDES_SPECIFICATION]->(spec);
"""

# Covered Entity to Business Associate
ce_engages_ba = """
MATCH (ce:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE ce.actor_id IN ['CE01', 'CE02', 'CE03']
MATCH (ba:Actor {industry_standard_regulation_id: 'HIPAA 2026', actor_id: 'BA01'})
MERGE (ce)-[:ACTOR_ENGAGES_BUSINESS_ASSOCIATE]->(ba);
"""

# Business Associate to Subcontractor
ba_engages_sc = """
MATCH (ba:Actor {industry_standard_regulation_id: 'HIPAA 2026', actor_id: 'BA01'})
MATCH (sc:Actor {industry_standard_regulation_id: 'HIPAA 2026', actor_id: 'SC01'})
MERGE (ba)-[:BUSINESS_ASSOCIATE_ENGAGES_SUBCONTRACTOR]->(sc);
"""

# Actors Sign Business Associate Agreement (BAA)
actors_sign_baa = """
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE a.actor_id IN ['CE01', 'BA01']
MATCH (baa:OrganizationalContext {industry_standard_regulation_id: 'HIPAA 2026', context_id: 'ORG10'})
MERGE (a)-[:ACTOR_SIGNS_AGREEMENT]->(baa);
"""

# Actors Maintain PHI/ePHI
actors_maintain_phi = """
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE a.actor_id IN ['CE01', 'BA01']
MATCH (phi:PHIData {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE phi.data_id IN ['DATA-00', 'EPHI01']
MERGE (a)-[:ACTOR_MAINTAINS_PHI]->(phi);
"""

# Regulator Audits Actors
regulator_audits_actors = """
MATCH (reg:Actor {industry_standard_regulation_id: 'HIPAA 2026', actor_id: 'RG01'})
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE a.actor_id IN ['CE01', 'BA01']
MERGE (reg)-[:REGULATOR_AUDITS_ACTOR]->(a);
"""

# Safeguards Protect PHI
safeguards_protect_phi = """
MATCH (sg:Safeguard {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE sg.control_id IN ['C07', 'C08']
MATCH (phi:PHIData {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE phi.data_id IN ['EPHI01', 'PHICAT03', 'PHICAT04']
MERGE (sg)-[:SAFEGUARD_PROTECTS_DATA]->(phi);
"""

# 2024 Attestation Governs Reproductive Health
attestation_governs_rh = """
MATCH (att:Safeguard {industry_standard_regulation_id: 'HIPAA 2026', control_id: 'P02'})
MATCH (rh:PHIData {industry_standard_regulation_id: 'HIPAA 2026', data_id: 'PHICAT03'})
MERGE (att)-[:SAFEGUARD_GOVERNS_LAWFUL_DISCLOSURE_OF_PHI]->(rh);
"""

# Notice of Privacy Practices (NPP) Governs SUD Records
safeguards_phi = """
MATCH (npp:Safeguard {industry_standard_regulation_id: 'HIPAA 2026', control_id: 'P03'})
MATCH (sud:PHIData {industry_standard_regulation_id: 'HIPAA 2026', data_id: 'PHICAT04'})
MERGE (npp)-[:SAFEGUARD_GOVERNS_LAWFUL_DISCLOSURE_OF_PHI]->(sud);
"""

# Security Incidents Trigger Breach Assessment
security_risk_breach = """
MATCH (inc:SecurityRisk {industry_standard_regulation_id: 'HIPAA 2026', security_id: 'SR02'})
MATCH (brk:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'B02'})
MERGE (inc)-[:INCIDENT_TRIGGERS_ASSESSMENT]->(brk);
"""

# Breach Requires Notifications
breach_management_notifications = """
MATCH (brc:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'B01'})
MATCH (req:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE req.breach_id IN ['B04', 'B05', 'B06']
MERGE (brc)-[:BREACH_REQUIRES_NOTIFICATION]->(req);
"""

# Rules Enforced by Penalties
rule_enforcement = """
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'R04'})
MATCH (e:Enforcement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE e.enf_id IN ['E05', 'E06', 'E07', 'E08']
MERGE (r)-[:RULE_ENFORCED_BY_TIER]->(e);
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

client.query(industry_standard_and_regulation)
time.sleep(2)

client.query(actors.replace('$file_path',""))
time.sleep(2)

client.query(data_PHI.replace('$file_path',""))
time.sleep(2)

client.query(rules_requirements.replace('$file_path',""))
time.sleep(2)

client.query(controls_safeguards.replace('$file_path',""))
time.sleep(2)

client.query(security_risk.replace('$file_path',""))
time.sleep(2)

client.query(breach_management.replace('$file_path',""))
time.sleep(2)

client.query(organizational.replace('$file_path',""))
time.sleep(2)

client.query(enforcement.replace('$file_path',""))
time.sleep(2)

# Relationships
client.query(framework_to_rules.replace('$file_path',""))
time.sleep(2)

client.query(rules_to_standards.replace('$file_path',""))
time.sleep(2)

client.query(standards_to_specifications.replace('$file_path',""))
time.sleep(2)

client.query(ce_engages_ba.replace('$file_path',""))
time.sleep(2)

client.query(ba_engages_sc.replace('$file_path',""))
time.sleep(2)

client.query(actors_sign_baa.replace('$file_path',""))
time.sleep(2)

client.query(actors_maintain_phi.replace('$file_path',""))
time.sleep(2)

client.query(regulator_audits_actors.replace('$file_path',""))
time.sleep(2)

client.query(safeguards_protect_phi.replace('$file_path',""))
time.sleep(2)

client.query(attestation_governs_rh.replace('$file_path',""))
time.sleep(2)

client.query(safeguards_phi.replace('$file_path',""))
time.sleep(2)

client.query(security_risk_breach.replace('$file_path',""))
time.sleep(2)

client.query(breach_management_notifications.replace('$file_path',""))
time.sleep(2)

client.query(rule_enforcement.replace('$file_path',""))
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
    with open('hipaa.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to hipaa.json")
else:
    logger.error("No data returned from the query.")

client.close()
