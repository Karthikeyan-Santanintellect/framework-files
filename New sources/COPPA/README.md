# COPPA — knowledge-graph CSV extraction

## What the source document actually is

The source PDF is **not** the COPPA statute (15 U.S.C. 6501–6506) and **not** FTC business
guidance. It is the **Federal Register publication of the FTC's final amended COPPA Rule**:

> Federal Trade Commission, 16 CFR Part 312, RIN 3084–AB20,
> *Children's Online Privacy Protection Rule; Final Rule*,
> Federal Register / Vol. 78, No. 12 / Thursday, January 17, 2013 / Rules and Regulations,
> pages 3972–4014. [FR Doc. 2012–31341]

The document has three parts:

1. the **Statement of Basis and Purpose (SBP)** — a long preamble discussing comments received
   on the 2011 NPRM and 2012 SNPRM, the regulatory analyses (RFA, PRA) and cost estimates;
2. the **regulatory text of 16 CFR Part 312 as amended**, §§ 312.1–312.13, effective July 1, 2013;
3. a **dissenting statement of Commissioner Maureen K. Ohlhausen**.

**This extraction models part 2 — the operative regulatory text of 16 CFR Part 312.** The SBP
preamble and the dissent are commentary/rulemaking history rather than binding provisions, and
extracting them at clause level would produce nodes that are not obligations. The statute itself
(15 U.S.C. 6501 *et seq.*) is present in the document only as citations, so it is represented
only as `ExternalReference` nodes — the statutory section text is not in the source and has not
been supplied from outside knowledge.

Source text used: `pdftotext -layout` extract. The Federal Register is set in three columns; the
regulatory text (source lines 3735–4179) was de-columnised at fixed character offsets (39 / 95 /
150) and re-linearised before extraction, so wording is preserved exactly with column wrapping
rejoined.

## Schema

The document's own vocabulary is *part → section (§) → lettered paragraph → numbered paragraph →
romanette*, plus a block of alphabetically ordered defined terms in § 312.2. The schema mirrors
that.

### Node types

| File | Type | What it holds |
|---|---|---|
| `nodes_Rule.csv` | `Rule` | The part itself: citation, title, issuing authority, authority citation, publication, effective date, statute implemented. |
| `nodes_Section.csv` | `Section` | The 13 sections §§ 312.1–312.13, with verbatim heading and (where the section is a single undivided block, e.g. §§ 312.1, 312.7, 312.8, 312.9, 312.10, 312.13) its full text. |
| `nodes_Provision.csv` | `Provision` | Every lettered/numbered/romanette subdivision that carries text, verbatim, hierarchical via `parent_provision_id`. `heading` carries the italic run-in heading where the document supplies one (e.g. *Methods for verifiable parental consent*, *Exceptions to prior parental consent*, *Criteria for approval of self-regulatory program guidelines*). `level` = depth of subdivision. |
| `nodes_Definition.csv` | `Definition` | The 17 terms defined in § 312.2, each with its verbatim lead-in text. |
| `nodes_DefinitionElement.csv` | `DefinitionElement` | The numbered/romanette subdivisions inside definitions (e.g. the ten enumerated categories of *Personal information*, the seven internal-operations activities), hierarchical via `parent_element_id`. |
| `nodes_Deadline.csv` | `Deadline` | Verbatim time limits and periods stated in the Rule (180 days, 120 days, July 1 2014 annual reporting, three-year recordkeeping, March 1 2013 safe-harbor re-filing, annual assessment). |
| `nodes_ExternalReference.csv` | `ExternalReference` | Statutes cited by the Rule: 15 U.S.C. 6501 et seq., the 6501–6508 authority citation, 6502(a), 6503, 6505, FTC Act §§ 5 and 18(a)(1)(B), 5 U.S.C. 551(1). |

### Relationship types

| File | Rel | Endpoints |
|---|---|---|
| `rels_HAS_SECTION.csv` | `HAS_SECTION` | Rule → Section |
| `rels_HAS_PROVISION.csv` | `HAS_PROVISION` | Section → top-level Provision |
| `rels_HAS_SUBPROVISION.csv` | `HAS_SUBPROVISION` | Provision → Provision |
| `rels_DEFINES.csv` | `DEFINES` | § 312.2 → Definition |
| `rels_HAS_ELEMENT.csv` | `HAS_ELEMENT` | Definition/DefinitionElement → DefinitionElement |
| `rels_HAS_DEADLINE.csv` | `HAS_DEADLINE` | Provision → Deadline |
| `rels_CITES.csv` | `CITES` | Rule/Section → ExternalReference |
| `rels_REFERENCES.csv` | `REFERENCES` | any node → Section/Provision it cross-cites (`cited_as` records the citation as printed) |

### How the topics named in the brief are reachable

* **Definitions** — `nodes_Definition.csv` + `nodes_DefinitionElement.csv` (§ 312.2).
* **Verifiable parental consent** — § 312.5: `312.5(a)` general requirement, `312.5(b)` methods
  (the six enumerated methods at `312.5(b)(2)(i)`–`(vi)`), `312.5(b)(3)` safe-harbor approval of
  new methods, `312.5(c)(1)`–`(8)` exceptions to prior parental consent; plus `312.12(a)` the
  voluntary Commission approval process for new consent methods.
* **Notice** — § 312.4: `(a)` general principles, `(b)` direct notice, `(c)(1)`–`(4)` the four
  direct-notice content sets with their itemised contents, `(d)` online notice with `(d)(1)`–`(3)`.
* **Safe harbor** — § 312.11 `(a)`–`(g)` including the performance standards `(b)(1)`–`(3)`,
  application contents `(c)(1)`–`(4)`, and reporting/recordkeeping `(d)(1)`–`(3)`.
* **Enforcement** — § 312.9 (text on the Section node) plus its `CITES` links to 15 U.S.C. 6503,
  6505, 6502(a) and FTC Act § 18(a)(1)(B).

## Files and row counts

| File | Rows |
|---|---|
| nodes_Rule.csv | 1 |
| nodes_Section.csv | 13 |
| nodes_Provision.csv | 100 |
| nodes_Definition.csv | 17 |
| nodes_DefinitionElement.csv | 36 |
| nodes_Deadline.csv | 7 |
| nodes_ExternalReference.csv | 8 |
| rels_HAS_SECTION.csv | 13 |
| rels_HAS_PROVISION.csv | 24 |
| rels_HAS_SUBPROVISION.csv | 76 |
| rels_DEFINES.csv | 17 |
| rels_HAS_ELEMENT.csv | 36 |
| rels_HAS_DEADLINE.csv | 7 |
| rels_CITES.csv | 6 |
| rels_REFERENCES.csv | 32 |

Total node ids: 182. Validation (unique ids per file; every relationship endpoint resolving to a
node id) passes.

## Caveats and gaps

* **Only the regulatory text is modelled.** The ~36 pages of Statement of Basis and Purpose,
  the Regulatory Flexibility Act / Paperwork Reduction Act analyses and cost estimates, and
  Commissioner Ohlhausen's dissent are present in the source but are not extracted as nodes.
* **The COPPA statute is not in this document.** No text of 15 U.S.C. 6501–6506 has been
  extracted; only the citations the Rule itself makes.
* **No penalties are stated in the Rule.** § 312.9 states only that a violation is treated as a
  violation of a rule defining an unfair or deceptive act or practice under FTC Act
  § 18(a)(1)(B); no monetary figure appears in the regulatory text, so none is recorded.
* **Verbatim quirks preserved.** The published text of the definition of *Support for the internal
  operations of the Web site or online service* reads "(2) So long as The information collected
  …" (capital "The" mid-sentence); § 312.5(c)(6)(iv) reads "where such information is not be used
  for any other purpose"; § 312.11(d)(1) cross-refers to "§ 312.5(b)(4)" although § 312.5(b) ends
  at paragraph (3). These are reproduced as printed and not corrected.
* Cross-references in `rels_REFERENCES.csv` are resolved to the most specific existing node; a
  citation to a paragraph that is not itself a node (e.g. `§ 312.5(b)(4)`) resolves to its
  section, with the printed citation kept in `cited_as`.
* Curly quotes/dashes from the Federal Register typesetting (’ ‘‘ ’’ –) are retained as in source.
* Source: `KB 2/USA/Children's Online Privacy Protection Act.pdf`.
