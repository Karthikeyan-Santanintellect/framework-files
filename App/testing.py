import sys
import logging
import time
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
logger.info("STEP 1: IDENTIFY ORPHAN NODES")
logger.info("="*80)

# Query 1: Find all orphan nodes (no relationships) - FIXED FOR NEO4J 5.x
# Using COUNT {} instead of deprecated size()
orphan_query = """
MATCH (n)
WHERE n.regional_standard_and_regulation_id = 'vcdpa'
AND NOT (n)-[]-()
WITH labels(n)[0] as node_type
RETURN node_type, count(*) as orphan_count
ORDER BY orphan_count DESC
"""

logger.info("\nFinding all orphan nodes...")

try:
    orphan_result = client.query(orphan_query)
    
    # Debug: Print the actual result format
    logger.info(f"\nDebug - Result type: {type(orphan_result)}")
    logger.info(f"Debug - Result: {orphan_result}")
    
    # Check if result is an error string
    if isinstance(orphan_result, str):
        logger.error(f"✗ Query returned error: {orphan_result}")
        client.close()
        sys.exit(1)
    
    if not orphan_result:
        logger.info("\n✓ No orphan nodes found!")
        logger.info("All nodes have relationships.")
        client.close()
        sys.exit(0)
    
    # Handle different result formats
    logger.info(f"\n✓ Found orphan nodes:\n")
    
    if isinstance(orphan_result, list) and len(orphan_result) > 0:
        # Check if result is list of dicts
        if isinstance(orphan_result[0], dict):
            for row in orphan_result:
                node_type = row.get('node_type', 'Unknown')
                orphan_count = row.get('orphan_count', 0)
                logger.info(f"  {str(node_type):40} : {orphan_count:3} orphan nodes")
        else:
            logger.error(f"Unexpected result format: {orphan_result[0]}")
            logger.error("Please check the query result structure")
    
except Exception as e:
    logger.error(f"✗ Error in orphan detection: {e}")
    logger.error(f"Error type: {type(e)}")
    import traceback
    traceback.print_exc()
    client.close()
    sys.exit(1)

# Query 2: Get sample orphan nodes for each type
logger.info("\n" + "="*80)
logger.info("STEP 2: GET SAMPLE ORPHAN NODES FOR EACH TYPE")
logger.info("="*80)

sample_orphans_query = """
MATCH (n)
WHERE n.regional_standard_and_regulation_id = 'vcdpa'
AND NOT (n)-[]-()
WITH labels(n)[0] as node_type, collect(n)[0..3] as samples
RETURN node_type, [s IN samples | s.id][0..3] as sample_ids
ORDER BY node_type
"""

logger.info("\nSample orphan nodes:\n")

try:
    sample_result = client.query(sample_orphans_query)
    
    orphan_types = {}
    
    if isinstance(sample_result, str):
        logger.error(f"✗ Query returned error: {sample_result}")
    elif isinstance(sample_result, list) and len(sample_result) > 0:
        if isinstance(sample_result[0], dict):
            for row in sample_result:
                node_type = row.get('node_type', 'Unknown')
                sample_ids = row.get('sample_ids', [])
                orphan_types[node_type] = sample_ids
                logger.info(f"  {str(node_type):30} - Samples: {sample_ids}")
    
except Exception as e:
    logger.error(f"✗ Error getting samples: {e}")
    logger.error(f"Error type: {type(e)}")

logger.info("\n" + "="*80)
logger.info("STEP 3: POSSIBLE RELATIONSHIPS FOR ORPHANS")
logger.info("="*80)

# For each orphan type, suggest what it should connect to
suggestions = {
    'ExternalFrameworkRequirement': 'Should connect to Requirement via REQUIREMENT_MAPPED_TO_EXTERNAL_FRAMEWORK',
    'Exemption': 'Should connect to Role via ROLE_QUALIFIES_FOR_EXEMPTION',
    'Threshold': 'Should connect to Role via ROLE_MEETS_THRESHOLD',
    'Policy': 'Should connect to Requirement via REQUIREMENT_SUPPORTED_BY_POLICY',
    'Process': 'Should connect to Requirement via REQUIREMENT_IMPACTS_PROCESS and System via PROCESS_SUPPORTED_BY_SYSTEM',
    'System': 'Should connect to Control via CONTROL_IMPLEMENTED_IN_SYSTEM and Process via PROCESS_SUPPORTED_BY_SYSTEM',
    'Control': 'Should connect to Requirement via REQUIREMENT_IMPLEMENTED_BY_CONTROL',
    'ImplementationSpec': 'Should connect to Requirement',
    'DataProtectionAssessment': 'Should connect to Requirement via REQUIREMENT_REQUIRES_DPA',
}

logger.info("\nSuggested relationships:\n")
for orphan_type in orphan_types.keys():
    if orphan_type in suggestions:
        logger.info(f"  {str(orphan_type):30} → {suggestions[orphan_type]}")
    else:
        logger.info(f"  {str(orphan_type):30} → CHECK YOUR CSV MAPPING FILES")

logger.info("\n" + "="*80)
logger.info("STEP 4: DIAGNOSTIC - CSV FILES TO CHECK")
logger.info("="*80)

csv_checks = {
    'ExternalFrameworkRequirement': 'VCDPA_Requirement_ExternalFramework_Mapping.csv',
    'Exemption': 'VCDPA_Role_Exemptions.csv',
    'Threshold': 'VCDPA_Role_Thresholds.csv',
    'Policy': 'VCDPA_Requirement_Policies.csv',
    'Process': ['VCDPA_Requirement_Processes.csv', 'VCDPA_Process_Systems.csv'],
    'System': ['VCDPA_Control_Systems.csv', 'VCDPA_Process_Systems.csv'],
    'Control': 'VCDPA_Requirement_Controls.csv',
    'DataProtectionAssessment': 'VCDPA_Requirement_DPAs.csv',
}

logger.info("\nTo fix orphans, verify these CSV files exist on GitHub:\n")

for orphan_type, csv_files in csv_checks.items():
    if orphan_type in orphan_types:
        if isinstance(csv_files, list):
            logger.info(f"  {orphan_type}:")
            for csv_file in csv_files:
                logger.info(f"    ✓ Check: {csv_file}")
        else:
            logger.info(f"  {orphan_type}:")
            logger.info(f"    ✓ Check: {csv_files}")

logger.info("\n" + "="*80)
logger.info("STEP 5: ACTION PLAN TO FIX ORPHANS")
logger.info("="*80)

logger.info("""
To fix orphan nodes, follow these steps:

1. CHECK CSV FILES:
   - Verify that relationship CSV files exist on GitHub
   - Check file paths and naming
   
2. VERIFY ID MATCHING:
   - Ensure orphan node IDs match the IDs in relationship CSVs
   - Check for case sensitivity (ABC-001 ≠ abc-001)
   
3. RE-RUN IMPORT:
   - Re-run the relationship import queries
   - Check for MATCH clause errors in logs
   
4. VERIFY FIX:
   - Run this script again to confirm orphans are resolved

5. IF STILL ORPHANED:
   - Create manual relationships using Cypher queries (see Step 6)
""")

logger.info("\n" + "="*80)
logger.info("STEP 6: MANUAL FIXES FOR ORPHAN TYPES")
logger.info("="*80)

logger.info("""
Run these Cypher queries to manually fix specific orphan types:

✓ For Exemption nodes orphaned:
MATCH (ex:Exemption {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (ex)-[]-()
MATCH (ro:Role {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (ro)-[:ROLE_QUALIFIES_FOR_EXEMPTION]->(ex)

✓ For Policy nodes orphaned:
MATCH (pol:Policy {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (pol)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_SUPPORTED_BY_POLICY]->(pol)

✓ For System nodes orphaned:
MATCH (sy:System {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (sy)-[]-()
MATCH (co:Control {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (co)-[:CONTROL_IMPLEMENTED_IN_SYSTEM]->(sy)

✓ For Process nodes orphaned:
MATCH (pro:Process {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (pro)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_IMPACTS_PROCESS]->(pro)

✓ For Control nodes orphaned:
MATCH (co:Control {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (co)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_IMPLEMENTED_BY_CONTROL]->(co)

✓ For DataProtectionAssessment nodes orphaned:
MATCH (dpa:DataProtectionAssessment {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (dpa)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_REQUIRES_DPA]->(dpa)

✓ For ImplementationSpec nodes orphaned:
MATCH (impl:ImplementationSpec {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (impl)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (impl)-[:IMPLEMENTS_REQUIREMENT]->(req)

✓ For ExternalFrameworkRequirement nodes orphaned:
MATCH (efr:ExternalFrameworkRequirement {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (efr)-[]-()
MATCH (req:Requirement {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (req)-[:REQUIREMENT_MAPPED_TO_EXTERNAL_FRAMEWORK]->(efr)

✓ For Threshold nodes orphaned:
MATCH (th:Threshold {regional_standard_and_regulation_id: 'vcdpa'})
WHERE NOT (th)-[]-()
MATCH (ro:Role {regional_standard_and_regulation_id: 'vcdpa'})
MERGE (ro)-[:ROLE_MEETS_THRESHOLD]->(th)
""")

logger.info("\n" + "="*80)
logger.info("SUMMARY")
logger.info("="*80)

total_orphans_query = """
MATCH (n)
WHERE n.regional_standard_and_regulation_id = 'vcdpa'
AND NOT (n)-[]-()
RETURN count(n) as total_orphans
"""

try:
    total_orphans = client.query(total_orphans_query)
    
    if isinstance(total_orphans, str):
        logger.error(f"✗ Query returned error: {total_orphans}")
        total_orphan_count = 0
    elif isinstance(total_orphans, list) and len(total_orphans) > 0:
        if isinstance(total_orphans[0], dict):
            total_orphan_count = total_orphans[0].get('total_orphans', 0)
        else:
            total_orphan_count = 0
    else:
        total_orphan_count = 0
    
    logger.info(f"\nTotal orphan nodes: {total_orphan_count}")
    logger.info(f"Orphan node types found: {len(orphan_types)}")
    
    if len(orphan_types) > 0:
        logger.info("\nOrphan types:")
        for otype in orphan_types.keys():
            logger.info(f"  - {otype}")
        logger.info("\n✓ Diagnostic complete!")
        logger.info("Next step: Run the manual fixes above or re-import CSV files")
    else:
        logger.info("\n✓ All nodes have relationships! Your graph is fully connected.")

except Exception as e:
    logger.error(f"✗ Error in final summary: {e}")

finally:
    client.close()