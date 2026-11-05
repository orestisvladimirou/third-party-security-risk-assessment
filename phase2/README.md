# Phase 2 — Fictional supplier evidence follow-up

**Educational simulation only.** No real supplier was tested or approved. Hypothetical follow-up date: 19 November 2026.

The v1.1 baseline is in `data/`; this follow-up does not overwrite its scores. The Excel workbook is a v1.1 snapshot, not a Phase 2 dashboard.

## Read in order

1. [Evidence assessment method](docs/10-evidence-method.md)
2. [Seven fictional evidence exhibits](evidence/)
3. [Evidence quality register](data/evidence_assessments.csv)
4. [Six reassessed risks](data/reassessment.csv)
5. [Action follow-ups](data/action_updates.csv)
6. [Approval and contract gates](data/decision_gates.csv)
7. [Management report](docs/11-reassessment-report.md)
8. [Decision audit trail](docs/12-decision-log.md)

## Scenario outcome

| Fictional supplier | Initial highest risk | Follow-up highest risk | Outcome |
| --- | --- | --- | --- |
| Cloud | 20 Critical | 15 High | HOLD |
| Payroll | 12 High | 8 Medium | CONDITIONAL — simulated only |
| Support | 16 High | 16 High | HOLD |

**Reasoning:** Scoped MFA evidence supports lower cloud account-compromise likelihood, but cloud recovery and contracting remain open. Payroll access and fallback exercises support lower risk; fictional contractual clearance is evaluated as an independent gate. Support supplies drafts rather than working controls, so its risks stay unchanged.

To validate, from the repository root run:

```bash
python scripts/validate_project.py
python scripts/validate_phase2.py
python -m unittest discover -s tests -v
```

All exhibits are synthetic and any simulated legal clearance is a scenario assumption, never a real executed agreement. No decision authorizes handling actual data.
