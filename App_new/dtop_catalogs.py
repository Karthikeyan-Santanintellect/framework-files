"""Loader — DTOP Catalogs.

Source folder : DTOP Catalogs/  (repo root, not under `New sources/`)
Source documents:
    DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/risk-catalog.json
    DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/control-catalog.json

Graph shape   : 7 node labels, 6 relationship types
Expected size : 2,893 nodes / 7,053 relationships

Hand-written, like `dtop_sources.py` and `enterprise_sources.py`, and merged
under its own anchor label `:DTOPCatalogNode`. That separation is deliberate:
`tools/repair_stranded_nodes.py` deletes any `:NewSourceNode` whose
`framework_id` is not one of the 64 `New sources/` folders, so reusing that
anchor here would put this graph one tool-run away from being silently deleted.
The anchor is also what makes the relationship MATCHes exact — the `rels_*.csv`
files record no endpoint labels.

Note the anchor is `:DTOPCatalogNode`, not `:DTOPNode`, and the root is
`:DTOPCatalogRoot`, not `:DTOPCatalog`. Both of those belong to `dtop_sources.py`
and must not be reused here.

The two source files share a taxonomy — all 11 `Domain` names and 32 of the 36
`FunctionalDomain` names are byte-identical in both — so they are loaded as one
catalogue with one set of domain nodes. Risks and controls therefore hang off
the same domain tree. Every node carries a `catalogs` property recording which
file(s) it came from: `risk`, `control`, or `risk;control`.

Labels are the source's own (`Domain`, `Control`, `Risk`, …), which collide by
design with the same-named labels in other frameworks; `framework_id` plus the
anchor label is what separates them, exactly as for every other loader here.
The one renamed label is `CSFFunction`, written `CSF Function` in the source —
the space would force backticks into every query, so the original spelling is
kept as the `source_label` property instead.

    python App_new/dtop_catalogs.py --dry-run   # validate, write nothing
    python App_new/dtop_catalogs.py             # load into Neo4j
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from new_sources_runtime import REPO_RAW_BASE, Loader, NodeStep, RelStep, run

FRAMEWORK_ID = 'DTOP_CATALOGS'
FOLDER = 'DTOP Catalogs'
ANCHOR = 'DTOPCatalogNode'

DOC_BASE = ('DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph'
            '/DtopCatalogs')
SOURCE_DOCUMENT = f'{DOC_BASE}/risk-catalog.json;{DOC_BASE}/control-catalog.json'

# --------------------------------------------------------------------------
# Catalogue root node. Labelled :DTOPCatalogRoot, matching the way the 64 use
# :NewSourceFramework rather than a bare :Framework label.
# --------------------------------------------------------------------------

constraint = """
CREATE CONSTRAINT dtop_catalog_node_key IF NOT EXISTS
FOR (n:DTOPCatalogNode) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;
"""

framework = """
MERGE (f:DTOPCatalogRoot {framework_id: 'DTOP_CATALOGS'})
SET f.name = 'DTOP Catalogs',
    f.folder = 'DTOP Catalogs',
    f.source_document = 'DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/risk-catalog.json;DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/control-catalog.json',
    f.description = 'DTOP risk and control catalogues over one shared domain taxonomy: 11 domains, 36 functional domains, 281 risks, 1,451 controls with their possible solutions, weightings and NIST CSF functions.',
    f.status = 'extracted';
"""

# Attach the catalogue to every node nothing else points at, so the whole thing
# can be traversed or deleted from one entry point. Here that is the 11 Domains.
roots = """
MATCH (f:DTOPCatalogRoot {framework_id: 'DTOP_CATALOGS'})
MATCH (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS'})
WHERE NOT (:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS'})-->(n)
MERGE (f)-[:HAS_ROOT]->(n);
"""

# --------------------------------------------------------------------------
# Nodes
# --------------------------------------------------------------------------

# nodes_Domain.csv  (11 rows, key domain_id)
# `type` is 'DTOM' on all 11; only the risk catalog states it, and the control
# catalog's identical Domain nodes inherit it through the merge.
node_domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.domain_id})
  SET
      n:Domain,
      n.domain_id = row.domain_id,
      n.name = row.name,
      n.type = row.type,
      n.functional_domain_count = toInteger(row.functional_domain_count),
      n.control_count = toInteger(row.control_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_FunctionalDomain.csv  (36 rows, key functionaldomain_id)
node_functionaldomain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.functionaldomain_id})
  SET
      n:FunctionalDomain,
      n.functionaldomain_id = row.functionaldomain_id,
      n.name = row.name,
      n.domain_count = toInteger(row.domain_count),
      n.risk_count = toInteger(row.risk_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Risk.csv  (281 rows, key risk_id)
# functional_domain and domain are the parent names, mirrored onto the node as
# well as modelled as edges, so the node stands alone without a traversal.
node_risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.risk_id})
  SET
      n:Risk,
      n.risk_id = row.risk_id,
      n.title = row.title,
      n.description = row.description,
      n.functional_domain = row.functional_domain,
      n.domain = row.domain,
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Control.csv  (1451 rows, key control_id)
# The key is the catalog's own control_id ('WEB-10'), which is unique across all
# 1,451 — no synthetic id is introduced. `description` is blank for 109 controls
# the catalog leaves undescribed; `weighting` and `csf_function` are blank for
# the 109 and 110 it leaves unweighted and unmapped.
node_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.control_id})
  SET
      n:Control,
      n.control_id = row.control_id,
      n.title = row.title,
      n.description = row.description,
      n.domain = row.domain,
      n.weighting = CASE row.weighting WHEN '' THEN null ELSE toInteger(row.weighting) END,
      n.csf_function = row.csf_function,
      n.solution_count = toInteger(row.solution_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Solution.csv  (1097 rows, key solution_id)
# One node per (size, description) pair. Solutions are shared: 1,097 nodes carry
# 2,598 HAS_POSSIBLE_SOLUTION edges.
node_solution = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.solution_id})
  SET
      n:Solution,
      n.solution_id = row.solution_id,
      n.size = row.size,
      n.description = row.description,
      n.control_count = toInteger(row.control_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Weighting.csv  (11 rows, key weighting_id)
node_weighting = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.weighting_id})
  SET
      n:Weighting,
      n.weighting_id = row.weighting_id,
      n.value = toInteger(row.value),
      n.control_count = toInteger(row.control_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_CSFFunction.csv  (6 rows, key csffunction_id)
# source_label records the catalog's own spelling, 'CSF Function'.
node_csffunction = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.csffunction_id})
  SET
      n:CSFFunction,
      n.csffunction_id = row.csffunction_id,
      n.name = row.name,
      n.source_label = row.source_label,
      n.control_count = toInteger(row.control_count),
      n.catalogs = row.catalogs,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
# Relationships
# --------------------------------------------------------------------------

# rels_HAS_FUNCTIONAL_DOMAIN.csv -> :HAS_FUNCTIONAL_DOMAIN  (40 rows)
# The union of both files: 31 pairs are stated in both, 8 only in the risk
# catalog, 1 only in the control catalog. `catalogs` on the edge says which.
rel_has_functional_domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_FUNCTIONAL_DOMAIN'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:HAS_FUNCTIONAL_DOMAIN]->(t)
  SET r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_RISK.csv -> :HAS_RISK  (281 rows)
rel_has_risk = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_RISK'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:HAS_RISK]->(t)
  SET r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_CONTROL.csv -> :HAS_CONTROL  (1451 rows)
# Controls attach to a Domain, not to a FunctionalDomain — that is how the
# control catalog states it, and it is why the functional domains carry risks
# but no controls.
rel_has_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_CONTROL'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:HAS_CONTROL]->(t)
  SET r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_POSSIBLE_SOLUTION.csv -> :HAS_POSSIBLE_SOLUTION  (2598 rows)
# `size` is kept on the edge so a control's solution for one organisation size
# can be selected without touching the Solution node.
rel_has_possible_solution = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_POSSIBLE_SOLUTION'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:HAS_POSSIBLE_SOLUTION]->(t)
  SET r.size = row.size,
      r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_WEIGHTING.csv -> :HAS_WEIGHTING  (1342 rows)
rel_has_weighting = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_WEIGHTING'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:HAS_WEIGHTING]->(t)
  SET r.value = toInteger(row.value),
      r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_MAPS_TO_FUNCTION.csv -> :MAPS_TO_FUNCTION  (1341 rows)
rel_maps_to_function = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'MAPS_TO_FUNCTION'
CALL (row) {
  MATCH (s:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.source_id})
  MATCH (t:DTOPCatalogNode {framework_id: 'DTOP_CATALOGS', node_id: row.target_id})
  MERGE (s)-[r:MAPS_TO_FUNCTION]->(t)
  SET r.function_name = row.function_name,
      r.catalogs = row.catalogs,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
LOADER = Loader(
    framework_id=FRAMEWORK_ID,
    name='DTOP Catalogs',
    folder=FOLDER,
    jurisdiction='n/a',
    source_document=SOURCE_DOCUMENT,
    constraint_cypher=constraint,
    framework_cypher=framework,
    root_cypher=roots,
    anchor=ANCHOR,
    base_url=REPO_RAW_BASE,
    node_steps=[
        NodeStep(label='Domain', csv_name='nodes_Domain.csv',
                 id_column='domain_id',
                 properties=['name', 'type', 'functional_domain_count',
                             'control_count', 'catalogs', 'source_document'],
                 rows=11, cypher=node_domain),
        NodeStep(label='FunctionalDomain',
                 csv_name='nodes_FunctionalDomain.csv',
                 id_column='functionaldomain_id',
                 properties=['name', 'domain_count', 'risk_count', 'catalogs',
                             'source_document'],
                 rows=36, cypher=node_functionaldomain),
        NodeStep(label='Risk', csv_name='nodes_Risk.csv',
                 id_column='risk_id',
                 properties=['title', 'description', 'functional_domain',
                             'domain', 'catalogs', 'source_document'],
                 rows=281, cypher=node_risk),
        NodeStep(label='Control', csv_name='nodes_Control.csv',
                 id_column='control_id',
                 properties=['title', 'description', 'domain', 'weighting',
                             'csf_function', 'solution_count', 'catalogs',
                             'source_document'],
                 rows=1451, cypher=node_control),
        NodeStep(label='Solution', csv_name='nodes_Solution.csv',
                 id_column='solution_id',
                 properties=['size', 'description', 'control_count',
                             'catalogs', 'source_document'],
                 rows=1097, cypher=node_solution),
        NodeStep(label='Weighting', csv_name='nodes_Weighting.csv',
                 id_column='weighting_id',
                 properties=['value', 'control_count', 'catalogs',
                             'source_document'],
                 rows=11, cypher=node_weighting),
        NodeStep(label='CSFFunction', csv_name='nodes_CSFFunction.csv',
                 id_column='csffunction_id',
                 properties=['name', 'source_label', 'control_count',
                             'catalogs', 'source_document'],
                 rows=6, cypher=node_csffunction),
    ],
    rel_steps=[
        RelStep(rel_type='HAS_FUNCTIONAL_DOMAIN',
                csv_name='rels_HAS_FUNCTIONAL_DOMAIN.csv',
                properties=['catalogs', 'source_document'],
                rows=40, cypher=rel_has_functional_domain),
        RelStep(rel_type='HAS_RISK', csv_name='rels_HAS_RISK.csv',
                properties=['catalogs', 'source_document'],
                rows=281, cypher=rel_has_risk),
        RelStep(rel_type='HAS_CONTROL', csv_name='rels_HAS_CONTROL.csv',
                properties=['catalogs', 'source_document'],
                rows=1451, cypher=rel_has_control),
        RelStep(rel_type='HAS_POSSIBLE_SOLUTION',
                csv_name='rels_HAS_POSSIBLE_SOLUTION.csv',
                properties=['size', 'catalogs', 'source_document'],
                rows=2598, cypher=rel_has_possible_solution),
        RelStep(rel_type='HAS_WEIGHTING', csv_name='rels_HAS_WEIGHTING.csv',
                properties=['value', 'catalogs', 'source_document'],
                rows=1342, cypher=rel_has_weighting),
        RelStep(rel_type='MAPS_TO_FUNCTION',
                csv_name='rels_MAPS_TO_FUNCTION.csv',
                properties=['function_name', 'catalogs', 'source_document'],
                rows=1341, cypher=rel_maps_to_function),
    ],
    expected_nodes_total=2893,
    expected_rels_total=7053,
)

if __name__ == "__main__":
    run(LOADER)
