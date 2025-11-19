#Create GDPR regulations Node
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
#Create GDPR framework Node
gdpr_framework = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (f:Framework {regulation_id: 'GDPR',framework_id : row.id})
ON CREATE SET
    r.framework_name = row.name,
    r.version = row.version,
    r.effective_date = date(row.effective_date),
    r.jurisdiction = row.jurisdiction,
    r.description = row.description;
"""
#Create GDPR reticle 
gdpr_reticle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ret:Reticle{regulation_id: 'GDPR',reticle_id : row.id})
ON CREATE SET
    ret.number : toInteger(row.reticleNumber),
    ret.name : row.name,
    ret.description : row.description;
"""

#Create GDPR chapter
gdpr_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ch:Chapter{regulation_id: 'GDPR',chapter_id : row.id})
ON CREATE SET
    ch.number : toInteger(row.chapter_num),
    ch.name : row.name,
    ch.description : row.description;
"""

#Create GDPR article
gdpr_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (ar:Article{regulation_id: 'GDPR',article_id : row.id})
ON CREATE SET
    ar.id = row.article_id,
    ar.name = row.name,
    ar.chapter_id = row.chapter_id,
    ar.chapter_name = row.chapter_name,
    ar.description = row.description;
"""

#Create GDPR concept
gdpr_concept = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (co:Concept{regulation_id: 'GDPR',concept_id : row.id})
ON CREATE SET
    co.name : row.name,
    co.category : row.category,
    co.description : row.description;
"""
#Create GDPR Legislative action
gdpr_legislative_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (l:Legislative_action{regulation_id: 'GDPR', legislative_action_id : row.id})
ON CREATE SET
    l.name : row.name,
    l.date : date(row.proposal_date),
    l.status : row.status,
    l.description : row.description;
"""

#Create GDPR Paragraph 
gdpr_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (p:Paragraph{regulation_id: 'GDPR', paragraph_id : row.id})
ON CREATE SET
    paragraph_id : row.paragraph_id,
    name : row.name,
    article_id : row.article_id,
    article_name : row.article_name,
    description : row.description;
"""
#Create REGULATION_HAS_FRAMEWORK
gdpr_regulation_framework = """
MATCH (r:Regulation {regulation_id: 'GDPR'})
MATCH (f:Framework {regulation_id: 'GDPR''})
MERGE (r)-[:HAS_FRAMEWORK]->(f);
"""


#Create HAS_CHAPTER relationship
gdpr_has_chapter = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {regulation_id: 'GDPR', id: row.start_id})
MATCH (ch:Chapter {regulation_id: 'GDPR', id: row.end_id})
MERGE (f)-[:HAS_CHAPTER {order: toInteger(row.order)}]->(ch);
"""

#Create CONTAINS_ARTICLE relationship
gdpr_contains_article = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ch:Chapter {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (ch)-[:CONTAINS_ARTICLE {order: toInteger(row.order)}]->(ar);
"""

#Create CONTAINS_PARAGRAPH relationship
gdpr_contains_paragraph = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (p:Paragraph {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:CONTAINS_PARAGRAPH {order: toInteger(row.order)}]->(p);
"""
#Create REFERENCES relationship
gdpr_references = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (p:Paragraph {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (p)-[:REFERENCES {
    referenceType: row.referenceType,
    sourceTextSnippet: row.sourceTextSnippet
}]->(ar);
"""
#Create PROVIDES_CONTEXT_FOR relationships
gdpr_provides_context_for = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ret:Recital {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (ret)-[:PROVIDES_CONTEXT_FOR {
    relevanceScore: toFloat(row.relevanceScore)
}]->(ar);
"""

#Create SPECIALIZES_PROVISONS_OF relations
gdpr_specializes_provisions_of = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (f:Framework {id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (f)-[:SPECIALIZES_PROVISIONS_OF {
    context: row.context
}]->(ar);
"""

#Create DEFINES_CONCEPT relations
gdpr_defines_concept = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:DEFINES_CONCEPT]->(co);
"""
#Create IMPLEMENTS_PRINCIPLE relation
gdpr_implements_principle = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:IMPLEMENTS_PRINCIPLE]->(co);
"""
#Create ESTABLISHES_CRITERIA relation
gdpr_establishes_criteria = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:ESTABLISHES_CRITERIA]->(co);
"""
#Create MANDATES_REQUIREMENTS relation
gdpr_mandates_requirement = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:MANDATES_REQUIREMENT]->(co);
"""
#Create DEFINES_RESPONSIBILITY relation
gdpr_defines_responsibility = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:DEFINES_RESPONSIBILITY]->(co);
"""

#Create GOVERNS_PROCEDURE
gdpr_governs_procedure = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:GOVERNS_PROCEDURE]->(co);
"""
#Create REQUIRE_ACTION relation
gdpr_requires_action = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (ar:Article {regulation_id: 'GDPR', id: row.start_id})
MATCH (co:Concept {regulation_id: 'GDPR', id: row.end_id})
MERGE (ar)-[:REQUIRES_ACTION {
    action: row.action
}]->(co);
"""

#Create AFFECTS_PROVISON relation
gdpr_affects_provision = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (l:LegislativeAction {regulation_id: 'GDPR', id: row.start_id})
MATCH (ar:Article {regulation_id: 'GDPR', id: row.end_id})
MERGE (l)-[:AFFECTS_PROVISION {
    changeType: row.changeType,
    description: row.description
}]->(ar);
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
                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Category.csv"))
time.sleep(2)

client.query(gdpr_reticle.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Control.csv"))
time.sleep(2)


client.query(gdpr_chapter.replace('$file_path',
                                               "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlObjective.csv"))
time.sleep(2)

client.query(gdpr_article.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Control.csv"))
time.sleep(2)

client.query(gdpr_concept.replace('$file_path',
                                     "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_Control.csv"))
time.sleep(2)

client.query(gdpr_legislative_action.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlSpecification.csv"))
time.sleep(2)

client.query(gdpr_paragraph.replace('$file_path',
                                                   "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HITRUST_ControlSpecification.csv"))
time.sleep(2)


client.query(gdpr_regulation_frameworkl)
time.sleep(2)

client.query(gdpr_has_chapter.replace('$file_path',
                                              "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_CONTROL.csv"))
time.sleep(2)

client.query(gdpr_contains_article.replace('$file_path',
                                                      "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_OBJECTIVE.csv"))
time.sleep(2)

client.query(gdpr_contains_paragraph.replace('$file_path',
                                                            "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/HAS_SPECIFICATION.csv"))
time.sleep(2)

client.query(gdpr_references.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_provides_context_for.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_specializes_provisions_of.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_defines_concept.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_implements_principle.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_establishes_criteria.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_mandates_requirement.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_defines_responsibility.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_governs_procedure.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_requires_action.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)

client.query(gdpr_affects_provision.replace('$file_path',
                                                    "https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HITRUST/MAPS_TO.csv"))
time.sleep(2)





logger.info("Graph structure loaded successfully.")

client.close()





