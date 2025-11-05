# UPDATED: Using MERGE to prevent errors on re-runs.
framework = """
MERGE (f:Framework {framework_id: 'HIPAA'})
ON CREATE SET
    f.name = 'Health Insurance Portability and Accountability Act',
    f.version = '2022',
    f.publication_date = date('2025-01-05'),
    f.status = 'Active',
    f.description = '';
"""

hipaa_standards = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (s:Standard {standard_id: row.id, framework_id: 'HIPAA'})
ON CREATE SET
    s.title = row.title,
    s.safeguard_type = row.safeguard_type,
    s.type = row.standard_type,
    s.text = row.text,
    s.req_type = row.req_type,
    s.section = row.section,
    s.source_doc = row.source_doc,
    s.source_section = row.source_section;
"""

mappings = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (m:Mapping {mapping_id: row.hipaa_id + '_TO_' + row.csf_subcategory_id, framework_id: "HIPAA"})
ON CREATE SET
    m.type = row.mapping_type,
    m.confidence = row.confidence,
    m.rationale = row.rationale,
    m.source_doc = row.source_doc,
    m.source_section = row.source_section;
"""

framework_hipaa_standards_rel = """
MATCH (f:Framework {framework_id: 'HIPAA'})
MATCH (c:Standard {framework_id: 'HIPAA'})
MERGE (f)-[:CONTAINS]->(c);
"""

# UPDATED: Scoped MATCH to framework_id for precision.
hipaa_parent_child_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.parent_id IS NOT NULL AND row.parent_id <> ''
MATCH (child:Standard {standard_id: row.id, framework_id: 'HIPAA'})
MATCH (parent:Standard {standard_id: row.parent_id, framework_id: 'HIPAA'})
MERGE (parent)-[:HAS_SPEC]->(child);
"""

hippa_subcategory_mapping_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MATCH (s:Standard {framework_id: "HIPAA", standard_id: row.hipaa_id})
MATCH (m:Mapping {mapping_id: row.hipaa_id + '_TO_' + row.csf_subcategory_id, framework_id: "HIPAA"})
MATCH (sc:Subcategory {subcategory_id: row.csf_subcategory_id, framework_id: "NIST_CSF_2.0"})
MERGE (s)-[:MAPS_TO {mapping_type: row.mapping_type, confidence: row.confidence}]->(m)-[:TARGET]->(sc);
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

client.query(framework)
time.sleep(2)

client.query(hipaa_standards.replace('$file_path',
                                     'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_standards.csv'))
time.sleep(2)

client.query(mappings.replace('$file_path',
                              'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_csf_mappings.csv'))
time.sleep(2)

client.query(framework_hipaa_standards_rel)
time.sleep(2)

client.query(hipaa_parent_child_rel.replace('$file_path',
                                            'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_standards.csv'))
time.sleep(2)

client.query(hippa_subcategory_mapping_rel.replace('$file_path',
                                                   'https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/HIPAA/hipaa_csf_mappings.csv'))
time.sleep(2)

logger.info("Graph structure loaded successfully.")

client.close()
