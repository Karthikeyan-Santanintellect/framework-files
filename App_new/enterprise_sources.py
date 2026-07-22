"""Loader — Enterprise Sources.

Source folder : Enterprise Sources/  (repo root, not under `New sources/`)
Source document:
    DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json

Graph shape   : 3 node labels, 2 relationship types
Expected size : 172 nodes / 181 relationships

Hand-written, like `dtop_sources.py`, and merged under its own anchor label
`:EnterpriseNode`. That separation is deliberate:
`tools/repair_stranded_nodes.py` deletes any `:NewSourceNode` whose
`framework_id` is not one of the 64 `New sources/` folders, so reusing that
anchor would put this graph one tool-run away from being silently deleted.

It carries `framework_id`, which is what the graph explorer coalesces over, so
Enterprise Sources appears there alongside the other catalogues.

`ProfileType` is also a label in `DTOP Sources/`, and both use ids like
`pt_business`. The nodes stay distinct because every MERGE is keyed on
(framework_id, node_id) under a different anchor label.

    python App_new/enterprise_sources.py --dry-run   # validate, write nothing
    python App_new/enterprise_sources.py             # load into Neo4j
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from new_sources_runtime import REPO_RAW_BASE, Loader, NodeStep, RelStep, run

FRAMEWORK_ID = 'ENTERPRISE_SOURCES'
FOLDER = 'Enterprise Sources'
ANCHOR = 'EnterpriseNode'

# --------------------------------------------------------------------------
# Catalogue root node
# --------------------------------------------------------------------------

constraint = """
CREATE CONSTRAINT enterprise_node_key IF NOT EXISTS
FOR (n:EnterpriseNode) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;
"""

framework = """
MERGE (f:EnterpriseCatalog {framework_id: 'ENTERPRISE_SOURCES'})
SET f.name = 'Enterprise Sources',
    f.folder = 'Enterprise Sources',
    f.source_document = 'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json',
    f.description = 'Enterprise source catalogue: 114 external sources with reputation scores, profile types and the web resources they point at.',
    f.status = 'extracted';
"""

roots = """
MATCH (f:EnterpriseCatalog {framework_id: 'ENTERPRISE_SOURCES'})
MATCH (n:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES'})
WHERE NOT (:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES'})-->(n)
MERGE (f)-[:HAS_ROOT]->(n);
"""

# --------------------------------------------------------------------------
# Nodes
# --------------------------------------------------------------------------

# nodes_EnterpriseSource.csv  (114 rows, key enterprisesource_id)
# name_is_duplicated flags the one SourceName that appears twice with
# different content; source_name is therefore NOT a unique key.
node_enterprisesource = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.enterprisesource_id})
  SET
      n:EnterpriseSource,
      n.enterprisesource_id = row.enterprisesource_id,
      n.source_name = row.source_name,
      n.url = row.url,
      n.description = row.description,
      n.reputation_score = toInteger(row.reputation_score),
      n.profile_type = row.profile_type,
      n.name_is_duplicated = toBoolean(row.name_is_duplicated),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_WebResource.csv  (55 rows, key webresource_id)
node_webresource = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.webresource_id})
  SET
      n:WebResource,
      n.webresource_id = row.webresource_id,
      n.url = row.url,
      n.referenced_by_count = toInteger(row.referenced_by_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_ProfileType.csv  (3 rows, key profiletype_id)
node_profiletype = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.profiletype_id})
  SET
      n:ProfileType,
      n.profiletype_id = row.profiletype_id,
      n.name = row.name,
      n.enterprisesource_count = toInteger(row.enterprisesource_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
# Relationships
# --------------------------------------------------------------------------

# rels_HAS_PROFILE_TYPE.csv -> :HAS_PROFILE_TYPE  (114 rows)
rel_has_profile_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_PROFILE_TYPE'
CALL (row) {
  MATCH (s:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.source_id})
  MATCH (t:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.target_id})
  MERGE (s)-[r:HAS_PROFILE_TYPE]->(t)
  SET r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_AVAILABLE_AT.csv -> :AVAILABLE_AT  (67 rows)
# Only the 67 entries with a URL. shared_with_others marks the ones whose
# page is catalogued under more than one name.
rel_available_at = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'AVAILABLE_AT'
CALL (row) {
  MATCH (s:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.source_id})
  MATCH (t:EnterpriseNode {framework_id: 'ENTERPRISE_SOURCES', node_id: row.target_id})
  MERGE (s)-[r:AVAILABLE_AT]->(t)
  SET r.url = row.url,
      r.shared_with_others = toBoolean(row.shared_with_others),
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
LOADER = Loader(
    framework_id=FRAMEWORK_ID,
    name='Enterprise Sources',
    folder=FOLDER,
    jurisdiction='n/a',
    source_document=(
        'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json'),
    constraint_cypher=constraint,
    framework_cypher=framework,
    root_cypher=roots,
    anchor=ANCHOR,
    base_url=REPO_RAW_BASE,
    node_steps=[
        NodeStep(label='EnterpriseSource', csv_name='nodes_EnterpriseSource.csv',
                 id_column='enterprisesource_id',
                 properties=['source_name', 'url', 'description',
                             'reputation_score', 'profile_type',
                             'name_is_duplicated', 'source_document'],
                 rows=114, cypher=node_enterprisesource),
        NodeStep(label='WebResource', csv_name='nodes_WebResource.csv',
                 id_column='webresource_id',
                 properties=['url', 'referenced_by_count', 'source_document'],
                 rows=55, cypher=node_webresource),
        NodeStep(label='ProfileType', csv_name='nodes_ProfileType.csv',
                 id_column='profiletype_id',
                 properties=['name', 'enterprisesource_count', 'source_document'],
                 rows=3, cypher=node_profiletype),
    ],
    rel_steps=[
        RelStep(rel_type='HAS_PROFILE_TYPE', csv_name='rels_HAS_PROFILE_TYPE.csv',
                properties=['source_document'],
                rows=114, cypher=rel_has_profile_type),
        RelStep(rel_type='AVAILABLE_AT', csv_name='rels_AVAILABLE_AT.csv',
                properties=['url', 'shared_with_others', 'source_document'],
                rows=67, cypher=rel_available_at),
    ],
)

if __name__ == "__main__":
    run(LOADER)
