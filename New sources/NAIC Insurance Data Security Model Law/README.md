# NAIC Insurance Data Security Model Law (Model #668)

## Source

- **Instrument:** Insurance Data Security Model Law, NAIC Model #668 (MO-668)
- **Publication:** *NAIC Model Laws, Regulations, Guidelines and Other Resources* — 4th Quarter 2017
- **Issuing body:** National Association of Insurance Commissioners
- **Source PDF:** `KB 2/USA/NAIC Insurance Data Security Model Law.pdf`
- **Chronological summary of actions (as printed):** 2017 4th Quarter (adopted by Executive/Plenary via conference call). 2025 (technical edit).

### Important: this is a model law, not directly binding law

Model #668 is a **model law drafted by the NAIC for adoption by individual states**. It has no
legal force of its own. It becomes binding only where a state legislature enacts it (with or
without amendment), and enacted versions differ from this text. The document itself signals this
throughout: it contains bracketed placeholders to be completed by the adopting state — e.g.
`[insert name of insurance regulatory body]` (Section 3E), `[adopting state]` (Section 3O),
`[insert state's data breach notification law]` (Section 6C), `[insert general penalty statute]`
(Section 10), `[insert a date]` (Section 13) — and marks Section 11 `[OPTIONAL]`. Bracketed
placeholders are retained verbatim in the extracted text; they are not resolved.

## Schema

The schema mirrors the model law's own structure and vocabulary: numbered **Sections**, lettered
**Subsections** (A, B, C …), numbered/lettered/roman **Clauses** nested to arbitrary depth
(`(1)`, `(a)`, `(i)`), the Section 3 **Definitions**, and the **Drafting Notes** the NAIC
interleaves with the operative text.

### Node types

| File | Node type | Rows | Notes |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | The model law itself; carries issuing body, model number, adoption history, and `instrument_type = "Model law for adoption by states"`. |
| `nodes_Section.csv` | Section | 13 | Sections 1–13. `text` is populated only for sections with no lettered subsections (1, 10, 11, 12, 13). |
| `nodes_Subsection.csv` | Subsection | 30 | Lettered subdivisions (Section 2A, 4A–4I, 5A–5D, 6A–6F, 7A–7B, 8A–8E, 9A–9B). `heading` holds the subsection's own caption where the document gives one (e.g. "Risk Assessment", "Incident Response Plan"). `text` is the chapeau where sub-clauses follow. |
| `nodes_Definition.csv` | Definition | 16 | Section 3A–3P. Definitions are typed separately from ordinary subsections because they carry a defined **term** rather than an obligation. |
| `nodes_Clause.csv` | Clause | 99 | Every numbered/lettered/roman subdivision that carries text, at any depth, e.g. `Section 4D(2)(g)`, `Section 6A(2)(b)(ii)`, `Section 3K(3)(a)`. `parent_id` points at the Subsection, Definition, or parent Clause. `level` records the document's own tier (`paragraph`, `subparagraph`, `clause`). |
| `nodes_DraftingNote.csv` | DraftingNote | 3 | The NAIC's "Drafting Note:" passages, **kept out of the operative text** and attached to the section they follow: the N.Y. 23 NYCRR 500 safe-harbour intent note (after Section 2), the examination-law confidentiality note (after Section 8), and the note that Section 11 applies only to states requiring the language. |
| `nodes_Requirement.csv` | Requirement | 12 | The deadlines and thresholds the model law states explicitly — February 15 annual certification, 72-hour notification, 250-Consumer threshold, five-year retention (×2), fewer-than-ten-employee exemption, 180-day grace period, one-/two-year implementation periods, annual board reporting and annual safeguard assessment. Each carries the verbatim sentence it comes from. |

### Relationship types

| File | Relationship | Rows | Meaning |
|---|---|---|---|
| `rels_HAS_SECTION.csv` | `HAS_SECTION` | 13 | Instrument → Section |
| `rels_HAS_SUBSECTION.csv` | `HAS_SUBSECTION` | 30 | Section → Subsection |
| `rels_DEFINES.csv` | `DEFINES` | 16 | Section 3 → Definition (carries the `term`) |
| `rels_HAS_CLAUSE.csv` | `HAS_CLAUSE` | 99 | Subsection / Definition / Clause → child Clause |
| `rels_HAS_DRAFTING_NOTE.csv` | `HAS_DRAFTING_NOTE` | 3 | Section → DraftingNote |
| `rels_STATES_REQUIREMENT.csv` | `STATES_REQUIREMENT` | 12 | Section / Subsection → Requirement |
| `rels_CROSS_REFERENCES.csv` | `CROSS_REFERENCES` | 23 | Provision → provision, for every internal reference the text makes ("as defined in Section 3", "the steps listed in Section 5B above", "exempt from Section 4", …). Carries the `quoted_reference` as it appears. |

Totals: **174 nodes**, **196 relationships**.

### Why this shape

The document is a short statute-shaped model act, so a Section → Subsection → Clause spine
reproduces its citation scheme exactly (a reader citing "Section 4D(2)(g)" lands on one node).
Two things justified separate node types rather than more subsections:

- **Definitions** are the sole content of Section 3 and are referenced by term throughout the
  rest of the Act, so they get a `term` field and their own type.
- **Drafting Notes** are NAIC commentary addressed to *adopting legislatures*, not obligations on
  Licensees. Mixing them into the clause text would make non-operative guidance indistinguishable
  from binding-once-adopted language, so they are typed separately as the task requires.

Requirements were split out because the model law's compliance-relevant numbers (72 hours,
250 Consumers, February 15, five years, ten employees, 180 days) are the parts most often queried,
and each is anchored to its verbatim source sentence rather than restated.

## Coverage and caveats

- The whole document (701 lines of `pdftotext -layout` output) was read; Sections 1–13, all 16
  definitions, all three drafting notes, the table of contents and the chronological summary are
  accounted for. Nothing is omitted except the table of contents itself (redundant with
  `nodes_Section.csv`), page headers/footers, and the `© 2017 NAIC` running footer.
- Column wrapping from the layout extract was rejoined into single-line prose with wording,
  punctuation and the source's curly quotes preserved exactly.
- Section 6E(1) and 6E(2) have no chapeau text of their own in the source — the numbered item
  goes straight to `(a)`. Those two Clause rows therefore carry an empty `text` cell, which is
  faithful to the document, with the substance in `6E(1)(a)/(b)` and `6E(2)(a)/(b)`.
- Section 6F's two paragraphs (the obligation and the "excused from this obligation" proviso) are
  unnumbered in the source and are held together on the single `SUB-6F` node.
- Section 8A references "Section 6B(2), (3), (4), (5), (8), (10), and (11)". The cross-reference
  is recorded once against `SUB-6B` with the full quoted reference, rather than fanned out into
  seven edges.
- Section 10 (Penalties) states no penalty amount — it defers to `[insert general penalty
  statute]`. No penalty figure is recorded because the document supplies none.
- The bracketed cross-references to external instruments (Producer Licensing Model Act, the
  adopting state's breach-notification law, state open-records law, state examination statutes)
  are left as verbatim text; they are not modelled as edges because no target node exists.
- No content was added from outside the source text.

## Validation

`check_naic.py` parses every CSV, asserts node ids are unique within and across files, asserts the
first column of each node file ends in `_id`, asserts every relationship file starts with
`source_id,target_id,rel_type`, and asserts every relationship endpoint resolves to a node id.
Result: **all checks pass, 0 unresolved endpoints, 0 duplicate ids**.
