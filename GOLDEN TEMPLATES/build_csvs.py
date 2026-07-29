"""Build the GOLDEN TEMPLATES node and relationship CSVs from `templateSources.json`.

Reads the DTOM golden policy-template catalogue out of the DTOP-OLD client
assets and writes the same `nodes_<Label>.csv` / `rels_<TYPE>.csv` shape used by
the framework folders in this repository: the first column of a nodes file is
`<label>_id`, and every rels file is `source_id,target_id,rel_type` plus any
edge properties.

    python "GOLDEN TEMPLATES/build_csvs.py"

The JSON is a flat list of 31 templates, each with a `Sources` array of citation
strings. Two things are parsed out of those strings rather than stored whole:

1.  491 of the 509 distinct entries are structured citations —
    `<Title>, accessed <Date>, <<URL>>` — and become `Source` nodes keyed on
    (title, URL). The accessed date is *not* part of the key, because five
    sources were accessed on two different dates by different templates; it
    goes on the `CITES` edge instead.
2.  The other 18 have no URL and become `InternalDocument` nodes. Seventeen are
    DTOM `.docx` files. The eighteenth is the literal string `</div>`, an HTML
    fragment that is clearly a scraping artifact — it is kept rather than
    dropped, flagged `is_malformed`, so the JSON's own `SourceCount` still
    reconciles against the edge count. See the folder README.

Every node keeps the verbatim original string, and every `CITES` edge keeps its
position in the array, so the `Sources` arrays rebuild from the CSVs exactly.

The one column that is a judgement rather than a fact is `possibly_maps_to` on
`DomainCode`, which flags a DTOP Catalogs domain the code may refer to. It is a
hint for a human, never a relationship, and `possibly_maps_to_basis` records
what the hint rests on.
"""

from __future__ import annotations

import csv
import datetime as _dt
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

SOURCE_JSON = Path(
    "/Users/gauthamsmacbook/Apps/Santan/DTOP-OLD/client/src/assets/docs"
    "/knowledgeRepository/info/templateSources.json"
)
#: Recorded on every row, matching how the framework folders cite their source.
SOURCE_DOCUMENT = (
    "DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/templateSources.json"
)
OUT = Path(__file__).resolve().parent
#: Read to compute the `possibly_maps_to` hint. Local to this repository, so the
#: build stays reproducible without reaching into DTOP-OLD for it.
DTOP_DOMAINS_CSV = OUT.parent / "DTOP Catalogs" / "nodes_Domain.csv"

#: `<Title>, accessed <Date>, <<URL>>`. The catalogue writes both "accessed" and
#: "accessed on"; both forms are accepted and the verbatim string is kept anyway.
CITATION = re.compile(
    r"^(?P<title>.*?),\s*accessed(?:\s+on)?\s+"
    r"(?P<date>[A-Za-z]+ \d{1,2}, \d{4}),\s*<(?P<url>[^>]*)>\s*$"
)

#: `DTOM-L2A-DPP-POL-006` -> level, domain code, artifact type, sequence.
TEMPLATE_ID = re.compile(
    r"^DTOM-(?P<level>L[0-9][A-Z]?)-(?P<domain>[A-Z]{3})-"
    r"(?P<artifact>[A-Z]{3})-(?P<seq>\d+)$"
)

#: Skipped when reducing a domain name to its initials.
STOPWORDS = {"and", "or", "of", "the", "for", "a", "an", "&"}


def slug(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", str(name)).strip("_").lower()
    return re.sub(r"_+", "_", s)


def digest(*parts: str) -> str:
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:12]


def iso_date(stated: str) -> str:
    """'March 9, 2026' -> '2026-03-09'. The verbatim form is kept alongside."""
    return _dt.datetime.strptime(stated, "%B %d, %Y").date().isoformat()


def initials(name: str) -> str:
    """First letters of the first three significant words of a domain name.

    'Third-Party Risk Management' -> TPR, 'Cloud & Platform Security' -> CPS.
    Hyphens split, so 'Third-Party' contributes two words.
    """
    words = [w for w in re.split(r"[^A-Za-z]+", name) if w and w.lower() not in STOPWORDS]
    return "".join(w[0] for w in words[:3]).upper()


def write(filename: str, header: list[str], rows: list[list]) -> None:
    with (OUT / filename).open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {filename:<38} {len(rows):>4} rows")


def domain_hint() -> dict[str, tuple[str, str]]:
    """Code -> (DTOP Catalogs domain, basis), for codes that clear the bar.

    Deliberately narrow, in the same spirit as `possibly_same_as` in
    `DTOP Sources/build_csvs.py`. Exactly one thing counts as evidence: the
    three-letter code is the initials of the first three significant words of a
    DTOP Catalogs domain name. A code that merely looks topically related is
    left blank — see the folder README for the one case that falls out this way.
    """
    if not DTOP_DOMAINS_CSV.exists():
        print(f"  note: {DTOP_DOMAINS_CSV.name} not found; hints left blank")
        return {}
    names = [r["name"] for r in
             csv.DictReader(DTOP_DOMAINS_CSV.open(encoding="utf-8"))]
    by_initials: dict[str, list[str]] = defaultdict(list)
    for n in names:
        by_initials[initials(n)].append(n)
    return {
        code: (matches[0],
               f"the code is the initials of the first three significant words "
               f"of the DTOP Catalogs domain “{matches[0]}”")
        for code, matches in by_initials.items() if len(matches) == 1
    }


def main() -> None:
    entries = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))["TemplateSources"]

    # ---- parse every Sources entry once --------------------------------
    # cited[template_id] = [(ordinal, target_id, kind, stated_text, iso, stated_date)]
    cited: dict[str, list[tuple]] = {}
    sources: dict[str, dict] = {}   # source_id -> title/url/verbatim
    internal: dict[str, dict] = {}  # internaldocument_id -> text
    src_dates: dict[str, set[str]] = defaultdict(set)
    src_templates: Counter = Counter()
    doc_templates: Counter = Counter()

    for e in entries:
        rows = []
        for i, raw in enumerate(e["Sources"], 1):
            m = CITATION.match(raw)
            if m:
                title, url = m.group("title"), m.group("url")
                sid = f"src_{digest(title, url)}"
                sources.setdefault(sid, {
                    "title": title, "url": url,
                    "host": urlparse(url).netloc, "verbatim": raw})
                stated = m.group("date")
                src_dates[sid].add(iso_date(stated))
                src_templates[sid] += 1
                rows.append((i, sid, "Source", raw, iso_date(stated), stated))
            else:
                did = f"doc_{slug(raw)}"
                internal.setdefault(did, {"text": raw})
                doc_templates[did] += 1
                rows.append((i, did, "InternalDocument", raw, "", ""))
        cited[e["TemplateId"]] = rows

    # ---- Template ------------------------------------------------------
    # `TemplatePath` is stored verbatim, never derived: nine templates sit in a
    # DTOM-L2A-ENT-DTOM directory that does not match their own id prefix.
    parts = {}
    t_rows = []
    for e in entries:
        m = TEMPLATE_ID.match(e["TemplateId"])
        if not m:
            raise ValueError(f"unparseable TemplateId: {e['TemplateId']}")
        parts[e["TemplateId"]] = m
        rows = cited[e["TemplateId"]]
        t_rows.append([
            e["TemplateId"], e["TemplateName"], m.group("level"),
            m.group("domain"), m.group("artifact"), int(m.group("seq")),
            e["TemplatePath"], e["SourceCount"],
            sum(1 for r in rows if r[2] == "Source"),
            sum(1 for r in rows if r[2] == "InternalDocument"),
            SOURCE_DOCUMENT])
    write("nodes_Template.csv",
          ["template_id", "name", "level", "domain_code", "artifact_type",
           "sequence", "template_path", "stated_source_count",
           "cited_source_count", "cited_internal_document_count",
           "source_document"], t_rows)

    # ---- Source --------------------------------------------------------
    # first_accessed / last_accessed differ for the five sources two templates
    # accessed on different days; they are equal for the other 480.
    write("nodes_Source.csv",
          ["source_id", "title", "url", "host", "verbatim", "template_count",
           "first_accessed", "last_accessed", "source_document"],
          [[sid, s["title"], s["url"], s["host"], s["verbatim"],
            src_templates[sid], min(src_dates[sid]), max(src_dates[sid]),
            SOURCE_DOCUMENT]
           for sid, s in sorted(sources.items())])

    # ---- InternalDocument ----------------------------------------------
    # Seventeen DTOM .docx files, plus one HTML fragment kept and flagged.
    MALFORMED_NOTE = ("HTML fragment, not a citation; it is the last entry in "
                      "each of the 4 Sources arrays that contain it")
    write("nodes_InternalDocument.csv",
          ["internaldocument_id", "text", "is_malformed", "note",
           "template_count", "source_document"],
          [[did, d["text"],
            "true" if d["text"].startswith("<") else "false",
            MALFORMED_NOTE if d["text"].startswith("<") else "",
            doc_templates[did], SOURCE_DOCUMENT]
           for did, d in sorted(internal.items())])

    # ---- Level / DomainCode / ArtifactType -----------------------------
    # No expanded names are invented for these codes: the JSON never states
    # what POL, PRG, DTM or DTS stand for, so only the code is recorded.
    hints = domain_hint()
    for label, group, extra_cols, extra in [
        ("Level", "level", [], lambda c: []),
        ("DomainCode", "domain",
         ["possibly_maps_to", "possibly_maps_to_basis"],
         lambda c: list(hints.get(c, ("", "")))),
        ("ArtifactType", "artifact", [], lambda c: []),
    ]:
        counts = Counter(m.group(group) for m in parts.values())
        write(f"nodes_{label}.csv",
              [f"{label.lower()}_id", "code", "template_count", *extra_cols,
               "source_document"],
              [[f"{slug(label)}_{slug(code)}", code, n, *extra(code),
                SOURCE_DOCUMENT]
               for code, n in sorted(counts.items())])

    # ---- CITES ---------------------------------------------------------
    # One row per Sources entry, in the order the JSON lists them. `ordinal` and
    # `stated_source_text` together let the original arrays be rebuilt verbatim.
    write("rels_CITES.csv",
          ["source_id", "target_id", "rel_type", "target_kind", "ordinal",
           "accessed_date", "accessed_date_stated", "stated_source_text",
           "source_document"],
          [[tid, target, "CITES", kind, i, iso, stated, text, SOURCE_DOCUMENT]
           for tid, rows in cited.items()
           for i, target, kind, text, iso, stated in rows])

    # ---- taxonomy edges ------------------------------------------------
    for rel, label, group in [("HAS_LEVEL", "Level", "level"),
                              ("IN_DOMAIN", "DomainCode", "domain"),
                              ("HAS_ARTIFACT_TYPE", "ArtifactType", "artifact")]:
        write(f"rels_{rel}.csv",
              ["source_id", "target_id", "rel_type", "source_document"],
              [[tid, f"{slug(label)}_{slug(m.group(group))}", rel,
                SOURCE_DOCUMENT] for tid, m in parts.items()])

    # ---- checks --------------------------------------------------------
    all_ids = [r[0] for f in sorted(OUT.glob("nodes_*.csv"))
               for r in list(csv.reader(f.open(encoding="utf-8")))[1:]]
    assert len(all_ids) == len(set(all_ids)), "duplicate node id across labels"

    known = set(all_ids)
    rel_rows = 0
    for f in sorted(OUT.glob("rels_*.csv")):
        for r in list(csv.reader(f.open(encoding="utf-8")))[1:]:
            rel_rows += 1
            assert r[0] in known and r[1] in known, f"dangling endpoint in {f.name}"

    # SourceCount must equal the CITES edges built for that template.
    for e in entries:
        assert e["SourceCount"] == len(cited[e["TemplateId"]]), \
            f"SourceCount mismatch for {e['TemplateId']}"

    print(f"\n  {len(all_ids)} nodes, {rel_rows} relationships "
          f"({sum(e['SourceCount'] for e in entries)} stated citations, all kept)")


if __name__ == "__main__":
    print(f"reading {SOURCE_JSON.name}")
    main()
