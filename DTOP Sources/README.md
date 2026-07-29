# DTOP Sources

Node and relationship CSVs for the DTO source catalogue, extracted from

```
DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/dtopSources.json
```

**7 DTO sources · 11 input sources · 2 profile types · 27 relationships**

The CSVs follow the same convention as the framework folders in this repository:
the first column of a `nodes_<Label>.csv` is `<label>_id`, and every
`rels_<TYPE>.csv` is `source_id,target_id,rel_type` plus any edge properties.

Loaded into Neo4j by [App_new/dtop_sources.py](../App_new/dtop_sources.py)
under `framework_id = 'DTOP_SOURCES'` and the anchor label `:DTOPNode`.

Regenerate with:

```bash
python "DTOP Sources/build_csvs.py"
```

## Files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_DTOSource.csv` | 7 | The seven entries in `DTOSources` |
| `nodes_InputSource.csv` | 11 | Every distinct name in a `Sources` list that is **not** itself one of the seven |
| `nodes_ProfileType.csv` | 2 | `Business` and `Technology` |
| `rels_DERIVED_FROM.csv` | 20 | One row per `Sources` entry — what each DTO source is built from |
| `rels_HAS_PROFILE_TYPE.csv` | 7 | Each DTO source to its profile type |

## Columns

**`nodes_DTOSource.csv`** — `dtosource_id`, `source_name`, `url`,
`description`, `reputation_score`, `profile_type`, `stated_source_count`,
`source_document`.

Every `URL` in the JSON is `null` and is written as an empty string. Every
`ReputationScore` is `9`, so the column carries no discriminating information
today; it is kept for fidelity. `profile_type` is duplicated onto the node as
well as modelled as an edge, so the CSV stands alone without a join.

**`nodes_InputSource.csv`** — `inputsource_id`, `name`,
`referenced_by_count`, `possibly_same_as`, `possibly_same_as_basis`,
`source_document`.

**`rels_DERIVED_FROM.csv`** — `target_kind` is `DTOSource` or `InputSource`,
so the two kinds of dependency can be separated without a join. `ordinal`
preserves the position of the entry within the JSON's `Sources` array, and
`stated_source_name` records the name exactly as written there. Together these
mean the original arrays can be reconstructed verbatim from the CSV.

## The dependency graph

Three `Sources` entries name another DTO source exactly, so the seven are not
fully independent:

```
Hi-Def Operating Model ──┐
                         ├──> Risky Business Process
CPRM Process Model ──────┘

Risk Register ──> (no DTO source; all four inputs are external)
Controls Register ──> Risk Register
```

The remaining 17 `Sources` entries point at input sources outside this
catalogue — `Business Profile` (referenced 5 times), `Master Risk Catalog` and
`Google Search (Industry Research)` (twice each), and eight others once each.

## `possibly_same_as` — read this before using it

Three input source names look like they may refer to a DTO source without
matching one exactly. Rather than silently merging them, they are kept as
separate `InputSource` nodes and the suspicion is recorded in two columns.
**`possibly_same_as` is a hint for a human. It is not a relationship, and
nothing in the CSVs treats it as one.**

| Input source | `possibly_same_as` | Basis |
|---|---|---|
| `Hi-Def Operating Model Heatmap` | Hi-Def Operating Model | One name contains the other |
| `CPRM Process Model Heatmap` | CPRM Process Model | One name contains the other |
| `Operational Risk Heatmap` | Risky Business Process | The Risky Business Process description opens *"An Operational Risk Heatmap that provides a unified view of operational risk…"* |

The third is the strongest of the three — the JSON itself defines Risky Business
Process as being an Operational Risk Heatmap — but the catalogue still lists
them under different names, so they remain distinct nodes here.

The other eight input sources have an empty hint. The bar is deliberately high:
a name merely appearing inside a description does **not** count, because every
description mentions its own inputs and that would flag all of them.

If you decide any of these pairs really is one artifact, the fix is a single
edit to the two `Sources` entries in the JSON, then a regenerate — not a
hand-edit of the CSVs.

## Fidelity

`build_csvs.py` copies values through unchanged; descriptions are byte-identical
to the JSON. The only derived columns are `stated_source_count`,
`referenced_by_count`, `dtosource_count`, `ordinal`, `target_kind` and the two
`possibly_same_as` columns — all of which are counts, positions or the hint
described above.

The build was checked by reconstructing the JSON from the CSVs: all seven
descriptions, names, scores and profile types match exactly, and all seven
`Sources` arrays rebuild in their original order with no dangling endpoints.
