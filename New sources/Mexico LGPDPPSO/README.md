# Mexico — General Law on the Protection of Personal Data Held by Obligated Subjects (LGPDPPSO), DOF 20-03-2025

## ⚠️ The source is a MACHINE TRANSLATION

All text in these CSVs comes from **`KB 2/Mexico/PDP-Public_03-21-2025_GoogleTranslate.pdf`**, a
**Google machine translation** of the Spanish original (every page of the PDF carries a
"Machine Translated by Google" banner). This is **not an official English text** and has no legal
force — the authoritative text is the Spanish version published in the *Diario Oficial de la
Federación* on 20 March 2025.

Consequences visible in the data, and things a consumer must not treat as substantive:

- Roman numeral **`I.`** is rendered by the translator as **`YO.`** ("I" translated as the Spanish
  pronoun). This has been normalised back to `I.` in clause markers; the underlying text is
  otherwise untouched.
- Terminology is inconsistent across the translation: *responsable* is variously "the person
  responsible", "the controller", "the responsible party"; *encargado* is sometimes also rendered
  "person in charge" — Title Four's heading reads "RELATIONSHIP BETWEEN THE PERSON IN CHARGE AND
  THE PERSON IN CHARGE", which in Spanish is *responsable*/*encargado*.
- Occasional garbled renderings survive verbatim (e.g. Art. 105 fr. V "I ran out of matter." for
  *quedó sin materia*).
- Word-level spacing artefacts from the PDF layer (e.g. "interes t", "m ay") are preserved as-is.

Every node file carries a `source_document` column naming this machine-translated PDF, and
`nodes_Instrument.csv` carries a `language_note` column restating the caveat.

Page furniture was stripped and **not** treated as content: the "Machine Translated by Google"
banner, the running head "GENERAL LAW ON THE PROTECTION OF PERSONAL DATA HELD BY OBLIGATED
SUBJECTS", "CHAMBER OF DEPUTIES OF THE H. CONGRESS OF THE UNION … New DOF Law 03-20-2025",
"General Secretariat", "Secretariat of Parliamentary Services", and the "N of 35" page numbers.

## Scope

This is the **public-sector** data-protection statute (obligated subjects: authorities, bodies and
organs of the Executive, Legislative and Judicial branches, autonomous bodies, trusts and public
funds, political parties, federative entities and municipalities). It is a **distinct instrument**
from the *Federal Law on the Protection of Personal Data Held by Private Parties* (LFPDPPP) — the
private-sector law — which this Decree also re-issues separately and which appears here only as a
referenced instrument.

## Schema

The document's own division is Título → Capítulo → Artículo → fracción (roman numeral) →
inciso (letter), plus unnumbered *párrafos* inside articles. The graph mirrors that vocabulary
rather than a generic template, with four small overlay types for the things the instrument itself
singles out (definitions, ARCO/portability rights, sanction grounds, enforcement measures).

### Node types

| File | Type | Rows | Notes |
|---|---|---|---|
| `nodes_Instrument.csv` | Instrument | 1 | official title, DOF publication, promulgator, translation caveat |
| `nodes_Title.csv` | Title (Título) | 11 | FIRST TITLE … TITLE ELEVENTH, with headings |
| `nodes_Chapter.csv` | Chapter (Capítulo) | 21 | includes "Single Chapter" (Capítulo Único) chapters |
| `nodes_Article.csv` | Article (Artículo) | 137 | Articles 1–137, complete and contiguous; `chapeau` + `full_text` |
| `nodes_Clause.csv` | Clause | 452 | 321 fractions, 107 paragraphs, 24 letter-incisos |
| `nodes_Definition.csv` | Definition | 32 | Article 3 fractions I–XXXII, term + verbatim definition |
| `nodes_Right.csv` | Right | 5 | Access, Rectification, Cancellation, Opposition (Arts. 38–41) + Data Portability (Art. 51) |
| `nodes_SanctionGround.csv` | SanctionGround | 14 | Article 132 fractions I–XIV (grounds for sanction) |
| `nodes_EnforcementMeasure.csv` | EnforcementMeasure | 2 | Article 122: public reprimand; fine of 150–1,500 UMA |
| `nodes_ReferencedInstrument.csv` | ReferencedInstrument | 5 | external laws the text invokes |
| `nodes_TransitoryProvision.csv` | TransitoryProvision | 20 | First … Twentieth transitory articles of the Decree |

### Relationship types

| File | Shape | Rows |
|---|---|---|
| `rels_HAS_TITLE.csv` | Instrument → Title | 11 |
| `rels_HAS_CHAPTER.csv` | Title → Chapter | 21 |
| `rels_HAS_ARTICLE.csv` | Chapter → Article | 137 |
| `rels_HAS_CLAUSE.csv` | Article → Clause, Clause → Clause (letters under a fraction); `parent_type` column | 452 |
| `rels_DEFINES.csv` | Clause (Art. 3 fraction) → Definition | 32 |
| `rels_ESTABLISHES_RIGHT.csv` | Article → Right | 5 |
| `rels_IS_SANCTION_GROUND.csv` | Clause → SanctionGround | 14 |
| `rels_IS_ENFORCEMENT_MEASURE.csv` | Clause → EnforcementMeasure | 2 |
| `rels_CROSS_REFERENCES.csv` | Article → Article (internal "… of this Law" citations) | 24 |
| `rels_REFERENCES_INSTRUMENT.csv` | Article/TransitoryProvision → ReferencedInstrument | 19 |
| `rels_HAS_TRANSITORY.csv` | Instrument → TransitoryProvision | 20 |

Id conventions: `Art21`, `Art21-VIII` (fraction), `Art21-VII-a` (letter under a fraction),
`Art21-P2` (unnumbered paragraph, numbered in reading order within the article), `T3-C5`,
`DEF-<Term>`, `SG-XIV`, `EM-II`, `TRANS-Fifth`.

## Coverage of the themes requested

- **Definitions** — Art. 3, all 32 fractions, as `Definition` nodes (term / verbatim definition).
- **ARCO rights** — Title Three: Arts. 37–41 (the rights), 42–50 (their exercise: identity proof,
  free of charge, 20-day response period in Art. 45, request contents in Art. 46, refusal grounds
  in Art. 49), Art. 51 (portability). Surfaced both as clause-level rows and as `Right` nodes.
- **Obligations of obligated subjects** — Title Two (principles Arts. 10–24; duties/security
  Arts. 25–36, incl. the security document, breach notification and breach log), Title Four
  (controller/processor, cloud computing), Title Five (transfers/remissions), Title Six (best
  practices, impact assessments, security/justice databases), Title Seven (Transparency Committee
  and Transparency Unit).
- **Transparency/access interaction** — captured through `rels_REFERENCES_INSTRUMENT` to the
  *General Law on Transparency and Access to Public Information* (and to the Federal law,
  the Constitution, the LFPDPPP and the General Law of Archives), which the LGPDPPSO leans on for
  Committee/Unit integration (Arts. 77, 79), enforcement (Art. 121) and reporting (Art. 132 fr. XIV).
- **Sanctions and enforcement** — Title Eleven: coercive measures (Arts. 121–131, incl. the
  150–1,500 UMA fine and repeat-offence rule) and sanction grounds (Arts. 132–137).

## Caveats and gaps

1. **Machine translation** — see the banner section above. Any quotation from these CSVs should be
   checked against the Spanish DOF text before use.
2. The PDF is the Chamber of Deputies compilation of **Article Two** of the multi-law Decree of
   20 March 2025. "Article One", "Article Three and Article Four" of the Decree are elided in the
   source itself as "………" and are therefore absent here — that is a gap in the source, not the
   extraction.
3. `TransitoryProvision` nodes belong to the **Decree**, not to the LGPDPPSO articles, and several
   of them concern the transparency law and the wind-up of INAI rather than data protection.
4. Unnumbered paragraphs were segmented using the PDF's indentation (a new paragraph begins at
   indent 13–20 columns; deeper indents are continuations of a fraction). Sequence checks confirm
   every article's fractions run I, II, III … with no gaps, but paragraph splits are a layout
   inference rather than an explicit marker in the text.
5. `rels_CROSS_REFERENCES` covers only explicit "Article(s) N … of this Law" citations; references
   phrased as "the previous article", "this Chapter" or "the preceding paragraph" are left in the
   clause text and not resolved into edges.
6. `nodes_Right.csv` `text` holds the chapeau of the article that establishes the right; the full
   article text remains in `nodes_Article.csv`.

## Validation

`check_mx.py` (in scratch) parses every CSV, asserts each node file's first column is `<type>_id`
and unique, asserts every relationship endpoint resolves to a node id, and prints row counts.
Result: **PASS** — 700 node ids, 737 relationship rows, 0 unresolved endpoints, 0 duplicates.
