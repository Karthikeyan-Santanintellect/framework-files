# Turkey KVKK — knowledge-graph CSV extraction

## CRITICAL CAVEAT: the source is not the statute

`SOURCE_PDF` — `KB 2/Turkey/Kişisel Verilerin Korunması Kanunu (Turkish Personal Data
Protection Law - KVKK).pdf` — is **not** the enacted text of Law No. 6698. It is a
peer-reviewed journal article:

> Evren, A. G., (2023). *Avrupa Birliği ve Türkiye Kişisel Verilerin Korunması Kanunlarının
> Karşılaştırmalı Analizi: Temel İlkeler, Yasal Dayanaklar ve İlgili Kişi Hakları*,
> Kişisel Verileri Koruma Dergisi. 5(2), 39-64.
> (English title: *A Comparative Analysis of the European Union and Turkish Personal Data
> Protection Laws: Basic Principles, Legal Grounds, and Rights of Data Subjects*)
> Author: Adife Gül, EVREN — Avukat, Konak/İZMİR — ORCID 0009-0008-4205-7538.
> Received (Geliş) 18.12.2023, accepted (Kabul) 25.12.2023. Published by the journal of the
> Turkish Personal Data Protection Authority (www.kvkk.gov.tr).

Consequently the requested statutory modelling — Bölüm/Parts, numbered Madde with
paragraphs and sub-clauses, the definitions article, the composition and powers of the
Kişisel Verileri Koruma Kurulu/Kurumu, the cross-border transfer articles, and the
misdemeanour and criminal provisions (Articles 17–18) — **cannot be produced from this
source**. The document quotes and cross-references KVKK articles but never reproduces any
article's operative text in full. To honour the contract's verbatim-only rule, no statutory
clause text has been invented. What is modelled below is the article's own structure and
every KVKK/GDPR cross-reference it actually makes.

**To model the statute itself, a source containing the text of 6698 sayılı Kanun (Turkish)
or its official English translation must be supplied.**

### Language
The document is bilingual. The title, the `ÖZ` abstract and many citations are in Turkish
and are stored **verbatim in Turkish, untranslated** (see `nodes_Section.csv`,
`SEC-OZ`, and `nodes_Reference.csv`). The body text, from `INTRODUCTION` to `CONCLUSION`,
is written by the author in English — it is original English, not a translation of the
statute, and no translator is named anywhere in the document.

## Schema

The schema models a scholarly comparative-law article, not a statute, because that is what
the document is. Its own vocabulary is used for node names ("legal principles", "legal
grounds", "rights of data subjects", "special categories of personal data").

Node types:

| Type | Meaning |
|---|---|
| `Document` | the article itself, with its bibliographic metadata |
| `Section` | the article's own headings (`ÖZ`, `ABSTRACT`, `INTRODUCTION`, `LEGAL PRINCIPLES`, `LEGAL GROUNDS`, `SPECIAL CATEGORIES…` + its two subsections, `THE RIGHTS OF DATA SUBJECTS`, `CONCLUSION`, `REFERENCES`) |
| `LegalPrinciple` | each named data-processing principle with its verbatim one-line definition and its KVKK status |
| `LegalGround` | each legal basis for processing, with its verbatim definition and whether it is stated to be missing from either instrument |
| `DataSubjectRight` | each data subject right discussed, with GDPR and KVKK references |
| `SpecialCategory` | the special categories of personal data as described, incl. the two the KVKK adds |
| `Measure` | measures for processing special categories that the text attributes to the Authority / Art. 9 |
| `Provision` | every KVKK, GDPR, Communique, Constitution or Directive article the document cites — the clause-level anchor of this extraction |
| `Table` / `TableRow` | Tables 1–5, decomposed to one row per comparison line with verbatim cells |
| `Finding` | verbatim assertions the article makes about the KVKK |
| `Reference` | the bibliography |

Relationship types: `HAS_SECTION`, `SUBSECTION_OF`, `DISCUSSES`, `CITES_PROVISION`,
`DEFINES_CATEGORY`, `CONTAINS_TABLE`, `HAS_ROW`, `ROW_ABOUT`, `RELATED_PRINCIPLE`,
`RELATED_LEGAL_GROUND`, `STATES_FINDING`, `CITES_REFERENCE`.

`Provision` carries the clause-level depth the contract asks for: 34 distinct KVKK
provisions (e.g. `KVKK-5(2)(ç)`, `KVKK-11(1)(g)`, `KVKK-10(1)(ç)`) and 87 GDPR provisions
are individually addressable and linked to the principle, ground or right they support.

## Files and row counts

| File | Rows |
|---|---|
| nodes_Document.csv | 1 |
| nodes_Section.csv | 11 |
| nodes_Provision.csv | 128 |
| nodes_LegalPrinciple.csv | 9 |
| nodes_LegalGround.csv | 9 |
| nodes_DataSubjectRight.csv | 11 |
| nodes_SpecialCategory.csv | 4 |
| nodes_Measure.csv | 3 |
| nodes_Table.csv | 5 |
| nodes_TableRow.csv | 49 |
| nodes_Finding.csv | 19 |
| nodes_Reference.csv | 37 |
| rels_has_section.csv | 11 |
| rels_subsection_of.csv | 2 |
| rels_discusses.csv | 32 |
| rels_cites_provision.csv | 107 |
| rels_defines_category.csv | 4 |
| rels_contains_table.csv | 5 |
| rels_has_row.csv | 49 |
| rels_row_about.csv | 20 |
| rels_related_principle.csv | 18 |
| rels_related_legal_ground.csv | 4 |
| rels_states_finding.csv | 19 |
| rels_cites_reference.csv | 37 |

**286 unique node ids; every relationship endpoint resolves.**

## Caveats and gaps

- **No statutory clause text.** No Madde is reproduced verbatim in the source, so none is in
  the CSVs. `Provision` nodes carry the citation label and instrument only; the `note`
  column holds text only where the source itself quoted or paraphrased something.
- **No Board / Authority institutional provisions, no transfer rules, no penalties.** The
  article does not cover KVKK Articles 15–25 (Board composition, complaint procedure,
  misdemeanours, criminal provisions) or Article 9's cross-border transfer regime beyond one
  passing mention that the Authority may take adequate measures. These are absent from the
  graph because they are absent from the source.
- **Definitions.** The document contains no defined-terms article. The "definitions" captured
  are the author's own one-line glosses of each principle and legal ground, stored verbatim
  in `verbatim_definition` and marked as such by their node type.
- **A citation error in the source is preserved as-is.** The ground "Data processing is
  necessary for the establishment, exercise or protection of any right" is cited by the
  author as "Art. 5(1)(e) of the KVKK"; in Law No. 6698 that ground sits in Article 5(2).
  The source's own label is kept verbatim and the discrepancy is flagged in the
  `comparative_note` column rather than silently corrected.
- **Table 2 is a two-column table** (GDPR exceptions vs KVKK grounds) whose columns are not
  row-aligned in the original layout; `col3` is empty for its rows and cell pairings reflect
  the printed layout, not a semantic correspondence.
- **Page headers/footers** (`KİŞİSEL VERİLERİ KORUMA DERGİSİ 5(2) nn` and the running title)
  and column-wrap line breaks were removed; wording is otherwise unchanged.
- Turkish characters (ç, ğ, ı, İ, ö, ş, ü) and the typographic quotes used in the source are
  preserved; all files are UTF-8.
