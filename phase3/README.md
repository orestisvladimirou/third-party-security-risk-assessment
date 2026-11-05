# Phase 3 — Ongoing supplier monitoring and event-triggered reassessment

**Independent fictional training scenario, not a real supplier review.** Modeled monitoring event: **1 December 2026** (future scenario date).

Following Phase 2's *fictional* conditional decision for payroll, a supplier-change notice identifies a proposed new subprocessor whose access and processing location have not been adequately evidenced. The assessment reopens the privacy/contract gate, reconsiders one risk score and places payroll back on **HOLD**.

## Follow the audit trail

1. [Supplier monitoring program](docs/13-monitoring-program.md)
2. [Invented subprocessor-change notice](evidence/P3-E01-payroll-change.md)
3. [Monitoring plan](data/monitoring_plan.csv) and [trigger log](data/monitoring_events.csv)
4. [Event-driven risk reassessment](data/event_reassessment.csv)
5. [Decision history](data/decision_history.csv) and [control gates](data/decision_gates.csv)
6. [Remediation actions](data/new_actions.csv)
7. [Management escalation report](docs/14-monitoring-report.md)

The v1.1 baseline remains in `data/`; Phase 2 follow-up remains in `phase2/`. Phase 3 is a separate point-in-time case. All “events”, people, decisions and evidence are invented.

Validate with `python scripts/validate_phase3.py` and `python -m unittest discover -s tests -v`.
