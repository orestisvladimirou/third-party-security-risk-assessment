#!/usr/bin/env python3
"""Read-only pre-publication checks for the fictional assessment portfolio.

Default mode reports actionable warnings without failing routine CI.
Use --strict before making the repository public: warnings become errors.
No external dependencies and no workbook changes.
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from validate_phase3 import ROOT, p3_load, validate_phase3

XMLNS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
WORKBOOK = ROOT / "Third_Party_Risk_Assessment.xlsx"

def local_link_issues():
    issues = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for link in pattern.findall(file.read_text(encoding="utf-8")):
            target = link.split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            if not (file.parent / target).exists():
                issues.append(f"Broken local link {file.relative_to(ROOT)} -> {target}")
    return issues

def workbook_audit():
    issues = []
    if not WORKBOOK.is_file():
        return ["Workbook is missing from the repository"]
    try:
        with zipfile.ZipFile(WORKBOOK) as archive:
            workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            sheets = [x.attrib["name"] for x in workbook.findall(".//" + XMLNS + "sheet")]
            # The imported workbook's second worksheet is named Vendors in both versions.
            if len(sheets) < 2 or sheets[1] != "Vendors":
                issues.append("Unexpected workbook sheet order; review Vendors manually")
            else:
                vendor_xml = ET.fromstring(archive.read("xl/worksheets/sheet2.xml"))
                cell = vendor_xml.find(".//" + XMLNS + "c[@r='F3']")
                value = cell.find(XMLNS + "v").text if cell is not None and cell.find(XMLNS + "v") is not None else None
                if value != "HOLD":
                    issues.append(f"Workbook Vendors!F3 is {value!r}, expected HOLD (QA-01)")
            for required in ("Phase Comparison", "Risk Evolution"):
                if required not in sheets:
                    issues.append(f"Repository workbook lacks reviewed v1.3 sheet: {required}")
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        issues.append(f"Could not audit Excel workbook: {exc}")
    return issues

def audit(strict=False):
    validate_phase3()
    issues = local_link_issues() + workbook_audit()
    decisions = {x["vendor_id"]: x["phase3_decision"] for x in p3_load("decision_gates.csv")}
    assert decisions == {"CLOUD-001": "HOLD", "PAY-001": "HOLD", "SUP-001": "HOLD"}
    print("PASS: Phase 1–3 consistency and newest simulated supplier decisions.")
    if issues:
        for problem in issues:
            print("PUBLICATION WARNING:", problem)
        if strict:
            raise SystemExit(f"BLOCKED: {len(issues)} pre-publication issue(s).")
        print(f"NOT PUBLICATION READY: {len(issues)} outstanding warning(s); use --strict for release gate.")
    else:
        print("PASS: workbook version and local documentation links match the latest review.")
    return issues

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--strict", action="store_true", help="Fail if publication warnings remain")
    args = p.parse_args()
    audit(strict=args.strict)
