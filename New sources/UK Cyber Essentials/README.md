# UK Cyber Essentials — Requirements for IT Infrastructure v3.3

**Source document:** `KB 2/Europe/cyber-essentials-requirements-for-it-infrastructure-v3-3.pdf`
**Publisher:** NCSC (National Cyber Security Centre)
**Version:** v3.3
**Effective / publication date:** April 2026 (the date stamped on every page footer and in the copyright line: "All material is UK Crown Copyright. April 2026")
**Copyright:** All material is UK Crown Copyright.

## Schema

The schema mirrors the scheme's own structure rather than a generic controls template. The
document is organised as lettered sections A–F, with section E holding the **five technical
control themes**; each theme carries an "Applies to" asset list, an **Aim**, an **Introduction**
and a **Requirements** block of bulleted obligation statements. Scope (section D) is likewise
a set of numbered sub-topics (i)–(vii) containing scoping rules. Both are extracted at
clause level.

### Node types

| File | Node type | Rows | What it holds |
|---|---|---:|---|
| `nodes_Instrument.csv` | Instrument | 1 | The publication itself: title, version, publisher, effective date, copyright |
| `nodes_Section.csv` | Section / Subsection | 17 | Lettered sections A–F, plus D's scope subsections (overview, asset management, (i)–(vii)) and F's zero-trust subsection |
| `nodes_ControlTheme.csv` | ControlTheme | 5 | The five technical control themes, each with its verbatim `applies_to` list and `aim` |
| `nodes_Clause.csv` | Clause | 166 | Every requirement statement, scope rule, definition-adjacent prose and bullet, verbatim, with `clause_ref`, `heading`, `obligation_type` (mandatory / recommended / informative) and page |
| `nodes_Definition.csv` | Definition | 14 | Every defined term in section B with its verbatim definition |
| `nodes_CloudServiceModel.csv` | CloudServiceModel | 3 | IaaS, PaaS, SaaS with the document's own description and example services |
| `nodes_AssetType.csv` | AssetType | 12 | Distinct asset types named across the five "Applies to" lists |
| `nodes_Role.csv` | Role | 8 | The person-roles in Table 2 (Employee … Customer) |
| `nodes_OwnershipCategory.csv` | OwnershipCategory | 3 | Table 2 columns: owned by your organisation / owned by a third party / BYOD |
| `nodes_Threshold.csv` | Threshold | 12 | Every numeric threshold and deadline the document states (14 days, CVSS v3 ≥ 7, 10 guesses in 5 minutes, 6/8/12 character minimums, three random words) |

### Relationship types

| File | Rel type | Rows |
|---|---|---:|
| `rels_section_part_of.csv` | PART_OF (subsection → section) | 10 |
| `rels_theme_part_of_section.csv` | PART_OF (theme → section E) | 5 |
| `rels_clause_contained_in.csv` | CONTAINED_IN (clause → section or theme) | 166 |
| `rels_clause_subclause_of.csv` | SUBCLAUSE_OF (bullet → parent clause) | 69 |
| `rels_defines.csv` | DEFINES (section B → definition) | 14 |
| `rels_applies_to_asset.csv` | APPLIES_TO (theme → asset type) | 43 |
| `rels_cloud_responsibility.csv` | IMPLEMENTED_BY (theme → cloud model, with `responsible_party`) — Table 1 | 15 |
| `rels_device_scope.csv` | DEVICE_SCOPE (role → ownership category, with `scope_status`) — Table 2 | 24 |
| `rels_cross_reference.csv` | CROSS_REFERENCES (clause → clause / definition / theme) | 11 |
| `rels_threshold_stated_in.csv` | STATED_IN (threshold → clause) | 12 |

## Design notes

- **Clause granularity.** Each bullet in a "Requirements" list is its own row and is linked to
  its lead-in sentence via `SUBCLAUSE_OF`; nested sub-bullets (e.g. firewall admin-interface
  protection options, the CVSS conditions, the password-quality options) are a third level.
- **`obligation_type`** is derived from the modal verb actually used in the clause ("must" →
  mandatory, "should"/"we recommend" → recommended, otherwise informative). It is a
  classification of the verbatim text, not added content.
- **Tables** are modelled as relationships with a property rather than as prose, so Table 1
  (shared responsibility per cloud model) and Table 2 (device scope per role/ownership) are
  queryable. Table 2's tick/cross glyphs are rendered using the document's own key
  ("✓ In scope ✘ Out of scope"); `N/A` is kept where the source prints N/A.

## Caveats and gaps

- This is the **requirements document** for the Cyber Essentials scheme, not a statute; it
  contains no penalties, offences or enforcement provisions, so no such nodes exist.
- **Figure 1** ("Scope of the requirements for IT infrastructure", page 8) is an image with no
  extractable text in the `pdftotext` output; only its caption exists in the source. It is not
  represented beyond that.
- Section E's per-theme "Applies to" lists are captured verbatim on the ControlTheme node and
  also normalised into `AssetType` nodes; casing differs between themes in the source
  (e.g. "Servers" in theme 5 vs "servers" elsewhere) and asset ids are normalised
  case-insensitively, with the exact per-theme wording preserved in the `as_stated` column.
- The Cyber Essentials Plus / assessment-question material is not part of this document and is
  therefore absent.

## Validation

A validation script parsed every CSV, asserted node-id uniqueness within each file, and asserted
that all 241 relationship endpoints resolve to a node id: **0 errors**.
