#Load Framework
framework ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {framework_id : 'SCF 2025'})
ON CREATE SET
  f.name = row.name,
  f.version = row.version,
  f.release_date = row.release_date,
  f.description = row.description,
  f.total_domains = toInteger(row.total_domains),
  f.total_controls = toInteger(row.total_controls),
  f.created_at = datetime()
 """
#Load Domain 
domain ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.domain_name,
    d.description = row.description,
    d.control_count = toInteger(row.control_count);
"""
#Load Controls
controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Control {control_id: row.control_id})
ON CREATE SET 
    c.control_name = row.control_name,
    c.control_description = row.control_text,
    c.domain_identifier = row.domain_identifier,
    c.PPTDF_scope = pptdf_list,
    c.control_question = row.control_question,
    c.relative_weighting = toInteger(row.relative_weighting),
    c.evidence_request_list = row.evidence_request_list,
    c.nist_csf_function = row.nist_csf_function,
    c.is_new_control = row.is_new_control,
    c.is_mcr = row.is_mcr,
    c.is_dsr = row.is_dsr,
    c.is_ma_d_applicable = row.is_ma_d_applicable;
"""
#Load External Controls
external_controls ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ec:ExternalControl {
    external_control_id: row.external_control_id,
    framework: row.framework})
ON CREATE SET 
    ec.framework_full_name = row.framework_full_name;
"""
#Load Business_guidance
business_guidance ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (bg:BusinessGuidance {
    control_id: row.control_id,
    business_size: row.business_size
})
ON CREATE SET 
    bg.guidance = row.guidance,
    bg.guidance_length = size(row.guidance),
    bg.guidance_word_count = size(split(row.guidance, ' ')),
    bg.created_at = datetime(),
    bg.data_source = row.data_source,
    bg.node_type = row.node_type;
"""

#Create Framework_Domain_relation
framework_domain_rel ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {name: row.framework_id, version: row.framework_version})
MATCH (d:Domain {identifier: row.domain_identifier})
MERGE (f)-[r:CONTAINS {relationship_type: row.relationship_type}]->(d)
ON CREATE SET 
    r.control_count = toInteger(row.control_count);
"""
#Create Domain_control_relation
domain_controls_rel="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (d:Domain {identifier: row.domain_identifier})
MATCH (c:Control {control_id: row.control_id})
MERGE (d)-[r:CONTAINS {relationship_type: row.relationship_type}]->(c)
ON CREATE SET 
    r.relative_weighting = toInteger(row.relative_weighting),
    r.pptdf_scope = row.pptdf_scope,
    r.is_new_control = row.is_new_control;
"""
#Create Control_external_controls_relation
control_external_control_rel="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {control_id: row.source_control_id})
MATCH (ec:ExternalControl {
    external_control_id: row.external_control_id,
    framework: row.framework
})
MERGE (c)-[r:MAPS_TO {relationship_type: row.relationship_type}]->(ec)
ON CREATE SET 
    r.created_at = datetime(),
    r.mapping_confidence = 'HIGH',
    r.relationship_sequence = 3;
"""
#Create Control_business_guidance relation
control_business_business_rel="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Control {control_id: row.source_control_id})
MATCH (bg:BusinessGuidance {
    control_id: row.source_control_id,
    business_size: row.business_size
})
MERGE (c)-[r:HAS_GUIDANCE {
    relationship_type: row.relationship_type,
    business_size: row.business_size
}]->(bg)
ON CREATE SET 
    r.guidance_length = toInteger(row.guidance_length),
    r.created_at = datetime();
"""



