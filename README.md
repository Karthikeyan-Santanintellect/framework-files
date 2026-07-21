# Compliance Framework Knowledge Graph

This repository holds the node and relationship CSVs for 26 compliance, security and privacy
frameworks, together with the loader scripts in [App_new/](App_new/) that build them into a
Neo4j graph.

Each framework is extracted from its authoritative source document (statute, regulation,
standard or official catalog) into a set of node CSVs and relationship CSVs, then loaded into
the Neo4j Aura instance (database `d7883150`).

## Graph contents

**26 frameworks · 7,399 nodes · 65,731 relationships · 285 node labels · 568 relationship types**

Every node carries a framework identifier, so any framework can be selected in isolation. The
property name depends on the framework's classification:

| Classification | Identifier property |
|---|---|
| IS frameworks & standards | `IS_frameworks_standard_id` |
| Industry standards & regulations | `industry_standard_regulation_id` |
| Regional standards & regulations | `regional_standard_regulation_id` |

## Nodes and relationships per framework

**Relationships** counts edges where both endpoints belong to that framework.
**Cross-framework** counts edges that link the framework to a *different* framework — control
crosswalks and mappings (for example SCF → ISO 27002, or a framework mapped to NIST CSF 2.0).
Each such edge is counted once for each of the two frameworks it connects.

| # | Framework | Neo4j ID | Nodes | Relationships | Cross-framework |
|---|-----------|----------|------:|--------------:|----------------:|
| 1 | CIS Controls | `CIS CONTROLS 8.1` | 188 | 823 | 283 |
| 2 | CPA | `CPA 1.0` | 201 | 342 | 25 |
| 3 | CPRA | `CPRA 2.0` | 182 | 855 | 8 |
| 4 | DORA | `DORA 2022/2554` | 222 | 1,781 | 70 |
| 5 | DPDPA | `DPDPA 1.0` | 296 | 4,303 | 106 |
| 6 | GDPR | `GDPR 2016/679` | 596 | 14,109 | 85 |
| 7 | GLBA | `GLBA 1999` | 69 | 342 | 74 |
| 8 | HIPAA | `HIPAA 2026` | 244 | 3,875 | 0 |
| 9 | HITECH | `HITECH_ACT_2009` | 200 | 5,591 | 40 |
| 10 | HITRUST | `HITRUST 11.6.0` | 1,197 | 1,862 | 60 |
| 11 | ISO 27001 | `ISO27001_2022` | 269 | 2,207 | 323 |
| 12 | ISO 27002 | `ISO27002_2022` | 221 | 11,815 | 503 |
| 13 | NERC CIP | `NERC_CIP` | 246 | 484 | 0 |
| 14 | NIS 2 | `NIS2-EU-2022-2555` | 228 | 2,998 | 266 |
| 15 | NIST AI RMF | `NIST_AI_RMF_1.0` | 96 | 1,448 | 247 |
| 16 | NIST CSF 2.0 | `NIST_CSF_2.0` | 135 | 134 | 1,213 |
| 17 | NIST PMF 1.0 | `NIST_PMF_1.0` | 169 | 168 | 361 |
| 18 | NIST PMF 1.1 | `NIST_PMF_1.1` | 137 | 144 | 0 |
| 19 | NIST RMF | `NIST_RMF_5.2` | 114 | 137 | 38 |
| 20 | PCI DSS | `PCI-DSS 4.0` | 233 | 5,167 | 0 |
| 21 | SCF | `SCF-2025.4` | 1,485 | 1,484 | 3,599 |
| 22 | SEC Cyber Rule | `SEC-2023` | 72 | 85 | 0 |
| 23 | SHIELD | `NY SHIELD 1.0` | 85 | 109 | 108 |
| 24 | TDPSA | `TDPSA 2023` | 160 | 175 | 26 |
| 25 | TISAX | `TISAX 2.8` | 60 | 39 | 9 |
| 26 | VCDPA | `VCDPA 2023` | 294 | 1,505 | 54 |
| | **Total** | | **7,399** | **61,982** | **7,498** |

The cross-framework column sums to 7,498 because each mapping edge is counted once for each of
the two frameworks it connects; there are **3,749 distinct** such edges. The relationship total
in the graph is therefore **65,247** = 61,498 within-framework + 3,749 cross-framework.

## Framework sources

| Framework | Source document |
|-----------|-----------------|
| CIS Controls | CIS Controls Guide v8.1.2 |
| CPA | Colorado Privacy Act Rules, 4 CCR 904-3 (with C.R.S. §§ 6-1-1301…1313) |
| CPRA | California Proposition 24 (2020) |
| DORA | Regulation (EU) 2022/2554 |
| DPDPA | Digital Personal Data Protection Act, 2023 (India) |
| GDPR | Regulation (EU) 2016/679 |
| GLBA | Gramm-Leach-Bliley Act, Title V |
| HIPAA | 45 CFR Part 164 Subparts C/D and 45 CFR Part 160 Subpart D |
| HITECH | Health Information Technology for Economic and Clinical Health Act (2009) |
| HITRUST | HITRUST CSF v11.6.0 |
| ISO 27001 | ISO/IEC 27001:2022 |
| ISO 27002 | ISO/IEC 27002:2022 |
| NIS 2 | Directive (EU) 2022/2555 |
| NIST AI RMF | NIST AI 100-1, AI RMF 1.0 |
| NIST CSF 2.0 | NIST Cybersecurity Framework 2.0 |
| NIST PMF 1.0 | NIST CSWP 10, Privacy Framework v1.0 (Jan 2020) |
| NIST PMF 1.1 | NIST CSWP 40 ipd, Privacy Framework v1.1 |
| NIST RMF | NIST SP 800-37r2 |
| PCI DSS | PCI DSS v4.0.1 (June 2024) |
| SCF | Secure Controls Framework 2025.4 |
| SEC Cyber Rule | SEC Cybersecurity Risk Management & Disclosure Rule (2023) |
| SHIELD | N.Y. Gen. Bus. Law §§ 899-aa, 899-bb |
| TDPSA | Texas HB4, Business & Commerce Code Ch. 541 |
| TISAX | ENX TISAX Participant Handbook v2.8 (ISA 5) |
| VCDPA | Va. Code §§ 59.1-575 through 59.1-585 |

## Loading

Loader scripts live in [App_new/](App_new/), one per framework, plus
[App_new/push_verified.py](App_new/push_verified.py) to run a group of them.

```bash
python App_new/gdpr.py          # load a single framework
python App_new/push_verified.py # load a set
```

Connection details are read from `.env` (see `.env.example`) by
[App_new/app.py](App_new/app.py).

The loaders use Cypher `LOAD CSV`, which executes **server-side on the Neo4j instance**. The
CSVs are therefore fetched over HTTPS from this repository's raw GitHub URLs, which means CSV
changes must be committed and pushed before a loader will pick them up.

## Querying by framework

```cypher
// All nodes for one framework
MATCH (n) WHERE n.regional_standard_regulation_id = 'GDPR 2016/679' RETURN n;

// Node counts by label for one framework
MATCH (n {IS_frameworks_standard_id: 'ISO27002_2022'})
RETURN labels(n)[0] AS label, count(*) AS nodes ORDER BY nodes DESC;

// Cross-framework control mappings
MATCH (a:Control {IS_frameworks_standard_id: 'SCF-2025.4'})
      -[:SCF_CONTROL_HAS_EXTERNAL_CONTROLS]->(b)
RETURN b.IS_frameworks_standard_id AS framework, count(*) AS mappings
ORDER BY mappings DESC;
```
