# Create GDPR Regulation Node
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
  f.legalType = row.Type,s
  f.version = row.Version,
  f.region = row.Region,
  f.effectiveDate = row.Effective_Date,
  f.description = row.Description;
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
MERGE (reg)-[:REGIONAL_STANDARD_REGULATION_HAS_RECITAL {order: row.Properties}]->(r);
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
MERGE (reg)-[:REGIONAL_REGULATION_HAS_LEGISLATIVE_ACTION {order: row.Properties}]->(la);
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

logger.info("Graph structure loaded successfully.")

output_filename = "gdpr.json"

res = client.query("""
    MATCH path = (:RegionalStandardAndRegulation)-[*]->()
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
    } AS graph_data
""")

if isinstance(res, str):
    logger.error(f"✗ Export query failed: {res}")
    client.close()
    sys.exit(1)

if not res or len(res) == 0:
    logger.warning(" No data returned from export query")
    client.close()
    sys.exit(1)

graph_data = res[0].get('graph_data', res[0])

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, default=str, ensure_ascii=False)

node_count = len(graph_data.get('nodes', []))
link_count = len(graph_data.get('links', []))

logger.info(f" Exported {node_count} nodes and {link_count} relationships")
logger.info(f" Graph data saved to: {output_filename}") 

client.close()





