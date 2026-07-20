"""Push ONLY the verified frameworks into Neo4j.

Connection details come from the .env file (see .env.example) via app.py.
Each framework has its own loader script that MERGEs its nodes/relationships
into the graph; this runner executes only the ones marked ✅ Verified in
verdict.md (after the 2026-07-20 remediation pass).

Usage:
    python push_verified.py                # push all verified frameworks
    python push_verified.py cis dora sec   # push a subset by key
    python push_verified.py --list         # list verified frameworks and exit

Note: the per-framework scripts LOAD CSV from the GitHub `main` branch raw
URLs, so the remediated CSVs must be committed and pushed to GitHub before the
fixes are reflected in the database.
"""

import sys
import time
import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("push_verified")

BASE_DIR = Path(__file__).resolve().parent

# key -> (display name, loader script). Order groups IS-frameworks, industry
# standards, then regional regulations. Only ✅ Verified frameworks are listed.
VERIFIED = [
    ("cis",      "CIS Controls",  "cis_controls.py"),
    ("iso27002", "ISO 27002",     "iso27002.py"),
    ("nistcsf",  "NIST CSF 2.0",  "nist_csf.py"),
    ("glba",     "GLBA",          "glba.py"),
    ("pcidss",   "PCI DSS",       "pcidss.py"),
    ("sec",      "SEC Cyber Rule","sec.py"),
    ("gdpr",     "GDPR",          "gdpr.py"),
    ("cpra",     "CPRA",          "cpra.py"),
    ("tdpsa",    "TDPSA",         "tdpsa.py"),
    ("dora",     "DORA",          "dora.py"),
]

SLEEP_BETWEEN = 2


def run_script(name, script, sleep=SLEEP_BETWEEN):
    full_path = BASE_DIR / script
    if not full_path.exists():
        logger.error("SKIP %s — script not found: %s", name, full_path)
        return False

    logger.info("Loading %s (%s) ...", name, script)
    try:
        subprocess.run([sys.executable, str(full_path)], check=True, cwd=str(BASE_DIR))
        logger.info("✓ Loaded %s", name)
        return True
    except subprocess.CalledProcessError:
        logger.error("✗ Failed %s (%s)", name, script, exc_info=True)
        return False
    finally:
        time.sleep(sleep)


def preflight():
    """Verify the Neo4j connection (from .env) before running any loader."""
    try:
        from app import Neo4jConnect
    except Exception:
        logger.exception("Could not import Neo4jConnect from app.py")
        return False

    client = Neo4jConnect()
    try:
        health = client.check_health()
        if health is not True:
            logger.error("Neo4j connection failed: %s", health)
            return False
        logger.info("Neo4j connection OK (database=%s)", client.database or "<default>")
        return True
    finally:
        client.close()


def main(argv):
    args = [a for a in argv if not a.startswith("-")]
    if "--list" in argv:
        print("Verified frameworks:")
        for key, disp, script in VERIFIED:
            print(f"  {key:9s}  {disp:15s}  {script}")
        return 0

    selected = VERIFIED
    if args:
        wanted = {a.lower() for a in args}
        selected = [row for row in VERIFIED if row[0] in wanted]
        unknown = wanted - {row[0] for row in VERIFIED}
        if unknown:
            logger.warning("Ignoring unknown keys: %s", ", ".join(sorted(unknown)))
        if not selected:
            logger.error("Nothing to run. Use --list to see valid keys.")
            return 1

    if not preflight():
        logger.error("Aborting — fix the Neo4j connection in .env and retry.")
        return 1

    logger.info("Pushing %d verified framework(s) into Neo4j ...", len(selected))
    results = {}
    for key, disp, script in selected:
        results[disp] = run_script(disp, script)

    ok = [n for n, r in results.items() if r]
    bad = [n for n, r in results.items() if not r]
    logger.info("Done. %d succeeded, %d failed.", len(ok), len(bad))
    if ok:
        logger.info("  Succeeded: %s", ", ".join(ok))
    if bad:
        logger.error("  Failed:    %s", ", ".join(bad))
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
