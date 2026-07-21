# South Africa POPIA — knowledge-graph CSV extraction

## CRITICAL SOURCE CAVEAT — READ FIRST

The task requested extraction of the **Protection of Personal Information Act, 2013 (Act 4 of 2013)**
itself — Chapters and Parts, section 1 definitions, the eight conditions for lawful processing,
the Information Regulator, prior authorisation, codes of conduct, direct marketing, transfer rules,
offences and penalties.

**The source PDF does not contain the Act.** `KB 2/Africa/Protection of Personal Information Act.pdf`
(23 pages, extracted to `Africa_Protection_of_Personal_Information_Act.txt`) is in fact:

> *Amendment of the Regulations relating to the Protection of Personal Information, 2018* —
> subordinate legislation made by the Information Regulator under section 113(3) of POPIA,
> signed by Adv. F.D.P. Tlakula on 21 January 2025 and tabled before Parliament under section 113(5).

The file contains **zero** text of the Act. There are no Chapters, no Parts, no numbered sections of
the Act, no section 1 definitions, no Conditions 1–8, no Chapter 9 transfer rules (section 72), no
Chapter 11 offences/penalties (sections 100–109 text), no prior-authorisation provisions
(sections 57–58), and no codes-of-conduct provisions (sections 60–68). Those provisions are only
ever *cited by number* from within the regulations.

Per the contract's verbatim-only rule, **none of that missing Act content has been supplied from
model knowledge.** What is modelled below is exactly and only what the source document contains.
To build the Act-level graph that was originally requested, a source PDF of the Act itself must be
obtained.

## Schema

The document is an amending statutory instrument, so the schema uses the document's own vocabulary
(Schedule → amendment items → Regulations / sub-regulations → Forms) rather than an Act-shaped
Chapter/Section model.

### Node types

| File | Type | What it is |
|---|---|---|
| `nodes_Instrument.csv` | Instrument | The amending instrument itself, with enabling provision, signing date, short title and commencement clause. |
| `nodes_TablingNotice.csv` | TablingNotice | The numbered items I–III of the Regulator's tabling notice, plus the signature block. |
| `nodes_AmendmentItem.csv` | AmendmentItem | Each numbered item of the Schedule (Amendment/Substitution/Insertion of Regulation 1, 2, 3, 4, 5, 6, 7, 12, 13; plus free-standing Transitional provisions and Short title). Carries the amending chapeau verbatim and, where the item substitutes a regulation, the substituted regulation heading. |
| `nodes_Provision.csv` | Provision | **Clause level.** Every numbered sub-regulation and sub-sub-regulation that carries text (e.g. 6.1, 6.1.3, 7.3.1.2, 9.2.1) is its own row with verbatim text, plus `deadline` and `obligated_party` where the text states them. Self-nesting via `parent_provision_id`. |
| `nodes_Definition.csv` | Definition | Each defined term inserted into Regulation 1, with its verbatim definition. |
| `nodes_DefinitionParagraph.csv` | DefinitionParagraph | Lettered paragraphs inside multi-limb definitions ("complaint" (a)–(c); "Office hours" (a)–(b)). |
| `nodes_Form.csv` | Form | Forms 1–5 as prescribed (with full verbatim titles), and Forms 17, 18, 19 recorded with `status = deleted` by the amendment to Regulation 12. |
| `nodes_FormSection.csv` | FormSection | The lettered/numbered blocks and notes inside each Form (Parts A/B, sections A–D, notes, the Form 2 reason list, the Form 4 consent wording). |
| `nodes_ActSection.csv` | ActSection | Every POPIA section cited by the regulations (11(3), 11(3)(a), 11(3)(b), 14, 18(1)(h)(iv), 24, 24(1), 24(1)(a), 24(1)(b), 61(1)(b), 63(3), 69(2), 73, 74, 74(1), 74(2), 76(1)(e), 92(1), 109(1), 113(3), 113(5)). Citation-only nodes — the Act's text is not in the source, so no text column is populated. |
| `nodes_ExternalInstrument.csv` | ExternalInstrument | Other legislation cited: Interpretation Act 1957, Electronic Communication and Transaction Act (as cited in the source), Protected Disclosures Act 2000, and the 2018 Regulations being amended. |

### Relationship types

| File | Rel | Meaning |
|---|---|---|
| `rels_CONTAINS.csv` | CONTAINS | Instrument → TablingNotice / AmendmentItem / Form. |
| `rels_HAS_PROVISION.csv` | HAS_PROVISION / HAS_SUBPROVISION | AmendmentItem → top-level sub-regulation; Provision → nested Provision. |
| `rels_DEFINES.csv` | DEFINES | Provision (1.1–1.4) → Definition. |
| `rels_HAS_PARAGRAPH.csv` | HAS_PARAGRAPH | Definition → DefinitionParagraph. |
| `rels_HAS_FORM_SECTION.csv` | HAS_FORM_SECTION | Form → FormSection. |
| `rels_REFERENCES_ACT_SECTION.csv` | REFERENCES_ACT_SECTION | Provision / Definition / Form / Instrument → ActSection, with the verbatim citing phrase in `quote`. |
| `rels_REFERENCES_STATUTE.csv` | REFERENCES_STATUTE, AMENDS | Provision / Definition / Instrument → ExternalInstrument, with verbatim `quote`. |
| `rels_PRESCRIBES_FORM.csv` | PRESCRIBES_FORM, DELETES_FORM | Provision → Form (which clause requires which form); AmendmentItem 12 → deleted Forms 17/18/19. |
| `rels_CROSS_REFERENCES.csv` | CROSS_REFERENCES | Internal sub-regulation cross-references (e.g. 3.4 → 3.2/3.3, 6.2 → 6.1, 7.2 → 7.10). |

## Row counts

### Nodes (159 node ids total)

| File | Rows |
|---|---|
| nodes_ActSection.csv | 21 |
| nodes_AmendmentItem.csv | 11 |
| nodes_Definition.csv | 6 |
| nodes_DefinitionParagraph.csv | 5 |
| nodes_ExternalInstrument.csv | 4 |
| nodes_Form.csv | 8 |
| nodes_FormSection.csv | 25 |
| nodes_Instrument.csv | 1 |
| nodes_Provision.csv | 74 |
| nodes_TablingNotice.csv | 4 |

### Relationships (186 total)

| File | Rows |
|---|---|
| rels_CONTAINS.csv | 23 |
| rels_CROSS_REFERENCES.csv | 8 |
| rels_DEFINES.csv | 6 |
| rels_HAS_FORM_SECTION.csv | 25 |
| rels_HAS_PARAGRAPH.csv | 5 |
| rels_HAS_PROVISION.csv | 74 |
| rels_PRESCRIBES_FORM.csv | 9 |
| rels_REFERENCES_ACT_SECTION.csv | 30 |
| rels_REFERENCES_STATUTE.csv | 6 |

## Source document

`KB 2/Africa/Protection of Personal Information Act.pdf` — recorded in every `source_document`
column as: *Protection of Personal Information Act, 2013 (Act 4 of 2013): Amendment of the
Regulations relating to the Protection of Personal Information, 2018 (tabled 21 January 2025)*.

## What the source DOES cover (relative to the original request)

- **Direct marketing** — covered, at clause level: amended Regulation 6 (6.1–6.4), consent for
  direct marketing via unsolicited electronic communication under s 69(2), the permitted channels
  (email, telephone, SMS/WhatsApp, fax, automated calling machine), the recording requirement, and
  the explicit rule that **"opt-out shall not constitute consent"** (6.4). Form 4 is the prescribed
  consent form.
- **Information Regulator** — covered procedurally: complaint handling (Regulation 7), the
  Regulator's 14-day acknowledgement duty (7.6), designated-office transfer within 14 days (7.4),
  assistance duties (7.3, 7.12), and protection of complainant identity (7.10–7.11).
- **Penalties** — covered only as an **administrative-fine payment mechanism** (new Regulation 13 /
  "Administrative Fines"): instalment arrangements after an infringement notice under s 109(1) and
  the two factors the Regulator must weigh. **No penalty amounts or offence definitions appear
  anywhere in the source.**
- **Codes of conduct** — covered only by the existence of prescribed Form 3 (application to issue a
  code of conduct under s 61(1)(b)) and the Regulation 5 terminology amendment substituting
  "relevant body/bodies" for "private or public body". The substantive code-of-conduct regime is not
  in the source.
- **Data subject rights procedure** — objection (Regulation 2, Form 1) and correction/deletion/
  destruction (Regulation 3, Form 2), including the 30-day notification deadline in 3.6.

## Not covered by the source (gaps)

- Chapters and Parts of the Act; any section of the Act as enacted text.
- Section 1 definitions of the Act (only the six regulation-level definitions are present).
- The eight conditions for lawful processing (Accountability, Processing limitation, Purpose
  specification, Further processing limitation, Information quality, Openness, Security safeguards,
  Data subject participation) — **entirely absent from the source**, so not modelled.
- Prior authorisation (ss 57–58), transborder transfer rules (s 72), offences and penalty amounts
  (ss 100–109 substantive text), Regulator establishment/powers (Chapter 5), exemptions.

## Other caveats

- **Numbering anomalies in the source are preserved verbatim, not corrected.** The item headed
  "Insertion of new Regulation 13" is numbered "8. Administrative Fines" in the body and its
  sub-provisions are numbered 9.1, 9.2, 9.2.1, 9.2.2. Provision ids follow the numbers as printed.
  Likewise the Schedule jumps from item 7 to item 12, and items 10 (Transitional provisions) and 11
  (Short title) appear after item 13's content.
- Regulation 7's chapeau states the amendment inserts "Regulation 7.3 to 7.18", but the source text
  only runs to 7.12. Only 7.1–7.12 exist in the document and only those are modelled.
- Sub-regulation 7.4 cites "sub-regulation 7.3.1.1.3", a numbering depth that does not exist in the
  printed text; the `CROSS_REFERENCES` edge points at the nearest existing provision (7.3.1) and the
  verbatim citing phrase is preserved in the `quote` column.
- The definition of "writing" cites "the Electronic Communication and Transaction Act, **2022** (Act
  No. 25 of 2002)" — an internal inconsistency in the source (the Act is of 2002). Reproduced as
  printed.
- Regulation 1 sub-item 1.1's chapeau is truncated in the source ("before the definition" with no
  term following). Reproduced as printed.
- Forms are largely blank fillable tables; `nodes_FormSection.csv` captures their headings, notes
  and static instruction text. Empty entry fields, signature rules and page furniture are not
  modelled as nodes.
- Layout artifacts (page numbers, column wrapping) were rejoined; wording is unchanged.

## Validation

A self-check script parsed every CSV and asserted: node-id uniqueness within each file, correct
`<type>_id` first column, presence of `source_document` on every node file, `source_id,target_id,
rel_type` as the first three relationship columns, and that all 372 relationship endpoints resolve
to a node id. **Result: 0 errors.**
