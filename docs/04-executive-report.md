# 04 — Executive assessment report

**To:** Fictional AFS Head of Information Security / Procurement / Legal  
**From:** Independent assessor (simulated exercise)  
**Date:** 5 November 2026  
**Subject:** Initial third-party technology vendor due diligence

> **This is a fictional teaching exercise. All provider statements and evidence are synthetic. No external assurance has been obtained.**

## Executive decision

**Hold onboarding of all three suppliers** pending acceptable evidence and appropriate approval. Their security controls are claimed but unverified, so none received numerical risk-reduction credit. Payroll additionally lacks a completed processor agreement. Procurement must not proceed with live personal-data processing or execute incomplete contractual arrangements on this basis.

| Supplier | Tier | Highest inherent | Highest residual | Decision | Principal issue |
|---|---|---|---|---|---|
| Atlas Cloud Hosting | 1 — Critical | 20 Critical | 20 Critical | Hold | Unverified privileged MFA; resilience evidence gap |
| Helios Payroll SaaS | 2 — High | 12 High | 12 High | Hold; legal gate | No validated control assurance; incomplete processor terms |
| Northstar Support Platform | 2 — High | 16 High | 16 High | Hold | Unverified access controls and incident notice |

## Findings

**Finding 1 — Cloud privileged access (R-001).** Administration compromise could affect a critical business function. A fictional MFA summary asserts partial deployment, but provides no validated enforcement or coverage; likelihood remains 4 and impact 5. **Request privileged access policy, enforcement export, and independent validation.** Owner: Cloud service owner; action ACT-001.

**Finding 2 — Cloud recovery (R-002).** The vendor claims tested backup restoration but the recovery time objective evidence is too broad for the assumed critical workload. Require AFS-specific recovery exercise and exit plan. Owner: Business continuity lead; ACT-002.

**Finding 3 — Payroll personal data (R-003).** Core security controls are merely asserted, while controller–processor terms, subprocessors and data returns are incomplete. **Block live employee-data processing pending Legal/DPO approval of the DPA.** Owner: Legal/DPO; ACT-003.

**Finding 4 — Payroll availability (R-004).** A manual contingency exists; require a documented payroll cutover and export test. Owner: HR operations; ACT-004.

**Finding 5 — Support access control (R-005).** Broad ticket visibility and missing periodic entitlement review may expose client data. Limit roles and demonstrate quarterly reviews. Owner: Support operations; ACT-005.

**Finding 6 — Support incident notification (R-006).** Contract does not specify a usable supplier-to-AFS incident escalation commitment. Agree triggers, contacts, notification timeline and evidence-sharing. Owner: Legal/Security; ACT-006.

## Next-step priorities

1. **Immediate / pre-onboarding:** Resolve CLOUD-001 access assurance and critical-service contracting; sign PAY-001 DPA before any real personal-data processing; keep SUP-001 on hold pending RBAC and incident terms.
2. **Within 30 days (scenario only):** Receive requested proof, rerate findings, check Legal/DPO sign-off and update procurement decisions.
3. **Within 60–90 days (scenario only):** Validate recovery tests, vendor monitoring commitments and exit planning.

## Limitations

Risk and control judgments depend on invented facts and low assurance. No unverified controls have been credited in the residual scores. Numbers are ordinal prioritization tools, not empirical prediction. No supplier can claim compliance based on this report. Legal obligations depend on actual regulated-entity scope, processing roles, criticality and relevant contract terms.
