# Compliance Framework Knowledge Graph

This repository holds the node and relationship CSVs for 90 compliance, security and privacy
frameworks, together with the loader scripts in [App_new/](App_new/) that build them into a
Neo4j graph.

Each framework is extracted from its authoritative source document (statute, regulation,
standard or official catalog) into a set of node CSVs and relationship CSVs, then loaded into
the Neo4j Aura instance (database `d7883150`).

The 90 come from two passes. **26** were extracted first and verified against their sources in
[verdict.md](verdict.md). A further **64** were extracted from the knowledge base into
[New sources/](New sources/) and loaded on 2026-07-21; they are in the graph but **not yet
verified**. See [New sources/source-audit.md](New sources/source-audit.md).

## Graph contents

**90 frameworks · 66,657 nodes · 143,915 relationships · 644 node labels · 967 relationship types**

Every node carries a framework identifier, so any framework can be selected in isolation. The
property name depends on the framework's classification:

| Classification | Identifier property | Frameworks |
|---|---|---:|
| IS frameworks & standards | `IS_frameworks_standard_id` | |
| Industry standards & regulations | `industry_standard_regulation_id` | 26 |
| Regional standards & regulations | `regional_standard_regulation_id` | |
| Extracted from `New sources/` | `framework_id` | 64 |

Nodes from the second pass also carry the label `:NewSourceNode`, and each of those 64 frameworks
has one `:NewSourceFramework` root node. Anything that resolves a framework should coalesce over
all four properties:

```cypher
coalesce(n.IS_frameworks_standard_id, n.industry_standard_regulation_id,
         n.regional_standard_regulation_id, n.framework_id)
```

## Nodes and relationships per framework

**Relationships** counts edges where both endpoints belong to that framework.
**Cross-framework** counts edges that link the framework to a *different* framework — control
crosswalks and mappings (for example SCF → ISO 27002, or a framework mapped to NIST CSF 2.0).
Each such edge is counted once for each of the two frameworks it connects.

| # | Framework | Neo4j ID | Nodes | Relationships | Cross-framework |
|---|-----------|----------|------:|--------------:|----------------:|
| 1 | CIS Controls | `CIS CONTROLS 8.1` | 188 | 823 | 283 |
| 2 | CPA | `CPA 1.0` | 201 | 342 | 25 |
| 3 | CPRA | `CPRA 2.0` | 182 | 855 | 8 |
| 4 | DORA | `DORA 2022/2554` | 222 | 1,781 | 70 |
| 5 | DPDPA | `DPDPA 1.0` | 296 | 4,303 | 106 |
| 6 | GDPR | `GDPR 2016/679` | 596 | 14,109 | 85 |
| 7 | GLBA | `GLBA 1999` | 69 | 342 | 74 |
| 8 | HIPAA | `HIPAA 2026` | 244 | 3,875 | 0 |
| 9 | HITECH | `HITECH_ACT_2009` | 200 | 5,591 | 40 |
| 10 | HITRUST | `HITRUST 11.6.0` | 1,197 | 1,862 | 60 |
| 11 | ISO 27001 | `ISO27001_2022` | 269 | 2,207 | 323 |
| 12 | ISO 27002 | `ISO27002_2022` | 221 | 11,815 | 503 |
| 13 | NERC CIP | `NERC_CIP` | 246 | 484 | 0 |
| 14 | NIS 2 | `NIS2-EU-2022-2555` | 228 | 2,998 | 266 |
| 15 | NIST AI RMF | `NIST_AI_RMF_1.0` | 96 | 1,448 | 247 |
| 16 | NIST CSF 2.0 | `NIST_CSF_2.0` | 135 | 134 | 1,213 |
| 17 | NIST PMF 1.0 | `NIST_PMF_1.0` | 169 | 168 | 361 |
| 18 | NIST PMF 1.1 | `NIST_PMF_1.1` | 137 | 144 | 0 |
| 19 | NIST RMF | `NIST_RMF_5.2` | 114 | 137 | 38 |
| 20 | PCI DSS | `PCI-DSS 4.0` | 233 | 5,167 | 0 |
| 21 | SCF | `SCF-2025.4` | 1,485 | 1,484 | 3,599 |
| 22 | SEC Cyber Rule | `SEC-2023` | 72 | 85 | 0 |
| 23 | SHIELD | `NY SHIELD 1.0` | 85 | 109 | 108 |
| 24 | TDPSA | `TDPSA 2023` | 160 | 175 | 26 |
| 25 | TISAX | `TISAX 2.8` | 60 | 39 | 9 |
| 26 | VCDPA | `VCDPA 2023` | 294 | 1,505 | 54 |
| | **Total** | | **7,399** | **61,982** | **7,498** |

The cross-framework column sums to 7,498 because each mapping edge is counted once for each of
the two frameworks it connects; there are **3,749 distinct** such edges. The relationship total
in the graph is therefore **65,247** = 61,498 within-framework + 3,749 cross-framework.

### The 64 frameworks from `New sources/`

Loaded 2026-07-21 from [New sources/](New sources/) — see
[source-audit.md](New sources/source-audit.md). These are **extracted and loaded but not yet
verified** in [verdict.md](verdict.md), unlike the 26 above.

They use a different identifier property, `framework_id`, and every node also carries the label
`:NewSourceNode`. **Cross-framework is 0 for all 64** — none of these sources contains a mapping
to another framework, so there are no crosswalk edges to or from them.

Each framework additionally has one `:NewSourceFramework` root node (64 in total, not counted
below) joined by `HAS_ROOT` to every node nothing else points at, so any one framework can be
traversed or deleted on its own.

| # | Framework | `framework_id` | Nodes | Relationships | Labels | Rel types |
|---|-----------|----------------|------:|--------------:|-------:|----------:|
| 1 | 21 CFR Part 11 | `21_CFR_PART_11` | 152 | 198 | 12 | 19 |
| 2 | ADGM Data Protection Regulations | `ADGM_DATA_PROTECTION_REGULATIONS` | 748 | 2,184 | 7 | 8 |
| 3 | APRA CPS 234 | `APRA_CPS_234` | 144 | 161 | 10 | 12 |
| 4 | ASD Essential Eight | `ASD_ESSENTIAL_EIGHT` | 338 | 644 | 6 | 7 |
| 5 | Argentina PDPA | `ARGENTINA_PDPA` | 265 | 282 | 10 | 11 |
| 6 | Australia Privacy Act 1988 | `AUSTRALIA_PRIVACY_ACT_1988` | 1,135 | 1,545 | 8 | 10 |
| 7 | BSI C5 | `BSI_C5` | 1,305 | 2,003 | 11 | 14 |
| 8 | Bahrain PDPL | `BAHRAIN_PDPL` | 479 | 521 | 12 | 13 |
| 9 | Brazil LGPD | `BRAZIL_LGPD` | 516 | 547 | 7 | 7 |
| 10 | CCPA 2025 | `CCPA_2025` | 716 | 897 | 9 | 10 |
| 11 | CMMC 2.0 | `CMMC_2_0` | 516 | 1,484 | 15 | 8 |
| 12 | COPPA | `COPPA` | 182 | 211 | 7 | 8 |
| 13 | COSO ERM | `COSO_ERM` | 890 | 1,022 | 17 | 15 |
| 14 | CPNI Rules | `CPNI_RULES` | 279 | 305 | 14 | 15 |
| 15 | Canada PIPEDA | `CANADA_PIPEDA` | 640 | 738 | 14 | 15 |
| 16 | China Data Security Law | `CHINA_DATA_SECURITY_LAW` | 192 | 210 | 10 | 11 |
| 17 | China PIPL | `CHINA_PIPL` | 282 | 287 | 9 | 9 |
| 18 | Colombia Ley 1581 | `COLOMBIA_LEY_1581` | 284 | 402 | 14 | 10 |
| 19 | DFARS | `DFARS` | 16,535 | 17,558 | 4 | 7 |
| 20 | DIFC Data Protection Law | `DIFC_DATA_PROTECTION_LAW` | 847 | 1,092 | 8 | 11 |
| 21 | DO-178C | `DO_178C` | 416 | 369 | 23 | 24 |
| 22 | ENISA ECSF | `ENISA_ECSF` | 246 | 415 | 22 | 25 |
| 23 | EU AI Act | `EU_AI_ACT` | 1,766 | 2,264 | 14 | 7 |
| 24 | EU Cyber Resilience Act | `EU_CYBER_RESILIENCE_ACT` | 978 | 1,258 | 11 | 12 |
| 25 | FDA Medical Device Cybersecurity | `FDA_MEDICAL_DEVICE_CYBERSECURITY` | 419 | 315 | 27 | 25 |
| 26 | FERPA (guidance) | `FERPA_GUIDANCE` | 151 | 272 | 8 | 11 |
| 27 | FFIEC Cybersecurity Assessment Tool | `FFIEC_CYBERSECURITY_ASSESSMENT_TOOL` | 873 | 1,598 | 14 | 13 |
| 28 | FISMA | `FISMA` | 2,139 | 2,350 | 23 | 13 |
| 29 | FedRAMP | `FEDRAMP` | 141 | 180 | 13 | 10 |
| 30 | ITAR | `ITAR` | 3,353 | 3,995 | 9 | 9 |
| 31 | India IT Act 2000 | `INDIA_IT_ACT_2000` | 1,255 | 1,344 | 16 | 6 |
| 32 | Indonesia PDP Law | `INDONESIA_PDP_LAW` | 512 | 600 | 11 | 16 |
| 33 | Japan APPI | `JAPAN_APPI` | 245 | 316 | 8 | 8 |
| 34 | Kenya Data Protection Act | `KENYA_DATA_PROTECTION_ACT` | 586 | 603 | 8 | 9 |
| 35 | MAS TRM Guidelines | `MAS_TRM_GUIDELINES` | 433 | 435 | 6 | 6 |
| 36 | MITRE ATT&CK | `MITRE_ATTACK` | 221 | 220 | 3 | 2 |
| 37 | Massachusetts Boards of Health Manual | `MASSACHUSETTS_BOARDS_OF_HEALTH_MANUAL` | 372 | 394 | 8 | 8 |
| 38 | Massachusetts Fraud and Abuse Compliance | `MASSACHUSETTS_FRAUD_AND_ABUSE_COMPLIANCE` | 312 | 351 | 22 | 27 |
| 39 | Mexico LFPDPPP | `MEXICO_LFPDPPP` | 1,075 | 1,223 | 19 | 15 |
| 40 | Mexico LGPDPPSO | `MEXICO_LGPDPPSO` | 700 | 737 | 11 | 11 |
| 41 | NAIC Insurance Data Security Model Law | `NAIC_INSURANCE_DATA_SECURITY_MODEL_LAW` | 174 | 196 | 7 | 7 |
| 42 | NIST SP 800-171r3 | `NIST_SP_800_171R3` | 1,406 | 2,520 | 14 | 20 |
| 43 | NIST SP 800-207 | `NIST_SP_800_207` | 184 | 183 | 21 | 22 |
| 44 | NIST SP 800-53r5 | `NIST_SP_800_53R5` | 3,512 | 6,870 | 5 | 5 |
| 45 | Nigeria Data Protection Act 2023 | `NIGERIA_DATA_PROTECTION_ACT_2023` | 1,405 | 1,518 | 20 | 20 |
| 46 | Philippines DPA IRR | `PHILIPPINES_DPA_IRR` | 452 | 507 | 8 | 5 |
| 47 | Qatar PDPPL | `QATAR_PDPPL` | 150 | 183 | 11 | 13 |
| 48 | RBI Cybersecurity Framework | `RBI_CYBERSECURITY_FRAMEWORK` | 214 | 218 | 14 | 14 |
| 49 | Russia 152-FZ | `RUSSIA_152_FZ` | 331 | 424 | 7 | 7 |
| 50 | SEBI Cybersecurity Framework | `SEBI_CYBERSECURITY_FRAMEWORK` | 887 | 1,192 | 27 | 18 |
| 51 | SOC 2 Trust Services Criteria | `SOC_2_TRUST_SERVICES_CRITERIA` | 474 | 666 | 8 | 8 |
| 52 | Sarbanes-Oxley Act | `SARBANES_OXLEY_ACT` | 672 | 715 | 6 | 6 |
| 53 | Saudi NCA ECC-2 2024 | `SAUDI_NCA_ECC_2_2024` | 364 | 392 | 9 | 10 |
| 54 | Singapore PDPA | `SINGAPORE_PDPA` | 1,392 | 1,597 | 13 | 13 |
| 55 | South Africa POPIA | `SOUTH_AFRICA_POPIA` | 159 | 186 | 10 | 12 |
| 56 | South Korea PIPA | `SOUTH_KOREA_PIPA` | 915 | 1,339 | 13 | 13 |
| 57 | Switzerland revFADP | `SWITZERLAND_REVFADP` | 572 | 694 | 12 | 12 |
| 58 | Thailand PDPA | `THAILAND_PDPA` | 569 | 691 | 8 | 9 |
| 59 | Turkey KVKK | `TURKEY_KVKK` | 286 | 308 | 12 | 12 |
| 60 | UAE PDPL | `UAE_PDPL` | 229 | 249 | 6 | 6 |
| 61 | UK Cyber Essentials | `UK_CYBER_ESSENTIALS` | 241 | 369 | 10 | 9 |
| 62 | UK NIS Regulations 2018 | `UK_NIS_REGULATIONS_2018` | 1,030 | 1,226 | 17 | 22 |
| 63 | UNECE UN R155 | `UNECE_UN_R155` | 340 | 452 | 13 | 16 |
| 64 | eIDAS Regulation | `EIDAS_REGULATION` | 598 | 752 | 10 | 13 |
| | **Total** | | **59,194** | **74,977** | | |

The CSVs in `New sources/` hold 59,203 node rows and 75,675 relationship rows. The graph holds
fewer of each because `MERGE` correctly collapses 9 ids that appear in two node files (one entity
under two labels) and 48 repeated relationship triples, and because 650 DFARS citations have a
blank target with nothing in-corpus to attach to. Every case is itemised in
[source-audit.md](New sources/source-audit.md#loading-into-neo4j).

### Source catalogues (not frameworks)

Three further datasets are loaded into the same graph but are **not compliance
frameworks** — they are the source catalogues and assessment banks extracted
from the DTOP-OLD project. Each uses its own anchor label and carries no
cross-framework mappings. See the folder READMEs for their internal schema:
[DTOP Sources](DTOP%20Sources/), [Enterprise Sources](Enterprise%20Sources/),
[Assessments and Questionnaires](Assessments%20and%20Questionnaires/).

| Catalogue | `framework_id` | Anchor label | Nodes | Relationships | Labels | Rel types |
|-----------|----------------|--------------|------:|--------------:|-------:|----------:|
| DTOP Sources | `DTOP_SOURCES` | `:DTOPNode` | 20 | 27 | 3 | 2 |
| Enterprise Sources | `ENTERPRISE_SOURCES` | `:EnterpriseNode` | 172 | 181 | 3 | 2 |
| Assessments and Questionnaires | `ASSESSMENTS_QUESTIONNAIRES` | `:AssessmentNode` | 1,841 | 8,484 | 13 | 16 |
| | **Total** | | **2,033** | **8,692** | | |

Node counts exclude each catalogue's single `:…Catalog` root node. The
relationship counts are internal to each catalogue; none of the three links to
any other catalogue or framework.

## Framework sources

| Framework | Source document |
|-----------|-----------------|
| CIS Controls | CIS Controls Guide v8.1.2 |
| CPA | Colorado Privacy Act Rules, 4 CCR 904-3 (with C.R.S. §§ 6-1-1301…1313) |
| CPRA | California Proposition 24 (2020) |
| DORA | Regulation (EU) 2022/2554 |
| DPDPA | Digital Personal Data Protection Act, 2023 (India) |
| GDPR | Regulation (EU) 2016/679 |
| GLBA | Gramm-Leach-Bliley Act, Title V |
| HIPAA | 45 CFR Part 164 Subparts C/D and 45 CFR Part 160 Subpart D |
| HITECH | Health Information Technology for Economic and Clinical Health Act (2009) |
| HITRUST | HITRUST CSF v11.6.0 |
| ISO 27001 | ISO/IEC 27001:2022 |
| ISO 27002 | ISO/IEC 27002:2022 |
| NIS 2 | Directive (EU) 2022/2555 |
| NIST AI RMF | NIST AI 100-1, AI RMF 1.0 |
| NIST CSF 2.0 | NIST Cybersecurity Framework 2.0 |
| NIST PMF 1.0 | NIST CSWP 10, Privacy Framework v1.0 (Jan 2020) |
| NIST PMF 1.1 | NIST CSWP 40 ipd, Privacy Framework v1.1 |
| NIST RMF | NIST SP 800-37r2 |
| PCI DSS | PCI DSS v4.0.1 (June 2024) |
| SCF | Secure Controls Framework 2025.4 |
| SEC Cyber Rule | SEC Cybersecurity Risk Management & Disclosure Rule (2023) |
| SHIELD | N.Y. Gen. Bus. Law §§ 899-aa, 899-bb |
| TDPSA | Texas HB4, Business & Commerce Code Ch. 541 |
| TISAX | ENX TISAX Participant Handbook v2.8 (ISA 5) |
| VCDPA | Va. Code §§ 59.1-575 through 59.1-585 |

### Sources for the 64 frameworks from `New sources/`

Taken from the `source_document` recorded in each folder's CSVs and reconciled against
[source-audit.md](New sources/source-audit.md).

⚠️ marks a framework where **the source document is not the instrument its name implies** — ten
rows. Eight are cases where reading the file during extraction disproved the original audit entry
outright (Australia Privacy Act, COSO ERM, DO-178C, FedRAMP, India IT Act, South Africa POPIA,
Turkey KVKK, UNECE R155); the other two (FERPA, CPNI) are guidance standing in for an absent
statute. In every one the graph models what the document actually contains — guidance, an
amendment, a notification, a vendor publication or a commentary — rather than the statute or
standard the name suggests. Treat those graphs accordingly. The Philippines DPA IRR row is the
regulations only; RA 10173 itself is likewise absent.

| Framework | Jurisdiction | Source document |
|-----------|--------------|-----------------|
| 21 CFR Part 11 | United States | 21 CFR Part 11, Electronic Records; Electronic Signatures (eCFR) + FDA *Scope and Application* guidance |
| ADGM Data Protection Regulations | United Arab Emirates | ADGM Data Protection Regulations |
| APRA CPS 234 | Australia | APRA Prudential Standard CPS 234 Information Security (July 2019) |
| ASD Essential Eight | Australia | ASD Essential Eight Maturity Model |
| Argentina PDPA | Argentina | Argentina Personal Data Protection Act 2000 |
| ⚠️ Australia Privacy Act 1988 | Australia | OAIC *Australian Privacy Principles Guidelines* (expressly non-binding), Oct 2025 — **the Privacy Act 1988 itself is absent from the source set** |
| BSI C5 | Germany | BSI Cloud Computing Compliance Criteria Catalogue (C5:2026) v1.0.1 |
| Bahrain PDPL | Bahrain | Bahrain Personal Data Protection Law |
| Brazil LGPD | Brazil | Lei nº 13.709 de 14 de agosto de 2018 (LGPD), consolidated Portuguese text |
| CCPA 2025 | United States | California Consumer Privacy Act of 2018, as amended effective 01/01/2025 (SB 1223, AB 1008, AB 1824) |
| CMMC 2.0 | United States | CMMC Model Overview v2.13 (Sept 2024), with v2.0 and a COGR Oct 2025 update |
| COPPA | United States | Children's Online Privacy Protection Rule, 16 CFR Part 312 |
| ⚠️ COSO ERM | United States | COSO ERM **Appendices Volume II only** + the Compliance Risk Management application paper — the framework body is absent; the 5 components and 20 principles come only from the application paper |
| ⚠️ CPNI Rules | United States | FCC Order 01-247 — **not** the codified CPNI rules at 47 CFR 64.2001–2011 |
| Canada PIPEDA | Canada | Personal Information Protection and Electronic Documents Act |
| China Data Security Law | China | Data Security Law of the People's Republic of China |
| China PIPL | China | Personal Information Protection Law |
| Colombia Ley 1581 | Colombia | Ley 1581 de 2012, Spanish statutory text |
| DFARS | United States | DFARS Volume III, Parts 201–253 |
| DIFC Data Protection Law | United Arab Emirates | DIFC Data Protection Law |
| ⚠️ DO-178C | United States | A Parasoft marketing ebook about DO-178C — **the standard itself is absent**, and its Annex A objectives tables are page images with no text layer |
| ENISA ECSF | European Union | ENISA *User Manual: European Cybersecurity Skills Framework (ECSF)*, Sept 2022 |
| EU AI Act | European Union | Regulation (EU) 2024/1689, Artificial Intelligence Act |
| EU Cyber Resilience Act | European Union | EU Cyber Resilience Act |
| FDA Medical Device Cybersecurity | United States | FDA Cybersecurity in Medical Devices guidance |
| ⚠️ FERPA (guidance) | United States | ED Student Privacy Policy Office *Parent Guide* (SPPO-21-04) and *Eligible Student Guide* (SPPO-23-01) — **guidance, not the statute** |
| FFIEC Cybersecurity Assessment Tool | United States | FFIEC Cybersecurity Assessment Tool |
| FISMA | United States | Federal Information Security Modernization Act of 2014, Public Law 113-283, with S.2902 and four FY25 CIO/IG/SAOP metrics documents |
| ⚠️ FedRAMP | United States | A 13-slide FedRAMP program-overview briefing deck (Aug 2023) — **no control baselines, playbook or CONOPS** |
| ITAR | United States | International Traffic in Arms Regulations, 22 CFR Parts 120–130, amended through 2 Oct 2025 |
| ⚠️ India IT Act 2000 | India | Four Gazette notifications of 17 Oct 2000 (commencement, Certifying Authorities Rules, Advisory Committee, Appellate Tribunal Procedure) — **the IT Act itself is absent** |
| Indonesia PDP Law | Indonesia | UU No. 27 of 2022 on Personal Data Protection, English translation |
| Japan APPI | Japan | Act on the Protection of Personal Information |
| Kenya Data Protection Act | Kenya | Kenya Data Protection Act (No. 24 of 2019) |
| MAS TRM Guidelines | Singapore | MAS Technology Risk Management Guidelines, January 2021 |
| MITRE ATT&CK | United States | MITRE ATT&CK matrix — an image-only PDF recovered by OCR; 206 of the source's own stated 235 techniques, each with a confidence flag |
| Massachusetts Boards of Health Manual | United States | MAHB *Manual of Laws and Regulations Relating to Boards of Health*, June 2016 — a public-health compendium, not a cyber/privacy framework |
| Massachusetts Fraud and Abuse Compliance | United States | Massachusetts Medical Society, *Fraud and Abuse Compliance* (2003) — healthcare billing compliance, not cyber/privacy |
| Mexico LFPDPPP | Mexico | LFPDPPP for private parties, DOF 20-03-2025 (new law), with the 2011 Regulations |
| Mexico LGPDPPSO | Mexico | LGPDPPSO for obligated subjects, DOF 20-03-2025 (machine translation) |
| NAIC Insurance Data Security Model Law | United States | NAIC Insurance Data Security Model Law (Model #668), Q4 2017 |
| NIST SP 800-171r3 | United States | NIST SP 800-171r3, *Protecting Controlled Unclassified Information* (May 2024) |
| NIST SP 800-207 | United States | NIST SP 800-207, *Zero Trust Architecture* (Aug 2020) |
| NIST SP 800-53r5 | United States | NIST SP 800-53r5, *Security and Privacy Controls for Information Systems and Organizations* |
| Nigeria Data Protection Act 2023 | Nigeria | Nigeria Data Protection Act 2023 Gazette text + the 2024 General Application and Implementation Directive |
| Philippines DPA IRR | Philippines | Implementing Rules and Regulations of the Data Privacy Act of 2012, final version — **RA 10173 itself is not in the source set** |
| Qatar PDPPL | Qatar | Qatar Personal Data Privacy Protection Law |
| RBI Cybersecurity Framework | India | RBI Cybersecurity Framework for Banks |
| Russia 152-FZ | Russia | Federal Law No. 152-FZ of 27 July 2006 *On Personal Data*, unofficial English translation |
| SEBI Cybersecurity Framework | India | SEBI Circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113 (20 Aug 2024), CSCRF v1.0 |
| SOC 2 Trust Services Criteria | United States | AICPA TSP Section 100, *2017 Trust Services Criteria* (incl. March 2020 updates) |
| Sarbanes-Oxley Act | United States | Sarbanes-Oxley Act of 2002 |
| Saudi NCA ECC-2 2024 | Saudi Arabia | NCA Essential Cybersecurity Controls ECC-2:2024 |
| Singapore PDPA | Singapore | Personal Data Protection Act 2012 (2020 Revised Edition) |
| ⚠️ South Africa POPIA | South Africa | *Amendment of the Regulations* under s 113(3), tabled Jan 2025 — **the POPIA Act itself is absent**: no chapters, definitions, conditions or offences |
| South Korea PIPA | South Korea | Personal Information Protection Act |
| Switzerland revFADP | Switzerland | Revised Federal Act on Data Protection |
| Thailand PDPA | Thailand | Personal Data Protection Act B.E. 2562 |
| ⚠️ Turkey KVKK | Turkey | Evren (2023), *Kişisel Verileri Koruma Dergisi* 5(2) — a 26-page comparative article on GDPR and KVKK. **Law 6698 is absent**; no Madde's operative text is reproduced |
| UAE PDPL | United Arab Emirates | Federal Decree-Law No. 45 of 2021 on the Protection of Personal Data |
| UK Cyber Essentials | United Kingdom | NCSC *Cyber Essentials: Requirements for IT Infrastructure* v3.3 |
| UK NIS Regulations 2018 | United Kingdom | UK Network and Information Systems Regulations 2018 |
| ⚠️ UNECE UN R155 | International | UN Regulation No. 155 (Add.154). **R156 (Software Update Management) is absent** despite the source filename naming both |
| eIDAS Regulation | European Union | eIDAS Regulation on electronic identification and trust services |

### Sources for the source catalogues

The three DTOP-OLD source catalogues (see the table above) are extracted from
files inside the DTOP-OLD project rather than from an external standard.

| Catalogue | Source document(s) |
|-----------|--------------------|
| DTOP Sources | `client/src/assets/docs/knowledgeRepository/info/dtopSources.json` |
| Enterprise Sources | `client/src/assets/docs/knowledgeRepository/info/enterpriseSources.json` |
| Assessments and Questionnaires | `client/src/data/sraFullData.json` (canonical HIPAA SRA, with the older `sraQuestionsData.json` and the `sraVulnerabilitiesData.json` stub) · `client/src/data/cri_statements.json` (CRI Profile v2.1 Expert Questionnaire) · `server/services/agentsV5/llmAssessment/statments/{IdP,XDR,SIEM,HRIS,CSP,DGP}.md` with the `server/services/agentsV5/catalog/*.csv` copies (6-domain Maturity Assessment) |

All paths are relative to the DTOP-OLD project root.

## Loading

Loader scripts live in [App_new/](App_new/), one per framework, plus
[App_new/push_verified.py](App_new/push_verified.py) to run a group of them.

```bash
python App_new/gdpr.py          # load a single framework
python App_new/push_verified.py # load a set
```

Connection details are read from `.env` (see `.env.example`) by
[App_new/app.py](App_new/app.py).

The loaders use Cypher `LOAD CSV`, which executes **server-side on the Neo4j instance**. The
CSVs are therefore fetched over HTTPS from this repository's raw GitHub URLs, which means CSV
changes must be committed and pushed before a loader will pick them up.

### The 64 loaders for `New sources/`

Each of the 64 also has its own loader in [App_new/](App_new/) — `App_new/coppa.py`,
`App_new/eu_ai_act.py`, and so on — but these are generated from the CSV headers on disk rather
than hand-written, so **edit the generator, never a generated loader**. They read from the
`gautham` branch, since `New sources/` is not on `main`.

```bash
python App_new/coppa.py --dry-run                 # validate, write nothing
python App_new/coppa.py                           # load one framework
python App_new/tools/load_new_sources.py          # load all 64, smallest first
```

| Tool | Purpose |
|---|---|
| [App_new/tools/gen_new_source_loaders.py](App_new/tools/gen_new_source_loaders.py) | Authors the 64 loaders. Re-run after any re-extraction |
| [App_new/tools/validate_new_sources.py](App_new/tools/validate_new_sources.py) | Offline dry-run — coverage, row counts, dangling endpoints, `--check-urls` |
| [App_new/tools/load_new_sources.py](App_new/tools/load_new_sources.py) | Runs all 64; `--only`, `--skip-loaded` |
| [App_new/tools/verify_new_sources_graph.py](App_new/tools/verify_new_sources_graph.py) | Read-only reconciliation of the graph against the loaders |
| [App_new/tools/repair_stranded_nodes.py](App_new/tools/repair_stranded_nodes.py) | Deletes nodes whose `framework_id` is not one of the 64 |

Every node is merged on `(framework_id, node_id)` under the `:NewSourceNode` anchor label, so
loads are **idempotent** — re-running repairs a partial load rather than duplicating it. The
anchor is what makes relationship endpoints resolvable: the `rels_*.csv` files record no endpoint
labels, and 153 relationship types legitimately span several labels.

## Graph explorer (index.html)

An interactive D3 visualisation of the whole database — framework map, per-framework
drill-down, cross-framework link explorer, node inspector and a Cypher console.

```bash
python make_viz.py --open     # generates ./index.html and opens it
```

[make_viz.py](make_viz.py) reads `.env` and injects the Neo4j credentials into
[viz/index.template.html](viz/index.template.html). The page then talks to Aura directly from
the browser over Bolt-on-WebSocket, so there is no server to run — just open the file.

> **The generated `index.html` contains the Neo4j password in plaintext.** It is listed in
> `.gitignore` and must never be committed: this repository is public (the loaders fetch CSVs
> from its raw URLs without authentication). Commit the template, not the output. If the file
> is ever pushed, rotate the Aura password immediately.

Everything is vendored into [viz/vendor/](viz/vendor/) (d3 v7, neo4j-driver-lite), so the page
works offline and cannot break because of a CDN change.

| Area | What it does |
|---|---|
| Overview | 90 framework bubbles sized by node count, joined by cross-framework edges weighted by mapping volume. Click one to open it. The 64 from `New sources/` appear as unconnected bubbles — those sources contain no cross-framework mappings. |
| Framework view | Loads that framework's nodes and relationships. Double-click any node to pull in its neighbours. |
| Cross-framework links | Every framework pair that shares edges, ranked by weight; click to see only those two and the edges bridging them. |
| Node inspector | Full property list for the selected node — long fields (verbatim requirement text, VSL tiers) render in full, not truncated. |
| Cypher console | Free-text queries plus a saved-query library. Returning nodes/relationships draws them; any other shape opens the results table. |
| Filters | Live show/hide by any of the 644 node labels and 967 relationship types, with counts. |

Canvas rendering with collision-aware labelling, so a dense framework stays readable; `Fit`,
`Pause`, and `PNG` export sit top-right, and <kbd>⌘↵</kbd> runs the query box.

## Querying by framework

```cypher
// All nodes for one framework
MATCH (n) WHERE n.regional_standard_regulation_id = 'GDPR 2016/679' RETURN n;

// Node counts by label for one framework
MATCH (n {IS_frameworks_standard_id: 'ISO27002_2022'})
RETURN labels(n)[0] AS label, count(*) AS nodes ORDER BY nodes DESC;

// Cross-framework control mappings
MATCH (a:Control {IS_frameworks_standard_id: 'SCF-2025.4'})
      -[:SCF_CONTROL_HAS_EXTERNAL_CONTROLS]->(b)
RETURN b.IS_frameworks_standard_id AS framework, count(*) AS mappings
ORDER BY mappings DESC;

// One of the 64 from New sources/ — all its nodes and internal relationships
MATCH (n:NewSourceNode {framework_id: 'EU_AI_ACT'})
OPTIONAL MATCH (n)-[r]->(:NewSourceNode {framework_id: 'EU_AI_ACT'})
RETURN n, r;

// Entry points into one of those frameworks
MATCH (:NewSourceFramework {framework_id: 'DFARS'})-[:HAS_ROOT]->(n) RETURN n;

// Node counts across all 90, whichever identifier property applies.
// toUpper() matches what the explorer does — one DPDPA node carries a
// lower-case id, so without it the result splits into 91 rows.
MATCH (n)
WITH toUpper(coalesce(n.IS_frameworks_standard_id, n.industry_standard_regulation_id,
                      n.regional_standard_regulation_id, n.framework_id)) AS framework
WHERE framework IS NOT NULL
RETURN framework, count(*) AS nodes ORDER BY nodes DESC;
```
