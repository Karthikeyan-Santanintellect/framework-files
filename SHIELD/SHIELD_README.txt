NY SHIELD ACT KNOWLEDGE-GRAPH CSV SET
=====================================
Framework : Stop Hacks and Improve Electronic Data Security Act ("SHIELD Act")
Statute   : N.Y. Gen. Bus. Law §§ 899-aa (breach notification) and 899-bb (data security protections)
Enacted   : S.5575-B / Ch. 117, Laws of 2019
Version   : NY SHIELD 1.0

SCOPE OF THIS DATA SET
----------------------
This is a purely STATUTORY / DEFINITIONAL graph. Every row is derived from the
text of §§ 899-aa and 899-bb. There are NO instance-level records: no companies,
no named persons, no auditors, no breach incidents, no dates of implementation,
no compliance scores. Anything of that kind that previously shipped here was
synthetic and has been removed.

Every node carries an `official_citation` (or `section_id`) tying it back to the
statute, and safeguard / definition text is reproduced verbatim from the statute.

FILES
-----
Node files
  SHIELD - Sections.csv
      35 statutory provisions: §899-aa definitions (1)(a)-(d), notification
      duties (2),(3), methods of notice (5), enforcement and penalties (6)(a),
      statute of limitations (6)(c), agency and CRA notice (8)(a),(b); and
      §899-bb compliant-regulated-entity and small-business definitions,
      the reasonable security requirement (2)(a)-(c), enforcement (2)(d) and
      the no-private-right-of-action clause (2)(e). Column `text` is verbatim.

  SHIELD_StatutoryDefinition_nodes.csv
      9 defined terms: personal information, private information, breach of the
      security of the system, consumer reporting agency, the person/business
      duty-bearer, service provider, compliant regulated entity, small business,
      and the no-private-right-of-action rule.

  SHIELD_PrivateInformation_nodes.csv
      The 6 data elements enumerated in §899-aa(1)(b)(i)(1)-(5) and (1)(b)(ii),
      plus the publicly-available-information exclusion.

  SHIELD_AdministrativeSafeguard_nodes.csv   6 rows, §899-bb(2)(b)(ii)(A)(1)-(6)
  SHIELD_TechnicalSafeguard_nodes.csv        4 rows, §899-bb(2)(b)(ii)(B)(1)-(4)
  SHIELD - Physical Safeguard.csv            4 rows, §899-bb(2)(b)(ii)(C)(1)-(4)
      Exactly the safeguards the statute enumerates, verbatim, and nothing else.

  SHIELD - Data Definitions.csv
      Data-element combination patterns that constitute private information.

  SHIELD - Legal Entities.csv
      Bodies with a role under the Act: NY Attorney General, NY Department of
      State, NY State Police, consumer reporting agencies, and the small-business
      classification.

  SHIELD - Legal Rules.csv
      Penalty amounts and caps (§899-aa(6)(a), §899-bb(2)(d)), the three/six-year
      limitations periods (§899-aa(6)(c)), the good-faith / inadvertent-disclosure
      exception, and the "unauthorized access" construction rule.

  SHIELD - Safe Harbor.csv
      The four compliant-regulated-entity safe harbours of §899-bb(1)(a)(i)-(iv):
      GLBA Title V, HIPAA/HITECH, 23 NYCRR Part 500, and the catch-all.

Relationship files
  SHIELD_DEFINED_IN_SECTION_relationships.csv
      23 edges. Each safeguard node and each statutory definition node points at
      the section of "SHIELD - Sections.csv" that establishes it.

  SHIELD_COMBINES_WITH_DATA_ELEMENT_relationships.csv
      6 edges. Data elements PI-001..PI-005 combine with personal information
      (DEF-001) to form private information under §899-aa(1)(b)(i); PI-006
      constitutes private information on its own under §899-aa(1)(b)(ii).

ID CONVENTIONS
--------------
  ADMIN-nnn / TECH-nnn / PHYS-nnn  enumerated safeguards
  DEF-nnn                          statutory definitions
  PI-nnn / PI-EXCL-nnn             private-information data elements, exclusions
  SH-*                             safe-harbour regimes
  DEC-* / PAI-* / PI-PARENT-*      data-element combination patterns
  NY_* / CRA_* / SB_DEF_*          legal entities and classifications
  CP-* / SOL-* / EXC-* / DEF-*     legal rules
  section_id                       bill-section notation, e.g. 4(2)(b)(ii)(A)(1)

INTEGRITY
---------
Zero dangling foreign keys: every source and target id in a relationship file
resolves to a row in a node file.

SOURCES
-------
  NY Senate Bill S.5575-B (2019-2020 Regular Sessions), statute text as enacted.
  N.Y. Gen. Bus. Law §§ 899-aa, 899-bb.
