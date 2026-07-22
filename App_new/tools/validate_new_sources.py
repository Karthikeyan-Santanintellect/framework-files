"""Dry-run validation for the 64 `New sources/` loaders. Writes nothing to Neo4j.

Checks, per framework:

  1. a loader exists in App_new/ and imports cleanly;
  2. every `nodes_*.csv` and `rels_*.csv` in the folder is covered by a step,
     and no step names a file that is not there;
  3. the row counts declared in the loader match the CSVs on disk;
  4. the node total matches the figure recorded in `New sources/source-audit.md`;
  5. every `source_id` / `target_id` resolves to a node the loader will create
     (dangling endpoints are reported — Neo4j would silently skip those rows);
  6. every CSV URL the loader will hand to LOAD CSV returns 200 (`--check-urls`).

    python App_new/tools/validate_new_sources.py
    python App_new/tools/validate_new_sources.py --check-urls
    python App_new/tools/validate_new_sources.py --only "EU AI Act"
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "New sources"
APP_NEW = REPO / "App_new"
AUDIT = SOURCES / "source-audit.md"

csv.field_size_limit(10 ** 9)


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = mod
    spec.loader.exec_module(mod)
    return mod


def audit_node_counts() -> dict[str, int]:
    """Folder -> node count as recorded in source-audit.md (`→ `Folder/` (N nodes)`)."""
    text = AUDIT.read_text(encoding="utf-8")
    out = {}
    for folder, count in re.findall(r"→ `([^`]+?)/` \(([\d,]+) nodes\)", text):
        out[folder] = int(count.replace(",", ""))
    return out


def head_ok(url: str) -> str | None:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return None if resp.status == 200 else f"HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}"
    except Exception as e:
        return f"{type(e).__name__}: {e}"


def check(loader, folder: Path, audit: dict[str, int], check_urls: bool):
    problems, notes = [], []

    # -- coverage -------------------------------------------------------
    on_disk_nodes = {f.name for f in folder.glob("nodes_*.csv")}
    on_disk_rels = {f.name for f in folder.glob("rels_*.csv")}
    step_nodes = {s.csv_name for s in loader.node_steps}
    step_rels = {s.csv_name for s in loader.rel_steps}

    for missing in sorted(on_disk_nodes - step_nodes):
        problems.append(f"node CSV not covered by any step: {missing}")
    for missing in sorted(on_disk_rels - step_rels):
        problems.append(f"rel CSV not covered by any step: {missing}")
    for extra in sorted(step_nodes - on_disk_nodes) + sorted(step_rels - on_disk_rels):
        problems.append(f"step references a CSV that is not on disk: {extra}")

    # -- the anchor properties must never be written from a CSV column ----
    # Overwriting `framework_id` or `node_id` would strand the node outside
    # its own framework and orphan every relationship pointing at it.
    for s in loader.node_steps:
        for col in (s.id_column, *s.properties):
            if col in ("framework_id", "node_id") and f"n.{col} = row.{col}" in s.cypher:
                problems.append(f"{s.csv_name}: column {col!r} is written straight to the "
                                f"anchor property n.{col}, which overwrites the merge key")

    # -- row counts + id index -------------------------------------------
    known: set[str] = set()
    for s in loader.node_steps:
        p = folder / s.csv_name
        if not p.exists():
            continue
        with p.open(encoding="utf-8-sig", newline="") as fh:
            r = csv.DictReader(fh)
            if (r.fieldnames or [None])[0] != s.id_column:
                problems.append(f"{s.csv_name}: id column is "
                                f"{(r.fieldnames or ['?'])[0]!r}, loader says {s.id_column!r}")
            rows = 0
            for row in r:
                rows += 1
                v = (row.get(s.id_column) or "").strip()
                if v:
                    known.add(v)
                else:
                    problems.append(f"{s.csv_name}: blank {s.id_column} on data row {rows}")
        if rows != s.rows:
            problems.append(f"{s.csv_name}: {rows} rows on disk, loader declares {s.rows}")

    # -- relationship counts + dangling endpoints -------------------------
    declared = defaultdict(int)
    for s in loader.rel_steps:
        declared[(s.csv_name, s.rel_type)] = s.rows
    actual = defaultdict(int)
    dangling = 0
    dangling_detail = defaultdict(int)
    blank = 0
    blank_detail = defaultdict(int)
    for csv_name in sorted(step_rels):
        p = folder / csv_name
        if not p.exists():
            continue
        with p.open(encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                t = (row.get("rel_type") or "").strip() or csv_name[len("rels_"):-4]
                actual[(csv_name, t)] += 1
                for side in ("source_id", "target_id"):
                    v = (row.get(side) or "").strip()
                    if not v:
                        blank += 1
                        blank_detail[(csv_name, t, side)] += 1
                    elif v not in known:
                        dangling += 1
                        dangling_detail[(csv_name, t, side)] += 1
    for key in set(declared) | set(actual):
        if declared.get(key, 0) != actual.get(key, 0):
            problems.append(f"{key[0]} [{key[1]}]: {actual.get(key, 0)} rows on disk, "
                            f"loader declares {declared.get(key, 0)}")
    if dangling:
        top = sorted(dangling_detail.items(), key=lambda kv: -kv[1])[:3]
        notes.append(f"{dangling} relationship endpoint(s) reference an id no node CSV "
                     f"defines — Neo4j will skip those rows. "
                     + "; ".join(f"{k[0]}[{k[1]}].{k[2]}={v}" for k, v in top))
    if blank:
        top = sorted(blank_detail.items(), key=lambda kv: -kv[1])[:3]
        notes.append(f"{blank} relationship endpoint(s) are blank — the citation has no "
                     f"target inside this corpus, so Neo4j will skip those rows. "
                     + "; ".join(f"{k[0]}[{k[1]}].{k[2]}={v}" for k, v in top))

    # -- audit reconciliation --------------------------------------------
    expected = audit.get(folder.name)
    if expected is None:
        notes.append("no node count recorded in source-audit.md")
    elif expected != loader.csv_node_rows:
        problems.append(f"node CSV rows {loader.csv_node_rows} != source-audit.md "
                        f"figure {expected}")

    # -- loadable vs CSV rows ---------------------------------------------
    if loader.expected_nodes != loader.csv_node_rows:
        notes.append(f"{loader.csv_node_rows - loader.expected_nodes} id(s) appear in "
                     f"two nodes_*.csv files — one entity modelled under two labels, so "
                     f"MERGE yields one node carrying both; the graph should hold "
                     f"{loader.expected_nodes:,} of {loader.csv_node_rows:,} rows")
    if loader.expected_rels != loader.csv_rel_rows:
        notes.append(f"{loader.csv_rel_rows - loader.expected_rels} of "
                     f"{loader.csv_rel_rows} relationship rows will not become a "
                     f"relationship (repeated triple, or an endpoint that is blank "
                     f"or outside the corpus); the graph should hold "
                     f"{loader.expected_rels:,}")

    # -- URLs -------------------------------------------------------------
    if check_urls:
        for csv_name in sorted(step_nodes | step_rels):
            why = head_ok(loader.url(csv_name))
            if why:
                problems.append(f"URL not reachable ({why}): {loader.url(csv_name)}")

    return problems, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check-urls", action="store_true",
                    help="HEAD every CSV URL (1,461 requests; slow)")
    ap.add_argument("--only", help="validate a single folder by name")
    args = ap.parse_args()

    sys.path.insert(0, str(APP_NEW))
    audit = audit_node_counts()

    folders = sorted(p for p in SOURCES.iterdir() if p.is_dir())
    if args.only:
        folders = [p for p in folders if p.name == args.only]
        if not folders:
            print(f"no folder named {args.only!r}", file=sys.stderr)
            return 2

    total_n = total_r = 0
    failed, noted = [], []
    for folder in folders:
        slug = re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", folder.name).strip("_")).lower()
        path = APP_NEW / f"{slug}.py"
        if not path.exists():
            print(f"FAIL  {folder.name}: no loader at App_new/{slug}.py")
            failed.append(folder.name)
            continue
        try:
            loader = load_module(path).LOADER
        except Exception as e:
            print(f"FAIL  {folder.name}: loader will not import — {type(e).__name__}: {e}")
            failed.append(folder.name)
            continue

        problems, notes = check(loader, folder, audit, args.check_urls)
        total_n += loader.expected_nodes
        total_r += loader.expected_rels
        status = "FAIL" if problems else ("WARN" if notes else "ok  ")
        print(f"{status}  {folder.name:<42} {loader.expected_nodes:>7,} nodes "
              f"{loader.expected_rels:>7,} rels  "
              f"{len(loader.node_steps):>3} labels {len(loader.rel_steps):>3} rel types")
        for p in problems:
            print(f"        ! {p}")
        for n in notes:
            print(f"        ~ {n}")
        if problems:
            failed.append(folder.name)
        elif notes:
            noted.append(folder.name)

    print("-" * 96)
    print(f"{len(folders)} framework(s): {total_n:,} nodes / {total_r:,} relationships")
    print(f"{len(failed)} failing, {len(noted)} with warnings, "
          f"{len(folders) - len(failed) - len(noted)} clean")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
