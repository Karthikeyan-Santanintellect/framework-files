# Create GDPR Regulation Node
regulation = """
MERGE (r:Regulation {regulation_id: 'GDPR'})
ON CREATE SET
    r.regulation_name = "General Data Protection Regulation",
    r.official_citation = "Regulation (EU) 2016/679",
    r.version = "2016/679",
    r.publication_date = date("2018-05-25"),
    r.effective_date = date("2018-05-25"),
    r.type = "EU Legislative",
    r.jurisdiction = "EU/EEA",
    r.description = "Comprehensive European regulation governing data protection and privacy for all individuals within the European Union and the European Economic Area";
"""

# Create GDPR Framework Node
gdpr_framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    f.name = row.name,
    f.version = row.version,
    f.effective_date = date(row.effectiveDate),
    f.jurisdiction = row.jurisdiction,
    f.description = row.description;
"""

# Create GDPR Recital Node
gdpr_recital = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ret:Recital {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    ret.recitalNumber = toInteger(row.recitalNumber),
    ret.name = row.name,
    ret.description = row.description;
"""

# Create GDPR Chapter Node
gdpr_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ch:Chapter {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    ch.chapterNumber = toInteger(row.chapterNum),
    ch.name = row.name,
    ch.description = row.description;
"""

# Create GDPR Article Node
gdpr_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:Article {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    ar.articleId = row.articleId,
    ar.name = row.name,
    ar.chapter_id = row.chapter_id,
    ar.chapter_name = row.chapter_name,
    ar.description = row.description;
"""

# Create GDPR Concept Node
gdpr_concept = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Concept {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    co.name = row.name,
    co.category = row.category,
    co.description = row.description;
"""

# Create GDPR LegislativeAction Node
gdpr_legislative_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (l:LegislativeAction {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    l.name = row.name,
    l.proposalDate = date(row.proposalDate),
    l.status = row.status,
    l.description = row.description;
"""

# Create GDPR Paragraph Node
gdpr_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph {regulation_id: 'GDPR', id: row.id})
ON CREATE SET
    p.paragraphId = row.paragraphId,
    p.name = row.name,
    p.article_id = row.article_id,
    p.article_name = row.article_name,
    p.description = row.description;
"""

# 1. HAS_FRAMEWORK (Regulation → Framework)
gdpr_regulation_framework = """
MATCH (r:Regulation {regulation_id: 'GDPR'})
MATCH (f:Framework {regulation_id: 'GDPR'})
MERGE (r)-[:HAS_FRAMEWORK]->(f);
"""

# 2. HAS_CHAPTER (Framework → Chapter)
gdpr_has_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {regulation_id: 'GDPR', id: row.start_id})
MATCH (ch:Chapter {regulation_id: 'GDPR', id: row.end_id})
MERGE (f)-[:HAS_CHAPTER {order: toInteger(row.order)}]->(ch);
"""

# 3. CONTAINS_ARTICLE (Chapter → Article)
gdpr_contains_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ch:Chapter {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (ch)-[:CONTAINS_ARTICLE {order: toInteger(row.order)}]->(ar);
"""

# 4. CONTAINS_PARAGRAPH (Article → Paragraph)
gdpr_contains_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (p:Paragraph {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:CONTAINS_PARAGRAPH {order: toInteger(row.order)}]->(p);
"""

# 5. PROVIDES_CONTEXT_FOR (Recital → Article)
gdpr_provides_context_for = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ret:Recital {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (ret)-[:PROVIDES_CONTEXT_FOR {relevanceScore: toFloat(row.relevanceScore)}]->(ar);
"""

# 6. SPECIALIZES_PROVISIONS_OF (Framework → Article)
gdpr_specializes_provisions_of = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (f)-[:SPECIALIZES_PROVISIONS_OF {context: row.context}]->(ar);
"""

# 7. DEFINES_CONCEPT (Article → Concept)
gdpr_defines_concept = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:DEFINES_CONCEPT]->(co);
"""

# 8. IMPLEMENTS_PRINCIPLE (Article → Concept)
gdpr_implements_principle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:IMPLEMENTS_PRINCIPLE]->(co);
"""

# 9. ESTABLISHES_CRITERIA (Article → Concept)
gdpr_establishes_criteria = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:ESTABLISHES_CRITERIA]->(co);
"""

# 10. MANDATES_REQUIREMENT (Article → Concept)
gdpr_mandates_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:MANDATES_REQUIREMENT]->(co);
"""

# 11. DEFINES_RESPONSIBILITY (Article → Concept)
gdpr_defines_responsibility = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:DEFINES_RESPONSIBILITY]->(co);
"""

# 12. GOVERNS_PROCEDURE (Article → Concept)
gdpr_governs_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:GOVERNS_PROCEDURE]->(co);
"""

# 13. REQUIRES_ACTION (Article → Concept)
gdpr_requires_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:REQUIRES_ACTION {action: row.action}]->(co);
"""

# 14. AFFECTS_PROVISION (LegislativeAction → Article)
gdpr_affects_provision = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (l:LegislativeAction {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (l)-[:AFFECTS_PROVISION {changeType: row.changeType, description: row.description}]->(ar);
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
                                              "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/HAS_CHAPTER.csv"))
time.sleep(2)

client.query(gdpr_contains_article.replace('$file_path',
                                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_ARTICLE.csv"))
time.sleep(2)

client.query(gdpr_contains_paragraph.replace('$file_path',
                                                            "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/GDPR/CONTAINS_PARAGRAPH.csv"))
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

client.close()





