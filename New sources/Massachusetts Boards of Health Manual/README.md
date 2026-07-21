# Massachusetts Association of Health Boards — Manual of Laws and Regulations Relating to Boards of Health (June 2016)

## ⚠️ This is NOT a cybersecurity, information-security or data-protection framework

Despite sitting in a knowledge base alongside cybersecurity and privacy frameworks, this document is a
**public-health law compendium for Massachusetts local boards of health**. It summarises the state statutes
(Massachusetts General Laws) and regulations (Code of Massachusetts Regulations) that give local boards of
health their powers and duties: communicable disease reporting, isolation and quarantine, housing and
sanitary code enforcement, food protection, swimming pools and beaches, medical/biological waste, hazardous
and solid waste siting, nuisances, burial permits, tanning facilities, smoking enforcement and so on.

It contains **no security controls, no cyber requirements and no general data-protection obligations**. Do not
map it to NIST CSF, ISO 27001, GDPR, HIPAA Security Rule or similar. The only provisions with any privacy
dimension are record-keeping and mandatory-reporting duties about identifiable individuals (disease reports,
tuberculosis certifications, cerebral palsy reports, death certificates, lead-poisoned children). Those are
isolated in `nodes_RecordsProvision.csv` and flagged there — the manual itself states **no confidentiality,
access-control, retention or breach rule** for them.

The manual is also **guidance, not the law itself**: it says the information "is provided as guidance only and
should not be relied upon as legal advice" and that its links "are not the official versions of the statutes or
regulations". It summarises the statutes; it does not reproduce their operative text.

## Source

Massachusetts Association of Health Boards, *Manual of Laws and Regulations Relating to Boards of Health*,
June 2016 — MAHB's update of the manual originally created by the Massachusetts Department of Public Health
pursuant to M.G.L. c. 111, s. 24. PDF: `KB 2/USA/MAHB-updated-Manual-of-Laws-and-Regulations-6.17.16-1.pdf`
(17 pages). Extraction is from a `pdftotext -layout` text render of that PDF.

## Schema and why

The manual's own structure is **Parts (roman-numbered) → lettered Sections → paragraphs and bullet items**, so
that spine is modelled literally, using the document's own vocabulary. Because the manual is a *compendium of
citations*, three further node types carry what actually matters analytically: the statutes/regulations it
compiles, the State Sanitary Code chapters it enumerates as a first-class series, and the board powers/duties
it asserts.

| Node type | Meaning |
|---|---|
| `Part` | A Part of the manual (PART I … PART IX as printed in the body). |
| `Section` | A lettered subsection within a Part (e.g. PART IV **B.** Chapter II: Housing). |
| `Provision` | The clause-level unit: each paragraph or bullet item, verbatim, rejoined from layout line-wraps. Carries `block_type` (`para`/`bullet`) and printed `page`. |
| `Citation` | Every legal authority the manual cites — M.G.L. statute sections, CMR regulations, case law, federal acts, named codes/programs. Normalised citation string, `code` (M.G.L./CMR), and `chapter_or_title`. |
| `SanitaryCodeChapter` | The chapters of the State Sanitary Code the manual enumerates (Chapters I–XI as listed), with the CMR citation and the regulation's own title. |
| `BoardPower` | One verbatim sentence per stated power or duty of a board of health, with `modality` (`must`/`shall`/`required`/`responsible`/`may`/`authorized`/`should`) and `power_type` (`duty` / `power` / `recommended practice`). |
| `DefinedTerm` | Terms the manual expressly defines, with verbatim definition. |
| `RecordsProvision` | **Privacy-relevant subset**: provisions imposing record-keeping, reporting, notification, certification or data-sharing duties, with `concerns_identifiable_persons` = yes/no. |

Relationship types: `HAS_SECTION`, `HAS_PROVISION`, `CITES`, `DESCRIBED_IN` / `PROMULGATED_AS`
(SanitaryCodeChapter → Section / Citation), `STATED_IN` (BoardPower → Provision), `DEFINED_IN`,
`DERIVED_FROM` (RecordsProvision → Provision).

`BoardPower` and `RecordsProvision` are *views* over `Provision` text — their `text` is verbatim source
sentences/paragraphs, and every row links back to the provision it came from. No text anywhere is paraphrased.

## Files

| File | Rows |
|---|---|
| `nodes_Part.csv` | 8 |
| `nodes_Section.csv` | 51 |
| `nodes_Provision.csv` | 62 |
| `nodes_Citation.csv` | 140 |
| `nodes_SanitaryCodeChapter.csv` | 10 |
| `nodes_BoardPower.csv` | 77 |
| `nodes_DefinedTerm.csv` | 6 |
| `nodes_RecordsProvision.csv` | 18 |
| `rels_part_has_section.csv` | 51 |
| `rels_has_provision.csv` | 62 |
| `rels_provision_cites_citation.csv` | 160 |
| `rels_sanitarycodechapter_links.csv` | 20 |
| `rels_boardpower_stated_in.csv` | 77 |
| `rels_definedterm_defined_in.csv` | 6 |
| `rels_recordsprovision_derived_from.csv` | 18 |

Every node file's first column is `<type>_id` and carries `source_document`; every relationship file begins
`source_id,target_id,rel_type`. A validation script confirmed: all ids unique, all 372 relationship endpoints
resolve, 0 errors.

## Caveats and gaps

- **Guidance, not statutory text.** The manual paraphrases and summarises; it reproduces very little verbatim
  statutory language. `Provision.text` is verbatim *manual* text, not verbatim M.G.L./CMR text. Nothing has
  been supplied from outside the document — where the manual states no detail, the cell is empty.
- **Part numbering is inconsistent in the source.** The table of contents lists Environmental Protection as
  PART VII and Miscellaneous as PART VIII, but the body headings print them as PART VIII and PART IX. Node ids
  follow the **body** headings (`PART_VIII` = Environmental Protection, `PART_IX` = Miscellaneous), so there is
  no `PART_VII`.
- **Sanitary Code Chapter IX is absent** from the manual (it jumps Chapter VIII → Chapter X); Chapter III's
  regulation title is not given in the text, so `regulation_title` is empty for it.
- **Part V section E is garbled in the source** — a single sentence is broken across a spurious "1. 2. 3."
  list numbering. It is preserved verbatim, stray numerals included.
- **No penalties, deadlines or thresholds beyond what the manual states.** Where the manual does give them
  (24-hour disease reporting, 7-day utility certification, 30-day variance/inspection windows, 45-day beach
  variance presumption, 21-day herbicide notice, 10-day trap permits, pre-1978 housing, children under six),
  they appear inside the verbatim provision and power text rather than in separate columns, because the
  document states them only in prose.
- Citation strings were normalised for whitespace, `M.G.L.`/`c.`/`s.` punctuation and hyphenation artifacts
  from the PDF render; section ranges and paragraph designators are otherwise as printed.
- The manual notes it "may be updated periodically"; this extraction reflects the June 2016 edition only.
