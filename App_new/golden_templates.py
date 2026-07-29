"""Loader — GOLDEN TEMPLATES.

Source folder : GOLDEN TEMPLATES/  (repo root, not under `New sources/`)
Source document:
    DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/templateSources.json

Graph shape   : 6 node labels, 4 relationship types
Expected size : 554 nodes / 1,075 relationships

Hand-written, like `dtop_sources.py`, `dtop_catalogs.py` and
`enterprise_sources.py`, and merged under its own anchor label
`:GoldenTemplateNode`. That separation is deliberate:
`tools/repair_stranded_nodes.py` deletes any `:NewSourceNode` whose
`framework_id` is not one of the 64 `New sources/` folders, so reusing that
anchor here would put this graph one tool-run away from being silently deleted.
The anchor is also what makes the relationship MATCHes exact — the `rels_*.csv`
files record no endpoint labels.

The catalogue is the 31 DTOM golden policy templates and the 982 sources they
cite. Citations are parsed: 485 `Source` nodes keyed on (title, URL), and 18
`InternalDocument` nodes for the entries with no URL. The accessed date lives on
the `CITES` edge rather than the node, because five sources were accessed on two
different dates by different templates.

One `InternalDocument` is the literal string `</div>`, an HTML fragment that is
plainly a scraping artifact. It is loaded rather than dropped, flagged
`is_malformed = true`, so the JSON's own `SourceCount` still reconciles against
the edge count. Filter it out with `WHERE NOT n.is_malformed`.

`possibly_maps_to` on `DomainCode` names a DTOP Catalogs domain the code may
refer to. It is a property only — deliberately NOT a relationship, so this
catalogue stays disconnected from every other one, as they all are. See the
folder README.

    python App_new/golden_templates.py --dry-run   # validate, write nothing
    python App_new/golden_templates.py             # load into Neo4j
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from new_sources_runtime import REPO_RAW_BASE, Loader, NodeStep, RelStep, run

FRAMEWORK_ID = 'GOLDEN_TEMPLATES'
FOLDER = 'GOLDEN TEMPLATES'
ANCHOR = 'GoldenTemplateNode'

SOURCE_DOCUMENT = (
    'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/templateSources.json')

# --------------------------------------------------------------------------
# Catalogue root node. Labelled :GoldenTemplateCatalog, matching the way the 64
# use :NewSourceFramework rather than a bare :Framework label.
# --------------------------------------------------------------------------

constraint = """
CREATE CONSTRAINT golden_template_node_key IF NOT EXISTS
FOR (n:GoldenTemplateNode) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;
"""

framework = """
MERGE (f:GoldenTemplateCatalog {framework_id: 'GOLDEN_TEMPLATES'})
SET f.name = 'Golden Templates',
    f.folder = 'GOLDEN TEMPLATES',
    f.source_document = 'DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/templateSources.json',
    f.description = 'DTOM golden policy-template catalogue: 31 templates across 4 levels, 10 domain codes and 6 artifact types, and the 982 sources they cite.',
    f.status = 'extracted';
"""

# Attach the catalogue to every node nothing else points at, so the whole thing
# can be traversed or deleted from one entry point. Here that is the 31
# Templates — every other node is the target of a CITES or taxonomy edge.
roots = """
MATCH (f:GoldenTemplateCatalog {framework_id: 'GOLDEN_TEMPLATES'})
MATCH (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES'})
WHERE NOT (:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES'})-->(n)
MERGE (f)-[:HAS_ROOT]->(n);
"""

# --------------------------------------------------------------------------
# Nodes
# --------------------------------------------------------------------------

# nodes_Template.csv  (31 rows, key template_id)
# level, domain_code and artifact_type are mirrored onto the node as well as
# modelled as edges, so the node stands alone without a traversal.
# template_path is stored verbatim: nine templates sit in a DTOM-L2A-ENT-DTOM
# directory that does not match their own id prefix, so it cannot be derived.
node_template = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.template_id})
  SET
      n:Template,
      n.template_id = row.template_id,
      n.name = row.name,
      n.level = row.level,
      n.domain_code = row.domain_code,
      n.artifact_type = row.artifact_type,
      n.sequence = toInteger(row.sequence),
      n.template_path = row.template_path,
      n.stated_source_count = toInteger(row.stated_source_count),
      n.cited_source_count = toInteger(row.cited_source_count),
      n.cited_internal_document_count = toInteger(row.cited_internal_document_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Source.csv  (485 rows, key source_id)
# first_accessed / last_accessed are ISO dates held as strings, so they sort
# lexically. They differ only for the five sources two templates accessed on
# different days. `verbatim` is the citation string exactly as the JSON writes
# it, including the accessed date baked into the text.
node_source = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.source_id})
  SET
      n:Source,
      n.source_id = row.source_id,
      n.title = row.title,
      n.url = row.url,
      n.host = row.host,
      n.verbatim = row.verbatim,
      n.template_count = toInteger(row.template_count),
      n.first_accessed = row.first_accessed,
      n.last_accessed = row.last_accessed,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_InternalDocument.csv  (18 rows, key internaldocument_id)
# Seventeen DTOM .docx files plus the one malformed entry.
node_internaldocument = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.internaldocument_id})
  SET
      n:InternalDocument,
      n.internaldocument_id = row.internaldocument_id,
      n.text = row.text,
      n.is_malformed = toBoolean(row.is_malformed),
      n.note = row.note,
      n.template_count = toInteger(row.template_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_Level.csv  (4 rows, key level_id)
# No expanded name is invented for the code — the JSON never states one.
node_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.level_id})
  SET
      n:Level,
      n.level_id = row.level_id,
      n.code = row.code,
      n.template_count = toInteger(row.template_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_DomainCode.csv  (10 rows, key domaincode_id)
# possibly_maps_to is a hint for a human, recorded as a property only. It is
# deliberately NOT turned into a relationship — see the folder README.
node_domaincode = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.domaincode_id})
  SET
      n:DomainCode,
      n.domaincode_id = row.domaincode_id,
      n.code = row.code,
      n.template_count = toInteger(row.template_count),
      n.possibly_maps_to = row.possibly_maps_to,
      n.possibly_maps_to_basis = row.possibly_maps_to_basis,
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# nodes_ArtifactType.csv  (6 rows, key artifacttype_id)
node_artifacttype = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
CALL (row) {
  MERGE (n:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.artifacttype_id})
  SET
      n:ArtifactType,
      n.artifacttype_id = row.artifacttype_id,
      n.code = row.code,
      n.template_count = toInteger(row.template_count),
      n.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
# Relationships
# --------------------------------------------------------------------------

# rels_CITES.csv -> :CITES  (982 rows)
# ordinal and stated_source_text are kept on the edge so the JSON's Sources
# arrays can be rebuilt verbatim from the graph. target_kind separates the two
# kinds of target without a join. accessed_date is blank for InternalDocument
# targets, which carry no date.
rel_cites = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'CITES'
CALL (row) {
  MATCH (s:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.source_id})
  MATCH (t:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.target_id})
  MERGE (s)-[r:CITES]->(t)
  SET r.ordinal = toInteger(row.ordinal),
      r.target_kind = row.target_kind,
      r.accessed_date = row.accessed_date,
      r.accessed_date_stated = row.accessed_date_stated,
      r.stated_source_text = row.stated_source_text,
      r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_LEVEL.csv -> :HAS_LEVEL  (31 rows)
rel_has_level = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_LEVEL'
CALL (row) {
  MATCH (s:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.source_id})
  MATCH (t:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.target_id})
  MERGE (s)-[r:HAS_LEVEL]->(t)
  SET r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_IN_DOMAIN.csv -> :IN_DOMAIN  (31 rows)
rel_in_domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'IN_DOMAIN'
CALL (row) {
  MATCH (s:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.source_id})
  MATCH (t:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.target_id})
  MERGE (s)-[r:IN_DOMAIN]->(t)
  SET r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# rels_HAS_ARTIFACT_TYPE.csv -> :HAS_ARTIFACT_TYPE  (31 rows)
rel_has_artifact_type = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.rel_type = 'HAS_ARTIFACT_TYPE'
CALL (row) {
  MATCH (s:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.source_id})
  MATCH (t:GoldenTemplateNode {framework_id: 'GOLDEN_TEMPLATES', node_id: row.target_id})
  MERGE (s)-[r:HAS_ARTIFACT_TYPE]->(t)
  SET r.source_document = row.source_document
} IN TRANSACTIONS OF 500 ROWS;
"""

# --------------------------------------------------------------------------
LOADER = Loader(
    framework_id=FRAMEWORK_ID,
    name='Golden Templates',
    folder=FOLDER,
    jurisdiction='n/a',
    source_document=SOURCE_DOCUMENT,
    constraint_cypher=constraint,
    framework_cypher=framework,
    root_cypher=roots,
    anchor=ANCHOR,
    base_url=REPO_RAW_BASE,
    node_steps=[
        NodeStep(label='Template', csv_name='nodes_Template.csv',
                 id_column='template_id',
                 properties=['name', 'level', 'domain_code', 'artifact_type',
                             'sequence', 'template_path', 'stated_source_count',
                             'cited_source_count',
                             'cited_internal_document_count',
                             'source_document'],
                 rows=31, cypher=node_template),
        NodeStep(label='Source', csv_name='nodes_Source.csv',
                 id_column='source_id',
                 properties=['title', 'url', 'host', 'verbatim',
                             'template_count', 'first_accessed',
                             'last_accessed', 'source_document'],
                 rows=485, cypher=node_source),
        NodeStep(label='InternalDocument',
                 csv_name='nodes_InternalDocument.csv',
                 id_column='internaldocument_id',
                 properties=['text', 'is_malformed', 'note', 'template_count',
                             'source_document'],
                 rows=18, cypher=node_internaldocument),
        NodeStep(label='Level', csv_name='nodes_Level.csv',
                 id_column='level_id',
                 properties=['code', 'template_count', 'source_document'],
                 rows=4, cypher=node_level),
        NodeStep(label='DomainCode', csv_name='nodes_DomainCode.csv',
                 id_column='domaincode_id',
                 properties=['code', 'template_count', 'possibly_maps_to',
                             'possibly_maps_to_basis', 'source_document'],
                 rows=10, cypher=node_domaincode),
        NodeStep(label='ArtifactType', csv_name='nodes_ArtifactType.csv',
                 id_column='artifacttype_id',
                 properties=['code', 'template_count', 'source_document'],
                 rows=6, cypher=node_artifacttype),
    ],
    rel_steps=[
        RelStep(rel_type='CITES', csv_name='rels_CITES.csv',
                properties=['target_kind', 'ordinal', 'accessed_date',
                            'accessed_date_stated', 'stated_source_text',
                            'source_document'],
                rows=982, cypher=rel_cites),
        RelStep(rel_type='HAS_LEVEL', csv_name='rels_HAS_LEVEL.csv',
                properties=['source_document'],
                rows=31, cypher=rel_has_level),
        RelStep(rel_type='IN_DOMAIN', csv_name='rels_IN_DOMAIN.csv',
                properties=['source_document'],
                rows=31, cypher=rel_in_domain),
        RelStep(rel_type='HAS_ARTIFACT_TYPE',
                csv_name='rels_HAS_ARTIFACT_TYPE.csv',
                properties=['source_document'],
                rows=31, cypher=rel_has_artifact_type),
    ],
    expected_nodes_total=554,
    expected_rels_total=1075,
)

if __name__ == "__main__":
    run(LOADER)
