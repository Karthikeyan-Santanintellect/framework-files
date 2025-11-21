# Create GDPR Regulation Node
regulation = """
MERGE (reg:Regulation {regulation_id: 'GDPR'})
ON CREATE SET
    reg.regulation_name = "General Data Protection Regulation",
    reg.official_citation = "Regulation (EU) 2016/679",
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
MERGE (c:Chapter {id: row.Node_ID})
ON CREATE SET
  c.number = toInteger(row.Chapter_Number),
  c.type = row.Node_Type,
  c.name = row.Name,
  c.articleRange = row.Article_Range,
  c.totalArticles = toInteger(row.Total_Articles),
  c.totalSections = toInteger(row.Total_Sections);
"""

# Create GDPR Section Node
gdpr_section = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CREATE (s:Section {id: row.Node_ID})
ON CREATE SET
  s.type = row.Node_Type,
  s.sectionNumber = row.Section_Number,
  s.chapter = row.Chapter,
  s.name = row.Name,
  s.articleRange = row.Article_Range;
"""

# Create GDPR Article Node
gdpr_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MEREG (a:Article {id: row.Node_ID})
ON CREATE SET
  a.type = row.Node_Type,
  a.number = toInteger(row.Article_Number),
  a.title = row.Title,
  a.chapter = row.Chapter,
  a.section = row.Section;
"""

# Create GDPR Recital Node
gdpr_recital = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (r:Recital {id: row.Node_ID}
ON CREATE SET
  r.type = row.Node_Type
  r.number  = toInteger(row.Recital_Number),
  r.title = row.Title;
"""

# Create GDPR Paragraph Node
gdpr_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph {id: row.Node_ID})
ON CREATE SET
    p.id = row.Article_ID
    p.type = row.Node_Type
    p.number = row.Paragraph_Number,
    p.article = row.Article,
    p.description = row.description;
"""

# Create GDPR Sub_Paragraph Node
gdpr_sub_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (sp:SubParagraph {id: row.Node_ID})
ON CREATE SET
  sp.type = row.Node_Type
  sp.letter = row.Sub_Paragraph_Letter,
  sp.paragraph = toInteger(row.Paragraph),
  sp.paragraphId = row.Paragraph_ID,
  sp.article = toInteger(row.Article),
  sp.description: row.Description;
"""

# Create GDPR Legistlative_Action Node
gdpr_legislative_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (la:LegislativeAction {id: row.Node_ID})
ON CREATE SET
  la.type = row.Node_Type
  la.actionType = row.Action_Type,
  la.title = row.Title,
  la.date = row.Date,
  la.description = row.Description;
"""
# Create GDPR Concept Node
gdpr_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Concept {id: row.Node_ID})
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
MERGE (f:Framework {id: row.Node_ID})
  f.type = row.Node_Type
  f.name = row.Framework_Name,
  f.type =row.Type,
  f.region = row.Region,
  f.description = row.Description;
"""
# Regulation → Chapter Relationships (11 relationships)
regulation_chapter_rel ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {id: row.Source_ID})
MATCH (c:Chapter {id: row.Target_ID})
MERGE (reg)-[:HAS_CHAPTER {order: row.Properties}]->(c);
"""

# Regulation → Recital Relationships 
regulation_recital_rel ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {id: row.Source_ID})
MATCH (r:Recital {id: row.Target_ID})
MERGE (reg)-[:HAS_RECITAL {order: row.Properties}]->(r);
"""
# Chapter → Section Relationships 
chapter_section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {id: row.Source_ID})
MATCH (s:Section {id: row.Target_ID})
MERGE (c)-[:CONTAINS_SECTION {order: row.Properties}]->(s);
"""
# Chapter → Article Relationships 
chapter_article ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (c:Chapter {id: row.Source_ID})
MATCH (a:Article {id: row.Target_ID})
MERGE (c)-[:CONTAINS_ARTICLE {order: row.Properties}]->(a);
"""

# Section → Article Relationships 
section_article ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Section {id: row.Source_ID})
MATCH (a:Article {id: row.Target_ID})
MERGE (s)-[:CONTAINS_ARTICLE {order: row.Properties}]->(a);
"""

#  Article → Recital Relationships 
article_recital ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {id: row.Source_ID})
MATCH (r:Recital {id: row.Target_ID})
MERGE (a)-[:SUPPORTED_BY {order: row.Properties}]->(r);
"""

# Article → Paragraph Relationships 
article_section ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {id: row.Source_ID})
MATCH (p:Paragraph {id: row.Target_ID})
MERGE (a)-[:HAS_PARAGRAPH {order: row.Properties}]->(p);
"""
# Paragraph → SubParagraph Relationships 
paragraph_sub_paragraph ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (p:Paragraph {id: row.Source_ID})
MATCH (sp:SubParagraph {id: row.Target_ID})
MERGE (p)-[:HAS_SUB_PARAGRAPH {order: row.Properties}]->(sp);
"""

# Regulation → LegislativeAction Relationships
regulation_legislative_action ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {id: row.Source_ID})
MATCH (la:LegislativeAction {id: row.Target_ID})
MERGE (reg)-[:HAS_LEGISLATIVE_ACTION {order: row.Properties}]->(la);
"""

# Regulation → Framework Relationships
regulation_framework ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {id: row.Source_ID})
MATCH (f:Framework {id: row.Target_ID})
MERGE (reg)-[:PART_OF_FRAMEWORK]->(f);
"""

# Article → Concept Relationships 
article_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {id: row.Source_ID})
MATCH (co:Concept {id: row.Target_ID})
MERGE (a)-[:DEFINES_CONCEPT {properties: row.Properties}]->(co);
"""
# Recital → Concept Relationships 
Recital_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Recital {id: row.Source_ID})
MATCH (co:Concept {id: row.Target_ID})
MERGE (a)-[:DEFINES_CONCEPT {properties: row.Properties}]->(co);
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

client.query(regulation)
time.sleep(2)

client.query(gdpr_framework.replace('$file_path',
                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Framework.csv"))
time.sleep(2)

client.query(gdpr_recital.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Recital.csv"))
time.sleep(2)


client.query(gdpr_chapter.replace('$file_path',
                                               "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Chapter.csv"))
time.sleep(2)

client.query(gdpr_article.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Article.csv"))
time.sleep(2)

client.query(gdpr_concept.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Concept.csv"))
time.sleep(2)

client.query(gdpr_legislative_action.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_LegislativeAction.csv"))
time.sleep(2)

client.query(gdpr_paragraph.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GDPR_Paragraph.csv"))
time.sleep(2)


client.query(gdpr_regulation_framework)
time.sleep(2)

client.query(gdpr_has_chapter.replace('$file_path',
                                              "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/HAS_CHAPTER_CORRECTED.csv"))
time.sleep(2)

client.query(gdpr_contains_article.replace('$file_path',
                                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_ARTICLE_CORRECTED.csv"))
time.sleep(2)

client.query(gdpr_contains_paragraph.replace('$file_path',
                                                            "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_PARAGRAPH_CORRECTED.csv"))
time.sleep(2)

client.query(gdpr_provides_context_for.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/PROVIDES_CONTEXT_FOR.csv"))
time.sleep(2)

client.query(gdpr_specializes_provisions_of.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/SPECIALIZES_PROVISIONS_OF.csv"))
time.sleep(2)

client.query(gdpr_defines_concept.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/DEFINES_CONCEPT.csv"))
time.sleep(2)

client.query(gdpr_implements_principle.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/IMPLEMENTS_PRINCIPLE.csv"))
time.sleep(2)

client.query(gdpr_establishes_criteria.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/ESTABLISHES_CRITERIA.csv"))
time.sleep(2)

client.query(gdpr_mandates_requirement.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/MANDATES_REQUIREMENT.csv"))
time.sleep(2)

client.query(gdpr_defines_responsibility.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/DEFINES_RESPONSIBILITY.csv"))
time.sleep(2)

client.query(gdpr_governs_procedure.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/GOVERNS_PROCEDURE.csv"))
time.sleep(2)

client.query(gdpr_requires_action.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/REQUIRES_ACTION.csv"))
time.sleep(2)

client.query(gdpr_affects_provision.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/AFFECTS_PROVISION.csv"))
time.sleep(2)





logger.info("Graph structure loaded successfully.")

res=client.query("MATCH path = (:Regulation {regulation_id: 'GDPR'})-[*]->() return path")

import json
with open('gdpr.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(res, default=str))

client.close()





