# 01 — Case study, governance and scope

**Scenario:** Asteria Financial Services (AFS) is a fictional EU-based investment services firm. AFS is **assumed** to be subject to DORA for teaching purposes; its actual licensing, size, functions and regulatory scope do not exist and are not being verified.

## Business assets and service dependencies

- Online client portal and internal trading support processes: availability and confidentiality matter; dependent on cloud hosting.
- Human Resources and payroll: employee identification, salaries and banking information; serviced by payroll SaaS.
- Customer support ticketing: client contact details, conversation notes, service history; serviced by support SaaS.

## In-scope suppliers

1. **CLOUD-001 — Atlas Cloud Hosting (fictional):** EU cloud application hosting and backups; assumed to support a **critical or important function** for this case.
2. **PAY-001 — Helios Payroll SaaS (fictional):** employee payroll services with personal data; NOT assumed to support a critical or important DORA function unless a separate documented criticality assessment concludes otherwise.
3. **SUP-001 — Northstar Support Platform (fictional):** support tickets involving client personal data; NOT assumed critical or important under DORA by default.

## Review objectives

- Establish a vendor inventory, service ownership, data flows, access modes, geographic dependencies and exit difficulty.
- Identify control gaps relevant to confidentiality, integrity, availability and legal/regulatory obligations.
- Obtain vendor answers **and** supporting evidence; treat a self-declaration differently from tested evidence.
- Quantify distinct risk scenarios and decide **approve / conditionally approve / hold / reject**.
- Define treatment owners, due dates, required proof and a monitoring cadence.

## Roles (fictional)

| Role | Responsibility |
|---|---|
| Information Security Officer (assessor) | Organize due diligence; challenge evidence; propose risk response |
| Service owner | Assess business impact, data flows, requirements and alternatives |
| Information Security Manager | Review high-risk acceptance; escalate critical risk |
| Procurement | Ensure conditions are part of supplier negotiation and onboarding |
| Legal / Data Protection Officer | Review GDPR processor clauses, DORA applicability and contract terms |
| Risk committee | Accept exceptions above stated tolerance; authorize hold/rejection |

## Simple illustrative risk appetite

- **Critical residual (17–25):** no onboarding; escalate to risk committee.
- **High residual (10–16):** default **hold**, unless formal conditional approval documents interim safeguards, a due date, and accountable senior risk acceptance. For this exercise, none of the high-residual suppliers receives unconditional approval.
- **Medium residual (5–9):** possible conditional approval with tracked remediation and required contract terms.
- **Low residual (1–4):** standard approval only if all mandatory legal / contractual gates are met.
- **Mandatory contract gate:** GDPR processor DPA (if required) and applicable DORA contractual provisions must be resolved before processing/contract execution, regardless of numerical scores.

## Exclusions

No penetration testing of any supplier, no access to real organizations, no live data, no security certification and no legal sign-off. All evidence documents are intentionally labelled **fictional/self-reported**.
