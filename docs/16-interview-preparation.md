# 16 — Interview preparation: Third-Party Security Risk Assessment

**Audience:** Graduate / early-career Information Security Officer applicants. This is an **independent, fully fictional portfolio exercise**, not professional supplier-audit experience.

## 60-second explanation

> I built a simulated third-party security risk assessment for a fictional EU financial-services firm. I assessed three ICT suppliers against a 24-question security questionnaire, documented the quality and limits of supplier evidence, and applied a consistent 5-by-5 likelihood-and-impact model across six risks. I also modeled follow-up verification and a later supplier change to show how ongoing monitoring can change onboarding decisions. The project includes risk registers, remediation actions, contract checklists, executive reports and automated checks. It helped me practise NIST CSF 2.0 supply-chain risk management and the relevant GDPR and DORA considerations. No actual vendor was audited.

## Suggested 3–5 minute walkthrough

1. **Business context (30 seconds):** A fictional EU-regulated financial firm depends on cloud hosting, payroll, and support SaaS. Explain why cloud is Tier 1 and the others Tier 2.
2. **Method (45 seconds):** Demonstrate the questionnaire and evidence register. Explain that vendor statements, scoped technical records, and signed legal agreements are not equivalent.
3. **Initial review (45 seconds):** Show R-001's 4×5 = **20 Critical**. The first draft over-credited a partial MFA claim; the recalibration removed unsupported mitigation.
4. **Follow-up (60 seconds):** Show synthetic P2-E01 and the **hypothetical** R-001 reduction to 2×5 = **10 High**. One useful control does not clear cloud's other High risk or its contract gates.
5. **Approval example (45 seconds):** Payroll risks are **8 Medium** and **6 Medium** in the modeled Phase 2. Legal and privacy contract checks remain independent of scoring; a fictional committee records only a conditional scenario decision.
6. **Monitoring and escalation (45 seconds):** Fictional P3-E01 proposes a new payroll subprocessor outside the previously reviewed scope. R-003 rises from 8 to **12 High**, the gate reopens, and payroll goes back to HOLD.
7. **Limits (15 seconds):** No live suppliers, actual client records, real legal review or production systems were involved.

## Questions and model answers

**Q1. What are inherent and residual risk?**  
Inherent risk is the exposure assessed without credited existing controls; residual risk remains after effective, sufficiently evidenced controls. A planned control or a vendor's unsupported claim should not automatically lower today's score.

**Q2. Why did you initially keep R-001 at 20, then later lower it to 10?**  
The initial evidence claimed MFA without demonstrating coverage or enforcement, so the baseline held at 4×5. A later **invented scenario test** included 12/12 privileged human identities, sampled challenges and no policy exclusions; I used that to model likelihood falling from 4 to 2 while impact stayed at 5. This is an ordinal judgment, not a measured attack probability.

**Q3. Why didn't cloud get approved after that?**  
Even after the one improvement, R-001 remained **High (10)**, R-002 stayed **High (15)** because a limited restore didn't cover the critical service, and relevant contractual/exit provisions were still unresolved. Under the exercise's risk appetite, these independently block approval.

**Q4. What evidence would you request from a vendor?**  
Scoped and dated security policies, configuration exports or controlled demonstrations, independent assurance reports with coverage and exceptions, recovery test outcomes, access reviews, subcontractor details, incident notice procedures and relevant executed contracts. I would validate scope, freshness, exclusions and corroboration rather than count a “Yes” answer as proof.

**Q5. What did the payroll decision demonstrate?**  
A simulated JIT access test reduced R-003 *likelihood* (3→2); a timed fallback drill reduced R-004 *impact* (4→2). The fictional legal/processor contract review was an independent gate, not part of the numerical control score. A conditional decision was only role-play, not real authority.

**Q6. Why did payroll revert to HOLD?**  
The proposed new subprocessor was outside the access evidence originally reviewed. I increased the *modeled* R-003 likelihood from 2 to 3, restoring **12 High**, and reopened privacy/contract review. The fictional event was a proposed change, not evidence that a transfer or breach occurred.

**Q7. How do GDPR and DORA differ in this project?**  
GDPR Article 28 concerns controller–processor arrangements when personal data are processed on the controller's behalf. DORA governs ICT risk management and third-party arrangements for in-scope financial entities; Article 30 includes general ICT contract provisions and additional terms for services supporting critical or important functions. Applicability must be determined per entity, service and processing activity. The project is not legal compliance certification.

**Q8. Why use NIST CSF 2.0 rather than claim ISO 27001 certification?**  
NIST CSF 2.0, particularly its GV.SC supply-chain category, structures intake, supplier prioritization, due diligence, risk response, monitoring, incident coordination and exit. The project draws conceptual connections with ISO/IEC 27001:2022 but has not conducted an accredited certification audit or demonstrated an operating ISMS.

**Q9. How would you handle a supplier refusing to supply sensitive evidence?**  
Request suitable alternatives: redacted extracts, a scoped independent assurance report, controlled read-only demonstrations or third-party attestations, and document residual uncertainty. Escalate to risk owners and hold onboarding if mandatory gates cannot be met. Never demand secrets or unnecessary personal data.

**Q10. What would you improve in a real organization?**  
Calibrate impact against documented business thresholds, add actual regulatory scoping and contract review, obtain independent control evidence, set accountable risk-acceptance authority, monitor concentration and subcontractor dependencies, and test the exit plan with business owners.

## Five facts to memorise

| Risk | Baseline | Phase 2 | Phase 3 |
| --- | ---: | ---: | ---: |
| R-001 cloud privileged takeover | 20 Critical | 10 High | 10 High |
| R-002 cloud outage | 15 High | 15 High | 15 High |
| R-003 payroll subprocessor access | 12 High | 8 Medium | 12 High |
| R-004 payroll outage | 12 High | 6 Medium | 6 Medium |
| R-005 support overprivilege | 16 High | 16 High | 16 High |
| R-006 support notification failure | 12 High | 12 High | 12 High |

**Latest modeled outcome:** HOLD all three suppliers. **The workbook in the repository remains v1.1 until the corrected version is uploaded.**

## Credible CV entry (only after actual review and publication)

**Independent Third-Party Security Risk Assessment (Simulated)** — Designed a NIST CSF 2.0-aligned assessment of three fictitious ICT suppliers; produced a 24-question due-diligence questionnaire, evidence-quality register, six-scenario risk model, treatment plans and executive reports; demonstrated scenario-based reassessment, supplier-change monitoring and GDPR/DORA contractual considerations.

**Avoid:** “audited financial-services vendors,” “verified supplier controls,” “obtained DORA compliance,” “worked as a security officer,” or implying that fictional evidence is genuine.
