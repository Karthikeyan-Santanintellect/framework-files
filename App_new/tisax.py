#Regulation
regulation = """
MERGE (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 2.8'})
ON CREATE SET
    reg.name = "Trusted Information Security Assessment Exchange",
    reg.version = "TISAX Participant Handbook 2.8 (ISA 5)",
    reg.status = "Active",
    reg.jurisdiction = "Automotive industry, primarily Europe",
    reg.effective_date = date("2025-03-13"),
    reg.enactment_date = date("2017-01-01"),
    reg.description = "Information security assessment and exchange scheme for the automotive industry, based on ISO/IEC 27001 and sector-specific requirements. Managed by the ENX Association and using the VDA Information Security Assessment (ISA) catalogue, it provides graded assessment levels and TISAX labels so manufacturers, suppliers, and service providers can demonstrate and share their information security maturity in a standardized way.";
"""

#assessment_level
# CSV: level_id,name,description,self_assessment,evidence,interviews,on_site_inspection,label_validity_years
assessment_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (al:AssessmentLevel {industry_standard_regulation_id: 'TISAX 2.8', assessment_level_id: row.level_id})
ON CREATE SET
  al.name                  = row.name,
  al.description           = row.description,
  al.self_assessment       = row.self_assessment,
  al.evidence              = row.evidence,
  al.interviews            = row.interviews,
  al.on_site_inspection    = row.on_site_inspection,
  al.label_validity_years  = row.label_validity_years;
"""

#Assessment_objective
# CSV: objective_id,number,name,description,isa_criteria_catalogues,assessment_level,catalogue_group
assessment_objective = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ao:AssessmentObjective {industry_standard_regulation_id: 'TISAX 2.8', assessment_objective_id: row.objective_id})
ON CREATE SET
  ao.number                 = toInteger(row.number),
  ao.name                   = row.name,
  ao.description            = row.description,
  ao.isa_criteria_catalogues = row.isa_criteria_catalogues,
  ao.assessment_level       = row.assessment_level,
  ao.catalogue_group        = row.catalogue_group;
"""

#LABEL_HIERARCHY (AssessmentObjective -> AssessmentObjective)
# CSV: source_objective_id,relationship_type,target_objective_id,source_label,target_label
label_hierarchy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (src:AssessmentObjective {assessment_objective_id: row.source_objective_id})
MATCH (tgt:AssessmentObjective {assessment_objective_id: row.target_objective_id})
MERGE (src)-[r:SUPERSET_OF]->(tgt)
ON CREATE SET
  r.type         = row.relationship_type,
  r.source_label = row.source_label,
  r.target_label = row.target_label;
"""

#audit_provider
# CSV: provider_id,provider_name,registration_number,accreditation_status,accreditation_date,
#      accreditation_expiry,supported_assessment_levels,geographic_coverage,industry_specialization,
#      max_concurrent_assessments,average_audit_duration_days,certification_count,quality_rating,
#      contact_person,website
audit_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ap:AuditProvider {industry_standard_regulation_id: 'TISAX 2.8', audit_provider_id: row.provider_id})
ON CREATE SET
  ap.name                         = row.provider_name,
  ap.registration_number          = row.registration_number,
  ap.accreditation_status         = row.accreditation_status,
  ap.accreditation_date           = row.accreditation_date,
  ap.accreditation_expiry         = row.accreditation_expiry,
  ap.supported_assessment_levels  = row.supported_assessment_levels,
  ap.geographic_coverage          = row.geographic_coverage,
  ap.industry_specialization      = row.industry_specialization,
  ap.max_concurrent_assessments   = row.max_concurrent_assessments,
  ap.average_audit_duration_days  = row.average_audit_duration_days,
  ap.certification_count          = row.certification_count,
  ap.quality_rating               = row.quality_rating,
  ap.contact_person               = row.contact_person,
  ap.website                      = row.website;
"""

#ISA_catalogue
# CSV: catalogue_id,number,name,description
isa_catalogue = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ic:ISACatalogue {industry_standard_regulation_id: 'TISAX 2.8', isa_catalogue_id: row.catalogue_id})
ON CREATE SET
  ic.number      = toInteger(row.number),
  ic.name        = row.name,
  ic.description = row.description;
"""

#control_question (header-only CSV by design - loads zero rows)
# CSV: question_id,sequence_number,question_text,question_category,criticality,applies_to_al1,
#      applies_to_al2,applies_to_al3,expected_evidence_types,maturity_levels,typical_response_options,
#      guidance_url,last_revision_date,related_control_ids
control_question = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cq:ControlQuestion {industry_standard_regulation_id: 'TISAX 2.8', control_question_id: row.question_id})
ON CREATE SET
  cq.sequence_number           = row.sequence_number,
  cq.question_text             = row.question_text,
  cq.question_category         = row.question_category,
  cq.criticality               = row.criticality,
  cq.applies_to_al1            = row.applies_to_al1,
  cq.applies_to_al2            = row.applies_to_al2,
  cq.applies_to_al3            = row.applies_to_al3,
  cq.expected_evidence_types   = row.expected_evidence_types,
  cq.maturity_levels           = row.maturity_levels,
  cq.typical_response_options  = row.typical_response_options,
  cq.guidance_url              = row.guidance_url,
  cq.last_revision_date        = row.last_revision_date,
  cq.related_control_ids       = row.related_control_ids;
"""

#Protection Object
# CSV: object_id,name,type,classification,protection_level,is_sensitive,data_categories_contained,
#      owner_department,criticality_to_business,location,last_assessment_date,
#      protection_controls_implemented,remaining_risk
protection_object = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (po:ProtectionObject {industry_standard_regulation_id: 'TISAX 2.8', protection_object_id: row.object_id})
ON CREATE SET
  po.name                       = row.name,
  po.type                       = row.type,
  po.classification             = row.classification,
  po.protection_level           = row.protection_level,
  po.is_sensitive               = row.is_sensitive,
  po.data_categories_contained  = row.data_categories_contained,
  po.owner_department           = row.owner_department,
  po.criticality_to_business    = row.criticality_to_business,
  po.location                   = row.location,
  po.last_assessment_date       = row.last_assessment_date,
  po.protection_controls_implemented = row.protection_controls_implemented,
  po.remaining_risk             = row.remaining_risk;
"""

#Assessment_result
# CSV: result_id,certification_date,validity_start,validity_end,assessment_level_achieved,
#      overall_compliance_percentage,findings_critical_count,findings_major_count,findings_minor_count,
#      findings_observations_count,non_conformities,corrective_actions_required,label_status,
#      label_validity_months,auditor_name,auditor_sign_off_date,confidentiality_level,
#      result_documentation_url,issuing_body
assessment_result = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:AssessmentResult {industry_standard_regulation_id: 'TISAX 2.8', assessment_result_id: row.result_id})
ON CREATE SET
  ar.certification_date            = row.certification_date,
  ar.validity_start                = row.validity_start,
  ar.validity_end                  = row.validity_end,
  ar.assessment_level_achieved     = row.assessment_level_achieved,
  ar.overall_compliance_percentage = row.overall_compliance_percentage,
  ar.findings_critical_count       = row.findings_critical_count,
  ar.findings_major_count          = row.findings_major_count,
  ar.findings_minor_count          = row.findings_minor_count,
  ar.findings_observations_count   = row.findings_observations_count,
  ar.non_conformities              = row.non_conformities,
  ar.corrective_actions_required   = row.corrective_actions_required,
  ar.label_status                  = row.label_status,
  ar.label_validity_months         = row.label_validity_months,
  ar.auditor_name                  = row.auditor_name,
  ar.auditor_sign_off_date         = row.auditor_sign_off_date,
  ar.confidentiality_level         = row.confidentiality_level,
  ar.result_documentation_url      = row.result_documentation_url,
  ar.issuing_body                  = row.issuing_body;
"""

#Exchange_node
# CSV: exchange_id,name,description,operator,status
exchange_node = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ex:TisaxExchange {industry_standard_regulation_id: 'TISAX 2.8', exchange_id: row.exchange_id})
ON CREATE SET
  ex.name        = row.name,
  ex.description = row.description,
  ex.operator    = row.operator,
  ex.status      = row.status;
"""

#Control_category
# CSV: category_id,name,description,code,display_order,focus_area,is_new_in_v6,total_controls_count
control_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cc:ControlCategory {industry_standard_regulation_id: 'TISAX 2.8', category_id: row.category_id})
ON CREATE SET
  cc.name = row.name,
  cc.description = row.description,
  cc.code = row.code,
  cc.display_order = toInteger(row.display_order),
  cc.focus_area = row.focus_area,
  cc.total_controls = toInteger(row.total_controls_count);
"""

#Role
# CSV: role_id,role_title,description,key_responsibilities,qualification_requirements,is_mandatory,
#      reporting_line,typical_department
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rl:Role {industry_standard_regulation_id: 'TISAX 2.8', role_id: row.role_id})
ON CREATE SET
  rl.title               = row.role_title,
  rl.description         = row.description,
  rl.responsibilities    = row.key_responsibilities,
  rl.qualification_reqs  = row.qualification_requirements,
  rl.is_mandatory        = toBoolean(row.is_mandatory),
  rl.reporting_line      = row.reporting_line,
  rl.typical_department  = row.typical_department;
"""

#Assessment_phase
# CSV: phase_id,name,description,sequence_order,typical_duration_weeks,required_inputs,
#      expected_deliverables,is_mandatory,process_owner
assessment_phase = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (aph:AssessmentPhase {industry_standard_regulation_id: 'TISAX 2.8', phase_id: row.phase_id})
ON CREATE SET
  aph.name               = row.name,
  aph.description        = row.description,
  aph.sequence_order     = toInteger(row.sequence_order),
  aph.typical_duration   = row.typical_duration_weeks,
  aph.required_inputs    = row.required_inputs,
  aph.deliverables       = row.expected_deliverables,
  aph.is_mandatory       = toBoolean(row.is_mandatory),
  aph.owner              = row.process_owner;
"""

#Finding
# CSV: finding_id,finding_type,description,severity_level,date_identified,auditor_comment,status,
#      remediation_deadline,root_cause_analysis,evidence_reference
finding = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fd:Finding {industry_standard_regulation_id: 'TISAX 2.8', finding_id: row.finding_id})
ON CREATE SET
  fd.type                 = row.finding_type,
  fd.description          = row.description,
  fd.severity             = row.severity_level,
  fd.date_identified      = row.date_identified,
  fd.auditor_comment      = row.auditor_comment,
  fd.status               = row.status,
  fd.remediation_deadline = row.remediation_deadline,
  fd.root_cause           = row.root_cause_analysis,
  fd.evidence_ref         = row.evidence_reference;
"""

#Relationships
#ISA -> control_question (header-only CSV by design - loads zero rows)
# CSV: source_catalogue_id,relationship_type,target_question_id,inclusion_date,applicability_level,
#      question_order,question_weight,response_required
ISA_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ic:ISACatalogue {isa_catalogue_id: row.source_catalogue_id})
MATCH (cq:ControlQuestion {control_question_id: row.target_question_id})
MERGE (ic)-[r:ISA_CONTROLS_CONTROL_QUESTION {type: row.relationship_type}]->(cq)
ON CREATE SET
  r.inclusion_date = row.inclusion_date,
  r.applicability_level = row.applicability_level,
  r.question_order = row.question_order,
  r.question_weight = row.question_weight,
  r.response_required = row.response_required;
"""

#Isa_catalogue_has_category
# CSV: source_catalogue_id,target_category_id,relationship_type,inclusion_date,is_mandatory
isa_catalogue_has_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ic:ISACatalogue {isa_catalogue_id: row.source_catalogue_id})
MATCH (cc:ControlCategory {category_id: row.target_category_id})
MERGE (ic)-[r:ISA_CATALOGUE_HAS_CATEGORY {type: row.relationship_type}]->(cc)
ON CREATE SET
  r.inclusion_date = row.inclusion_date,
  r.is_mandatory   = toBoolean(row.is_mandatory);
"""

#Assessment_result_contains_finding
# CSV: source_result_id,target_finding_id,relationship_type,impact_on_label,verification_method
assessment_result_contains_finding = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:AssessmentResult {assessment_result_id: row.source_result_id})
MATCH (fd:Finding {finding_id: row.target_finding_id})
MERGE (ar)-[r:ASSESSMENT_RESULT_CONTAINS_FINDING {type: row.relationship_type}]->(fd)
ON CREATE SET
  r.impact_on_label     = row.impact_on_label,
  r.verification_method = row.verification_method;
"""

#Orphan_assessment_phase
orphan_assessment_phase = """
MATCH (orphan:AssessmentPhase) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 2.8'})
MERGE (reg)-[:TISAX_PRESCRIBES_PHASE]->(orphan);
"""

#Orphan_audit_provider
orphan_audit_provider = """
MATCH (orphan:AuditProvider) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 2.8'})
MERGE (reg)-[:TISAX_ACCREDITS_PROVIDER]->(orphan);
"""

#Orphan_role
orphan_role = """
MATCH (orphan:Role) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 2.8'})
MERGE (reg)-[:TISAX_DEFINES_ROLE]->(orphan);
"""

#Orphan_assessment_level
orphan_assessment_level = """
MATCH (orphan:AssessmentLevel) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:IndustryStandardAndRegulation {industry_standard_regulation_id: 'TISAX 2.8'})
MERGE (reg)-[:TISAX_DEFINES_ASSESSMENT_LEVEL]->(orphan);
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

#Nodes
client.query(regulation)
time.sleep(2)

client.query(assessment_level.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_AssessmentLevel_nodes.csv'))
time.sleep(2)

client.query(assessment_objective.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_AssessmentObjective_nodes.csv'))
time.sleep(2)

client.query(label_hierarchy.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_LABEL_HIERARCHY_relationships.csv'))
time.sleep(2)

client.query(audit_provider.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_AuditProvider_nodes.csv'))
time.sleep(2)

client.query(isa_catalogue.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_ISACatalogue_nodes.csv'))
time.sleep(2)

client.query(control_question.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_ControlQuestion_nodes.csv'))
time.sleep(2)

client.query(protection_object.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_ProtectionObject_nodes.csv'))
time.sleep(2)

client.query(assessment_result.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_AssessmentResult_nodes.csv'))
time.sleep(2)

client.query(exchange_node.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_Exchange_nodes.csv'))
time.sleep(2)

client.query(control_category.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/control_categories.csv"))
time.sleep(2)

client.query(role.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/roles.csv"))
time.sleep(2)

client.query(assessment_phase.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/assessment_phases.csv"))
time.sleep(2)

client.query(finding.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/findings.csv"))
time.sleep(2)

#Relationships
client.query(ISA_control.replace('$file_path', 'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX_ISA_CONTAINS_QUESTIONS.csv'))
time.sleep(2)

client.query(isa_catalogue_has_category.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX%20-%20ISA%20Catalogue%20Control%20Category.csv"))
time.sleep(2)

client.query(assessment_result_contains_finding.replace('$file_path', "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/TISAX/TISAX%20-%20Assement%20Result%20Findings.csv"))
time.sleep(2)

client.query(orphan_assessment_phase)
time.sleep(2)

client.query(orphan_audit_provider)
time.sleep(2)

client.query(orphan_role)
time.sleep(2)

client.query(orphan_assessment_level)
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

# results = client.query(query)

# if results and len(results) > 0:
#     graph_data = results[0]['graph_data']
#
#     import json
#     with open('tisax.json', 'w', encoding='utf-8') as f:
#         f.write(json.dumps(graph_data, default=str, indent=2))
#     logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to tisax.json")
# else:
#     logger.error("No data returned from the query.")

client.close()
