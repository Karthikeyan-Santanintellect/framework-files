# GOLDEN TEMPLATES

Node and relationship CSVs for the DTOM golden policy-template catalogue,
extracted from

```
DTOP-OLD/client/src/assets/docs/knowledgeRepository/info/templateSources.json
```

**31 templates · 485 sources · 18 internal documents · 982 citations · 554 nodes · 1,075 relationships**

The CSVs follow the same convention as the framework folders in this repository:
the first column of a `nodes_<Label>.csv` is `<label>_id`, and every
`rels_<TYPE>.csv` is `source_id,target_id,rel_type` plus any edge properties.

Loaded into Neo4j by [App_new/golden_templates.py](../App_new/golden_templates.py)
under `framework_id = 'GOLDEN_TEMPLATES'` and the anchor label
`:GoldenTemplateNode`.

Regenerate with:

```bash
python "GOLDEN TEMPLATES/build_csvs.py"
```

## Files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Template.csv` | 31 | The 31 golden templates |
| `nodes_Source.csv` | 485 | Every distinct cited source that has a URL |
| `nodes_InternalDocument.csv` | 18 | Every distinct cited entry that has no URL |
| `nodes_Level.csv` | 4 | `L1`, `L2A`, `L2B`, `L2C` |
| `nodes_DomainCode.csv` | 10 | `ENT`, `AIS`, `APS`, `CDR`, `CPS`, `DPP`, `IAM`, `INS`, `PPS`, `TPR` |
| `nodes_ArtifactType.csv` | 6 | `POL`, `PRG`, `PRC`, `PLB`, `DTM`, `DTS` |
| `rels_CITES.csv` | 982 | One row per `Sources` entry, in the order the JSON lists them |
| `rels_HAS_LEVEL.csv` | 31 | Template to its level |
| `rels_IN_DOMAIN.csv` | 31 | Template to its domain code |
| `rels_HAS_ARTIFACT_TYPE.csv` | 31 | Template to its artifact type |

## Shape

```
                     ┌──HAS_LEVEL─────────> Level (4)
Template (31) ───────┼──IN_DOMAIN─────────> DomainCode (10)
      │              └──HAS_ARTIFACT_TYPE─> ArtifactType (6)
      │
      ├──CITES {ordinal, accessed_date}──> Source (485)            [has a URL]
      └──CITES {ordinal}─────────────────> InternalDocument (18)   [no URL]
```

## Citations are parsed, not stored whole

The 31 templates list 982 sources between them, 509 of them distinct. They come
in two shapes:

**491 are structured citations** — `<Title>, accessed <Date>, <<URL>>` — for
example:

```
NIST Cybersecurity Framework (CSF) 2.0, accessed March 9, 2026,
<https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>
```

These become **485** `Source` nodes keyed on `(title, URL)`. The accessed date
is not part of the key: five sources were accessed on two different dates by
different templates, and they are one source, not two. The date therefore lives
on the `CITES` edge, and the node carries `first_accessed` / `last_accessed`.

**18 have no URL** and become `InternalDocument` nodes — 17 DTOM `.docx` files
plus one malformed entry (below).

Both node types keep the citation string exactly as the JSON writes it, and
every `CITES` edge keeps its `ordinal` and its `stated_source_text`. The
original `Sources` arrays therefore rebuild verbatim from the CSVs.

## `</div>` — the one malformed entry

One "source" is the literal string `</div>`. It is cited by four templates, and
in every one of them it is the **last** entry in the array, which makes it a
scraping artifact rather than a citation.

It is **kept, not dropped**, as an `InternalDocument` with `is_malformed = true`
and a `note` explaining why. Dropping it would have made the JSON's own
`SourceCount` stop reconciling for those four templates (42→41, 13→12, 43→42,
29→28). Keeping it means `sum(SourceCount) == 982 == the CITES edge count`,
which the build script asserts.

```cypher
// exclude it
MATCH (t:Template {framework_id:'GOLDEN_TEMPLATES'})-[:CITES]->(n)
WHERE NOT coalesce(n.is_malformed, false)
RETURN t.template_id, count(n);
```

It is the only `InternalDocument` whose `text` does not end in `.docx`, so it is
easy to spot either way.

## Node identifiers

| Label | `<label>_id` | Example |
|---|---|---|
| Template | the catalogue's own `TemplateId`, verbatim | `DTOM-L2A-DPP-POL-006` |
| Source | `src_<sha1(title\|url)[:12]>` | `src_afeaaa8353db` |
| InternalDocument | `doc_<slug(text)>` | `doc_dtom_contextual_architecture_for_programs_docx` |
| Level | `level_<slug(code)>` | `level_l2a` |
| DomainCode | `domaincode_<slug(code)>` | `domaincode_dpp` |
| ArtifactType | `artifacttype_<slug(code)>` | `artifacttype_pol` |

`Template` has a natural key already, so it is used as-is. `Source` titles run
to well over a hundred characters and are not unique against their URLs on their
own, so the key is content-addressed over both. All 554 ids are unique across
every label, which the build script asserts — that matters because the loader
merges on `(framework_id, node_id)` under a single anchor label and the
`rels_*.csv` files record no endpoint labels.

## The TemplateId decomposes; the TemplatePath does not

Every `TemplateId` splits cleanly:

```
DTOM - L2A - DPP - POL - 006
       │     │     │     └── sequence
       │     │     └──────── artifact type
       │     └────────────── domain code
       └──────────────────── level
```

All four parts are stored as properties on `Template` **and** modelled as nodes
and edges, so templates can be grouped either way.

`TemplatePath` is a different matter and is **stored verbatim, never derived**.
For 22 templates the directory matches the id prefix, but the **nine `L2A`
templates all sit in a `DTOM-L2A-ENT-DTOM` directory** that matches none of
their ids:

```
actual   .../templates/DTOM-L2A-ENT-DTOM/DTOM-L2A-DPP-POL-006 - Data Privacy… .md
implied  .../templates/DTOM-L2A-DPP-POL/DTOM-L2A-DPP-POL-006 - Data Privacy… .md
```

All 31 paths were checked against the DTOP-OLD working tree and **all 31 files
exist** at the path the JSON gives, so the JSON is right and the id prefix is
simply not the directory name.

## `possibly_maps_to` — read this before using it

Eight of the ten domain codes look like they name a domain from the
[DTOP Catalogs](../DTOP%20Catalogs/) catalogue. Rather than silently linking the
two catalogues, the suspicion is recorded in two columns on `DomainCode`.
**`possibly_maps_to` is a hint for a human. It is not a relationship, and
nothing in the CSVs or the loader treats it as one** — this catalogue stays
disconnected from every other one, as they all are.

| Code | `possibly_maps_to` |
|---|---|
| `APS` | Application & Product Security |
| `CDR` | Cyber Defense & Resilience |
| `CPS` | Cloud & Platform Security |
| `DPP` | Data Privacy & Protection |
| `IAM` | Identity and Access Management |
| `INS` | Infrastructure & Network Security |
| `PPS` | Personnel & Physical Security |
| `TPR` | Third-Party Risk Management |

The bar is deliberately high, and exactly one thing counts as evidence: **the
three-letter code is the initials of the first three significant words of a DTOP
Catalogs domain name**, matching exactly one domain. Nothing else qualifies —
topical resemblance does not, because almost every code resembles some domain.

Two codes come out blank, both correctly:

- **`ENT`** is *Enterprise*. It is the domain code for 22 of the 31 templates
  and corresponds to no single domain at all.
- **`AIS`** — *AI Safety & Security* — is very probably the catalogue's *AI &
  Emerging Technology Security*, but it fails the test: those initials are
  `AET`, not `AIS`. It is left blank rather than asserted on a hunch. **This is
  the one hint most likely to be right and missing.**

Note also that the codes and the domain names are not written identically even
where they clearly correspond: the template says *Cyber Defence and Resilience*,
the catalogue *Cyber Defense & Resilience*. Any future merge has to reckon with
that, which is another reason it is a hint and not an edge.

If you decide any of these pairs really is one thing, the fix belongs in the
source JSON, not in a hand-edit of the CSVs.

## Columns

**`nodes_Template.csv`** — `template_id`, `name`, `level`, `domain_code`,
`artifact_type`, `sequence`, `template_path`, `stated_source_count`,
`cited_source_count`, `cited_internal_document_count`, `source_document`. The
last two split `stated_source_count` by target kind and always sum to it.

**`nodes_Source.csv`** — `source_id`, `title`, `url`, `host`, `verbatim`,
`template_count`, `first_accessed`, `last_accessed`, `source_document`. `host`
is derived from the URL. `first_accessed` and `last_accessed` are ISO dates held
as strings so they sort lexically, and are equal for all but five sources.

**`nodes_InternalDocument.csv`** — `internaldocument_id`, `text`,
`is_malformed`, `note`, `template_count`, `source_document`.

**`nodes_Level.csv` / `nodes_DomainCode.csv` / `nodes_ArtifactType.csv`** —
`<label>_id`, `code`, `template_count`, `source_document`, plus the two
`possibly_maps_to` columns on `DomainCode`. **No expanded names are invented**:
the JSON never states what `POL`, `PRG`, `DTM` or `DTS` stand for, so only the
code is recorded.

**`rels_CITES.csv`** — `target_kind` is `Source` or `InternalDocument`, so the
two can be separated without a join. `ordinal` preserves the position within the
JSON's `Sources` array and `stated_source_text` records the entry exactly as
written. `accessed_date` (ISO) and `accessed_date_stated` (verbatim, e.g.
`March 9, 2026`) are blank for `InternalDocument` targets, which carry no date.

## Distributions

**Templates by artifact type** — `POL` 13, `PRG` 7, `PRC` 5, `PLB` 4, `DTM` 1,
`DTS` 1. **By level** — `L1` 4, `L2A` 9, `L2B` 9, `L2C` 9. **By domain code** —
`ENT` 22, and one each for the other nine.

**Citations per template** range from 13 (Regulatory Engagement Playbook) to 55
(Cloud and Platform Security), 982 in total.

**Source reuse** — 430 of the 485 sources are cited by exactly one template. The
most reused are cited by 18 templates each: NIST CSF 2.0, NIST SP 800-53 Rev. 5,
GDPR, the COSO ERM Framework and the OECD Principles of Corporate Governance.
Among the internal documents, *DTOM Contextual Architecture for Programs.docx*
is cited by 6.

**Publishers** — 324 distinct hosts. The corpus leans on NIST above all
(`csrc.nist.gov` 26 citations, `nvlpubs.nist.gov` 13), then
`learn.microsoft.com` 15 and `www.paloaltonetworks.com` 10.

**Accessed dates** — four crawl dates: 2025-12-14 (297 sources), 2025-12-28
(117), 2026-03-09 (50) and 2025-12-13 (21).

## Fidelity

`build_csvs.py` copies values through unchanged. The derived columns are the
`*_count` totals, `host`, `first_accessed` / `last_accessed`, the ISO form of
`accessed_date`, the four `TemplateId` parts, `is_malformed`, and the two
`possibly_maps_to` columns described above. Everything else is verbatim.

The build was checked by reconstructing the JSON from the CSVs: **all 31
templates rebuild byte-identical**, including every `Sources` array in its
original order, every `SourceCount` and every `TemplatePath`. The script asserts
id uniqueness, endpoint resolvability, and that each template's stated
`SourceCount` equals the number of `CITES` edges built for it.

## Queries

```cypher
// One template and everything it cites
MATCH (t:Template {framework_id:'GOLDEN_TEMPLATES', template_id:'DTOM-L1-ENT-POL-001'})
      -[r:CITES]->(n)
RETURN r.ordinal AS ordinal, r.target_kind AS kind,
       coalesce(n.title, n.text) AS source, n.url AS url
ORDER BY ordinal;

// Sources shared by the most templates
MATCH (s:Source {framework_id:'GOLDEN_TEMPLATES'})<-[:CITES]-(t:Template)
WITH s, count(t) AS templates WHERE templates > 10
RETURN s.title, s.url, templates ORDER BY templates DESC;

// Which publishers the corpus leans on
MATCH (s:Source {framework_id:'GOLDEN_TEMPLATES'})
RETURN s.host, count(*) AS sources ORDER BY sources DESC LIMIT 20;

// Templates by artifact type and level
MATCH (t:Template {framework_id:'GOLDEN_TEMPLATES'})
RETURN t.level, t.artifact_type, count(*) AS templates
ORDER BY t.level, t.artifact_type;

// The domain-code hints, and the two that are deliberately blank
MATCH (d:DomainCode {framework_id:'GOLDEN_TEMPLATES'})
RETURN d.code, d.template_count, d.possibly_maps_to, d.possibly_maps_to_basis
ORDER BY d.code;
```
