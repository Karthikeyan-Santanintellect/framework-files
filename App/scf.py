constraint_is_framework = """
CREATE CONSTRAINT is_framework_unique IF NOT EXISTS
FOR (f:ISFrameworksAndStandard) REQUIRE f.ISframework_standard_id IS NODE KEY
"""

constraint_domain = """
CREATE CONSTRAINT domain_unique IF NOT EXISTS 
FOR (d:Domain) REQUIRE d.identifier IS NODE KEY
"""

constraint_control = """
CREATE CONSTRAINT control_unique IF NOT EXISTS 
FOR (c:Control) REQUIRE c.control_id IS NODE KEY
"""

# Load Framework
IS_framework_and_standard = """
MERGE (f:ISFrameworksAndStandard {ISframework_standard_id:"SCF-2025.2.2"})
ON CREATE SET
    f.name            = "SCF",
    f.full_name       = "Secure Controls Framework",
    f.version         = "2025.2.2",
    f.publication_date = date("2025-06-12"),
    f.status          = "Active",
    f.total_controls  = 1342,
    f.description     = "A comprehensive cybersecurity and data privacy control framework organized into multiple domains.";
"""

# Load Domain 
domain = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE (d:Domain {identifier: row.identifier})
ON CREATE SET 
    d.name = row.name,
    d.description = row.description,
    d.created_at = datetime()
"""

# Load Controls
controls = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.control_id IS NOT NULL AND trim(row.control_id) <> ''
CALL {
    WITH row
    MERGE (c:Control {control_id: trim(row.control_id)})
    ON CREATE SET 
        c.control_name = row.control_name,
        c.control_text = row.control_text,
        c.domain_identifier = trim(row.domain_identifier),
        c.pptdf_scope = row.pptdf_scope,
        c.control_question = row.control_question,
        c.relative_weighting = toInteger(row.relative_weighting),
        c.nist_csf_function = row.nist_csf_function,
        c.is_new_control = toBoolean(row.is_new_control),
        c.is_mcr = toBoolean(row.is_mcr),
        c.is_dsr = toBoolean(row.is_dsr),
        c.control_type = row.control_type,
        c.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""



# Create Framework→Domain Relationships
framework_domain_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.framework_name IS NOT NULL AND row.domain_identifier IS NOT NULL
CALL {
    WITH row
    MATCH (f:ISFrameworksAndStandard {ISframework_standard_id:"SCF-2025.2.2"})
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MERGE (f)-[r:IS_FRAMEWORKS_AND_STANDARD_CONTAINS_DOMAIN]->(d)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

# Create Domain → Controls Relationships
domain_controls_rel = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row WHERE row.domain_identifier IS NOT NULL AND row.control_id IS NOT NULL
    AND trim(row.domain_identifier) <> '' AND trim(row.control_id) <> ''
CALL {
    WITH row
    MATCH (d:Domain {identifier: trim(row.domain_identifier)})
    MATCH (c:Control {control_id: trim(row.control_id)})
    MERGE (d)-[r:DOMAIN_CONTAINS_CONTROL]->(c)
    ON CREATE SET r.created_at = datetime()
} IN TRANSACTIONS OF 500 ROWS
"""

#control -> CIS_control Mappings
control_cis_control = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.CIS_Control IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.CIS_Control),
        source_framework: "CIS"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.CIS_Control),
        ext.source_framework = "CIS",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "CIS"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "CIS",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;
"""
#control -> CPRA 
control_cpra = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.CPRA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.CPRA),
        source_framework: "CPRA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.CPRA),
        ext.source_framework = "CPRA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "CPRA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "CPRA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;
"""
#control ->DPDPA
control_dpdpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.DPDPA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.DPDPA),
        source_framework: "DPDPA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.DPDPA),
        ext.source_framework = "DPDPA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "DPDPA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "DPDPA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;
"""
#control -> GDPR
control_gdpr = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.GDPR IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.GDPR),
        source_framework: "GDPR"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.GDPR),
        ext.source_framework = "GDPR",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "GDPR"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "GDPR",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> GLBA
control_glba = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.GLBA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.GLBA),
        source_framework: "GLBA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.GLBA),
        ext.source_framework = "GLBA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "GLBA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "GLBA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> HIPAA
control_hipaa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.HIPAA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.HIPAA),
        source_framework: "HIPAA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.HIPAA),
        ext.source_framework = "HIPAA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "HIPAA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "HIPAA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> HITECH
control_hitech = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.HITECH IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.HITECH),
        source_framework: "HITECH"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.HITECH),
        ext.source_framework = "HITECH",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "HITECH"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "HITECH",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> iso_27001
control_iso_27001 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.ISO27001 IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.ISO27001),
        source_framework: "ISO 27001"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.ISO27001),
        ext.source_framework = "ISO 27001",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "ISO 27001"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "ISO 27001",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> iso_27002
control_iso_27002 = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.ISO27002 IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.ISO27002),
        source_framework: "ISO 27002"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.ISO27002),
        ext.source_framework = "ISO 27002",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "ISO 27002"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "ISO 27002",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> nerc_cip
control_nerc_cip = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.NERC_CIP IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.NERC_CIP),
        source_framework: "NERC CIP"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.NERC_CIP),
        ext.source_framework = "NERC CIP",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "NERC CIP"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "NERC CIP",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> nist_ai_rmf
control_nist_ai_rmf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.NIST_AI_RMF IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.NIST_AI_RMF),
        source_framework: "NIST AI RMF"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.NIST_AI_RMF),
        ext.source_framework = "NIST AI RMF",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "NIST AI RMF"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "NIST AI RMF",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> nist_csf
control_nist_csf = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.NIST_CSF IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.NIST_CSF),
        source_framework: "NIST CSF"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.NIST_CSF),
        ext.source_framework = "NIST CSF",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "NIST CSF"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "NIST CSF",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> nist_rmf
control_nist_rmf ="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.NIST_RMF IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.NIST_RMF),
        source_framework: "NIST RMF"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.NIST_RMF),
        ext.source_framework = "NIST RMF",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "NIST RMF"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "NIST RMF",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> PCIDSS
control_pcidss = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.PCIDSS IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.PCIDSS),
        source_framework: "PCI DSS"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.PCIDSS),
        ext.source_framework = "PCI DSS",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "PCI DSS"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "PCI DSS",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""

#control -> TDPSA
control_tdpsa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.TDPSA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.TDPSA),
        source_framework: "TDPSA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.TDPSA),
        ext.source_framework = "TDPSA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "TDPSA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "TDPSA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""
#control -> TISAX
control_tisax = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.TISAX IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.TISAX),
        source_framework: "TISAX"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.TISAX),
        ext.source_framework = "TISAX",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "TISAX"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "TISAX",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""

#control->vcdpa
control_vcdpa = """
LOAD CSV WITH HEADERS FROM '$file_path' AS row
WITH row
WHERE row.SCF_ID IS NOT NULL AND row.VCDPA IS NOT NULL

CALL {
    WITH row
    MATCH (scf:Control {control_id: trim(row.SCF_ID)})
    
    MERGE (ext:ExternalControl {
        control_id: trim(row.VCDPA),
        source_framework: "VCDPA"
    })
    ON CREATE SET
        ext.control_type = "External",
        ext.control_name = trim(row.VCDPA),
        ext.source_framework = "VCDPA",
        ext.created_at = datetime()
    
    MERGE (scf)-[r:CONTROL_MAPS_TO_EXTERNAL {
        framework: "VCDPA"
    }]->(ext)
    ON CREATE SET 
        r.source_framework = "VCDPA",
        r.relationship_type = "MAPS_TO",
        r.created_date = date()
        
} IN TRANSACTIONS OF 1000 ROWS;

"""


import os
import time
import logging
import json
from app import Neo4jConnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Neo4jConnect()

health = client.check_health()
if health is not True:
    print("Neo4j connection error:", health)
    os._exit(1)

logger.info("Creating constraints...")

# CREATE CONSTRAINTS 
client.query(constraint_is_framework)
time.sleep(1)

client.query(constraint_domain)
time.sleep(1)

client.query(constraint_control)
time.sleep(1)

logger.info("Constraints created successfully.")

logger.info("Loading graph structure...")

# LOAD DATA


client.query(IS_framework_and_standard)
time.sleep(2)

client.query(domain.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domains_simplified.csv"))
time.sleep(2)

client.query(controls.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_controls_simplified.csv"))
time.sleep(2)


client.query(framework_domain_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_framework_domain_relationships.csv"))
time.sleep(2)

client.query(domain_controls_rel.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/neo4j_domain_control_relationships.csv"))
time.sleep(2)


client.query(control_cis_control.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_CIS_Mapping.csv"))
time.sleep(2)

client.query(control_cpra.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_CPRA_Mapping.csv"))
time.sleep(2)

client.query(control_dpdpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_DPDPA_Mapping.csv"))
time.sleep(2)

client.query(control_gdpr.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_GDPR_Mapping.csv"))
time.sleep(2)

client.query(control_glba.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_GLBA_Mapping.csv"))
time.sleep(2)

client.query(control_hipaa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_HIPAA_Mapping.csv"))
time.sleep(2)

client.query(control_hitech.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_HITECH_Mapping.csv"))
time.sleep(2)

client.query(control_iso_27001.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_ISO27001_Mapping.csv"))
time.sleep(2)

client.query(control_iso_27002.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_ISO27002_Mapping.csv"))
time.sleep(2)

client.query(control_nerc_cip.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NERC_CIP_Mapping.csv"))
time.sleep(2)

client.query(control_nist_ai_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_AI_RMF_Mapping.csv"))
time.sleep(2)

client.query(control_nist_csf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_CSF_Mapping.csv"))
time.sleep(2)

client.query(control_nist_rmf.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_NIST_RMF_Mapping.csv"))
time.sleep(2)

client.query(control_pcidss.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_PCIDSS_Mapping.csv"))
time.sleep(2)

client.query(control_tdpsa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_TDPSA_Mapping.csv"))
time.sleep(2)

client.query(control_tisax.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_TISAX_Mapping.csv"))
time.sleep(2)

client.query(control_vcdpa.replace('$file_path',"https://github.com/Karthikeyan-Santanintellect/framework-files/raw/refs/heads/main/SCF/SCF_VCDPA_Mapping.csv"))
time.sleep(2)


logger.info("Graph structure loaded successfully.")

res = client.query("""
    MATCH (n)
    WITH collect(DISTINCT n) AS allNodes
    MATCH ()-[r]-()
    WITH allNodes, collect(DISTINCT r) AS allRels
    RETURN {
      nodes: [node IN allNodes | node {
        .*,
        id: elementId(node),
        labels: labels(node),
        mainLabel: head(labels(node))
      }],
      rels: [rel IN allRels | rel {
        .*,
        id: elementId(rel),
        type: type(rel),
        from: elementId(startNode(rel)),
        to: elementId(endNode(rel))
      }]
    } AS graph_data
""")

import json

graph = None

try:
    # CASE 1: res is a list of dictionaries (Standard)
    if isinstance(res, list) and len(res) > 0 and isinstance(res[0], dict):
        graph = res[0].get("graph_data")

    # CASE 2: res is a list of strings (Needs JSON parsing)
    elif isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
        print("Detected string result, attempting to parse JSON...")
        try:
            parsed = json.loads(res[0])
            if isinstance(parsed, dict):
                graph = parsed.get("graph_data", parsed) 
        except json.JSONDecodeError:
            print("Error: Could not parse res[0] as JSON.")

    # CASE 3: res is a single dictionary
    elif isinstance(res, dict):
         graph = res.get("graph_data")

    if graph:
        with open("scf.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(graph, default=str, indent=2))
        logger.info("✓ Exported graph data to scf.json")
        
        # Print statistics
        if isinstance(graph, dict):
            num_nodes = len(graph.get("nodes", []))
            num_rels = len(graph.get("rels", []))
            logger.info(f"Graph exported: {num_nodes} nodes, {num_rels} relationships")
    else:
        logger.error("Failed to extract 'graph_data' from response.")

except Exception as e:
    logger.error(f"An error occurred during export: {e}")

client.close()