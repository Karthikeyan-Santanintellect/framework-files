TISAX Knowledge-Graph CSV Set
==================================================

Framework : TISAX (Trusted Information Security Assessment Exchange)
Owner     : ENX Association (governs TISAX; the VDA publishes the ISA)
Source    : "TISAX Participant Handbook", version 2.8, dated 2025-03-13,
            ENX doc ID 602, classification Public.
Criteria  : ISA (Information Security Assessment) - the handbook links the
            catalogue download portal.enx.com/isa5-en.xlsx, i.e. ISA 5.
            The audit provider uses the ISA version that is valid when the
            initial assessment is ordered (Handbook 7.11).

SCOPE OF THIS DATA SET
----------------------
This set models the TISAX FRAMEWORK ONLY - the process, the actors, the
assessment levels, the assessment objectives / TISAX labels, the ISA criteria
catalogues, the finding types and the overall assessment results, all as
defined in the handbook. It contains NO organisations, auditors, assessments,
scores, budgets or dates: those would be instance data and are not defined by
the source document. All previously present fictional instance rows have been
removed.

FILES THAT SHIP (17)
--------------------
Node files
1.  TISAX_AssessmentObjective_nodes.csv (12 rows)
    The 12 current TISAX assessment objectives / TISAX labels
    (Handbook Table 3, p.33), with the applicable ISA criteria catalogue(s)
    (Table 7, p.58-59) and the implied assessment level (Table 5, p.39).
2.  TISAX_AssessmentLevel_nodes.csv (3 rows)
    AL 1 / AL 2 / AL 3 and the assessment methods per level
    (Handbook 4.3.3.5, Table 6, p.40-42). Label validity 3 years
    (5.4.14.2); AL 1 results are not used in TISAX, hence "n/a".
3.  TISAX_ISACatalogue_nodes.csv (3 rows)
    The three ISA criteria catalogues: Information Security, Prototype
    Protection, Data Protection (Handbook 5.2.2.1, p.58).
4.  TISAX_ProtectionObject_nodes.csv (8 rows)
    The protection objects named by the 12 assessment objectives
    (information with high / very high protection needs, prototype parts and
    components, prototype vehicles, test vehicles, prototypes at events and
    shootings, personal data, special categories of personal data).
5.  TISAX_AuditProvider_nodes.csv (1 row)
    The CONCEPT of a TISAX audit provider as defined by the handbook
    (contracted by ENX Association, impartial, may assess registered
    participants only). No individual firms - the handbook does not list any;
    contact details are only issued in the registration confirmation email.
6.  TISAX_AssessmentResult_nodes.csv (3 rows)
    The three possible overall assessment results: conform, minor
    non-conform, major non-conform (Handbook 5.4.5, p.87), with the label
    consequence of each. Instance columns (dates, auditor, URLs, percentages)
    are retained for schema stability but are intentionally empty.
7.  TISAX_Exchange_nodes.csv (1 row)
    The ENX portal exchange platform and its publishing/sharing mechanics
    (Handbook 6, p.101-106).
8.  TISAX_ControlQuestion_nodes.csv (HEADER ONLY - 0 rows)
    The ISA control questions live in a separate VDA document (the ISA Excel
    workbook) which is NOT part of this source. Nothing is fabricated here.
9.  findings.csv (4 rows)
    The four TISAX finding types: major non-conformity, minor
    non-conformity, observation, room for improvement (Handbook Table 11,
    p.85-86), with their definitions and required reactions.
10. roles.csv (9 rows)
    The actors defined by the handbook: ENX Association, TISAX participant,
    active participant, passive participant, TISAX audit provider, auditor,
    participant main contact, assessment scope contact, person in charge of
    information security.
11. assessment_phases.csv (10 rows)
    The real TISAX process: the 3 steps (registration, assessment, exchange)
    expanded into the handbook's sub-steps and assessment types (kick-off
    meeting, assessment phase 1, initial assessment, corrective action plan
    preparation and assessment, follow-up assessment).
    typical_duration_weeks is empty on purpose - the handbook explicitly
    declines to forecast durations.
12. control_categories.csv (5 rows)
    Only the ISA chapters the handbook actually enumerates: 8.1 - 8.5 of the
    Prototype Protection criteria catalogue (Handbook Table 8, p.61-62).

Relationship files
13. TISAX_LABEL_HIERARCHY_relationships.csv (7 rows)
    The TISAX label superset hierarchy (Handbook 5.4.14.1, p.98).
14. TISAX - ISA Catalogue Control Category.csv (5 rows)
    ISA-002 (Prototype Protection) HAS_CATEGORY CAT-01..CAT-05.
15. TISAX - Assement Result Findings.csv (4 rows)
    Overall assessment result CONTAINS_FINDING finding type, encoding the
    handbook's rule that a minor non-conformity yields "minor non-conform"
    (temporary labels) and a major non-conformity yields "major non-conform"
    (no labels).
16. TISAX_ISA_CONTAINS_QUESTIONS.csv (HEADER ONLY - 0 rows)
    Empty because TISAX_ControlQuestion_nodes.csv is header-only.

Other
17. TISAX_README.txt (this file)

FILES REMOVED IN THIS PASS (23)
-------------------------------
All of the following contained only invented instance data (fictional
companies, auditors, assessments, results, budgets, URLs, dates) and had no
counterpart in the handbook:
  TISAX_Organization_nodes.csv, TISAX_Participant_nodes.csv,
  TISAX_Assessment_nodes.csv, TISAX - Requirements.csv,
  TISAX_REGISTERS_IN_TISAX_relationships.csv,
  TISAX_PARTICIPANT_REGISTERS_IN_TISAX_relationships.csv,
  TISAX_PARTICIPATES_IN_EXCHANGE_relationships.csv,
  TISAX_SHARES_RESULTS_WITH_relationships.csv,
  TISAX_SELECTS_ASSESSMENT_LEVEL_relationships.csv,
  TISAX_UNDERGOES_ASSESSMENT_relationships.csv,
  TISAX_Organisation_Chooses_AuditProvider_relationships.csv,
  TISAX_CONTAINS_ASSESSMENT_OBJECTIVE_relationships.csv,
  TISAX_ISA_CATALOGUE_relationships.csv,
  TISAX_MEETS_CRITERIA_relationships.csv,
  TISAX_PROTECTS_OBJECT_relationships.csv,
  TISAX_RESULT_OF_ASSESSMENT_relationships.csv,
  TISAX_ANSWERS_FULLY_UNIQUE_relationships.csv,
  TISAX - Assesment Assesment Phase.csv,
  security_policies.csv, rel_org_establishes_policy.csv,
  data_categories.csv, rel_object_classified_as.csv,
  rel_org_assigns_role.csv

KEY FACTS ENCODED (all from Handbook 2.8)
-----------------------------------------
- 3-step process: Registration -> Assessment -> Exchange.
- Assessment sub-steps: preparation (ISA self-assessment), audit provider
  selection, the assessment(s), assessment result.
- Assessment types: initial, corrective action plan, follow-up.
- Assessment elements: formal opening meeting, assessment procedure, formal
  closing meeting.
- Assessment levels AL 1 / AL 2 / AL 3 and their methods; AL 2.5 exists as an
  alternate method for AL 2 but is formally evaluated as AL 2.
- Protection needs: normal, high, very high; protection goals C / I / A.
- 12 assessment objectives; TISAX labels are the corresponding output.
- Label validity: 3 years from the end of the assessment process. Temporary
  labels: up to 9 months after the closing meeting of the initial assessment,
  bounded by the longest corrective-action implementation period.
- Nine-month maximum to resolve non-conformities after the initial
  assessment's closing meeting.
- Corrective action plan content: finding, root cause, corrective actions,
  implementation date, compensating measures, justified implementation
  periods (>3 months justification, >6 months justification + evidence,
  never >9 months).
- Report sections A-E map 1:1 to the exchange platform sharing levels.
- Maturity levels 0-5 (Incomplete, Performed, Managed, Established,
  Predictable, Optimizing) - defined in the ISA, described in Handbook
  Table 10.

RESIDUAL GAPS / KNOWN LIMITATIONS
---------------------------------
- ISA control questions and requirements are NOT included. They are published
  by the VDA in a separate ISA workbook, not in the handbook.
- Only the Prototype Protection chapters (8.1-8.5) are modelled in
  control_categories.csv; the handbook names Information Security and Data
  Protection chapters only by example ("2 Human Resources", "9 Access
  Control"), so they are not enumerated here.
- The handbook also defines participant status (Incomplete, Awaiting
  approval, Preliminary, Registered, Expired), assessment scope status
  (Incomplete, Awaiting your order, Awaiting ENX approval, Awaiting your
  payment, Registered, Active, Expired) and assessment status (Initial
  assessment ordered, Initial assessment ongoing, Waiting for corrective
  action plan assessment, Waiting for follow-up, Finished). These state
  machines have no corresponding CSV in this set.
- TISAX_ProtectionObject_nodes.csv has no relationship file linking it to the
  assessment objectives; the previous PROTECTS_OBJECT file was
  assessment-instance based and was deleted.

Foreign-key integrity: verified, zero dangling references.
Status: framework-grounded, ready for graph load.
