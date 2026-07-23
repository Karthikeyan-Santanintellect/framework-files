"""Build the Assessments & Questionnaires node and relationship CSVs.

Extracts the three assessment question banks that ship inside the DTOP-OLD
client and server into the same `nodes_<Label>.csv` / `rels_<TYPE>.csv` shape
used by the other folders in this repository:

  1. HIPAA Security Risk Assessment (SRA)  — sraFullData.json (canonical),
     with sraQuestionsData.json (older) and sraVulnerabilitiesData.json (stub)
     represented as superseded DataSources.
  2. Expert Questionnaire (CRI Profile v2.1) — cri_statements.json, 85 items.
  3. Maturity Assessment — 6 domain banks, ~671 statements, taken as the union
     of the canonical .md banks and their slightly-divergent .csv copies, each
     statement flagged in_md / in_csv.

    python "Assessments and Questionnaires/build_csvs.py"

Design decisions (all confirmed with the requester):

* SRA question ids are section-scoped — `Q1` recurs in every section — so
  every question is keyed by (section, id) and each option's `next` branch is
  resolved within its own section.
* The maturity .md is canonical; the .csv copies diverge by 1-5 statements
  each. Statements are the union, keyed by their verbatim text, with in_md /
  in_csv booleans, so nothing from either copy is lost.
* All 85 CRI statement ids also occur in the 671 maturity statements ("a
  curated subset"); that overlap is emitted as ALSO_IN edges.
* CRI and maturity share the same CRI Profile v2.1 subcategory taxonomy (all 31
  CRI subcategories are among the 110 maturity ones), so Subcategory nodes are
  deduplicated and shared across both assessments.

Everything written is present in the source files; the only derived values are
counts, presence flags and deterministic ids.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

DTOP = Path("/Users/gauthamsmacbook/Apps/Santan/DTOP-OLD")
DATA = DTOP / "client/src/data"
MD_DIR = DTOP / "server/services/agentsV5/llmAssessment/statments"
CSV_DIR = DTOP / "server/services/agentsV5/catalog"
OUT = Path(__file__).resolve().parent

# Maturity domain -> (md filename stem, csv filename stem). The CSP domain's
# csv copy is named CS.csv; every other pair shares a stem.
MATURITY = {
    "IdP": ("IdP", "IdP"), "XDR": ("XDR", "XDR"), "SIEM": ("SIEM", "SIEM"),
    "HRIS": ("HRIS", "HRIS"), "CSP": ("CSP", "CS"), "DGP": ("DGP", "DGP"),
}


def h(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:10]


def slug(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    return re.sub(r"_+", "_", s)


def write(filename: str, header: list[str], rows: list[list]) -> None:
    with (OUT / filename).open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {filename:<34} {len(rows):>5} rows")


def read_md(stem: str) -> list[tuple[str, str, str]]:
    """(subject_tags, 'ID: text', subcategory) for one maturity .md bank."""
    lines = [l.rstrip("\n") for l in (MD_DIR / f"{stem}.md").open(encoding="utf-8")
             if l.startswith("|")][2:]
    out = []
    for l in lines:
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) >= 3:
            out.append((cells[0], cells[1], cells[2]))
    return out


def read_csv_bank(stem: str) -> list[tuple[str, str, str]]:
    with (CSV_DIR / f"{stem}.csv").open(encoding="utf-8-sig", newline="") as fh:
        return [tuple(r[:3]) for r in list(csv.reader(fh))[1:] if len(r) >= 3]


def split_statement(cell: str) -> tuple[str, str]:
    """'PR.AA-05.02: The organization…' -> ('PR.AA-05.02', 'The organization…')."""
    m = re.match(r"^([A-Z]{2}\.[A-Z]{2}-\d+\.\d+)\s*:\s*(.*)$", cell, re.S)
    return (m.group(1), m.group(2).strip()) if m else ("", cell.strip())


# collectors -----------------------------------------------------------------
subcats: dict[str, str] = {}          # text -> id
tags: dict[str, str] = {}             # #tag -> id
threats: dict[str, str] = {}          # text -> id


def subcat_id(text: str) -> str:
    text = text.strip()
    if text and text not in subcats:
        subcats[text] = f"sub_{h(text)}"
    return subcats.get(text, "")


def tag_id(t: str) -> str:
    if t not in tags:
        tags[t] = f"tag_{slug(t)}"
    return tags[t]


def threat_id(text: str) -> str:
    text = text.strip()
    if text not in threats:
        threats[text] = f"thr_{h(text)}"
    return threats[text]


def main() -> None:
    SRC = "DTOP-OLD"  # short provenance prefix used in source_document

    n_asmt, n_ds, n_sec, n_q, n_opt = [], [], [], [], []
    n_vuln, n_stmt, n_dom, n_sup = [], [], [], []
    r_has_section, r_has_question, r_has_option, r_leads_to = [], [], [], []
    r_has_vuln, r_has_threat, r_cites = [], [], []
    r_has_domain, r_has_statement, r_in_sub, r_tagged, r_also_in = [], [], [], [], []
    r_sourced, r_supersedes, r_prior, r_from_src = [], [], [], []

    # -- DataSource nodes ------------------------------------------------
    def ds(sid, path, kind, note=""):
        n_ds.append([sid, path, kind, note, path])
        return sid

    sra_full = ds("src_srafulldata", "client/src/data/sraFullData.json",
                  "json", "Canonical HIPAA SRA question and vulnerability bank")
    sra_old = ds("src_sraquestionsdata", "client/src/data/sraQuestionsData.json",
                 "json", "Older SRA question set (124q, no education/reference); superseded")
    sra_stub = ds("src_sravulnerabilitiesdata",
                  "client/src/data/sraVulnerabilitiesData.json",
                  "json", "3-group vulnerability stub; superseded by sraFullData")
    cri_src = ds("src_cri_statements", "client/src/data/cri_statements.json",
                 "json", "CRI Profile v2.1 expert questionnaire, 85 statements")
    md_src, csv_src = {}, {}
    for dom, (mstem, cstem) in MATURITY.items():
        md_src[dom] = ds(f"src_md_{slug(dom)}",
                         f"server/services/agentsV5/llmAssessment/statments/{mstem}.md",
                         "md", f"Canonical {dom} maturity statement bank")
        csv_src[dom] = ds(f"src_csv_{slug(dom)}",
                          f"server/services/agentsV5/catalog/{cstem}.csv",
                          "csv", f"CSV copy of the {dom} bank (may diverge from the .md)")

    # =========================== SRA ====================================
    full = json.loads((DATA / "sraFullData.json").read_text())["sections"]
    old = json.loads((DATA / "sraQuestionsData.json").read_text())["sections"]
    old_text = {(s["id"], q["id"]): q["text"] for s in old for q in s["questions"]}

    n_asmt.append(["asmt_sra", "HIPAA Security Risk Assessment (SRA)",
                   "HIPAA Security Rule", "branching",
                   sum(len(s["questions"]) for s in full),
                   sum(len(s.get("vulnerabilities", [])) for s in full),
                   "SraQuestionsPage.tsx, SraPage.tsx", "/sra, /sra/questions",
                   "", SRC])
    r_sourced += [["asmt_sra", sra_full, "SOURCED_FROM", SRC]]
    r_supersedes += [[sra_full, sra_old, "SUPERSEDES", SRC],
                     [sra_full, sra_stub, "SUPERSEDES", SRC]]

    for s in full:
        secn = re.search(r"\d+", s["id"]).group()
        sec_id = f"sra_s{secn}"
        n_sec.append([sec_id, s["id"], s["title"],
                      len(s["questions"]), len(s.get("vulnerabilities", [])), SRC])
        r_has_section.append(["asmt_sra", sec_id, "HAS_SECTION", SRC])

        for q in s["questions"]:
            qid = f"{sec_id}_{slug(q['id'])}"
            n_q.append([qid, q["id"], sec_id, q["text"], len(q["options"]), SRC])
            r_has_question.append([sec_id, qid, "HAS_QUESTION", SRC])

            # superseded prior text
            prev = old_text.get((s["id"], q["id"]))
            if prev is not None and prev != q["text"]:
                sup_id = f"sup_{sec_id}_{slug(q['id'])}"
                n_sup.append([sup_id, q["id"], sec_id, prev, SRC])
                r_prior.append([qid, sup_id, "HAD_PRIOR_TEXT", SRC])
                r_from_src.append([sup_id, sra_old, "FROM_SOURCE", SRC])

            for i, o in enumerate(q["options"], 1):
                oid = f"{qid}_o{i}"
                n_opt.append([oid, qid, i, o.get("text", ""),
                              o.get("education", ""), o.get("reference", ""),
                              o.get("next", ""), SRC])
                r_has_option.append([qid, oid, "HAS_OPTION", SRC])
                nx = o.get("next")
                if nx and nx != "END":
                    tgt = f"{sec_id}_{slug(nx)}"
                    r_leads_to.append([oid, tgt, "LEADS_TO", nx, SRC])
                # references: one line per framework -> CITES edge with detail
                for line in re.split(r"[\n;]", o.get("reference", "")):
                    m = re.match(r"\s*(HIPAA|NIST CSF|HPH CPG|HICP)\s*:\s*(.*)$",
                                 line.strip())
                    if m:
                        r_cites.append([oid, f"fw_{slug(m.group(1))}", "CITES",
                                        m.group(2).strip(), SRC])

        for v in s.get("vulnerabilities", []):
            vid = f"{sec_id}_{slug(v['id'])}"
            n_vuln.append([vid, v["id"], sec_id, v["title"],
                           len(v.get("threats", [])), SRC])
            r_has_vuln.append([sec_id, vid, "HAS_VULNERABILITY", SRC])
            for t in v.get("threats", []):
                r_has_threat.append([vid, threat_id(t), "HAS_THREAT", SRC])

    # =========================== CRI ====================================
    cri = json.loads((DATA / "cri_statements.json").read_text())
    n_asmt.append(["asmt_expert", "Expert Questionnaire (CRI Profile v2.1)",
                   "CRI Profile v2.1", "diagnostic", len(cri), 0,
                   "ExpertQuestionnaireTab.tsx, MaturityAssessmentPage.tsx", "", "",
                   SRC])
    r_sourced.append(["asmt_expert", cri_src, "SOURCED_FROM", SRC])

    cri_by_stmtid: dict[str, list[str]] = {}
    cri_domains: dict[str, int] = {}
    cri_stmt_ids: list[tuple[str, str]] = []   # (node_id, statement_id)
    for x in cri:
        cat = x["category"]
        cri_domains[cat] = cri_domains.get(cat, 0) + 1
    for cat, cnt in cri_domains.items():
        dom_id = f"dom_cri_{slug(cat)}"
        n_dom.append([dom_id, cat, "cri_dtom", cnt, SRC])
        r_has_domain.append(["asmt_expert", dom_id, "HAS_DOMAIN", SRC])
    seen_cri: dict[str, int] = {}
    for x in cri:
        base = f"stmt_cri_{slug(x['statement_id'])}"
        seen_cri[base] = seen_cri.get(base, 0) + 1
        sid = base if seen_cri[base] == 1 else f"{base}_{seen_cri[base]}"
        n_stmt.append([sid, "expert", x["statement_id"], x["description"],
                       x["subcategory"], x["category"], "", "true", "false", SRC])
        r_has_statement.append([f"dom_cri_{slug(x['category'])}", sid,
                                "HAS_STATEMENT", SRC])
        if x["subcategory"].strip():
            r_in_sub.append([sid, subcat_id(x["subcategory"]), "IN_SUBCATEGORY", SRC])
        cri_by_stmtid.setdefault(x["statement_id"], []).append(sid)
        cri_stmt_ids.append((sid, x["statement_id"]))

    # ======================== Maturity ==================================
    n_asmt.append(["asmt_maturity", "Maturity Assessment",
                   "CRI Profile v2.1", "diagnostic",
                   0, 0, "maturityAssessment agents (one per domain)",
                   "/dtop/api/v3/maturity-assessment/{type}/", "", SRC])

    mat_total = 0
    mat_by_stmtid: dict[str, list[str]] = {}
    for dom, (mstem, cstem) in MATURITY.items():
        dom_id = f"dom_mat_{slug(dom)}"
        md_rows = read_md(mstem)
        csv_rows = read_csv_bank(cstem)
        csv_text = {c[1].strip() for c in csv_rows}
        md_text = {m[1].strip() for m in md_rows}

        # union keyed by verbatim statement cell, md order first then csv-only
        order: list[tuple[str, str, str]] = list(md_rows)
        for c in csv_rows:
            if c[1].strip() not in md_text:
                order.append(c)

        r_has_domain.append(["asmt_maturity", dom_id, "HAS_DOMAIN", SRC])
        r_sourced += [["asmt_maturity", md_src[dom], "SOURCED_FROM", SRC],
                      ["asmt_maturity", csv_src[dom], "SOURCED_FROM", SRC]]

        for i, (subj, stmt_cell, subcat) in enumerate(order, 1):
            sid = f"stmt_mat_{slug(dom)}_{i:03d}"
            stmt_id, desc = split_statement(stmt_cell)
            in_md = "true" if stmt_cell.strip() in md_text else "false"
            in_csv = "true" if stmt_cell.strip() in csv_text else "false"
            n_stmt.append([sid, "maturity", stmt_id, desc, subcat, dom,
                           subj, in_md, in_csv, SRC])
            r_has_statement.append([dom_id, sid, "HAS_STATEMENT", SRC])
            if subcat.strip():
                r_in_sub.append([sid, subcat_id(subcat), "IN_SUBCATEGORY", SRC])
            for t in re.findall(r"#\w+", subj):
                r_tagged.append([sid, tag_id(t), "TAGGED", SRC])
            if stmt_id:
                mat_by_stmtid.setdefault(stmt_id, []).append(sid)
            mat_total += 1

        n_dom.append([dom_id, dom, "maturity", len(order), SRC])

    # fill the maturity assessment's item count now that it is known
    for row in n_asmt:
        if row[0] == "asmt_maturity":
            row[4] = mat_total

    # ALSO_IN: each CRI statement -> maturity statements sharing its id
    for sid, stmt_id in cri_stmt_ids:
        for msid in mat_by_stmtid.get(stmt_id, []):
            r_also_in.append([sid, msid, "ALSO_IN", stmt_id, SRC])

    # ===================== emit shared-taxonomy nodes ===================
    n_sub = [[i, text, SRC] for text, i in subcats.items()]
    n_tag = [[i, t, SRC] for t, i in tags.items()]
    n_thr = [[i, text, SRC] for text, i in threats.items()]
    n_fw = [["fw_hipaa", "HIPAA", "HIPAA Security Rule citations", SRC],
            ["fw_nist_csf", "NIST CSF", "NIST Cybersecurity Framework subcategories", SRC],
            ["fw_hph_cpg", "HPH CPG", "HPH Cybersecurity Performance Goals", SRC],
            ["fw_hicp", "HICP", "Health Industry Cybersecurity Practices", SRC]]

    # ============================ write =================================
    write("nodes_Assessment.csv",
          ["assessment_id", "name", "framework", "kind", "item_count",
           "vulnerability_count", "ui", "routes", "notes", "source_document"], n_asmt)
    write("nodes_DataSource.csv",
          ["datasource_id", "path", "format", "note", "source_document"], n_ds)
    write("nodes_Section.csv",
          ["section_id", "label", "title", "question_count", "vulnerability_count",
           "source_document"], n_sec)
    write("nodes_Question.csv",
          ["question_id", "label", "section_id", "text", "option_count",
           "source_document"], n_q)
    write("nodes_AnswerOption.csv",
          ["answeroption_id", "question_id", "ordinal", "text", "education",
           "reference", "next", "source_document"], n_opt)
    write("nodes_Vulnerability.csv",
          ["vulnerability_id", "label", "section_id", "title", "threat_count",
           "source_document"], n_vuln)
    write("nodes_Threat.csv", ["threat_id", "text", "source_document"], n_thr)
    write("nodes_ReferencedFramework.csv",
          ["referencedframework_id", "name", "description", "source_document"], n_fw)
    write("nodes_Domain.csv",
          ["domain_id", "name", "domain_kind", "statement_count", "source_document"],
          n_dom)
    write("nodes_Statement.csv",
          ["statement_id_key", "assessment", "statement_id", "description",
           "subcategory", "domain", "subject_tags", "in_md", "in_csv",
           "source_document"], n_stmt)
    write("nodes_Subcategory.csv",
          ["subcategory_id", "path", "source_document"], n_sub)
    write("nodes_SubjectTag.csv", ["subjecttag_id", "tag", "source_document"], n_tag)
    write("nodes_SupersededText.csv",
          ["supersededtext_id", "label", "section_id", "text", "source_document"],
          n_sup)

    write("rels_HAS_SECTION.csv", ["source_id", "target_id", "rel_type",
                                   "source_document"], r_has_section)
    write("rels_HAS_QUESTION.csv", ["source_id", "target_id", "rel_type",
                                    "source_document"], r_has_question)
    write("rels_HAS_OPTION.csv", ["source_id", "target_id", "rel_type",
                                  "source_document"], r_has_option)
    write("rels_LEADS_TO.csv", ["source_id", "target_id", "rel_type",
                                "next_label", "source_document"], r_leads_to)
    write("rels_HAS_VULNERABILITY.csv", ["source_id", "target_id", "rel_type",
                                         "source_document"], r_has_vuln)
    write("rels_HAS_THREAT.csv", ["source_id", "target_id", "rel_type",
                                  "source_document"], r_has_threat)
    write("rels_CITES.csv", ["source_id", "target_id", "rel_type", "citation",
                             "source_document"], r_cites)
    write("rels_HAS_DOMAIN.csv", ["source_id", "target_id", "rel_type",
                                  "source_document"], r_has_domain)
    write("rels_HAS_STATEMENT.csv", ["source_id", "target_id", "rel_type",
                                     "source_document"], r_has_statement)
    write("rels_IN_SUBCATEGORY.csv", ["source_id", "target_id", "rel_type",
                                      "source_document"], r_in_sub)
    write("rels_TAGGED.csv", ["source_id", "target_id", "rel_type",
                              "source_document"], r_tagged)
    write("rels_ALSO_IN.csv", ["source_id", "target_id", "rel_type",
                               "statement_id", "source_document"], r_also_in)
    write("rels_SOURCED_FROM.csv", ["source_id", "target_id", "rel_type",
                                    "source_document"], r_sourced)
    write("rels_SUPERSEDES.csv", ["source_id", "target_id", "rel_type",
                                  "source_document"], r_supersedes)
    write("rels_HAD_PRIOR_TEXT.csv", ["source_id", "target_id", "rel_type",
                                      "source_document"], r_prior)
    write("rels_FROM_SOURCE.csv", ["source_id", "target_id", "rel_type",
                                   "source_document"], r_from_src)

    total_nodes = (len(n_asmt) + len(n_ds) + len(n_sec) + len(n_q) + len(n_opt) +
                   len(n_vuln) + len(n_thr) + len(n_fw) + len(n_dom) + len(n_stmt) +
                   len(n_sub) + len(n_tag) + len(n_sup))
    total_rels = (len(r_has_section) + len(r_has_question) + len(r_has_option) +
                  len(r_leads_to) + len(r_has_vuln) + len(r_has_threat) +
                  len(r_cites) + len(r_has_domain) + len(r_has_statement) +
                  len(r_in_sub) + len(r_tagged) + len(r_also_in) + len(r_sourced) +
                  len(r_supersedes) + len(r_prior) + len(r_from_src))
    print(f"\n  TOTAL {total_nodes} nodes / {total_rels} relationships")


if __name__ == "__main__":
    print("reading DTOP-OLD assessment banks")
    main()
