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
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_RULE]->(r);
"""

# Security Rule to its Standards (45 CFR 164.308-316)
rules_to_standards = """
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'R02'})
MATCH (s:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_type: 'Standard'})
WHERE s.rule_id <> 'STD-00'
MERGE (r)-[:RULE_HAS_STANDARD]->(s);
"""

# Standards to Specifications, paired by CFR citation
# (a Standard sits at e.g. 164.308(a)(1)(i); its specifications at 164.308(a)(1)(ii)(A-D))
standards_to_specifications = """
UNWIND [
    ['STD-308A1', ['SPEC-308A1A', 'SPEC-308A1B', 'SPEC-308A1C', 'SPEC-308A1D']],
    ['STD-308A3', ['SPEC-308A3A', 'SPEC-308A3B', 'SPEC-308A3C']],
    ['STD-308A4', ['SPEC-308A4A', 'SPEC-308A4B', 'SPEC-308A4C']],
    ['STD-308A5', ['SPEC-308A5A', 'SPEC-308A5B', 'SPEC-308A5C', 'SPEC-308A5D']],
    ['STD-308A6', ['SPEC-308A6A']],
    ['STD-308A7', ['SPEC-308A7A', 'SPEC-308A7B', 'SPEC-308A7C', 'SPEC-308A7D', 'SPEC-308A7E']],
    ['STD-308B1', ['SPEC-308B3']],
    ['STD-310A1', ['SPEC-310A2I', 'SPEC-310A2II', 'SPEC-310A2III', 'SPEC-310A2IV']],
    ['STD-310D1', ['SPEC-310D2I', 'SPEC-310D2II', 'SPEC-310D2III', 'SPEC-310D2IV']],
    ['STD-312A1', ['SPEC-312A2I', 'SPEC-312A2II', 'SPEC-312A2III', 'SPEC-312A2IV']],
    ['STD-312C1', ['SPEC-312C2']],
    ['STD-312E1', ['SPEC-312E2I', 'SPEC-312E2II']],
    ['STD-314A1', ['SPEC-314A2I', 'SPEC-314A2II', 'SPEC-314A2III']],
    ['STD-314B1', ['SPEC-314B2']],
    ['STD-316B1', ['SPEC-316B2I', 'SPEC-316B2II', 'SPEC-316B2III']]
] AS pair
UNWIND pair[1] AS spec_id
MATCH (s:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: pair[0]})
MATCH (spec:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: spec_id})
MERGE (s)-[:STANDARD_INCLUDES_SPECIFICATION]->(spec);
"""

# Rules to the requirements that sit directly under them
# (permitted disclosures and individual rights under the Privacy Rule, the
#  general provisions of the Security Rule, the breach provisions, enforcement)
rules_to_requirements = """
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (q:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE (r.rule_id = 'R01' AND (q.rule_type IN ['PrivacyProvision', 'IndividualRight'] OR q.rule_id = 'PD00'))
   OR (r.rule_id = 'R02' AND q.rule_id STARTS WITH 'SECGEN')
   OR (r.rule_id = 'R03' AND q.rule_id STARTS WITH 'BN')
   OR (r.rule_id = 'R04' AND q.rule_id STARTS WITH 'ENFRULE')
MERGE (r)-[:RULE_HAS_REQUIREMENT]->(q);
"""

# PD00 is the parent of the twelve permitted use/disclosure categories
permitted_disclosure_categories = """
MATCH (p:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'PD00'})
MATCH (c:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_type: 'PermittedDisclosure'})
WHERE c.rule_id <> 'PD00'
MERGE (p)-[:RULE_HAS_REQUIREMENT]->(c);
"""

# The framework root node holds the four top-level Rules
framework_root_to_rules = """
MATCH (f:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: 'FRAME-00'})
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE r.rule_id IN ['R01', 'R02', 'R03', 'R04']
MERGE (f)-[:RULE_HAS_REQUIREMENT]->(r);
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

# A security incident is what triggers the breach risk assessment (45 CFR 164.402(2))
security_risk_breach = """
MATCH (s:SecurityRisk {industry_standard_regulation_id: 'HIPAA 2026', security_id: 'SR02'})
MATCH (b:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'BRCH-01'})
MERGE (s)-[:INCIDENT_TRIGGERS_ASSESSMENT]->(b);
"""

# The four culpability tiers of 45 CFR 160.404(b)(2) apply to violations of any Rule
rule_enforcement = """
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE r.rule_id IN ['R01', 'R02', 'R03', 'R04']
MATCH (e:Enforcement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE e.enf_id IN ['E05', 'E06', 'E07', 'E08']
MERGE (r)-[:RULE_ENFORCED_BY_TIER]->(e);
"""

# Each Rule has its own violation category
rule_violation_category = """
UNWIND [['R01', 'E02'], ['R02', 'E03'], ['R03', 'E04']] AS pair
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: pair[0]})
MATCH (e:Enforcement {industry_standard_regulation_id: 'HIPAA 2026', enf_id: pair[1]})
MERGE (r)-[:RULE_VIOLATION_CATEGORY]->(e);
"""

# Enforcement escalation path: violation -> OCR investigation -> action -> penalty
enforcement_escalation = """
UNWIND [
    ['E01', 'E09'], ['E02', 'E09'], ['E03', 'E09'], ['E04', 'E09'],
    ['E09', 'E10'],
    ['E10', 'E11'], ['E10', 'E12'], ['E10', 'E13'],
    ['E12', 'E15'], ['E12', 'E16'], ['E12', 'E17'], ['E12', 'E14'],
    ['E01', 'E18']
] AS pair
MATCH (a:Enforcement {industry_standard_regulation_id: 'HIPAA 2026', enf_id: pair[0]})
MATCH (b:Enforcement {industry_standard_regulation_id: 'HIPAA 2026', enf_id: pair[1]})
MERGE (a)-[:ENFORCEMENT_ESCALATES_TO]->(b);
"""

# framework to actors/entities ##
framework_actors = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_ACTORS]->(a);
"""
# framework to organizational context ##
framework_organizational = """
MATCH (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (o:OrganizationalContext {industry_standard_regulation_id: 'HIPAA 2026'})
MERGE (i)-[:INDUSTRY_STANDARD_REGULATION_CONTAINS_ORGANIZATIONAL_CONTEXT]->(o);
"""
# Actors that create, receive, maintain or transmit PHI (the workforce and
# contracting chain); regulators and data subjects are related by other edges
actor_phi = """
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE a.actor_id IN ['CE01', 'CE02', 'CE03', 'BA01', 'SC01', 'WF01', 'PS01']
MATCH (d:PHIData {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE d.data_id IN ['DATA-00', 'EPHI01']
MERGE (a)-[:ACTOR_HANDLES_DATA]->(d);
"""
# The Security Rule safeguards apply to ePHI; the Privacy, breach, governance and
# documentation safeguards apply to PHI in any form
phi_safeguard = """
MATCH (d:PHIData {industry_standard_regulation_id: 'HIPAA 2026'})
MATCH (c:Safeguard {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE (d.data_id = 'EPHI01' AND c.category = 'Security')
   OR (d.data_id = 'DATA-00' AND c.category IN ['Privacy', 'Breach', 'Governance',
                                                'Data Sharing logic', 'Operational Workflow'])
MERGE (d)-[:DATA_PROTECTED_BY_SAFEGUARD]->(c);
"""
# Safeguards paired with the risks they address
safeguard_risk = """
UNWIND [
    ['C01', ['SR01', 'SR06', 'SR10', 'SR11']],
    ['C02', ['SR06']],
    ['C03', ['SR06']],
    ['C04', ['SR06']],
    ['C05', ['SR06']],
    ['C06', ['SR10']],
    ['C07', ['SR06']],
    ['C08', ['SR06']],
    ['C09', ['SR-00']],
    ['C10', ['SR06', 'SR11']],
    ['C11', ['SR06']],
    ['C12', ['SR13']],
    ['C13', ['SR12']],
    ['C14', ['SR06']],
    ['C15', ['SR06']],
    ['C16', ['SR06']],
    ['C17', ['SR06']],
    ['C19', ['SR-00']],
    ['C20', ['SR-00']],
    ['B01', ['SR02', 'SR03', 'SR07', 'SR08', 'SR09']],
    ['SAFE-00', ['SR04']]
] AS pair
UNWIND pair[1] AS risk_id
MATCH (c:Safeguard {industry_standard_regulation_id: 'HIPAA 2026', control_id: pair[0]})
MATCH (s:SecurityRisk {industry_standard_regulation_id: 'HIPAA 2026', security_id: risk_id})
MERGE (c)-[:SAFEGUARD_MITIGATES_RISK]->(s);
"""

# The breach notification workflow: which provision governs which step
breach_rule_to_step = """
UNWIND [
    ['R03',  ['BRCH-00']],
    ['BN01', ['BRCH-01', 'BRCH-02', 'BRCH-09', 'BRCH-10', 'BRCH-11',
              'BRCH-12', 'BRCH-13', 'BRCH-14', 'BRCH-15']],
    ['BN02', ['BRCH-16']],
    ['BN03', ['BRCH-03', 'BRCH-04', 'BRCH-07', 'BRCH-17']],
    ['BN04', ['BRCH-06']],
    ['BN05', ['BRCH-05']],
    ['BN06', ['BRCH-18']],
    ['BN07', ['BRCH-19']],
    ['BN08', ['BRCH-08', 'BRCH-20']]
] AS pair
UNWIND pair[1] AS breach_id
MATCH (r:HIPAARule {industry_standard_regulation_id: 'HIPAA 2026', rule_id: pair[0]})
MATCH (b:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: breach_id})
MERGE (r)-[:RULE_GOVERNS_BREACH_STEP]->(b);
"""

# The sequence the breach management nodes describe in their trigger column
breach_step_sequence = """
UNWIND [
    ['BRCH-16', 'BRCH-01'],
    ['BRCH-01', 'BRCH-02'], ['BRCH-01', 'BRCH-08'], ['BRCH-01', 'BRCH-18'],
    ['BRCH-02', 'BRCH-04'], ['BRCH-02', 'BRCH-05'], ['BRCH-02', 'BRCH-06'],
    ['BRCH-02', 'BRCH-20'],
    ['BRCH-04', 'BRCH-03'], ['BRCH-04', 'BRCH-07'], ['BRCH-04', 'BRCH-17'],
    ['BRCH-18', 'BRCH-02']
] AS pair
MATCH (a:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: pair[0]})
MATCH (b:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: pair[1]})
MERGE (a)-[:BREACH_STEP_TRIGGERS]->(b);
"""

# The four-factor risk assessment of 45 CFR 164.402(2)
breach_assessment_factors = """
MATCH (a:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'BRCH-02'})
MATCH (f:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE f.breach_id IN ['BRCH-12', 'BRCH-13', 'BRCH-14', 'BRCH-15']
MERGE (a)-[:BREACH_ASSESSMENT_FACTOR]->(f);
"""

# The three exclusions from the definition of breach, 45 CFR 164.402(1)
breach_definition_exceptions = """
MATCH (b:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'BRCH-01'})
MATCH (x:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE x.breach_id IN ['BRCH-09', 'BRCH-10', 'BRCH-11']
MERGE (b)-[:BREACH_DEFINITION_EXCEPTION]->(x);
"""

# Law enforcement delay applies to each notification, 45 CFR 164.412
breach_notification_delay = """
MATCH (n:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE n.breach_id IN ['BRCH-04', 'BRCH-05', 'BRCH-06', 'BRCH-18']
MATCH (d:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'BRCH-19'})
MERGE (n)-[:BREACH_NOTIFICATION_DELAYED_BY]->(d);
"""

# Affected individuals are the data subjects who receive the notice
breach_affects_actor = """
MATCH (b:BreachManagement {industry_standard_regulation_id: 'HIPAA 2026', breach_id: 'BRCH-03'})
MATCH (a:Actor {industry_standard_regulation_id: 'HIPAA 2026', actor_id: 'DS01'})
MERGE (b)-[:BREACH_AFFECTS_ACTOR]->(a);
"""
# NIST CSF 2.0 - Mapping to HIPAA 2026 (Example of cross-framework relationships)
# Cross-mapping NIST CSF 2.0 Subcategories to HIPAA 2026 Safeguards
nist_to_hipaa_mapping = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.relationship = 'MAPPED_TO_HIPAA_SAFEGUARD'
MATCH (sc:Subcategory {
    subcategory_id: row.source_id, 
    IS_frameworks_standard_id: 'NIST_CSF_2.0'
})
MATCH (sg:Safeguard {
    control_id: row.target_id, 
    industry_standard_regulation_id: 'HIPAA 2026'
})

// 3. Create the cross-framework relationship
MERGE (sc)-[:NIST_CSF_MAPPED_TO_HIPAA_SAFEGUARD]->(sg);
"""

# Each category CSV has a root node; hang its members off it so the taxonomies
# are navigable rather than a loose bag of nodes
root_containment = """
UNWIND [
    ['PHIData', 'data_id', 'DATA-00'],
    ['PHIData', 'data_id', 'LIFE-00'],
    ['Enforcement', 'enf_id', 'ENF-00'],
    ['Safeguard', 'control_id', 'SAFE-00'],
    ['SecurityRisk', 'security_id', 'SR-00'],
    ['BreachManagement', 'breach_id', 'BRCH-00'],
    ['OrganizationalContext', 'context_id', 'CTX-00']
] AS spec
MATCH (root {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE spec[0] IN labels(root) AND root[spec[1]] = spec[2]
MATCH (child {industry_standard_regulation_id: 'HIPAA 2026'})
WHERE spec[0] IN labels(child)
  AND child[spec[1]] <> spec[2]
  AND (CASE spec[2]
         WHEN 'LIFE-00' THEN child[spec[1]] STARTS WITH 'PHILIFE'
         WHEN 'DATA-00' THEN NOT child[spec[1]] STARTS WITH 'PHILIFE'
         ELSE true
       END)
MERGE (root)-[:ROOT_CONTAINS]->(child);
"""

# The security risk chain described by the related_to column
security_risk_chain = """
UNWIND [
    ['SR01', 'SR05'], ['SR05', 'SR06'], ['SR06', 'SR04'],
    ['SR02', 'SR03'], ['SR03', 'SR07'], ['SR03', 'SR08'], ['SR03', 'SR09'],
    ['SR01', 'SR10']
] AS pair
MATCH (a:SecurityRisk {industry_standard_regulation_id: 'HIPAA 2026', security_id: pair[0]})
MATCH (b:SecurityRisk {industry_standard_regulation_id: 'HIPAA 2026', security_id: pair[1]})
MERGE (a)-[:SECURITY_RISK_LEADS_TO]->(b);
"""

# Drop every HIPAA relationship before rebuilding, so a re-run replaces the edge
# set instead of merging new edges alongside stale ones
clear_relationships = """
MATCH (n {industry_standard_regulation_id: 'HIPAA 2026'})-[r]-()
DELETE r;
"""



import os
import time
import logging
from app import Neo4jConnect

BASE_URL = "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/HIPAA"

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

client.query(actors.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Actors.csv"))
time.sleep(2)

client.query(data_PHI.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Data_PHI.csv"))
time.sleep(2)

client.query(rules_requirements.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Rules%20&%20Requirements.csv"))
time.sleep(2)

client.query(controls_safeguards.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Controls%20&%20Safeguards.csv"))
time.sleep(2)

client.query(security_risk.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Security%20&%20Risk.csv"))
time.sleep(2)

client.query(breach_management.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Breach%20Management.csv"))
time.sleep(2)

client.query(organizational.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Organizational.csv"))
time.sleep(2)

client.query(enforcement.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20Enforcement.csv"))
time.sleep(2)

# Relationships
client.query(clear_relationships)
time.sleep(2)

client.query(framework_to_rules)
time.sleep(2)

client.query(framework_root_to_rules)
time.sleep(2)

client.query(rules_to_standards)
time.sleep(2)

client.query(standards_to_specifications)
time.sleep(2)

client.query(rules_to_requirements)
time.sleep(2)

client.query(permitted_disclosure_categories)
time.sleep(2)

client.query(ce_engages_ba)
time.sleep(2)

client.query(ba_engages_sc)
time.sleep(2)

client.query(actors_sign_baa)
time.sleep(2)

client.query(actors_maintain_phi)
time.sleep(2)

client.query(regulator_audits_actors)
time.sleep(2)

client.query(safeguards_protect_phi)
time.sleep(2)

client.query(attestation_governs_rh)
time.sleep(2)

client.query(safeguards_phi)
time.sleep(2)

client.query(root_containment)
time.sleep(2)

client.query(security_risk_chain)
time.sleep(2)

client.query(security_risk_breach)
time.sleep(2)

client.query(rule_enforcement)
time.sleep(2)

client.query(rule_violation_category)
time.sleep(2)

client.query(enforcement_escalation)
time.sleep(2)

client.query(breach_rule_to_step)
time.sleep(2)

client.query(breach_step_sequence)
time.sleep(2)

client.query(breach_assessment_factors)
time.sleep(2)

client.query(breach_definition_exceptions)
time.sleep(2)

client.query(breach_notification_delay)
time.sleep(2)

client.query(breach_affects_actor)
time.sleep(2)

client.query(framework_actors)
time.sleep(2)

client.query(framework_organizational)
time.sleep(2)

client.query(actor_phi)
time.sleep(2)


client.query(phi_safeguard)
time.sleep(2)

client.query(safeguard_risk)
time.sleep(2)

client.query(nist_to_hipaa_mapping.replace('$file_path', f"{BASE_URL}/HIPAA%20-%20CSF%20Mapping.csv"))
time.sleep(2)





logger.info("Graph structure loaded successfully.")

query = """
MATCH (n {industry_standard_regulation_id: 'HIPAA 2026'})
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
