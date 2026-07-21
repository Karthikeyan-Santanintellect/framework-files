# Brazil — Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709, de 14 de agosto de 2018

Knowledge-graph CSV extraction of the LGPD at clause level, **verbatim in Portuguese**.

## Source documents

Two source texts were supplied for the same law:

| File | Content | Used |
|---|---|---|
| `KB 2/South America/lei-13709-14-agosto-2018-787077-normaatualizada-pl.pdf` (`South_America_lei_13709_14_agosto_2018_787077_normaatualizada_pl.txt`) | **Texto consolidado / norma atualizada** published by the Câmara dos Deputados, Centro de Documentação e Informação. Portuguese. Carries in-line amendment notes up to *Medida Provisória nº 1.317, de 17/9/2025, convertida na Lei nº 15.352, de 25/2/2026* and the vetoes of *Lei nº 15.134, de 6/5/2025*. | **PRIMARY — all node/relationship text comes from this file.** |
| `South_America_Lei_Geral_de_Protec_a_o_de_Dados_LGPD_Brazil.txt` | Unofficial **English translation** issued by the ANPD ("Brazilian Data Protection Law (LGPD) (As amended by Law No. 13,853/2019)"), whose own preface states it is a first version subject to revision. | Secondary — used **only** to populate the `title_en` column on `nodes_Capitulo.csv` / `nodes_Secao.csv`. |

**How the two differ.** They are the same statute at different vintages and in different languages.
The English file stops at the consolidation as amended by Lei nº 13.853/2019, so it does **not** contain
the later material present in the Portuguese consolidated text: the 2022 changes (Lei nº 14.460/2022 —
art. 55-M, inciso V-A of art. 55-C, revocation of arts. 55-B and §§ 1º–3º of art. 55-A), the 2025 vetoes
(Seção III-A and art. 14-A, § 2º-A of art. 52 — Lei nº 15.134/2025), and the 2025/2026 re-drafting of
Capítulo IX and of the definitions of *encarregado* and *autoridade nacional* (MP nº 1.317/2025 → Lei nº
15.352/2026, which renames the authority "Agência Nacional de Proteção de Dados"). The Portuguese file is
therefore strictly the more complete of the two and is the sole source of substantive text here.
No text was translated; the only English in these CSVs is the chapter/section headings copied verbatim
from the ANPD translation.

## Schema

The schema mirrors the statute's own structure and vocabulary (Capítulo → Seção → Artigo → dispositivo),
plus two typed views the contract requires (defined terms and penalties).

### Node files

| File | Type | Meaning | Rows |
|---|---|---|---|
| `nodes_Lei.csv` | `Lei` | The instrument itself (title, ementa, preâmbulo, date). | 1 |
| `nodes_Capitulo.csv` | `Capitulo` | The 10 Capítulos, with heading and any amendment note. | 10 |
| `nodes_Secao.csv` | `Secao` | The 15 Seções (including the vetoed Seção III-A). | 15 |
| `nodes_Artigo.csv` | `Artigo` | All 81 artigos, incl. 14-A, 55-A…55-M, 58-A, 58-B. `texto_caput` is the verbatim caput. | 81 |
| `nodes_Dispositivo.csv` | `Dispositivo` | Every subdivision carrying text: parágrafos, parágrafo único, incisos, alíneas — including incisos nested inside a parágrafo (e.g. art. 11 § 4º I) and alíneas nested inside an inciso (e.g. art. 11 II "a"). | 378 |
| `nodes_Definicao.csv` | `Definicao` | The 19 defined terms of art. 5º, term and definition split at the colon used by the source. | 19 |
| `nodes_Sancao.csv` | `Sancao` | The 12 administrative sanctions listed in the caput of art. 52 (incl. the three vetoed incisos VII–IX). | 12 |

Every node file carries `source_document`. Status columns record `vigente` / `vetado` / `revogado`,
derived only from the source's own "(VETADO)" / "(Revogado …)" markers. `nota_alteracao` holds the
source's own trailing parenthetical amendment note; the full verbatim text (note included) is always
kept in `texto` / `texto_caput`.

### Relationship files

| File | Shape | Rows |
|---|---|---|
| `rels_HAS_CAPITULO.csv` | `Lei` → `Capitulo` | 10 |
| `rels_HAS_SECAO.csv` | `Capitulo` → `Secao` | 15 |
| `rels_HAS_ARTIGO.csv` | `Secao` (or `Capitulo`, where a chapter has no sections) → `Artigo` | 81 |
| `rels_HAS_DISPOSITIVO.csv` | `Artigo` → `Dispositivo`, and `Dispositivo` → `Dispositivo` for nesting | 378 |
| `rels_DEFINES.csv` | `art_5` → `Definicao` | 19 |
| `rels_IMPOSES_SANCAO.csv` | `art_52` → `Sancao` | 12 |
| `rels_REFERENCES.csv` | any `Artigo`/`Dispositivo` → the `Artigo` it cites; `citation` column holds the source's own wording | 32 |

### Identifiers

`lei_13709_2018`; `cap_IX`; `sec_II_III-A`; `art_55-J`; `art_11_inc_II_ali_a`, `art_52_par_6_inc_I`,
`art_33_pu`; `def_5_XII`; `sanc_52_II`.

## Caveats and notes

- **Cross-references** (`rels_REFERENCES.csv`) are conservative: only explicit citations of the form
  "art(s). N … desta Lei" are captured. Citations to *other* statutes (Lei nº 12.527/2011, Lei nº
  9.307/1996, Marco Civil, etc.) are preserved inside the verbatim text but are not modelled as nodes,
  since those statutes are outside this instrument.
- **Deliberate duplication:** `Definicao` and `Sancao` rows restate text that also appears in the
  corresponding `Dispositivo` row. Each carries a `dispositivo_id` back-pointer so the two views can be
  reconciled.
- **Vetoed / revoked provisions are retained** as rows with their source text (e.g. `art_14-A`,
  `sec_II_III-A`, `art_52_par_2-A`, `art_7_par_1`), because the consolidated source retains them.
  `sec_II_III-A` has an empty `titulo` — the source prints no heading for it, only the veto note.
- The caput of art. 52 carries the source's own note "(Artigo republicado no DOU Edição Extra de
  15/8/2018)".
- **Art. 60** amends the Marco Civil da Internet and quotes amended text of arts. 7º and 16 of Lei nº
  12.965/2014. That quoted block is kept inside `art_60`'s `texto_caput` and is deliberately **not**
  decomposed into `Dispositivo` rows, since those incisos belong to a different law.
- One layout artifact was repaired: in art. 55-J the source ran incisos XXI and XXII onto a single line;
  they were split at "XXII - " with wording unchanged. Column-wrapped lines throughout were rejoined into
  single-line prose with wording preserved exactly.
- Key thresholds/deadlines stated by the law are present verbatim in the clause text, e.g. the 2% of
  Brazilian turnover / R$ 50.000.000,00 per-infraction cap (art. 52 II), the 15-day access response
  (art. 19 II), the maximum 6-month suspensions (art. 52 X and XI), the 5-member Conselho Diretor with
  4-year mandates (art. 55-D), the 23-member Conselho Nacional (art. 58-A), and the entry-into-force
  dates of art. 65.

## Validation

A self-check script confirms: `nodes_*` ids are unique within each file; every endpoint of all 547
relationship rows resolves to one of the 516 node ids; every node row carries `source_document`; every
`rels_*` file starts with `source_id,target_id,rel_type`; all files parse as UTF-8 CSV with a header row.
