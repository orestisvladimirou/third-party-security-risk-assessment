# Third-Party Security Risk Assessment & Vendor Due Diligence

**Independent cybersecurity portfolio exercise · Version 1.3 · 5 November 2026**

> **SIMULATED CASE STUDY.** Asteria Financial Services (AFS), all supplier names, evidence, incidents, control claims, decisions and risk ratings in this repository are fictional. This is **not** an audit of any real entity, an ISO/IEC 27001 certification, regulatory legal advice, or a representation of paid professional experience.

## Publication status: private, technical checks passed

The repository now contains the **reviewed v1.3 Excel workbook**, replacing the obsolete payroll decision and adding Phase Comparison and Risk Evolution sheets. Automated technical release checks passed. **Keep the repository private until the owner completes a manual review and expressly approves publication.** Read the [portfolio quality audit](docs/15-portfolio-quality-audit.md), [workbook provenance](docs/17-workbook-provenance.md), and [updated interview preparation](docs/16-interview-preparation.md).

## Phase 2 follow-up

[Read the simulated evidence verification and reassessment](phase2/README.md). This follow-up has seven fictional exhibits, six revised risk scores, gated vendor decisions, and automated integrity checks. The Excel workbook retains the v1.1 baseline dashboard **and now includes cross-phase comparison sheets**; Phase 2 source data are in `phase2/data/`. No actual supplier or personal data is involved.

## Phase 3 monitoring scenario

[Review the ongoing supplier monitoring and event-driven reassessment](phase3/README.md). This separate fictional scenario records a proposed payroll subprocessor change, a risk increase, and the withdrawal of the earlier simulation-only conditional decision. All three suppliers are on HOLD in the modeled Phase 3 state.

## Business problem

A fictional EU financial-services firm needs a consistent process for approving, monitoring and exiting third-party technology providers. The assignment is to review three proposed vendors before contracting, distinguish control assertions from reliable evidence, quantify cyber risks, and recommend defensible onboarding decisions.

## Portfolio outcomes

- Scope and tier **three fictional service providers** by data sensitivity, operational dependency and substitutability.
- Design a **24-question due-diligence questionnaire** spanning security, privacy, continuity and governance.
- Evaluate **72 fictional supplier responses** and track evidence quality / gaps.
- Document **six risk scenarios** with inherent vs residual likelihood, impact, rationale, owners and remediation, including a recorded evidence-calibration correction.
- Produce a senior-management summary and legal/security contract checklist.
- Map the workflow to **NIST CSF 2.0 GV.SC**, with conceptual links to **ISO/IEC 27001:2022**, **GDPR Article 28**, and **DORA Articles 28–30**.

## Read in order

1. [Case study and boundaries](docs/01-case-study.md)
2. [Risk methodology](docs/02-risk-methodology.md)
3. [Vendor review workflow](docs/03-assessment-workflow.md)
4. [Executive decision report](docs/04-executive-report.md)
5. [Contract and privacy checklist](docs/05-contract-checklist.md)
6. [Standards crosswalk and sources](docs/06-framework-crosswalk.md)
7. [How to defend the assessment in an interview](docs/07-interview-notes.md)
8. [Evidence calibration and revised approval rationale](docs/08-evidence-calibration.md)
9. [GitHub publication checklist](docs/09-publication-checklist.md)
10. [Portfolio quality audit and resolved workbook issue](docs/15-portfolio-quality-audit.md)
11. [Three-phase interview walkthrough](docs/16-interview-preparation.md)
12. [Workbook provenance and data versioning](docs/17-workbook-provenance.md)
13. [Independent mock interview practice](docs/18-mock-interview.md)

## Data and evidence

| File | Purpose |
| --- | --- |
| `data/vendors.csv` | Vendor inventory, criticality and assumed data access |
| `data/questionnaire.csv` | Reusable due-diligence questions and evidence requirements |
| `data/vendor_responses.csv` | 72 synthetic answers with confidence and evidence references |
| `data/evidence_register.csv` | Evidence log distinguishing synthetic claims from evidence gaps |
| `data/risk_register.csv` | Risk assessment, severity, residual ratings, actions and treatment |
| `data/calibration_log.csv` | Revision log showing original optimistic scores, conservative recalibration and evidence required |
| `data/remediation_tracker.csv` | Named owners, due dates and acceptance criteria |
| `evidence/*.md` | Sample **synthetic** vendor-provided evidence artefacts |
| `templates/*.md` | Reusable forms for a new vendor/assessment |

## Run quality checks

Requires Python 3.10+; no external dependencies.

```bash
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python scripts/audit_publication.py
python -m unittest discover -s tests -v
```

The validators recompute scores, check risk bands, verify cross-phase references and decision gates, and flag publication issues. Run `python scripts/audit_publication.py --strict` as the **final release gate**: it must pass before making the repository public. You can edit the scenario data, rerun the checks, and discuss why the decision changes.

## Assumptions and interpretation

AFS is **assumed for this exercise** to be an EU financial entity within DORA scope. Not every third-party function is automatically a DORA **critical or important function**. In this case cloud hosting is **assumed critical**; the others are assessed separately. The GDPR controller/processor relationship is evaluated per processing activity, not inferred merely from the supplier being a SaaS provider. Contract checklists identify subjects for legal review; they are **not legal findings**.

Risk scores are **scenario-based judgments**, not statistical frequencies or assurance of compliance. In version 1.1 unverified control claims are not counted as effective controls, so residual scores remain at inherent levels pending evidence. **All three initial (v1.1) supplier decisions are HOLD.** See the calibration log for what changed from version 1.0.

## Authoring and GitHub presentation

Suggested repository name: `third-party-security-risk-assessment`. A GitHub Actions workflow (`.github/workflows/validate.yml`) runs the same built-in Python data checks on pushes and pull requests. This project intentionally does not rely on any other personal projects. Publish only this fictional case-study data; do not upload real supplier questionnaires, client data, secrets, internal contracts or staff information.

For the complete three-stage interview explanation, use [`docs/16-interview-preparation.md`](docs/16-interview-preparation.md). The older [`docs/07-interview-notes.md`](docs/07-interview-notes.md) focuses on the baseline.
