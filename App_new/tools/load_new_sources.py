"""Load every `New sources/` framework into Neo4j, one loader at a time.

Runs the 64 `App_new/<slug>.py` loaders in ascending size order, so anything
structurally wrong surfaces on a small framework before the 16,535-node DFARS
graph is attempted. Each loader is idempotent (everything is MERGE keyed on
`(framework_id, node_id)`), so a re-run repairs a partial load rather than
duplicating it.

    python App_new/tools/load_new_sources.py                 # all 64
    python App_new/tools/load_new_sources.py --only DFARS    # one
    python App_new/tools/load_new_sources.py --skip-loaded   # resume a run
"""

from __future__ import annotations

import argparse
import importlib.util
import logging
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "New sources"
APP_NEW = REPO / "App_new"

logging.getLogger("neo4j").setLevel(logging.ERROR)


def slug(name: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")).lower()


def load_loader(name: str):
    path = APP_NEW / f"{slug(name)}.py"
    spec = importlib.util.spec_from_file_location(slug(name), path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[slug(name)] = mod
    spec.loader.exec_module(mod)
    return mod.LOADER


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append", help="load only these folders")
    ap.add_argument("--skip-loaded", action="store_true",
                    help="skip frameworks already at their expected node count")
    args = ap.parse_args()

    sys.path.insert(0, str(APP_NEW))
    from app import Neo4jConnect

    names = [p.name for p in sorted(SOURCES.iterdir()) if p.is_dir()]
    if args.only:
        names = [n for n in names if n in set(args.only)]

    loaders = sorted((load_loader(n) for n in names), key=lambda l: l.expected_nodes)

    probe = Neo4jConnect()
    if probe.check_health() is not True:
        print("Neo4j unreachable", file=sys.stderr)
        return 1

    results, started = [], time.time()
    for i, L in enumerate(loaders, 1):
        if args.skip_loaded:
            got = probe.query(
                "MATCH (n:NewSourceNode {framework_id: $f}) RETURN count(n) AS n",
                others={"f": L.framework_id})
            if isinstance(got, list) and got and got[0]["n"] == L.expected_nodes:
                print(f"[{i:>2}/{len(loaders)}] skip {L.name} — already at "
                      f"{L.expected_nodes:,} nodes", flush=True)
                continue

        t0 = time.time()
        print(f"[{i:>2}/{len(loaders)}] {L.name} — {L.expected_nodes:,} nodes / "
              f"{L.expected_rels:,} rels", flush=True)
        code = L.execute(pause=0.1)

        counts = probe.query(
            "MATCH (n:NewSourceNode {framework_id: $f}) "
            "OPTIONAL MATCH (n)-[r]->(:NewSourceNode {framework_id: $f}) "
            "RETURN count(DISTINCT n) AS nodes, count(DISTINCT r) AS rels",
            others={"f": L.framework_id})
        got_n = counts[0]["nodes"] if isinstance(counts, list) and counts else -1
        got_r = counts[0]["rels"] if isinstance(counts, list) and counts else -1
        ok = code == 0 and got_n == L.expected_nodes and got_r == L.expected_rels
        results.append((L.name, L.expected_nodes, got_n, L.expected_rels, got_r, ok))
        print(f"           -> {got_n:,}/{L.expected_nodes:,} nodes, "
              f"{got_r:,}/{L.expected_rels:,} rels "
              f"[{'ok' if ok else 'MISMATCH'}] {time.time() - t0:.0f}s", flush=True)

    print("=" * 92, flush=True)
    bad = [r for r in results if not r[5]]
    for name, en, gn, er, gr, _ in bad:
        print(f"MISMATCH  {name:<42} nodes {gn:,}/{en:,}  rels {gr:,}/{er:,}")
    total = probe.query("MATCH (n:NewSourceNode) RETURN count(n) AS n")
    print(f"{len(results)} loaded, {len(bad)} mismatched, "
          f"{time.time() - started:.0f}s total")
    print(f":NewSourceNode in graph: {total[0]['n']:,}")
    probe.close()
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
