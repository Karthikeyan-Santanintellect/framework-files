# MITRE ATT&CK Enterprise Framework — knowledge-graph CSVs

Source document: `KB 2/USA/Mitre Att&ck.pdf`
Framework version stated on the poster: **v15, current as of April 2024** (© 2024 MITRE).

---

## ⚠️ READ THIS FIRST — the source is OCR of an image poster

The source PDF is a **single-page image poster** of the ATT&CK Enterprise matrix. It has
**no text layer**. Everything in these CSVs was recovered from a **tesseract OCR pass** over
that image. Consequences you must accept before using this data:

1. **The technique lists are incomplete.** The matrix is a dense 14-column grid and OCR bled
   content across column boundaries, dropping whole cells. We recovered **206 of the 235
   techniques the poster itself claims** (see the table below).
2. **Some recovered names are unreliable.** Where OCR mangled or truncated a name we kept it
   **verbatim as OCR produced it** and marked it `low` confidence — e.g. `Financial Thett`,
   `Fyfittration Over Alternative Protocol`, `Inout Capture`, `0S Credential Dumping`,
   `File and Directory D'SCovery`, `Sehecer esr`. **These were deliberately not "corrected"**
   from outside knowledge of ATT&CK, and no technique known to exist in ATT&CK was added if it
   could not be read in the source.
3. **Tactic assignment for some techniques is inferred**, not read. Column position was
   reconstructed from left-to-right token order on each OCR line. The Privilege Escalation
   column was eroded almost entirely; every technique attributed to it is `low` confidence.
4. **The number in each tactic header is the source's own authoritative count.** It is stated
   on the poster ("43 techniques", etc.) and is captured verbatim in
   `nodes_Tactic.stated_technique_count_text`. Trust that number over the number of technique
   rows present here.
5. **For any real use, prefer MITRE's canonical machine-readable ATT&CK data**, published as
   **STIX 2.1 / JSON** (`github.com/mitre-attack/attack-stix-data`, and the ATT&CK Workbench /
   TAXII services). That data is complete, versioned, carries technique IDs (`T####`),
   sub-techniques, descriptions, mitigations and data sources — none of which an image poster
   can give you. This extraction is a structural sketch of the poster, not a substitute.

### Stated vs. recovered, per tactic

| # | Tactic | Stated by source | Recovered here | Gap |
|---|--------|-----------------:|---------------:|----:|
| 1 | RECONNAISSANCE | 10 | 10 | 0 |
| 2 | RESOURCE DEVELOPMENT | 8 | 7 | 1 |
| 3 | INITIAL ACCESS | 10 | 10 | 0 |
| 4 | EXECUTION | 14 | 13 | 1 |
| 5 | PERSISTENCE | 20 | 19 | 1 |
| 6 | PRIVILEGE ESCALATION | 14 | 6 | **8** |
| 7 | DEFENSE EVASION | 43 | 34 | **9** |
| 8 | CREDENTIAL ACCESS | 17 | 15 | 2 |
| 9 | DISCOVERY | 32 | 29 | 3 |
| 10 | LATERAL MOVEMENT | 9 | 8 | 1 |
| 11 | COLLECTION | 17 | 17 | 0 |
| 12 | COMMAND AND CONTROL | 18 | 16 | 2 |
| 13 | EXFILTRATION | 9 | 9 | 0 |
| 14 | IMPACT | 14 | 13 | 1 |
| | **TOTAL** | **235** | **206** | **29** |

OCR confidence distribution across the 206 technique rows: **high 122, medium 57, low 27**.

---

## Schema

The poster's own structure is a matrix: one framework, 14 ordered tactic columns, and a stack
of technique cells within each column. The schema uses exactly that vocabulary — there are no
clauses, sections or obligations in this source, so the statute-shaped patterns do not apply.

**Node types**

- `Framework` — the poster itself (title, version, currency, publisher, URL as printed).
- `Tactic` — the 14 column headers, in printed left-to-right order, each carrying the
  source's own stated technique count both as printed text and as an integer.
- `Technique` — one row per technique cell recovered from OCR, with the name **exactly as OCR
  produced it**, its tactic, its position within the column, and the OCR provenance columns
  described below.

**Relationship types**

- `HAS_TACTIC` — Framework → Tactic (14).
- `HAS_TECHNIQUE` — Tactic → Technique (206), carrying `ocr_confidence` so a query can filter
  the graph down to only cleanly-read edges.

**OCR provenance columns on `nodes_Technique.csv`**

- `ocr_confidence` — `high` = read cleanly on a single OCR line in an unambiguous column
  position; `medium` = name rejoined from two wrapped OCR lines; `low` = OCR typo, truncation,
  unreadable output, or uncertain column attribution.
- `ocr_source_lines` — the line number(s) in the OCR text the name came from, so any cell can
  be re-checked against the raw OCR.
- `ocr_note` — what specifically went wrong with that cell, where anything did.

## Files

| File | Rows |
|------|-----:|
| `nodes_Framework.csv` | 1 |
| `nodes_Tactic.csv` | 14 |
| `nodes_Technique.csv` | 206 |
| `rels_HAS_TACTIC.csv` | 14 |
| `rels_HAS_TECHNIQUE.csv` | 206 |

Validated: all node ids unique within their file; every `source_id`/`target_id` in every
relationship file resolves to an existing node id.

## Further caveats and gaps

- **No technique IDs.** The poster prints names only, not `T1059`-style ATT&CK IDs, so none are
  recorded. The `technique_id` column here is a local surrogate key (`TA07-T12`), **not** an
  ATT&CK identifier.
- **No sub-techniques.** The poster marks cells that have sub-techniques with a small glyph
  (its legend reads "Has sub-techniques"), but does not list them. OCR rendered the glyph
  inconsistently as `=`, `=|`, `~`, `©`, so it was not reliable enough to record as a flag.
- **No descriptions, mitigations, detections or data sources** — the poster contains none.
- **Duplicate technique names across tactics are genuine** (e.g. `Valid Accounts` under both
  Initial Access and Persistence; `Traffic Signaling` under Persistence, Privilege Escalation
  and Command and Control). ATT&CK legitimately places one technique under several tactics.
  One duplicate is instead suspected OCR noise and is flagged as such in `ocr_note`:
  `Virtualization/Sandbox evasion` (Defense Evasion, differently cased second occurrence).
- **Two Discovery rows are unreadable OCR output** (`Sehecer esr`, `Dear DN;`). They are
  retained, verbatim and `low` confidence, as placeholders marking that a cell exists there and
  could not be recovered — not as technique names.
- **The poster URL** is recorded as OCR read it (`attack.mitre.o`, truncated on the image edge).
