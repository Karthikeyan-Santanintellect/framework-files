# NIST SP 800-53r5 — Security and Privacy Controls for Information Systems and Organizations

**Source:** `KB 2/USA/NIST.SP.800-53r5.pdf` (492 pages)
**Extraction:** full verbatim, clause level. Chapter 3 (the control catalog, §§3.1–3.20) was split across
five parallel extractions by control family and merged here; header schemas were identical by
construction and the merge de-duplicated on primary key.

## Schema

A control catalog, so the model follows the catalog's own structure rather than a statute shape.

| File | Rows | What it holds |
|---|---:|---|
| `nodes_Family.csv` | 20 | The 20 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR) |
| `nodes_Control.csv` | 322 | Every control, with verbatim `control_text`, `discussion` and its `related_controls` line |
| `nodes_ControlEnhancement.csv` | 867 | Every enhancement, verbatim, with `status` (Active / Withdrawn) |
| `nodes_ControlItem.csv` | 1,105 | **Clause-level decomposition** — the `a.` / `1.` / `(a)` sub-items of controls and enhancements |
| `nodes_ODP.csv` | 1,198 | Organization-Defined Parameters — every `[Assignment: organization-defined …]` and `[Selection: …]`, verbatim, attached to the finest-grained owner |
| `rels_structure.csv` | 3,492 | HAS_CONTROL, HAS_ENHANCEMENT, HAS_ITEM, HAS_ODP |
| `rels_related.csv` | 3,378 | RELATED_TO, derived from each control's "Related Controls:" line |

**3,512 nodes · 6,870 relationships.** All ids unique; every relationship endpoint resolves.

## Notes and caveats

- **Withdrawn items are retained, not deleted:** 24 controls and 158 enhancements are withdrawn.
  A withdrawn control keeps its verbatim `[Withdrawn: Incorporated into …]` note as its
  `control_text`; withdrawn enhancements carry `status = Withdrawn`. Some withdrawn controls
  (e.g. SA-12) still list enhancements in the source — those are kept as printed.
- `nodes_Control.csv` has no `status` column, so control-level withdrawal is signalled only by the
  `[Withdrawn: …]` text at the start of `control_text`.
- One relationship was dropped at merge: the source prints `All XX-1 Controls` as a related-control
  target in the PS-1/PT-1/RA-1 policy controls. It is a verbatim phrase, not a control id, and
  resolves to no node. Everything else resolves.
- `enhancement_name` keeps the document's full header form, e.g.
  `BASELINE CONFIGURATION | UNAUTHORIZED SOFTWARE` — split on the pipe if a short name is wanted.
- Page headers/footers, the vertical "This publication is available free of charge…" sidebar and
  "Quick link to … Summary Table" lines were stripped as furniture. Layout wrapping was rejoined,
  including hyphen-split tokens.
- The `References:` lines under each control were not modelled (no target file in the schema).
- **Not extracted:** Chapter 1–2 narrative, and the back matter (Appendix A glossary, Appendix B
  acronyms, Appendix C control summary tables). The catalog itself — the part that matters for
  control mapping — is complete.

## Why this one matters beyond itself

`verdict.md` records that the existing **NIST RMF** graph carries only 20 sample SP 800-53
controls, because SP 800-37 does not enumerate them. This folder is the real catalog those
20 samples were standing in for, and can be used to replace them.
