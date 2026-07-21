#!/usr/bin/env python3
"""Generate index.html for the graph explorer.

Reads the Neo4j credentials from .env and injects them into
viz/index.template.html, writing the result to index.html in the repo root.

    python make_viz.py            # writes ./index.html
    python make_viz.py --open     # writes it and opens it in the browser

THE GENERATED index.html CONTAINS A LIVE NEO4J PASSWORD IN PLAINTEXT.
It is listed in .gitignore and must never be committed: this repository is
public, and the CSV loaders fetch from its raw URLs without authentication.
Commit the template (viz/index.template.html), not the output.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "viz" / "index.template.html"
OUTPUT = ROOT / "index.html"
ENV = ROOT / ".env"
VENDOR = [ROOT / "viz" / "vendor" / "d3.v7.min.js",
          ROOT / "viz" / "vendor" / "neo4j-driver-lite.js"]


def read_env(path: Path) -> dict[str, str]:
    if not path.exists():
        sys.exit(f"error: {path} not found — copy .env.example and fill in the Neo4j credentials.")
    env: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def to_browser_uri(uri: str) -> str:
    """The browser driver speaks Bolt over WebSocket; neo4j+s / bolt+s are fine as-is.

    Only the unencrypted neo4j:// scheme needs flagging, since a page served over
    https cannot open a plaintext ws:// connection.
    """
    if uri.startswith(("neo4j+s://", "neo4j+ssc://", "bolt+s://", "bolt+ssc://")):
        return uri
    if uri.startswith(("neo4j://", "bolt://")):
        print(f"warning: {uri} is unencrypted; this works only when the page is opened over http/file.")
        return uri
    sys.exit(f"error: unrecognised NEO4J_URI scheme: {uri!r}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--open", action="store_true", help="open the generated page in the default browser")
    args = ap.parse_args()

    if not TEMPLATE.exists():
        sys.exit(f"error: template missing: {TEMPLATE}")
    missing = [p.name for p in VENDOR if not p.exists()]
    if missing:
        sys.exit(f"error: vendored library missing from viz/vendor/: {', '.join(missing)}")

    env = read_env(ENV)
    uri = env.get("NEO4J_URI")
    user = env.get("NEO4J_USERNAME")
    password = env.get("NEO4J_PASSWORD")
    database = env.get("NEO4J_DATABASE", "")
    if not (uri and user and password):
        sys.exit("error: .env must define NEO4J_URI, NEO4J_USERNAME and NEO4J_PASSWORD.")

    generated = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    page = TEMPLATE.read_text(encoding="utf-8")
    for token, value in {
        "__NEO4J_URI__": to_browser_uri(uri),
        "__NEO4J_USER__": user,
        "__NEO4J_PASSWORD__": password,
        "__NEO4J_DATABASE__": database,
        "__DB_LABEL__": html.escape(database or "server default"),
        "__GENERATED_AT__": generated,
    }.items():
        if token not in page:
            sys.exit(f"error: template is missing the {token} placeholder.")
        # JS string literals: escape backslashes and quotes so an odd password cannot break out.
        safe = value.replace("\\", "\\\\").replace('"', '\\"') if token.startswith("__NEO4J") else value
        page = page.replace(token, safe)

    OUTPUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}  ({OUTPUT.stat().st_size / 1024:.0f} KB)")
    print(f"  database : {database or 'server default'} @ {uri}")
    print(f"  open with: open {OUTPUT.name}     (contains a plaintext password — gitignored, never commit)")

    if args.open:
        webbrowser.open(OUTPUT.as_uri())


if __name__ == "__main__":
    main()
