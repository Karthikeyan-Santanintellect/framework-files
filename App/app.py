import os
import time
import logging
from neo4j import GraphDatabase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'neo4j+ssc://b5e7a476.databases.neo4j.io'
USER = 'neo4j'
PASSWORD = "z8JxqCCl8pOYuhCtPNA8-ds3TpBwnZQ8Olqj3P-bjBU"


class Neo4jConnect:
    def __init__(self):
        self.driver = GraphDatabase.driver(URL, auth=(USER, PASSWORD), notifications_disabled_categories=['UNRECOGNIZED'])

    def close(self):
        self.driver.close()

    def check_health(self):
        with self.driver.session() as session:
            try:
                session.run("RETURN 1")
                return True
            except Exception as e:
                return str(e)

    def query(self, query, parameters=None, others=None):
        try:
            with self.driver.session() as session:
                if others:
                    result = session.run(query, **others)
                else:
                    result = session.run(query)
                return [record.data() for record in result]
        except Exception as e:
            return str(e)