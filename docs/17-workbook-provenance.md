# 17 — Workbook provenance and version controls

This repository contains an Excel workbook, `Third_Party_Risk_Assessment.xlsx`, originally generated for the **v1.1 baseline assessment**. It is **not** a live report of the later simulated follow-up and monitoring phases.

## Known repository-file discrepancy (QA-01)

The workbook's `Vendors!F3` currently contains **CONDITIONAL - NO LIVE DATA** (an obsolete draft), even though `data/vendors.csv`, `data/risk_register.csv`, and the workbook's own `Dashboard` record correctly show **HOLD** for the initial Helios payroll assessment.

An updated **v1.3 reviewed workbook** has been generated outside the repository. It corrects `Vendors!F3`, retains the ten historical worksheets, and adds:
- `Phase Comparison`: three vendors across v1.1 baseline, v1.2 follow-up and v1.3 event monitoring, with the latest highest risk score.
- `Risk Evolution`: all six risk scores across three phases, calculated as likelihood multiplied by impact.
- An explicit baseline note on the original `Dashboard` tab.

**Action required before public release:** Replace the stale repository workbook with the reviewed v1.3 workbook (or commit that newer workbook as an additional versioned file and explicitly archive the original). Validate the committed file rather than assuming a local download and GitHub's copy are identical.

## Authoritative data by phase

| Scope | Authoritative source |
| --- | --- |
| Initial assessment | `data/risk_register.csv`, `data/vendors.csv` |
| Reassessment and conditional simulated decision | `phase2/data/reassessment.csv`, `phase2/data/decision_gates.csv` |
| Monitoring and most recent scenario | `phase3/data/event_reassessment.csv`, `phase3/data/decision_gates.csv` |
| Cross-phase decision history | `phase3/data/decision_history.csv` |

The historical `data/calibration_log.csv` intentionally retains earlier rejected draft values; those are not current approvals.

## Verification targets after replacing Excel

1. The `Vendors` sheet shows PAY-001 **HOLD**.
2. The `Dashboard` states it is a v1.1 baseline, not the latest decision.
3. The `Phase Comparison` sheet shows payroll: HOLD → CONDITIONAL (SIMULATED) → HOLD.
4. `Risk Evolution` shows R-001: **20 → 10 → 10** and R-003: **12 → 8 → 12**.
5. There are no formula errors, and all latest decisions remain fictional.
6. Before changing repository visibility, run the publication audit in strict mode against the updated workbook.

Do not represent this simulated workbook as an actual compliance attestation, supplier audit, or operational risk register.
