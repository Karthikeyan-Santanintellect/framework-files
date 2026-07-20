#Create regulations from JSON file
regulations = """
CALL apoc.load.json('$file_path') YIELD value UNWIND value AS row 
CREATE (r:`Regulation Catalog` {name : row.full_name,
short_name :row.short_name,
publisher : row.publisher,
version_number : row.version_number,
publication_date : row.publication_date,
status : row.status,
description : row.description,
coverage : row.coverage,
applicable_areas :  row.applicable_areas})
RETURN r;
"""

import os
import time
import logging
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()
health = client.check_health()

if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Loading regulations...")

client.query(regulations.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/REGULATIONS/Regulations.json"))
time.sleep(2)

logger.info("Graph structure loaded successfully.")

client.close()