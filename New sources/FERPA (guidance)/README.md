# FERPA — U.S. Department of Education guidance (knowledge-graph CSVs)

## ⚠️ CRITICAL: this is NOT the FERPA statute and NOT the FERPA regulations

Everything in this folder is extracted from **two U.S. Department of Education, Student Privacy
Policy Office (SPPO) guidance documents** about FERPA. Neither the FERPA statute
(**20 U.S.C. § 1232g**) nor the FERPA regulations (**34 CFR Part 99**) is present in this
knowledge base, and no part of either has been reproduced or reconstructed here.

SPPO-21-04 states this expressly on its face:

> "Other than statutory and regulatory requirements included in the document, the contents of this
> guidance do not have the force and effect of law and are not meant to bind the public. This
> document is intended only to provide clarity to the public regarding existing requirements under
> the law or agency policies."

SPPO-23-01 carries no such disclaimer in its text but is likewise SPPO guidance, not the law.

Accordingly:
- Every reference the guides make to the statute or to Part 99 is modelled as an
  **`ExternalReference` node**, each flagged `NOT PRESENT IN THIS KNOWLEDGE BASE — external
  reference only`. No underlying statutory or regulatory text has been invented.
- Any question that turns on the exact wording of 20 U.S.C. § 1232g or 34 CFR Part 99 **cannot be
  answered from this graph**; it must be answered against the primary sources.
- The `status_caveat` column on both `Document` nodes repeats this warning.

## Source documents

| document_id | Designation | Title | Issued | PDF |
|---|---|---|---|---|
| `DOC-PG` | SPPO-21-04 | A Parent Guide to the Family Educational Rights and Privacy Act (FERPA) | July 9, 2021 | `KB 2/USA/A parent guide to ferpa_508.pdf` |
| `DOC-ES` | SPPO-23-01 | An Eligible Student Guide to the Family Educational Rights and Privacy Act (FERPA) | March 8, 2023 | `KB 2/USA/Family Educational Rights and Privacy Act.pdf` |

Each guide is modelled as its own document node with its own section and clause tree, so the
parent-facing and eligible-student-facing statements of the same rule are never conflated.

## Schema and why

The guides are not statutes, so a Part/Article schema would misrepresent them. They are short
narrative guidance with a stable shape: an unnumbered heading structure, a bulleted "rights"
list, a "Disclosure" section whose sub-headings are the named consent exceptions, a bulleted
"Other Exceptions" list, and closing sections on annual notification and complaints. The schema
follows exactly that, using the documents' own vocabulary.

**Node types**

| Type | Meaning |
|---|---|
| `Document` | One SPPO guide, with issuing body, date, audience, force-of-law statement, status caveat |
| `Section` | A heading or sub-heading of a guide (`level`, `parent_section_id`) |
| `Clause` | The extraction unit — one paragraph, numbered condition, or bullet, verbatim, with page |
| `Right` | A right the guides describe (inspect and review, seek amendment, consent to disclosure, file a complaint, hearing, insert statement, opt out of directory information, annual notification) |
| `DisclosureException` | An exception to the general consent requirement — the four named ones plus each enumerated "other" exception |
| `Definition` | A term the guides quote or gloss, with its verbatim wording |
| `ExternalReference` | Law cited but **not present here** (FERPA statute, 34 CFR Part 99, IDEA provisions, IRC § 152, HEA title IV) |
| `Resource` | A URL or postal address the guides point readers to |

**Relationship types:** `HAS_SECTION`, `HAS_SUBSECTION`, `HAS_CLAUSE`, `DESCRIBES_RIGHT`,
`DESCRIBES_EXCEPTION`, `HAS_CONDITION` (exception/right → its enumerated conditions),
`DEFINES_TERM`, `CITES_EXTERNAL`, `LINKS_TO`, `COVERS_RIGHT` (document → right),
`CORRESPONDS_TO` (parallel clause in the other guide — audience-adapted wording of the same rule).

## Files and row counts

| File | Rows (excl. header) |
|---|---|
| `nodes_Document.csv` | 2 |
| `nodes_Section.csv` | 27 |
| `nodes_Clause.csv` | 71 |
| `nodes_Right.csv` | 8 |
| `nodes_DisclosureException.csv` | 14 |
| `nodes_Definition.csv` | 10 |
| `nodes_ExternalReference.csv` | 7 |
| `nodes_Resource.csv` | 12 |
| `rels_HAS_SECTION.csv` | 11 |
| `rels_HAS_SUBSECTION.csv` | 16 |
| `rels_HAS_CLAUSE.csv` | 71 |
| `rels_DESCRIBES_RIGHT.csv` | 27 |
| `rels_DESCRIBES_EXCEPTION.csv` | 26 |
| `rels_HAS_CONDITION.csv` | 14 |
| `rels_DEFINES_TERM.csv` | 19 |
| `rels_CITES_EXTERNAL.csv` | 21 |
| `rels_LINKS_TO.csv` | 20 |
| `rels_CORRESPONDS_TO.csv` | 31 |
| `rels_COVERS_RIGHT.csv` | 16 |

Totals: **151 nodes**, **272 relationships** across 8 node files and 11 relationship files.

## Stated thresholds and deadlines (as the guides state them)

- Inspect and review: "not more than 45 calendar days following receipt of a request".
- Complaint filing: "within 180 days of the date of the alleged violation or of the date that the
  parent knew or reasonably should have known of the alleged violation".
- Rights transfer: "When a student reaches 18 years of age or attends an institution of
  postsecondary education at any age".
- Alcohol/controlled-substance parental notification (SPPO-23-01 only): "the student is under 21
  years of age at the time of the disclosure to the parent".
- Dually enrolled students: parents retain rights over high-school records "if the student is
  under the age of 18 years".

No penalties are stated in either guide.

## Caveats and gaps

1. **Guidance, not law.** See the warning at the top. The statute and 34 CFR Part 99 are absent.
2. **No Q&A structure was found.** Both guides are prose with headings and bullets; neither is
   organised as questions and answers, so no `Question`/`Answer` node type was created.
3. **The two guides differ substantively**, not only in audience. Differences preserved in the data:
   - SPPO-23-01 adds a paragraph on academic transcripts and copies (`ES-C2.1.2`), a statement that
     a school may withhold PII if the student owes money (`ES-C2.3.1`), and four further "other"
     exceptions (financial aid; victim notification of disciplinary results; final results to any
     third party; alcohol/controlled-substance notification to parents) not in SPPO-21-04.
   - SPPO-21-04 adds IDEA/IEP-specific amendment guidance (`PG-C2.2.2`) and two "other" exceptions
     (child welfare/foster care; juvenile justice) not in SPPO-23-01.
   - "Other Exceptions" bullets with no counterpart carry no `CORRESPONDS_TO` edge.
4. **Definitions are glosses, not regulatory definitions.** The guides paraphrase or partially quote
   the regulatory definitions ("generally defined as…", "The FERPA regulations define…"). The
   `verbatim_definition` field is verbatim to the *guide*, not to 34 CFR § 99.3.
5. **"Directory information" is illustrative.** The list is introduced with "may include information
   such as" — it is not exhaustive and is not a designation any school has made.
6. **Exception lists are expressly non-exhaustive** — "include, but are not limited to" — and the
   guides state conditions are omitted: "Provided certain conditions are met that are not included
   in the summary below".
7. **Source text quality.** Both files are clean `pdftotext -layout` extracts with no OCR noise.
   Page headers/footers and running page numbers were removed and wrapped lines rejoined; wording,
   including the source's curly quotation marks, is preserved exactly. `source_page` records the
   PDF page(s) each clause spans.
8. **Rights nodes are cross-document.** A `Right` node carries `verbatim_basis` quoted from
   SPPO-21-04 (parent phrasing); the eligible-student phrasing of the same right lives on the
   corresponding `ES-` clause reached via `DESCRIBES_RIGHT`.

## Validation

`check_ferpa.py` parsed every CSV and asserted: node id column naming, presence of
`source_document` on every node file, uniqueness of every node id within its file,
`source_id,target_id,rel_type` as the first three relationship columns, no duplicate edges, and
resolution of every relationship endpoint to a node id. **Result: 0 errors.**
