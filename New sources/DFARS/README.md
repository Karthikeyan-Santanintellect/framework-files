# DFARS — Defense Federal Acquisition Regulation Supplement

**Source:** `KB 2/USA/DFARS.pdf` — Volume III, Parts 201–253 (+ Part 270 and Appendices A–I), 1,466 pages
**Extraction:** full verbatim, clause level. The largest document in the knowledge base by a wide
margin; extracted by nine parallel agents split on PART boundaries, plus a tenth pass to recover
three clauses that fell between slice boundaries. Merged here and de-duplicated on primary key.

## Schema

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Part.csv` | 65 | PARTs 201–253, 270, and Appendices A–I (modelled as peer-level Parts) |
| `nodes_Subpart.csv` | 358 | Subparts, e.g. 239.71 |
| `nodes_Section.csv` | 2,100 | Every section and every 252-series clause, with its prescription/date line |
| `nodes_Provision.csv` | 14,012 | **Clause-level decomposition** — `(a)` / `(1)` / `(i)` / `(A)` nesting to depth 7, plus Basic/Alternate variants and quoted defined terms |
| `rels_structure.csv` | 16,470 | HAS_SUBPART, HAS_SECTION, HAS_PROVISION |
| `rels_references.csv` | 1,738 | CROSS_REFERENCES between DFARS provisions, with the verbatim `cited_text` |

**16,535 nodes · 18,208 relationships.** All ids unique; **0 unresolved relationship endpoints**.

## Completeness

- **447 of 447** `252.xxx-yyyy` clause headers present in the source are extracted — verified by
  diffing the extracted section numbers against a regex sweep of the source text.
- Section coverage in each slice was independently cross-checked against that PART's own printed
  table of contents; slices 1–4 report 100% TOC agreement.
- **252.204-7012** (Safeguarding Covered Defense Information and Cyber Incident Reporting) — the
  clause that drives CMMC — is captured in full: 52 provisions, all 16 defined terms,
  paragraphs (a)–(n) and their sub-levels.
- **PART 239** (Acquisition of Information Technology) is captured at full clause depth.

### Boundary repair (worth knowing about)

Three clauses — **252.225-7001**, **252.225-7044**, **252.229-7001** — were initially dropped by
*both* slices adjacent to them. The cause is a `pdftotext` artifact: the running header at the top
of each page prints the number of the *next* clause, so a naive boundary detector treats it as the
start of a new clause and truncates the current one mid-text. The three were re-extracted from
corrected spans running through their real `(End of clause)` terminators, and verified by a
token-multiset comparison against the de-furnitured source (10,627 vs 10,627 tokens, zero missing,
zero extra). All 10 variants (4 + 4 + 2 Basic/Alternate) reach their terminator.

## Caveats

- `rels_references.csv` contains only DFARS-internal citations that resolve to a node here.
  Citations to FAR, PGI, U.S.C. and CFR remain inline in the verbatim provision text but are not
  edges — there are no nodes for them.
- Some provisions have empty `text`: these are genuine container markers whose children carry the
  text (e.g. the `(1)` in a printed `(1) (i)` run). `[Reserved]` / `Removed.` markers are kept as
  printed rather than dropped.
- Multi-column tables do not survive `pdftotext -layout` faithfully. The known case is
  Table 215.403-1 (in `PROV-215.403-5-b-3`), where column ordering is approximate; the text is
  present but its tabular structure is not reliable.
- Appendix A contains two copies of "Part 1 — Charter" (a 2019 and an earlier 2007 charter); both
  are kept verbatim rather than de-duplicated, since they are different documents.
- Page furniture (running heads, page numbers, "This page intentionally left blank", TOC blocks)
  was stripped. Source typos and typesetting defects — `Definitions.As used`, `PRESCRIPTION OFFORMS`,
  a defective `End of clause)` missing its opening parenthesis — are preserved verbatim.
