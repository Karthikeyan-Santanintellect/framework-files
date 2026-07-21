#Regional Regulation
regional_standard_and_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    reg.name = "New York Stop Hacks and Improve Electronic Data Security (SHIELD) Act",
    reg.version = "1.0",
    reg.base_regulation = "New York Information Security Breach and Notification Act",
    reg.codification = "New York General Business Law Article 39-F §§ 899-aa and 899-bb",
    reg.effective_date = date("2020-03-21"),
    reg.enactment_date = date("2019-07-25"),
    reg.enforcement_date = date("2020-03-21"),
    reg.status = "Active",
    reg.description = "The SHIELD Act is New York's data security and breach notification law that amends the state's Information Security Breach and Notification Act, expands the scope of 'private information', and requires any person or business that owns or licenses private information of New York residents to implement reasonable administrative, technical, and physical safeguards, enforced by the New York Attorney General.",
    reg.jurisdiction = "New York (State)";
"""

# Sections
sections = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sec:Section {section_id: row.section_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    sec.official_citation = row.official_citation,
    sec.heading = row.heading,
    sec.text = row.text;
"""
#Administrative Safeguards
administrative_safeguards = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sf:AdministrativeSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    sf.safeguard_category = row.safeguard_category,
    sf.official_citation = row.official_citation,
    sf.section_id = row.section_id,
    sf.statutory_text = row.statutory_text;
"""

#technical_safeguards
technical_safeguards = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ts:TechnicalSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    ts.safeguard_category = row.safeguard_category,
    ts.official_citation = row.official_citation,
    ts.section_id = row.section_id,
    ts.statutory_text = row.statutory_text;
"""
# Physical Safeguards
physical_safeguards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ps:PhysicalSafeguard {safeguard_id: row.safeguard_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    ps.safeguard_category = row.safeguard_category,
    ps.official_citation = row.official_citation,
    ps.section_id = row.section_id,
    ps.statutory_text = row.statutory_text;
"""
#private_information
private_information = """
Load CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pvi:PrivateInformation {info_id: row.info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    pvi.element_name = row.element_name,
    pvi.element_type = row.element_type,
    pvi.official_citation = row.official_citation,
    pvi.statutory_text = row.statutory_text,
    pvi.requires_combination_with_personal_information = row.requires_combination_with_personal_information;
"""
# Statutory Definitions
statutory_definition = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:StatutoryDefinition {definition_id: row.definition_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
ON CREATE SET
    d.term = row.term,
    d.official_citation = row.official_citation,
    d.statutory_text = row.statutory_text;
"""
# Data Element Combinations
data_element_combination = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'DEC'
MERGE (dec:DataElementCombination {combination_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    dec.type = row.type,
    dec.elements = row.elements_list,
    dec.requires_name = row.requires_personal_name_boolean,
    dec.description = row.description;
"""
# Publicly Available Information
public_info_exclusion = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'PAI'
MERGE (pai:PubliclyAvailableInformation {exclusion_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    pai.name = row.type,
    pai.description = row.description;
"""
# Personal Information (Parent Node)
personal_information = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.combination_id STARTS WITH 'PI'
MERGE (pi:PersonalInformation {type_id: row.combination_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    pi.name = row.type,
    pi.description = row.description;
"""
# Regulatory Bodies
regulatory_bodies = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.authority_id <> 'SB_DEF_001'
MERGE (rb:RegulatoryBody {authority_id: row.authority_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    rb.name = row.name,
    rb.role = row.role,
    rb.jurisdiction = row.jurisdiction,
    rb.exclusive_enforcement = row.exclusive_enforcement,
    rb.description = row.description;
"""
# Small Business Definition
small_business_def = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.authority_id = 'SB_DEF_001'
MERGE (sb:SmallBusinessDefinition {definition_id: row.authority_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    sb.name = row.name,
    sb.description = row.description;
"""
# Civil Penalties
civil_penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rule_id STARTS WITH 'CP'
MERGE (cp:CivilPenalty {penalty_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    cp.name = row.name,
    cp.violation_type = row.violation_type,
    cp.amount_per_violation = row.amount,
    cp.cap_amount = row.cap_amount,
    cp.description = row.description;
"""
# Statute of Limitations
statute_of_limitations = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rule_id STARTS WITH 'SOL'
MERGE (sol:StatuteOfLimitations {rule_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    sol.name = row.name,
    sol.description = row.description;
"""
# Inadvertent Disclosure
inadvertent_disclosure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rule_id STARTS WITH 'EXC'
MERGE (id:InadvertentDisclosure {exception_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    id.name = row.name,
    id.description = row.description;
"""

# Unauthorized Access
unauthorized_access = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rule_id STARTS WITH 'DEF'
MERGE (ua:UnauthorizedAccess {rule_id: row.rule_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    ua.name = row.name,
    ua.description = row.description;
"""
# Compliant Regulated Entity
compliant_regulated_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cre:CompliantRegulatedEntity {entity_id: row.entity_id, regional_standard_regulation_id: row.regional_standard_regulation_id})
ON CREATE SET
    cre.regulation_type = row.regulation_type,
    cre.deemed_compliant_status = row.deemed_compliant_status,
    cre.official_citation = row.official_citation;
"""


#Relationships
# regulation to section
regulation_section = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (sec:Section {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_GOVERNS_SECTION]->(sec);
"""

# Private Information -> Statutory Definition (data element combination trigger)
private_information_statutory_definition = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (SourceInfo:PrivateInformation {info_id: row.source_info_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (TargetDef:StatutoryDefinition {definition_id: row.target_definition_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (SourceInfo)-[r:PRIVATE_INFORMATION_COMBINES_WITH_DATA_ELEMENT]->(TargetDef)
ON CREATE SET
    r.official_citation = row.official_citation,
    r.statutory_basis = row.statutory_basis;
"""

# Safeguards / Definitions -> Section (polymorphic, no APOC)
defined_in_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (sec:Section {section_id: row.target_section_id, regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (n {regional_standard_regulation_id: 'NY SHIELD 1.0'})
WHERE n.safeguard_id = row.source_node_id OR n.definition_id = row.source_node_id
MERGE (n)-[r:DEFINED_IN_SECTION]->(sec)
ON CREATE SET r.official_citation = row.official_citation;
"""

# Link Attorney General to Civil Penalties
regulatory_bodies_civil_penalties = """
MATCH (rb:RegulatoryBody {authority_id: 'NY_AG'})
MATCH (cp:CivilPenalty {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (rb)-[:ATTORNEY_GENERAL_ENFORCES_PENALTY]->(cp);
"""

# Link Private Information to Data Element Combinations (Triggers)
private_information_data_element_combination = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (dec:DataElementCombination {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pvi)-[:PRIVACY_INFORMATION_DEFINED_BY_COMBINATION]->(dec);
"""

#Link Private Information to Parent Category (Personal Information)
personal_information_private_information = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (parent:PersonalInformation {type_id: 'PI-PARENT-001', regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pvi)-[:PRIVACY_INFORMATION_SUBTYPE_OF_PERSONAL_INFORMATION]->(parent);
"""

# Link Private Information to Publicly Available Information (Exclusion)
private_information_publicly_available_information = """
MATCH (pvi:PrivateInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MATCH (pai:PubliclyAvailableInformation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (pvi)-[:PRIVACY_INFORMATION_EXCLUDES_DEFINITION]->(pai);
"""

orphan_small_business = """
MATCH (orphan:SmallBusinessDefinition) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_statute_limitations = """
MATCH (orphan:StatuteOfLimitations) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_inadvertent_disclosure = """
MATCH (orphan:InadvertentDisclosure) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_unauthorized_access = """
MATCH (orphan:UnauthorizedAccess) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""

orphan_compliant_regulated_entity = """
MATCH (orphan:CompliantRegulatedEntity) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_GRANTS_SAFE_HARBOR]->(orphan);
"""

orphan_statutory_definition = """
MATCH (orphan:StatutoryDefinition) WHERE NOT EXISTS ((orphan)--())
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NY SHIELD 1.0'})
MERGE (reg)-[:REGULATION_DEFINES_LEGAL_TERM]->(orphan);
"""


import sys
import os
import time
import logging
import json
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    client.close()
    sys.exit(1)

logger.info("Loading graph structure...")


#Nodes
client.query(regional_standard_and_regulation)
time.sleep(2)

client.query(sections.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Sections.csv"))
time.sleep(2)

client.query(administrative_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_AdministrativeSafeguard_nodes.csv"))
time.sleep(2)

client.query(technical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_TechnicalSafeguard_nodes.csv"))
time.sleep(2)

client.query(physical_safeguards.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Physical%20Safeguard.csv"))
time.sleep(2)

client.query(private_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_PrivateInformation_nodes.csv"))
time.sleep(2)

client.query(statutory_definition.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_StatutoryDefinition_nodes.csv"))
time.sleep(2)

client.query(data_element_combination.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(public_info_exclusion.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(personal_information.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Data%20Definitions.csv"))
time.sleep(2)

client.query(regulatory_bodies.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Entities.csv"))
time.sleep(2)

client.query(small_business_def.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Entities.csv"))
time.sleep(2)

client.query(civil_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(statute_of_limitations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(inadvertent_disclosure.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(unauthorized_access.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Legal%20Rules.csv"))
time.sleep(2)

client.query(compliant_regulated_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD%20-%20Safe%20Harbor.csv"))
time.sleep(2)


#Relationships
client.query(regulation_section)
time.sleep(2)

client.query(defined_in_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_DEFINED_IN_SECTION_relationships.csv"))
time.sleep(2)

client.query(private_information_statutory_definition.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/gautham/SHIELD/SHIELD_COMBINES_WITH_DATA_ELEMENT_relationships.csv"))
time.sleep(2)

client.query(regulatory_bodies_civil_penalties)
time.sleep(2)

client.query(private_information_data_element_combination)
time.sleep(2)

client.query(personal_information_private_information)
time.sleep(2)

client.query(private_information_publicly_available_information)
time.sleep(2)

client.query(orphan_small_business)
time.sleep(2)

client.query(orphan_statute_limitations)
time.sleep(2)

client.query(orphan_inadvertent_disclosure)
time.sleep(2)

client.query(orphan_unauthorized_access)
time.sleep(2)

client.query(orphan_compliant_regulated_entity)
time.sleep(2)

client.query(orphan_statutory_definition)
time.sleep(2)

logger.info("Graph structure loaded successfully.")

cleanup_query = """
MATCH (n)
WHERE size(labels(n)) = 0
DETACH DELETE n
"""

logger.info("Cleaning up ghost nodes (nodes with no labels)...")
client.query(cleanup_query)
logger.info("✓ Ghost nodes removed from database.")

query = """
MATCH (n)
WHERE size(labels(n)) > 0
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

#     import json
#     with open('shield.json', 'w', encoding='utf-8') as f:
#         f.write(json.dumps(graph_data, default=str, indent=2))
#     logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to shileld.json")
# else:
#     logger.error("No data returned from the query.")

client.close()
