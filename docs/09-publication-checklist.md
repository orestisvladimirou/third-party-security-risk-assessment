# 09 — GitHub publication and presentation checklist

**Status as of 2026-11-05: Automated technical release checks passed.** The reviewed workbook is committed. Keep the repository private until the owner completes a manual content/history review and explicitly approves public release. See [portfolio audit](15-portfolio-quality-audit.md) and [workbook provenance](17-workbook-provenance.md).

## Additional checks for versions 1.2 and 1.3

- Read [Phase 2](../phase2/README.md) and [Phase 3](../phase3/README.md); explain why the simulated payroll decision changes from HOLD to CONDITIONAL_SIMULATED and back to HOLD.
- Confirm the reviewed **v1.3 workbook** contains a clearly labelled historical dashboard and the Phase Comparison / Risk Evolution worksheets.
- Run `python scripts/validate_phase2.py` and `python scripts/validate_phase3.py` alongside existing checks.
- Verify that all new evidence, signatures, policy tests, committee decisions, future scenario dates, and supplier changes are labelled **fictional**.
- Before publishing, re-check all links and data, inspect repository history for sensitive material, and ensure the latest GitHub Actions workflow passes.
- Update CV wording to describe **independent simulated GRC portfolio work**, not actual client assessments.

## Before publishing

**Resolved:** The reviewed `Third_Party_Risk_Assessment.xlsx` is now committed to GitHub. `Vendors!F3` is HOLD and the Phase Comparison / Risk Evolution sheets are present. Run `python scripts/audit_publication.py --strict` again before publication and obtain owner approval.

1. Read `README.md` and the management report; be able to explain every risk score and every HOLD decision.
2. Confirm all organizations and artefacts in the repository are labelled **fictional/synthetic**.
3. Do not add confidential customer information, actual vendor responses, passwords, API keys, regulated personal data, real contracts or employee details.
4. Run `python scripts/validate_project.py` and `python -m unittest discover -s tests -v` from the project root.
5. Review `data/calibration_log.csv` and `docs/08-evidence-calibration.md`. The correction demonstrates professional judgment and traceability, not a flaw to conceal.
6. Confirm the workbook dashboard matches the source CSV risk register. The CSVs are the case-study's authoritative data for automated checks.

## Suggested public repository setup

- Repository: `third-party-security-risk-assessment`
- Description: `Simulated supplier due-diligence case study for an EU financial-services organisation: NIST CSF 2.0, evidence assessment, risk register, treatment and DORA/GDPR contract considerations.`
- Include README, all `data/` CSVs, the reviewed workbook, `docs/`, `templates/`, example `evidence/`, `scripts/`, `tests/` and `.github/workflows/validate.yml`.
- Add repository topics such as `cybersecurity`, `grc`, `third-party-risk`, `risk-assessment`, `nist-csf`, `dora`, `gdpr`.
- Leave the project public only after you have inspected it and approved publication. An open-source license is a separate choice; no license is granted by default.

## Demo flow (3–5 minutes)

For an up-to-date walkthrough use [the v1.3 interview guide](16-interview-preparation.md). The original steps below describe **only the initial v1.1 baseline**, not the full three-phase case study.

1. Explain the fictional company, suppliers and why cloud hosting is Tier 1.
2. Show the 24-question due-diligence template and the synthetic evidence register.
3. Open R-001 in Risk Register: 4×5=20 Critical before and after unverified claims.
4. Open Calibration Log: demonstrate why the earlier 10/25 residual was invalidated and what evidence would permit a justified rescore.
5. Show remediation tracker ACT-001 and Legal's processor agreement gate for PAY-001.
6. Open the initial management report: explain why all three **baseline** supplier decisions were HOLD.
7. Open the Phase 2 reassessment and Phase 3 decision history: explain simulated conditional payroll acceptance and its subsequent withdrawal.

## Accurate CV/interview description

> Independent Third-Party Security Risk Assessment (simulated case study): built a NIST CSF 2.0-aligned supplier due-diligence process for three fictional ICT providers, documented 24 security questions and 72 synthetic responses, assessed six risks and remediation actions, and produced evidence-calibrated recommendations and GDPR/DORA contractual considerations.

**Do not describe this as paid work, an accredited ISO audit, a real vendor audit, or a certification.**
