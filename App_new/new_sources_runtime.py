"""Shared execution plumbing for the 64 `New sources/` loaders.

Every framework in `New sources/` has its own loader in this directory
(`App_new/<slug>.py`). Those files hold the framework's bespoke Cypher: one
statement per `nodes_*.csv` label and one per relationship type. This module
holds only the parts that are identical for all of them — argument parsing,
dry-run reporting, URL reachability checks and sequenced execution — so the
loaders stay readable as schema documents.

Usage from a loader:

    from new_sources_runtime import Loader, NodeStep, RelStep
    ...
    if __name__ == "__main__":
        LOADER.main()

Run a loader with `--dry-run` to validate without touching Neo4j.
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("new_sources")

# The `New sources/` tree lives on branch `gautham`; it is not on `main`.
# Update this one constant after the branch merges.
REPO_RAW_BASE = (
    "https://github.com/Karthikeyan-Santanintellect/framework-files"
    "/raw/refs/heads/gautham"
)
RAW_BASE = f"{REPO_RAW_BASE}/New%20sources"

#: Every node loaded from `New sources/` carries this label in addition to its
#: own, keyed by (framework_id, node_id). The `rels_*.csv` files record only
#: `source_id`/`target_id` with no endpoint label, and 153 relationship types
#: legitimately span several labels, so this anchor is what makes the
#: relationship MATCHes exact.
ANCHOR = "NewSourceNode"


@dataclass
class NodeStep:
    """One `nodes_<Label>.csv` file."""

    label: str
    csv_name: str
    id_column: str
    properties: list[str]
    rows: int
    cypher: str
    #: Distinct non-blank ids. Equals `rows` unless the CSV repeats an id, in
    #: which case MERGE correctly produces one node for several rows.
    loadable: int = -1

    def __post_init__(self):
        if self.loadable < 0:
            self.loadable = self.rows


@dataclass
class RelStep:
    """One relationship type within one `rels_*.csv` file.

    A single rels file may carry several `rel_type` values, so the loader emits
    one step per distinct type and filters the CSV on it.
    """

    rel_type: str
    csv_name: str
    properties: list[str]
    rows: int
    cypher: str
    #: Rows that will actually become a relationship: distinct
    #: (source_id, target_id) pairs whose endpoints both exist. Below `rows`
    #: where the CSV repeats a pair (MERGE collapses it) or where an endpoint
    #: is blank or outside the corpus (the MATCH finds nothing).
    loadable: int = -1

    def __post_init__(self):
        if self.loadable < 0:
            self.loadable = self.rows


@dataclass
class Loader:
    framework_id: str
    name: str
    folder: str
    jurisdiction: str
    source_document: str
    framework_cypher: str
    constraint_cypher: str
    root_cypher: str
    node_steps: list[NodeStep] = field(default_factory=list)
    rel_steps: list[RelStep] = field(default_factory=list)
    #: Distinct node ids across the whole folder. Summing the per-file figures
    #: would double-count an id that appears in two nodes_*.csv files — the EU
    #: AI Act has 8 and UK NIS 1, each one entity deliberately modelled under
    #: two labels — so the folder-level total is computed once at generation.
    expected_nodes_total: int = -1
    #: Anchor label these nodes are merged under, and the raw base their CSVs
    #: sit below. The defaults are what the 64 `New sources/` loaders use;
    #: a folder outside that tree overrides both. Keeping a separate anchor
    #: matters — `tools/repair_stranded_nodes.py` deletes any `:NewSourceNode`
    #: whose framework_id is not one of the 64 folders.
    anchor: str = ANCHOR
    base_url: str = RAW_BASE
    #: Distinct (source, target, type) triples across the whole folder. Summing
    #: the per-step figures would double-count a triple that appears in two
    #: different rels files — DO-178C has one such pair — so the framework-level
    #: total is computed once at generation and carried here.
    expected_rels_total: int = -1

    # -- helpers ---------------------------------------------------------
    def url(self, csv_name: str) -> str:
        from urllib.parse import quote

        return f"{self.base_url}/{quote(self.folder)}/{quote(csv_name)}"

    @property
    def csv_node_rows(self) -> int:
        return sum(s.rows for s in self.node_steps)

    @property
    def csv_rel_rows(self) -> int:
        return sum(s.rows for s in self.rel_steps)

    @property
    def expected_nodes(self) -> int:
        """Nodes the graph should hold — distinct ids, not CSV rows."""
        if self.expected_nodes_total >= 0:
            return self.expected_nodes_total
        return sum(s.loadable for s in self.node_steps)

    @property
    def expected_rels(self) -> int:
        """Relationships the graph should hold.

        Below the CSV row count wherever a folder repeats a
        (source, target, type) triple or cites something outside the corpus;
        both are properties of the source data, not of the load.
        """
        if self.expected_rels_total >= 0:
            return self.expected_rels_total
        return sum(s.loadable for s in self.rel_steps)

    def statements(self) -> list[tuple[str, str]]:
        """(description, cypher) in execution order, URLs substituted."""
        out: list[tuple[str, str]] = [
            ("constraint", self.constraint_cypher),
            (f"framework node {self.framework_id}", self.framework_cypher),
        ]
        for s in self.node_steps:
            out.append(
                (f"nodes  {s.label:<28} {s.rows:>6} rows",
                 s.cypher.replace("$file_path", self.url(s.csv_name)))
            )
        for s in self.rel_steps:
            out.append(
                (f"rels   {s.rel_type:<28} {s.rows:>6} rows",
                 s.cypher.replace("$file_path", self.url(s.csv_name)))
            )
        out.append(("link framework to root nodes", self.root_cypher))
        return out

    # -- modes -----------------------------------------------------------
    def dry_run(self, check_urls: bool = True, show_cypher: bool = False) -> int:
        """Report the plan without writing to Neo4j. Returns an exit code."""
        logger.info("=" * 78)
        logger.info("%s  (framework_id=%s)", self.name, self.framework_id)
        from urllib.parse import unquote

        tree = unquote(self.base_url[len(REPO_RAW_BASE):].lstrip("/"))
        logger.info("folder      %s%s", f"{tree}/" if tree else "", self.folder)
        logger.info("source      %s", self.source_document)
        logger.info("expects     %s nodes / %s relationships across %s node files "
                    "and %s relationship types",
                    f"{self.expected_nodes:,}", f"{self.expected_rels:,}",
                    len(self.node_steps), len(self.rel_steps))
        logger.info("=" * 78)

        for desc, cypher in self.statements():
            logger.info("  %s", desc)
            if show_cypher:
                logger.info("%s", "\n".join("      " + l for l in cypher.strip().splitlines()))

        if not check_urls:
            return 0

        csv_names = [s.csv_name for s in self.node_steps]
        csv_names += [s.csv_name for s in self.rel_steps if s.csv_name not in csv_names]
        logger.info("-" * 78)
        logger.info("checking %s CSV URLs...", len(csv_names))
        bad = []
        for csv_name in csv_names:
            u = self.url(csv_name)
            try:
                req = urllib.request.Request(u, method="HEAD")
                with urllib.request.urlopen(req, timeout=30) as resp:
                    if resp.status != 200:
                        bad.append((csv_name, str(resp.status)))
            except urllib.error.HTTPError as e:
                bad.append((csv_name, f"HTTP {e.code}"))
            except Exception as e:  # network/DNS/TLS
                bad.append((csv_name, type(e).__name__ + ": " + str(e)))
        if bad:
            logger.error("  %s URL(s) NOT reachable:", len(bad))
            for csv_name, why in bad:
                logger.error("    %-55s %s", csv_name, why)
            return 1
        logger.info("  all %s URLs reachable", len(csv_names))
        return 0

    def execute(self, pause: float = 0.5) -> int:
        from app import Neo4jConnect

        client = Neo4jConnect()
        health = client.check_health()
        if health is not True:
            logger.error("Neo4j connection error: %s", health)
            client.close()
            return 1

        logger.info("Loading %s into Neo4j...", self.name)
        failures = 0
        try:
            for desc, cypher in self.statements():
                logger.info("  %s", desc)
                result = client.query(cypher)
                if isinstance(result, str):  # Neo4jConnect returns the error text
                    logger.error("    FAILED: %s", result)
                    failures += 1
                time.sleep(pause)

            counts = client.query(
                f"MATCH (n:{self.anchor} {{framework_id: $fid}}) "
                f"OPTIONAL MATCH (n)-[r]->(:{self.anchor} {{framework_id: $fid}}) "
                f"RETURN count(DISTINCT n) AS nodes, count(DISTINCT r) AS rels",
                others={"fid": self.framework_id},
            )
        finally:
            client.close()

        if isinstance(counts, list) and counts:
            got_n, got_r = counts[0]["nodes"], counts[0]["rels"]
            logger.info("in graph: %s nodes / %s relationships (expected %s / %s)",
                        f"{got_n:,}", f"{got_r:,}",
                        f"{self.expected_nodes:,}", f"{self.expected_rels:,}")
            if got_n != self.expected_nodes or got_r != self.expected_rels:
                logger.warning("count mismatch — see the folder README for known "
                               "dangling references")
        return 1 if failures else 0

    def main(self, argv: list[str] | None = None) -> int:
        p = argparse.ArgumentParser(description=f"Load {self.name} into Neo4j.")
        p.add_argument("--dry-run", action="store_true",
                       help="report the plan and check CSV URLs; write nothing")
        p.add_argument("--no-url-check", action="store_true",
                       help="with --dry-run, skip the network reachability check")
        p.add_argument("--show-cypher", action="store_true",
                       help="with --dry-run, print every generated statement")
        args = p.parse_args(argv)
        if args.dry_run:
            code = self.dry_run(check_urls=not args.no_url_check,
                                show_cypher=args.show_cypher)
        else:
            code = self.execute()
        return code


def run(loader: Loader) -> None:
    sys.exit(loader.main())
