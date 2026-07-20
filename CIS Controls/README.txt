# CIS Controls v8.1.2 Knowledge Graph Dataset

## Overview
This dataset models the CIS Critical Security Controls v8.1.2 as a knowledge graph.
It contains all 18 Controls and all 153 Safeguards with their full descriptions and
their mappings to Implementation Groups, Asset Classes, and Security Functions.

Source document: CIS_Controls_Guide_v8.1.2_0325_v2.pdf (Center for Internet Security).

NOTE: This README was rewritten to match the CSV files that actually ship in this
folder. Earlier versions of this file described a different `nodes_*.csv` /
`relations_*.csv` naming scheme (and a GoverningBody / Framework->Control layer)
that are NOT present here. The descriptions below are authoritative.

## Dataset Contents

### Node CSV Files
1. **nodes_framework.csv** (1 record)
   - Columns: name, version, description, total_controls, total_safeguards
   - The top-level CIS Controls framework node (v8.1, 18 controls, 153 safeguards).

2. **CIS Controls - Controls.csv** (18 records)
   - Columns: control_id, name, description
   - The 18 CIS Controls with full descriptions.

3. **CIS Controls - Safeguard.csv** (153 records)
   - Columns: safeguard_id, title, asset_type, security_function, implementation_groups, description
   - Every safeguard, with its single asset_type, single security_function, the
     implementation groups it belongs to (semicolon-separated, e.g. "IG1;IG2;IG3"),
     and the full safeguard description.

4. **CIS Controls - Implementation Group.csv** (3 records)
   - Columns: name, title, description
   - IG1 (Essential Cyber Hygiene), IG2 (Enterprise Security), IG3 (Very Sensitive Data).

5. **CIS Controls - Asset Class.csv** (7 records)
   - Columns: name, description
   - Devices, Applications, Data, Users, Network, Software, Documentation.

6. **CIS Controls - Security Functions.csv** (6 records)
   - Columns: name, source, description
   - NIST CSF 2.0 functions: Govern, Identify, Protect, Detect, Respond, Recover.

### Relationship CSV Files
All relationship files share the columns:
from_node_type, from_node_id, relationship_type, to_node_type, to_node_id

1. **CIS Control - Control Safeguard.csv** (153 relationships)
   - Control -[HAS_SAFEGUARD]-> Safeguard

2. **CIS Controls - Safeguard Implementation.csv** (339 relationships)
   - Safeguard -[BELONGS_TO_IG]-> ImplementationGroup
   - A safeguard belongs to one or more IGs (IG1 safeguards are also in IG2 and IG3).

3. **CIS Control - Safeguard Asset.csv** (153 relationships)
   - Safeguard -[APPLIES_TO_ASSET]-> AssetClass
   - One asset-class edge per safeguard (each safeguard has a single asset_type).

4. **CIS Control - Safeguard Security Function.csv** (153 relationships)
   - Safeguard -[MAPS_TO_FUNCTION]-> SecurityFunction
   - One security-function edge per safeguard.

## Graph Data Model

```
                    +-----------------+
                    |   Framework     |
                    | (CIS v8.1.2)    |
                    +--------+--------+
                             |
                        (HAS_CONTROL, conceptual)
                             |
                    +--------v--------+
                    |    Control      |
                    | (18 controls)   |
                    +--------+--------+
                             |
                       HAS_SAFEGUARD
                             |
                    +--------v--------+
                    |   Safeguard     |
                    | (153 safeguards)|
                    +--------+--------+
                             |
          +------------------+------------------+
          |                  |                  |
    BELONGS_TO_IG    APPLIES_TO_ASSET   MAPS_TO_FUNCTION
          |                  |                  |
  +-------v------+  +--------v-------+  +-------v-------+
  |Implementation|  |  AssetClass    |  |   Security    |
  |    Group     |  |  (7 classes)   |  |   Function    |
  | (IG1/IG2/IG3)|  |                |  |  (6 funcs)    |
  +--------------+  +----------------+  +---------------+
```

## Statistics

- Total nodes: 188
  - 1 Framework
  - 18 Controls
  - 153 Safeguards
  - 3 ImplementationGroups
  - 7 AssetClasses
  - 6 SecurityFunctions

- Total relationships: 798
  - 153 Control -> Safeguard (HAS_SAFEGUARD)
  - 339 Safeguard -> ImplementationGroup (BELONGS_TO_IG)
  - 153 Safeguard -> AssetClass (APPLIES_TO_ASSET)
  - 153 Safeguard -> SecurityFunction (MAPS_TO_FUNCTION)

- Implementation Group coverage:
  - IG1: 56 safeguards
  - IG2: 130 safeguards
  - IG3: 153 safeguards (all)

- Asset Class distribution (one per safeguard):
  - Data: 31, Documentation: 28, Software: 25, Devices: 24, Users: 23, Network: 22

## File Format
- UTF-8 encoding, comma delimiter, header row included, no BOM.
- Fields containing commas (notably safeguard descriptions) are double-quoted.

## Version
- CIS Controls Version: 8.1.2
- Source Document: CIS_Controls_Guide_v8.1.2_0325_v2.pdf
- Publisher: Center for Internet Security (CIS)

## License & Attribution
This dataset is based on the CIS Critical Security Controls v8.1.2 published by the
Center for Internet Security (CIS). CIS Controls are copyright (c) Center for
Internet Security. For official documentation, visit https://www.cisecurity.org/controls/
