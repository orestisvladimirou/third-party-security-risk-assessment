#!/usr/bin/env python3
"""One-time, reproducible upgrade of the simulated assessment workbook.

Preserves all ten historical v1.1 worksheets. Uses the versioned CSVs as
authoritative data for two additional cross-phase sheets. No live data.
"""
import csv
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "Third_Party_Risk_Assessment.xlsx"
NAVY = "142B44"
BLUE = "24527A"
PALE = "EAF2F8"
WHITE = "FFFFFF"
DARK = "263749"
MUTED = "617487"

def records(path):
    with (ROOT / path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def setup(ws, title, headers, widths):
    ws.sheet_view.showGridLines = False
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(headers))
    ws.cell(1, 1, title)
    ws.cell(1, 1).font = Font(name="Aptos Display", size=15, color=WHITE, bold=True)
    ws.cell(1, 1).fill = PatternFill("solid", fgColor=NAVY)
    ws.cell(1, 1).alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 34
    ws.row_dimensions[2].height = 11
    for col, (label, width) in enumerate(zip(headers, widths), 1):
        ws.column_dimensions[get_column_letter(col)].width = width
        c = ws.cell(3, col, label)
        c.font = Font(name="Aptos", size=10, color=WHITE, bold=True)
        c.fill = PatternFill("solid", fgColor=BLUE)
        c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws.row_dimensions[3].height = 31
    ws.freeze_panes = "C4"

def data_row(ws, row, values):
    for col, value in enumerate(values, 1):
        cell = ws.cell(row, col, value)
        cell.font = Font(name="Aptos", size=10, color=DARK)
        cell.fill = PatternFill("solid", fgColor=WHITE if row % 2 else PALE)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 29

def note(ws, row, text, last):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=last)
    c = ws.cell(row, 1, text)
    c.font = Font(name="Aptos", size=10, color=MUTED, italic=True)
    c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[row].height = 30

def main():
    wb = load_workbook(PATH)
    baseline_vendors = {r["vendor_id"]: r for r in records("data/vendors.csv")}
    baseline_risks = {r["risk_id"]: r for r in records("data/risk_register.csv")}
    p2_risks = {r["risk_id"]: r for r in records("phase2/data/reassessment.csv")}
    p3_risks = {r["risk_id"]: r for r in records("phase3/data/event_reassessment.csv")}
    p2_decisions = {r["vendor_id"]: r for r in records("phase2/data/decision_gates.csv")}
    p3_decisions = {r["vendor_id"]: r for r in records("phase3/data/decision_gates.csv")}
    assert len(baseline_vendors) == 3 and len(baseline_risks) == len(p2_risks) == len(p3_risks) == 6
    assert len(p2_decisions) == len(p3_decisions) == 3

    # Correct the obsolete initial payroll decision in the original workbook.
    vendors = wb["Vendors"]
    for row in range(2, vendors.max_row + 1):
        vid = vendors.cell(row, 1).value
        if vid in baseline_vendors:
            vendors.cell(row, 6).value = baseline_vendors[vid]["decision"]
    assert vendors["F3"].value == "HOLD"

    dashboard = wb["Dashboard"]
    dashboard["A25"] = ("This dashboard is the historical v1.1 baseline. "
                        "See Phase Comparison / Risk Evolution for hypothetical follow-ups.")
    dashboard["A25"].font = Font(name="Aptos", size=10, color=MUTED, italic=True)
    dashboard.merge_cells("A25:H25")
    dashboard.row_dimensions[25].height = 26

    for name in ("Phase Comparison", "Risk Evolution"):
        if name in wb:
            del wb[name]

    comp = wb.create_sheet("Phase Comparison")
    setup(comp, "SUPPLIER DECISION HISTORY | SIMULATED CASE STUDY",
          ["Supplier ID", "Supplier", "Baseline v1.1", "Phase 2 v1.2",
           "Phase 3 v1.3", "Latest highest risk"],
          [16, 26, 24, 26, 20, 21])
    for row, vid in enumerate(("CLOUD-001", "PAY-001", "SUP-001"), 4):
        p2 = p2_decisions[vid]["decision"]
        if p2 == "CONDITIONAL_SIMULATED":
            p2 = "CONDITIONAL (SIMULATED)"
        data_row(comp, row, [vid, baseline_vendors[vid]["vendor_name"],
                             baseline_vendors[vid]["decision"], p2,
                             p3_decisions[vid]["phase3_decision"],
                             int(p3_decisions[vid]["highest_score"])])
    note(comp, 8,
         "Latest scenario date: 2026-12-01. This is a fictional future event, not an actual assessment.", 6)
    note(comp, 10,
         "All suppliers, evidence, approvals and monitoring events are synthetic teaching examples.", 6)

    evo = wb.create_sheet("Risk Evolution")
    setup(evo, "SCENARIO RISK SCORE EVOLUTION",
          ["Risk ID", "Vendor", "Baseline L", "Baseline I", "Baseline score",
           "P2 L", "P2 I", "P2 score", "P3 L", "P3 I", "P3 score"],
          [14, 18] + [15] * 9)
    for row, rid in enumerate(sorted(baseline_risks), 4):
        b, p2, p3 = baseline_risks[rid], p2_risks[rid], p3_risks[rid]
        data_row(evo, row, [
            rid, b["vendor_id"],
            int(b["residual_likelihood"]), int(b["residual_impact"]), f"=C{row}*D{row}",
            int(p2["phase2_likelihood"]), int(p2["phase2_impact"]), f"=F{row}*G{row}",
            int(p3["phase3_likelihood"]), int(p3["phase3_impact"]), f"=I{row}*J{row}",
        ])
    note(evo, 11,
         "All scores are hypothetical ordinal likelihood × impact, not statistical forecasts or audited controls.", 11)

    assert wb.sheetnames[-2:] == ["Phase Comparison", "Risk Evolution"]
    assert len(wb.sheetnames) == 12
    wb.save(PATH)

if __name__ == "__main__":
    main()
