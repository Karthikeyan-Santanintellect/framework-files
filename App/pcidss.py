# Create PCIDSS Standard Node
standard = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_standard.csv' AS row
MERGE (s:Standard {standard_id: 'PCI-DSS'})
ON CREATE SET
  s.name =  row.name,
  s.version = row.version,
  s.publication_date = date(row.publication_date),
  s.retirement_date = date(row.retirement_date),
  s.effective_date = date(row.effective_date),
  s.mandatory_date_future = date(row.mandatory_date_future),
  s.revision_type = row.revision_type;
"""
//Organization Nodes
organization = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_organization.csv' AS row
MERGE (o:Organization {name: row.name})
ON CREATE SET
  o.type = row.type,
  o.founded = date(row.founded),
  o.headquarters = row.headquarters,
  o.website =  row.website,
  o.purpose =  row.purpose;
"""
//  RequirementGroup Nodes
requirement_group = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_requirement_group.csv' AS row
MERGE (rg:RequirementGroup {group_id:row.group_id})
ON CREATE SET
  name = row.name;
"""
//  Requirement Nodes
requirement ="""
LOAD CSV WITH HEADERS FROM 'file:///nodes_requirement.csv' AS row
MERGE (r:Requirement {req_id: toInteger(row.req_id)
ON CREATE SET
  r.name = row.name,
  r.requirement_group = row.requirement_group;
"""
// SubRequirement Nodes 
sub_requirement = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_subrequirement.csv' AS row
MERGE (sr:SubRequirement {req_id: row.req_id})
ON CREATE SET
  sr.name = row.name,
  sr.req_id = row.req_id,
  sr.milestone = toInteger(row.milestone),
  sr.becomes_mandatory_on = date(row.becomes_mandatory_on);
"""
// DefinedApproach Nodes 
defined_approach ="""
LOAD CSV WITH HEADERS FROM 'file:///nodes_defined_approach.csv' AS row
MERGE (da:DefinedApproach {req_id: row.req_id}
ON CREATE SET
  da.name = row.name;
"""
// TestingProcedure Nodes 
testing_procedure ="""
LOAD CSV WITH HEADERS FROM 'file:///nodes_testing_procedure.csv' AS row
MERGE (tp:TestingProcedure {test_id: row.test_id}
ON CREATE SET
  tp.name = row.name,
  tp.related_defined_approach = row.related_defined_approach;
"""
// CustomizedApproachObjective Nodes 
customized_approach_objective = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_customized_approach_objective.csv' AS row
MERGE (cao:CustomizedApproachObjective {req_id: row.req_id}
ON CREATE SET
  cao.name = row.name;
"""
//  TargetedRiskAnalysis Nodes
target_risk_analysis ="""
LOAD CSV WITH HEADERS FROM 'file:///nodes_targeted_risk_analysis.csv' AS row
MERGE (tra:TargetedRiskAnalysis {tra_id: row.tra_id}
ON CREATE SET
  tra.name = row.name,
  tra.type = row.type,
  tra.status = row.status,
  tra.owner = row.owner,
  tra.date_completed = date(row.date_completed),
  tra.related_req_id = row.related_req_id;
"""
//  CustomizedControl Nodes 
customized_control = """
LOAD CSV WITH HEADERS FROM 'file:///nodes_customized_control.csv' AS row
MERGE (cc:CustomizedControl {control_id: row.control_id}
ON CREATE SET
  cc.name = row.name,
  cc.description = row.description,
  cc.owner = row.owner,
  cc.implementation_date = date(row.implementation_date)
  cc.related_objective_req_id = row.related_objective_req_id;
"""
//  Guidance Nodes
guidance ="""
LOAD CSV WITH HEADERS FROM 'file:///nodes_guidance.csv' AS row
MERGE (g:Guidance {guidance_id: row.guidance_id}
ON CREATE SET
  g.name = row.name,
  g.related_subrequirement = row.related_subrequirement;
"""

// 1. PUBLISHES (Organization -> Standard) 
pcidss_publishes ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_publishes.csv' AS row
MATCH (o:Organization {name: row.source_name})
MATCH (s:Standard {name: row.target_name, version: row.target_version})
MERGE (o)-[:PUBLISHES]->(s);
"""
// 2. IS_REVISION_OF (Standard -> Standard) 
pcidss_IS_revision_of ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_is_revision_of.csv' AS row
MATCH (source:Standard {version: row.source_version})
MATCH (target:Standard {version: row.target_version})
MERGE (source)-[:IS_REVISION_OF {revision_type: row.revision_type}]->(target);
"""

// 3. SUPERSEDES (Standard -> Standard) 
pcidss_superedes = """
LOAD CSV WITH HEADERS FROM 'file:///relationships_supersedes.csv' AS row
MATCH (source:Standard {version: row.source_version})
MATCH (target:Standard {version: row.target_version})
MERGE (source)-[:SUPERSEDES {supersede_date: date(row.supersede_date)}]->(target);
"""
// 4. HAS_GROUP (Standard -> RequirementGroup) 
pcidss_has_group ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_group.csv' AS row
MATCH (s:Standard {version: row.source_standard_version})
MATCH (rg:RequirementGroup {group_id: row.target_group_id})
MERGE (s)-[:HAS_GROUP]->(rg);
"""

// 5. HAS_REQUIREMENT (RequirementGroup -> Requirement) 
pcidss_has_requirement ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_requirement.csv' AS row
MATCH (rg:RequirementGroup {group_id: row.source_group_id})
MATCH (r:Requirement {req_id: toInteger(row.target_req_id)})
MERGE (rg)-[:HAS_REQUIREMENT]->(r);
"""
// 6. HAS_SUB_REQUIREMENT (Requirement -> SubRequirement) 
pcidss_has_sub_requirement = """
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_sub_requirement.csv' AS row
MATCH (r:Requirement {req_id: toInteger(row.source_req_id)})
MATCH (sr:SubRequirement {req_id: row.target_subreq_id})
MERGE (r)-[:HAS_SUB_REQUIREMENT]->(sr);
"""
// 7. HAS_DEFINED_APPROACH (SubRequirement -> DefinedApproach) 
pcidss_has_defined_approach = """
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_defined_approach.csv' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id})
MATCH (da:DefinedApproach {req_id: row.target_defined_approach_id})
MERGE (sr)-[:HAS_DEFINED_APPROACH]->(da);
"""

// 8. HAS_TEST (DefinedApproach -> TestingProcedure) 
pcidss_has_test ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_test.csv' AS row
MATCH (da:DefinedApproach {req_id: row.source_defined_approach_id})
MATCH (tp:TestingProcedure {test_id: row.target_test_id})
MERGE (da)-[:HAS_TEST]->(tp);
"""

// 9. HAS_CUSTOMIZED_OBJECTIVE (SubRequirement -> CustomizedApproachObjective) 
pcidss_has_customized_objective ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_customized_objective.csv' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id})
MATCH (cao:CustomizedApproachObjective {req_id: row.target_customized_objective_id})
MERGE (sr)-[:HAS_CUSTOMIZED_OBJECTIVE]->(cao);
"""
// 10. HAS_GUIDANCE (SubRequirement -> Guidance) 
pcidss_has_guidance = """
LOAD CSV WITH HEADERS FROM 'file:///relationships_has_guidance.csv' AS row
MATCH (sr:SubRequirement {req_id: row.source_subreq_id})
MATCH (g:Guidance {guidance_id: row.target_guidance_id})
MERGE (sr)-[:HAS_GUIDANCE]->(g);
"""

// 11. REQUIRES_TRA (CustomizedApproachObjective -> TargetedRiskAnalysis) 
pcidss_requires_tra = """
LOAD CSV WITH HEADERS FROM 'file:///relationships_requires_tra.csv' AS row
MATCH (cao:CustomizedApproachObjective {req_id: row.source_customized_objective_id})
MATCH (tra:TargetedRiskAnalysis {tra_id: row.target_tra_id})
MERGE (cao)-[:REQUIRES_TRA]->(tra);
"""

// 12. VALIDATES (TargetedRiskAnalysis -> CustomizedControl) 
pcidss_validates ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_validates.csv' AS row
MATCH (tra:TargetedRiskAnalysis {tra_id: row.source_tra_id})
MATCH (cc:CustomizedControl {control_id: row.target_control_id})
MERGE (tra)-[:VALIDATES]->(cc);
"""

// 13. ADDRESSES (CustomizedControl -> CustomizedApproachObjective) 
pcidss_addresses ="""
LOAD CSV WITH HEADERS FROM 'file:///relationships_addresses.csv' AS row
MATCH (cc:CustomizedControl {control_id: row.source_control_id})
MATCH (cao:CustomizedApproachObjective {req_id: row.target_customized_objective_id})
MERGE (cc)-[:ADDRESSES]->(cao);
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

client.query(standard)
time.sleep(2)

client.query(organization.replace('$file_path',
                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Framework.csv"))
time.sleep(2)

client.query(requirement_group.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Recital.csv"))
time.sleep(2)


client.query(requirement.replace('$file_path',
                                               "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Chapter.csv"))
time.sleep(2)

client.query(sub_requirement.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Article.csv"))
time.sleep(2)

client.query(defined_approach.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Concept.csv"))
time.sleep(2)

client.query(testing_procedure.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_LegislativeAction.csv"))
time.sleep(2)

client.query(customized_approach_objective.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Paragraph.csv"))
time.sleep(2)

client.query(target_risk_analysis.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Paragraph.csv"))
time.sleep(2)

client.query(customized_control.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Paragraph.csv"))
time.sleep(2)

client.query(guidance.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Paragraph.csv"))
time.sleep(2)



client.query(pcidss_publishes.replace('$file_path',
                                              "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/HAS_CHAPTER.csv"))
time.sleep(2)

client.query(pcidss_IS_revision_of.replace('$file_path',
                                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_ARTICLE.csv"))
time.sleep(2)

client.query(pcidss_superedes.replace('$file_path',
                                                            "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_PARAGRAPH.csv"))
time.sleep(2)

client.query(pcidss_has_group.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/PROVIDES_CONTEXT_FOR.csv"))
time.sleep(2)

client.query(pcidss_has_requirement.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/SPECIALIZES_PROVISIONS_OF.csv"))
time.sleep(2)

client.query(pcidss_has_sub_requirement.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/DEFINES_CONCEPT.csv"))
time.sleep(2)

client.query(pcidss_has_defined_approach.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/IMPLEMENTS_PRINCIPLE.csv"))
time.sleep(2)

client.query(pcidss_has_test.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/ESTABLISHES_CRITERIA.csv"))
time.sleep(2)

client.query(pcidss_has_customized_objective.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/MANDATES_REQUIREMENT.csv"))
time.sleep(2)

client.query(pcidss_has_guidance.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/DEFINES_RESPONSIBILITY.csv"))
time.sleep(2)

client.query(pcidss_requires_tra.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GOVERNS_PROCEDURE.csv"))
time.sleep(2)

client.query(pcidss_validates.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/REQUIRES_ACTION.csv"))
time.sleep(2)

client.query(pcidss_addresses.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/AFFECTS_PROVISION.csv"))
time.sleep(2)





logger.info("Graph structure loaded successfully.")

client.close()

