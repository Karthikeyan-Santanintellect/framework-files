"""Build the DTOP Catalogs node and relationship CSVs from the two catalog JSONs.

Reads the DTOP risk and control catalogues out of the DTOP-OLD client assets and
writes the same `nodes_<Label>.csv` / `rels_<TYPE>.csv` shape used by the
framework folders in this repository: the first column of a nodes file is
`<label>_id`, and every rels file is `source_id,target_id,rel_type` plus any
edge properties.

    python "DTOP Catalogs/build_csvs.py"

Both JSONs are already graph exports (`nodes` / `rels` with Neo4j element ids).
Those element ids come from two *different* instances and are not stable, so
they are discarded and every node is re-keyed on its own content — see
`ID_SCHEME` below.

The two files share a taxonomy: all 11 `Domain` names and 32 of the 36
`FunctionalDomain` names appear in both, byte-identical. They are deduplicated
into one set of nodes so risks and controls hang off the same domain tree, and
a `catalogs` column on every row records which file(s) the row came from.

Everything written is present in the JSON. The derived columns are the counts
(`*_count`), the `catalogs` provenance column, the denormalised parent names on
Risk/Control, and `source_label` on CSFFunction, which records the label's
original spelling.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

SOURCE_DIR = Path(
    "/Users/gauthamsmacbook/Apps/Santan/DTOP-OLD/client/src/assets/docs"
    "/knowledgeRepository/graph/DtopCatalogs"
)
#: Recorded on every row, matching how the framework folders cite their source.
DOC_BASE = (
    "DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs"
)
DOC = {
    "risk": f"{DOC_BASE}/risk-catalog.json",
    "control": f"{DOC_BASE}/control-catalog.json",
}
OUT = Path(__file__).resolve().parent

#: How each label's `<label>_id` is built. Control is the one label with a
#: natural key already in the source — `control_id` ("WEB-10") is unique across
#: all 1,451 — so it is used verbatim rather than being re-slugged into a
#: synthetic id and forcing the source property to be renamed.
ID_SCHEME = {
    "Domain": "dom_<slug(name)>",
    "FunctionalDomain": "fd_<slug(name)>",
    "Risk": "risk_<slug(title)>",
    "Control": "the source control_id, verbatim",
    "Solution": "sol_<slug(size)>_<sha1(size|description)[:10]>",
    "Weighting": "wt_<value>",
    "CSFFunction": "csf_<slug(name)>",
}

#: The control catalog writes this label with a space in it. It is loaded as
#: `CSFFunction` so no query needs backticks; the original spelling is kept as
#: the `source_label` column.
CSF_SOURCE_LABEL = "CSF Function"


def slug(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", str(name)).strip("_").lower()
    return re.sub(r"_+", "_", s)


def solution_id(size: str, description: str) -> str:
    """Content-addressed, because a Solution has no natural key.

    The same description recurs under several sizes (402 distinct descriptions
    across 1,097 rows), so the size is part of the hashed key, not just the
    prefix.
    """
    digest = hashlib.sha1(f"{size}|{description}".encode("utf-8")).hexdigest()
    return f"sol_{slug(size)}_{digest[:10]}"


def write(filename: str, header: list[str], rows: list[list]) -> None:
    with (OUT / filename).open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {filename:<36} {len(rows):>5} rows")


def provenance(cats: set[str]) -> tuple[str, str]:
    """`catalogs` and `source_document` for a row, in a fixed order."""
    ordered = [c for c in ("risk", "control") if c in cats]
    return ";".join(ordered), ";".join(DOC[c] for c in ordered)


def main() -> None:
    raw = {k: json.loads((SOURCE_DIR / f"{k}-catalog.json").read_text("utf-8"))
           for k in ("risk", "control")}

    # element id -> node dict, per catalog, so rels can be resolved
    by_eid = {k: {n["id"]: n for n in v["nodes"]} for k, v in raw.items()}

    def nid(cat: str, eid: str) -> str:
        """Stable id for the node an element id points at."""
        n = by_eid[cat][eid]
        lab = n["mainLabel"]
        if lab == "Control":
            return n["control_id"]
        if lab == "Solution":
            return solution_id(n["size"], n["description"])
        if lab == "Weighting":
            return f"wt_{n['value']}"
        if lab == CSF_SOURCE_LABEL:
            return f"csf_{slug(n['name'])}"
        if lab == "Risk":
            return f"risk_{slug(n['title'])}"
        return {"Domain": "dom_", "FunctionalDomain": "fd_"}[lab] + slug(n["name"])

    # ---- provenance ----------------------------------------------------
    # Which catalog(s) each node id came from. Domains and most functional
    # domains are in both.
    cats: dict[str, set[str]] = {}
    for cat, doc in raw.items():
        for n in doc["nodes"]:
            cats.setdefault(nid(cat, n["id"]), set()).add(cat)

    # ---- edge tallies used for the *_count columns ---------------------
    edges: dict[str, set[tuple[str, str]]] = {}
    edge_cats: dict[tuple[str, str, str], set[str]] = {}
    for cat, doc in raw.items():
        for r in doc["rels"]:
            pair = (nid(cat, r["from"]), nid(cat, r["to"]))
            edges.setdefault(r["type"], set()).add(pair)
            edge_cats.setdefault((r["type"], *pair), set()).add(cat)

    fd_per_domain = Counter(s for s, _ in edges["HAS_FUNCTIONAL_DOMAIN"])
    domains_per_fd = Counter(t for _, t in edges["HAS_FUNCTIONAL_DOMAIN"])
    ctl_per_domain = Counter(s for s, _ in edges["HAS_CONTROL"])
    risk_per_fd = Counter(s for s, _ in edges["HAS_RISK"])
    sol_per_ctl = Counter(s for s, _ in edges["HAS_POSSIBLE_SOLUTION"])
    ctl_per_sol = Counter(t for _, t in edges["HAS_POSSIBLE_SOLUTION"])
    ctl_per_wt = Counter(t for _, t in edges["HAS_WEIGHTING"])
    ctl_per_csf = Counter(t for _, t in edges["MAPS_TO_FUNCTION"])

    # parent lookups, for the denormalised columns
    domain_of_fd = {t: s for s, t in edges["HAS_FUNCTIONAL_DOMAIN"]}
    fd_of_risk = {t: s for s, t in edges["HAS_RISK"]}
    domain_of_ctl = {t: s for s, t in edges["HAS_CONTROL"]}
    wt_of_ctl = {s: t for s, t in edges["HAS_WEIGHTING"]}
    csf_of_ctl = {s: t for s, t in edges["MAPS_TO_FUNCTION"]}

    names: dict[str, str] = {}   # node id -> display name, for denormalising

    def node_rows(label: str):
        """Every node with `label`, deduplicated by id across both catalogs."""
        seen: dict[str, dict] = {}
        for cat, doc in raw.items():
            for n in doc["nodes"]:
                if n["mainLabel"] != label:
                    continue
                key = nid(cat, n["id"])
                # A node present in both files: keep the richer of the two, so
                # Domain keeps `type` (only the risk catalog states it).
                if key not in seen or len(n) > len(seen[key]):
                    seen[key] = n
        return sorted(seen.items())

    # ---- Domain --------------------------------------------------------
    rows = []
    for key, n in node_rows("Domain"):
        names[key] = n["name"]
        cat, doc = provenance(cats[key])
        rows.append([key, n["name"], n.get("type", ""), fd_per_domain[key],
                     ctl_per_domain[key], cat, doc])
    write("nodes_Domain.csv",
          ["domain_id", "name", "type", "functional_domain_count",
           "control_count", "catalogs", "source_document"], rows)

    # ---- FunctionalDomain ----------------------------------------------
    rows = []
    for key, n in node_rows("FunctionalDomain"):
        names[key] = n["name"]
        cat, doc = provenance(cats[key])
        rows.append([key, n["name"], domains_per_fd[key], risk_per_fd[key],
                     cat, doc])
    write("nodes_FunctionalDomain.csv",
          ["functionaldomain_id", "name", "domain_count", "risk_count",
           "catalogs", "source_document"], rows)

    # ---- Risk ----------------------------------------------------------
    rows = []
    for key, n in node_rows("Risk"):
        names[key] = n["title"]
        fd = fd_of_risk.get(key, "")
        cat, doc = provenance(cats[key])
        rows.append([key, n["title"], n.get("description", ""),
                     names.get(fd, ""), names.get(domain_of_fd.get(fd, ""), ""),
                     cat, doc])
    write("nodes_Risk.csv",
          ["risk_id", "title", "description", "functional_domain", "domain",
           "catalogs", "source_document"], rows)

    # ---- Weighting -----------------------------------------------------
    rows = []
    for key, n in node_rows("Weighting"):
        names[key] = str(n["value"])
        cat, doc = provenance(cats[key])
        rows.append([key, n["value"], ctl_per_wt[key], cat, doc])
    write("nodes_Weighting.csv",
          ["weighting_id", "value", "control_count", "catalogs",
           "source_document"], rows)

    # ---- CSFFunction ---------------------------------------------------
    rows = []
    for key, n in node_rows(CSF_SOURCE_LABEL):
        names[key] = n["name"]
        cat, doc = provenance(cats[key])
        rows.append([key, n["name"], CSF_SOURCE_LABEL, ctl_per_csf[key],
                     cat, doc])
    write("nodes_CSFFunction.csv",
          ["csffunction_id", "name", "source_label", "control_count",
           "catalogs", "source_document"], rows)

    # ---- Control -------------------------------------------------------
    # `weighting` and `csf_function` are mirrored onto the node as well as
    # modelled as edges, so the CSV stands alone without a join. Both are blank
    # for the 109/110 controls the catalog leaves unweighted or unmapped.
    rows = []
    for key, n in node_rows("Control"):
        names[key] = n["title"]
        cat, doc = provenance(cats[key])
        rows.append([key, n["title"], n.get("description", ""),
                     names.get(domain_of_ctl.get(key, ""), ""),
                     names.get(wt_of_ctl.get(key, ""), ""),
                     names.get(csf_of_ctl.get(key, ""), ""),
                     sol_per_ctl[key], cat, doc])
    write("nodes_Control.csv",
          ["control_id", "title", "description", "domain", "weighting",
           "csf_function", "solution_count", "catalogs", "source_document"],
          rows)

    # ---- Solution ------------------------------------------------------
    rows = []
    for key, n in node_rows("Solution"):
        cat, doc = provenance(cats[key])
        rows.append([key, n["size"], n["description"], ctl_per_sol[key],
                     cat, doc])
    write("nodes_Solution.csv",
          ["solution_id", "size", "description", "control_count", "catalogs",
           "source_document"], rows)

    # ---- relationships -------------------------------------------------
    # One row per distinct (type, source, target). The only place this
    # deduplicates anything is HAS_FUNCTIONAL_DOMAIN, where 31 of the 71 stated
    # edges are the same pair written in both files.
    sizes = {solution_id(n["size"], n["description"]): n["size"]
             for n in raw["control"]["nodes"] if n["mainLabel"] == "Solution"}

    def rel_rows(rel_type: str, extra=lambda s, t: []):
        out = []
        for s, t in sorted(edges[rel_type]):
            cat, doc = provenance(edge_cats[(rel_type, s, t)])
            out.append([s, t, rel_type, *extra(s, t), cat, doc])
        return out

    for rel_type, extra_cols, extra in [
        ("HAS_FUNCTIONAL_DOMAIN", [], lambda s, t: []),
        ("HAS_RISK", [], lambda s, t: []),
        ("HAS_CONTROL", [], lambda s, t: []),
        ("HAS_POSSIBLE_SOLUTION", ["size"], lambda s, t: [sizes[t]]),
        ("HAS_WEIGHTING", ["value"], lambda s, t: [t.removeprefix("wt_")]),
        ("MAPS_TO_FUNCTION", ["function_name"], lambda s, t: [names[t]]),
    ]:
        write(f"rels_{rel_type}.csv",
              ["source_id", "target_id", "rel_type", *extra_cols,
               "catalogs", "source_document"],
              rel_rows(rel_type, extra))

    # ---- checks --------------------------------------------------------
    # Node ids must be unique across every label, because the loader merges on
    # (framework_id, node_id) under one anchor label and the rels files record
    # no endpoint label.
    all_ids = [r[0] for f in OUT.glob("nodes_*.csv")
               for r in list(csv.reader(f.open(encoding="utf-8")))[1:]]
    assert len(all_ids) == len(set(all_ids)), "duplicate node id across labels"

    known = set(all_ids)
    for f in OUT.glob("rels_*.csv"):
        for r in list(csv.reader(f.open(encoding="utf-8")))[1:]:
            assert r[0] in known and r[1] in known, f"dangling endpoint in {f.name}"

    stated = sum(len(d["rels"]) for d in raw.values())
    built = sum(len(edges[t]) for t in edges)
    print(f"\n  {len(all_ids)} nodes, {built} relationships "
          f"({stated} stated, {stated - built} duplicate pairs merged)")


if __name__ == "__main__":
    print("reading risk-catalog.json, control-catalog.json")
    main()
