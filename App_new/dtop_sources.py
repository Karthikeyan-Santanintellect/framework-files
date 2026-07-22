"""Loader — DTOP Sources.

Source folder : DTOP Sources/  (repo root, not under `New sources/`)
Source document:
    DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/dtopSources.json

Graph shape   : 3 node labels, 2 relationship types
Expected size : 20 nodes / 27 relationships

Unlike the 64 `New sources/` loaders this one is hand-written, and it merges
under its own anchor label `:DTOPNode` rather than `:NewSourceNode`. That
separation is deliberate: `tools/repair_stranded_nodes.py` deletes any
`:NewSourceNode` whose `framework_id` is not one of the 64 `New sources/`
folders, so reusing that anchor here would put this graph one tool-run away
from being silently deleted.

It does carry `framework_id`, which is what the graph explorer coalesces over,
so DTOP Sources appears there alongside the compliance frameworks.

    python App_new/dtop_sources.py --dry-run   # validate, write nothing
    python App_new/dtop_sources.py             # load into Neo4j
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from new_sources_runtime import REPO_RAW_BASE, Loader, NodeStep, RelStep, run

FRAMEWORK_ID = 'DTOP_SOURCES'
FOLDER = 'DTOP Sources'
ANCHOR = 'DTOPNode'

# --------------------------------------------------------------------------
# Catalogue root node. Labelled :DTOPCatalog, matching the way the 64 use
# :NewSourceFramework rather than a bare :Framework label.
# --------------------------------------------------------------------------

constraint = """
CREATE CONSTRAINT dtop_node_key IF NOT EXISTS
FOR (n:DTOPNode) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;
"""

framework = """
MERGE (f:DTOPCatalog {framework_id: 'DTOP_SOURCES'})
SET f.name = 'DTOP Sources',
    f.folder = 'DTOP Sources',
    f.source_document = 'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/dtopSources.json',
    f.description = 'DTO source catalogue: the seven generated artefacts, what each is derived from, and their profile types.',
    f.status = 'extracted';
"""

# Attach the catalogue to every node nothing else points at, so the whole
# thing can be traversed or deleted from one entry point.
roots = """
MATCH (f:DTOPCatalog {framework_id: 'DTOP_SOURCES'})
MATCH (n:DTOPNode {framework_id: 'DTOP_SOURCES'})
WHERE NOT (:DTOPNode {framework_id: 'DTOP_SOURCES'})-->(n)
MERGE (f)-[:HAS_ROOT]->(n);
"""

# --------------------------------------------------------------------------
# Nodes
# --------------------------------------------------------------------------

# nodes_DTOSource.csv  (7 rows, key dtosource_id)
node_dtosource = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.dtosource_id})
  SET
      n:DTOSource,
      n.dtosource_id = row.dtosource_id,
      n.source_name = row.source_name,
      n.url = row.url,
      n.description = row.description,
      n.reputation_score = toInteger(row.reputation_score),
      n.profile_type = row.profile_type,
      n.stated_source_count = toInteger(row.stated_source_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_InputSource.csv  (11 rows, key inputsource_id)
# possibly_same_as is a hint for a human, recorded as a property only. It is
# deliberately NOT turned into a relationship — see the folder README.
node_inputsource = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.inputsource_id})
  SET
      n:InputSource,
      n.inputsource_id = row.inputsource_id,
      n.name = row.name,
      n.referenced_by_count = toInteger(row.referenced_by_count),
      n.possibly_same_as = row.possibly_same_as,
      n.possibly_same_as_basis = row.possibly_same_as_basis,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_ProfileType.csv  (2 rows, key profiletype_id)
node_profiletype = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.profiletype_id})
  SET
      n:ProfileType,
      n.profiletype_id = row.profiletype_id,
      n.name = row.name,
      n.dtosource_count = toInteger(row.dtosource_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
# Relationships
# --------------------------------------------------------------------------

# rels_DERIVED_FROM.csv -> :DERIVED_FROM  (20 rows)
# ordinal and stated_source_name are kept on the edge so the JSON's Sources
# arrays can be rebuilt verbatim from the graph.
rel_derived_from = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'DERIVED_FROM'
CALL (row) {
  MATCH (s:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.source_id})
  MATCH (t:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.target_id})
  MERGE (s)-[r:DERIVED_FROM]->(t)
  SET r.target_kind = row.target_kind,
      r.ordinal = toInteger(row.ordinal),
      r.stated_source_name = row.stated_source_name,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_PROFILE_TYPE.csv -> :HAS_PROFILE_TYPE  (7 rows)
rel_has_profile_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_PROFILE_TYPE'
CALL (row) {
  MATCH (s:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.source_id})
  MATCH (t:DTOPNode {framework_id: 'DTOP_SOURCES', node_id: row.target_id})
  MERGE (s)-[r:HAS_PROFILE_TYPE]->(t)
  SET r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
LOADER = Loader(
    framework_id=FRAMEWORK_ID,
    name='DTOP Sources',
    folder=FOLDER,
    jurisdiction='n/a',
    source_document=(
        'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/dtopSources.json'),
    constraint_cypher=constraint,
    framework_cypher=framework,
    root_cypher=roots,
    anchor=ANCHOR,
    base_url=REPO_RAW_BASE,
    node_steps=[
        NodeStep(label='DTOSource', csv_name='nodes_DTOSource.csv',
                 id_column='dtosource_id',
                 properties=['source_name', 'url', 'description',
                             'reputation_score', 'profile_type',
                             'stated_source_count', 'source_document'],
                 rows=7, cypher=node_dtosource),
        NodeStep(label='InputSource', csv_name='nodes_InputSource.csv',
                 id_column='inputsource_id',
                 properties=['name', 'referenced_by_count', 'possibly_same_as',
                             'possibly_same_as_basis', 'source_document'],
                 rows=11, cypher=node_inputsource),
        NodeStep(label='ProfileType', csv_name='nodes_ProfileType.csv',
                 id_column='profiletype_id',
                 properties=['name', 'dtosource_count', 'source_document'],
                 rows=2, cypher=node_profiletype),
    ],
    rel_steps=[
        RelStep(rel_type='DERIVED_FROM', csv_name='rels_DERIVED_FROM.csv',
                properties=['target_kind', 'ordinal', 'stated_source_name',
                            'source_document'],
                rows=20, cypher=rel_derived_from),
        RelStep(rel_type='HAS_PROFILE_TYPE', csv_name='rels_HAS_PROFILE_TYPE.csv',
                properties=['source_document'],
                rows=7, cypher=rel_has_profile_type),
    ],
)

if __name__ == "__main__":
    run(LOADER)
