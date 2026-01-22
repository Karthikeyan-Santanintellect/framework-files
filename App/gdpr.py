# regulation
regional_standard_and_regulation = """
MERGE (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
    reg.name = "General Data Protection Regulation",
    reg.citation = "Regulation (EU) 2016/679",
    reg.version = "2016/679",
    reg.publication_date = date("2018-05-25"),
    reg.effective_date = date("2018-05-25"),
    reg.type = "EU Legislative",
    reg.jurisdiction = "EU/EEA",
    reg.description = "Comprehensive European regulation governing data protection and privacy for all individuals within the European Union and the European Economic Area";
"""

# Create GDPR chapter Node
gdpr_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (c:Chapter {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  c.number = row.Chapter_Number,
  c.type = row.Node_Type,
  c.name = row.Name,
  c.articleRange = row.Article_Range,
  c.totalArticles = toInteger(row.Total_Articles),
  c.totalSections = toInteger(row.Total_Sections);
"""

# Create GDPR Section Node
gdpr_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Section {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  s.type = row.Node_Type,
  s.number = row.Section_Number,
  s.chapter = row.Chapter,
  s.name = row.Name,
  s.articleRange = row.Article_Range;
"""

# Create GDPR Article Node
gdpr_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (a:Article {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  a.type = row.Node_Type,
  a.number = row.Article_Number,
  a.title = row.Title,
  a.chapter = row.Chapter,
  a.section = row.Section;
"""

# Create GDPR Recital Node
gdpr_recital = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Recital {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  r.type = row.Node_Type,
  r.number = row.Recital_Number,
  r.title = row.Title;
"""

# Create GDPR Paragraph Node
gdpr_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
    p.articleId = row.Article_ID,
    p.type = row.Node_Type,
    p.number = row.Paragraph_Number,
    p.article = row.Article,
    p.description = row.Description;
"""

# Create GDPR Sub_Paragraph Node
gdpr_sub_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:SubParagraph {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  sp.type = row.Node_Type,
  sp.letter = row.Sub_Paragraph_Letter,
  sp.paragraph = row.Paragraph,
  sp.paragraphId = row.Paragraph_ID,
  sp.article = row.Article,
  sp.description = row.Description;
"""

# Create GDPR Legistlative_Action Node
gdpr_legislative_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (la:LegislativeAction {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  la.type = row.Node_Type,
  la.actionType = row.Action_Type,
  la.title = row.Title,
  la.date = row.Date,
  la.description = row.Description;
"""
# Create GDPR Concept Node
gdpr_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Concept {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  co.type = row.Node_Type,
  co.name = row.Concept_Name,
  co.category = row.Category,
  co.primaryArticle = row.Primary_Article,
  co.description = row.Description;
"""
# Create GDPR Framework Node
gdpr_framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {Node_ID: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  f.type = row.Node_Type,
  f.frameworkName = row.Framework_Name,
  f.legalType = row.Type,
  f.version = row.Version,
  f.region = row.Region,
  f.effectiveDate = row.Effective_Date,
  f.description = row.Description;
"""

#ActorRole
gdpr_actor_role ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:ActorRole {actor_role_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  ar.name = row.name,
  ar.type = row.type,
  ar.definition = row.definition,
  ar.parent_concept = row.parent_concept,
  ar.regulated_by_articles = row.regulated_by_articles;
  """
#Datacategory
gdpr_data_category ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (dc:DataCategory {data_category_id: row.Node_ID,regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
dc.name = row.name,
  dc.definition = row.definition,
  dc.level = row.level,
  dc.parent_category = row.parent_category,
  dc.is_restricted = row.is_restricted,
  dc.regulated_by_articles = row.regulated_by_articles;
"""
#Data Subjects
gdpr_data_subject ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ds:DataSubjectRight {data_subject_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  ds.name = row.name,
  ds.definition = row.definition,
  ds.regulated_by_articles = row.regulated_by_articles,
  ds.applies_to_actors = row.applies_to_actors,
  ds.enforcement_mechanism = row.enforcement_mechanism;
"""
#Lawful_basis
gdpr_lawful_basis ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (lb:LawfulBasis {lawful_basis_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  lb.name = row.name,
  lb.definition = row.definition,
  lb.type = row.type,
  lb.restricted = row.restricted,
  lb.regulated_by_articles = row.regulated_by_articles,
  lb.use_cases = row.use_cases;
"""
#Principle 
gdpr_principle ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pl:Principle {principle_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pl.name = row.name,
  pl.definition = row.definition,
  pl.aspect = row.aspect,
  pl.regulated_by_articles = row.regulated_by_articles,
  pl.applies_to_processing = row.applies_to_processing,
  pl.applies_to_data_category = row.applies_to_data_category;
"""
#Processing_activity
gdpr_processing_activity ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pa:ProcessingActivity {processing_id : row.Node_ID,regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pa.name = row.name,
  pa.definition = row.definition,
  pa.category = row.category,
  pa.regulated_by_articles = row.regulated_by_articles,
  pa.requires_lawful_basis = row.requires_lawful_basis,
  pa.requires_principle_compliance = row.requires_principle_compliance;
"""

#ComplianceMechanism
gdpr_compliance_mechanism ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (cm:ComplianceMechanism {mechanism_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  cm.name = row.name,
  cm.definition = row.definition,
  cm.category = row.category,
  cm.is_mandatory = row.is_mandatory,
  cm.regulated_by_articles = row.regulated_by_articles,
  cm.applicable_to_roles = row.applicable_to_roles;
"""
#ProcessingContext
gdpr_processing_context ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pc:ProcessingContext {context_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pc.name = row.name,
  pc.description = row.description,
  pc.special_requirements = row.special_requirements,
  pc.regulated_by_articles = row.regulated_by_articles,
  pc.applies_to_data_categories = row.applies_to_data_categories,
  pc.applies_to_processing_activities = row.applies_to_processing_activities;
"""
#Penalty 
gdpr_penalty ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pen:Penalty {penalty_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pen.type = row.penalty_type,
  pen.name = row.name,
  pen.definition = row.definition,
  pen.max_amount = row.max_amount,
  pen.min_amount = row.min_amount,
  pen.violation_category = row.violation_category,
  pen.regulated_by_articles = row.regulated_by_articles,
  pen.applicable_to_actors = row.applicable_to_actors;
"""

#TRANSFER MECHANISM
gdpr_transfer_mechanism ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tm:TransferMechanism {
  transfer_id: row.Node_ID,
  regional_standard_regulation_id: 'GDPR 2016/679'
})
ON CREATE SET
  tm.name = row.name,
  tm.definition = row.definition,
  tm.type = row.Node_Type,
  tm.mechanism_id = row.mechanism_id,
  tm.regulated_by_articles = row.regulated_by_articles,
  tm.applies_to_countries = row.applies_to_countries,
  tm.effectiveness_level = row.effectiveness_level;
"""
#EnforcementAuthority
gdpr_enforcement_authority ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ea:EnforcementAuthority {enforcement_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  ea.Node_ID = row.Node_ID,
  ea.name = row.name,
  ea.definition = row.definition,
  ea.role = row.role,
  ea.powers = row.powers,
  ea.regulated_by_articles = row.regulated_by_articles,
  ea.applies_to_jurisdictions = row.applies_to_jurisdictions;
  """

# Technical & Organisational Measures
technical_organisational_measures ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (tom:TechnicalOrganisationalMeasure {tom_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  tom.name = row.name,
  tom.category = row.category,
  tom.description = row.description,
  tom.supports_principle = row.supports_principle; 
"""
# Personal Data Breach
personal_data_breach ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pdb:PersonalDataBreach {breach_type_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pdb.type = row.type,
  pdb.notification_deadline = row.notification_deadline,
  pdb.requires_authority_notification = row.requires_authority_notification,
  pdb.requires_subject_notification = row.requires_subject_notification;
"""
# Processor Contract
processor_contract ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (pc:ProcessorContract {contract_requirement_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  pc.clause_name = row.clause_name,
  pc.mandatory_content = row.mandatory_content,
  pc.obligates_actor = row.obligates_actor;
"""
# joint Controller Agreement
joint_controller_agreement ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (jca:JointControllerAgreement {agreement_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  jca.name = row.name,
  jca.essence_available_to_subject = toBoolean(row.essence_available_to_subject),
  jca.allocates_responsibility = row.allocates_responsibility;
"""
#Record of Processing Activities
record_of_processing_activities ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ropa:RecordOfProcessingActivities {ropa_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  ropa.content_elements = row.content_elements,
  ropa.legal_basis = "Article 30",
  ropa.last_updated = date(row.last_updated);
"""
# Risk Assessment Outcome
risk_assessment_outcome ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rao:RiskAssessmentOutcome {outcome_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  rao.risk_level = row.risk_level,
  rao.triggers_consultation = toBoolean(row.triggers_consultation);
"""
# Infringement (Violation Event)
infringement_violation_event ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (inf:Infringement {infringement_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  inf.name = row.name,
  inf.violates_article = row.violates_article,
  inf.triggers_penalty = row.triggers_penalty;
"""
#Senior Management
senior_management ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sm:SeniorManagement {management_role_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  sm.title = row.title,
  sm.reports_received = row.reports_received;
"""
#Representative
representative ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (rep:Representative {rep_id: row.Node_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
ON CREATE SET
  rep.name = row.name,
  rep.jurisdiction = row.jurisdiction,
  rep.mandated_by_controller = row.mandated_by_controller;
"""





# Regulation → Chapter Relationships 
regional_standard_regulation_chapter ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (c:Chapter {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (reg)-[:REGIONAL_STANDARD_AND_REGULATION_HAS_CHAPTER {order: row.Properties}]->(c);
"""
#Framework -> chapter Relationships
framework_chapter ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (c:Chapter {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (f)-[:FRAMEWORK_HAS_CHAPTER {order: row.Properties}]->(c);
"""


# Regulation → Recital Relationships 
regional_standard_regulation_recital ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (r:Recital {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (reg)-[:REGIONAL_STANDARD_AND_REGULATION_HAS_RECITAL {order: row.Properties}]->(r);
"""
# Chapter → Section Relationships 
chapter_section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (s:Section {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (c)-[:CHAPTER_CONTAINS_SECTION {order: row.Properties}]->(s);
"""
# Chapter → Article Relationships 
chapter_article ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (c)-[:CHAPTER_CONTAINS_ARTICLE {order: row.Properties}]->(a);
"""

# Section → Article Relationships 
section_article ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (s)-[:SECTION_CONTAINS_ARTICLE {order: row.Properties}]->(a);
"""

#  Article → Recital Relationships 
article_recital ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (r:Recital {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_SUPPORTED_BY_RECITAL {order: row.Properties}]->(r);
"""

# Article → Paragraph Relationships 
article_paragraph ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (p:Paragraph {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_CONTAINS_PARAGRAPH {order: row.Properties}]->(p);
"""
# Recital → Paragraph Relationships
recital_paragraph ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Recital {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (p:Paragraph {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (r)-[:RECITAL_CONTAINS_PARAGRAPH{Properties:row.Properties}]->(p);
"""
# Paragraph → SubParagraph Relationships 
paragraph_sub_paragraph ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (p:Paragraph {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (sp:SubParagraph {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (p)-[:PARAGRAPH_HAS_SUB_PARAGRAPH {order: row.Properties}]->(sp);
"""

# Regulation → LegislativeAction Relationships
regional_standard_regulation_legislative_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (la:LegislativeAction {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (reg)-[:REGIONAL_STANDARD_AND_REGULATION_HAS_LEGISLATIVE_ACTION {order: row.Properties}]->(la);
"""




# Article → Concept Relationships 
article_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (co:Concept {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_DEFINES_CONCEPT {properties: row.Properties}]->(co);
"""
# Recital → Concept Relationships 
recital_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Recital {Node_ID: row.Source_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (co:Concept {Node_ID: row.Target_ID, regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (r)-[:RECITAL_DEFINES_CONCEPT {properties: row.Properties}]->(co);
"""

#Data_category -> RegionalStandardRegulation
datacategory_regulation ="""
MATCH (dc:DataCategory {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (dc)-[:DATA_CATEGORY_PROTECTED_BY_REGULATION]->(reg);
"""
#Processing_activity ->RegionalStandardRegulation
processing_activity_regulation ="""
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pa)-[:PROCESSING_ACTIVITY_REGULATED_BY_REGULATION]->(reg);
"""
#LawfulBasis -> RegionalStandardAndRegulation
lawful_basis_regulation ="""
MATCH (lb:LawfulBasis {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (lb)-[:LAWFUL_BASIS_REQUIRED_BY_REGULATION]->(reg);
"""
# Principle → RegionalStandardAndRegulation
principle_regulation ="""
MATCH (pl:Principle {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (p)-[:PRINCIPLE_EMBODIED_IN_REGULATION]->(reg);
"""
#ComplianceMechanism → RegionalStandardAndRegulation
compliance_mechanism_regulation ="""
MATCH (cm:ComplianceMechanism {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (reg:RegionalStandardAndRegulation {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (cm)-[:COMPLIANCE_MECHANISM_DEFINED_BY_REGULATION]->(reg);
"""
#DataSubjectRight→ ActorRole (Data Subject)
data_subject_actor_role ="""
MATCH (ds:DataSubjectRight {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (dr)-[:DATA_SUBJECT_RIGHT_HELD_BY_ACTOR_ROLE]->(ar);
"""
#Article → ActorRole
article_actor_role ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ar:ActorRole{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_DEFINES_ACTOR_ROLE]->(ar);
"""
#Article → DataCategory
article_data_category ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (dc:DataCategory{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_DEFINES_DATA_CATEGORY]->(dc);
"""
#Article → DataSubjectRight
article_data_subject ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ds:DataSubjectRight{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_DEFINES_DATA_SUBJECT_RIGHT]->(ds);
"""
#Article → LawfulBasis
article_lawful_basis ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (lb:LawfulBasis{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_SPECIFIES_LAWFUL_BASIS]->(lb);
"""
#Article → Principle
article_principle ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pl:Principle{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_EMBODIES_PRINCIPLE]->(pl);
"""
#Article → ProcessingActivity
article_processing_activity ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pa:ProcessingActivity{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_REGULATES_PROCESSING_ACTIVITY]->(pa);
"""
#Article → ComplianceMechanism
article_compliance_mechanism ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (cm:ComplianceMechanism{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_DEFINES_OBLIGATION]->(cm);
"""
#Article → TransferMechanism
article_transfer_mechanism ="""
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (tm:TransferMechanism{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[:ARTICLE_REGULATES_TRANSFER]->(tm);
"""
# Penalty → Article
penalty_article ="""
MATCH (pen:Penalty {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pen)-[:PENALTY_DEFINED_BY_ARTICLE]->(a);
"""

# DataSubjectRight → Article
datasubject_right_article ="""
MATCH (ds:DataSubjectRight {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ds)-[:DATA_SUBJECT_RIGHT_ENFORCED_BY_ARTICLE]->(a);
"""

# DataSubjectRight → EnforcementAuthority
datasubject_right_enforcement_authority ="""
MATCH (ds:DataSubjectRight {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ea:EnforcementAuthority{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ds)-[:DATA_SUBJECT_RIGHT_ENFORCED_BY_ENFORCEMENT_AUTHORITY]->(ea);
"""
#EnforcementAuthority → Article
enforcement_authority_article ="""
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ea)-[:ENFORCEMENT_AUTHORITY_ENFORCES_ARTICLE]->(a);
"""
#EnforcementAuthority → Penalty
enforcement_authority_penalty ="""
MATCH (ea:EnforcementAuthority {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pen:Penalty{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ea)-[:ENFORCEMENT_AUTHORITY_IMPOSES_PENALTY ]->(pen);
"""
#Penalty → ComplianceMechanism
penalty_compliance_mechanism = """
MATCH (pen:Penalty{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (cm:ComplianceMechanism{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pen)-[:PENALTY_IMPOSES_COMPLIANCE_MECHANISM]->(cm)
"""
#Penalty → Article
penalty_article ="""
MATCH (pen:Penalty{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pen)-[:PENALTY_FOR_VIOLATION_OF_ARTICLE]->(a);
"""
#Article → ProcessingContext
article_processing_context ="""
MATCH (a:Article{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pc:ProcessingContext{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (a)-[: ARTICLE_APPLIES_TO_PROCESSING_CONTEXT]->(pc);
"""
#ProcessingContext →  Principle
processing_context_principle ="""
MATCH (pc:ProcessingContext{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pl:Principle{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pc)-[:PROCESSING_CONTEXT_SUBJECT_TO_PRINCIPLE]->(pl);
"""
#ProcessingContext -> ComplianceMechanism
processing_context_compliance_mechanism ="""
MATCH (pc:ProcessingContext{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (cm:ComplianceMechanism{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pc)-[:PROCESSING_CONTEXT_REQUIRES_MECHANISM]->(cm);
"""
#ProcessingContext -> TransferMechanism
processing_context_transfer_mechanism =""" 
MATCH (pc:ProcessingContext{regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (tm:TransferMechanism {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (pc)-[:PROCESSING_CONTEXT_REQUIRES_TRANSFER_MECHANISM]->(tm);
"""
#DataCategory → TransferMechanism
datacategory_transfer_mechanism ="""
MATCH (dc:DataCategory {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (tm:TransferMechanism {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (dc)-[:DATA_CATEGORY_CAN_BE_TRANSFERRED]->(tm);
"""
#ActorRole → ProcessingActivity
actor_role_processing_activity ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pa:ProcessingActivity{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:ACTOR_ROLE_PERFORMS_PROCESSING_ACTIVITY]->(pa);
"""
#ActorRole → DataCategory
actor_role_data_category ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (dc:DataCategory {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:ACTOR_ROLE_RESPONSIBLE_FOR_DATA_CATEGORY]->(dc);
"""
#ActorRole → ComplianceMechanism
actor_role_compliance_mechanism ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (cm:ComplianceMechanism{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:ACTOR_ROLE_OVERSEES_COMPLIANCE_MECHANISM]->(cm);
"""
#ActorRole → Principle
actor_role_principle ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pl:Principle{regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:ACTOR_ROLE_MUST_COMPLY_WITH_PRINCIPLE]->(pl);
"""
# Controller -> TOMs
controller_tom ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Controller'})
MATCH (tom:TechnicalOrganisationalMeasure {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:ACTOR_ROLE_IMPLEMENTS_MEASURE]->(tom);
"""
# TOMs -> Principle
tom_principle ="""
MATCH (tom:TechnicalOrganisationalMeasure {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (p:Principle {regional_standard_regulation_id: 'GDPR 2016/679'})
WHERE tom.supports_principle CONTAINS p.name
MERGE (tom)-[:TECHNICAL_ORGANISATIONAL_MEASURES_SUPPORTS_PRINCIPLE]->(p);
"""
# Breach -> Authority
breach_authority ="""
MATCH (pdb:PersonalDataBreach {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Protection Authority'})
WHERE pdb.requires_authority_notification = true
MERGE (pdb)-[:PERSONAL_DATA_BREACH_REQUIRES_AUTHORITY_NOTIFICATION]->(ar);
"""
# Breach -> Article
breach_article = """
MATCH (pdb:PersonalDataBreach {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
WHERE pdb.regulated_by_articles CONTAINS toString(a.number)
MERGE (pdb)-[:DATA_BREACH_IS_SUBJECT_TO_ARTICLE]->(a);
"""
# Controller -> RoPA
controller_ropa ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Controller'})
MATCH (ropa:RecordOfProcessingActivities {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:CONTROLLER_MAINTAINS_RECORD]->(ropa);
"""
# RoPA -> Processing Activity
ropa_processing_activity ="""
MATCH (ropa:RecordOfProcessingActivities {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pa:ProcessingActivity {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ropa)-[:RECORD_OF_PROCESSING_ACTIVITIES_CONTAINS_PROCESSING_ACTIVITY]->(pa);
"""
# DPIA -> Risk Outcome
dpia_risk_outcome ="""
MATCH (cm:ComplianceMechanism {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Protection Impact Assessment (DPIA)'})
MATCH (rao:RiskAssessmentOutcome {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (cm)-[:COMPLIANCE_MECHANISM_IMPOSES_RISK_ASSESSMENT]->(rao);
"""

# Risk Outcome -> Authority
rao_authority ="""
MATCH (rao:RiskAssessmentOutcome {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Protection Authority'})
WHERE rao.triggers_consultation = true
MERGE (rao)-[:RISK_ASSESSMENT_OUTCOME_REQUIRES_AUTHORITY_NOTIFICATION]->(ar);
"""
# Controller -> Processor Contract
controller_processor_contract ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Controller'})
MATCH (pc:ProcessorContract {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:DATA_CONTROLLER_ENFORCES_CONTRACT]->(pc);
"""
# Processor Contract -> Processor
processor_contract_processor ="""
MATCH (pc:ProcessorContract {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Processor'})
WHERE pc.obligates_actor = 'Processor' OR pc.obligates_actor = 'Data Processor'
MERGE (pc)-[:PROCESSOR_CONTRACT_OBLIGATES_ACTOR]->(ar);
"""

# Joint Controller -> Agreement
joint_controller_jca ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Joint Controller'})
MATCH (jca:JointControllerAgreement {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:JOINT_CONTROLLER_HAS__AGREEMENT]->(jca);
"""
# Infringement -> Article
infringement_article ="""
MATCH (inf:Infringement {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (a:Article {regional_standard_regulation_id: 'GDPR 2016/679'})
WHERE inf.violates_article CONTAINS toString(a.number)
MERGE (inf)-[:INFRINGEMENT_VIOLATES_ARTICLE]->(a);
"""
# Infringement -> Penalty
infringement_penalty ="""
MATCH (inf:Infringement {regional_standard_regulation_id: 'GDPR 2016/679'})
MATCH (pen:Penalty {regional_standard_regulation_id: 'GDPR 2016/679'})
WHERE inf.triggers_penalty = pen.penalty_id OR inf.tier_level = pen.violation_category
MERGE (inf)-[:INFRINGEMENT_TRIGGERS_PENALTY]->(pen);
"""
# DPO -> Senior Management
dpo_senior_management ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Protection Officer'})
MATCH (sm:SeniorManagement {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:DATA_PROTECTION_OFFICER_REPORTS_DIRECTLY_TO_SENIOR_MANAGEMENT]->(sm);
"""
# Controller -> Representative
controller_representative ="""
MATCH (ar:ActorRole {regional_standard_regulation_id: 'GDPR 2016/679', name: 'Data Controller'})
MATCH (rep:Representative {regional_standard_regulation_id: 'GDPR 2016/679'})
MERGE (ar)-[:CONTROLLER_HAS_REPRESENTATIVE]->(rep);
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

client.query(regional_standard_and_regulation)
time.sleep(2)

client.query(gdpr_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/2_chapter_nodes.csv"))
time.sleep(2)

client.query(gdpr_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/3_section_nodes.csv"))
time.sleep(2)

client.query(gdpr_article.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/article_node.csv"))
time.sleep(2)

client.query(gdpr_recital.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/5_recital_nodes.csv"))
time.sleep(2)

client.query(gdpr_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/12_paragraph_nodes.csv"))
time.sleep(2)

client.query(gdpr_sub_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/13_subparagraph_nodes.csv"))
time.sleep(2)

client.query(gdpr_legislative_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/14_legislative_action_nodes.csv"))
time.sleep(2)

client.query(gdpr_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/15_concept_nodes_COMPLETE.csv"))
time.sleep(2)

client.query(gdpr_framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/1_framework_nodes_CORRECTED.csv"))
time.sleep(2)

client.query(gdpr_actor_role.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_ActorRoles.csv"))
time.sleep(2)

client.query(gdpr_data_category.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_DataCategories.csv"))
time.sleep(2)

client.query(gdpr_data_subject.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_DataSubjectRights.csv"))
time.sleep(2)

client.query(gdpr_lawful_basis.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_LawfulBasis.csv"))
time.sleep(2)

client.query(gdpr_principle.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_Principles.csv"))
time.sleep(2)

client.query(gdpr_processing_activity.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_ProcessingActivities.csv"))
time.sleep(2)

client.query(gdpr_compliance_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_ComplianceMechanisms.csv"))
time.sleep(2)

client.query(gdpr_processing_context.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_ProcessingContexts.csv"))
time.sleep(2)

client.query(gdpr_penalty.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_Penalties.csv"))
time.sleep(2)

client.query(gdpr_transfer_mechanism.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_TransferMechanisms.csv"))
time.sleep(2)


client.query(gdpr_enforcement_authority.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/GDPR_EnforcementAuthorities.csv"))
time.sleep(2)

client.query(technical_organisational_measures.replace('$file_path',""))
time.sleep(2)

client.query(personal_data_breach.replace('$file_path',""))
time.sleep(2)

client.query(processor_contract.replace('$file_path',""))
time.sleep(2)

client.query(joint_controller_agreement.replace('$file_path',""))
time.sleep(2)

client.query(record_of_processing_activities.replace('$file_path',""))
time.sleep(2)

client.query(risk_assessment_outcome.replace('$file_path',""))
time.sleep(2)

client.query(infringement_violation_event.replace('$file_path',""))
time.sleep(2)

client.query(senior_management.replace('$file_path',""))
time.sleep(2)

client.query(representative.replace('$file_path',""))
time.sleep(2)




# Relationships
client.query(regional_standard_regulation_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/6_relationships_regulation_to_chapter.csv"))
time.sleep(2)

client.query(framework_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/16_relationships_framework_to_chapter_UNIQUE.csv"))
time.sleep(2)

client.query(regional_standard_regulation_recital.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/7_relationships_regulation_to_recital.csv"))
time.sleep(2)

client.query(chapter_section.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/8_relationships_chapter_to_section.csv"))
time.sleep(2)

client.query(chapter_article.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/9_relationships_chapter_to_article.csv"))
time.sleep(2)

client.query(section_article.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/10_relationships_section_to_article.csv"))
time.sleep(2)

client.query(article_recital.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/11_relationships_article_to_recital.csv"))
time.sleep(2)

client.query(article_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/17_relationships_article_to_paragraph.csv"))
time.sleep(2)

client.query(recital_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/23_relationships_recital_to_paragraph_CLEANED.csv"))
time.sleep(2)

client.query(paragraph_sub_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/18_relationships_paragraph_to_subparagraph.csv"))
time.sleep(2)

client.query(regional_standard_regulation_legislative_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/19_relationships_regulation_to_legislative_action.csv"))
time.sleep(2)

client.query(article_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/21_relationships_article_to_concepts.csv"))
time.sleep(2)

client.query(recital_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/22_relationships_recital_to_concepts.csv"))
time.sleep(2)

client.query(datacategory_regulation)
time.sleep(2)

client.query(processing_activity_regulation)
time.sleep(2)

client.query(lawful_basis_regulation)
time.sleep(2)

client.query(principle_regulation)
time.sleep(2)

client.query(compliance_mechanism_regulation)
time.sleep(2)

client.query(data_subject_actor_role)
time.sleep(2)

client.query(article_actor_role)
time.sleep(2)

client.query(article_data_category)
time.sleep(2)

client.query(article_data_subject)
time.sleep(2)

client.query(article_lawful_basis)
time.sleep(2)

client.query(article_principle)
time.sleep(2)

client.query(article_processing_activity)
time.sleep(2)

client.query(article_compliance_mechanism)
time.sleep(2)

client.query(article_transfer_mechanism)
time.sleep(2)

client.query(penalty_article)
time.sleep(2)

client.query(datasubject_right_article)
time.sleep(2)

client.query(datasubject_right_enforcement_authority)
time.sleep(2)

client.query(enforcement_authority_article)
time.sleep(2)

client.query(enforcement_authority_penalty)
time.sleep(2)

client.query(penalty_compliance_mechanism)
time.sleep(2)

client.query(penalty_article)
time.sleep(2)

client.query(article_processing_context)
time.sleep(2)

client.query(processing_context_principle)  
time.sleep(2)

client.query(processing_context_compliance_mechanism)
time.sleep(2)

client.query(processing_context_transfer_mechanism)
time.sleep(2)

client.query(datacategory_transfer_mechanism)
time.sleep(2)

client.query(actor_role_processing_activity)
time.sleep(2)

client.query(actor_role_data_category)
time.sleep(2)

client.query(actor_role_compliance_mechanism)
time.sleep(2)

client.query(actor_role_principle)
time.sleep(2)

client.query(controller_tom)
time.sleep(2)

client.query(tom_principle)
time.sleep(2)

client.query(breach_authority)
time.sleep(2)

client.query(breach_article)
time.sleep(2)

client.query(controller_ropa)
time.sleep(2)

client.query(ropa_processing_activity)
time.sleep(2)

client.query(dpia_risk_outcome)
time.sleep(2)

client.query(rao_authority)
time.sleep(2)

client.query(controller_processor_contract)
time.sleep(2)

client.query(processor_contract_processor)
time.sleep(2)

client.query(joint_controller_jca)
time.sleep(2)

client.query(infringement_article)
time.sleep(2)

client.query(infringement_penalty)
time.sleep(2)

client.query(dpo_senior_management)
time.sleep(2)

client.query(controller_representative)
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
    with open('gdpr.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(graph_data, default=str, indent=2))
    logger.info(f"✓ Exported {len(graph_data['nodes'])} nodes and {len(graph_data['rels'])} relationships to gdpr.json")
else:
    logger.error("No data returned from the query.")

client.close()



