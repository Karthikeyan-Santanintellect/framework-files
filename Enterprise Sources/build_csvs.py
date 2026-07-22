"""Build the Enterprise Sources node and relationship CSVs from
`enterpriseSources.json`.

Reads the enterprise source catalogue out of the DTOP-OLD client assets and
writes the same `nodes_<Label>.csv` / `rels_<TYPE>.csv` shape used by the
framework folders in this repository: first column of a nodes file is
`<label>_id`, and every rels file is `source_id,target_id,rel_type` plus any
edge properties.

    python "Enterprise Sources/build_csvs.py"

Two things in the source data need care, both handled here rather than papered
over:

* `SourceName` is **not** unique. "Reputable Breach Databases" appears twice
  with a different URL, description and ProfileType, so the two are genuinely
  different entries. Ids get a numeric suffix on collision, in file order.
* Nine URLs are shared by two or three entries each. Those become a single
  `WebResource` node so the sharing is visible; the URL also stays as a
  property on the source, so nothing needs a join to read it.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

SOURCE_JSON = Path(
    "/Users/gauthamsmacbook/Apps/Santan/DTOP-OLD/client/src/assets/docs"
    "/knowledgeRepository/info/enterpriseSources.json"
)
#: Recorded on every row, matching how the framework folders cite their source.
SOURCE_DOCUMENT = (
    "DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json"
)
OUT = Path(__file__).resolve().parent


def slug(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return re.sub(r"_+", "_", s)


def url_slug(url: str) -> str:
    """Readable id for a URL: host plus the first path segment, deduplicated."""
    stripped = re.sub(r"^https?://", "", url).rstrip("/")
    return slug(stripped)[:80]


def write(filename: str, header: list[str], rows: list[list]) -> None:
    with (OUT / filename).open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {filename:<36} {len(rows):>3} rows")


def main() -> None:
    entries = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))["EnterpriseSources"]

    # ---- ids, with a suffix wherever a SourceName repeats ---------------
    ids: list[str] = []
    seen: dict[str, int] = {}
    for e in entries:
        base = f"es_{slug(e['SourceName'])}"
        seen[base] = seen.get(base, 0) + 1
        ids.append(base if seen[base] == 1 else f"{base}_{seen[base]}")

    # ---- WebResource ----------------------------------------------------
    # One node per distinct non-null URL. Built before the source rows so each
    # source can carry the resource id it points at.
    urls: dict[str, int] = {}
    for e in entries:
        if e["URL"]:
            urls[e["URL"]] = urls.get(e["URL"], 0) + 1
    res_id: dict[str, str] = {}
    used: dict[str, int] = {}
    for url in urls:
        base = f"web_{url_slug(url)}"
        used[base] = used.get(base, 0) + 1
        res_id[url] = base if used[base] == 1 else f"{base}_{used[base]}"

    write("nodes_WebResource.csv",
          ["webresource_id", "url", "referenced_by_count", "source_document"],
          [[res_id[u], u, n, SOURCE_DOCUMENT] for u, n in urls.items()])

    # ---- EnterpriseSource ----------------------------------------------
    write("nodes_EnterpriseSource.csv",
          ["enterprisesource_id", "source_name", "url", "description",
           "reputation_score", "profile_type", "name_is_duplicated",
           "source_document"],
          [[i, e["SourceName"], "" if e["URL"] is None else e["URL"],
            e["Description"], e["ReputationScore"], e["ProfileType"],
            "true" if sum(1 for x in entries
                          if x["SourceName"] == e["SourceName"]) > 1 else "false",
            SOURCE_DOCUMENT]
           for i, e in zip(ids, entries)])

    # ---- ProfileType ----------------------------------------------------
    profiles = sorted({e["ProfileType"] for e in entries})
    write("nodes_ProfileType.csv",
          ["profiletype_id", "name", "enterprisesource_count", "source_document"],
          [[f"pt_{slug(p)}", p,
            sum(1 for e in entries if e["ProfileType"] == p), SOURCE_DOCUMENT]
           for p in profiles])

    # ---- HAS_PROFILE_TYPE ----------------------------------------------
    write("rels_HAS_PROFILE_TYPE.csv",
          ["source_id", "target_id", "rel_type", "source_document"],
          [[i, f"pt_{slug(e['ProfileType'])}", "HAS_PROFILE_TYPE", SOURCE_DOCUMENT]
           for i, e in zip(ids, entries)])

    # ---- AVAILABLE_AT ---------------------------------------------------
    # Only the 67 entries that carry a URL; the other 47 get no edge.
    write("rels_AVAILABLE_AT.csv",
          ["source_id", "target_id", "rel_type", "url", "shared_with_others",
           "source_document"],
          [[i, res_id[e["URL"]], "AVAILABLE_AT", e["URL"],
            "true" if urls[e["URL"]] > 1 else "false", SOURCE_DOCUMENT]
           for i, e in zip(ids, entries) if e["URL"]])


if __name__ == "__main__":
    print(f"reading {SOURCE_JSON.name}")
    main()
