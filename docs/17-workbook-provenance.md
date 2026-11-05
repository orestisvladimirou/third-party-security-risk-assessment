# 17 — Workbook provenance and version controls

This repository contains the reviewed **v1.3 Excel workbook**, with the historical v1.1 dashboard preserved and additional Phase Comparison and Risk Evolution sheets. No worksheet represents a live supplier assessment.

## Resolved repository-file discrepancy (QA-01)

The original workbook had an obsolete **CONDITIONAL - NO LIVE DATA** entry at `Vendors!F3`. The corrected workbook on GitHub now displays **HOLD** for that initial assessment.

The reviewed **v1.3 workbook was committed** to GitHub as commit `e22e4c7a`. It corrects `Vendors!F3`, retains the ten historical worksheets, and adds:
- `Phase Comparison`: three vendors across v1.1 baseline, v1.2 follow-up and v1.3 event monitoring, with the latest highest risk score.
- `Risk Evolution`: all six risk scores across three phases, calculated as likelihood multiplied by impact.
- An explicit baseline note on the original `Dashboard` tab.

**Verification:** The one-time upgrade workflow executed the strict publication audit successfully against the regenerated workbook before committing it. The later routine checks should continue to run against the committed file.

## Authoritative data by phase

| Scope | Authoritative source |
| --- | --- |
| Initial assessment | `data/risk_register.csv`, `data/vendors.csv` |
| Reassessment and conditional simulated decision | `phase2/data/reassessment.csv`, `phase2/data/decision_gates.csv` |
| Monitoring and most recent scenario | `phase3/data/event_reassessment.csv`, `phase3/data/decision_gates.csv` |
| Cross-phase decision history | `phase3/data/decision_history.csv` |

The historical `data/calibration_log.csv` intentionally retains earlier rejected draft values; those are not current approvals.

## Verification targets (satisfied in reviewed workbook)

1. The `Vendors` sheet shows PAY-001 **HOLD**.
2. The `Dashboard` states it is a v1.1 baseline, not the latest decision.
3. The `Phase Comparison` sheet shows payroll: HOLD → CONDITIONAL (SIMULATED) → HOLD.
4. `Risk Evolution` shows R-001: **20 → 10 → 10** and R-003: **12 → 8 → 12**.
5. There are no formula errors, and all latest decisions remain fictional.
6. Before changing repository visibility, run the publication audit in strict mode against the updated workbook.

Do not represent this simulated workbook as an actual compliance attestation, supplier audit, or operational risk register.
