# Regulation 
regional_standard_regulation ="""
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DORA 2022/2554'})
ON CREATE SET
    reg.name = "Digital Operational Resilience Act",
    reg.citation = "Regulation (EU) 2022/2554",
    reg.version = "2022/2554",
    reg.publication_date = date("2022-12-27"),
    reg.effective_date = date("2025-01-17"),
    reg.type = "EU Legislative",
    reg.jurisdiction = "EU/EEA",
    reg.description = "EU regulation on digital operational resilience for the financial sector, ensuring financial entities can withstand, respond to, and recover from ICT-related disruptions and threats.";
"""
# Chapters
chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {id: row.id})
ON CREATE SET 
    c.label = row.label,
    c.chapter_number = row.chapter_number,
    c.name = row.name,
    c.description = row.description;
"""
# Article 
article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Article {id: row.id})
ON CREATE SET 
    a.label = row.label,
    a.article_number = row.article_number,
    a.name = row.name,
    a.parent_chapter = row.parent_chapter;
"""
# Competent Authority
competent_authority = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ca:CompetentAuthority {id: row.id})
ON CREATE SET 
    ca.label = row.label,
    ca.name = row.name,
    ca.legal_reference = row.legal_reference,
    ca.primary_powers = row.primary_powers,
    ca.sector_responsibility = row.sector_responsibility;
"""
# Critical Functions
critical_functions = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cf:CriticalFunction {id: row.id})
ON CREATE SET   
    cf.name = row.name,
    cf.legal_reference = row.legal_reference,
    cf.impact_criteria = row.impact_criteria;
"""
# Critical ICT Provider
critical_ict_proider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ctp:CriticalICTProvider {id: row.id})
ON CREATE SET 
    ctp.name = row.name,
    ctp.legal_reference = row.legal_reference,
    ctp.designation_criteria = row.designation_criteria,
    ctp.oversight_status = row.oversight_status;
"""
# Cyber Threat
cyber_threat = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ct:CyberThreat {id: row.id})
ON CREATE SET 
    ct.name = row.name,
    ct.legal_reference = row.legal_reference,
    ct.threat_type = row.threat_type,
    ct.notification_type = row.notification_type,
    ct.properties = row.properties;
"""
# Facility
facility = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Facility {id: row.id})
ON CREATE SET 
    f.name = row.name,
    f.legal_reference = row.legal_reference,
    f.facility_types = row.facility_types,
    f.inspection_rights = row.inspection_rights;    
"""
# ICT Risk
ict_risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ir:ICTRisk {id: row.id})
ON CREATE SET 
    ir.name = row.name,
    ir.legal_reference = row.legal_reference,
    ir.source = row.source,
    ir.impact_area = row.impact_area,
    ir.description = row.description;
"""
# Fiancial Entity
financial_entity = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (fe:FinancialEntity {id: row.id})
ON CREATE SET 
    fe.name = row.name,
    fe.entity_type = row.entity_type,
    fe.legal_reference = row.legal_reference,
    fe.size_attribute = row.size_attribute,
    fe.compliance_regime = row.compliance_regime;
"""
# ICT Control
ict_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ic:ICTControl {id: row.id})
ON CREATE SET
    ic.name = row.name,
    ic.legal_reference = row.legal_reference,
    ic.control_type = row.control_type,
    ic.methods = row.methods;
"""

# ICT Service
ict_service = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (is:ICTService {id: row.id})
ON CREATE SET 
    is.name = row.name,
    is.legal_reference = row.legal_reference,
    is.service_type = row.service_type,
    is.scope_exclusions = row.scope_exclusions,
    is.mandatory_attributes = row.mandatory_attributes;  
"""
# Information Asset
information_asset = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ia:InformationAsset {id: row.id})
ON CREATE SET 
    ia.name = row.name,
    ia.legal_reference = row.legal_reference,
    ia.classification = row.classification;
"""
# ICT Asset
ict_asset = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ica:ICTAsset {id: row.id})
ON CREATE SET 
    ica.name = row.name,
    ica.legal_reference = row.legal_reference,
    ica.category = row.category,
    ica.properties = row.properties;
"""
# Joint Examination Term
joint_examination_term = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (je:JointExaminationTeam {id: row.id})
ON CREATE SET 
    je.name = row.name,
    je.legal_reference = row.legal_reference,
    je.composition = row.composition,
    je.tasks = row.tasks;
"""
# Juridsction
jurisdiction = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ju:Jurisdiction {id: row.id})
ON CREATE SET 
    ju.name = row.name,
    ju.legal_reference = row.legal_reference,
    ju.authority_level = row.authority_level,
    ju.scope = row.scope;
"""
# Lead Overseer
lead_overeseer ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lo:LeadOverseer {id: row.id})
ON CREATE SET 
    lo.name = row.name,
    lo.legal_reference = row.legal_reference,
    lo.oversight_tools = row.oversight_tools,
    lo.assigned_esa = row.assigned_esa;
"""
# Legacy ICT Systems
legacy_ict_systems = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lis:LegacyICTSystems {id: row.id})
ON CREATE SET 
    lis.name = row.name,
    lis.legal_reference = row.legal_reference,
    lis.status = row.status,
    lis.requirements = row.requirements,
    lis.risk_attributes = row.risk_attributes;
"""
# Major Incident
major_incident = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mi:MajorIncident {id: row.id})
ON CREATE SET 
    mi.name = row.name,
    mi.legal_reference = row.legal_reference,
    mi.classification_criteria = row.classification_criteria,
    mi.reporting_obligation = row.reporting_obligation,
    mi.properties = row.properties;
"""
# Management Body
management_body ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (mb:ManagementBody {id: row.id})
ON CREATE SET  
    mb.name = row.name,
    mb.legal_reference = row.legal_reference,
    mb.responsibility_type = row.responsibility_type,
    mb.primary_duties = row.primary_duties,
    mb.required_skills = row.required_skills;
"""
# Network Systems
network_systems ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ns:NetworkSystems {id: row.id})
ON CREATE SET 
    ns.name = row.name,
    ns.legal_reference = row.legal_reference,
    ns.security_objectives = row.security_objectives;
"""
# Oversight Forum
oversight_forum = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (of:OversightForum {id: row.id})
ON CREATE SET 
    of.name = row.name,
    of.legal_reference = row.legal_reference,
    of.composition = row.composition,
    of.primary_tasks = row.primary_tasks,
    of.governance_role = row.governance_role;
"""
# Penalty
penalty = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pe:Penalty {id: row.id})
ON CREATE SET 
    pe.name = row.name,
    pe.legal_reference = row.legal_reference,
    pe.max_penalty = row.max_penalty,
    pe.condition = row.condition;
"""
# Processing Location
processing_location = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pl:ProcessingLocation {id: row.id})
ON CREATE SET 
    pl.name = row.name,
    pl.legal_reference = row.legal_reference,
    pl.data_types = row.data_types,
    pl.contractual_requirement = row.contractual_requirement;
"""
# Remediation Plan
remediation_plan = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rp:RemediationPlan {id: row.id})
ON CREATE SET 
    rp.name = row.name,
    rp.legal_reference = row.legal_reference,
    rp.trigger = row.trigger,
    rp.objective = row.objective,
    rp.reporting_requirement = row.reporting_requirement;
"""
# Requirements
requirements = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (re:Requirements {id: row.id})
ON CREATE SET 
    re.article_id = row.article_id,
    re.requirement_text = row.requirement_text;
"""
# ICT Third Party Service Provider
third_party_service_provider = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (its:ICTThirdPartyServiceProvider {id: row.id})
ON CREATE SET 
    its.name = row.name,
    its.legal_reference = row.legal_reference,
    its.provider_type = row.provider_type,
    its.mandatory_clauses = row.mandatory_clauses,
    its.description = row.description;
"""
# Subsidiary
subsidiary = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (su:Subsidiary {id: row.id})
ON CREATE SET
    su.name = row.name,
    su.legal_reference = row.legal_reference,
    su.establishment_rule = row.establishment_rule,
    su.compliance_period = row.compliance_period;
"""
# Threat Led Penetration Test
threat_led_penetration_test = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tlp:ThreatLedPenetrationTest {id: row.id})
ON CREATE SET
    tlp.name = row.name,
    tlp.legal_reference = row.legal_reference,
    tlp.frequency = row.frequency,
    tlp.scope = row.scope,
    tlp.tester_requirements = row.tester_requirements,
    tlp.authority_role = row.authority_role;
"""

# Relationships

reg_to_chapters = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DORA 2022/2554'})
MATCH (c:Chapter)
MERGE (reg)-[:REGULATION_CONTAINS_CHAPTER]->(c);
"""

# Chapters to Articles
chapters_to_articles = """
MATCH (c:Chapter)
MATCH (a:Article)
MERGE (c)-[:CHAPTER_CONTAINS_ARTICLE]->(a);
"""

# Articles to Requirements
articles_to_requirements = """
MATCH (a:Article)
MATCH (re:Requirements)
MERGE (a)-[:ARTICLE_CONTAINS_REQUIREMENT]->(re);
"""

# Competent Authority to Financial Entity
competent_authority_financial_entity = """
MATCH (ca:CompetentAuthority)
MATCH (fe:FinancialEntity)
MERGE (ca)-[:COMPETENT_AUTHORITY_SUPERVISES_FINANCIAL_ENTITY]->(fe);
"""

# Lead Overseer to Critical ICT Providers
lead_overseer_critical_ict_providers = """
MATCH (lo:LeadOverseer)
MATCH (ctp:CriticalICTProvider)
MERGE (lo)-[:LEAD_OVERSEER_OVERSEES_CRITICAL_ICT_PROVIDER]->(ctp);
"""

# Management Body to Financial Entity
management_body_financial_entity = """
MATCH (mb:ManagementBody)
MATCH (fe:FinancialEntity)
MERGE (mb)-[:MANAGEMENT_BODY_GOVERNS_FINANCIAL_ENTITY]->(fe);
"""

# Joint Examination Team to Lead Overseer
joint_examination_team_lead_overseer = """
MATCH (je:JointExaminationTeam)
MATCH (lo:LeadOverseer)
MERGE (je)-[:JOINT_EXAMINATION_TEAM_ASSISTED_BY_LEAD_OVERSEER]->(lo);
"""

# Oversight Forum to Lead Overseer
oversight_forum_lead_overseer = """
MATCH (of:OversightForum)
MATCH (lo:LeadOverseer)
MERGE (of)-[:OVERSIGHT_FORUM_COORDINATES_LEAD_OVERSEER]->(lo);
"""

# Financial Entity to ICT Risk
financial_entity_ict_risk = """
MATCH (fe:FinancialEntity)
MATCH (ir:ICTRisk)
MERGE (fe)-[:FINANCIAL_ENTITY_MANAGES_ICT_RISK]->(ir);
"""

# ICT Control Mitigates to ICT Risk
ict_control_mitigates_ict_risk = """
MATCH (ic:ICTControl)
MATCH (ir:ICTRisk)
MERGE (ic)-[:ICT_CONTROL_MITIGATES_ICT_RISK]->(ir);
"""

# Financial Entity to Assets
financial_entity_owns_assets = """
MATCH (fe:FinancialEntity)
MATCH (ia:InformationAsset)
MATCH (ica:ICTAsset)
MERGE (fe)-[:FINANCIAL_ENTITY_OWNS_INFORMATION_ASSET]->(ia)
MERGE (fe)-[:FINANCIAL_ENTITY_OWNS_ASSETS]->(ica);
"""

# ICT Service to Assets
# (Fixed typo: REPLIES -> RELIES)
ict_service_assets = """
MATCH (is:ICTService)
MATCH (ica:ICTAsset)
MERGE (is)-[:ICT_SERVICE_RELIES_ON_ICT_ASSET]->(ica);
"""

# Network Systems to ICT Services
network_systems_ict_services = """
MATCH (ns:NetworkSystems)
MATCH (is:ICTService)
MERGE (ns)-[:NETWORK_SYSTEMS_SUPPORT_ICT_SERVICE]->(is);
"""

# Financial Entity to Major Incident
financial_entity_reports_major_incident = """
MATCH (fe:FinancialEntity)
MATCH (mi:MajorIncident)
MERGE (fe)-[:FINANCIAL_ENTITY_REPORTS_MAJOR_INCIDENT]->(mi);
"""

# Major Incident Reported to Competent Authority
major_incident_competent_authority = """
MATCH (mi:MajorIncident)
MATCH (ca:CompetentAuthority)
MERGE (mi)-[:MAJOR_INCIDENT_REPORTED_TO_COMPETENT_AUTHORITY]->(ca);
"""

# Financial Entity to TLPT
financial_entity__tlpt = """
MATCH (fe:FinancialEntity)
MATCH (tlp:ThreatLedPenetrationTest) 
MERGE (fe)-[:FINANCIAL_ENTITY_CONDUCTS_THREAT_LED_PENETRATION_TEST]->(tlp); 
"""

# Remediation Plan to TLPT
remediation_plan_tlpt = """
MATCH (rp:RemediationPlan)
MATCH (tlp:ThreatLedPenetrationTest)
MERGE (rp)-[:REMEDIATION_PLAN_TRIGGERED_BY_THREAT_LED_PENETRATION_TEST]->(tlp);
"""

# Financial Entity Third Party
financial_entity_third_party = """
MATCH (fe:FinancialEntity)
MATCH (its:ICTThirdPartyServiceProvider)
MERGE (fe)-[:FINANCIAL_ENTITY_CONTRACTS_THIRD_PARTY_SERVICE_PROVIDER]->(its);
"""

# Third Party ICT Service
third_party_ict_service = """
MATCH (its:ICTThirdPartyServiceProvider)
MATCH (is:ICTService)
MERGE (its)-[:THIRD_PARTY_PROVIDES_ICT_SERVICE]->(is);
"""

# Third Party Subsidiary
third_party_subsidiary = """
MATCH (its:ICTThirdPartyServiceProvider)
MATCH (su:Subsidiary)
MERGE (its)-[:THIRD_PARTY_HAS_SUBSIDIARY]->(su);
"""

# Third Party to Processing Location
third_party_processing_location = """
MATCH (its:ICTThirdPartyServiceProvider)
MATCH (pl:ProcessingLocation)
MERGE (its)-[:THIRD_PARTY_OPERATES_IN_PROCESSING_LOCATION]->(pl);
"""

# Regulation to Jurisdiction
reg_jurisdiction = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DORA 2022/2554'})
MATCH (ju:Jurisdiction)
MERGE (reg)-[:REGULATION_CONTAINS_JURISDICTION]->(ju);
"""

# Competent Authority to Jurisdiction
competent_authority_jurisdiction = """
MATCH (ca:CompetentAuthority)
MATCH (ju:Jurisdiction)
MERGE (ca)-[:COMPETENT_AUTHORITY_SUPERVISES_JURISDICTION]->(ju);
"""

# Financial Entity to Critical Functions
financial_entity_critical_functions = """
MATCH (fe:FinancialEntity)
MATCH (cf:CriticalFunction)
MERGE (fe)-[:FINANCIAL_ENTITY_CRITICAL_FUNCTION]->(cf);
"""

# ICT Services to Critical Functions
ict_services_critical_functions = """
MATCH (is:ICTService)
MATCH (cf:CriticalFunction)
MERGE (is)-[:ICT_SERVICE_SUPPORTS_CRITICAL_FUNCTION]->(cf);
"""

# Cyber Threat to ICT Risk
cyber_threat_ict_risk = """
MATCH (ct:CyberThreat)
MATCH (ir:ICTRisk)
MERGE (ct)-[:CYBER_THREAT_INCREASES_ICT_RISK]->(ir);
"""

# Cyber Threat to Major Incidents
cyber_threat_major_incident = """
MATCH (ct:CyberThreat)
MATCH (mi:MajorIncident)
MERGE (ct)-[:CYBER_THREAT_CAN_CAUSE_MAJOR_INCIDENT]->(mi);
"""

# Financial Entity to Facility
financial_entity_facility = """
MATCH (fe:FinancialEntity)
MATCH (f:Facility)
MERGE (fe)-[:FINANCIAL_ENTITY_OPERATES_AT_FACILITY]->(f);   
"""

# Facility houses ICT Assets
# (Fixed the 'ia' vs 'ica' variable mismatch)
facility_ict_asset = """
MATCH (f:Facility)
MATCH (ica:ICTAsset)
WHERE ica.category IN ['Hardware', 'Infrastructure', 'Servers']
MERGE (f)-[:FACILITY_HOUSES_ICT_ASSET]->(ica);
"""

# Financial Entity to Legacy ICT Systems
financial_entity_legacy_ict_systems = """
MATCH (fe:FinancialEntity)
MATCH (lis:LegacyICTSystems)
MERGE (fe)-[:FINANCIAL_ENTITY_USES_LEGACY_ICT_SYSTEMS]->(lis);
"""

# Legacy System to ICT Risk
legacy_system_ict_risk = """
MATCH (lis:LegacyICTSystems)
MATCH (ir:ICTRisk)
MERGE (lis)-[:LEGACY_SYSTEM_POSES_ICT_RISK]->(ir);
"""

# Competent Authority to Penalty
competent_authority_penalty = """
MATCH (ca:CompetentAuthority)
MATCH (pe:Penalty)
MERGE (ca)-[:COMPETENT_AUTHORITY_ENFORCES_PENALTY]->(pe);
"""

# Regulation to Penalty
reg_defines_penalty = """
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'DORA 2022/2554'})
MATCH (pe:Penalty)
MERGE (reg)-[:REGULATION_DEFINES_PENALTY]->(pe);
"""
# Critical Function to Critical ITC Provider
critical_functions_critical_ict_providers = """
MATCH (ctp:CriticalICTProvider) 
MATCH (cf:CriticalFunction)
MERGE (cf)-[:CRITICAL_FUNCTION_SUPPORTS_CRITICAL_ICT_PROVIDER]->(ctp);
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

client.query(regional_standard_regulation)
time.sleep(2)

client.query(chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Chapter.csv"))
time.sleep(2)

client.query(article.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Article.csv"))
time.sleep(2)

client.query(competent_authority.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Competent%20Authority.csv"))
time.sleep(2)

client.query(critical_functions.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Critical%20Functions.csv"))
time.sleep(2)

client.query(critical_ict_proider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Critical%20ICT%20Provider.csv"))
time.sleep(2)

client.query(cyber_threat.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Cyber%20Threat.csv"))
time.sleep(2)

client.query(facility.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Facility.csv"))
time.sleep(2)

client.query(ict_risk.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20ICT%20Risk.csv"))
time.sleep(2)

client.query(financial_entity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Financial%20Entity.csv"))
time.sleep(2)


client.query(ict_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20ICT%20Control.csv"))
time.sleep(2)

client.query(ict_service.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20ICT%20Service.csv"))
time.sleep(2)


client.query(information_asset.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Inforamtion%20Asset.csv"))
time.sleep(2)

client.query(ict_asset.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20ICT%20Asset.csv")) 
time.sleep(2) 

client.query(joint_examination_term.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Joint%20Examination%20Team.csv"))
time.sleep(2)

client.query(jurisdiction.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Jurisdiction.csv"))
time.sleep(2)

client.query(lead_overeseer.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Lead%20Overseer.csv"))
time.sleep(2)

client.query(legacy_ict_systems.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Legacy%20ICT%20System.csv"))
time.sleep(2)

client.query(major_incident.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Major%20Incident.csv"))
time.sleep(2)

client.query(management_body.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Management%20Body.csv"))
time.sleep(2)

client.query(network_systems.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Network%20Systems.csv"))
time.sleep(2)

client.query(oversight_forum.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Oversight%20Forum.csv"))
time.sleep(2)

client.query(penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Penalty.csv"))
time.sleep(2)

client.query(processing_location.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Processing%20Location.csv"))
time.sleep(2)

client.query(remediation_plan.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Remediation%20Plan.csv"))
time.sleep(2)

client.query(requirements.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Requirements.csv"))
time.sleep(2)
              
client.query(third_party_service_provider.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-ICT%20Third%20Party%20Service%20Provider.csv"))
time.sleep(2)

client.query(subsidiary.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Subsidiary.csv"))
time.sleep(2)

client.query(threat_led_penetration_test.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/DORA/DORA%20-%20Threat%20Led%20Penetration%20Test.csv"))
time.sleep(2)

# Relationships
client.query(reg_to_chapters)
time.sleep(2)

client.query(chapters_to_articles)
time.sleep(2)

client.query(articles_to_requirements)
time.sleep(2)

client.query(competent_authority_financial_entity)
time.sleep(2)

client.query(lead_overseer_critical_ict_providers)
time.sleep(2)

client.query(management_body_financial_entity)
time.sleep(2)

client.query(joint_examination_team_lead_overseer)
time.sleep(2)

client.query(oversight_forum_lead_overseer)
time.sleep(2)

client.query(financial_entity_ict_risk)
time.sleep(2)

client.query(ict_control_mitigates_ict_risk)
time.sleep(2)

client.query(financial_entity_owns_assets)
time.sleep(2)

client.query(ict_service_assets)
time.sleep(2)

client.query(network_systems_ict_services)
time.sleep(2)

client.query(financial_entity_reports_major_incident)
time.sleep(2)

client.query(major_incident_competent_authority)
time.sleep(2)

client.query(financial_entity__tlpt)
time.sleep(2)

client.query(remediation_plan_tlpt)
time.sleep(2)

client.query(financial_entity_third_party)
time.sleep(2)

client.query(third_party_ict_service)
time.sleep(2)

client.query(third_party_subsidiary)
time.sleep(2)

client.query(third_party_processing_location)
time.sleep(2)

client.query(reg_jurisdiction)
time.sleep(2)

client.query(competent_authority_jurisdiction)
time.sleep(2)

client.query(financial_entity_critical_functions)
time.sleep(2)

client.query(ict_services_critical_functions)
time.sleep(2)

client.query(cyber_threat_ict_risk)
time.sleep(2)

client.query(cyber_threat_major_incident)
time.sleep(2)

client.query(financial_entity_facility)
time.sleep(2)

client.query(facility_ict_asset)
time.sleep(2)

client.query(financial_entity_legacy_ict_systems)
time.sleep(2)

client.query(legacy_system_ict_risk)
time.sleep(2)

client.query(competent_authority_penalty)
time.sleep(2)

client.query(reg_defines_penalty)
time.sleep(2)

client.query(critical_functions_critical_ict_providers)
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

results = client.query(query)

if results and len(results) > 0:
    graph_data = results[0]['graph_data']
    
    import json
    with open('dora.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to dora.json")
else:
    logger.error("No data returned from the query.")

client.close()