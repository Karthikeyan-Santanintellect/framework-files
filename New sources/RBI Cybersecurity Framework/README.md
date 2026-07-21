# RBI Cyber Security Framework in Banks — knowledge-graph CSVs

## Source document

- **Instrument:** Cyber Security Framework in Banks (RBI circular)
- **Circular number:** RBI/2015-16/418
- **Reference number:** DBS.CO/CSITE/BC.11/33.01.001/2015-16
- **Date:** June 2, 2016 (Jyeshtha 12, 1938 (saka))
- **Issuer:** Reserve Bank of India, Department of Banking Supervision, Central Office, Mumbai
- **Addressed to:** The Chairman/ Managing Director /Chief Executive Officer, All Scheduled Commercial Banks (excluding Regional Rural Banks)
- **Signatory:** (R.Ravikumar), Chief General Manager
- **PDF:** `KB 2/India/RBI Cybersecurity Framework for Banks.pdf`

## Schema and why

The document is a circular with three annexes, so the graph mirrors that exact shape rather
than a generic controls template.

- **Circular** — the instrument itself, carrying the circular/reference numbers and date.
- **Paragraph** — the 18 numbered paragraphs of the circular body, each with the printed
  side-heading that introduces it (paragraphs 2, 5, 8 and 12 continue the preceding heading and
  therefore carry an empty `heading`).
- **Annex** — Annex 1, Annex-2, Annex-3.
- **AnnexPreamble** / **KeyPoint** — Annex 1's opening statement and its lettered key points a–f.
- **ControlDomain** — the 24 numbered baseline control groupings in Annex 1 (`1) Inventory
  Management of Business IT Assets` … `24) Customer Education and Awareness`).
- **Control** — the substantive control set: every numbered clause `n.m` in Annex 1 (106 rows),
  verbatim. Clauses 19.1–19.3 and 19.4–19.6 additionally carry the printed sub-headings
  "Responding to Cyber-Incidents:" and "Recovery from Cyber - Incidents:" in `sub_heading`.
- **ControlSubItem** — the lettered items (a)–(f) nested under control 19.6.
- **SOCSection** — the headed sections of Annex-2 (C-SOC governance, technology, process, people,
  external integration, implementation model). Annex-2 is discursive guidance with no numbered
  clause scheme, so it is captured at heading level with the full verbatim block text.
- **ReportingForm** / **FormItem** — Annex-3's two reporting templates and their numbered items:
  the "Template for reporting Cyber Incidents" (sections *Security Incident Reporting* and
  *Basic Information*, whose numbering restarts) and the CSIR Form (items 1–18 plus E1 under
  *Attack Vectors*).
- **Deadline** — the three stated time obligations: September 30, 2016 (Board-approved
  cyber-security policy confirmation, para 3); July 31, 2016 (gap self-assessment submission by
  the CISO, para 16); "within two to 6 hours" (Security Incident Reporting to RBI, Annex-3).
- **ReferencedBody** — bodies the circular names for reporting/coordination (CSITE Cell, CERT-IN,
  IDRBT, IB-CART, NCIIPC).
- **PriorCircular** — the 2011 G. Gopalakrishna Committee circular referenced in paragraph 1.

Relationship types: `HAS_PARAGRAPH`, `HAS_ANNEX`, `HAS_PREAMBLE`, `HAS_KEY_POINT`,
`HAS_CONTROL_DOMAIN`, `HAS_CONTROL`, `HAS_SUB_ITEM`, `HAS_SECTION`, `HAS_FORM`, `HAS_ITEM`,
`HAS_DEADLINE`, `REFERENCES` (paragraph → annex, with the quoted sentence), `REFERENCES_BODY`,
`REFERENCES_PRIOR_CIRCULAR`.

## Files

### Nodes

| File | Rows |
|---|---|
| nodes_Annex.csv | 3 |
| nodes_AnnexPreamble.csv | 1 |
| nodes_Circular.csv | 1 |
| nodes_Control.csv | 106 |
| nodes_ControlDomain.csv | 24 |
| nodes_ControlSubItem.csv | 6 |
| nodes_Deadline.csv | 3 |
| nodes_FormItem.csv | 27 |
| nodes_KeyPoint.csv | 6 |
| nodes_Paragraph.csv | 18 |
| nodes_PriorCircular.csv | 1 |
| nodes_ReferencedBody.csv | 5 |
| nodes_ReportingForm.csv | 2 |
| nodes_SOCSection.csv | 11 |

**Total nodes: 214**

### Relationships

| File | Rows |
|---|---|
| rels_annex_has_domain.csv | 24 |
| rels_annex_has_form.csv | 2 |
| rels_annex_has_keypoint.csv | 6 |
| rels_annex_has_preamble.csv | 1 |
| rels_annex_has_socsection.csv | 11 |
| rels_circular_has_annex.csv | 3 |
| rels_circular_has_paragraph.csv | 18 |
| rels_circular_supersedes_reference.csv | 1 |
| rels_control_has_subitem.csv | 6 |
| rels_domain_has_control.csv | 106 |
| rels_form_has_item.csv | 27 |
| rels_paragraph_references_annex.csv | 3 |
| rels_paragraph_references_body.csv | 7 |
| rels_provision_has_deadline.csv | 3 |

**Total relationships: 218**

## Caveats and gaps

- The circular states that Annex 1 is "An indicative but not exhaustive list of requirements";
  the baseline controls are therefore expressed as recommended/mandated practice rather than as
  a closed compliance catalogue. No maturity levels, scoring or penalties are stated anywhere in
  the document, so no such nodes exist.
- The document contains **no definitions section**; there are no defined terms to extract.
- Paragraph 1 is unnumbered in the source (it follows the "Introduction" heading); it is
  numbered `1` here so that subsequent paragraph numbering matches the printed numbers 2–18.
- Annex-2 is narrative guidance with mixed numbering (`1 -`, `2 -`) and bullet lists that restart
  in several sub-blocks; modelling it at clause level would have produced arbitrary identifiers,
  so it is modelled at heading level with the full text of each block preserved verbatim.
- Annex-3 is a fillable form. Form-field artefacts present in the PDF text ("Click here to enter
  text.", "Choose an item.", checkbox glyphs ☐) are preserved verbatim inside the item text.
- Bilingual (Hindi/English) page headers, the department footer block and page numbers were
  removed as layout artefacts; wrapped lines were rejoined into single-line prose with wording
  unchanged.
- The source text shows one OCR/typo artefact carried through verbatim: control 9.1 reads
  "positive identify verification" and controls 14.1 read "anti-rouge"/"rouge applications" as
  printed in the original.
- Generated by script from a `pdftotext -layout` extract. All ids are unique and every
  relationship endpoint resolves to a node id (verified).
