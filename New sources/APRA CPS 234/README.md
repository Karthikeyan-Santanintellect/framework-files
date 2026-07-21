# APRA Prudential Standard CPS 234 — Information Security

**Source document:** APRA Prudential Standard CPS 234 Information Security (July 2019)
**Source PDF:** `KB 2/Australia/APRA Prudential Standard CPS 234.pdf`
**Jurisdiction:** Australia — Australian Prudential Regulation Authority (APRA)
**Commencement:** 1 July 2019 (paragraph 5); for information assets managed by a third party, from the earlier of the next renewal date of the contract or 1 July 2020 (paragraph 6).

## Schema

The schema mirrors the standard's own structure: an unnumbered "Objectives and key requirements"
preamble, then headed sections containing consecutively numbered paragraphs 1–36, many of which
have lettered sub-paragraphs, plus 14 numbered footnotes. The standard has no attachments.

### Node types
| File | Type | Rows | Notes |
|---|---|---|---|
| `nodes_Standard.csv` | Standard | 1 | The instrument itself, with verbatim objectives text |
| `nodes_Section.csv` | Section | 15 | Headed divisions in document order (Objectives … APRA notification) |
| `nodes_KeyRequirement.csv` | KeyRequirement | 4 | The four bullets in the Objectives preamble |
| `nodes_Paragraph.csv` | Paragraph | 36 | Numbered paragraphs 1–36; `closing_text` holds flush text after sub-paragraphs (only paragraph 4) |
| `nodes_Subparagraph.csv` | Subparagraph | 41 | Lettered subdivisions, e.g. `PARA-35(a)` |
| `nodes_Definition.csv` | Definition | 17 | 13 defined terms from paragraph 12(a)–(m) plus 4 group definitions from paragraph 10 |
| `nodes_Footnote.csv` | Footnote | 14 | Footnotes 1–14, each attached to the paragraph/sub-paragraph carrying its marker |
| `nodes_EnablingProvision.csv` | EnablingProvision | 5 | The five Acts/sections in paragraph 1 under which the standard is made |
| `nodes_RegulatedEntityType.csv` | RegulatedEntityType | 5 | The APRA-regulated entity types in paragraph 2(a)–(e) |
| `nodes_Deadline.csv` | Deadline | 6 | Stated periods: 72 hours, 10 business days, annual reviews, commencement dates |

### Relationship types
| File | Rel type | Rows |
|---|---|---|
| `rels_has_section.csv` | HAS_SECTION | 15 |
| `rels_has_key_requirement.csv` | HAS_KEY_REQUIREMENT | 4 |
| `rels_has_paragraph.csv` | HAS_PARAGRAPH | 36 |
| `rels_has_subparagraph.csv` | HAS_SUBPARAGRAPH | 41 |
| `rels_defines.csv` | DEFINES | 17 |
| `rels_has_footnote.csv` | HAS_FOOTNOTE | 14 |
| `rels_made_under.csv` | MADE_UNDER | 5 |
| `rels_applies_to.csv` | APPLIES_TO | 5 |
| `rels_entity_type_defined_in.csv` | DEFINED_IN | 5 |
| `rels_imposes_deadline.csv` | IMPOSES_DEADLINE | 6 |
| `rels_cross_reference.csv` | CROSS_REFERENCES | 7 |
| `rels_key_requirement_implemented_by.csv` | IMPLEMENTED_BY | 6 |

## Notification deadlines (verbatim)

- Paragraph 35 — "must notify APRA as soon as possible and, in any case, **no later than 72 hours**, after becoming aware of an information security incident that: (a) materially affected, or had the potential to materially affect, financially or non-financially, the entity or the interests of depositors, policyholders, beneficiaries or other customers; or (b) has been notified to other regulators, either in Australia or other jurisdictions."
- Paragraph 36 — "must notify APRA as soon as possible and, in any case, **no later than 10 business days**, after it becomes aware of a material information security control weakness which the entity expects it will not be able to remediate in a timely manner."

## Applicability

Applies to all "APRA-regulated entities": ADIs (incl. foreign ADIs and authorised banking NOHCs);
general insurers (incl. Category C insurers, authorised insurance NOHCs, parent entities of Level 2
insurance groups); life companies (incl. friendly societies, EFLICs, registered life NOHCs); private
health insurers registered under the PHIPS Act; and RSE licensees under the SIS Act in respect of
their business operations. For a foreign ADI, Category C insurer or EFLIC the obligations apply only
to Australian branch operations (paragraph 3).

## Caveats

- The standard sets no monetary penalties; enforcement flows from the enabling Acts, which the text
  does not detail. Penalty fields are therefore absent.
- Footnote markers were removed from paragraph body text (they are layout artifacts of the PDF
  extract); footnote text is preserved verbatim in `nodes_Footnote.csv` with its attachment point.
- Paragraph 10 and paragraph 12 chapeaux are stored with their definition lists inline in the
  paragraph `text` column; the individual terms are also separate `Definition` nodes.
- The `IMPLEMENTED_BY` links between the four Objectives key requirements and the substantive
  paragraphs are structural inferences from matching wording, not statements in the source.
- No attachments or schedules exist in this instrument.

## Validation

A checker asserted unique node ids (globally unique across files) and confirmed every relationship
endpoint resolves to a node id. Result: **OK**.
