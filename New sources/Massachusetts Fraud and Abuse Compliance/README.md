# Massachusetts Medical Society — Fraud and Abuse Compliance: Implementing a Compliance Plan (2003)

## What this instrument is — and what it is not

**This is not a cybersecurity framework and not a data-protection framework.** It sits in this knowledge
base among cybersecurity and privacy instruments, but it belongs to a different domain entirely: it is a
**healthcare billing fraud-and-abuse compliance guide for physician practices**, concerned with Medicare
and Medicaid claims, coding, documentation, kickbacks and physician self-referral. It contains nothing
about information security, confidentiality of health data, breach notification or privacy.

**It is not law.** It is a guidance booklet published by a **state professional association** (the
Massachusetts Medical Society), authored by outside counsel. It has no legal force. Where it describes
statutes — the False Claims Act, the Anti-Kickback Statute, the Stark Law, and various Massachusetts
statutes — it *summarises* them in its own words. **No statutory text is reproduced in this document**,
and none has been reproduced in these CSVs. Statutes are therefore modelled as **external references
carrying the manual's own summary**, not as extracted law.

**It carries its own disclaimer**, reproduced verbatim in `nodes_Document.csv`:

> "The information contained in this manual is intended to serve as a general resource and guide. It is
> not to be construed as legal advice. Attorneys with knowledge of the fraud and abuse laws should be
> consulted regarding the application of these laws to specific situations."

**It is from 2003 and is materially out of date.** Every dollar figure, citation, agency name, URL and
enforcement priority in it reflects the law as of 2003. The underlying law has changed substantially
since — including through the Deficit Reduction Act 2005, the Fraud Enforcement and Recovery Act 2009,
the Affordable Care Act 2010 (60-day overpayment rule, Stark and Anti-Kickback amendments), the Bipartisan
Budget Act 2015 penalty inflation adjustments, and the 2020 Stark/Anti-Kickback "Regulatory Sprint" final
rules. Specific artefacts of its age that appear in the data and should **not** be relied on as current:

- Penalty figures quoted as `$5,500–$11,000` per false claim, `$10,000` per item/service civil money
  penalty, and `$15,000` per claim under Stark — all since inflation-adjusted upward.
- **HCFA** (Health Care Financing Administration), which was renamed CMS in 2001; the manual still refers
  to "HCFA 1500" forms and `www.hcfa.gov/medlearn`.
- **ICD-9 / ICD-9-CM** and **CPT-4** coding, since superseded by ICD-10.
- The **OIG Fiscal Year 2002 Work Plan** — a single expired annual enforcement plan.
- URLs (`www.oig.hhs.gov/authorities/docs/physician.pdf`, `http://epls.arnet.gov`) that are dead or moved.
- The manual's own statement that the OIG's compliance guidance is "entirely voluntary" — compliance
  programs later became a statutory condition of enrolment for many providers under the ACA.

Content should be treated as a **historical snapshot of 2003 physician-practice compliance practice**, and
as a record of *how* a compliance program is structured, not as an authority on current US healthcare law.

## Source

`KB 2/USA/MAfraud.PDF` — Massachusetts Medical Society, *Fraud and Abuse Compliance: Implementing a
Compliance Plan (2003)*. Prepared by Paul Shaw, Esq. of Brown, Rudnick, Berlack Israels LLP with the MMS
Office of the General Counsel and Department of Health Policy/Health Systems. ©2003 Massachusetts Medical
Society. Extracted from a `pdftotext -layout` rendering (45 pages of printed content, 1,991 text lines).

## Schema and why

The document is a five-chapter guidance manual, not a statute, so a Part/Section/Sub-clause schema would
misrepresent it. The schema follows the manual's **own** structure and vocabulary — chapters and named
sections, the OIG's "seven elements" presented as numbered **Steps**, named **risk areas**, dated
**Special Fraud Alerts**, an annual **work plan**, and the Chapter 4 **forms** (a sample compliance program,
an employee compliance statement, an in-service training handbook, a code of conduct and a compliance
officer outline). Statutes and OIG publications are pushed out into reference-style node types because
the manual only describes them.

### Node types

| File | Type | Rows | What it holds |
|---|---|---|---|
| `nodes_Document.csv` | Document | 1 | The manual itself, with its verbatim disclaimer, preparation note and copyright |
| `nodes_Chapter.csv` | Chapter | 6 | Introduction + Chapters 1–5, with title and page |
| `nodes_Section.csv` | Section | 19 | Named headings within each chapter (from the table of contents and body) |
| `nodes_ComplianceStep.csv` | ComplianceStep | 7 | The **seven elements of an effective compliance program**, as the OIG's step-by-step approach: Auditing and Monitoring; Written Policies and Procedures; Appointing a Compliance Officer; Training and Education; Responding to Detected Offenses; Open Lines of Communication; Enforcing Disciplinary Standards |
| `nodes_Statute.csv` | Statute | 19 | **External references.** Federal criminal (18 U.S.C. §§ 1347, 1035, 669, 287, 1341/1343, 1518, 1001; 42 U.S.C. § 1320a-7b(a)), Anti-Kickback (42 U.S.C. § 1320a-7(b)), civil False Claims Act, Stark / Stark I / Stark II, and Massachusetts statutes (M.G.L. c. 118E § 21A; M.G.L. c. 175H §§ 2-4; state anti-kickback). Column `description` holds the manual's summary, **not** statutory text |
| `nodes_StatuteClause.csv` | StatuteClause | 13 | Named sub-points the manual makes about a statute (FCA elements of liability, the "knowing/knowingly" standard, Stark's no-intent rule, licensing consequences, etc.) |
| `nodes_Penalty.csv` | Penalty | 6 | Monetary penalties and exclusion periods as stated in 2003 |
| `nodes_ExclusionGround.csv` | ExclusionGround | 18 | 4 mandatory + 14 permissive exclusion grounds |
| `nodes_SafeHarbor.csv` | SafeHarbor | 8 | The Anti-Kickback safe harbour categories the manual lists |
| `nodes_DesignatedHealthService.csv` | DesignatedHealthService | 10 | The ten Stark II "designated health services" |
| `nodes_RiskArea.csv` | RiskArea | 31 | The four core risk areas; the OIG coding/billing risk areas; reasonable-and-necessary, documentation, HCFA 1500, inducements; the appendix risk areas (LMRP, ABN, incentive arrangements, third-party billing, professional courtesy); and the nine risk areas restated in the Chapter 4 handbook |
| `nodes_GuidanceItem.csv` | GuidanceItem | 27 | Bulleted requirements/checklist items hanging off a risk area (documentation guidelines, HCFA 1500 checks, the four ABN requirements, suspect incentive arrangements, professional-courtesy observations) |
| `nodes_Example.csv` | Example | 45 | Every illustrative example of prohibited conduct the manual gives, typed as *Prohibited conduct*, *OIG example*, *Violation example*, etc. These are the document's own hypotheticals ("Dr. X", "a podiatrist") — no instance data was invented |
| `nodes_FraudAlert.csv` | FraudAlert | 7 | The dated OIG Special Fraud Alerts summarised (1989–2000) |
| `nodes_WorkPlanItem.csv` | WorkPlanItem | 9 | OIG Fiscal Year 2002 Work Plan focus areas |
| `nodes_Form.csv` | Form | 5 | The Chapter 4 sample documents |
| `nodes_FormClause.csv` | FormClause | 21 | Clause-level content of those forms — the nine numbered provisions of the Sample Fraud and Abuse Compliance Program, the three paragraphs of the Compliance Statement, the handbook sections and the sample Code of Conduct |
| `nodes_ProgramComponent.csv` | ProgramComponent | 9 | The nine "Compliance Program Components" listed in the training handbook, with their explanatory text |
| `nodes_OfficerResponsibility.csv` | OfficerResponsibility | 14 | The Outline of Compliance Officer Responsibilities (compliance notebook, legal review of contracts, audits, investigations, screening, exit interviews, etc.) |
| `nodes_Definition.csv` | Definition | 14 | Every term the manual actually defines: false claim, knowing/knowingly, referral, remuneration, fair market value, reasonable and necessary, upcoding, unbundling, clustering, double billing, modifier, professional courtesy, moonlighting, compliance program |
| `nodes_ExternalReference.csv` | ExternalReference | 10 | OIG guidance and work plans, the Medicare Learning Network, LEIE and EPLS exclusion lists, the HHS/DOJ HCFAC FY2001 annual report (source of the enforcement statistics), and the four MMS support services |
| `nodes_Statement.csv` | Statement | 13 | Chapter-level narrative propositions not attached to a step (voluntariness, flexibility, scaling to practice size, the Chapter 5 conclusions) |

### Relationship files

| File | Rows | Relationship types |
|---|---|---|
| `rels_contains.csv` | 43 | `HAS_CHAPTER`, `HAS_SECTION`, `HAS_STATEMENT`, `HAS_FORM` |
| `rels_has_step.csv` | 7 | `HAS_STEP` (carries `step_number`) |
| `rels_statute_structure.csv` | 34 | `DESCRIBES_STATUTE`, `HAS_CLAUSE`, `HAS_PART` (Stark → Stark I/II) |
| `rels_penalties.csv` | 24 | `HAS_PENALTY`, `HAS_GROUND` |
| `rels_scope.csv` | 18 | `HAS_SAFE_HARBOR`, `COVERS_DESIGNATED_SERVICE` |
| `rels_risk_areas.csv` | 69 | `IDENTIFIES_RISK_AREA`, `HAS_GUIDANCE_ITEM`, `ADDRESSES_RISK_AREA`, `RELATES_TO_STATUTE` |
| `rels_examples.csv` | 45 | `HAS_EXAMPLE` |
| `rels_oig_initiatives.csv` | 21 | `LISTS_FRAUD_ALERT`, `IMPLICATES_STATUTE`, `LISTS_WORK_PLAN_ITEM` |
| `rels_forms.csv` | 56 | `HAS_CLAUSE`, `LISTS_COMPONENT`, `HAS_RESPONSIBILITY`, `CORRESPONDS_TO_STEP`, `REVIEWS_AGAINST`, `USES_REFERENCE` |
| `rels_definitions.csv` | 14 | `DEFINES` |
| `rels_references.csv` | 20 | `CITES` |

**Totals:** 22 node files / 312 nodes; 11 relationship files / 351 relationships.

## Sample policies and checklists provided by the manual

The manual supplies ready-to-adopt forms, all captured in `nodes_Form.csv` / `nodes_FormClause.csv`:

1. **Sample Fraud and Abuse Compliance Program** — nine numbered provisions (Policy Statement; Compliance
   with Documentation, Coding, Billing…; Compliance Officer; Standards of Conduct; Education; Internal
   Reporting and Corrective Action; Auditing and Monitoring; Disciplinary Action; Government Investigations),
   ending "APPROVED AND ADOPTED: __________, 2003".
2. **Compliance Statement** — an employee acknowledgement form with signature blocks.
3. **Fraud and Abuse Compliance Program Educational Handbook (In-Service Training)**.
4. **Sample Code of Conduct Relating to Coding and Billing Practices**.
5. **Outline of Compliance Officer Responsibilities** — effectively an operational checklist.

Audit checklists appear as `nodes_OfficerResponsibility.csv` rows (`od_monitoring_auditing`,
`od_corrective_actions`, `od_investigation`, `od_screening`) and in `nodes_GuidanceItem.csv`.

## Caveats and gaps

- **No statutory text.** Only the manual's paraphrases. Anyone needing operative law must go to the
  statutes themselves — and to their post-2003 versions.
- **Numbering.** Only the sample program's nine provisions, the ten designated health services and the
  seven steps carry document-assigned numbers. Bulleted items are unnumbered in the source; synthetic ids
  (`gi_doc_1` …) were assigned to make them addressable, but **no numbering was invented in any text field**.
- **Duplication is real, not an artefact.** Risk areas, the Anti-Kickback description and the disciplinary
  provisions appear two or three times — in Chapter 1, Chapter 3 and again in the Chapter 4 handbook. These
  are kept as distinct nodes with distinct `listing` values because their wording differs and they serve
  different audiences (physician vs. staff training). A `ra_hb_*` node is the handbook restatement of a
  `ra_cb_*` risk area, not a duplicate row.
- **The "seven elements" are presented flexibly.** The manual stresses the OIG "takes a more flexible
  approach" for small practices and that "some practices may never fully implement all of the [seven]
  components." The steps should not be read as mandatory controls.
- **Chapter 4 form blanks** (`_________________ [insert name]`, `[Board of Directors]`) are preserved
  verbatim as they appear; they are template placeholders, not missing data.
- **Source typos preserved verbatim** per the verbatim-only rule: "Embesslement" (for Embezzlement, §669
  heading), "Filling for services" (for Filing), "Our advise is simple" (for advice), and "have not have
  been followed". These are the document's errors, not extraction errors.
- **Statute citations reproduced as printed.** The manual cites the Anti-Kickback Statute as
  42 U.S.C. §1320a-7(b) and the criminal False Claims Act as 18 U.S.C. § 287; both are recorded as given.
- No OCR noise or column-wrap corruption was found; the layout extract was clean and page
  headers/footers/running titles were stripped during extraction.

## Validation

`check_mafraud.py` parses every CSV, asserts each node file's first column is `<type>_id`, asserts id
uniqueness within each file, asserts every relationship `source_id`/`target_id` resolves to a node id, and
asserts every relationship file's first three columns are `source_id,target_id,rel_type`. Result: **all
312 node ids unique, all 702 relationship endpoints resolve, 0 errors.**
