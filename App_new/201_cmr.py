"""Loader — 201 CMR 17.00 (Massachusetts Standards for the Protection of
Personal Information).

Verified and loaded 2026-07-23. Replaces an earlier draft whose LOAD CSV
statements were given an empty file path (so nothing loaded) and which created
a `Resident` node in place of the Service Provider.

The folder holds 17 single-row concept CSVs — the defined terms of 201 CMR
17.02 and the WISP / computer-system requirements of 17.03-17.04 — each with
its own bespoke columns. This loader reads them locally and sets every column
as a property, so no column can be mis-mapped, then wires the concepts together
with the relationships the regulation implies. Every node carries
`regional_standard_regulation_id = '201 CMR 17.00'`, so the framework appears in
the graph explorer alongside the other regional regulations.

    python App_new/201_cmr.py
"""

import csv
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import Neo4jConnect

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("201cmr")

RID = "201 CMR 17.00"
FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "201 CMR 17")

# file -> Neo4j label
NODE_FILES = {
    "201 CMR - Person.csv": "Person",
    "201 CMR - Resident.csv": "Resident",
    "201 CMR - Service Provider.csv": "ServiceProvider",
    "201 CMR - Employee.csv": "Employee",
    "201 CMR - Terminated Employee.csv": "TerminatedEmployee",
    "201 CMR - Personal Information.csv": "PersonalInformation",
    "201 CMR - Record.csv": "Record",
    "201 CMR - Security Policies.csv": "SecurityPolicy",
    "201 CMR - Inforamtion Security Program.csv": "InformationSecurityProgram",
    "201 CMR - Computer System.csv": "ComputerSystem",
    "201 CMR - User Authentication.csv": "UserAuthentication",
    "201 CMR - System Security Agent Software.csv": "SystemSecurityAgentSoftware",
    "201 CMR - Firewall Protection.csv": "FirewallProtection",
    "201 CMR - Portable Devices.csv": "PortableDevice",
    "201 CMR - Public Networks .csv": "PublicNetwork",
    "201 CMR - Wireless System .csv": "WirelessSystem",
    "201 CMR - Breach .csv": "BreachOfSecurity",
}

# (fromLabel, REL_TYPE, toLabel) — each label holds exactly one node, so every
# edge connects a single pair. Mirrors the operative logic of the regulation.
RELS = [
    ("RegionalStandardAndRegulation", "REGULATION_HAS_INFORMATION_SECURITY_PROGRAM", "InformationSecurityProgram"),
    ("Person", "PERSON_OWNS_PERSONAL_INFORMATION", "PersonalInformation"),
    ("Person", "PERSON_DEVELOPS_AND_MAINTAINS_INFORMATION_SECURITY_PROGRAM", "InformationSecurityProgram"),
    ("Person", "PERSON_OVERSEES_SERVICE_PROVIDER", "ServiceProvider"),
    ("Person", "PERSON_TRAINS_EMPLOYEE", "Employee"),
    ("Person", "PERSON_IMPOSES_DISCIPLINARY_MEASURES_ON_EMPLOYEE", "Employee"),
    ("Person", "PERSON_PREVENTS_ACCESS_BY_TERMINATED_EMPLOYEE", "TerminatedEmployee"),
    ("PersonalInformation", "PERSONAL_INFORMATION_RELATES_TO_RESIDENT", "Resident"),
    ("ServiceProvider", "SERVICE_PROVIDER_PERMITTED_ACCESS_TO_PERSONAL_INFORMATION", "PersonalInformation"),
    ("InformationSecurityProgram", "INFORMATION_SECURITY_PROGRAM_INCLUDES_SECURITY_POLICY", "SecurityPolicy"),
    ("InformationSecurityProgram", "INFORMATION_SECURITY_PROGRAM_PROTECTS_RECORDS", "Record"),
    ("InformationSecurityProgram", "INFORMATION_SECURITY_PROGRAM_ESTABLISHES_SECURITY_FOR_COMPUTER_SYSTEM", "ComputerSystem"),
    ("ComputerSystem", "COMPUTER_SYSTEM_REQUIRES_USER_AUTHENTICATION", "UserAuthentication"),
    ("ComputerSystem", "COMPUTER_SYSTEM_REQUIRES_FIREWALL_PROTECTION", "FirewallProtection"),
    ("ComputerSystem", "COMPUTER_SYSTEM_REQUIRES_SYSTEM_SECURITY_AGENT_SOFTWARE", "SystemSecurityAgentSoftware"),
    ("PortableDevice", "PORTABLE_DEVICE_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION", "PersonalInformation"),
    ("PublicNetwork", "PUBLIC_NETWORK_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION", "PersonalInformation"),
    ("WirelessSystem", "WIRELESS_SYSTEM_REQUIRES_ENCRYPTION_OF_PERSONAL_INFORMATION", "PersonalInformation"),
    ("BreachOfSecurity", "BREACH_OF_SECURITY_COMPROMISES_PERSONAL_INFORMATION", "PersonalInformation"),
]


def main():
    c = Neo4jConnect()
    if c.check_health() is not True:
        log.error("Neo4j unreachable"); return 1

    c.query(
        "MERGE (r:RegionalStandardAndRegulation {regional_standard_regulation_id:$rid}) "
        "SET r.name='Standards for the Protection of Personal Information of Residents of the Commonwealth', "
        "r.citation='201 CMR 17.00', r.version='17.00', r.type='State Regulation', "
        "r.jurisdiction='Massachusetts, USA', "
        "r.description='Minimum standards for safeguarding personal information of Massachusetts "
        "residents in paper and electronic records to prevent identity theft and fraud.'",
        others={"rid": RID})

    total = 0
    for fname, label in NODE_FILES.items():
        with open(os.path.join(FOLDER, fname), encoding="utf-8-sig", newline="") as fh:
            data = [dict(r) for r in csv.DictReader(fh)]
        c.query(
            f"UNWIND $rows AS row "
            f"MERGE (n:{label} {{regional_standard_regulation_id:$rid, node_id:row.node_id}}) "
            f"SET n += row",
            others={"rows": data, "rid": RID})
        total += len(data)

    for a, rel, b in RELS:
        c.query(f"MATCH (x:{a} {{regional_standard_regulation_id:$rid}}) "
                f"MATCH (y:{b} {{regional_standard_regulation_id:$rid}}) "
                f"MERGE (x)-[:{rel}]->(y)", others={"rid": RID})

    got = c.query("MATCH (n {regional_standard_regulation_id:$rid}) "
                  "OPTIONAL MATCH (n)-[r]->({regional_standard_regulation_id:$rid}) "
                  "RETURN count(DISTINCT n) AS n, count(DISTINCT r) AS r", others={"rid": RID})[0]
    log.info("in graph: %d nodes / %d relationships (%d concept rows + 1 regulation, %d rel types)",
             got["n"], got["r"], total, len(RELS))
    c.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
