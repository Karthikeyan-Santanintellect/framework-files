# Assessments and Questionnaires

Node and relationship CSVs for the three assessment question banks that ship
inside the **DTOP-OLD** project, extracted from:

```
client/src/data/sraFullData.json            HIPAA SRA — canonical
client/src/data/sraQuestionsData.json       HIPAA SRA — older question set (superseded)
client/src/data/sraVulnerabilitiesData.json HIPAA SRA — vulnerability stub (superseded)
client/src/data/cri_statements.json         Expert Questionnaire (CRI Profile v2.1)
server/services/agentsV5/llmAssessment/statments/{IdP,XDR,SIEM,HRIS,CSP,DGP}.md   Maturity — canonical
server/services/agentsV5/catalog/{IdP,XDR,SIEM,HRIS,CS,DGP}.csv                   Maturity — csv copies
```

**1,841 nodes · 8,484 relationships** across three assessments.

The CSVs follow the same convention as the other folders in this repository:
the first column of a `nodes_<Label>.csv` is `<label>_id`, and every
`rels_<TYPE>.csv` is `source_id,target_id,rel_type` plus any edge properties.
**Nothing here is loaded into Neo4j** — there is no loader for this folder.

Regenerate with:

```bash
python "Assessments and Questionnaires/build_csvs.py"
```

## The three assessments

| Assessment | Items | Structure |
|---|---:|---|
| HIPAA Security Risk Assessment (SRA) | 125 questions | 7 sections · 484 branching answer options · 40 vulnerabilities · 148 distinct threats |
| Expert Questionnaire (CRI Profile v2.1) | 85 statements | 8 DTOM domains; a curated subset of the maturity banks |
| Maturity Assessment | 688 statements | 6 domain banks (IdP, XDR, SIEM, HRIS, CSP, DGP) |

## Node files

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Assessment.csv` | 3 | The three assessments, with item counts, UI components and routes |
| `nodes_DataSource.csv` | 16 | Every source file, canonical and superseded |
| `nodes_Section.csv` | 7 | SRA sections |
| `nodes_Question.csv` | 125 | SRA questions, keyed by section |
| `nodes_AnswerOption.csv` | 484 | SRA answer options with their education text, framework references and `next` branch |
| `nodes_Vulnerability.csv` | 40 | SRA vulnerabilities |
| `nodes_Threat.csv` | 148 | Distinct SRA threat descriptions (206 uses deduplicated) |
| `nodes_ReferencedFramework.csv` | 4 | HIPAA, NIST CSF, HPH CPG, HICP — cited by every SRA option |
| `nodes_Domain.csv` | 14 | 8 CRI DTOM domains + 6 maturity domains |
| `nodes_Statement.csv` | 773 | 85 CRI + 688 maturity diagnostic statements |
| `nodes_Subcategory.csv` | 110 | CRI Profile v2.1 subcategory paths, shared by both statement sets |
| `nodes_SubjectTag.csv` | 106 | Maturity subject hashtags |
| `nodes_SupersededText.csv` | 11 | Prior wording of the 11 SRA questions that changed |

## Relationship files

| File | Rows | Meaning |
|---|---:|---|
| `rels_HAS_SECTION.csv` | 7 | Assessment → Section |
| `rels_HAS_QUESTION.csv` | 125 | Section → Question |
| `rels_HAS_OPTION.csv` | 484 | Question → AnswerOption |
| `rels_LEADS_TO.csv` | 439 | AnswerOption → next Question (branching flow; 45 options end the section) |
| `rels_HAS_VULNERABILITY.csv` | 40 | Section → Vulnerability |
| `rels_HAS_THREAT.csv` | 206 | Vulnerability → Threat |
| `rels_CITES.csv` | 1,936 | AnswerOption → ReferencedFramework, with the citation text on the edge |
| `rels_HAS_DOMAIN.csv` | 14 | Assessment → Domain |
| `rels_HAS_STATEMENT.csv` | 773 | Domain → Statement |
| `rels_IN_SUBCATEGORY.csv` | 773 | Statement → Subcategory |
| `rels_TAGGED.csv` | 3,334 | Statement → SubjectTag (maturity only) |
| `rels_ALSO_IN.csv` | 315 | CRI Statement → maturity Statement(s) sharing its statement id |
| `rels_SOURCED_FROM.csv` | 14 | Assessment → DataSource |
| `rels_SUPERSEDES.csv` | 2 | Canonical SRA source → the older question set and the vulnerability stub |
| `rels_HAD_PRIOR_TEXT.csv` | 11 | Question → SupersededText |
| `rels_FROM_SOURCE.csv` | 11 | SupersededText → the older DataSource |

## Four decisions the data forced

### 1. SRA question ids are section-scoped

`Q1` is a different question in every section — there are 125 questions but only
30 distinct ids. Questions are therefore keyed by **(section, id)**
(`sra_s1_q1`, `sra_s2_q1`, …), and each option's `next` value is resolved to a
question **within the same section**. 439 options branch to another question; 45
end the section (`next = END`).

### 2. Maturity is the union of the .md and .csv copies

The 6 `.md` banks are canonical; the `catalog/*.csv` copies drift from them by
1–5 statements each (17 statements are csv-only across all six). Rather than pick
one or duplicate everything, each statement is **one node flagged `in_md` /
`in_csv`**:

| | Statements |
|---|---:|
| in both .md and .csv | 654 |
| .md only | 17 |
| .csv only | 17 |
| **total maturity** | **688** |

Query `in_md = false` or `in_csv = false` to see exactly where the two copies
disagree. (The CSP domain's csv copy is the file `catalog/CS.csv`; every other
domain's two files share a name.)

### 3. The Expert Questionnaire is a real subset of the maturity banks

All 85 CRI statement ids also occur among the maturity statements — the
"curated subset" described in the project. That overlap is not asserted in
prose only; it is emitted as **315 `ALSO_IN` edges** from each CRI statement to
every maturity statement sharing its id (an id recurs across domains, so 85
statements produce 315 edges). Both statement sets also point at the **same 110
`Subcategory` nodes** — all 31 CRI subcategories are among them — so the shared
CRI Profile v2.1 taxonomy is one set of nodes, not two.

### 4. The two superseded SRA files are kept as history, not duplicates

`sraFullData.json` is canonical. The older `sraQuestionsData.json` and the
`sraVulnerabilitiesData.json` stub are modelled as `DataSource` nodes that the
canonical source `SUPERSEDES`. The only content carried forward from the older
file is the **11 questions whose wording changed**, as `SupersededText` nodes
linked to the current question by `HAD_PRIOR_TEXT`. The other ~113 identical
questions are not duplicated.

## Fidelity

`build_csvs.py` copies text through unchanged — question, option, statement,
threat and education text are verbatim. The only derived values are counts,
the `in_md` / `in_csv` flags, and deterministic ids (a slug, or an md5 prefix
for deduplicated threats and subcategories).

The build was checked by reconstructing each source from the CSVs: all 125 SRA
questions, 484 options, 40 vulnerabilities, 85 CRI statements and the 688
maturity statements match their sources, the presence split reconciles
(654 + 17 + 17), every `ALSO_IN` edge links a genuinely shared statement id,
and there are no dangling relationship endpoints across any of the 16
relationship files.

## Differences from the other source folders

`DTOP Sources/` and `Enterprise Sources/` are flat source catalogues. This
folder is deeper: it models the **internal structure** of each assessment —
sections, branching questions and answer options, vulnerabilities and threats,
diagnostic statements and their shared taxonomy — so it has more node labels
(13) and relationship types (16) than either catalogue.
