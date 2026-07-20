query = """CREATE CONSTRAINT framework_id_unique FOR (f:Framework) REQUIRE f.framework_id IS UNIQUE;
CREATE CONSTRAINT clause_framework_composite_unique FOR (c:Clause) REQUIRE (c.framework_id, c.clause_id) IS UNIQUE;
CREATE CONSTRAINT control_framework_composite_unique FOR (ctrl:Control) REQUIRE (ctrl.framework_id, ctrl.control_id) IS UNIQUE;
CREATE CONSTRAINT requirement_framework_composite_unique FOR (r:Requirement) REQUIRE (r.framework_id, r.requirement_id) IS UNIQUE;
CREATE CONSTRAINT control_category_framework_composite_unique FOR (cc:ControlCategory) REQUIRE (cc.framework_id, cc.category_id) IS UNIQUE;
CREATE CONSTRAINT category_framework_composite_unique FOR (c:Category) REQUIRE (c.framework_id, c.category_id) IS UNIQUE;
CREATE CONSTRAINT attribute_framework_composite_unique FOR (a:Attribute) REQUIRE (a.framework_id, a.attribute_id) IS UNIQUE;
CREATE CONSTRAINT guideline_framework_composite_unique FOR (g:Guideline) REQUIRE (g.framework_id, g.guideline_id) IS UNIQUE;
CREATE CONSTRAINT function_framework_composite_unique IF NOT EXISTS FOR (fn:Function) REQUIRE (fn.framework_id, fn.function_id) IS UNIQUE;
CREATE CONSTRAINT subcategory_framework_composite_unique IF NOT EXISTS FOR (s:Subcategory) REQUIRE (s.framework_id, s.subcategory_id) IS UNIQUE;
CREATE CONSTRAINT step_framework_composite_unique IF NOT EXISTS FOR (s:Step) REQUIRE (s.framework_id, s.step_id) IS UNIQUE;
CREATE CONSTRAINT family_framework_composite_unique IF NOT EXISTS FOR (cf:ControlFamily) REQUIRE (cf.framework_id, cf.family_id) IS UNIQUE;
CREATE CONSTRAINT role_framework_composite_unique IF NOT EXISTS FOR (r:Role) REQUIRE (r.framework_id, r.role_id) IS UNIQUE;
CREATE CONSTRAINT system_framework_composite_unique IF NOT EXISTS FOR (sys:System) REQUIRE (sys.framework_id, sys.system_id) IS UNIQUE;"""


import os
import logging
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Neo4j connection success")

logger.info("Creating constraints")
for constraint in query.split('\n'):
    client.query(constraint)

client.close()
