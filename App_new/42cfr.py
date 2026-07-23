"""Loader — 42 CFR Part 2 (Confidentiality of SUD Patient Records).

Verified and loaded 2026-07-23. Replaces an earlier draft that created a
`Regulation` node the relationships never matched and joined every subpart to
every section (and every entity to every entity) with cartesian MERGEs.

This loader reads the folder's CSVs locally and loads them with parameterised
UNWIND — no LOAD CSV, so it does not depend on a branch or raw-URL being
reachable. Nodes carry `regional_standard_regulation_id = '42_CFR_PART_2'`, the
same identifier property the other regional regulations use, so the framework
appears in the graph explorer alongside them.

Graph: 1 regulation + 5 subparts + 38 sections + 13 entities + 4 assets +
9 controls, wired as Regulation→Subpart→Section (section-to-subpart inferred
from the section number, which is exact for Part 2) plus the regulation to its
defined entities, assets and controls.

    python App_new/42cfr.py
"""

import csv
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import Neo4jConnect

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("42cfr")

RID = "42_CFR_PART_2"
FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "42 CFR Part 2")

# file -> (Neo4j label, id column)
NODE_FILES = {
    "42 CFR - Subpart.csv": ("Subpart", "id"),
    "42 CFR - Sections.csv": ("Section", "id"),
    "42 CFR - Entity.csv": ("Entity", "id"),
    "42 CFR - Asset .csv": ("Asset", "id"),
    "42 CFR - Control.csv": ("Control", "id"),
}


def rows(name):
    with open(os.path.join(FOLDER, name), encoding="utf-8-sig", newline="") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def subpart_of(section_id):
    """Section number -> subpart id. Exact for Part 2's numbering scheme.

    The number after the dot is a section index, not a decimal — '2.1' is
    section 1 (Subpart A), '2.11' is section 11 (Subpart B) — so it must be
    parsed as an integer string, never as a float.
    """
    d = int(section_id.replace("SEC-", "").split(".")[1])   # '2.11' -> 11
    if d < 10:  return "SUB-A"
    if d < 30:  return "SUB-B"
    if d < 50:  return "SUB-C"
    if d < 60:  return "SUB-D"
    return "SUB-E"


def main():
    c = Neo4jConnect()
    if c.check_health() is not True:
        log.error("Neo4j unreachable"); return 1

    c.query(
        "MERGE (r:RegionalStandardAndRegulation {regional_standard_regulation_id:$rid}) "
        "SET r.name='42 CFR Part 2', r.citation='42 CFR Part 2', "
        "r.jurisdiction='US Federal', r.authority='Secretary of HHS', "
        "r.description='Confidentiality of Substance Use Disorder Patient Records'",
        others={"rid": RID})

    total_nodes = 0
    for fname, (label, idc) in NODE_FILES.items():
        data = rows(fname)
        for d in data:
            d["node_id"] = d[idc]
        c.query(
            f"UNWIND $rows AS row "
            f"MERGE (n:{label} {{regional_standard_regulation_id:$rid, node_id:row.node_id}}) "
            f"SET n += row",
            others={"rows": data, "rid": RID})
        total_nodes += len(data)
        log.info("  %-10s %3d nodes", label, len(data))

    # Regulation -> Subpart
    c.query("MATCH (r:RegionalStandardAndRegulation {regional_standard_regulation_id:$rid}) "
            "MATCH (s:Subpart {regional_standard_regulation_id:$rid}) "
            "MERGE (r)-[:REGULATION_HAS_SUBPART]->(s)", others={"rid": RID})
    # Subpart -> Section (inferred, exact)
    sec_map = [{"sec": s["id"], "sub": subpart_of(s["id"])} for s in rows("42 CFR - Sections.csv")]
    c.query("UNWIND $m AS m "
            "MATCH (sub:Subpart {regional_standard_regulation_id:$rid, node_id:m.sub}) "
            "MATCH (sec:Section {regional_standard_regulation_id:$rid, node_id:m.sec}) "
            "MERGE (sub)-[:SUBPART_HAS_SECTION]->(sec)", others={"m": sec_map, "rid": RID})
    # Regulation -> Entity / Asset / Control
    for label, rel in [("Entity", "REGULATION_DEFINES_ENTITY"),
                       ("Asset", "REGULATION_DEFINES_ASSET"),
                       ("Control", "REGULATION_DEFINES_CONTROL")]:
        c.query(f"MATCH (r:RegionalStandardAndRegulation {{regional_standard_regulation_id:$rid}}) "
                f"MATCH (n:{label} {{regional_standard_regulation_id:$rid}}) "
                f"MERGE (r)-[:{rel}]->(n)", others={"rid": RID})

    got = c.query("MATCH (n {regional_standard_regulation_id:$rid}) "
                  "OPTIONAL MATCH (n)-[r]->({regional_standard_regulation_id:$rid}) "
                  "RETURN count(DISTINCT n) AS n, count(DISTINCT r) AS r", others={"rid": RID})[0]
    log.info("in graph: %d nodes / %d relationships (%d node rows loaded + 1 regulation)",
             got["n"], got["r"], total_nodes)
    c.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
