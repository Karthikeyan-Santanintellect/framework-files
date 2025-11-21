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
MERGE (s:Section {id: row.Node_ID})
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
MERGE (a:Article {id: row.Node_ID})
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
MERGE (r:Recital {id: row.Node_ID})
ON CREATE SET
  r.type = row.Node_Type,
  r.number  = toInteger(row.Recital_Number),
  r.title = row.Title;
"""

# Create GDPR Paragraph Node
gdpr_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph {id: row.Node_ID})
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
MERGE (sp:SubParagraph {id: row.Node_ID})
ON CREATE SET
  sp.type = row.Node_Type,
  sp.letter = row.Sub_Paragraph_Letter,
  sp.paragraph = row.Paragraph,
  sp.paragraphId = row.Paragraph_ID,
  sp.article = toInteger(row.Article),
  sp.description = row.Description;
"""

# Create GDPR Legistlative_Action Node
gdpr_legislative_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (la:LegislativeAction {id: row.Node_ID})
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
ON CREATE SET
  f.type = row.Node_Type,
  f.name = row.Framework_Name,
  f.frameworkType = row.Type,
  f.version = row.Version,
  f.region = row.Region,
  f.effectiveDate = row.Effective_Date,
  f.description = row.Description;
"""

# Regulation → Chapter Relationships (11 relationships)
regulation_chapter ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {regulation_id: 'GDPR'})
MATCH (c:Chapter {id: row.Target_ID})
MERGE (reg)-[:HAS_CHAPTER {order: row.Properties}]->(c);
"""

# Regulation → Recital Relationships 
regulation_recital ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {regulation_id: 'GDPR'})
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
article_paragraph ="""
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
MATCH (reg:Regulation {regulation_id: 'GDPR'})
MATCH (la:LegislativeAction {id: row.Target_ID})
MERGE (reg)-[:HAS_LEGISLATIVE_ACTION {order: row.Properties}]->(la);
"""

# Regulation → Framework Relationships
regulation_framework ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (reg:Regulation {regulation_id: 'GDPR'})
MATCH (f:Framework {id: row.Target_ID})
MERGE (reg)-[:PART_OF_FRAMEWORK {properties: row.Properties}]->(f);
"""

# Article → Concept Relationships 
article_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (a:Article {id: row.Source_ID})
MATCH (co:Concept {id: row.Target_ID})
MERGE (a)-[:DEFINES_CONCEPT {properties: row.Properties}]->(co);
"""
# Recital → Concept Relationships 
recital_concept ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (r:Recital {id: row.Source_ID})
MATCH (co:Concept {id: row.Target_ID})
MERGE (r)-[:DEFINES_CONCEPT {properties: row.Properties}]->(co);
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


client.query(gdpr_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/15_concept_nodes.csv"))
time.sleep(2)

client.query(gdpr_framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/16_framework_nodes.csv"))
time.sleep(2)

client.query(regulation_chapter.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/6_relationships_regulation_to_chapter.csv"))
time.sleep(2)

client.query(regulation_recital.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/7_relationships_regulation_to_recital.csv"))
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

client.query(paragraph_sub_paragraph.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/18_relationships_paragraph_to_subparagraph.csv"))
time.sleep(2)

client.query(regulation_legislative_action.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/19_relationships_regulation_to_legislative_action.csv"))
time.sleep(2)

client.query(regulation_framework.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/20_relationships_regulation_to_framework.csv"))
time.sleep(2)

client.query(article_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/21_relationships_article_to_concepts.csv"))
time.sleep(2)

client.query(recital_concept.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR_NEW/22_relationships_recital_to_concepts.csv"))
time.sleep(2)


logger.info("Graph structure loaded successfully.")

res=client.query("""MATCH path = (:Regulation)-[*]->()
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
  links: [r IN uniqueRels | r {
    .*,
    id: elementId(r),     
    type: type(r),         
    source: elementId(startNode(r)), 
    target: elementId(endNode(r)) 
  }]
} AS graph_data""")

import json
with open('gdpr.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(res, default=str))

client.close()





