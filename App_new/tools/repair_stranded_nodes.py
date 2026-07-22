"""Remove nodes stranded outside their own framework, then report what is left.

Four folders ship a `nodes_Framework.csv` whose id column is literally
`framework_id` — the same name as the anchor property the loaders merge on. An
earlier generator wrote that column straight through, overwriting the merge key,
so the node landed under the CSV's own value (MITRE's, for instance, became
`FW-ATTACK-ENT`) and every relationship pointing at it failed to match.

The generator no longer does this — the column is written as `csv_framework_id`
— but any node created before the fix is still stranded. This deletes those and
nothing else: a node is stranded exactly when its `framework_id` is not one of
the 64 folder ids.

    python App_new/tools/repair_stranded_nodes.py --dry-run
    python App_new/tools/repair_stranded_nodes.py
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "New sources"
APP_NEW = REPO / "App_new"

logging.getLogger("neo4j").setLevel(logging.ERROR)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report, delete nothing")
    args = ap.parse_args()

    sys.path.insert(0, str(APP_NEW))
    from app import Neo4jConnect

    valid = {re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", p.name).strip("_")).upper()
             for p in SOURCES.iterdir() if p.is_dir()}
    print(f"{len(valid)} valid framework ids")

    c = Neo4jConnect()
    if c.check_health() is not True:
        print("Neo4j unreachable", file=sys.stderr)
        return 1

    rows = c.query(
        "MATCH (n:NewSourceNode) WHERE NOT n.framework_id IN $valid "
        "RETURN n.framework_id AS fid, labels(n) AS labels, count(*) AS c "
        "ORDER BY c DESC", others={"valid": sorted(valid)})
    if not rows:
        print("no stranded nodes")
        c.close()
        return 0

    total = sum(r["c"] for r in rows)
    print(f"{total} stranded node(s):")
    for r in rows:
        print(f"  framework_id={r['fid']!r:<22} labels={r['labels']}  x{r['c']}")

    if args.dry_run:
        print("\n--dry-run: nothing deleted")
        c.close()
        return 0

    c.query("MATCH (n:NewSourceNode) WHERE NOT n.framework_id IN $valid "
            "DETACH DELETE n", others={"valid": sorted(valid)})
    left = c.query("MATCH (n:NewSourceNode) WHERE NOT n.framework_id IN $valid "
                   "RETURN count(n) AS n", others={"valid": sorted(valid)})
    print(f"\ndeleted {total}; stranded remaining: {left[0]['n']}")
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
