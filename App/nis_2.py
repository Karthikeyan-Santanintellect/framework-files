# Regulation
from enum import member
import re

from App import sec


regional_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    reg.name = "NIS 2 Directive (EU) 2022/2555",
    reg.version = "2022/2555",
    reg.status = "Active",
    reg.jurisdiction = "European Union",
    reg.effective_date = "2023-01-16", 
    reg.description = "Directive (EU) 2022/2555 on measures for a high common level of cybersecurity across the Union. It repeals the previous NIS Directive (2016/1148) and modernizes the legal framework to address increased digitization and an evolving threat landscape, expanding the scope of cybersecurity rules to new sectors and entities.";
    """
# Chapters
chapters =  """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {id: row.chapter_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    c.number = row.chapter_number,
    c.title = row.title,
    c.range = row.article_range,
    c.reference = row.page_reference,
    c.description = row.description;
"""
# Articles
articles = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Article {id: row.article_id,regional_standard_regulation_id: 'NIS2-EU-2022-2555'})    
ON CREATE SET
    a.number = row.article_number,
    a.subject = row.subject,
    a.reference = row.page_reference,
    a.mandatory = row.mandatory,
    a.applicable_to = row.applicable_to_essential,
    a.applicable_to_important = row.applicable_to_important,
    a.summary = row.key_content_summary;
"""
#certification_bodies 
certification_bodies = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cb:CertificationBody {id: row.certification_body_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    cab.name = row.certification_body_name,
    cab.country = row.country,
    cab.accreditation = row.accreditation,
    cab.offered = row.services_offered,
    cab.approved = row.nis2_approved,
    cab.certified = row.iso27001_certification,
    cab.website = row.website;
"""
#Agent_types
agent_types = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ag:Agent {id: row.agent_type_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET ag.name = row.type_name,
    ag.definition = row.definition,
    ag.reference = row.page_reference,
    ag.regime = row.supervisory_regime,
    ag.maxFineAmount = row.max_fine_amount,
    ag.maxFinePercentage = row.max_fine_percentage,
    ag.obligations = row.key_obligations;
"""
#Concepts
concepts = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Concept {id: row.concept_id, regional_standard_id : 'NIS2-EU-2022-2555'})
ON CREATE SET
    co.name = row.name,
    co.article = row.sub_article,
    co.reference = row.page_reference,
    co.category = row.category,
    co.mandatory = mandatory,
    co.description = row.description,
    co.standards = row.related_standards;
"""
#Incidents -aggregated
incidents = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (in:Incident {id: row.incident_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    in.year = row.year,
    in.period = row.reporting_period,
    in.reported = row.total_incidents_reported,
    in.reporting = row.member_states_reporting,
    in.count = row.system_failures_count,
    in.observed = row.ddos_attacks_observed,
    in.reported = row.cross_border_incidents_reported,
    in.report = row.source_report;
"""
#Deadlines
deadlines = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Deadline {id: row.deadline_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    d.name = row.deadline_name,
    d.duration = row.duration_iso8601,
    d.fixedDate = row.fixed_date,
    d.reference = row.page_reference,
    d.description = row.description,
    d.consequence_of_miss = row.consequence_of_miss;
"""
# control_frameworks
control_frameworks = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:ControlFramework {id: row.control_framework_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    cf.name = row.framework_name,
    cf.standardReference = row.standard_reference,
    cf.organization = row.issuing_organization,
    cf.date = row.publication_date,
    cf.article21 = row.maps_to_article_21
    cf.rvailability = row.public_availability,
    cf.frameworkType = row.framework_type,
    cf.certificationAvailable =row.certification_available
    cf.recognized = row.belgium_nis2_recognized,
    cf.description = row.description;
"""
# obligations
obligations = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ob:Obligation {id: row.obligation_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    ob.name = row.obligation_name,
    ob.reference = row.page_reference,
    ob.mandatory = CASE WHEN row.mandatory = 'TRUE' THEN true ELSE false END,
    ob.description = row.description,
    ob.method = row.verification_method,
    ob.compliance = row.penalty_for_non_compliance;
"""
# member_state
member_state = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ms:MemberState {id: row.member_state_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    ms.name = row.member_state,
    ms.authority_name = row.competent_authority_name,
    ms.type = row.authority_type,
    ms.website = row.website,
    ms.csirt_name = row.csirt_name,
    ms.csirt_website = row.csirt_website,
    ms.contact = row.single_point_of_contact,
    ms.status = row.transposition_status,
    ms.law_name = row.law_name,
    ms.date = row.entry_into_force_date,
    ms.entities = row.estimated_entities,
    ms.deadline = row.registration_deadline,
    ms.portal = row.registration_portal;
"""
#organizational_data
organizational_data = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (od:OrganizationalData {id: row.org_id, regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
ON CREATE SET
    od.type = row.data_type,
    od.category = row.category,
    od.description = row.description,
    od.Source = row.data_source,
    od.updated = row.last_updated,
    od.country = row.country,
    od.numeric = row.value_numeric,
    od.text = row.value_text,
    od.notes = row.notes;
"""
#sector
sector ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Sector {
  sector_id: row.sector_id,
  regional_standard_regulation_id: 'NIS2-EU-2022-2555'
})
ON CREATE SET
  s.name        = row.sector_name,
  s.annex       = row.annex,
  s.criticality = row.criticality,
  s.page        = row.page_reference,
  s.subsectors  = row.subsectors,
  s.examples    = row.example_entity_types;
"""
# penalties
penalties = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Penalty {
  penalty_id: row.penalty_id,
  regional_standard_regulation_id: 'NIS2-EU-2022-2555'
})
ON CREATE SET
  p.type              = row.penalty_type,
  p.article_ref       = row.article_reference,
  p.page              = row.page_reference,
  p.applies_to        = row.applies_to_entity_type,
  p.max_amount_eur    = row.max_amount_eur,
  p.max_pct_turnover  = row.max_percentage_global_turnover,
  p.description       = row.description,
  p.legal_basis       = row.legal_basis_formula,
  p.triggers          = row.triggers;
"""
#recitals
recitals = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Recital {
  id: row.recital_id,
  regional_standard_regulation_id: 'NIS2-EU-2022-2555'
})
ON CREATE SET
  r.number        = row.recital_number,
  r.page          = row.page_reference,
  r.description   = row.description,
  r.related_items = row.related_articles,
  r.theme         = row.theme;
"""
#vulnerability
vulnerability = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (v:Vulnerability {
  id: row.vulnerability_id,
  regional_standard_regulation_id: 'NIS2-EU-2022-2555'
})
ON CREATE SET
  v.cve_id                = row.cve_id,
  v.disclosure_date       = row.disclosure_date,
  v.severity_cvss         = row.severity_cvss,
  v.affected_product      = row.affected_product_service,
  v.vendor                = row.vendor,
  v.vuln_type             = row.vulnerability_type,
  v.exploitation_status   = row.exploitation_status,
  v.mitigation_available  = row.mitigation_available,
  v.euvd_entry            = row.euvd_entry,
  v.nis2_sector_impact    = row.nis2_sector_impact;
"""
#service - types
service_types = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (st:ServiceType {
  id: row.service_type_id,
  regional_standard_regulation_id: 'NIS2-EU-2022-2555'
})
ON CREATE SET
  st.name                   = row.service_type_name,
  st.article_reference      = row.article_reference,
  st.page_reference         = row.page_reference,
  st.definitions_source     = row.definitions_source,
  st.mandatory_for_entities = row.mandatory_for_entities,
  st.nist_cef_category      = row.nist_cef_category,
  st.description            = row.description,
  st.eu_regulation_applies  = row.eu_regulation_applies;
"""
# Relationships
# 1. Regulation -> Chapter
regulation_chapters = """
MATCH (r:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (c:Chapter {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (r)-[:REGULATION_CONTAINS_CHAPTER]->(c);
"""

# 2. Chapter -> Article
chapter_articles = """
MATCH (c:Chapter {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (a:Article {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (c)-[:CHAPTER_INCLUDES_ARTICLE]->(a);
"""
# 3. Regulation -> Recital
regulation_recitals = """
MATCH (r:Recital {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (reg)-[:REGULATION_CONTAINS_RECITAL]->(r);
"""

# 4. Recital -> Article
recitals_articles = """
MATCH (r:Recital {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (a:Article {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (r)-[:RECITAL_EXPLAINS_ARTICLE]->(a);
"""

# 5. Article -> Obligation
article_obligations = """
MATCH (a:Article {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (ob:Obligation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (a)-[:ARTICLE_DEFINES_OBLIGATION]->(ob);
"""

# 6. Obligation -> Deadline
obligations_deadlines = """
MATCH (ob:Obligation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (d:Deadline {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (ob)-[:OBLIGATION_HAS_DEADLINE]->(d);
"""

# 7. Obligation -> Sector
obligations_sectors = """
MATCH (ob:Obligation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (s:Sector {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (ob)-[:OBLIGATION_APPLIES_TO_SECTOR]->(s);
"""

# 8. Sector -> ServiceType 
sector_service_types = """
MATCH (s:Sector {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (st:ServiceType {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (s)-[:SECTOR_INCLUDES_SERVICE]->(st);
"""

# 9. Vulnerability -> Sector
vulnerability_sectors = """
MATCH (v:Vulnerability {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (s:Sector {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (v)-[:VULNERABILITY_IMPACTS_SECTOR]->(s);
"""

# 10. Penalties -> Article
penalties_articles = """
MATCH (p:Penalty {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (a:Article {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (p)-[:PENALTY_ENFORCES_ARTICLE]->(a);
"""

# 11. Penalties -> Concept 
penalties_concepts = """
MATCH (p:Penalty {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (co:Concept {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (p)-[:PENALTY_APPLIES_TO_ENTITY]->(co);
"""

# 12. MemberState -> Incident
member_state_incidents = """
MATCH (ms:MemberState {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (i:Incident {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (ms)-[:MEMBER_STATE_REPORTED_INCIDENT]->(i);
"""

# 13. MemberState -> Agent 
member_state_agents = """
MATCH (ms:MemberState {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (at:Agent {regional_standard_regulation_id: 'NIS2-EU-2022-2555'}) 
MERGE (ms)-[:MEMBER_STATE_DESIGNATES_AUTHORITY]->(at);
"""

# 14. ControlFramework -> Article 
control_framework_articles = """
MATCH (cf:ControlFramework {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (a:Article {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (cf)-[:CONTROL_FRAMEWORK_MAPS_TO_REQUIREMENT]->(a);
"""

# 15. CertificationBody -> ControlFramework
certification_bodies_control_frameworks = """
MATCH (cb:CertificationBody {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (cf:ControlFramework {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (cb)-[:CERTIFICATION_BODY_AUDITS_FRAMEWORK]->(cf);
"""

# 16. MemberState -> Regulation
member_state_regulation = """
MATCH (ms:MemberState {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'NIS2-EU-2022-2555'})
MERGE (ms)-[:MEMBER_STATE_TRANSPOSES_REGULATION]->(reg);
"""