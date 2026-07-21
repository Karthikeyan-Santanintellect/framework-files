# Colombia — Ley Estatutaria 1581 de 2012 (protección de datos personales)

Knowledge-graph CSV extraction of the full enacting text of **LEY ESTATUTARIA 1581 DE 2012
(Octubre 17)**, *"Por la cual se dictan disposiciones generales para la protección de datos
personales"*.

- **Source document:** `KB 2/South America/Ley_1581_de_2012.pdf` (Departamento Administrativo de
  la Función Pública, EVA – Gestor Normativo edition; `pdftotext -layout` extract).
- **Language:** all extracted text is **verbatim Spanish**. Nothing has been translated,
  paraphrased or summarised. Layout wrapping and page headers/footers
  ("Departamento Administrativo de la Función Pública", "Ley 1581 de 2012 … EVA - Gestor
  Normativo") were removed and clauses split across page breaks were rejoined.

## Schema

The schema mirrors the statute's own vocabulary: `TÍTULO` → (`CAPÍTULO`) → `Artículo` →
subdivisions (`inciso`, `literal`, `numeral`, `parágrafo`). Only Título VII is subdivided into
capítulos; the other títulos hold articles directly. On top of that structural spine, a small
set of semantic node types lifts the substantive content the statute enumerates (definitions,
principles, rights, duties, functions of the supervisory authority, sanctions, and the criteria
for grading them), each linked back to the exact clause it comes from so no text is duplicated
without provenance.

### Node files

| File | Rows | Contents |
|---|---|---|
| `nodes_Instrumento.csv` | 1 | The law itself: official title, date, epígrafe, enacting body, the source's regulatory notes, publication reference. |
| `nodes_Titulo.csv` | 9 | Títulos I–IX with their headings. |
| `nodes_Capitulo.csv` | 3 | Capítulos I–III of Título VII. |
| `nodes_Articulo.csv` | 30 | Artículos 1–30, with epígrafe and the verbatim heading paragraph. |
| `nodes_Clausula.csv` | 157 | Every subdivision carrying text: `tipo` ∈ {inciso, literal, numeral, parágrafo}, verbatim `texto`, ordered by `orden`. |
| `nodes_Definicion.csv` | 7 | Artículo 3 defined terms (a–g) with verbatim definitions. |
| `nodes_Principio.csv` | 8 | Artículo 4 principios rectores (a–h). |
| `nodes_Derecho.csv` | 6 | Artículo 8 derechos de los Titulares (a–f). |
| `nodes_Deber.csv` | 27 | Artículo 17 duties of Responsables (a–o) and Artículo 18 duties of Encargados (a–l), with `sujeto`. |
| `nodes_Funcion.csv` | 11 | Artículo 21 functions of the Superintendencia de Industria y Comercio (a–k). |
| `nodes_Sancion.csv` | 4 | Artículo 23 sanctions (a–d), with the stated ceiling (2.000 SMMLV) and the six-month suspension term where the text states them. |
| `nodes_CriterioGraduacion.csv` | 6 | Artículo 24 criteria for grading sanctions (a–f). |
| `nodes_Actor.csv` | 8 | Actors named by the law (SIC, its Delegatura para la Protección de Datos Personales, Titular, Responsable, Encargado, Gobierno Nacional, Procuraduría General de la Nación, Corte Constitucional). |
| `nodes_ReferenciaExterna.csv` | 7 | External instruments cited in the enacting text (Ley 1266 de 2008, Ley 79 de 1993, arts. 15 and 20 of the Constitución Política, Código Contencioso Administrativo, Decreto Nacional 886 de 2014, Presupuesto General de la Nación). |

### Relationship files

| File | Rows | Meaning |
|---|---|---|
| `rels_CONTAINS.csv` | 199 | Instrumento → Título → (Capítulo) → Artículo → Cláusula. |
| `rels_DERIVED_FROM.csv` | 69 | Semantic node → its source clause (`DEFINED_IN`, `STATED_IN`, `GRANTED_BY`, `IMPOSED_BY`, `ASSIGNED_BY`, `IMPOSED_UNDER`). |
| `rels_REFERS_TO_ACTOR.csv` | 123 | Cláusula → Actor named in its text. |
| `rels_REFERENCES.csv` | 9 | Cláusula → external instrument cited. |
| `rels_CROSS_REFERENCES.csv` | 2 | Cláusula → another Artículo of this law it cites. |

All ids are unique within their file and every relationship endpoint resolves to a node id
(verified by an automated check).

## Deadlines and thresholds captured (all verbatim in the clause text)

Consultas: diez (10) días hábiles, extendable by cinco (5) días hábiles (art. 14). Reclamos:
five days to complete an incomplete claim, dos (2) meses before desistimiento, dos (2) días
hábiles to transfer or to insert the "reclamo en trámite" legend, quince (15) días hábiles to
decide, extendable by ocho (8) días hábiles (art. 15). Encargados must update within cinco (5)
días hábiles (art. 18 d). Sanctions: multas up to dos mil (2.000) SMMLV, suspensión up to seis
(6) meses, cierre temporal, cierre inmediato y definitivo (art. 23). Régimen de transición:
seis (6) meses (art. 28).

## Caveats and gaps

- **No "exequible" conditioning notes are present in this source.** The Función Pública EVA
  edition of the text carries no per-article constitutionality annotations. It records only two
  Constitutional Court references, both kept verbatim in the data: the header note
  *"Reglamentada parcialmente por el Decreto Nacional 1377 de 2013, Reglamentada Parcialmente por
  el Decreto 1081 de 2015. Ver sentencia C-748 de 2011. Ver Decreto 255 de 2022."*
  (stored in `nodes_Instrumento.csv`, column `notas`), and the sanction note that the law was
  signed *"En cumplimiento de lo dispuesto en la Sentencia C-748 de 2011 proferida por la Corte
  Constitucional…"*. Any per-article "exequible/condicionalmente exequible" declarations from
  C-748 de 2011 are **not** in this source and have deliberately not been supplied.
- Artículo 25 begins with the inline editorial insertion *"Reglamentado por el Decreto Nacional
  886 de 2014"* immediately before the statutory sentence; it is retained verbatim inside the
  first inciso rather than being silently deleted.
- Artículo 20 lists only literal a) in the source; there is no literal b).
- Artículo 21 literal j) reads "datos personajes" in the source (an apparent typo for
  "personales"); kept verbatim.
- The signature block, ministerial signatures, the Diario Oficial note and the informational
  disclaimer of the publisher are outside the enacting text and are not modelled as clauses
  (publication reference is kept on the Instrumento node).
- The extract's ligature glyphs (ﬁ, ﬂ) were NFKC-normalised to "fi"/"fl"; no other character
  changes were made.
