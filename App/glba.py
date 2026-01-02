'GLBA 1999'#Regulation
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

#Regulation → Rule
regulation_rule ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (i:IndustryStandardAndRegulation{industry_standard_regulation_id:'GLBA 1999'})
MATCH (ru:Rule{industry_standard_regulation_id: 'GLBA 1999',rule_id:row.target_rule_id})
MERGE (i)-[:REGULATION_HAS_RULE{type:row.relationship_type}]->(ru);
"""
#Rule → Section
rule_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ru:Rule{industry_standard_regulation_id: 'GLBA 1999',rule_id:row.source_rule_id})
MATCH (sec:Section{industry_standard_regulation_id: 'GLBA 1999',section_id:row.target_section_id})
MERGE (ru)-[:RULE_HAS_SECTION{type:row.relationship_type}]->(sec);
"""
#Section → Requirement
section_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section{industry_standard_regulation_id: 'GLBA 1999',section_id:row.source_section_id})
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.target_requirement_id})
MERGE (sec)-[:SECTION_HAS_REQUIREMENT{type:row.relationship_type}]->(r);
"""
#Requirement → Role
requirement_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (ro:Role{industry_standard_regulation_id: 'GLBA 1999',role_id:row.target_role_id})
MERGE (r)-[:REQUIREMENT_APPLIES_TO_ROLE{type:row.relationship_type}]->(ro);
"""
#Requirement → DataCategory
requirement_datacategory = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (dc:DataCategory{industry_standard_regulation_id: 'GLBA 1999',data_id:row.target_data_id})
MERGE (r)-[:REQUIREMENT_APPLIES_TO_DATACATEGORY{type:row.relationship_type}]->(dc);
"""
#Requirement → EventType
requirement_event_type ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (et:EventType{industry_standard_regulation_id: 'GLBA 1999',event_id:row.target_eventtype_id})
MERGE (r)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE{type:row.relationship_type}]->(et);
"""
#Requirement → Safeguard
requirement_safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (s:Safeguard{industry_standard_regulation_id: 'GLBA 1999',safeguard_id:row.target_safeguard_id})
MERGE (r)-[:REQUIREMENT_REQUIRES_SAFEGUARD{type:row.relationship_type}]->(s);
"""
#Requirement → Policy
requirement_policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement {
  industry_standard_regulation_id: 'GLBA 1999',
  requirement_id: row.source_requirement_id
})
MATCH (po:Policy {
  industry_standard_regulation_id: 'GLBA 1999',
  policy_id: row.target_policy_id
})
MERGE (r)-[:REQUIREMENT_SUPPORTED_BY_POLICY {
  type: row.relationship_type
}]->(po);
"""

#Requirement → Control
requirement_control ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (co:Control{industry_standard_regulation_id: 'GLBA 1999',control_id:row.target_control_id})
MERGE (r)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL{type:row.relationship_type}]->(co);
"""
#Control → System
control_system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (co:Control{industry_standard_regulation_id: 'GLBA 1999',control_id:row.source_control_id})
MATCH (sys:System{industry_standard_regulation_id: 'GLBA 1999',system_id:row.target_system_id})
MERGE (co)-[:CONTROL_IMPLEMENTED_IN_SYSTEM{type:row.relationship_type}]->(sys);
"""
#Requirement → Process
requirement_process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (pr:Process{industry_standard_regulation_id: 'GLBA 1999',process_id:row.target_process_id})
MERGE (r)-[:REQUIREMENT_IMPACTS_PROCESS{type:row.relationship_type}]->(pr);
"""
#Role → Role (Customer → Financial Institution)
role_role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (src:Role{industry_standard_regulation_id: 'GLBA 1999',role_id:row.source_role_id})
MATCH (tgt:Role{industry_standard_regulation_id: 'GLBA 1999',role_id:row.target_role_id})
MERGE (src)-[:ROLE_HAS_ROLE{
    type:row.relationship_type,
    description:row.relationship_description
    }]->(tgt);
"""
#Requirement → EnforcementAction
requirement_enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Requirement{industry_standard_regulation_id: 'GLBA 1999',requirement_id:row.source_requirement_id})
MATCH (ea:EnforcementAction{industry_standard_regulation_id: 'GLBA 1999',enforcement_action_id:row.target_enforcement_id})
MERGE (r)-[:REQUIREMENT_ENFORCED_BY_ENFORCEMENT_ACTION{type:row.relationship_type}]->(ea);
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

client.query(rule.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Rule_nodes.csv'))
time.sleep(2)

client.query(section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Section_nodes.csv'))
time.sleep(2)

client.query(requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Requirement_nodes.csv'))
time.sleep(2)

client.query(role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Role_nodes.csv'))
time.sleep(2)

client.query(datacategory.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_DataCategory_nodes.csv'))
time.sleep(2)

client.query(eventype.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_EventType_nodes.csv'))
time.sleep(2)

client.query(safeguard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Safeguard_nodes.csv'))
time.sleep(2)

client.query(enforcement_action.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_EnforcementAction_nodes.csv'))
time.sleep(2)

client.query(policy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Policy_nodes.csv'))
time.sleep(2)

client.query(control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Control_nodes.csv'))
time.sleep(2)

client.query(system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_System_nodes.csv'))
time.sleep(2)

client.query(process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_Process_nodes.csv'))
time.sleep(2)




client.query(regulation_rule.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASRULE_relationships.csv'))  

client.query(rule_section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASSECTION_relationships.csv'))
time.sleep(2)

client.query(section_requirement.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASREQUIREMENT_relationships.csv'))
time.sleep(2)

client.query(requirement_role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_APPLIESTOROLE_relationships.csv'))
time.sleep(2)   

client.query(requirement_datacategory.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_APPLIESTODATA_relationships.csv'))
time.sleep(2)

client.query(requirement_event_type.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_TRIGGERSEVENTTYPE_relationships.csv'))
time.sleep(2)

client.query(requirement_safeguard.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_REQUIRESSAFEGUARD_relationships.csv'))
time.sleep(2)   

client.query(requirement_policy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_SUPPORTEDBYPOLICY_relationships.csv'))
time.sleep(2)   

client.query(requirement_control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_IMPLEMENTEDBYCONTROL_relationships.csv'))    
time.sleep(2)   

client.query(control_system.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_IMPLEMENTEDINSYSTEM_relationships.csv'))    
time.sleep(2)

client.query(requirement_process.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_IMPACTSPROCESS_relationships.csv'))
time.sleep(2)   

client.query(role_role.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_HASRELATIONSHIPWITH_relationships.csv'))
time.sleep(2)

client.query(requirement_enforcement_action.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GLBA/GLBA_ENFORCEDBY_relationships.csv'))
time.sleep(2)

 
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
with open('glba.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to glba.json")

client.close()

