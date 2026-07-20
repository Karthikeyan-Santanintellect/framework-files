#Regulation
regulation = """
MERGE (i:IndustryStandardAndRegulation {industry_standard_regulation_id: 'GLBA 1999'})
ON CREATE SET
  i.name = "Gramm-Leach-Bliley Act",
  i.version = "1999 (Pub. L. 106-102)",
  i.status = "Active",
  i.jurisdiction = "United States (Federal)",
  i.effective_date = date("1999-11-12"),
  i.enactment_date = date("1999-11-12"),
  i.description = "Federal law that requires financial institutions to explain their information-sharing practices to their customers and to safeguard sensitive data. It includes the Financial Privacy Rule, Safeguards Rule, and pretexting provisions.";
"""

#rule
rule = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ru:Rule{industry_standard_regulation_id: 'GLBA 1999', rule_id: row.ruleid})
ON CREATE SET
    ru.name = row.name,
    ru.description = row.description,
    ru.citation = row.citation;
"""

#section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section{industry_standard_regulation_id: 'GLBA 1999', section_id: row.sectionid})
ON CREATE SET
    sec.fullcitation = row.fullcitation,
    sec.heading = row.heading,
    sec.text = row.text;
"""
#requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Requirement{industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.requirementid})
ON CREATE SET
    r.type = row.type,
    r.text = row.text,
    r.priority = row.priority,
    r.frequency = row.frequency;
"""
#role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role{industry_standard_regulation_id: 'GLBA 1999', role_id: row.roleid})
ON CREATE SET
    ro.name = row.name,
    ro.description = row.description;
"""
#datacategory
datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory{industry_standard_regulation_id: 'GLBA 1999', data_id: row.dataid})
ON CREATE SET
    dc.name = row.name,
    dc.description = row.description,
    dc.examples = row.examples;
"""
#Eventype
eventype = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType{industry_standard_regulation_id: 'GLBA 1999', event_id:row.eventtypeid})
ON CREATE SET
    et.name = row.name,
    et.deadline = row.deadline;
"""
#safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999', safeguard_id: row.safeguardid})
ON CREATE SET
    s.name = row.name,
    s.type = row.type,
    s.description = row.description;
"""
#enforcement_action
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row  
MERGE (ea:EnforcementAction{industry_standard_regulation_id: 'GLBA 1999', enforcement_action_id: row.enforcementid})
ON CREATE SET
    ea.authority = row.authority,
    ea.description = row.description;
"""
#policy
policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:Policy{industry_standard_regulation_id: 'GLBA 1999', policy_id: row.policyid})
ON CREATE SET
    po.name = row.name,
    po.owner = row.owner;
"""
#control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Control{industry_standard_regulation_id: 'GLBA 1999', control_id: row.controlid})
ON CREATE SET
    co.name = row.name,
    co.category = row.category;
"""
#system
system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sys:System{industry_standard_regulation_id: 'GLBA 1999', system_id: row.systemid})
ON CREATE SET
    sys.name = row.name,
    sys.holds_npi = row.holds_npi;
"""
#process
process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pr:Process{industry_standard_regulation_id: 'GLBA 1999', process_id: row.processid})
ON CREATE SET
    pr.name = row.name;
"""

#QualifiedIndividual
qualified_individual = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (qi:QualifiedIndividual {industry_standard_regulation_id: 'GLBA 1999', qi_id: row.id})
ON CREATE SET 
    qi.name = row.name,
    qi.description = row.description,
    qi.mandate_source = row.mandate_source;
"""

#BoardOfDirectors
board_of_directors = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bod:BoardOfDirectors {industry_standard_regulation_id: 'GLBA 1999', bod_id: row.id})
ON CREATE SET 
    bod.name = row.name,
    bod.description = row.description;
"""

#ServiceProvider
service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:ServiceProvider {industry_standard_regulation_id: 'GLBA 1999', sp_id: row.id})
ON CREATE SET 
    sp.name = row.name,
    sp.description = row.description,
    sp.service_type = row.service_type;
"""

#RiskAssessment
risk_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ra:RiskAssessment {industry_standard_regulation_id: 'GLBA 1999', assessment_id: row.id})
ON CREATE SET 
    ra.name = row.name,
    ra.description = row.description,
    ra.category = row.category;
"""

#Threat
threat = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Threat {industry_standard_regulation_id: 'GLBA 1999', threat_id: row.id})
ON CREATE SET 
    t.name = row.name,
    t.description = row.description,
    t.category = row.category;
"""

#Asset
asset = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ast:Asset {industry_standard_regulation_id: 'GLBA 1999', asset_id: row.id})
ON CREATE SET 
    ast.name = row.name,
    ast.description = row.description,
    ast.category = row.category;
"""

#PrivacyNotice
privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pn:PrivacyNotice {industry_standard_regulation_id: 'GLBA 1999', notice_id: row.id})
ON CREATE SET 
    pn.name = row.name,
    pn.details = row.details,
    pn.timing = row.timing;
"""

#OptOutMechanism
opt_out_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (oom:OptOutMechanism {industry_standard_regulation_id: 'GLBA 1999', mechanism_id: row.id})
ON CREATE SET 
    oom.name = row.name,
    oom.details = row.details,
    oom.type = row.type;
"""

#NonAffiliatedThirdParty
non_affiliated_third_party = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (natp:NonAffiliatedThirdParty {industry_standard_regulation_id: 'GLBA 1999', entity_id: row.id})
ON CREATE SET 
    natp.name = row.name,
    natp.details = row.details;
"""

#SecurityBreach
security_breach = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sb:SecurityBreach {industry_standard_regulation_id: 'GLBA 1999', breach_id: row.id})
ON CREATE SET 
    sb.name = row.name,
    sb.description = row.description;
"""

#SocialEngineeringTactic
social_engineering_tactic = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (set:SocialEngineeringTactic {industry_standard_regulation_id: 'GLBA 1999', tactic_id: row.id})
ON CREATE SET 
    set.name = row.name,
    set.description = row.description;
"""
#Relationships
#Regulation → Rule
regulation_rule ="""
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id:'GLBA 1999'})
MATCH (ru:Rule{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (i)-[:REGULATION_HAS_RULE]->(ru);
"""
#Rule → Section
rule_section = """
MATCH (ru:Rule{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (sec:Section{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (ru)-[:RULE_HAS_SECTION]->(sec);
"""
#Section → Requirement
section_requirement = """
MATCH (sec:Section{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (sec)-[:SECTION_HAS_REQUIREMENT]->(r);
"""
#Requirement → Role
requirement_role = """
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ro:Role{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_APPLIES_TO_ROLE]->(ro);
"""
#Requirement → DataCategory
requirement_datacategory = """
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (dc:DataCategory{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_APPLIES_TO_DATACATEGORY]->(dc);
"""
#Requirement → EventType
requirement_event_type ="""
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (et:EventType{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE]->(et);
"""
#Requirement → Safeguard
requirement_safeguard = """
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(s);
"""
#Requirement → Policy
requirement_policy = """
MATCH (r:Requirement {
  industry_standard_regulation_id: 'GLBA 1999'
})
MATCH (po:Policy {
  industry_standard_regulation_id: 'GLBA 1999'
})
MERGE (r)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(po);
"""

#Requirement → Control
requirement_control ="""
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (co:Control{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co);
"""
#Control → System
control_system = """
MATCH (co:Control{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (sys:System{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (co)-[:CONTROL_IMPLEMENTED_IN_SYSTEM]->(sys);
"""
#Requirement → Process
requirement_process = """
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (pr:Process{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_IMPACTS_PROCESS]->(pr);
"""
#Role → Role (Customer → Financial Institution)
role_role = """
MATCH (src:Role{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (tgt:Role{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (src)-[:ROLE_HAS_ROLE]->(tgt);
"""
#Requirement → EnforcementAction
requirement_enforcement_action = """
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999'})
MATCH (ea:EnforcementAction{industry_standard_regulation_id: 'GLBA 1999'})
MERGE (r)-[:REQUIREMENT_ENFORCED_BY_ENFORCEMENT_ACTION]->(ea);
"""

#Requirement → QualifiedIndividual
requirement_qualified_individual = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.source_requirement_id})
MATCH (qi:QualifiedIndividual {industry_standard_regulation_id: 'GLBA 1999', qi_id: row.target_qi_id})
MERGE (r)-[:REQUIRES_DESIGNATION_OF_QUALIFIED_INDIVIDUAL{
    type: row.relationship_type,
    description: row.description
}]->(qi);
"""

#QualifiedIndividual → BoardOfDirectors
qualified_individual_board = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (qi:QualifiedIndividual {industry_standard_regulation_id: 'GLBA 1999', qi_id: row.source_qi_id})
MATCH (bod:BoardOfDirectors {industry_standard_regulation_id: 'GLBA 1999', bod_id: row.target_bod_id})
MERGE (qi)-[:QUALIFIED_INDIVIDUAL_REPORTS_TO_BOARD_OF_DIRECTORS{
    type: row.relationship_type,
    description: row.description
}]->(bod);
"""

#RiskAssessment → Asset
risk_assessment_asset = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ra:RiskAssessment {industry_standard_regulation_id: 'GLBA 1999', assessment_id: row.source_assessment_id})
MATCH (ast:Asset {industry_standard_regulation_id: 'GLBA 1999', asset_id: row.target_asset_id})
MERGE (ra)-[:RISK_ASSESSMENT_EVALUATES_RISK_IN_ASSET{
    type: row.relationship_type,
    description: row.description
}]->(ast);
"""

#RiskAssessment → Threat
risk_assessment_threat = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ra:RiskAssessment {industry_standard_regulation_id: 'GLBA 1999', assessment_id: row.source_assessment_id})
MATCH (t:Threat {industry_standard_regulation_id: 'GLBA 1999', threat_id: row.target_threat_id})
MERGE (ra)-[:RISK_ASSESSMENT_IDENTIFIES_THREAT {
    type: row.relationship_type,
    description: row.description
}]->(t);
"""

#Safeguard → Threat
safeguard_threat = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Safeguard {industry_standard_regulation_id: 'GLBA 1999', safeguard_id: row.source_safeguard_id})
MATCH (t:Threat {industry_standard_regulation_id: 'GLBA 1999', threat_id: row.target_threat_id})
MERGE (s)-[:SAFEGUARD_MITIGATES_THREAT {
    type: row.relationship_type,
    description: row.description
}]->(t);
"""

#Requirement → PrivacyNotice
requirement_privacy_notice = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.source_requirement_id})
MATCH (pn:PrivacyNotice {industry_standard_regulation_id: 'GLBA 1999', notice_id: row.target_notice_id})
MERGE (r)-[:REQUIREMENT_MUST_PROVIDE_PRIVACY_NOTICE {
    type: row.relationship_type,
    description: row.description
}]->(pn);
"""

#PrivacyNotice → OptOutMechanism
privacy_notice_mechanism = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (pn:PrivacyNotice {industry_standard_regulation_id: 'GLBA 1999', notice_id: row.source_notice_id})
MATCH (oom:OptOutMechanism {industry_standard_regulation_id: 'GLBA 1999', mechanism_id: row.target_mechanism_id})
MERGE (pn)-[:PRIVACY_NOTICE_CONTAINS_MECHANISM {
    type: row.relationship_type,
    description: row.description
}]->(oom);
"""

#OptOutMechanism → NonAffiliatedThirdParty
opt_out_third_party = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (oom:OptOutMechanism {industry_standard_regulation_id: 'GLBA 1999', mechanism_id: row.source_mechanism_id})
MATCH (natp:NonAffiliatedThirdParty {industry_standard_regulation_id: 'GLBA 1999', entity_id: row.target_entity_id})
MERGE (oom)-[:OPT_OUT_MECHANISM_APPLIES_TO_THIRD_PARTY {
    type: row.relationship_type,
    description: row.description
}]->(natp);
"""

#SecurityBreach → Requirement
breach_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sb:SecurityBreach {industry_standard_regulation_id: 'GLBA 1999', breach_id: row.source_breach_id})
MATCH (r:Requirement {industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.target_requirement_id})
MERGE (sb)-[:SECURITY_BREACH_TRIGGERS_NOTIFICATION {
    type: row.relationship_type,
    description: row.description
}]->(r);
"""
#Requirement → ServiceProvider
requirement_service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.source_requirement_id})
MATCH (sp:ServiceProvider {industry_standard_regulation_id: 'GLBA 1999', sp_id: row.target_sp_id})
MERGE (r)-[:REQUIREMENT_REQUIRES_OVERSIGHT_OF_SERVICE_PROVIDER {
    type: row.relationship_type,
    description: row.description
}]->(sp);
"""
#Requirement → SocialEngineeringTactic
requirement_social_engineering = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {industry_standard_regulation_id: 'GLBA 1999', requirement_id: row.source_requirement_id})
MATCH (set:SocialEngineeringTactic {industry_standard_regulation_id: 'GLBA 1999', tactic_id: row.target_tactic_id})
MERGE (r)-[:REQUIREMENT_PROHIBITS_TACTIC {
    type: row.relationship_type,
    description: row.description
}]->(set);
"""

orphan_privacy_notice = """
MATCH (orphan:PrivacyNotice) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'GLBA 1999'})
MERGE (reg)-[:REGULATION_MANDATES_PRIVACY_NOTICE]->(orphan);
"""

orphan_opt_out = """
MATCH (orphan:OptOutMechanism) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'GLBA 1999'})
MERGE (reg)-[:REGULATION_REQUIRES_OPT_OUT_MECHANISM]->(orphan);
"""
orphan_threat = """
MATCH (orphan:Threat) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'GLBA 1999'})
MERGE (reg)-[:REGULATION_IDENTIFIES_SECURITY_THREAT]->(orphan);
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

client.query(regulation)
time.sleep(2)

client.query(rule.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Rule.csv"))
time.sleep(2)

client.query(section.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Section.csv"))
time.sleep(2)


client.query(requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Requirement.csv"))
time.sleep(2)


client.query(role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Role.csv"))
time.sleep(2)


client.query(datacategory.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Data%20Category.csv"))
time.sleep(2)


client.query(eventype.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Event%20types.csv"))
time.sleep(2)

client.query(safeguard.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Safeguard.csv"))
time.sleep(2)


client.query(enforcement_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Enforcement%20Action.csv"))
time.sleep(2)


client.query(policy.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Policy.csv"))
time.sleep(2)


client.query(control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Control.csv"))
time.sleep(2)


client.query(system.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20System.csv"))
time.sleep(2)


client.query(process.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Process.csv"))
time.sleep(2)



client.query(qualified_individual.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/QualifiedIndividual.csv"))
time.sleep(2)


client.query(board_of_directors.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/BoardOfDirectors.csv"))
time.sleep(2)

client.query(service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/ServiceProvider.csv"))
time.sleep(2)

client.query(risk_assessment.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/RiskAssessment.csv"))
time.sleep(2)

client.query(threat.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/Threat.csv"))
time.sleep(2)

client.query(asset.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/Asset.csv"))
time.sleep(2)

client.query(privacy_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/PrivacyNotice.csv"))
time.sleep(2)

client.query(opt_out_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/OptOutMechanism.csv"))
time.sleep(2)

client.query(non_affiliated_third_party.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/NonAffiliatedThirdParty.csv"))
time.sleep(2)

client.query(security_breach.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/SecurityBreach.csv"))
time.sleep(2)

client.query(social_engineering_tactic.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/SocialEngineeringTactic.csv"))
time.sleep(2)


#relationships
client.query(regulation_rule) 
time.sleep(2)

client.query(rule_section)
time.sleep(2)

client.query(section_requirement)
time.sleep(2)

client.query(requirement_role)
time.sleep(2)

client.query(requirement_datacategory)
time.sleep(2)

client.query(requirement_event_type)
time.sleep(2)

client.query(requirement_safeguard)
time.sleep(2)

client.query(requirement_policy)
time.sleep(2)

client.query(requirement_control)
time.sleep(2)


client.query(control_system)
time.sleep(2)

client.query(requirement_process)
time.sleep(2)

client.query(role_role)
time.sleep(2)

client.query(requirement_enforcement_action)
time.sleep(2)

client.query(requirement_qualified_individual.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/Requirement_QualifiedIndividual_rel.csv"))
time.sleep(2)

client.query(qualified_individual_board.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/QualifiedIndividual_BoardOfDirectors_rel.csv"))
time.sleep(2)

client.query(risk_assessment_asset.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/RiskAssessment_Asset_rel.csv"))
time.sleep(2)

client.query(risk_assessment_threat.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/RiskAssessment_Threat_rel.csv"))
time.sleep(2)

client.query(safeguard_threat.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/Safeguard_Threat_rel.csv"))
time.sleep(2)

client.query(requirement_privacy_notice.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/Requirement_PrivacyNotice_rel.csv"))
time.sleep(2)

client.query(privacy_notice_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/PrivacyNotice_OptOutMechanism_rel.csv"))
time.sleep(2)

client.query(opt_out_third_party.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/OptOutMechanism_NonAffiliatedThirdParty_rel.csv"))
time.sleep(2)

client.query(breach_requirement.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/SecurityBreach_Requirement_rel.csv"))
time.sleep(2)

client.query(requirement_service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Requirement%20Service%20Provider.csv"))
time.sleep(2)

client.query(requirement_social_engineering.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA%20-%20Requirement%20Social%20EngineeringTactic.csv"))
time.sleep(2)

client.query(orphan_privacy_notice)
time.sleep(2)

client.query(orphan_opt_out)
time.sleep(2)

client.query(orphan_threat)
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
    with open('glba.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to glba.json")
else:
    logger.error("No data returned from the query.")

client.close()
