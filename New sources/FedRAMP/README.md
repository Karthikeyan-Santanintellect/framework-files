# FedRAMP — knowledge-graph extraction

## What this source actually is (read first)

`KB 2/USA/FedRAMP.pdf` is **not** the FedRAMP policy memo, **not** a security controls
baseline, **not** an authorization playbook, and **not** a CONOPS.

It is a **13-slide public program-overview briefing deck**, titled
"Federal Risk and Authorization Management Program", presented by
**Brian Conrad, Acting Director**, dated **August 29, 2023**, with the footer
`FedRAMP.gov` and contact `info@fedramp.gov`.

Consequences for modelling:

- There are **no numbered sections or subsections** anywhere in the document. The only
  numbering present is the slide page numbers and the "1 / 2 / 3" labels on the long-term
  goals slide.
- There are **no control baselines enumerated**. Baselines are *mentioned* ("Develops
  customized baselines for Cloud Services", "Rev 5 Transition — Modernize baselines") but
  no control, control family, or impact-level catalogue appears.
- There is **no formal definitions section**. A handful of terms are named and glossed in
  passing (FedRAMP, P-ATO, OSCAL, Agency Initial ATO, Agency Leveraged ATO,
  FedRAMP Authorized); these are captured in `nodes_Concept.csv` with only the verbatim
  gloss text the deck supplies, and an empty `text` cell where the deck supplies none.
- The authorization process is presented as **two paths with descriptive bullets**, not as
  an ordered procedure. `nodes_PathStep.csv` preserves the bullets in their printed order;
  the `order` column is presentation order, not a stated procedural sequence.
- Slide 9 ("Program Growth") is a chart image with no extractable text, and slide 10 is a
  "Q&A" slide. Both exist as `Slide` nodes with no statements. Note also that the deck's
  own ordering puts "Q&A" (slide 10) *before* "Major FY23 Changes" (11) and
  "FedRAMP Long Term Goals" (12).

Because the document is a deck rather than a normative instrument, the schema is built
around **Slide → Statement** as the clause-level spine, with typed entity nodes projected
out of the slides that carry structured content. The `Statement` node is the honest
equivalent of a "clause" here: every distinct bullet, labelled block, and prose line in the
deck is one row, verbatim.

## Schema

Node types:

| Node type | Meaning |
|---|---|
| `Slide` | One page of the deck (13). |
| `Statement` | Clause-level unit: every bullet / labelled block / prose line, verbatim, tied to its slide and its printed heading. |
| `LegalAuthority` | The four authorities on the "Legal and Policy Framework" slide. |
| `GovernanceBody` | Bodies named in the "New FedRAMP Governance Model" diagram, plus the JAB as named on the paths slide. |
| `Responsibility` | The sub-bullets attributed to a body inside the governance diagram. |
| `AuthorizationPath` | The two paths to authorization (JAB P-ATO, Agency ATO). |
| `PathStep` | Each descriptive bullet under a path. |
| `StakeholderGroup` | The three counted stakeholder populations. |
| `Worklane` | The six FedRAMP PMO worklanes. |
| `Benefit` | The four labelled efficiencies on slide 3. |
| `ChangeTheme` | The four "Major FY23 Changes" columns. |
| `Goal` | The three numbered long-term goals. |
| `Concept` | Terms the deck names and glosses. |

Relationship types: `HAS_STATEMENT`, `NEXT_SLIDE`, `PRESENTS`, `HAS_RESPONSIBILITY`,
`HAS_STEP`, `HAS_ACTIVITY`, `HAS_ACTION`, `AUTHORIZED_BY`, `PACKAGE_SUBMITTED_TO`,
`OPERATES_WORKLANE`.

`HAS_ACTIVITY` / `HAS_ACTION` link a `Worklane` / `ChangeTheme` to the same `Statement`
rows that sit under its printed heading, so bullets are stored once and reachable from both
the slide spine and the typed entity.

## Files and row counts

| File | Rows |
|---|---|
| nodes_Slide.csv | 13 |
| nodes_Statement.csv | 74 |
| nodes_LegalAuthority.csv | 4 |
| nodes_GovernanceBody.csv | 10 |
| nodes_Responsibility.csv | 7 |
| nodes_AuthorizationPath.csv | 2 |
| nodes_PathStep.csv | 5 |
| nodes_StakeholderGroup.csv | 3 |
| nodes_Worklane.csv | 6 |
| nodes_Benefit.csv | 4 |
| nodes_ChangeTheme.csv | 4 |
| nodes_Goal.csv | 3 |
| nodes_Concept.csv | 6 |
| rels_slide_has_statement.csv | 74 |
| rels_slide_next.csv | 12 |
| rels_slide_presents.csv | 42 |
| rels_body_has_responsibility.csv | 7 |
| rels_path_has_step.csv | 5 |
| rels_worklane_has_activity.csv | 24 |
| rels_changetheme_has_action.csv | 8 |
| rels_path_body.csv | 2 |
| rels_pmo_operates_worklane.csv | 6 |

Node rows total 141; relationship rows total 180.

## Source

`source_document` on every node = `KB 2/USA/FedRAMP.pdf`.
Extracted from a `pdftotext -layout` render (289 lines).

## Caveats and gaps

- **Wording is verbatim**, with two mechanical normalizations applied: the PDF's `ﬁ`/`ﬂ`
  ligature glyphs were expanded to `fi`/`fl`, and curly quotes were straightened. Column
  wrapping from the layout extract was rejoined into single-line prose.
- **Slide 11 layout is damaged in the text extract.** The four-column "Major FY23 Changes"
  slide interleaves its bullet markers and its column headers, so the association of
  "(Authorization Boundary Guidance)" and "Enable a risk management approach for protecting
  federal data" with the fourth column ("Modernize baselines External/3rd Party Services")
  rather than the third ("Rev 5 Transition") is inferred from horizontal position and is the
  single least certain assignment in this extraction. The bullet texts themselves are verbatim.
- **Slide 5 governance diagram has no stated edges.** The boxes and their sub-bullets are
  captured, but the diagram's connecting lines carry no labels in the text extract, so no
  hierarchy relationships between governance bodies were created. "Up to 4 additional agencies"
  is recorded as a statement, not as nodes.
- `FedRAMP BOARD` (slide 5) and `Joint Authorization Board` (slide 6) are kept as separate
  `GovernanceBody` rows because the deck uses the two names on different slides without
  stating they are the same body — the FY23 changes slide separately notes "Plan for changes
  to the Joint Authorization Board".
- **No penalties, deadlines, or thresholds** are stated anywhere in the deck. The only
  numeric values are the stakeholder counts (221 / 300+ / 61 / 40) on slide 7, held on
  `nodes_StakeholderGroup.csv`.
- Cross-references to other instruments (FISMA, OMB A-130, NIST standards, the FedRAMP
  Authorization Act, OSCAL) are captured as `LegalAuthority` / `Concept` nodes with the
  deck's own descriptive text only; no external content was imported.
- Slide 12 carries no page-number footer in the extract; its number 12 is by position.

## Validation

`check_fedramp.py` parses every CSV, asserts node-id uniqueness within and across files,
asserts each `source_id`/`target_id` resolves to a node id, and checks the required header
conventions. Result: **0 errors**.
