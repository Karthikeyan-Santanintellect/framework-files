# Source Audit — KB 2 / KB 3 vs. this repository

What exists in the knowledge base (`source-verifier/KB 2/` and `source-verifier/KB 3/`) against
what has actually been extracted into this repository, so the remaining work is explicit.

*This folder holds the extracted CSVs for every instrument listed below as ❌ in the original
audit. Drop new source documents here and update the tables as they are extracted.*

**Audit date:** 2026-07-21 · **Extraction pass completed:** 2026-07-21 · **Loaded into Neo4j:** 2026-07-21
**Knowledge base:** 128 files — 126 PDFs (KB 2: 117 across 25 jurisdiction folders, 150 MB · KB 3: 9, 20 MB)
plus one `.zip` and one `.xlsx`
**Rows are instruments, not files.** Where one instrument ships as several PDFs (Mexico's law
LFPDPPP comes as 4, FISMA as 6, CMMC as 4) they are grouped into a single row and the file count noted.

> ## ⚠️ Superseded in part — extraction pass, 2026-07-21
>
> All 64 missing instruments below have since been extracted into folders in this directory
> (see [README.md](README.md)). Doing so forced every source file open, which revealed that
> **eight documents are not the instrument their filename claims**. The affected rows below are
> annotated inline with **[CORRECTED]**. The headline consequence: the **KVKK statute, POPIA Act,
> India IT Act, Australian Privacy Act, DO-178C standard, COSO framework body and UN R156 are
> absent from the knowledge base** — the files bearing those names contain something else.

## Summary

| Status | Count | Meaning |
|---|---:|---|
| ✅ **Done** | **26** | Extracted, verified against its source in `verdict.md`, and loaded into Neo4j |
| ✅ **Extracted and loaded** | **64** | Built in this pass into `New sources/`, given a loader in `App_new/`, and **loaded into Neo4j on 2026-07-21** — not yet verified in `verdict.md` |
| ✅ **Verified and loaded** | **2** | `201 CMR 17` and `42 CFR Part 2` — verified against their source regulation and **loaded into Neo4j on 2026-07-23** |
| ⚠️ **Built, not verified** | **2** | CSVs exist elsewhere in the repo, never verified in `verdict.md` and **not in the graph** |
| 📎 **Supporting material** | **13** | Secondary/duplicate documents that do not warrant their own framework |

**Nothing in the knowledge base is now unextracted.** The 64 formerly-missing instruments produced
**59,203 CSV node rows / 75,675 CSV relationship rows** across 64 folders — see [README.md](README.md).
Loaded, they are **59,194 nodes / 74,977 relationships**; the difference is explained under
[Loading into Neo4j](#loading-into-neo4j) and is a property of the source data, not of the load.

**The graph now holds 92 frameworks** — the 26 originally verified, the 64 from this pass, and
`201 CMR 17` and `42 CFR Part 2` (verified and loaded 2026-07-23). Three further **source
catalogues** (DTOP Sources, Enterprise Sources, Assessments and Questionnaires) are also in the
graph but are not compliance frameworks — see [README.md](../README.md).

**KB 3 is fully consumed** — all 9 files map to a completed framework. Every gap below is in KB 2.

Coverage by document count: of the 128 files, 25 back a completed framework, 2 back an unverified
one, 16 are supporting material, and the remaining **85 were extracted in this pass** into the 64
instrument folders here. Every file in the knowledge base is now either extracted or explicitly
classified as supporting material.

---

## ✅ Done (26)

Verified and loaded. Full per-framework findings are in [verdict.md](../verdict.md).

| # | Framework | Repo folder | Source |
|---|---|---|---|
| 1 | CIS Controls | `CIS Controls` | KB 2/Europe/CIS_Controls_Guide_v8.1.2_0325_v2.pdf |
| 2 | CPA | `CPA` | KB 2/USA/CPA.pdf |
| 3 | CPRA | `CPRA` | KB 3/CPRA - California Prop 24 (2020).pdf |
| 4 | DORA | `DORA` | KB 2/Europe/DORA.pdf |
| 5 | DPDPA | `DPDPA` | KB 2/India/Digital Personal Data Protection Act (DPDPA).pdf |
| 6 | GDPR | `GDPR` | KB 2/Europe/GDPR.pdf |
| 7 | GLBA | `GLBA` | KB 2/USA/GLBA.pdf |
| 8 | HIPAA | `HIPAA` | KB 2/USA/HIPAA.pdf + 45 CFR 164 C/D, 160 D *(fetched externally)* |
| 9 | HITECH | `HITECH` | KB 2/USA/HITECH.pdf |
| 10 | HITRUST | `HITRUST` | KB 2/USA/HITRUST CSF v11.6.0/CSF PDF v11.6.0.pdf |
| 11 | ISO 27001 | `ISO 27001` | KB 3/ISO IEC 27001-2022 (Information Security Management Systems).pdf |
| 12 | ISO 27002 | `ISO 27002` | KB 3/ISO IEC 27002-2022 (Information Security Controls).pdf |
| 13 | NERC CIP | `NERC` | KB 3/NERC CIP Reliability Standards (CIP-002 to CIP-014).pdf |
| 14 | NIST AI RMF | `NIST AI RMF` | KB 2/Europe/NIST AI Risk Management Framework.pdf |
| 15 | NIST CSF 2.0 | `NIST CSF 2.0` | KB 2/Europe/NIST CSF 2.0.pdf |
| 16 | NIST PMF 1.0 | `NIST PMF 1.0` | NIST CSWP 10 *(fetched externally — not in the KB)* |
| 17 | NIST PMF 1.1 | `NIST PMF 1.1` | KB 3/NIST Privacy Framework 1.1 (CSWP 40 IPD).pdf |
| 18 | NIST RMF | `NIST RMF` | KB 2/Europe/NIST RMF SP.800-37r2.pdf |
| 19 | NIS 2 | `NIS_2` | KB 2/Europe/NIS2 Directive (Network and Information Security).pdf |
| 20 | PCI DSS | `PCI - DSS` | KB 3/PCI DSS v4.0.1 (June 2024).pdf |
| 21 | SCF | `SCF` | KB 3/SCF Recommended Practices.pdf + SCF 2025.4 workbook *(fetched externally)* |
| 22 | SEC Cyber Rule | `SEC` | KB 3/SEC Cybersecurity Risk Management Disclosure Rule 2023.pdf |
| 23 | SHIELD | `SHIELD` | KB 2/USA/NY Shield Act.pdf |
| 24 | TDPSA | `TDPSA` | KB 3/TDPSA - Texas HB4 (Business & Commerce Code Ch541).pdf |
| 25 | TISAX | `TISAX` | KB 2/Germany/TISAX Participant Handbook.pdf |
| 26 | VCDPA | `VCDPA` | KB 2/USA/VCDPA.pdf + Va. Code §§59.1-575…585 *(fetched externally)* |

Two of these needed a source the KB did not hold: **NIST PMF 1.0** (the KB file at that path is
actually the 1.1 draft) and **SCF** (the control catalog ships only as a workbook). Both were
retrieved externally. **NERC** was unresolvable until the CIP Reliability Standards were added
to KB 3 on 2026-07-21.

## ✅ Verified and loaded 2026-07-23 (2)

Both had their extraction sitting in the repo unverified and unloaded. On 2026-07-23 each was
checked against the structure of its source regulation, its loader was rewritten (the earlier
drafts were broken — `201_cmr.py` loaded from empty file paths and created a `Resident` in place
of the Service Provider; `42cfr.py` matched a `Regulation` label it never created and joined every
subpart to every section with a cartesian MERGE), and loaded into Neo4j.

| Framework | Repo folder | Loader | `regional_standard_regulation_id` | In graph | Verification |
|---|---|---|---|---|---|
| 201 CMR 17 | `201 CMR 17` | `App_new/201_cmr.py` | `201 CMR 17.00` | 18 nodes / 19 rels | 17 concept nodes match the 17.02 definitions and 17.03–17.04 requirements; no orphans |
| 42 CFR Part 2 | `42 CFR Part 2` | `App_new/42cfr.py` | `42_CFR_PART_2` | 70 nodes / 69 rels | Subparts A–E and sections 2.1–2.68 match the real Part 2 structure; section→subpart inferred from the section number and confirmed exact |

## ⚠️ Built, not verified (2)

CSVs exist in the repo but these never went through `verdict.md` verification and **neither is in
the Neo4j instance**. They are the only remaining framework folders in the repo that are not in the
graph — both because their standard is absent from the knowledge base.

| Framework | Repo folder | CSVs | Loader | Source in KB | Gap |
|---|---|---:|---|---|---|
| ISO 42001 | `ISO 42001` | 5 | `App_new/iso42001.py` | **none — no ISO 42001 PDF in the KB** | Unverifiable without a source |
| ISO 27701 | `ISO 27701` | 8 | **none** | **none — no ISO 27701 PDF in the KB** | No loader *and* no source |

Two of the four (201 CMR 17, 42 CFR Part 2) have their source in the KB and could be verified
and loaded immediately. ISO 42001 and ISO 27701 would need their standards obtained first.

---

## ✅ Extracted and loaded in this pass (64) — formerly ❌ Missing

**Every row below has been built** into a folder in this directory **and loaded into Neo4j**. They
are listed here in their original audit grouping; the status of the whole section changed from
❌ Missing to 🟦 Extracted (2026-07-21) and then to ✅ Loaded the same day.

The node counts quoted per row are **CSV rows**. Nine of them do not become separate nodes — see
[Loading into Neo4j](#loading-into-neo4j).

All 64 were opened and read in full during extraction, so **every row is now content-verified** —
the `✔ content-verified` marks below record which ones had *already* been verified at audit time.
Rows marked **[CORRECTED]** are those where reading the file proved the original audit entry wrong.

### Americas — USA (23)

| Instrument | Files | Notes |
|---|---:|---|
| NIST SP 800-53r5 — Security and Privacy Controls | 1 | The control catalog behind NIST RMF; the RMF graph currently carries only 20 sample controls · **→ `NIST SP 800-53r5/` (3,512 nodes)** |
| NIST SP 800-171r3 — Protecting CUI | 1 | Prerequisite for CMMC Level 2 · **→ `NIST SP 800-171r3/` (1,406 nodes)** |
| NIST SP 800-207 — Zero Trust Architecture | 1 | · **→ `NIST SP 800-207/` (184 nodes)** |
| CMMC 2.0 | 4 | ✔ content-verified — DoD Model Overview v2.13 (Sept 2024), v2.0 (2021), a CMMC 2.0 brief and a COGR October 2025 update · **→ `CMMC 2.0/` (516 nodes)** |
| FISMA | 6 | ✔ content-verified — the enacted Public Law 113-283 (2014) plus S.2902 (117th Congress) and four FY25 CIO/IG/SAOP metrics documents · **→ `FISMA/` (2,139 nodes)** |
| FedRAMP | 1 | **[CORRECTED]** ✔ content-verified — **not a standard, baseline, playbook or CONOPS**. A 13-slide program-overview briefing deck (Aug 2023). No control baselines exist in it · **→ `FedRAMP/` (141 nodes)** |
| SOC 2 | 1 | ✔ content-verified — AICPA TSP Section 100, *2017 Trust Services Criteria* · **→ `SOC 2 Trust Services Criteria/` (474 nodes)** |
| Sarbanes-Oxley Act | 1 | · **→ `Sarbanes-Oxley Act/` (672 nodes)** |
| COSO ERM | 2 | **[CORRECTED]** ✔ content-verified — the first file is **Appendices Volume II only**: no components, no principles, no glossary. The 5 components and 20 principles exist only in the second file (the Compliance Risk Management application paper) · **→ `COSO ERM/` (890 nodes)** |
| FFIEC Cybersecurity Assessment Tool | 1 | · **→ `FFIEC Cybersecurity Assessment Tool/` (873 nodes)** |
| NAIC Insurance Data Security Model Law | 1 | · **→ `NAIC Insurance Data Security Model Law/` (174 nodes)** |
| COPPA — Children's Online Privacy Protection Act | 1 | · **→ `COPPA/` (182 nodes)** |
| FERPA | 2 | ✔ content-verified — **both files are ED guidance** (a Parent Guide and an Eligible Student Guide), **not the statute**; the statutory text is absent · **→ `FERPA (guidance)/` (151 nodes)** |
| 21 CFR Part 11 — Electronic Records / Signatures | 2 | ✔ content-verified — eCFR authoritative text + FDA *Scope and Application* guidance · **→ `21 CFR Part 11/` (152 nodes)** |
| FDA Cybersecurity for Medical Devices | 1 | · **→ `FDA Medical Device Cybersecurity/` (419 nodes)** |
| CPNI Rules | 1 | ✔ content-verified — FCC 01-247 order, not the codified 47 CFR 64.2001–2011 rules · **→ `CPNI Rules/` (279 nodes)** |
| DFARS | 1 | ✔ content-verified — Volume III, Parts 201–253 · **→ `DFARS/` (16,535 nodes)** |
| ITAR | 1 | ✔ content-verified — amended through 2 Oct 2025 · **→ `ITAR/` (3,353 nodes)** |
| DO-178C — Airborne Systems Software | 1 | **[CORRECTED]** ✔ content-verified — **not the standard**. A Parasoft marketing ebook; the Annex A objectives tables are page images with no text layer. The DO-178C standard is absent from the KB · **→ `DO-178C/` (416 nodes)** |
| MITRE ATT&CK | 1 | ⛔ image-only PDF. **[EXTRACTED via OCR]** — 206 of the source's own stated 235 techniques recovered, each with an OCR confidence flag · **→ `MITRE ATTACK/` (221 nodes)** |
| Massachusetts Boards of Health — Manual of Laws | 1 | ✔ content-verified — MAHB 2016 manual; a public-health law compendium, not a cyber/privacy framework · **→ `Massachusetts Boards of Health Manual/` (372 nodes)** |
| Massachusetts fraud & abuse compliance manual | 1 | ✔ content-verified — Massachusetts Medical Society (2003); healthcare billing compliance, not cyber/privacy · **→ `Massachusetts Fraud and Abuse Compliance/` (312 nodes)** |
| CCPA | 1 | ✔ content-verified — CCPA of 2018 as amended effective 01/01/2025. **Largely covered already**: the `CPRA` folder models Civil Code 1798.100–.199.40. Worth diffing for the 2025 SB 1223 / AB 1008 / AB 1824 amendments the 2020 text lacks · **→ `CCPA 2025/` (716 nodes)** |

### Americas — Latin America & Canada (6)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| PIPEDA | Canada | 1 | · **→ `Canada PIPEDA/` (640 nodes)** |
| Mexico LFPDPPP (private parties) | Mexico | 4 | ✔ content-verified — **new law, DOF 20-03-2025** plus the 2011 Regulations, an evolution note and an EU-Mexico comparison · **→ `Mexico LFPDPPP/` (1,075 nodes)** |
| Mexico LGPDPPSO (obligated subjects) | Mexico | 1 | ✔ content-verified — General Law, DOF 20-03-2025; a separate instrument from the above · **→ `Mexico LGPDPPSO/` (700 nodes)** |
| Brazil LGPD (Lei 13.709/2018) | Brazil | 2 | ✔ content-verified — Portuguese consolidated text + a second copy · **→ `Brazil LGPD/` (516 nodes)** |
| Colombia Ley 1581 de 2012 | Colombia | 1 | ✔ content-verified — Spanish statutory text · **→ `Colombia Ley 1581/` (284 nodes)** |
| Argentina Personal Data Protection Act 2000 | Argentina | 1 | · **→ `Argentina PDPA/` (265 nodes)** |

### Europe, UK & Germany (7)

| Instrument | Files | Notes |
|---|---:|---|
| EU Artificial Intelligence Act | 1 | Largest remaining EU gap; pairs with the existing NIST AI RMF graph · **→ `EU AI Act/` (1,774 nodes)** |
| EU Cyber Resilience Act | 1 | · **→ `EU Cyber Resilience Act/` (978 nodes)** |
| eIDAS Regulation | 1 | · **→ `eIDAS Regulation/` (598 nodes)** |
| ENISA European Cybersecurity Skills Framework | 1 | User manual · **→ `ENISA ECSF/` (246 nodes)** |
| UK NIS Regulations 2018 | 1 | UK counterpart to the completed NIS 2 graph · **→ `UK NIS Regulations 2018/` (1,031 nodes)** |
| UK Cyber Essentials | 1 | ✔ content-verified — NCSC *Requirements for IT Infrastructure v3.3* · **→ `UK Cyber Essentials/` (241 nodes)** |
| BSI C5 — Cloud Computing Compliance Controls Catalogue | 1 | Germany; the only KB 2/Germany source besides the completed TISAX handbook · **→ `BSI C5/` (1,305 nodes)** |

### Asia-Pacific (15)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| Information Technology Act 2000 | India | 1 | **[CORRECTED]** ✔ content-verified — **not the Act**. Four Gazette notifications of 17 Oct 2000 (commencement, Certifying Authorities Rules + Schedules I–V, Advisory Committee, Appellate Tribunal Procedure Rules). No sections, no s.2 definitions, no offence provisions. The IT Act is absent from the KB · **→ `India IT Act 2000/` (1,255 nodes)** |
| RBI Cybersecurity Framework for Banks | India | 1 | · **→ `RBI Cybersecurity Framework/` (214 nodes)** |
| SEBI Cybersecurity & Cyber Resilience Framework | India | 1 | · **→ `SEBI Cybersecurity Framework/` (887 nodes)** |
| PIPL — Personal Information Protection Law | China | 1 | · **→ `China PIPL/` (282 nodes)** |
| Data Security Law | China | 1 | · **→ `China Data Security Law/` (192 nodes)** |
| APPI | Japan | 1 | · **→ `Japan APPI/` (245 nodes)** |
| PIPA | South Korea | 1 | · **→ `South Korea PIPA/` (915 nodes)** |
| PDPA | Singapore | 1 | · **→ `Singapore PDPA/` (1,392 nodes)** |
| MAS Technology Risk Management Guidelines | Singapore | 1 | · **→ `MAS TRM Guidelines/` (433 nodes)** |
| PDP Law | Indonesia | 1 | · **→ `Indonesia PDP Law/` (512 nodes)** |
| PDPA | Thailand | 1 | · **→ `Thailand PDPA/` (569 nodes)** |
| Australian Privacy Act 1988 + NDB scheme | Australia | 4 | **[CORRECTED]** ✔ content-verified — **none of the four files contain the Act**. The main file is the OAIC *APP Guidelines* (expressly non-binding); the others are an AMSRO factsheet, a **Fortinet vendor white paper** and the OAIC statistics report. The Privacy Act 1988 is absent from the KB · **→ `Australia Privacy Act 1988/` (1,135 nodes)** |
| APRA Prudential Standard CPS 234 | Australia | 1 | · **→ `APRA CPS 234/` (144 nodes)** |
| ASD Essential Eight Maturity Model | Australia | 1 | · **→ `ASD Essential Eight/` (338 nodes)** |
| Philippines Data Privacy Act 2012 — IRR | Philippines | 1 | ✔ content-verified — the final IRR only (a July 2016 draft is listed under supporting material). **The Act itself (RA 10173) is not in the KB** · **→ `Philippines DPA IRR/` (452 nodes)** |

### Middle East, Africa & International (13)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| UAE Federal Decree-Law 45/2021 (PDPL) | UAE | 1 | · **→ `UAE PDPL/` (229 nodes)** |
| DIFC Data Protection Law | UAE | 1 | Separate free-zone regime · **→ `DIFC Data Protection Law/` (847 nodes)** |
| ADGM Data Protection Regulations | UAE | 1 | Separate free-zone regime · **→ `ADGM Data Protection Regulations/` (748 nodes)** |
| Qatar Personal Data Privacy Protection Law | Qatar | 1 | · **→ `Qatar PDPPL/` (150 nodes)** |
| Bahrain Personal Data Protection Law | Bahrain | 1 | · **→ `Bahrain PDPL/` (479 nodes)** |
| NCA Essential Cybersecurity Controls (ECC-2:2024) | Saudi Arabia | 1 | ✔ content-verified — the current ECC-2:2024 controls · **→ `Saudi NCA ECC-2 2024/` (364 nodes)** |
| Turkey KVKK | Turkey | 1 | **[CORRECTED]** ✔ content-verified — **not the statute**. A 26-page journal article (Evren 2023, *Kişisel Verileri Koruma Dergisi* 5(2)) comparing GDPR and KVKK; it never reproduces a Madde's operative text. Law 6698 is absent from the KB · **→ `Turkey KVKK/` (286 nodes)** |
| Switzerland revised FADP | Switzerland | 1 | · **→ `Switzerland revFADP/` (572 nodes)** |
| Russia Federal Law 152-FZ | Russia | 2 | ✔ content-verified — one is an unofficial English translation · **→ `Russia 152-FZ/` (331 nodes)** |
| Kenya Data Protection Act | Kenya | 1 | · **→ `Kenya Data Protection Act/` (586 nodes)** |
| Nigeria Data Protection Act 2023 | Nigeria | 3 | ✔ content-verified — the 2023 Gazette text and the 2024 GAID implementation directive. **`Nigeria_DPA.pdf` is image-only with zero extractable text** · **→ `Nigeria Data Protection Act 2023/` (1,405 nodes)** |
| South Africa POPIA | South Africa | 1 | **[CORRECTED]** ✔ content-verified — **not the Act**. The 2025 *Amendment of the Regulations* under s 113(3): no chapters, no s 1 definitions, no eight conditions, no offences. The POPIA Act is absent from the KB · **→ `South Africa POPIA/` (159 nodes)** |
| UNECE WP.29 — UN Regulation 155 | International | 1 | **[CORRECTED]** ✔ content-verified — Add.154 contains **R155 only**. R156 (Software Update Management) is a separate addendum (Add.155) and is **absent from the KB**, despite the filename naming both · **→ `UNECE UN R155/` (340 nodes)** |

---

## 📎 Supporting material (13 rows · 16 files)

Present in the KB but not instruments in their own right — duplicates, secondary commentary,
superseded versions or documents attached to an already-completed framework.

| File | Relates to | Why it is not a framework |
|---|---|---|
| KB 2/USA/NERC CIP.pdf | NERC (done) | The *CIP Roadmap — 2025 Work Plan Priority*; superseded by the KB 3 Standards |
| KB 2/Europe/NIST Privacy Framework.pdf | NIST PMF 1.1 (done) | Mislabeled — it is the 1.1 draft, a duplicate of the KB 3 file |
| KB 2/Europe/NIST.AI.600-1.pdf | NIST AI RMF (done) | The Generative AI Profile, an extension of AI RMF 1.0 |
| KB 2/USA/HITRUST CSF v11.6.0/ — 4 further files | HITRUST (done) | Version-comparison, summary of changes, introduction, authoritative-sources cross-reference |
| KB 2/USA/HITRUST CSF v11.6.0.zip | HITRUST (done) | Archive of the folder above |
| KB 2/Saudi Arabia/NCA-Compliance-Whitepaper-1.pdf | Saudi ECC | ✔ verified — a vendor whitepaper on the superseded ECC-1:2018 |
| KB 2/South America/2020-colombia-en-faq.pdf | Colombia | ✔ verified — an EFF report on communication-privacy law, not the statute |
| KB 2/South America/DLA-Piper-Data-Protection-Laws-of-the-World-Colombia.pdf | Colombia | Law-firm summary |
| KB 2/Mexico/DLA-Piper-Data-Protection-Laws-of-the-World-Mexico.pdf | Mexico | Law-firm summary |
| KB 2/Mexico/eu_-_mexico-_gdpr_v._federal_law_and_regulations_ (1).pdf | Mexico | Duplicate of the file without the `(1)` suffix |
| KB 2/Mexico/PDP-Public_03-21-2025_GoogleTranslate (1).pdf | Mexico | Duplicate |
| KB 2/Africa/SECTION-112_2_C_-HEALTH-REGULATIONS-FINAL-1.pdf | South Africa | ✔ verified — a 26 Sept 2025 *invitation for public comment* on draft POPIA health regulations, not enacted law |
| KB 2/Philippines/updated-draft-July-12-2016.pdf | Philippines | ✔ verified — a draft of the IRR superseded by the final version |

---

## Loading into Neo4j

All 64 were loaded on 2026-07-21. Each folder has its own loader at `App_new/<slug>.py`
(e.g. `App_new/coppa.py`, `App_new/eu_ai_act.py`), spelling out that framework's own Cypher: one
`MERGE` per `nodes_<Label>.csv` and one per distinct `rel_type`. Run any of them with `--dry-run`
to validate without writing.

| Tool | Purpose |
|---|---|
| `App_new/tools/gen_new_source_loaders.py` | Authors the 64 loaders from the CSV headers on disk. Re-run after any re-extraction; edit the generator, never a generated file |
| `App_new/tools/validate_new_sources.py` | Offline dry-run — coverage, row counts, dangling endpoints, reconciliation against this file, `--check-urls` |
| `App_new/tools/load_new_sources.py` | Runs all 64 smallest-first; `--only`, `--skip-loaded` |
| `App_new/tools/verify_new_sources_graph.py` | Read-only reconciliation of the graph against the loaders |
| `App_new/tools/repair_stranded_nodes.py` | Deletes nodes whose `framework_id` is not one of the 64 |

**Graph conventions.** Every node carries `framework_id` and an anchor label `:NewSourceNode`,
merged on `(framework_id, node_id)`. The anchor is what makes relationship endpoints resolvable:
the `rels_*.csv` files record no endpoint labels, and 153 relationship types legitimately span
several labels. Each folder also gets one `:NewSourceFramework` root node linked by `HAS_ROOT` to
every node nothing else points at, so any of the 64 can be traversed or deleted on its own. The
root deliberately does **not** use the bare `:Framework` label — four folders ship a node of their
own under that label. Loads are idempotent; re-running repairs a partial load rather than
duplicating it.

### Why the graph holds fewer rows than the CSVs

**59,194 nodes / 74,977 relationships** loaded, against 59,203 / 75,675 CSV rows. Every difference
is a property of the source data, and `MERGE` handling it this way is correct.

| Framework | CSV rows | In graph | Cause |
|---|---:|---:|---|
| DFARS | 18,208 rels | 17,558 | 650 citations with a blank `target_id` (e.g. `PGI 201.106`) — nothing in-corpus to attach to |
| CMMC 2.0 | 1,518 rels | 1,484 | 34 repeated `(source, target, rel_type)` triples |
| FISMA | 2,360 rels | 2,350 | 10 repeated triples |
| UNECE UN R155 | 455 rels | 452 | 3 repeated triples |
| DO-178C | 370 rels | 369 | 1 triple appearing in two different `rels_*.csv` files |
| EU AI Act | 1,774 nodes | 1,766 | `annexIII_1..8` appear in both `nodes_Point.csv` and `nodes_HighRiskArea.csv` — one entity, two labels, identical text and `source_line` |
| UK NIS Regulations 2018 | 1,031 nodes | 1,030 | `sch2p9` appears in both `nodes_Provision.csv` and `nodes_SchedulePara.csv` — same paragraph, same citation |

### Data hazards the load exposed

Worth knowing before extracting anything new:

- **`rel_type` is authoritative, the filename is not.** 397 of the 481 `rels_*.csv` files carry a
  type that differs from their name, and many carry several types in one file.
- **A column named `framework_id` collides with the graph key.** Four folders
  (`MITRE ATTACK`, `ASD Essential Eight`, `Saudi NCA ECC-2 2024`, `SEBI Cybersecurity Framework`)
  have a `nodes_Framework.csv` whose id column is literally `framework_id`. Written through, it
  overwrites the merge key and strands the node outside its own framework. The generator now emits
  it as `csv_framework_id` and the validator fails if this regresses.

## Data-quality flags

Issues that will block or distort extraction and are worth resolving before the work starts.

| Flag | Affected | Impact |
|---|---|---|
| ⛔ **Image-only PDFs** | `KB 2/USA/Mitre Att&ck.pdf`, `KB 2/Africa/Nigeria_DPA.pdf` | Zero extractable text — `pdftotext` returns nothing. Needs OCR or a replacement source. Nigeria is unaffected in practice because the Gazette text is present in another file; MITRE ATT&CK has no alternative in the KB |
| ⚠️ **Guidance instead of statute** | FERPA (both files), CPNI, Philippines DPA | The authoritative text is absent; extracting these would produce a graph of guidance, exactly the scope mismatch that made HIPAA and HITECH difficult |
| ⚠️ **Filename ≠ content** | `NERC CIP.pdf`, `NIST Privacy Framework.pdf` | Two confirmed cases. Any new extraction should verify the cover page first |
| ⚠️ **Exact duplicates** | 3 files (Mexico ×2, Nigeria/Brazil overlap) | Wasted effort if treated as distinct sources |
| ⚠️ **Superseded versions** | Saudi ECC-1:2018 whitepaper, Philippines draft IRR, CMMC v2.0 vs v2.13 | Extract the current version, not the older one |
| ⚠️ **No source in the KB** | ISO 42001, ISO 27701 | Already built in this repo but unverifiable until the standards are obtained |

## Suggested order of work

Items 3–5 of the original plan (the US catalogs, the large regulatory gaps and the privacy-law
long tail) are **done** — all 64 are extracted. So is the former item 1: **loaders for the 64 new
folders are written and all 64 are in the graph** (see [Loading into Neo4j](#loading-into-neo4j)).
What remains:

1. **Verify the 64 in `verdict.md`.** They are extracted and loaded but none has been checked
   against its source the way the original 26 were. This is now the largest quality gap: the graph
   holds 92 frameworks but only 28 are verified.
2. ~~**Finish what was already built** — verify and load `201 CMR 17` and `42 CFR Part 2`.~~
   **Done 2026-07-23** — both verified against their source regulation, their loaders rewritten,
   and loaded into Neo4j (see [Verified and loaded 2026-07-23](#-verified-and-loaded-2026-07-23-2)).
3. **Obtain the standards the KB does not contain.** The extraction pass proved seven instruments
   are absent despite files bearing their names: the **KVKK statute, POPIA Act, India IT Act,
   Australian Privacy Act, DO-178C, the COSO framework body and UN R156** — plus **ISO 42001** and
   **ISO 27701**, which have CSVs in the repo but no source at all, and the **ENISA ECSF Role
   Profiles** and **Philippines RA 10173**. Sourcing these is now the main blocker to completeness.
4. **Consider replacing the NIST RMF sample controls** with the real `NIST SP 800-53r5` catalog
   extracted here (322 controls, 867 enhancements) — `verdict.md` flags the 20-sample-control
   weakness.
5. **Consider reconciling `CPRA` against `CCPA 2025`**, which carries the SB 1223 / AB 1008 /
   AB 1824 amendments the 2020 Prop 24 text lacks.
