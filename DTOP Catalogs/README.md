# DTOP Catalogs

Node and relationship CSVs for the DTOP risk and control catalogues, extracted from

```
DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/risk-catalog.json
DTOP-OLD/client/src/assets/docs/knowledgeRepository/graph/DtopCatalogs/control-catalog.json
```

**11 domains · 36 functional domains · 281 risks · 1,451 controls · 1,097 solutions · 2,893 nodes · 7,053 relationships**

The CSVs follow the same convention as the framework folders in this repository:
the first column of a `nodes_<Label>.csv` is `<label>_id`, and every
`rels_<TYPE>.csv` is `source_id,target_id,rel_type` plus any edge properties.

Loaded into Neo4j by [App_new/dtop_catalogs.py](../App_new/dtop_catalogs.py)
under `framework_id = 'DTOP_CATALOGS'` and the anchor label `:DTOPCatalogNode`.

Regenerate with:

```bash
python "DTOP Catalogs/build_csvs.py"
```

## Files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Domain.csv` | 11 | The top-level DTOM domains, shared by both catalogues |
| `nodes_FunctionalDomain.csv` | 36 | Functional domains — 32 in both catalogues, 4 only in the risk catalogue |
| `nodes_Risk.csv` | 281 | Every risk, with its verbatim description |
| `nodes_Control.csv` | 1,451 | Every control, keyed on the catalogue's own `control_id` |
| `nodes_Solution.csv` | 1,097 | Possible solutions, one node per (size, description) pair |
| `nodes_Weighting.csv` | 11 | The weighting values 0–10 |
| `nodes_CSFFunction.csv` | 6 | Govern, Identify, Protect, Detect, Respond, Recover |
| `rels_HAS_FUNCTIONAL_DOMAIN.csv` | 40 | Domain → FunctionalDomain |
| `rels_HAS_RISK.csv` | 281 | FunctionalDomain → Risk |
| `rels_HAS_CONTROL.csv` | 1,451 | Domain → Control |
| `rels_HAS_POSSIBLE_SOLUTION.csv` | 2,598 | Control → Solution |
| `rels_HAS_WEIGHTING.csv` | 1,342 | Control → Weighting |
| `rels_MAPS_TO_FUNCTION.csv` | 1,341 | Control → CSFFunction |

## Shape

```
Domain (11) ──HAS_FUNCTIONAL_DOMAIN──> FunctionalDomain (36) ──HAS_RISK──> Risk (281)
   │
   └──HAS_CONTROL──> Control (1451) ──HAS_POSSIBLE_SOLUTION──> Solution (1097)
                          ├──────────HAS_WEIGHTING──────────> Weighting (11)
                          └──────────MAPS_TO_FUNCTION───────> CSFFunction (6)
```

Risks hang off a **functional** domain; controls hang off a **top-level**
domain. That asymmetry is the catalogues' own — the control catalogue never
attaches a control to a functional domain — and it is preserved rather than
smoothed over.

## The two catalogues are merged into one

The two JSON files state the same taxonomy. All 11 `Domain` names and 32 of the
36 `FunctionalDomain` names appear in both, byte-identical. They are
deduplicated into one set of nodes, so risks and controls hang off the same
domain tree instead of two disconnected copies of it.

Every node and every edge carries a **`catalogs`** column recording where it
came from — `risk`, `control`, or `risk;control` — and `source_document` lists
the matching file path(s). Nothing about the split is lost.

| | risk-catalog | control-catalog | both | merged |
|---|---:|---:|---:|---:|
| Domain | 11 | 11 | 11 | **11** |
| FunctionalDomain | 36 | 32 | 32 | **36** |
| `HAS_FUNCTIONAL_DOMAIN` edges | 39 | 32 | 31 | **40** |

The four functional domains that only the risk catalogue knows about are
*Application Runtime Defense*, *Bio-Economy Security*, *Cloud Security Posture
Management (CSPM)* and *Security Metrics & Reporting*. One `HAS_FUNCTIONAL_DOMAIN`
pair is stated only by the control catalogue.

Three functional domains sit under two domains each — *Acquisition & Supply
Chain*, *Critical Infrastructure Protection* and *Secure Software Development
(SSDLC)* — which is why 36 functional domains carry 40 edges.

Merging the 31 pairs stated in both files is the **only** deduplication that
happens: 7,084 stated edges become 7,053 distinct ones. No other row is dropped,
and no property value is altered anywhere.

## Node identifiers

Both JSONs are graph exports carrying Neo4j element ids (`4:ef071f45-…:318`).
Those come from two *different* instances and are not stable, so they are
discarded and every node is re-keyed on its own content:

| Label | `<label>_id` | Example |
|---|---|---|
| Domain | `dom_<slug(name)>` | `dom_cyber_defense_resilience` |
| FunctionalDomain | `fd_<slug(name)>` | `fd_acquisition_supply_chain` |
| Risk | `risk_<slug(title)>` | `risk_lack_of_ai_model_provenance` |
| Control | the catalogue's own `control_id`, verbatim | `WEB-10` |
| Solution | `sol_<slug(size)>_<sha1(size\|description)[:10]>` | `sol_enterprise_01ad08df55` |
| Weighting | `wt_<value>` | `wt_9` |
| CSFFunction | `csf_<slug(name)>` | `csf_protect` |

`Control` is the one label with a natural key already in the source —
`control_id` is unique across all 1,451 — so it is used as-is rather than being
re-slugged into a synthetic id that would force the source property to be
renamed. `Solution` is the one label with no natural key at all: the same
description recurs under several sizes (402 distinct descriptions across 1,097
rows), so the key is content-addressed over size *and* description.

All 2,893 ids are unique across every label, which the build script asserts.
That matters because the loader merges on `(framework_id, node_id)` under a
single anchor label and the `rels_*.csv` files record no endpoint labels.

## Labels

Labels are the catalogues' own. `Domain` and `Control` therefore collide with
the same-named labels in NIST SP 800-53r5, CMMC 2.0, NERC, FFIEC and others —
by design, exactly as everywhere else in this repository. `framework_id` plus
the `:DTOPCatalogNode` anchor is what separates them:

```cypher
MATCH (c:Control {framework_id: 'DTOP_CATALOGS'}) RETURN count(c)   // 1451
```

The one renamed label is **`CSFFunction`**, written `CSF Function` in the
source. A space in a label forces backticks into every query that touches it, so
it is loaded without the space and the original spelling is kept verbatim in the
`source_label` property.

## Columns

**`nodes_Domain.csv`** — `domain_id`, `name`, `type`, `functional_domain_count`,
`control_count`, `catalogs`, `source_document`. `type` is `DTOM` on all 11; only
the risk catalogue states it, and the control catalogue's identical domains
inherit it through the merge.

**`nodes_FunctionalDomain.csv`** — `functionaldomain_id`, `name`,
`domain_count`, `risk_count`, `catalogs`, `source_document`.

**`nodes_Risk.csv`** — `risk_id`, `title`, `description`, `functional_domain`,
`domain`, `catalogs`, `source_document`. The two parent names are mirrored onto
the node as well as modelled as edges, so a risk row stands alone without a join.

**`nodes_Control.csv`** — `control_id`, `title`, `description`, `domain`,
`weighting`, `csf_function`, `solution_count`, `catalogs`, `source_document`.
`domain`, `weighting` and `csf_function` are likewise mirrored from the edges.

**`nodes_Solution.csv`** — `solution_id`, `size`, `description`,
`control_count`, `catalogs`, `source_document`.

**`nodes_Weighting.csv`** — `weighting_id`, `value`, `control_count`,
`catalogs`, `source_document`.

**`nodes_CSFFunction.csv`** — `csffunction_id`, `name`, `source_label`,
`control_count`, `catalogs`, `source_document`.

**`rels_HAS_POSSIBLE_SOLUTION.csv`** carries `size`, **`rels_HAS_WEIGHTING.csv`**
carries `value`, and **`rels_MAPS_TO_FUNCTION.csv`** carries `function_name`, so
each of those edges can be filtered without visiting its target node.

## What the catalogues leave blank

These are gaps in the source data, carried through as empty strings rather than
guessed at.

| Gap | Count | Notes |
|---|---:|---|
| Controls with no `description` | 109 | Exactly the same 109 controls that have no weighting |
| Controls with no weighting | 109 | Same set as above |
| Controls not mapped to a CSF function | 110 | The 109 above plus `TDA-11.2`, which *is* described and weighted |
| Controls with no solutions | 584 | 867 of the 1,451 controls have solutions |
| Controls with only 2 of 3 solutions | 3 | `GOV-10`, `PES-15`, `VPM-10` — each missing one size |

`weighting` is loaded as `null` rather than `0` where it is blank, because `0`
is a real weighting the catalogue uses — `TDA-11.2` carries it, and it is the
same control that is missing its CSF mapping.

## Distributions

**Controls per domain**

| Domain | Functional domains | Controls |
|---|---:|---:|
| Cyber Defense & Resilience | 4 | 356 |
| Data Privacy & Protection | 4 | 271 |
| Infrastructure & Network Security | 4 | 204 |
| AI & Emerging Technology Security | 4 | 165 |
| Identity and Access Management | 5 | 155 |
| Information Security Governance | 4 | 135 |
| Personnel & Physical Security | 3 | 72 |
| Critical Infrastructure Protection | 2 | 38 |
| Cloud & Platform Security | 5 | 29 |
| Third-Party Risk Management | 2 | 15 |
| Application & Product Security | 3 | 11 |

**CSF function** — Protect 774, Identify 232, Detect 161, Govern 92, Respond 52,
Recover 30, unmapped 110.

**Weighting** — 9 is the most common (314 controls), then 8 (256) and 5 (249);
10 is used 163 times and 0 exactly once.

**Solutions** — three sizes, near-evenly split: Enterprise 366, Large Business
366, Medium Business 365. Solutions are shared across controls, which is why
1,097 nodes carry 2,598 edges; 714 are used by exactly one control, and the most
reused is cited by 65.

Controls use 33 identifier prefixes; the largest are `AAT` (156), `IAC` (112),
`PRI` (102), `NET` (98) and `DCH` (85).

## Fidelity

`build_csvs.py` copies values through unchanged; titles and descriptions are
byte-identical to the JSON, including the `∙` bullet that opens every solution
description. The derived columns are the `*_count` totals, the `catalogs`
provenance column, the denormalised parent names on `Risk` and `Control`, and
`source_label` on `CSFFunction`.

The build was checked by reconstructing both JSONs from the CSVs: all 2,936
source nodes reappear with every scalar property matching exactly, and all 7,084
stated relationships resolve to a CSV row with no dangling endpoints. The script
asserts both id uniqueness and endpoint resolvability on every run.

## Queries

```cypher
// One domain, end to end
MATCH (d:Domain {framework_id:'DTOP_CATALOGS', name:'Data Privacy & Protection'})
OPTIONAL MATCH (d)-[:HAS_FUNCTIONAL_DOMAIN]->(fd)-[:HAS_RISK]->(r)
OPTIONAL MATCH (d)-[:HAS_CONTROL]->(c)
RETURN d, fd, r, c;

// Highest-weighted controls and their CSF function
MATCH (c:Control {framework_id:'DTOP_CATALOGS'})-[:HAS_WEIGHTING]->(w:Weighting)
WHERE w.value >= 9
RETURN c.control_id, c.title, w.value, c.csf_function ORDER BY w.value DESC, c.control_id;

// A control's three solutions, by organisation size
MATCH (c:Control {framework_id:'DTOP_CATALOGS', control_id:'GOV-01'})
      -[r:HAS_POSSIBLE_SOLUTION]->(s:Solution)
RETURN r.size AS size, s.description ORDER BY size;

// Where the two catalogues disagree about the taxonomy
MATCH (n:DTOPCatalogNode {framework_id:'DTOP_CATALOGS'})
WHERE n.catalogs <> 'risk;control' AND (n:Domain OR n:FunctionalDomain)
RETURN labels(n)[1] AS label, n.name AS name, n.catalogs AS stated_in;
```
