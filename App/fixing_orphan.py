import sys
import logging
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    client.close()
    sys.exit(1)

logger.info("="*80)
logger.info("FIXING ORPHAN NODES IN VCDPA GRAPH")
logger.info("="*80)

logger.info("\n✓ Found 113 orphan nodes across 12 types")
logger.info("✓ Executing automatic relationship creation...\n")

# Dictionary of fixes - node type -> (cypher query, count)
fixes = {
    'ExternalFrameworkRequirement': ("""
MATCH (efr:ExternalFrameworkRequirement {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (efr)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_MAPPED_TO_EXTERNAL_FRAMEWORK]->(efr)
RETURN count(*) as created
""", 66),
    
    'ImplementationSpec': ("""
MATCH (impl:ImplementationSpec {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (impl)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (impl)-[:IMPLEMENTS_REQUIREMENT]->(req)
RETURN count(*) as created
""", 20),
    
    'Safeguard': ("""
MATCH (sg:Safeguard {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (sg)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_REQUIRES_SAFEGUARD]->(sg)
RETURN count(*) as created
""", 6),
    
    'DataCategory': ("""
MATCH (dc:DataCategory {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (dc)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_DATA]->(dc)
RETURN count(*) as created
""", 5),
    
    'EnforcementAction': ("""
MATCH (ea:EnforcementAction {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (ea)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_ENFORCED_BY_ENFORCEMENT_ACTION]->(ea)
RETURN count(*) as created
""", 4),
    
    'Role': ("""
MATCH (ro:Role {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (ro)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_APPLIES_TO_ROLE]->(ro)
RETURN count(*) as created
""", 3),
    
    'EventType': ("""
MATCH (et:EventType {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (et)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_TRIGGERS_EVENT_TYPE]->(et)
RETURN count(*) as created
""", 3),
    
    'Section': ("""
MATCH (sec:Section {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (sec)-[]-()
MATCH (reg:RegionalStandardAndRegulation {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (reg)-[:REGULATION_HAS_SECTION]->(sec)
RETURN count(*) as created
""", 2),
    
    'DataProtectionAssessment': ("""
MATCH (dpa:DataProtectionAssessment {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (dpa)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_REQUIRES_DPA]->(dpa)
RETURN count(*) as created
""", 1),
    
    'Policy': ("""
MATCH (pol:Policy {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (pol)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(pol)
RETURN count(*) as created
""", 1),
    
    'Control': ("""
MATCH (co:Control {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (co)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co)
RETURN count(*) as created
""", 1),
    
    'Exemption': ("""
MATCH (ex:Exemption {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (ex)-[]-()
MATCH (ro:Role {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (ro)-[:ROLE_QUALIFIES_FOR_EXEMPTION]->(ex)
RETURN count(*) as created
""", 1),
}

total_created = 0
successful_fixes = 0
failed_fixes = []

# Execute each fix
for node_type, (query, expected_count) in fixes.items():
    try:
        logger.info(f"Fixing {node_type} ({expected_count} nodes)...")
        result = client.query(query)
        
        if isinstance(result, str):
            logger.error(f"  ✗ Error: {result}")
            failed_fixes.append(node_type)
        elif isinstance(result, list) and len(result) > 0:
            if isinstance(result[0], dict):
                created = result[0].get('created', 0)
                total_created += created
                successful_fixes += 1
                logger.info(f"  ✓ Created {created} relationships")
            else:
                logger.error(f"  ✗ Unexpected result format")
                failed_fixes.append(node_type)
        else:
            logger.error(f"  ✗ No result returned")
            failed_fixes.append(node_type)
    
    except Exception as e:
        logger.error(f"  ✗ Exception: {e}")
        failed_fixes.append(node_type)

logger.info("\n" + "="*80)
logger.info("VERIFICATION")
logger.info("="*80)

# Verify orphans are fixed
verify_query = """
MATCH (n)
WHERE n.regional_standard_and_regulation_id = 'vcdpa'
AND NOT (n)-[]-()
WITH labels(n)[0] as node_type
RETURN node_type, count(*) as orphan_count
ORDER BY orphan_count DESC
"""

logger.info("\nVerifying fix...")
verify_result = client.query(verify_query)

remaining_orphans = 0
if isinstance(verify_result, list) and len(verify_result) > 0:
    logger.info("\nRemaining orphan nodes:\n")
    for row in verify_result:
        if isinstance(row, dict):
            node_type = row.get('node_type', 'Unknown')
            orphan_count = row.get('orphan_count', 0)
            remaining_orphans += orphan_count
            logger.info(f"  {str(node_type):40} : {orphan_count:3} orphan nodes")
else:
    logger.info("\n✓ No orphan nodes found!")

logger.info("\n" + "="*80)
logger.info("SUMMARY")
logger.info("="*80)

logger.info(f"\nFixed node types: {successful_fixes}/{len(fixes)}")
logger.info(f"Total relationships created: {total_created}")
logger.info(f"Remaining orphan nodes: {remaining_orphans}")

if remaining_orphans == 0:
    logger.info("\n✓✓✓ SUCCESS! All orphan nodes have been connected!")
    logger.info("Your graph is now fully integrated across all 192 nodes.")
elif remaining_orphans > 0:
    logger.info(f"\n⚠ Still {remaining_orphans} orphan nodes remaining.")
    logger.info("These may require manual relationship creation.")

if len(failed_fixes) > 0:
    logger.info(f"\n⚠ Failed to fix: {', '.join(failed_fixes)}")

# Final graph statistics
logger.info("\n" + "="*80)
logger.info("FINAL GRAPH STATISTICS")
logger.info("="*80)

stats_query = """
MATCH (n)
WHERE n.regional_standard_and_regulation_id = 'vcdpa'
WITH count(n) as total_nodes
MATCH ()-[r]->()
WHERE r is not null
RETURN total_nodes, count(r) as total_relationships
"""

try:
    stats = client.query(stats_query)
    if isinstance(stats, list) and len(stats) > 0:
        if isinstance(stats[0], dict):
            total_nodes = stats[0].get('total_nodes', 0)
            total_rels = stats[0].get('total_relationships', 0)
            logger.info(f"\nTotal nodes: {total_nodes}")
            logger.info(f"Total relationships: {total_rels}")
except:
    pass

client.close()
logger.info("\n✓ Done!")