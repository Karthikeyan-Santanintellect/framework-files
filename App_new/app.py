import os
import time
import logging
from pathlib import Path
from neo4j import GraphDatabase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _load_dotenv():
    """Load environment variables from a .env file without requiring python-dotenv.

    Looks for a .env next to this file (App/.env) first, then in the project
    root (framework-files/.env). Existing os.environ values are NOT overridden.
    """
    here = Path(__file__).resolve().parent
    candidates = [here / ".env", here.parent / ".env"]

    # Prefer python-dotenv if it happens to be installed (handles quoting/escapes).
    try:
        from dotenv import load_dotenv as _ld
        for path in candidates:
            if path.exists():
                _ld(path)
        return
    except Exception:
        pass

    for path in candidates:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


_load_dotenv()

# Connection details are read from the environment (.env). The literals below are
# only fallbacks so existing runs keep working if the .env is missing a value.
URL = os.getenv("NEO4J_URI") or "neo4j+ssc://20ec6dbd.databases.neo4j.io"
USER = os.getenv("NEO4J_USERNAME") or "neo4j"
PASSWORD = os.getenv("NEO4J_PASSWORD") or "N3uwyddew5teuQ8ybSQSYOfNamD0LItwavzsJ2gmg34"
DATABASE = os.getenv("NEO4J_DATABASE") or None  # None -> server default (usually "neo4j")


class Neo4jConnect:
    def __init__(self):
        self.database = DATABASE
        self.driver = GraphDatabase.driver(
            URL,
            auth=(USER, PASSWORD),
            notifications_disabled_categories=['UNRECOGNIZED'],
        )

    def _session(self):
        if self.database:
            return self.driver.session(database=self.database)
        return self.driver.session()

    def close(self):
        self.driver.close()

    def check_health(self):
        with self._session() as session:
            try:
                session.run("RETURN 1")
                return True
            except Exception as e:
                return str(e)

    def query(self, query, parameters=None, others=None):
        try:
            with self._session() as session:
                if others:
                    result = session.run(query, **others)
                else:
                    result = session.run(query)
                return [record.data() for record in result]
        except Exception as e:
            print(f"Error executing query: {e}")
            return str(e)
