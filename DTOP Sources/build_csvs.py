"""Build the DTOP Sources node and relationship CSVs from `dtopSources.json`.

Reads the DTO source catalogue out of the DTOP-OLD client assets and writes the
same `nodes_<Label>.csv` / `rels_<TYPE>.csv` shape used by the framework folders
in this repository: first column of a nodes file is `<label>_id`, and every rels
file is `source_id,target_id,rel_type` plus any edge properties.

    python "DTOP Sources/build_csvs.py"

Everything written is present in the JSON. The one derived column is
`possibly_same_as` on InputSource, which flags a name that looks like it refers
to a DTOSource without matching one exactly; it is a hint for a human, never a
relationship, and `possibly_same_as_basis` records what the hint rests on.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

SOURCE_JSON = Path(
    "/Users/gauthamsmacbook/Apps/Santan/DTOP-OLD/client/src/assets/docs"
    "/knowledgeRepository/info/dtopSources.json"
)
#: Recorded on every row, matching how the framework folders cite their source.
SOURCE_DOCUMENT = (
    "DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/dtopSources.json"
)
OUT = Path(__file__).resolve().parent


def slug(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return re.sub(r"_+", "_", s)


def write(filename: str, header: list[str], rows: list[list]) -> None:
    with (OUT / filename).open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {filename:<34} {len(rows):>3} rows")


def main() -> None:
    entries = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))["DTOSources"]
    names = [e["SourceName"] for e in entries]
    by_name = {n: f"dto_{slug(n)}" for n in names}

    # ---- DTOSource -----------------------------------------------------
    dto_rows = [
        [by_name[e["SourceName"]], e["SourceName"],
         "" if e["URL"] is None else e["URL"],
         e["Description"], e["ReputationScore"], e["ProfileType"],
         len(e["Sources"]), SOURCE_DOCUMENT]
        for e in entries
    ]
    write("nodes_DTOSource.csv",
          ["dtosource_id", "source_name", "url", "description",
           "reputation_score", "profile_type", "stated_source_count",
           "source_document"], dto_rows)

    # ---- ProfileType ---------------------------------------------------
    profiles = sorted({e["ProfileType"] for e in entries})
    write("nodes_ProfileType.csv",
          ["profiletype_id", "name", "dtosource_count", "source_document"],
          [[f"pt_{slug(p)}", p,
            sum(1 for e in entries if e["ProfileType"] == p), SOURCE_DOCUMENT]
           for p in profiles])

    # ---- InputSource ---------------------------------------------------
    # Every distinct Sources entry that is NOT itself one of the DTOSources.
    referenced: dict[str, int] = {}
    for e in entries:
        for s in e["Sources"]:
            referenced[s] = referenced.get(s, 0) + 1
    externals = [s for s in sorted(referenced) if s not in by_name]

    def hint(name: str) -> tuple[str, str]:
        """A near-match to a DTOSource name, and what the hint rests on.

        Deliberately narrow. Only two things count as evidence:

        1. one name contains the other verbatim ("Hi-Def Operating Model
           Heatmap" vs "Hi-Def Operating Model");
        2. a DTOSource description *opens by defining itself as* this thing
           ("An Operational Risk Heatmap that provides…" for Risky Business
           Process).

        A mere mention inside a description is not evidence — every
        description mentions its inputs, so that would flag all of them.
        """
        for n in names:
            if n != name and (n in name or name in n):
                return n, "one name contains the other"
        for e in entries:
            for article in ("A ", "An "):
                if e["Description"].startswith(f"{article}{name} "):
                    return e["SourceName"], (
                        f"the {e['SourceName']} description opens "
                        f'"{article}{name} …"')
        return "", ""

    ext_rows = []
    for s in externals:
        same, basis = hint(s)
        ext_rows.append([f"in_{slug(s)}", s, referenced[s], same, basis,
                         SOURCE_DOCUMENT])
    write("nodes_InputSource.csv",
          ["inputsource_id", "name", "referenced_by_count", "possibly_same_as",
           "possibly_same_as_basis", "source_document"], ext_rows)

    # ---- DERIVED_FROM --------------------------------------------------
    # One row per Sources entry, in the order the JSON lists them. The target
    # is a DTOSource where the name matches one exactly, an InputSource
    # otherwise; target_kind says which.
    df_rows = []
    for e in entries:
        for i, s in enumerate(e["Sources"], 1):
            target = by_name.get(s) or f"in_{slug(s)}"
            df_rows.append([by_name[e["SourceName"]], target, "DERIVED_FROM",
                            "DTOSource" if s in by_name else "InputSource",
                            i, s, SOURCE_DOCUMENT])
    write("rels_DERIVED_FROM.csv",
          ["source_id", "target_id", "rel_type", "target_kind", "ordinal",
           "stated_source_name", "source_document"], df_rows)

    # ---- HAS_PROFILE_TYPE ----------------------------------------------
    write("rels_HAS_PROFILE_TYPE.csv",
          ["source_id", "target_id", "rel_type", "source_document"],
          [[by_name[e["SourceName"]], f"pt_{slug(e['ProfileType'])}",
            "HAS_PROFILE_TYPE", SOURCE_DOCUMENT] for e in entries])


if __name__ == "__main__":
    print(f"reading {SOURCE_JSON.name}")
    main()
