# New sources — knowledge-graph CSVs

Clause-level, verbatim extractions of every instrument in `source-verifier/KB 2` that had not
already been built into this repository. One folder per instrument, each with its own bespoke
schema modelled on that document's own structure, and its own `README.md` documenting the schema,
row counts and caveats.

**Built:** 2026-07-21 · **64 folders · 59,203 nodes · 75,675 relationships**
See [source-audit.md](source-audit.md) for the audit these folders answer.

## What these are

- **Verbatim.** Every text field comes from the source document. Nothing was paraphrased into a
  fact or supplied from general knowledge of the instrument. Where a document does not say
  something, the cell is empty.
- **Clause level.** Every numbered or lettered subdivision that carries obligation text is its own
  row — `12(2)(a)` is a row, not a sentence buried inside section 12.
- **No synthetic data.** No sample companies, no invented incidents, no fictional people. This is
  the opposite of the operational layer that had to be pruned from NERC, SHIELD, TISAX and VCDPA.
- **Bespoke schemas.** A statute gets Parts → Sections → Clauses; a controls catalog gets Domains →
  Controls → Enhancements; a maturity model gets Strategies × Levels. Node files are
  `nodes_<Type>.csv` with `<type>_id` first; relationship files are `rels_<name>.csv` with
  `source_id,target_id,rel_type` first.

## Integrity

Every folder was verified independently of the agent that built it:

- **0 dangling references** across all folders — every relationship endpoint resolves to a node.
- **0 duplicate ids** within any node file.
- Every folder has a `README.md`.

Two folders intentionally reuse an id across two node files, where the same source clause is
modelled both structurally and semantically: **EU AI Act** (8 Annex III points appear as both
`Point` and `HighRiskArea`) and **UK NIS 2018** (`sch2p9` as both `Provision` and `SchedulePara`).
The shared id is the link between the two views. This is safe for label-scoped
`MERGE (n:Label {id: …})` loading — which is what the existing `App_new/` loaders do — but a
loader that merged on id alone across labels would collide.

## Not yet done

These folders contain **CSVs only**. There are no Neo4j loaders and nothing here is in the graph.
The existing 26 frameworks each have an `App_new/*.py` loader; equivalents would need writing
before any of this can be loaded.

## Notable source findings

Extracting at clause depth forced every file open, which exposed eight documents that are not what
their filename claims. These are recorded in `source-audit.md` and in each folder's README:

| Source | Claimed | Actually is |
|---|---|---|
| `Turkey/…KVKK.pdf` | The KVKK statute | A 2023 journal article comparing GDPR and KVKK |
| `Africa/Protection of Personal Information Act.pdf` | POPIA | The 2025 amendment to the POPIA *Regulations* |
| `India/Information Technology Act 2000.pdf` | The IT Act | Four Gazette notifications + the Certifying Authorities Rules |
| `USA/FedRAMP.pdf` | A FedRAMP standard | A 13-slide program-overview briefing deck |
| `Australia/Australian Privacy Act 1988.pdf` | The Privacy Act | The OAIC *APP Guidelines* (non-binding) |
| `USA/DO-178C ….pdf` | The DO-178C standard | A Parasoft marketing ebook |
| `USA/COSO Enterprise Risk Management Framework.pdf` | The ERM framework | Appendices Volume II only — no principles |
| `UNECE WP.29 & UN Regulation No. 155 & 156.pdf` | R155 **and** R156 | R155 only (Add.154); R156 is a separate addendum |

Consequently the **KVKK statute, the POPIA Act, the India IT Act, the Australian Privacy Act,
the DO-178C standard, the COSO framework body and UN R156 are all absent from the knowledge base.**
Each affected folder models what the document genuinely contains and flags the gap rather than
inventing the missing instrument.

Also worth knowing:

- **Japan APPI** is the 2003 text — no Personal Information Protection Commission, none of the
  2015/2016 amendments. **South Korea PIPA** predates the 2023 amendment.
- **ENISA ECSF** — the User Manual defines the role-profile template but does not contain the
  12 role profiles; those are a separate publication.
- **Philippines** has the IRR but not the Data Privacy Act itself. **FERPA** has only ED guidance,
  not the statute or 34 CFR Part 99. **CPNI** is an FCC order, not the codified rules.
- **SOX** is the OLRC compilation, which omits amendatory provisions — §§ 409, 802 and 906 have no
  text because each works purely by amending another act.
- **MITRE ATT&CK** is OCR of a single-page image poster: 206 of the source's own stated 235
  techniques were recoverable, each row carrying an OCR confidence. Use MITRE's STIX/JSON for real
  work.
- Several sources are **unofficial or machine translations** — Mexico LGPDPPSO is a Google
  translation; China PIPL, Japan APPI, Korea PIPA, Thailand PDPA, Bahrain, Qatar, UAE, Russia and
  Argentina are translations of varying provenance. Each folder's README says which.

## Cross-repository note

`NIST SP 800-53r5` is the control catalog that the existing **NIST RMF** graph is missing —
`verdict.md` records that RMF carries only 20 sample controls because SP 800-37 does not enumerate
them. `CCPA 2025` is a newer snapshot of the same Civil Code sections as the existing `CPRA`
folder, carrying the SB 1223 / AB 1008 / AB 1824 amendments the 2020 Prop 24 text lacks.
