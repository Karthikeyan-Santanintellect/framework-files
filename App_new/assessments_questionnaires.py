"""Loader — Assessments and Questionnaires.

Source folder : Assessments and Questionnaires/  (repo root, not `New sources/`)
Source        : the three DTOP-OLD assessment banks — see the folder README.

Graph shape   : 13 node labels, 16 relationship types
Expected size : 1,841 nodes / 8,484 relationships

Hand-written, like `dtop_sources.py` and `enterprise_sources.py`, and merged
under its own anchor label `:AssessmentNode` with an `:AssessmentCatalog` root.
That separation is deliberate: `tools/repair_stranded_nodes.py` deletes any
`:NewSourceNode` whose framework_id is not one of the 64 `New sources/`
folders, so reusing that anchor would put this graph one tool-run away from
being deleted.

It carries `framework_id`, which is what the graph explorer coalesces over, so
Assessments and Questionnaires appears there alongside the other catalogues.

The 29 node/relationship statements are built from compact specs below rather
than spelled out one by one, so a column can only be loaded one way. Integer
and boolean columns are cast; everything else loads as a string.

    python App_new/assessments_questionnaires.py --dry-run   # validate only
    python App_new/assessments_questionnaires.py             # load into Neo4j
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from new_sources_runtime import REPO_RAW_BASE, Loader, NodeStep, RelStep, run

FID = 'ASSESSMENTS_QUESTIONNAIRES'
FOLDER = 'Assessments and Questionnaires'
ANCHOR = 'AssessmentNode'

INT_COLS = {"item_count", "vulnerability_count", "ordinal", "option_count",
            "statement_count", "question_count", "threat_count"}
BOOL_COLS = {"in_md", "in_csv"}


def _val(col: str) -> str:
    if col in INT_COLS:
        return f"toInteger(row.{col})"
    if col in BOOL_COLS:
        return f"toBoolean(row.{col})"
    return f"row.{col}"


def node_cypher(label: str, id_col: str, props: list[str]) -> str:
    sets = [f"      n:{label}", f"      n.{id_col} = row.{id_col}"]
    sets += [f"      n.{c} = {_val(c)}" for c in props]
    body = ",\n".join(sets)
    return (
        f"LOAD CSV WITH HEADERS FROM '$file_path' AS row\n"
        f"CALL (row) {{\n"
        f"  MERGE (n:{ANCHOR} {{framework_id: '{FID}', node_id: row.{id_col}}})\n"
        f"  SET\n{body}\n"
        f"}} IN TRANSACTIONS OF 500 ROWS;\n"
    )


def rel_cypher(rtype: str, extra: list[str]) -> str:
    sets = ""
    props = [c for c in extra if c != "rel_type"]
    if props:
        sets = "\n  SET " + ",\n      ".join(f"r.{c} = {_val(c)}" for c in props)
    return (
        f"LOAD CSV WITH HEADERS FROM '$file_path' AS row\n"
        f"CALL (row) {{\n"
        f"  MATCH (s:{ANCHOR} {{framework_id: '{FID}', node_id: row.source_id}})\n"
        f"  MATCH (t:{ANCHOR} {{framework_id: '{FID}', node_id: row.target_id}})\n"
        f"  MERGE (s)-[r:{rtype}]->(t){sets}\n"
        f"}} IN TRANSACTIONS OF 500 ROWS;\n"
    )


# (label, csv, id_col, [props], rows) ---------------------------------------
NODES = [
    ("Assessment", "nodes_Assessment.csv", "assessment_id",
     ["name", "framework", "kind", "item_count", "vulnerability_count", "ui",
      "routes", "notes", "source_document"], 3),
    ("DataSource", "nodes_DataSource.csv", "datasource_id",
     ["path", "format", "note", "source_document"], 16),
    ("Section", "nodes_Section.csv", "section_id",
     ["label", "title", "question_count", "vulnerability_count", "source_document"], 7),
    ("Question", "nodes_Question.csv", "question_id",
     ["label", "section_id", "text", "option_count", "source_document"], 125),
    ("AnswerOption", "nodes_AnswerOption.csv", "answeroption_id",
     ["question_id", "ordinal", "text", "education", "reference", "next",
      "source_document"], 484),
    ("Vulnerability", "nodes_Vulnerability.csv", "vulnerability_id",
     ["label", "section_id", "title", "threat_count", "source_document"], 40),
    ("Threat", "nodes_Threat.csv", "threat_id", ["text", "source_document"], 148),
    ("ReferencedFramework", "nodes_ReferencedFramework.csv", "referencedframework_id",
     ["name", "description", "source_document"], 4),
    ("Domain", "nodes_Domain.csv", "domain_id",
     ["name", "domain_kind", "statement_count", "source_document"], 14),
    ("Statement", "nodes_Statement.csv", "statement_id_key",
     ["assessment", "statement_id", "description", "subcategory", "domain",
      "subject_tags", "in_md", "in_csv", "source_document"], 773),
    ("Subcategory", "nodes_Subcategory.csv", "subcategory_id",
     ["path", "source_document"], 110),
    ("SubjectTag", "nodes_SubjectTag.csv", "subjecttag_id",
     ["tag", "source_document"], 106),
    ("SupersededText", "nodes_SupersededText.csv", "supersededtext_id",
     ["label", "section_id", "text", "source_document"], 11),
]

# (rel_type, csv, [extra props], rows) --------------------------------------
RELS = [
    ("HAS_SECTION", "rels_HAS_SECTION.csv", [], 7),
    ("HAS_QUESTION", "rels_HAS_QUESTION.csv", [], 125),
    ("HAS_OPTION", "rels_HAS_OPTION.csv", [], 484),
    ("LEADS_TO", "rels_LEADS_TO.csv", ["next_label"], 439),
    ("HAS_VULNERABILITY", "rels_HAS_VULNERABILITY.csv", [], 40),
    ("HAS_THREAT", "rels_HAS_THREAT.csv", [], 206),
    ("CITES", "rels_CITES.csv", ["citation"], 1936),
    ("HAS_DOMAIN", "rels_HAS_DOMAIN.csv", [], 14),
    ("HAS_STATEMENT", "rels_HAS_STATEMENT.csv", [], 773),
    ("IN_SUBCATEGORY", "rels_IN_SUBCATEGORY.csv", [], 773),
    ("TAGGED", "rels_TAGGED.csv", [], 3334),
    ("ALSO_IN", "rels_ALSO_IN.csv", ["statement_id"], 315),
    ("SOURCED_FROM", "rels_SOURCED_FROM.csv", [], 14),
    ("SUPERSEDES", "rels_SUPERSEDES.csv", [], 2),
    ("HAD_PRIOR_TEXT", "rels_HAD_PRIOR_TEXT.csv", [], 11),
    ("FROM_SOURCE", "rels_FROM_SOURCE.csv", [], 11),
]

constraint = f"""
CREATE CONSTRAINT assessment_node_key IF NOT EXISTS
FOR (n:{ANCHOR}) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;
"""

framework = f"""
MERGE (f:AssessmentCatalog {{framework_id: '{FID}'}})
SET f.name = 'Assessments and Questionnaires',
    f.folder = 'Assessments and Questionnaires',
    f.source_document = 'DTOP-OLD assessment banks (SRA, CRI Expert Questionnaire, Maturity)',
    f.description = 'Three DTOP-OLD assessments: HIPAA SRA, CRI Profile v2.1 Expert Questionnaire, and the 6-domain Maturity Assessment.',
    f.status = 'extracted';
"""

roots = f"""
MATCH (f:AssessmentCatalog {{framework_id: '{FID}'}})
MATCH (n:{ANCHOR} {{framework_id: '{FID}'}})
WHERE NOT (:{ANCHOR} {{framework_id: '{FID}'}})-->(n)
MERGE (f)-[:HAS_ROOT]->(n);
"""

LOADER = Loader(
    framework_id=FID,
    name='Assessments and Questionnaires',
    folder=FOLDER,
    jurisdiction='n/a',
    source_document='DTOP-OLD assessment banks (SRA, CRI Expert Questionnaire, Maturity)',
    constraint_cypher=constraint,
    framework_cypher=framework,
    root_cypher=roots,
    anchor=ANCHOR,
    base_url=REPO_RAW_BASE,
    node_steps=[
        NodeStep(label=lbl, csv_name=csv, id_column=idc, properties=props,
                 rows=rows, cypher=node_cypher(lbl, idc, props))
        for (lbl, csv, idc, props, rows) in NODES
    ],
    rel_steps=[
        RelStep(rel_type=rt, csv_name=csv, properties=extra, rows=rows,
                cypher=rel_cypher(rt, extra))
        for (rt, csv, extra, rows) in RELS
    ],
)

if __name__ == "__main__":
    run(LOADER)
