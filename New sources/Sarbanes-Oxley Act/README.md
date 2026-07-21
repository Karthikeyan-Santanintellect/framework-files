# Sarbanes-Oxley Act of 2002 — knowledge-graph CSVs

**Source document:** `KB 2/USA/Sarbanes-Oxley Act.pdf` — the House Office of the Legislative
Counsel compilation of the Sarbanes-Oxley Act of 2002 (Public Law 107–204, approved July 30,
2002, 116 Stat. 745), *As Amended Through P.L. 117–328, Enacted December 29, 2022*.
Extraction was performed from a `pdftotext -layout` text render of that PDF; all text is
verbatim from the compilation, with typesetting line-breaks and end-of-line hyphenation
rejoined and running heads / page footers removed.

## Schema

The Act's own structural vocabulary is used: an **Act** divided into **Titles** (Roman
numerals), which contain numbered **Sections**, which contain a recursive hierarchy of
lettered/numbered **Provisions** (the Act's own levels: subsection `(a)`, paragraph `(1)`,
subparagraph `(A)`, clause `(i)`, subclause `(I)`, item `(aa)`). Every subdivision that carries
text is its own row, so e.g. section 302(a)(4)(B) is a row in its own right. Two cross-cutting
node types are added because the instrument states them explicitly: **Definition** (defined
terms with their verbatim text) and **Footnote** (the compiler's five notes, including the two
recording that the Supreme Court held paragraphs unconstitutional in *Free Enterprise Fund*).

### Node files

| file | rows | first column | notes |
|---|---|---|---|
| `nodes_Act.csv` | 1 | `act_id` | short title, long title, public law citation, amended-through note, enacting clause |
| `nodes_Title.csv` | 10 | `title_id` | Titles I–V and VII–XI (see caveats) |
| `nodes_Section.csv` | 44 | `section_id` | section number, heading, bracketed U.S. Code citation, owning title, free-standing text for sections with no subdivisions |
| `nodes_Provision.csv` | 581 | `provision_id` | citation (e.g. `Section 302(a)(4)(B)`), level, marker, depth, heading, verbatim text, U.S.C. bracket, extracted deadline and penalty phrases, omission note |
| `nodes_Definition.csv` | 31 | `definition_id` | defined term, verbatim defining text, and `definition_full_text` which appends the subordinate provisions of that definition |
| `nodes_Footnote.csv` | 5 | `footnote_id` | compiler footnote text and the section it annotates |

### Relationship files

| file | rows | meaning |
|---|---|---|
| `rels_HAS_TITLE.csv` | 10 | Act → Title |
| `rels_HAS_SECTION.csv` | 44 | Title → Section (Act → Section for sections 1–3, which sit before Title I) |
| `rels_HAS_PROVISION.csv` | 581 | Section → Provision and Provision → Provision (carries the child's `level`) |
| `rels_DEFINES.csv` | 31 | Provision → Definition |
| `rels_CROSS_REFERENCES.csv` | 44 | Section/Provision → Section, for references to sections **of this Act** only (references to the Securities Exchange Act of 1934, title 18/28 U.S.C. etc. are deliberately not linked) |
| `rels_ANNOTATES.csv` | 5 | Footnote → Section |

IDs are derived from the citation: `SOX`, `SOX-T3`, `SOX-S302`, `SOX-S302-a-4-B`.

## Caveats and gaps

- **The compilation deliberately omits the Act's amendatory provisions.** Its own footnote 1
  states that the Act "largely amended other Acts and the amendatory provisions are not shown".
  Omitted text is marked in the source by `* * * * * * *` runs; those are captured as a
  `text_omitted_note` on the enclosing section or provision rather than being reconstructed.
- Consequently the following sections listed in the Act's table of contents have **no text in
  this source** and therefore no rows: 202–206, 301, 305, 402, **409**, 601–604, **802**, 803,
  806, 807, 902–904, **906**, 1102, 1103, 1105–1107. Sections 409, 802 and 906 were specifically
  requested; they are absent because each operates purely by amending the Securities Exchange Act
  of 1934 or title 18, U.S. Code, and the compiler does not print amendatory text. Nothing was
  supplied from outside the source. Sections **302** and **404** are present in full.
- Title VI has no heading or sections in the source, so only ten Title nodes exist.
- Section 110 (definitions for Title I, added by later amendment) appears in the text but not in
  the Act's original table of contents; it is included.
- Section 306(b) genuinely contains two paragraphs numbered (3) (the source's footnote 5 explains
  that the first provides for an amendment). Both rows are kept; the second carries the id
  suffix `~2` so ids stay unique, while its citation remains `Section 306(b)(3)`.
- A few provisions have an empty `text` field (e.g. 108(a), 201(a), 401(a), 403(a), 501(a),
  804(a)): the marker is printed in the compilation but its amendatory content is not.
- `deadline` and `penalty` columns hold phrases lifted verbatim from the provision text
  ("Not later than 180 days after the date of enactment of this Act", "shall be unlawful", …);
  they are convenience extracts, and an empty cell only means no such phrase was matched.
- The table of contents in section 1(b) is not reproduced as data; section 1 itself is retained.

## Validation

`nodes_*`/`rels_*` were re-parsed after generation: all node ids are unique within their file
(672 ids total), every `source_id`/`target_id` resolves to a node id, every node file starts with
`<type>_id` and carries `source_document`. 0 errors.
