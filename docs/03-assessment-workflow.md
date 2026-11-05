# 03 — Reproducible supplier-assessment workflow

1. **Intake and classification.** Create vendor ID; identify service, service owner, business function, personal data, hosting geography, subprocessors, alternative providers, and whether DORA *critical or important function* status is justified. Use `templates/vendor-intake.md`.
2. **Tier and scope.** Decide Tier 1/2/3 based on impact and substitutability. Higher tiers receive deeper due diligence and more frequent review; document the reasons.
3. **Send questionnaire.** Use `data/questionnaire.csv`. Seek evidence such as MFA configuration exports, independent audit reports, DR test outcomes, incident procedures, subprocessor lists and contracts. Do not request secrets or unrelated personal data.
4. **Log evidence.** Capture source, date, scope, limitations and independent verification status in `data/evidence_register.csv`. In this exercise all documents are fictional.
5. **Challenge responses.** Mark `Yes`, `Partial`, `No`, or `Unknown`; record answers and evidence IDs in `data/vendor_responses.csv`. Missing evidence is not assumed to mean a control does not exist, but cannot justify a claim of assurance.
6. **Threat scenarios and scoring.** Describe plausible risk events (not vague labels), score inherent risk, document claimed controls, and explain residual likelihood/impact in `data/risk_register.csv`. **Unverified assertions receive no numerical reduction** under this case-study policy; use `data/calibration_log.csv` to inspect each changed judgment.
7. **Decide and remediate.** Use the risk appetite in `01-case-study.md`. Capture owner, acceptance criteria, due date, status, and escalation in `data/remediation_tracker.csv`.
8. **Contract review.** Send the conditional checklist to Legal/DPO. Contract clauses are **not** self-certification of compliance. Apply DORA requirements based on entity/function status and GDPR Article 28 only to processor relationships.
9. **Monitor and exit.** Schedule periodic attestations, material incident review, access review, critical service continuity/exit planning, subcontractor changes, and end-of-contract data return/deletion.

## Approval gates used for this simulation

| Supplier | Risk decision | Additional mandatory gate | Onboarding outcome |
|---|---|---|---|
| CLOUD-001 | Hold (critical residual privileged access risk) | DORA critical-function contract and demonstrable exit/testing obligations | **HOLD** |
| PAY-001 | Hold (high residual; unverified controls) | Executed GDPR-compliant processor agreement before live personal-data processing | **HOLD — DO NOT PROCESS DATA** |
| SUP-001 | Hold (high residual findings; unverified controls) | Processor agreement and enforceable incident notification clause, if processor role applies | **HOLD** |

No approval in the sample has been made by a real risk committee or legal team.
