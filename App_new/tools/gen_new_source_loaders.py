"""Author the 64 `App_new/<slug>.py` loaders for the `New sources/` folders.

Each generated file is a standalone, bespoke loader: it spells out that
framework's own Cypher — one MERGE per `nodes_<Label>.csv`, one per distinct
`rel_type` — derived from the CSV headers actually present on disk. Only the
argument parsing / dry-run / execution plumbing is shared, via
`new_sources_runtime`.

Re-run this whenever the CSVs under `New sources/` are regenerated:

    python App_new/tools/gen_new_source_loaders.py

Conventions the generated loaders follow, and why:

* Every node is merged on the anchor label `:NewSourceNode` keyed by
  `(framework_id, node_id)`, then given its own label and properties. The
  `rels_*.csv` files carry no endpoint labels, and 153 relationship types
  legitimately span several labels, so the anchor is what lets a relationship
  MATCH its endpoints exactly.
* Nine IDs (EU AI Act `annexIII_1..8`, UK NIS `sch2p9`) appear in two
  `nodes_*.csv` files each. Inspection of the source rows shows these are one
  entity modelled twice, not a collision — same text, same source line, same
  citation. Merging on the anchor gives them both labels on one node, which is
  the intended shape.
* `rel_type` inside the CSV is authoritative, not the filename: 397 of the 481
  rels files carry a type that differs from their name, and many carry several.
  Each distinct type gets its own filtered statement.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "New sources"
OUT_DIR = REPO / "App_new"

csv.field_size_limit(10 ** 9)

# Jurisdiction as recorded in `New sources/source-audit.md`. Nothing here is
# inferred — the audit groups the 23 US instruments under "Americas — USA" and
# names the jurisdiction explicitly for every other row.
JURISDICTION = {
    # Americas — USA (23)
    "NIST SP 800-53r5": "United States", "NIST SP 800-171r3": "United States",
    "NIST SP 800-207": "United States", "CMMC 2.0": "United States",
    "FISMA": "United States", "FedRAMP": "United States",
    "SOC 2 Trust Services Criteria": "United States",
    "Sarbanes-Oxley Act": "United States", "COSO ERM": "United States",
    "FFIEC Cybersecurity Assessment Tool": "United States",
    "NAIC Insurance Data Security Model Law": "United States",
    "COPPA": "United States", "FERPA (guidance)": "United States",
    "21 CFR Part 11": "United States",
    "FDA Medical Device Cybersecurity": "United States",
    "CPNI Rules": "United States", "DFARS": "United States",
    "ITAR": "United States", "DO-178C": "United States",
    "MITRE ATTACK": "United States",
    "Massachusetts Boards of Health Manual": "United States",
    "Massachusetts Fraud and Abuse Compliance": "United States",
    "CCPA 2025": "United States",
    # Americas — Latin America & Canada (6)
    "Canada PIPEDA": "Canada", "Mexico LFPDPPP": "Mexico",
    "Mexico LGPDPPSO": "Mexico", "Brazil LGPD": "Brazil",
    "Colombia Ley 1581": "Colombia", "Argentina PDPA": "Argentina",
    # Europe, UK & Germany (7)
    "EU AI Act": "European Union", "EU Cyber Resilience Act": "European Union",
    "eIDAS Regulation": "European Union", "ENISA ECSF": "European Union",
    "UK NIS Regulations 2018": "United Kingdom",
    "UK Cyber Essentials": "United Kingdom", "BSI C5": "Germany",
    # Asia-Pacific (15)
    "India IT Act 2000": "India", "RBI Cybersecurity Framework": "India",
    "SEBI Cybersecurity Framework": "India", "China PIPL": "China",
    "China Data Security Law": "China", "Japan APPI": "Japan",
    "South Korea PIPA": "South Korea", "Singapore PDPA": "Singapore",
    "MAS TRM Guidelines": "Singapore", "Indonesia PDP Law": "Indonesia",
    "Thailand PDPA": "Thailand", "Australia Privacy Act 1988": "Australia",
    "APRA CPS 234": "Australia", "ASD Essential Eight": "Australia",
    "Philippines DPA IRR": "Philippines",
    # Middle East, Africa & International (13)
    "UAE PDPL": "United Arab Emirates",
    "DIFC Data Protection Law": "United Arab Emirates",
    "ADGM Data Protection Regulations": "United Arab Emirates",
    "Qatar PDPPL": "Qatar", "Bahrain PDPL": "Bahrain",
    "Saudi NCA ECC-2 2024": "Saudi Arabia", "Turkey KVKK": "Turkey",
    "Switzerland revFADP": "Switzerland", "Russia 152-FZ": "Russia",
    "Kenya Data Protection Act": "Kenya",
    "Nigeria Data Protection Act 2023": "Nigeria",
    "South Africa POPIA": "South Africa", "UNECE UN R155": "International",
}


def slug(folder: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", folder).strip("_").lower()
    return re.sub(r"_+", "_", s)


def framework_id(folder: str) -> str:
    return slug(folder).upper()


def read_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return next(csv.reader(fh))


def scan(folder: Path):
    """Return (node_files, rel_files, source_documents) for one framework."""
    nodes = OrderedDict()
    id_owner: dict[str, set[str]] = {}
    source_docs: OrderedDict[str, int] = OrderedDict()

    for f in sorted(folder.glob("nodes_*.csv")):
        label = f.stem[len("nodes_"):]
        with f.open(encoding="utf-8-sig", newline="") as fh:
            r = csv.DictReader(fh)
            cols = r.fieldnames or []
            rows = 0
            ids: set[str] = set()
            for row in r:
                rows += 1
                v = (row.get(cols[0]) or "").strip()
                if v:
                    ids.add(v)
                    id_owner.setdefault(v, set()).add(label)
                # Some rows record several source documents in one cell, already
                # joined with " | " (e.g. FERPA). Split so the loader header
                # lists each document once.
                for doc in (row.get("source_document") or "").split(" | "):
                    doc = doc.strip()
                    if doc:
                        source_docs[doc] = source_docs.get(doc, 0) + 1
        nodes[label] = dict(file=f.name, id_column=cols[0], cols=cols, rows=rows,
                            distinct_ids=len(ids))

    # `loadable` is what the graph will actually hold. It differs from the CSV
    # row count in three ways, all properties of the source data rather than of
    # the load: a repeated id merges to one node; a repeated
    # (source, target, type) triple merges to one relationship; and an endpoint
    # that is blank or outside the corpus matches nothing, so the row is
    # dropped. Recording it here keeps the post-load reconciliation honest.
    for label, spec in nodes.items():
        spec["loadable"] = spec["distinct_ids"]

    known = set(id_owner)
    rels = []
    for f in sorted(folder.glob("rels_*.csv")):
        with f.open(encoding="utf-8-sig", newline="") as fh:
            r = csv.DictReader(fh)
            cols = r.fieldnames or []
            per_type: OrderedDict[str, int] = OrderedDict()
            seen_pairs: dict[str, set[tuple[str, str]]] = {}
            for row in r:
                t = (row.get("rel_type") or "").strip() or f.stem[len("rels_"):]
                per_type[t] = per_type.get(t, 0) + 1
                s_id = (row.get("source_id") or "").strip()
                t_id = (row.get("target_id") or "").strip()
                if s_id in known and t_id in known:
                    seen_pairs.setdefault(t, set()).add((s_id, t_id))
        loadable = {t: len(seen_pairs.get(t, ())) for t in per_type}
        rels.append(dict(file=f.name, cols=cols, per_type=per_type, loadable=loadable,
                         pairs=seen_pairs))

    # A triple can appear in two different rels files (DO-178C has one), and
    # MERGE collapses those too, so the folder-level total is the union.
    folder_triples: set[tuple[str, str, str]] = set()
    for r in rels:
        for t, pairs in r["pairs"].items():
            folder_triples |= {(s, tg, t) for s, tg in pairs}

    return nodes, rels, source_docs, len(folder_triples), len(id_owner)


#: Properties the anchor node is merged on. A CSV column of the same name must
#: never be written straight through, or it would overwrite the merge key and
#: strand the node outside its own framework. Four folders ship a
#: `nodes_Framework.csv` whose id column is literally `framework_id`.
RESERVED = ("framework_id", "node_id")


def prop_name(column: str) -> str:
    return f"csv_{column}" if column in RESERVED else column


def node_cypher(fid: str, label: str, spec: dict) -> str:
    idc = spec["id_column"]
    props = [c for c in spec["cols"] if c != idc]
    sets = [f"      n:{label}", f"      n.{prop_name(idc)} = row.{idc}"]
    sets += [f"      n.{prop_name(c)} = row.{c}" for c in props]
    body = ",\n".join(sets)
    return (
        f"LOAD CSV WITH HEADERS FROM '$file_path' AS row\n"
        f"CALL (row) {{\n"
        f"  MERGE (n:NewSourceNode {{framework_id: '{fid}', node_id: row.{idc}}})\n"
        f"  SET\n{body}\n"
        f"}} IN TRANSACTIONS OF 500 ROWS;\n"
    )


def rel_cypher(fid: str, rel_type: str, cols: list[str]) -> str:
    props = [c for c in cols if c not in ("source_id", "target_id", "rel_type")]
    set_clause = ""
    if props:
        set_clause = "\n  SET " + ",\n      ".join(
            f"r.{prop_name(c)} = row.{c}" for c in props)
    return (
        f"LOAD CSV WITH HEADERS FROM '$file_path' AS row\n"
        f"WITH row WHERE row.rel_type = '{rel_type}'\n"
        f"CALL (row) {{\n"
        f"  MATCH (s:NewSourceNode {{framework_id: '{fid}', node_id: row.source_id}})\n"
        f"  MATCH (t:NewSourceNode {{framework_id: '{fid}', node_id: row.target_id}})\n"
        f"  MERGE (s)-[r:{rel_type}]->(t){set_clause}\n"
        f"}} IN TRANSACTIONS OF 500 ROWS;\n"
    )


def py(s: str) -> str:
    return '"""' + s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"') + '"""'


def emit(folder: Path) -> tuple[str, str, int, int]:
    name = folder.name
    fid = framework_id(name)
    nodes, rels, source_docs, rels_total, nodes_total = scan(folder)
    jur = JURISDICTION.get(name)
    if jur is None:
        raise SystemExit(f"No jurisdiction recorded for {name!r}; add it to JURISDICTION.")
    docs = list(source_docs) or ["(not recorded in the CSVs)"]
    total_nodes = sum(s["rows"] for s in nodes.values())
    total_rels = sum(sum(r["per_type"].values()) for r in rels)  # CSV rows

    L = []
    L.append('"""Loader — %s.' % name)
    L.append("")
    L.append("Source folder : New sources/%s" % name)
    L.append("Source document(s):")
    for d in docs:
        L.append("    %s" % d)
    L.append("")
    L.append("Graph shape   : %d node labels, %d relationship types"
             % (len(nodes), sum(len(r['per_type']) for r in rels)))
    L.append("Expected size : %s nodes / %s relationships"
             % (f"{total_nodes:,}", f"{total_rels:,}"))
    L.append("")
    L.append("Generated by App_new/tools/gen_new_source_loaders.py from the CSV")
    L.append("headers on disk. Edit the generator, not this file.")
    L.append("")
    L.append("    python App_new/%s.py --dry-run   # validate, write nothing" % slug(name))
    L.append("    python App_new/%s.py             # load into Neo4j" % slug(name))
    L.append('"""')
    L.append("")
    L.append("import os")
    L.append("import sys")
    L.append("")
    L.append("sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))")
    L.append("")
    L.append("from new_sources_runtime import Loader, NodeStep, RelStep, run")
    L.append("")
    L.append("FRAMEWORK_ID = %r" % fid)
    L.append("FOLDER = %r" % name)
    L.append("")
    L.append("# --------------------------------------------------------------------------")
    L.append("# Framework root node. Labelled :NewSourceFramework, not :Framework —")
    L.append("# four folders ship a node of their own labelled Framework, and a bare")
    L.append("# :Framework merge key would silently fuse the root into it.")
    L.append("# --------------------------------------------------------------------------")
    L.append("")
    L.append("constraint = %s" % py(
        "\nCREATE CONSTRAINT new_source_node_key IF NOT EXISTS\n"
        "FOR (n:NewSourceNode) REQUIRE (n.framework_id, n.node_id) IS UNIQUE;\n"))
    L.append("")
    esc_docs = " | ".join(d.replace("'", "\\'") for d in docs)
    L.append("framework = %s" % py(
        f"\nMERGE (f:NewSourceFramework {{framework_id: '{fid}'}})\n"
        f"SET f.name = '{name.replace(chr(39), chr(92) + chr(39))}',\n"
        f"    f.jurisdiction = '{jur.replace(chr(39), chr(92) + chr(39))}',\n"
        f"    f.folder = '{name.replace(chr(39), chr(92) + chr(39))}',\n"
        f"    f.source_document = '{esc_docs}',\n"
        f"    f.status = 'extracted';\n"))
    L.append("")
    L.append("# Attach the framework to every node that nothing else points at, so each")
    L.append("# of the 64 graphs has a single entry point and can be traversed or deleted")
    L.append("# independently of the other 63.")
    L.append("roots = %s" % py(
        f"\nMATCH (f:NewSourceFramework {{framework_id: '{fid}'}})\n"
        f"MATCH (n:NewSourceNode {{framework_id: '{fid}'}})\n"
        f"WHERE NOT (:NewSourceNode {{framework_id: '{fid}'}})-->(n)\n"
        f"MERGE (f)-[:HAS_ROOT]->(n);\n"))
    L.append("")
    L.append("# --------------------------------------------------------------------------")
    L.append("# Nodes — one statement per nodes_<Label>.csv")
    L.append("# --------------------------------------------------------------------------")
    node_vars = []
    for label, spec in nodes.items():
        var = "node_" + slug(label)
        node_vars.append((var, label, spec))
        L.append("")
        L.append("# %s  (%s rows, key %s)" % (spec["file"], f"{spec['rows']:,}", spec["id_column"]))
        L.append("%s = %s" % (var, py("\n" + node_cypher(fid, label, spec))))

    L.append("")
    L.append("# --------------------------------------------------------------------------")
    L.append("# Relationships — one statement per rel_type. The rel_type column is")
    L.append("# authoritative; a single rels_*.csv may carry several types.")
    L.append("# --------------------------------------------------------------------------")
    rel_vars: list[tuple[str, str, dict, int]] = []
    seen = set()
    for r in rels:
        for rtype, count in r["per_type"].items():
            var = "rel_" + slug(rtype)
            n = 2
            while var in seen:
                var = "rel_%s_%d" % (slug(rtype), n)
                n += 1
            seen.add(var)
            rel_vars.append((var, rtype, r, count))
            L.append("")
            L.append("# %s -> :%s  (%s rows)" % (r["file"], rtype, f"{count:,}"))
            L.append("%s = %s" % (var, py("\n" + rel_cypher(fid, rtype, r["cols"]))))

    L.append("")
    L.append("# --------------------------------------------------------------------------")
    L.append("LOADER = Loader(")
    L.append("    framework_id=FRAMEWORK_ID,")
    L.append("    name=%r," % name)
    L.append("    folder=FOLDER,")
    L.append("    jurisdiction=%r," % jur)
    L.append("    source_document=%r," % " | ".join(docs))
    L.append("    constraint_cypher=constraint,")
    L.append("    framework_cypher=framework,")
    L.append("    root_cypher=roots,")
    L.append("    node_steps=[")
    for var, label, spec in node_vars:
        L.append("        NodeStep(label=%r, csv_name=%r, id_column=%r," % (label, spec["file"], spec["id_column"]))
        L.append("                 properties=%r," % [c for c in spec["cols"] if c != spec["id_column"]])
        L.append("                 rows=%d, loadable=%d, cypher=%s),"
                 % (spec["rows"], spec["loadable"], var))
    L.append("    ],")
    L.append("    rel_steps=[")
    for var, rtype, r, count in rel_vars:
        props = [c for c in r["cols"] if c not in ("source_id", "target_id", "rel_type")]
        L.append("        RelStep(rel_type=%r, csv_name=%r," % (rtype, r["file"]))
        L.append("                properties=%r," % props)
        L.append("                rows=%d, loadable=%d, cypher=%s),"
                 % (count, r["loadable"][rtype], var))
    L.append("    ],")
    L.append("    expected_nodes_total=%d," % nodes_total)
    L.append("    expected_rels_total=%d," % rels_total)
    L.append(")")
    L.append("")
    L.append("if __name__ == \"__main__\":")
    L.append("    run(LOADER)")
    L.append("")

    return slug(name) + ".py", "\n".join(L), total_nodes, total_rels


def main() -> int:
    folders = sorted(p for p in SOURCES.iterdir() if p.is_dir())
    if len(folders) != 64:
        print(f"warning: expected 64 folders, found {len(folders)}", file=sys.stderr)

    written, tn, tr = [], 0, 0
    for folder in folders:
        fname, text, n, r = emit(folder)
        (OUT_DIR / fname).write_text(text, encoding="utf-8")
        written.append((fname, folder.name, n, r))
        tn += n
        tr += r

    for fname, folder, n, r in written:
        print(f"  {fname:<46} {folder:<42} {n:>7,} nodes {r:>7,} rels")
    print(f"\n{len(written)} loaders written to App_new/ — {tn:,} nodes / {tr:,} relationships")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
