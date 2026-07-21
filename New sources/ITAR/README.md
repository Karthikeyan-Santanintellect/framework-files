# ITAR — 22 CFR Parts 120–130 — knowledge-graph CSVs

**Source document:** International Traffic in Arms Regulations (ITAR), 22 C.F.R. Chapter I,
Subchapter M, Parts 120–130, amended through 2 October 2025 (`KB 2/USA/ITAR.pdf`; extracted with
`pdftotext -layout`). The PDF is the Export Compliance Training Institute's unofficial searchable
compilation of the official CFR text; the regulatory text itself is reproduced verbatim.

All text in these CSVs is taken verbatim from that source. Where a paragraph was split across a
page break, the fragments were rejoined with a single space; no wording was added, paraphrased or
supplied from outside the document.

## Schema

The schema follows the instrument's own vocabulary: Part → Subpart → Section → Clause, with the
U.S. Munitions List modelled separately because it is an enumerated list rather than prose.

### Node types

| File | Type | What it is |
|---|---|---|
| `nodes_Part.csv` | `Part` | The 11 parts (120–130), with each part's `Authority` and `Source` notes. |
| `nodes_Subpart.csv` | `Subpart` | Part 120's Subparts A–C (General Information / General Policies and Processes / Definitions). |
| `nodes_Section.csv` | `Section` | Every `§ x.y` section, including `[Reserved]` sections and reserved ranges (`section_number_end`). `lead_text` holds undesignated lead-in prose. |
| `nodes_Clause.csv` | `Clause` | Every lettered/numbered subdivision of a section — (a), (a)(1), (a)(1)(i), (a)(1)(i)(A) — with `clause_path`, `label`, `level`, verbatim `text`, `parent_id`. |
| `nodes_USMLCategory.csv` | `USMLCategory` | The 21 USML categories (I–XXI) of § 121.1. |
| `nodes_USMLEntry.csv` | `USMLEntry` | Every enumerated USML paragraph/sub-paragraph, nested up to 7 levels, flagged `significant_military_equipment` (source asterisk, per § 120.10(c)) and `mtcr_annex` (trailing “(MT)”, per § 120.10(d)). |
| `nodes_Definition.csv` | `Definition` | Defined terms: each section of Part 120 Subpart C (§§ 120.30–120.69), the term list in § 121.0, and the Part 130 definition sections (§§ 130.2–130.8), with full verbatim definition text. These are the operative definitions for the whole regime (defense article, defense service, technical data, export, release, etc.). |
| `nodes_Note.csv` | `Note` | Every “Note N to paragraph …”, “Note to Category …”, editorial/effective-date note, and the two country tables of § 126.1 (`note_kind = table`), attached to the node they follow. |
| `nodes_SupplementEntry.csv` | `SupplementEntry` | Rows of Supplement No. 1 to Part 126 (exclusions from the Canadian/Australian/UK exemptions, with the per-column X flags) and Supplement No. 2 (Excluded Technology List for § 126.7). |

Violations and penalties (Part 127), administrative procedures (Part 128), brokering (Part 129) and
political contributions/fees (Part 130) are carried at clause level in `nodes_Clause.csv` under their
sections — e.g. § 127.1 Violations, § 127.3 Penalties for violations, § 127.10 Civil penalty,
§ 127.12 Voluntary disclosures. Monetary thresholds, deadlines and fee tiers appear inside the
verbatim clause text (e.g. registration fee tiers in § 122.3, the $500,000 / $100,000 / $5,000
thresholds in Part 130, the $50,000,000 / $200,000,000 major-defense-equipment thresholds in
§ 120.37).

### Relationship types

| File | Rel | Endpoints |
|---|---|---|
| `rels_HAS_SUBPART.csv` | `HAS_SUBPART` | Part → Subpart |
| `rels_HAS_SECTION.csv` | `HAS_SECTION` | Part/Subpart → Section |
| `rels_HAS_CLAUSE.csv` | `HAS_CLAUSE` | Section → Clause, Clause → Clause |
| `rels_HAS_CATEGORY.csv` | `HAS_CATEGORY` | § 121.1 → USMLCategory |
| `rels_HAS_ENTRY.csv` | `HAS_ENTRY` | USMLCategory → USMLEntry, USMLEntry → USMLEntry |
| `rels_DEFINES.csv` | `DEFINES` | Section → Definition |
| `rels_HAS_NOTE.csv` | `HAS_NOTE` | Part/Section/Clause/Category/USMLEntry → Note |
| `rels_HAS_SUPPLEMENT_ENTRY.csv` | `HAS_SUPPLEMENT_ENTRY` | Part 126 → SupplementEntry |
| `rels_CROSS_REFERENCES.csv` | `CROSS_REFERENCES` | any node → Section or USMLCategory it cites (`target_kind` column) |

## Row counts

| File | Rows |
|---|---|
| nodes_Part.csv | 11 |
| nodes_Subpart.csv | 3 |
| nodes_Section.csv | 194 |
| nodes_Clause.csv | 1519 |
| nodes_USMLCategory.csv | 21 |
| nodes_USMLEntry.csv | 1181 |
| nodes_Definition.csv | 48 |
| nodes_Note.csv | 250 |
| nodes_SupplementEntry.csv | 126 |
| rels_HAS_SUBPART.csv | 3 |
| rels_HAS_SECTION.csv | 194 |
| rels_HAS_CLAUSE.csv | 1519 |
| rels_HAS_CATEGORY.csv | 21 |
| rels_HAS_ENTRY.csv | 1181 |
| rels_DEFINES.csv | 48 |
| rels_HAS_NOTE.csv | 250 |
| rels_HAS_SUPPLEMENT_ENTRY.csv | 126 |
| rels_CROSS_REFERENCES.csv | 653 |

Of the USML entries, 105 are flagged as Significant Military Equipment and 35 carry the (MT)
MTCR-Annex annotation. The 194 sections match the source's table of contents exactly (no section
missing, none extra).

## Validation

A checker asserts that every node id is unique within its file and that every `source_id` /
`target_id` in every relationship file resolves to a node id — result: PASS, 0 duplicates,
0 dangling endpoints. A separate check confirms that every stored text value occurs verbatim in the
source: 3,414 text fields checked, 3,334 match as a single contiguous span and the remaining 80 are
concatenations of contiguous verbatim source fragments (page-break rejoins and table-cell joins);
0 fields contain text that cannot be located in the source.

## Caveats and gaps

- The PDF is an unofficial compilation ("practice aid"); the official text is the CFR/Federal
  Register. Page headers/footers and the publisher's front matter and table of contents were
  removed and are not represented as nodes.
- Federal Register amendment citations (`[87 FR 16411, Mar. 23, 2022, as amended …]`) and
  "Link to an amendment published at …" lines were not modelled as their own nodes; Part-level
  `Authority` and `Source` notes are captured on `nodes_Part.csv`.
- Supplement No. 1 to Part 126 is a four-column table in the source. The exclusion text was rebuilt
  from the wrapped cell lines and the CA (§ 126.5) / AS (§ 126.16) / UK (§ 126.17) flags were
  recovered from the column position of each "X" marker; column-position recovery on a
  `pdftotext -layout` table is heuristic, so verify individual flags against the PDF before relying
  on them. The 17 explanatory Notes that follow that table are in `nodes_Note.csv`.
- Two country tables in § 126.1(d) are stored as `note_kind = table` rows rather than one node per
  country.
- Lettered sub-lists that appear inside Notes (e.g. "(a) in production; (b) determined to be subject
  to the EAR …") are kept inside the note text, not promoted to clause nodes.
- `[Reserved]` sections, clauses and USML entries are retained with a `reserved` flag so that the
  numbering of the instrument stays complete.
