"""Reconcile what is in Neo4j against what each `New sources/` loader expects.

Compares, per framework, the node and relationship counts in the graph with the
`expected_nodes` / `expected_rels` the loader declares — which are distinct ids
and distinct (source, target, type) triples, not raw CSV rows. Read-only.

    python App_new/tools/verify_new_sources_graph.py
"""

from __future__ import annotations

import importlib.util
import logging
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "New sources"
APP_NEW = REPO / "App_new"

logging.getLogger("neo4j").setLevel(logging.ERROR)


def main() -> int:
    sys.path.insert(0, str(APP_NEW))
    from app import Neo4jConnect

    c = Neo4jConnect()
    if c.check_health() is not True:
        print("Neo4j unreachable", file=sys.stderr)
        return 1

    bad, en_t, er_t, gn_t, gr_t = [], 0, 0, 0, 0
    for p in sorted(x for x in SOURCES.iterdir() if x.is_dir()):
        slug = re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", p.name).strip("_")).lower()
        spec = importlib.util.spec_from_file_location(slug, APP_NEW / f"{slug}.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[slug] = mod
        spec.loader.exec_module(mod)
        L = mod.LOADER

        r = c.query(
            "MATCH (n:NewSourceNode {framework_id: $f}) "
            "OPTIONAL MATCH (n)-[e]->(:NewSourceNode {framework_id: $f}) "
            "RETURN count(DISTINCT n) AS nodes, count(DISTINCT e) AS rels",
            others={"f": L.framework_id})
        gn, gr = r[0]["nodes"], r[0]["rels"]
        ok = gn == L.expected_nodes and gr == L.expected_rels
        en_t += L.expected_nodes; er_t += L.expected_rels; gn_t += gn; gr_t += gr
        print(f"{'ok  ' if ok else 'FAIL'}  {p.name:<42} "
              f"{gn:>7,}/{L.expected_nodes:<7,} nodes  {gr:>7,}/{L.expected_rels:<7,} rels")
        if not ok:
            bad.append(p.name)

    roots = c.query("MATCH (f:NewSourceFramework) RETURN count(f) AS n")[0]["n"]
    orphan = c.query("MATCH (f:NewSourceFramework) WHERE f:NewSourceNode "
                     "RETURN count(f) AS n")[0]["n"]
    print("-" * 92)
    print(f"graph    {gn_t:,} nodes / {gr_t:,} relationships")
    print(f"expected {en_t:,} nodes / {er_t:,} relationships")
    print(f":NewSourceFramework root nodes: {roots} (fused into a CSV node: {orphan})")
    print(f"{len(bad)} framework(s) off" if bad else "all 64 frameworks reconcile")
    for n in bad:
        print("   ", n)
    c.close()
    return 1 if bad or roots != 64 or orphan else 0


if __name__ == "__main__":
    raise SystemExit(main())
