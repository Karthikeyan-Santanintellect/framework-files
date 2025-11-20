# CIS Controls v8.1 Neo4j Data Model - Complete Dataset

## Overview
This dataset contains complete data for modeling CIS Critical Security Controls v8.1 in a Neo4j graph database. All 153 safeguards across 18 controls are included with their complete descriptions and mappings.

## Dataset Contents

### Node CSV Files (7 files)
These files contain the entities/nodes in the graph:

1. **nodes_framework.csv** (1 record)
   - Columns: name, version, description, total_controls, total_safeguards
   - The main CIS Controls v8.1 framework node

2. **nodes_governing_body.csv** (1 record)
   - Columns: name, alias, type, mission
   - Center for Internet Security organization

3. **nodes_controls.csv** (18 records)
   - Columns: control_id, name, description
   - All 18 CIS Controls with full descriptions

4. **nodes_safeguards.csv** (153 records)
   - Columns: safeguard_id, description, version
   - All 153 safeguards with complete descriptions

5. **nodes_implementation_group.csv** (3 records)
   - Columns: name, description, safeguard_count
   - IG1, IG2, and IG3 implementation groups

6. **nodes_asset_class.csv** (7 records)
   - Columns: name, description
   - Seven asset types: Devices, Users, Applications, Data, Networks, Software, Documentation

7. **nodes_security_function.csv** (6 records)
   - Columns: name, source
   - Six NIST CSF 2.0 functions: Govern, Identify, Protect, Detect, Respond, Recover

### Relationship CSV Files (6 files)
These files define the connections between nodes:

1. **relations_framework_to_governing_body.csv** (1 relationship)
   - Columns: from_node_type, from_node_id, relationship_type, to_node_type, to_node_id
   - Links: Framework → PUBLISHED_BY → GoverningBody

2. **relations_framework_to_control.csv** (18 relationships)
   - Links: Framework → HAS_CONTROL → Control

3. **relations_control_to_safeguard.csv** (153 relationships)
   - Links: Control → HAS_SAFEGUARD → Safeguard

4. **relations_safeguard_to_implementation_group.csv** (339 relationships)
   - Links: Safeguard → BELONGS_TO_IG → ImplementationGroup
   - Note: Safeguards can belong to multiple IGs (e.g., IG1 safeguards also in IG2 and IG3)

5. **relations_safeguard_to_asset_class.csv** (218 relationships)
   - Links: Safeguard → APPLIES_TO_ASSET → AssetClass
   - Note: Safeguards can apply to multiple asset types

6. **relations_safeguard_to_security_function.csv** (153 relationships)
   - Links: Safeguard → MAPS_TO_FUNCTION → SecurityFunction

### Mapping Data File (1 file)

1. **safeguard_mappings.csv** (153 records)
   - Columns: safeguard_id, implementation_groups, asset_classes, security_functions
   - Comprehensive mapping data for all safeguards
   - Implementation groups as comma-separated values (e.g., "IG1,IG2,IG3")
   - Asset classes as comma-separated values (e.g., "Data,Documentation")
   - Security functions as comma-separated values (e.g., "Govern,Identify")

## Graph Data Model

```
                    ┌─────────────────┐
                    │ GoverningBody   │
                    │  (CIS)          │
                    └─────────▲───────┘
                              │
                     PUBLISHED_BY
                              │
                    ┌─────────┴───────┐
                    │   Framework     │
                    │  (CIS v8.1)     │
                    └─────────┬───────┘
                              │
                         HAS_CONTROL
                              │
                    ┌─────────▼───────┐
                    │    Control      │
                    │  (18 controls)  │
                    └─────────┬───────┘
                              │
                      HAS_SAFEGUARD
                              │
                    ┌─────────▼───────┐
                    │   Safeguard     │
                    │ (153 safeguards)│
                    └─────────┬───────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
        BELONGS_TO_IG   APPLIES_TO_ASSET  MAPS_TO_FUNCTION
              │               │               │
      ┌───────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
      │Implementation│ │  AssetClass│ │  Security  │
      │    Group     │ │ (7 types)  │ │  Function  │
      │ (IG1,IG2,IG3)│ │            │ │ (6 funcs)  │
      └──────────────┘ └────────────┘ └────────────┘
```

## Statistics

- **Total Nodes**: 189
  - 1 Framework
  - 1 GoverningBody
  - 18 Controls
  - 153 Safeguards
  - 3 ImplementationGroups
  - 7 AssetClasses
  - 6 SecurityFunctions

- **Total Relationships**: 882
  - 1 Framework to GoverningBody
  - 18 Framework to Control
  - 153 Control to Safeguard
  - 339 Safeguard to ImplementationGroup
  - 218 Safeguard to AssetClass
  - 153 Safeguard to SecurityFunction

## Usage Examples

### Loading Nodes into Neo4j

```cypher
// Load Framework
LOAD CSV WITH HEADERS FROM 'file:///nodes_framework.csv' AS row
CREATE (f:Framework {
  name: row.name,
  version: row.version,
  description: row.description,
  total_controls: toInteger(row.total_controls),
  total_safeguards: toInteger(row.total_safeguards)
});

// Load Controls
LOAD CSV WITH HEADERS FROM 'file:///nodes_controls.csv' AS row
CREATE (c:Control {
  control_id: row.control_id,
  name: row.name,
  description: row.description
});

// Load Safeguards
LOAD CSV WITH HEADERS FROM 'file:///nodes_safeguards.csv' AS row
CREATE (s:Safeguard {
  safeguard_id: row.safeguard_id,
  description: row.description,
  version: row.version
});
```

### Creating Relationships

```cypher
// Create Control to Safeguard relationships
LOAD CSV WITH HEADERS FROM 'file:///relations_control_to_safeguard.csv' AS row
MATCH (c:Control {control_id: row.from_node_id})
MATCH (s:Safeguard {safeguard_id: row.to_node_id})
CREATE (c)-[:HAS_SAFEGUARD]->(s);

// Create Safeguard to ImplementationGroup relationships
LOAD CSV WITH HEADERS FROM 'file:///relations_safeguard_to_implementation_group.csv' AS row
MATCH (s:Safeguard {safeguard_id: row.from_node_id})
MATCH (ig:ImplementationGroup {name: row.to_node_id})
CREATE (s)-[:BELONGS_TO_IG]->(ig);
```

### Sample Queries

```cypher
// Find all IG1 safeguards
MATCH (s:Safeguard)-[:BELONGS_TO_IG]->(ig:ImplementationGroup {name: 'IG1'})
RETURN s.safeguard_id, s.description
ORDER BY s.safeguard_id;

// Find safeguards that protect Data assets
MATCH (s:Safeguard)-[:APPLIES_TO_ASSET]->(ac:AssetClass {name: 'Data'})
RETURN s.safeguard_id, s.description;

// Find all Govern function safeguards
MATCH (s:Safeguard)-[:MAPS_TO_FUNCTION]->(sf:SecurityFunction {name: 'Govern'})
RETURN s.safeguard_id, s.description;

// Multi-dimensional query: IG1 safeguards for Data Protection
MATCH (s:Safeguard)-[:BELONGS_TO_IG]->(ig:ImplementationGroup {name: 'IG1'})
MATCH (s)-[:APPLIES_TO_ASSET]->(ac:AssetClass {name: 'Data'})
MATCH (s)-[:MAPS_TO_FUNCTION]->(sf:SecurityFunction {name: 'Protect'})
RETURN s.safeguard_id, s.description;
```

## Data Validation

All data has been validated against:
- CIS Controls v8.1 official documentation
- CIS Controls Navigator
- NIST CSF 2.0 mapping
- Official CIS white papers and guides

## Implementation Notes

1. **Implementation Groups**:
   - IG1: 56 safeguards (essential cyber hygiene)
   - IG2: 130 safeguards (IG1 + 74 additional)
   - IG3: 153 safeguards (all safeguards)

2. **Asset Classes** (v8.1 update):
   - New in v8.1: "Documentation" asset class
   - Includes security plans, policies, and procedures

3. **Security Functions** (NIST CSF 2.0):
   - New in v8.1: "Govern" function
   - Aligns with NIST Cybersecurity Framework 2.0

## File Format

All CSV files use:
- UTF-8 encoding
- Comma delimiter
- Header row included
- No BOM (Byte Order Mark)

## Version

- **CIS Controls Version**: 8.1
- **Dataset Version**: 1.0
- **Last Updated**: November 2024
- **Source Document**: Modeling-CIS-Controls-in-Neo4j.docx

## License & Attribution

This dataset is based on CIS Critical Security Controls v8.1 published by the Center for Internet Security (CIS).
CIS Controls are copyright © Center for Internet Security.

For official CIS Controls documentation, visit: https://www.cisecurity.org/controls/

## Support

For questions about this dataset structure or Neo4j implementation, refer to the source document's 
implementation guide which includes detailed Cypher scripts and query examples.
