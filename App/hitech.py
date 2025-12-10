# Regulation
regulation = """
MERGE (r:IndustryStandardAndRegulation {IS_framework_standard_id: "HITECH_ACT_2009"})
ON CREATE SET
  r.name = "Health Information Technology for Economic and Clinical Health Act",
  r.version = "2009",
  r.enactment_date = date("2009-02-17"),
  r.description = "U.S. legislation to promote the adoption and meaningful use of health information technology.";
"""
#title
title = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (t:Title {IS_framework_standard_id: "HITECH_ACT_2009",title_id: row.title_id})
ON CREATE SET
    t.name = row.title_name,
    t.description = row.title_description;
"""
#subtitle
subtitle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Subtitle {IS_framework_standard_id: "HITECH_ACT_2009",subtitle_id: row.subtitle_id})
ON CREATE SET
    s.title_id = row.title_id,
    s.name = row.subtitle_name,
    s.description = row.subtitle_description;
"""
#section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {IS_framework_standard_id: "HITECH_ACT_2009",section_id: row.section_id})
ON CREATE SET
    sec.subtitle_id = row.subtitle_id,
    sec.full_citation = row.full_citation,
    sec.heading = row.heading,
    sec.text = row.text,
    sec.topic = row.topic;
"""
#requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rq:Requirement {IS_framework_standard_id: "HITECH_ACT_2009",requirement_id: row.requirement_id})
ON CREATE SET
    rq.section_id = row.section_id,
    rq.text = row.text,
    rq.type = row.type,
    rq.priority = row.priority,
    rq.status = row.status;
"""
#role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {IS_framework_standard_id: "HITECH_ACT_2009",role_id: row.role_id})
ON CREATE SET
    ro.name = row.name,
    ro.description = row.description;
"""
#data_category
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:DataCategory {IS_framework_standard_id: "HITECH_ACT_2009",data_id: row.data_id})
ON CREATE SET
    d.name = row.name,
    d.description = row.description;
"""
#safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {IS_framework_standard_id: "HITECH_ACT_2009",safeguard_id: row.safeguard_id})
ON CREATE SET
    sg.name = row.name,
    sg.description = row.description,
    sg.type = row.type;
"""
#event_type
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {IS_framework_standard_id: "HITECH_ACT_2009",event_type_id: row.event_type_id})
ON CREATE SET
    et.name = row.name,
    et.description = row.description;
"""
#enforcement_action
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (e:EnforcementAction {IS_framework_standard_id: "HITECH_ACT_2009",enforcement_id: row.enforcement_id})
ON CREATE SET
    e.authority = row.authority,
    e.description = row.description,
    e.type = row.type;
"""
#incentive_program
incentive_program = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ip:IncentiveProgram {IS_framework_standard_id: "HITECH_ACT_2009",program_id: row.program_id})
ON CREATE SET
    ip.title_id = row.title_id,
    ip.name = row.name,
    ip.description = row.description,
    ip.payer = row.payer;
"""
#meaningful_use_criterion
meaningful_use_criterion = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (m:MeaningfulUseCriterion {IS_framework_standard_id: "HITECH_ACT_2009",criterion_id: row.criterion_id})
ON CREATE SET
    m.program_id = row.program_id,
    m.stage = row.stage,
    m.description = row.description;
"""
#implementation_spec
implementation_spec = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (i:ImplementationSpec {IS_framework_standard_id: "HITECH_ACT_2009",impl_id: row.impl_id})
ON CREATE SET
    i.name= row.name,
    i.description = row.description,
    i.owner = row.owner;
"""
#policy
policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:Policy {IS_framework_standard_id: "HITECH_ACT_2009",policy_id: row.policy_id})
ON CREATE SET
    po.name = row.name,
    po.description = row.description,
    po.owner = row.owner;
"""
#control
control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {IS_framework_standard_id: "HITECH_ACT_2009",control_id: row.control_id})
ON CREATE SET
    c.name = row.name,
    c.description = row.description,
    c.category = row.category;
"""
#system
system = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sy:System {IS_framework_standard_id: "HITECH_ACT_2009",system_id: row.system_id})
ON CREATE SET
    sy.name = row.name,
    sy.type = row.type,
    sy.owner = row.owner;
"""
#process
process = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Process {IS_framework_standard_id: "HITECH_ACT_2009",process_id: row.process_id})
ON CREATE SET
    p.name = row.name,
    p.description = row.description;
"""
#external_framewrork_requiremets
external_framework_requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (efr:ExternalFrameworkRequirements {IS_framework_standard_id: "HITECH_ACT_2009",external_framework_requirement_id: row.external_framework_requirement_id})
ON CREATE SET
    efr.requirement_id = row.requirement_id,
    efr.source_framework = row.source_framework,
    efr.text = row.text;
"""
#regulation_title_rel
regulation_title_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:IndustryStandardAndRegulation {version:row.regulation_version, name: row.regulation_name})
MATCH (t:Title {id: row.title_id})
MERGE (r)-[:REGULATION_CONTAINS_TITLES]->(t);
"""
#title_subtitle_rel
title_subtitle_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (t:Title {id: row.title_id})
MATCH (s:Subtitle {id: row.subtitle_id})
MERGE (t)-[:TITLE_CONTAINS_SUBTITLES]->(s);
"""
#subtitle_section_rel
subtitle_section_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Subtitle {id: row.subtitle_id})
MATCH (sec:Section {id: row.section_id})
MERGE (s)-[:SUBTITLE_CONTAINS_SECTIONS]->(sec);
"""
#section_requirement_rel
section_requirement_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {id: row.section_id})
MATCH (rq:Requirement {id: row.requirement_id})
MERGE (sec)-[:SECTION_HAS_REQUIREMENTS]->(rq);
"""
#requirement_role_rel
requirement_role_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (ro:Role {id: row.role_id})
MERGE (rq)-[:REQUIREMENT_APPLIES_TO_ROLE]->(ro);
"""
#requirement_data_category_rel
requirement_data_category_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (d:DataCategory {id: row.data_id})
MERGE (rq)-[:REQUIREMENT_INCLUDES_DATA_CATEGORY]->(d);
"""
#requirement_safeguard_rel
requirement_safeguard_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (sg:Safeguard {id: row.safeguard_id})
MERGE (rq)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg);
"""
#requirement_event_type_rel
requirement_event_type_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (et:EventType {id: row.event_type_id})
MERGE (rq)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE]->(et);
"""
#requirement_policy_rel
requirement_policy_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (po:Policy {id: row.policy_id})
MERGE (rq)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(po);
"""
#requirement_control_rel
requirement_control_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (c:Control {id: row.control_id})
MERGE (rq)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(c);
"""
#control_system_rel
control_system_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {id: row.control_id})
MATCH (sy:System {id: row.system_id})
MERGE (c)-[:CONTROL_IMPLEMENTED_IN_SYSTEM]->(sy);
"""
#requirement_process_rel
requirement_process_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (p:Process {id: row.process_id})
MERGE (rq)-[:REQUIREMENT_IMPACTS_PROCESS]->(p);
"""
#title_incentive_program_rel
title_incentive_program_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (t:Title {id: row.title_id})
MATCH (ip:IncentiveProgram {id: row.program_id})
MERGE (t)-[:TITLE_ESTABLISHED_INCENTIVE_PROGRAM]->(ip);
"""
#incentive_program_meaningful_use_criterion_rel
incentive_program_meaningful_use_criterion_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ip:IncentiveProgram {id: row.program_id})
MATCH (m:MeaningfulUseCriterion {id: row.criterion_id})
MERGE (ip)-[:INCENTIVE_PROGRAM_USES_MEANINGFUL_USE_CRITERION]->(m);
"""
#requirement_meaningful_use_criterion_rel
requirement_meaningful_use_criterion_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (m:MeaningfulUseCriterion {id: row.criterion_id})
MERGE (rq)-[:REQUIREMENT_DRIVES_MEANINGFUL_USE_CRITERION]->(m);
"""
#requirement_enforcement_action_rel
requirement_enforcement_action_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (e:EnforcementAction {id: row.enforcement_id})
MERGE (rq)-[:REQUIREMENT_SUBJECT_TO_ENFORCEMENT_ACTION]->(e);
"""
#section_enforcement_action_rel
section_enforcement_action_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {id: row.section_id})
MATCH (e:EnforcementAction {id: row.enforcement_id})
MERGE (sec)-[:SECTION_SUBJECT_TO_ENFORCEMENT_ACTION]->(e);
"""
#requirements_implementation_spec_rel
requirements_implementation_spec_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.requirement_id})
MATCH (i:ImplementationSpec {id: row.impl_id})
MERGE (rq)-[:REQUIREMENT_HAS_IMPLEMENTATION_SPEC]->(i);
"""
#implementation_spec_control_rel
implementation_spec_control_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (i:ImplementationSpec {id: row.impl_id})
MATCH (c:Control {id: row.control_id})
MERGE (i)-[:IMPLEMENTATION_SPEC_INCLUDES_CONTROL]->(c);
"""
#policy_control_rel
policy_control_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (po:Policy {id: row.policy_id})
MATCH (c:Control {id: row.control_id})
MERGE (po)-[:POLICY_ENFORCES_CONTROL]->(c);
"""
#process_system_rel
process_system_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (p:Process {id: row.process_id})
MATCH (sy:System {id: row.system_id})
MERGE (p)-[:PROCESS_INVOLVES_SYSTEM]->(sy);
"""
#requirement_external_framework_requirements_rel
requirement_external_framework_requirements_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (rq:Requirement {id: row.source_requirement_id})
MATCH (efr:ExternalFrameworkRequirements {id: row.target_requirement_id})
MERGE (rq)-[:REQUIREMENT_MAPS_TO_EXTERNAL_FRAMEWORK_REQUIREMENT{strength: row.strength,
justification:row.justification,source:row.source}]->(efr);
"""
#control_control_rel
control_control_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {id: row.source_control_id})
MATCH (c:Control {id: row.target_control_id})
MERGE (c)-[:CONTROL_MAPPED_TO_CONTROL{strength: row.strength,
justification:row.justification,source:row.source}]->(c);
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

client.query(title.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_functions.csv'))
time.sleep(2)

client.query(subtitle.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_categories.csv'))
time.sleep(2)

client.query(section.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/NIST%20AI%20RMF/ai_rmf_subcategories.csv'))
time.sleep(2)

client.query(requirement.replace)
time.sleep(2)

client.query(role)
time.sleep(2)

client.query(data_category.replace)
time.sleep(2)

client.query(safeguard.replace)
time.sleep(2)

client.query(event_type.replace)
time.sleep(2)

client.query(enforcement_action.replace)
time.sleep(2)

client.query(incentive_program.replace)
time.sleep(2)

client.query(meaningful_use_criterion.replace)
time.sleep(2)

client.query(implementation_spec.replace)
time.sleep(2)

client.query(policy.replace)
time.sleep(2)

client.query(control.replace)
time.sleep(2)

client.query(system.replace)
time.sleep(2)


client.query(process.replace)
time.sleep(2)

client.query(external_framework_requirements.replace)
time.sleep(2)

client.query(regulation_title_rel.replace)
time.sleep(2)

client.query(title_subtitle_rel.replace)
time.sleep(2)

client.query(subtitle_section_rel.replace)
time.sleep(2)   

client.query(section_requirement_rel.replace)
time.sleep(2)

client.query(requirement_role_rel.replace)
time.sleep(2)

client.query(requirement_data_category_rel.replace)
time.sleep(2)   

client.query(requirement_safeguard_rel.replace)
time.sleep(2)   

client.query(requirement_event_type_rel.replace)    
time.sleep(2)   

client.query(requirement_policy_rel.replace)    
time.sleep(2)

client.query(requirement_control_rel.replace)
time.sleep(2)   

client.query(control_system_rel.replace)
time.sleep(2)

client.query(requirement_process_rel.replace)
time.sleep(2)

client.query(title_incentive_program_rel.replace)
time.sleep(2)

client.query(incentive_program_meaningful_use_criterion_rel.replace)
time.sleep(2)

client.query(requirement_meaningful_use_criterion_rel.replace)
time.sleep(2)

client.query(requirement_enforcement_action_rel.replace)
time.sleep(2)

client.query(section_enforcement_action_rel.replace)
time.sleep(2)

client.query(requirements_implementation_spec_rel.replace)
time.sleep(2)

client.query(implementation_spec_control_rel.replace)
time.sleep(2)

client.query(policy_control_rel.replace)
time.sleep(2)

client.query(process_system_rel.replace)
time.sleep(2)

client.query(requirement_external_framework_requirements_rel.replace)
time.sleep(2)   

client.query(control_control_rel.replace)
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
with open('nist-ai-rmf.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, default=str, indent=2))
logger.info("✓ Exported graph data to nist-ai-rmf.json")


client.close()










