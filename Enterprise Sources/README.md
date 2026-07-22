# Enterprise Sources

Node and relationship CSVs for the enterprise source catalogue, extracted from

```
DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json
```

**114 enterprise sources · 55 web resources · 3 profile types · 181 relationships**

The CSVs follow the same convention as the framework folders in this repository:
the first column of a `nodes_<Label>.csv` is `<label>_id`, and every
`rels_<TYPE>.csv` is `source_id,target_id,rel_type` plus any edge properties.

Regenerate with:

```bash
python "Enterprise Sources/build_csvs.py"
```

## Files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_EnterpriseSource.csv` | 114 | Every entry in `EnterpriseSources`, in file order |
| `nodes_WebResource.csv` | 55 | Each distinct non-null `URL` |
| `nodes_ProfileType.csv` | 3 | `Business`, `Security`, `Technology` |
| `rels_HAS_PROFILE_TYPE.csv` | 114 | Each source to its profile type |
| `rels_AVAILABLE_AT.csv` | 67 | Each source to the URL it points at |

## What the catalogue looks like

| Profile type | Sources |
|---|---:|
| Security | 40 |
| Business | 38 |
| Technology | 36 |

`ReputationScore` runs 5–10 and is, unlike the DTOP catalogue, genuinely
varied: 5 (3), 6 (12), 7 (30), 8 (27), 9 (35), 10 (7).

**47 of the 114 have no URL** and therefore no `AVAILABLE_AT` edge. That is the
source data, not a gap in extraction — those entries name a kind of source
("Reputable Breach Databases", "Industry Analyst Reports") rather than a
specific page.

## Two collisions in the source data

Both are real and are handled explicitly rather than smoothed over.

### `SourceName` is not unique

**"Reputable Breach Databases" appears twice, and the two are different
entries** — different URL, description and profile type:

| id | Profile | URL | Description |
|---|---|---|---|
| `es_reputable_breach_databases` | Technology | *(none)* | Breach tracking and incident databases |
| `es_reputable_breach_databases_2` | Security | haveibeenpwned.com | Have I Been Pwned, Privacy Rights Clearinghouse, Identity Theft Resource Center |

They are kept as two nodes. Ids get a numeric suffix on collision, in file
order, so the other 113 keep a clean slug. Both rows carry
`name_is_duplicated = true` so the situation is visible without a group-by.

Note the consequence: **matching a source by `source_name` can return two
nodes.** Match on `enterprisesource_id` when you need exactly one.

### Nine URLs are shared by several sources

67 entries carry a URL but only 55 URLs are distinct. The same page is
catalogued repeatedly under different names, usually one per profile type:

| Shared URL | Sources pointing at it |
|---|---|
| sec.gov EDGAR company search | SEC EDGAR · SEC Item 1C Disclosures · SEC Cybersecurity Disclosures |
| cisa.gov advisories | National CERT Advisories · National CERT/CISA Advisories · CISA Advisories and Alerts |
| iso.org | ISO 27001/27701 Directories · ISO Certifications · ISO 27001 Certified Organization Directories |
| usaspending.gov | USASpending.gov · USASpending.gov (Technology) |
| linkedin.com | LinkedIn · LinkedIn (Security Leadership) |
| glassdoor.com | Glassdoor · Glassdoor (Security Culture) |
| gsa.gov | Government Procurement Portals · GSA Schedules and Contracts |
| aicpa.org | SOC 2 Attestations · SOC 2 Attestations (AICPA) |
| ocrportal.hhs.gov breach report | Sector Breach Portals · HHS Breach Notifications |

Each distinct URL is one `WebResource` node, so those groups are visible as
shared structure — this is the only real connectivity in the dataset, since
these entries have no dependency list. It is a factual join on identical
strings, not an interpretation: no attempt is made to decide whether
"SEC EDGAR" and "SEC Item 1C Disclosures" are *really* the same thing.

The URL also stays as a column on `nodes_EnterpriseSource.csv` and on the
`AVAILABLE_AT` edge, so the common case needs no join. `shared_with_others` on
the edge and `referenced_by_count` on the resource both flag the sharing.

## Columns

**`nodes_EnterpriseSource.csv`** — `enterprisesource_id`, `source_name`, `url`,
`description`, `reputation_score`, `profile_type`, `name_is_duplicated`,
`source_document`. A `null` URL is written as an empty string. `profile_type`
is duplicated onto the node as well as modelled as an edge, so the CSV stands
alone.

**`nodes_WebResource.csv`** — `webresource_id`, `url`, `referenced_by_count`,
`source_document`. The id is derived from the host and path.

**`rels_AVAILABLE_AT.csv`** — carries `url` and `shared_with_others`.

## Fidelity

`build_csvs.py` copies values through unchanged. The only derived columns are
`referenced_by_count`, `enterprisesource_count`, `name_is_duplicated` and
`shared_with_others` — all counts or flags computed from the data itself.

The build was checked by reconstructing the JSON from the CSVs and comparing it
to the original: **all 114 entries match on every field, in file order**, with
no dangling endpoints.

## Differences from `DTOP Sources/`

The two catalogues have the same field names but a different shape, so the CSVs
differ:

* Enterprise entries have **no `Sources` array**, so there is no `DERIVED_FROM`
  edge and no dependency graph between them.
* Enterprise `URL`s are mostly populated (67 of 114) where every DTOP `URL` is
  `null`, which is why `WebResource` exists here and not there.
* Enterprise `ReputationScore` varies 5–10; every DTOP score is 9.
