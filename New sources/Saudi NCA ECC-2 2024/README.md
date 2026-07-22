# Saudi Arabia NCA — Essential Cybersecurity Controls (ECC-2:2024)

Knowledge-graph CSV extraction of the National Cybersecurity Authority's
**Essential Cybersecurity Controls (ECC – 2 : 2024)**.

## Source

- **Document:** Essential Cybersecurity Controls (ECC – 2 : 2024), National Cybersecurity
  Authority (NCA), Kingdom of Saudi Arabia.
- **PDF:** `KB 2/Saudi Arabia/ECC--2024-EN.pdf` (cited only; extraction was made from a
  `pdftotext -layout` text render of that PDF).
- **Edition:** ECC-2 is the **current edition and supersedes ECC-1:2018**. The document's
  "Update and Review" section states: *"NCA has updated the previous version of the ECC
  (i.e., ECC-1:2018)"*, and Appendix (C) itemises the changes between the two editions.
  Main domain 5 (Industrial Control Systems Cybersecurity) of ECC-1 was deleted and its
  controls moved to the OTCC (Operational Technology Cybersecurity Controls).
- **Classification:** `Document Classification: Public`, `TLP: White` — no sharing
  restrictions.
- **Language:** this file is the **English edition of an Arabic original**. The document's
  own disclaimer states that the controls are governed by the laws of the Kingdom of Saudi
  Arabia and that *"the Arabic version will be the binding language for all matters relating
  to the meaning or interoperation of this document"*. All text captured here is therefore a
  published English translation, not the legally binding text.
- A separate vendor whitepaper on the older ECC-1:2018 exists elsewhere in the knowledge
  base; it was **not** used. Every row below comes from this file only.

## Schema

The document is a controls catalogue with its own four-level numbering scheme
(`domain-subdomain-control-subcontrol`, e.g. `2-3-2-6`), so the graph mirrors that
hierarchy using the document's own vocabulary.

| Node type | Meaning |
|---|---|
| `Framework` | The instrument itself (ECC-2:2024) with version, issuing authority, TLP marking and binding-language note. |
| `Section` | The front-matter narrative sections: disclaimers, TLP scheme, Update and Review, Executive Summary, Introduction, Objectives, ECC Scope of Work, ECC Statement of Applicability, Implementation and Compliance, Assessment and Compliance Tool, Structure. |
| `MainDomain` | The 4 Cybersecurity Main Domains (1–4). |
| `Subdomain` | The 28 Subdomains, each with its verbatim **Objective**. |
| `Control` | The 108 numbered Main Controls (e.g. `1-1-1`), verbatim. |
| `SubControl` | The 92 numbered Sub-controls (e.g. `2-2-3-1`), each its own clause-level row, verbatim. |
| `Term` | The 70 defined terms of Appendix (A) with verbatim definitions. |
| `Abbreviation` | The 18 abbreviations of Appendix (B). |
| `UpdateEntry` | The 31 rows of Appendix (C): List of Updates against ECC-1:2018. |

| Relationship | From → To |
|---|---|
| `HAS_SECTION` | Framework → Section |
| `HAS_MAIN_DOMAIN` | Framework → MainDomain |
| `HAS_SUBDOMAIN` | MainDomain → Subdomain |
| `HAS_CONTROL` | Subdomain → Control |
| `HAS_SUBCONTROL` | Control → SubControl |
| `DEFINES_TERM` | Framework → Term |
| `HAS_ABBREVIATION` | Framework → Abbreviation |
| `HAS_UPDATE` | Framework → UpdateEntry |
| `UPDATES` | UpdateEntry → the Control / SubControl / Subdomain / Term / Section it changes |
| `CROSS_REFERENCES` | Internal references the text states (control `4-2-3` → Main Domains 1, 2, 3 and Subdomain 4-1; the Statement of Applicability → Subdomain 4-2) |

The counts stated in the document's own Introduction — 4 main domains, 28 subdomains,
108 main controls, 92 sub-controls — match the extracted row counts exactly.

## Files

| File | Rows (excl. header) |
|---|---|
| `nodes_Framework.csv` | 1 |
| `nodes_Section.csv` | 12 |
| `nodes_MainDomain.csv` | 4 |
| `nodes_Subdomain.csv` | 28 |
| `nodes_Control.csv` | 108 |
| `nodes_SubControl.csv` | 92 |
| `nodes_Term.csv` | 70 |
| `nodes_Abbreviation.csv` | 18 |
| `nodes_UpdateEntry.csv` | 31 |
| `rels_HAS_SECTION.csv` | 12 |
| `rels_HAS_MAIN_DOMAIN.csv` | 4 |
| `rels_HAS_SUBDOMAIN.csv` | 28 |
| `rels_HAS_CONTROL.csv` | 108 |
| `rels_HAS_SUBCONTROL.csv` | 92 |
| `rels_DEFINES_TERM.csv` | 70 |
| `rels_HAS_ABBREVIATION.csv` | 18 |
| `rels_HAS_UPDATE.csv` | 31 |
| `rels_UPDATES.csv` | 24 |
| `rels_CROSS_REFERENCES.csv` | 5 |

All ids are unique across the node files and every relationship endpoint resolves to a node
id (verified by script).

## Scope, applicability and compliance (as stated)

Captured verbatim in `nodes_Section.csv`:

- **Scope of work** — applicable to government agencies in the Kingdom (including ministries,
  authorities, establishments and others) and their affiliated companies and entities (inside
  and outside the kingdom), as well as all private sector entities owning, operating or
  hosting Critical National Infrastructures (CNIs); other entities are encouraged to leverage
  them.
- **Statement of applicability** — each entity shall comply with all controls applicable to
  it; the document gives Subdomain (4-2) Cloud Computing and Hosting Cybersecurity as an
  example of applicability that varies by entity.
- **Implementation and compliance** — mandated by Article 10(3) of the NCA's Statute and High
  Order No. 57231 dated 10/11/1439H.; the NCA evaluates compliance via self-assessment,
  periodic reports of the compliance tool and/or field auditing visits, and will issue an
  *ECC-2:2024 Assessment and Compliance Tool*.

## Caveats and gaps

- **No implementation/maturity levels exist in this document.** ECC-2:2024 states a single
  mandatory baseline ("the minimum cybersecurity requirements"); there are no tiers, levels
  or maturity bands to model. The only graded scheme present is the Traffic Light Protocol,
  which is captured as a `Section`.
- **Appendix (C) before/after columns are not captured.** That table is a five-column,
  fully justified layout; in the `-layout` text render the *Previous text* / *Updated text*
  columns interleave on the same physical lines and cannot be split back into cells with
  confidence. Rather than risk garbled or invented text, each `UpdateEntry` records only the
  verbatim *Update type*, *Section* and *Rationale* cells, plus a resolved link to the node
  the change applies to. The current (post-update) wording is already held verbatim on the
  Control / SubControl / Term nodes.
- `UPD-05` (`Modification`, `Control 1-7-2`) is linked to current control `1-7-1`: ECC-1's
  control 1-7-1 was deleted, so the renumbered survivor carries the Appendix (C) "updated
  text" verbatim. Deleted items (ECC-1 controls 1-7-1, 2-7-3, sub-control 4-2-3-3, main
  domain 5, the term *Privacy*, ICS/SIS abbreviations) have no target node, since they do not
  exist in ECC-2 — their `target_reference` is empty by design.
- Sub-control `1-6-3-5` ends without a full stop in the source; it is reproduced as printed.
- Figures 1–4 are images; only their rendered text labels appear (in the `Structure` section).
  Bulleted lists inside long definitions and objectives are flattened to single-line prose,
  wording unchanged.
- The Arabic page furniture (`مقيد - محدود`), page numbers, running heads and the
  `Document classification: Public / TLP: White` footers were stripped as layout artifacts.
