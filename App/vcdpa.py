#Regulation
regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_and_regulation_id: 'vcdpa'})
ON CREATE SET
    reg.name = 'Virginia Consumer Data Protection Act (VCDPA)',
    reg.ciation = 'Va. Code Ann. §§ 59.1-571 to 59.1-575 (2023)',
    reg.version = '2023',
    reg.status = 'Active',
    reg.effective_date = date('2023-01-01'),
    reg.jurisdiction = 'Virginia, USA',
    reg.description = 'The Virginia Consumer Data Protection Act (VCDPA) is a comprehensive data privacy law that establishes consumer rights and data protection obligations for businesses operating in Virginia.',
    reg.url = 'https://law.lis.virginia.gov/vacode/title59.1/chapter52/section59.1-575/';
"""
#section
section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {regional_standard_and_regulation_section_id: 'vcdpa' , section_id: row.section_id})
ON CREATE SET
    sec.full_citation = row.full_citation,
    sec.heading = row.heading,
    sec.text = row.text,
    sec.topic = row.topic;
"""
#Requirement
requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (req:Requirement {regional_standard_and_regulation_id: 'vcdpa', requirement_id: row.requirement_id})
ON CREATE SET
    req.section_id = row.section_id,
    req.requirement_text = row.requirement_text,
    req.requirement_type = row.requirement_type,
    req.priority = row.priority,
    req.status = row.status,
    req.deadline = row.deadline,
    req.extendable = CASE WHEN row.extendable = 'Yes' THEN true ELSE false END,
    req.extension_period = row.extension_period;
"""
#Role
role = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ro:Role {regional_standard_and_regulation_id: 'vcdpa', role_id: row.role_id})
ON CREATE SET
    ro.name = row.name,
    ro.description = row.description,
    ro.threshold = row.threshold;
"""

#Data Category
data_category = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {regional_standard_and_regulation_id: 'vcdpa', data_id: row.data_id})
ON CREATE SET
    dc.type = row.category_type,
    dc.name = row.name,
    dc.description = row.description,
    dc.definition_section = row.definition_section,
    dc.requires_consent = CASE WHEN row.requires_consent = 'Yes' THEN true ELSE false END;
"""
#Event_Type
event_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (et:EventType {regional_standard_and_regulation_id: 'vcdpa', event_type_id: row.event_type_id})
ON CREATE SET
    et.name = row.name,
    et.description = row.description,
    et.deadline = row.deadline,
    et.extendable = CASE WHEN row.extendable = 'Yes' THEN true ELSE false END,
    et.extension_period = row.extension_period;
    et.cost = row.cost;
"""
#Safeguard
safeguard = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sg:Safeguard {regional_standard_and_regulation_id: 'vcdpa', safeguard_id: row.safeguard_id})
ON CREATE SET
    sg.name = row.name,
    sg.description = row.description,
    sg.type = row.type,
    sg.applies_to = row.applies_to_section;
"""
#enforcement_action
enforcement_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAction {regional_standard_and_regulation_id: 'vcdpa', id: row.enforcement_id})
ON CREATE SET
    ea.type = row.type,
    ea.authority = row.authority,
    ea.violation_amount = row.violation_amount,
    ea.description = row.description,
    ea.section = row.section,
    ea.cure_period = row.cure_period,
    ea.private_right_of action = CASE WHEN row.private_right_of_action = 'Yes' THEN true ELSE false END;
"""
#data_protection_assessment
data_protection_assessment = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dpa:DataProtectionAssessment {regional_standard_and_regulation_id: 'vcdpa', dpa_id: row.dpa_id})
ON CREATE SET
    dpa.trigger = row.trigger,
    dpa.description = row.description,
    dpa.section = row.section,
    dpa.required_elements = row.required_elements;
"""
#implementation_spec
implementation_spec = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ispec:ImplementationSpec {regional_standard_and_regulation_id: 'vcd pa', impl_id: row.impl_id})
ON CREATE SET
    ispec.requirement_id = row.requirement_id,
    ispec.name = row.name,
    ispec.description = row.description,
    ispec.owner = row.owner;
"""
#policy
policy = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pol:Policy {regional_standard_and_regulation_id: 'vcdpa', policy_id: row.policy_id})
ON CREATE SET
    pol.name = row.name,
    pol.description = row.description,
    



