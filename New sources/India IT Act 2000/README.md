# India — Information Technology Act 2000 (source PDF: subordinate legislation)

**Source document:** `KB 2/India/Information Technology Act 2000.pdf`
(extracted with `pdftotext -layout`, 4,378 text lines)

## IMPORTANT — what this source actually contains

The PDF filed under the name *Information Technology Act 2000* **does not contain the text of
the Act itself.** It contains the four Gazette notifications issued under the Act on
17 October 2000 (Gazette of India, Extraordinary, Part II, Section 3, Sub-section (i),
File No. 1(20)/97-IID(NII)/F6, signed P.M. Singh, Joint Secretary):

| Notification | Enabling power | Content |
|---|---|---|
| G.S.R 788 (E) | sub-section (3) of section 1 | appoints 17 October 2000 as the commencement date |
| G.S.R 789 (E) | section 87 | Information Technology (Certifying Authorities) Rules, 2000 — rules 1–34 + Schedules I–V |
| G.S.R 790 (E) | section 88 | constitutes the Cyber Regulation Advisory Committee (21 members) |
| G.S.R 791 (E) | section 87 | Cyber Regulations Appellate Tribunal (Procedure) Rules, 2000 — rules 1–28 + Forms 1–2 |

Consequently the following, which the extraction brief asked for, **are not present in the
source and have therefore not been extracted** — supplying them would have required inventing
text from outside the document, which the contract forbids:

- Chapters I–XIII of the Act and its numbered **sections** (including section 2 definitions);
- the **offences and penalties** chapter — sections 43A, 65–67, 69, 72A and related provisions;
- the Act's own Schedules (the First to Fourth Schedules).

**Amendment status:** the text is the original 17 October 2000 Gazette material and is
consolidated to **no amendments** — it predates the Information Technology (Amendment) Act,
2008 (which introduced ss. 43A, 66A–66F, 67A–67C, 69A/69B and 72A and replaced "digital
signature" with "electronic signature" and the Cyber Regulations Appellate Tribunal with the
Cyber Appellate Tribunal). Nothing in this source reflects those changes. To model the Act's
sections and offence provisions, a consolidated copy of the Act (as amended to 2009 / 2023)
must be supplied as a separate source.

## Schema

The schema mirrors the document's own vocabulary: Notification → Rules → sub-rules/clauses,
plus Schedules that are either guideline documents, forms, or a glossary.

### Node types

| File | Type | Rows | What it is |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | the notified package as a whole |
| `nodes_Notification.csv` | Notification | 4 | the four G.S.R. notifications, with enabling power |
| `nodes_RuleSet.csv` | RuleSet | 2 | the two sets of rules made under section 87 |
| `nodes_Rule.csv` | Rule | 62 | numbered rules (CA 1–34, CRAT 1–28) with marginal title |
| `nodes_Provision.csv` | Provision | 268 | clause-level sub-rules — `(1)`, `(a)`, `(i)` … verbatim, incl. 2 numbered paragraphs of G.S.R 790 |
| `nodes_Definition.csv` | Definition | 25 | defined terms from rule 2 of each rule set |
| `nodes_Schedule.csv` | Schedule | 5 | Schedules I–V to the Certifying Authorities Rules |
| `nodes_Guideline.csv` | Guideline | 87 | numbered guideline paragraphs of Schedule II (IT Security Guidelines) and Schedule III (Security Guidelines for CAs), including decimal sub-paragraphs |
| `nodes_GuidelineProvision.csv` | GuidelineProvision | 456 | clause-level items inside those paragraphs, verbatim |
| `nodes_GlossaryTerm.csv` | GlossaryTerm | 213 | Schedule V glossary entries with verbatim definitions |
| `nodes_Acronym.csv` | Acronym | 17 | Schedule V acronym table |
| `nodes_Standard.csv` | Standard | 10 | the product/standard table in rule 6 |
| `nodes_Form.csv` | Form | 4 | Schedule I form, Schedule IV form, CRAT Form-1, Form-2 |
| `nodes_FormField.csv` | FormField | 79 | numbered fields of those forms (verbatim labels) |
| `nodes_Committee.csv` | Committee | 1 | Cyber Regulation Advisory Committee |
| `nodes_CommitteeMember.csv` | CommitteeMember | 21 | its members with designation and role |

**Total node rows: 1,255.**

### Relationship types

| File | rel_type | Rows |
|---|---|---|
| `rels_contains.csv` | CONTAINS / CONSTITUTES | 1,198 |
| `rels_defines.csv` | DEFINES (provision → defined term) | 25 |
| `rels_prescribes_standard.csv` | PRESCRIBES_STANDARD (rule 6 → standard) | 10 |
| `rels_has_member.csv` | HAS_MEMBER | 21 |
| `rels_references.csv` | REFERENCES (internal cross-refs to rules, Schedules and Schedule-II paragraphs; carries `ref_kind`) | 90 |

**Total relationship rows: 1,344.**

Every node file starts with `<type>_id` and carries `source_document`; every relationship file
starts with `source_id,target_id,rel_type`.

### Cross-references
Provision, Guideline and GuidelineProvision rows carry `act_section_refs`, `rule_refs`,
`schedule_refs` and `para_refs` columns holding the numbers cited in the verbatim text.
References to **sections of the Act** are kept only as column values (e.g. `24`, `35`, `57`,
`87`), because the Act's sections are not in this source and so cannot be relationship
endpoints — every foreign key in the `rels_*` files resolves to a node id in this folder.

## Caveats and known gaps

1. **The Act itself is absent** (see above). No section, chapter, offence or penalty node
   exists because no such text exists in the source.
2. Provisos and "Explanation" passages are retained verbatim but stay attached to the
   provision they follow rather than becoming separate nodes; no text is dropped.
3. Schedule III of the source mis-numbers two consecutive sub-paragraphs as `18.1`
   ("Generation" and "Distribution of Keys") and skips `18.4`. Both are kept
   (`S3-P18.1`, `S3-P18.1-2`) exactly as printed.
4. Only top-level numbered fields of the application forms are modelled; lettered
   sub-fields (A./B./(i) …) inside a field are not separate rows.
5. The PDF layout table in rule 6 was rejoined column-wise; minor OCR/typo artefacts
   present in the source (e.g. "fi9nal", "Regstrar", "hoursof", "sliall") are preserved
   verbatim rather than corrected.
6. Page headers/footers, index/table-of-contents listings for Schedules II and III, and
   signature blocks are not modelled as nodes.
