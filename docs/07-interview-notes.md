# 07 — Explaining the portfolio project in an interview

**Note for v1.3:** This page originally described the initial v1.1 baseline. For the complete three-phase interview narrative and current model outcomes, use [the updated interview preparation guide](16-interview-preparation.md). The latest simulated phase is Phase 3: all three suppliers HOLD.

## Honest elevator pitch

> I built a simulated third-party security assessment for a fictional EU financial-services firm. I designed the supplier intake and due-diligence process, evaluated fictional security evidence, developed a 5×5 risk model with explicit assumptions, created a remediation tracker, and produced management and contract-review recommendations. I mapped the workflow to NIST CSF 2.0 and considered where GDPR Article 28 and DORA Articles 28–30 may apply. This was independent study, not a professional audit.

## Questions to practise

**Q: What is the difference between inherent and residual risk?**  
A: Inherent is exposure without existing controls; residual is the remaining exposure after *effective, sufficiently evidenced* existing controls. Our first draft prematurely reduced R-001 from 20 Critical to 10 High based on an unverified MFA claim. I corrected it: residual remains 20 Critical until evidence is evaluated. If full coverage were later verified, 10 High could become a plausible **new** assessment, but is not the current **baseline** score. The fictional Phase 2 test later reassesses R-001 to **10 High**, and Phase 3 retains 10 High; see the updated guide.

**Q: Why didn't you just approve a supplier with an ISO certificate?**  
A: Certificate scope, currency, applicable services, shared responsibility and control implementation still need checking. A certificate alone cannot prove a particular service or contractual obligation is covered.

**Q: How would you handle a vendor that refuses to share evidence?**  
A: Record the gap, evaluate alternate assurance such as relevant independent reports, restrict access, apply compensating controls if justified, escalate, and hold procurement when risk appetite or mandatory gates are not met.

**Q: Does DORA apply to every supplier?**  
A: Obligations are assessed for in-scope financial entities and their ICT third-party arrangements. The severity of some provisions depends on whether the ICT service supports a critical or important function; Article 29 specifically addresses concentration for those dependencies.

**Q: When does GDPR Article 28 apply?**  
A: When a vendor processes personal data on the controller's behalf. Document the processing operation and roles; then assess whether the processor agreement has the mandated subjects and obligations.

**Q: Why are all residual scores in the initial baseline the same as inherent?**  
A: In this teaching dataset, every relevant supporting claim is synthetic and unverified. I chose a conservative rule of no numeric credit until effective controls can be validated. The `calibration_log.csv` records the correction, and the verification exercise shows how scores may change with evidence.

**Q: What would you do with a high residual risk?**  
A: Default to hold; propose mitigation with accountable owner, time limit and evidence acceptance criteria. If the organization's policy allows an exception, obtain an authorized decision rather than personally waiving it.

## Limitations to acknowledge

- Every vendor, evidence artefact and score is fictional and was not independently validated.
- Risk likelihood is judgmental; a more mature program would calibrate it with incident history and organizational loss thresholds.
- The questionnaires are illustrative; depth should change for Tier 1 suppliers and highly sensitive data.
- The legal checklist does not substitute for counsel; cross-border transfer analysis and DORA technical standards would need further treatment.

## Future iterations

1. Add a formally versioned supplier security policy, sign-off matrix and exception register.
2. Expand the high-tier questionnaire and score evidence quality explicitly.
3. Introduce automated due-date reminders, monthly KPI reporting and a supplier reassessment schedule.
4. Add a concentration risk assessment comparing two alternative hosting providers and an exit simulation.

**Example CV wording (only after finishing and verifying):**

**Third-Party Security Risk Assessment | Independent Case Study** — Designed a fictional supplier due-diligence process aligned with NIST CSF 2.0; evaluated three simulated technology suppliers; built inherent/residual risk registers, remediation tracking and management recommendations; documented conditional GDPR/DORA contract considerations. **Do not imply employer participation, formal audit work, certification or direct supplier testing.**
