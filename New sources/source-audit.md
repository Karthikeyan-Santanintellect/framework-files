# Source Audit — KB 2 / KB 3 vs. this repository

What exists in the knowledge base (`source-verifier/KB 2/` and `source-verifier/KB 3/`) against
what has actually been extracted into this repository, so the remaining work is explicit.

*This folder is the staging area for sources not yet in the graph — drop new instruments here,
then update the tables below as they are extracted.*

**Audit date:** 2026-07-21
**Knowledge base:** 128 files — 126 PDFs (KB 2: 117 across 25 jurisdiction folders, 150 MB · KB 3: 9, 20 MB)
plus one `.zip` and one `.xlsx`
**Rows are instruments, not files.** Where one instrument ships as several PDFs (Mexico's law
LFPDPPP comes as 4, FISMA as 6, CMMC as 4) they are grouped into a single row and the file count noted.

## Summary

| Status | Count | Meaning |
|---|---:|---|
| ✅ **Done** | **26** | Extracted, verified against its source in `verdict.md`, and loaded into Neo4j |
| ⚠️ **Built, not verified** | **4** | CSVs exist in the repo, but never verified in `verdict.md` and **not in the graph** |
| ❌ **Missing** | **64** | A source sits in the KB and nothing has been extracted from it |
| 📎 **Supporting material** | **13** | Secondary/duplicate documents that do not warrant their own framework |

**KB 3 is fully consumed** — all 9 files map to a completed framework. Every gap below is in KB 2.

Coverage by document count: of the 128 files, 25 back a completed framework, 2 back an unverified
one, 16 are supporting material, and **85 have never been extracted** — two thirds of the
knowledge base is untouched.

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

## ⚠️ Built, not verified (4)

CSVs exist in the repo but these never went through `verdict.md` verification and **none of them
are in the Neo4j instance** — the graph holds 26 frameworks, not 30.

| Framework | Repo folder | CSVs | Loader | Source in KB | Gap |
|---|---|---:|---|---|---|
| 201 CMR 17 | `201 CMR 17` | 17 | `App_new/201_cmr.py` | KB 2/USA/201cmr17.pdf | Never verified; never loaded |
| 42 CFR Part 2 | `42 CFR Part 2` | 5 | `App_new/42cfr.py` | KB 2/USA/42 CFR Part 2.pdf | Never verified; never loaded |
| ISO 42001 | `ISO 42001` | 5 | `App_new/iso42001.py` | **none — no ISO 42001 PDF in the KB** | Unverifiable without a source |
| ISO 27701 | `ISO 27701` | 8 | **none** | **none — no ISO 27701 PDF in the KB** | No loader *and* no source |

Two of the four (201 CMR 17, 42 CFR Part 2) have their source in the KB and could be verified
and loaded immediately. ISO 42001 and ISO 27701 would need their standards obtained first.

---

## ❌ Missing (64)

A source exists in KB 2 and nothing has been extracted. Rows marked **✔ content-verified** were
confirmed by opening the PDF, because filenames in this KB have proven unreliable — `NERC CIP.pdf`
turned out to be a roadmap and `NIST Privacy Framework.pdf` was the 1.1 draft. Unmarked rows are
identified from the filename plus its jurisdiction folder.

### Americas — USA (23)

| Instrument | Files | Notes |
|---|---:|---|
| NIST SP 800-53r5 — Security and Privacy Controls | 1 | The control catalog behind NIST RMF; the RMF graph currently carries only 20 sample controls |
| NIST SP 800-171r3 — Protecting CUI | 1 | Prerequisite for CMMC Level 2 |
| NIST SP 800-207 — Zero Trust Architecture | 1 | |
| CMMC 2.0 | 4 | ✔ content-verified — DoD Model Overview v2.13 (Sept 2024), v2.0 (2021), a CMMC 2.0 brief and a COGR October 2025 update |
| FISMA | 6 | ✔ content-verified — the enacted Public Law 113-283 (2014) plus S.2902 (117th Congress) and four FY25 CIO/IG/SAOP metrics documents |
| FedRAMP | 1 | ✔ content-verified |
| SOC 2 | 1 | ✔ content-verified — AICPA TSP Section 100, *2017 Trust Services Criteria* |
| Sarbanes-Oxley Act | 1 | |
| COSO ERM | 2 | ✔ content-verified — *Integrating with Strategy and Performance* (appendices) + *Compliance Risk Management* application paper |
| SOX/COSO adjacent: FFIEC Cybersecurity Assessment Tool | 1 | |
| NAIC Insurance Data Security Model Law | 1 | |
| COPPA — Children's Online Privacy Protection Act | 1 | |
| FERPA | 2 | ✔ content-verified — **both files are ED guidance** (a Parent Guide and an Eligible Student Guide), **not the statute**; the statutory text is absent |
| 21 CFR Part 11 — Electronic Records / Signatures | 2 | ✔ content-verified — eCFR authoritative text + FDA *Scope and Application* guidance |
| FDA Cybersecurity for Medical Devices | 1 | |
| CPNI Rules | 1 | ✔ content-verified — FCC 01-247 order, not the codified 47 CFR 64.2001–2011 rules |
| DFARS | 1 | ✔ content-verified — Volume III, Parts 201–253 |
| ITAR | 1 | ✔ content-verified — amended through 2 Oct 2025 |
| DO-178C — Airborne Systems Software | 1 | |
| MITRE ATT&CK | 1 | ⛔ **image-only PDF — zero extractable text**; needs OCR or a different source |
| Massachusetts Boards of Health — Manual of Laws | 1 | ✔ content-verified — MAHB 2016 manual; a public-health law compendium, not a cyber/privacy framework |
| Massachusetts fraud & abuse compliance manual | 1 | ✔ content-verified — Massachusetts Medical Society (2003); healthcare billing compliance, not cyber/privacy |
| CCPA | 1 | ✔ content-verified — CCPA of 2018 as amended effective 01/01/2025. **Largely covered already**: the `CPRA` folder models Civil Code 1798.100–.199.40. Worth diffing for the 2025 SB 1223 / AB 1008 / AB 1824 amendments the 2020 text lacks |

### Americas — Latin America & Canada (6)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| PIPEDA | Canada | 1 | |
| Mexico LFPDPPP (private parties) | Mexico | 4 | ✔ content-verified — **new law, DOF 20-03-2025** plus the 2011 Regulations, an evolution note and an EU-Mexico comparison |
| Mexico LGPDPPSO (obligated subjects) | Mexico | 1 | ✔ content-verified — General Law, DOF 20-03-2025; a separate instrument from the above |
| Brazil LGPD (Lei 13.709/2018) | Brazil | 2 | ✔ content-verified — Portuguese consolidated text + a second copy |
| Colombia Ley 1581 de 2012 | Colombia | 1 | ✔ content-verified — Spanish statutory text |
| Argentina Personal Data Protection Act 2000 | Argentina | 1 | |

### Europe, UK & Germany (7)

| Instrument | Files | Notes |
|---|---:|---|
| EU Artificial Intelligence Act | 1 | Largest remaining EU gap; pairs with the existing NIST AI RMF graph |
| EU Cyber Resilience Act | 1 | |
| eIDAS Regulation | 1 | |
| ENISA European Cybersecurity Skills Framework | 1 | User manual |
| UK NIS Regulations 2018 | 1 | UK counterpart to the completed NIS 2 graph |
| UK Cyber Essentials | 1 | ✔ content-verified — NCSC *Requirements for IT Infrastructure v3.3* |
| BSI C5 — Cloud Computing Compliance Controls Catalogue | 1 | Germany; the only KB 2/Germany source besides the completed TISAX handbook |

### Asia-Pacific (15)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| Information Technology Act 2000 | India | 1 | Complements the completed DPDPA graph |
| RBI Cybersecurity Framework for Banks | India | 1 | |
| SEBI Cybersecurity & Cyber Resilience Framework | India | 1 | |
| PIPL — Personal Information Protection Law | China | 1 | |
| Data Security Law | China | 1 | |
| APPI | Japan | 1 | |
| PIPA | South Korea | 1 | |
| PDPA | Singapore | 1 | |
| MAS Technology Risk Management Guidelines | Singapore | 1 | |
| PDP Law | Indonesia | 1 | |
| PDPA | Thailand | 1 | |
| Australian Privacy Act 1988 + Notifiable Data Breaches scheme | Australia | 4 | ✔ content-verified — the Act plus the NDB scheme guideline, an overview and the Jan–Jun 2024 statistics report |
| APRA Prudential Standard CPS 234 | Australia | 1 | |
| ASD Essential Eight Maturity Model | Australia | 1 | |
| Philippines Data Privacy Act 2012 — IRR | Philippines | 1 | ✔ content-verified — the final IRR only (a July 2016 draft is listed under supporting material). **The Act itself (RA 10173) is not in the KB** |

### Middle East, Africa & International (13)

| Instrument | Jurisdiction | Files | Notes |
|---|---|---:|---|
| UAE Federal Decree-Law 45/2021 (PDPL) | UAE | 1 | |
| DIFC Data Protection Law | UAE | 1 | Separate free-zone regime |
| ADGM Data Protection Regulations | UAE | 1 | Separate free-zone regime |
| Qatar Personal Data Privacy Protection Law | Qatar | 1 | |
| Bahrain Personal Data Protection Law | Bahrain | 1 | |
| NCA Essential Cybersecurity Controls (ECC-2:2024) | Saudi Arabia | 1 | ✔ content-verified — the current ECC-2:2024 controls |
| Turkey KVKK | Turkey | 1 | |
| Switzerland revised FADP | Switzerland | 1 | |
| Russia Federal Law 152-FZ | Russia | 2 | ✔ content-verified — one is an unofficial English translation |
| Kenya Data Protection Act | Kenya | 1 | |
| Nigeria Data Protection Act 2023 | Nigeria | 3 | ✔ content-verified — the 2023 Gazette text and the 2024 GAID implementation directive. **`Nigeria_DPA.pdf` is image-only with zero extractable text** |
| South Africa POPIA | South Africa | 1 | |
| UNECE WP.29 — UN Regulations 155 & 156 | International | 1 | ✔ content-verified — E/ECE/TRANS/505/Rev.3/Add.154 (2021); automotive cybersecurity, pairs with the completed TISAX graph |

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

1. **Finish what is already built** — verify and load `201 CMR 17` and `42 CFR Part 2`; their
   sources are in the KB and the loaders exist. This moves 30 frameworks to a consistent state.
2. **Obtain the two missing standards** — ISO 42001 and ISO 27701, so the existing CSVs stop
   being unverifiable.
3. **High-leverage US catalogs** — NIST SP 800-53r5 and SP 800-171r3. 800-53r5 would also fix
   the known weakness in the NIST RMF graph, which today carries 20 sample controls.
4. **Large regulatory gaps with existing neighbours** — EU AI Act (pairs with NIST AI RMF),
   UK NIS Regulations (pairs with NIS 2), India IT Act (pairs with DPDPA).
5. **The privacy-law long tail** — roughly 25 national data-protection laws across APAC, LATAM,
   the Middle East and Africa. These share a common shape and would extract well as a batch
   against a single schema.
