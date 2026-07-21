# 21 CFR Part 11 — Electronic Records; Electronic Signatures

Knowledge-graph CSV extraction of **two distinct instruments**, modelled in one folder but kept
strictly separate:

| Instrument node | Type | Source |
|---|---|---|
| `INST-REG` | Regulation (binding) | 21 CFR Part 11, eCFR, **up to date as of 5/21/2026** — `KB 2/USA/21 CFR Part 11.pdf` |
| `INST-GUID` | Guidance (nonbinding) | *Guidance for Industry: Part 11, Electronic Records; Electronic Signatures — Scope and Application*, FDA, August 2003 (Pharmaceutical CGMPs) — `KB 2/USA/Part-11--Electronic-Records--Electronic-Signatures.pdf` |

The eCFR text carries the notice "This content is from the eCFR and is authoritative but unofficial."
The guidance carries "Contains Nonbinding Recommendations" on every page. Both notices are stored on
the respective `Instrument` rows (`status_note`, `binding_status`, `currency_date`).

## Schema

The schema uses each document's own vocabulary. The regulation is Part → Subpart → Section (§) →
Clause (paragraph / sub-paragraph / sub-sub-paragraph, recursive); the guidance is Guidance Section →
Sub-section, with footnotes, references and enforcement positions hanging off it.

### Node types

| File | Type | Rows | Notes |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 2 | regulation + guidance; authority, source credit, eCFR currency date |
| `nodes_Subpart.csv` | Subpart | 3 | A General Provisions, B Electronic Records, C Electronic Signatures |
| `nodes_Section.csv` | Section | 10 | 9 §§ plus `SEC-11.30` etc.; carries undesignated chapeau text (§§ 11.10, 11.30, 11.70, 11.300) and FR amendment notes |
| `nodes_Clause.csv` | Clause | 66 | every lettered/numbered subdivision, verbatim, with `citation`, `label`, `level`, `parent_clause_id` |
| `nodes_Definition.csv` | Definition | 9 | § 11.3(b)(1)–(9) defined terms, verbatim |
| `nodes_ExternalReference.csv` | ExternalReference | 14 | out-of-part citations the regulation names (part 117, § 101.11(d), docket 92S-0251, …) |
| `nodes_GuidanceSection.csv` | GuidanceSection | 14 | I, II, III, III.A, III.B(+1,2), III.C(+1–5), IV |
| `nodes_GuidanceFootnote.csv` | GuidanceFootnote | 8 | footnotes 1–8, verbatim |
| `nodes_GuidanceTerm.csv` | GuidanceTerm | 5 | terms the guidance itself defines (predicate rules, legacy system, part 11 records, *should*, hybrid) |
| `nodes_EnforcementPosition.csv` | EnforcementPosition | 8 | see below |
| `nodes_Reference.csv` | Reference | 7 | section IV FDA + industry references |
| `nodes_WithdrawnDocument.csv` | WithdrawnDocument | 6 | draft guidances and CPG 7153.17 whose withdrawal section II announces |

The ten sections are exactly those in the eCFR table of contents: §§ 11.1, 11.2, 11.3 (Subpart A);
11.10, 11.30, 11.50, 11.70 (Subpart B); 11.100, 11.200, 11.300 (Subpart C).

### Enforcement discretion (the point of the guidance)

`nodes_EnforcementPosition.csv` captures explicitly that the guidance changes how the regulation is
applied. Each row records the verbatim `statement`, the verbatim `caveat` (what still must be
complied with, i.e. predicate rules), and for legacy systems the four verbatim `criteria`
(pipe-separated). Positions:

- `EP-VALIDATION`, `EP-AUDIT-TRAIL`, `EP-COPIES`, `EP-RETENTION` — enforcement discretion for
  § 11.10(a), (e)+(k)(2), (b), (c) respectively, plus corresponding requirements in § 11.30.
- `EP-LEGACY` — enforcement discretion for **all** part 11 requirements for pre-20 Aug 1997 systems.
- `EP-NARROW-SCOPE` — interpretive position on §§ 11.2(a), 11.2(b).
- `EP-CONTINUED-ENFORCEMENT` — provisions FDA states it will continue to enforce (§ 11.10 controls,
  § 11.30, §§ 11.50/11.70/11.100/11.200/11.300).
- `EP-PART11-IN-EFFECT` — "Note that part 11 remains in effect…".

### Relationship types

| File | Rel types | Rows |
|---|---|---|
| `rels_contains.csv` | `HAS_SUBPART`, `HAS_SECTION`, `HAS_CLAUSE`, `HAS_SUBCLAUSE` | 79 |
| `rels_guidance_structure.csv` | `HAS_SECTION`, `HAS_SUBSECTION`, `HAS_FOOTNOTE`, `DEFINES_TERM`, `CITES_REFERENCE`, `ANNOUNCES` | 42 |
| `rels_defines.csv` | `DEFINES` (clause → definition) | 9 |
| `rels_cross_references.csv` | `CROSS_REFERENCES` (in-part, with quoted context) | 5 |
| `rels_external_references.csv` | `REFERS_TO_EXTERNAL` | 14 |
| `rels_guidance_discusses.csv` | `DISCUSSES`, `REFERS_TO_SECTION` — guidance → regulation node, **only where the guidance itself states the citation** (`stated_citation` column holds the quoted citation) | 22 |
| `rels_enforcement_applies_to.csv` | `DISCRETION_APPLIES_TO`, `INTERPRETS`, `CONTINUES_TO_ENFORCE` | 20 |
| `rels_instrument_links.csv` | `PROVIDES_GUIDANCE_ON` (guidance → regulation) | 1 |
| `rels_withdrawn_by.csv` | `ANNOUNCES_WITHDRAWAL_OF` | 6 |

Totals: **152 nodes, 198 relationships** across 12 node files and 9 relationship files.

## Caveats and gaps

- Guidance→regulation links are deliberately conservative: a link exists only where the guidance
  text prints the section/paragraph citation. Where the guidance says "any corresponding requirement
  in § 11.30" the link points at the **section** `SEC-11.30` (it has no lettered paragraphs), not at
  an invented paragraph.
- § 11.30 and § 11.70 have no lettered paragraphs; their full operative text is stored in the
  `undesignated_text` column of `nodes_Section.csv`, so they produce no `Clause` rows.
- The regulation states no penalties or deadlines beyond the dates it names (effective/reference date
  20 Aug 1997, docket 92S-0251, FR amendment history); those are recorded where stated and nowhere
  invented.
- The guidance's bulleted lists are preserved inline in the section `text` field, joined into prose
  with `;` separators — bullet glyphs are dropped but wording is unchanged. Legacy-system criteria are
  additionally broken out as discrete pipe-separated values on `EP-LEGACY`.
- Guidance page furniture ("Contains Nonbinding Recommendations", line numbers, page numbers) and the
  title-page contact block were treated as layout artifacts and excluded from clause text.
- Source PDFs were not read; extraction is from the `pdftotext -layout` text only. No OCR noise was
  observed in either extract.
- Validation: all node ids are unique (globally, not just per file) and every relationship endpoint
  resolves to a node id.
