# 05 — Third-party security, privacy and resilience contract checklist

**For fictional review only.** This is a negotiation and evidence checklist, **not legal advice** or a complete DORA/GDPR compliance template. Legal/DPO must interpret applicability and confirm terms before execution.

| Topic | Contract / evidence question | Conditional basis |
|---|---|---|
| Defined services | Are exact ICT functions, scope, service owners and SLAs written down? | DORA Art. 30 where applicable |
| Location and transfers | Are service locations, storage/processing countries and advance-change notices specified? | DORA Art. 30; GDPR transfer rules as applicable |
| Security obligations | Are access control, encryption, vulnerability management and independent assurance obligations recorded? | NIST GV.SC-05; applicable DORA terms |
| Incident collaboration | Are report triggers, notification contacts, cooperation, evidence preservation and assistance commitments specified? | DORA Art. 30; GDPR processor duties as applicable |
| Continuity and exit | Are backup/restore, continuity, recovery, exit, data retrieval and termination responsibilities documented? | DORA Art. 30; NIST GV.SC-10 |
| Subcontracting | Are critical-service subcontracting conditions, changes and dependency visibility addressed? | DORA Art. 30; GDPR Art. 28 for processors |
| Audit / inspection rights | Are suitable monitoring, assurance and inspection rights in place where legally needed? | DORA Art. 30, with enhanced terms for critical/important functions |
| Supplier monitoring | Are KPIs, change notification, annual or event-triggered re-review responsibilities included? | NIST GV.SC-07 / 09; ISO supplier controls concepts |
| Processor relationship | Has controller vs processor status been determined for each personal-data activity? | GDPR Art. 28 only for processor services |
| Processing purpose | Does any processor agreement state subject matter, duration, nature/purpose, data categories and controller rights? | GDPR Art. 28(3) |
| Documented instructions | Does processor agree to act on controller's documented instructions, subject to lawful exceptions? | GDPR Art. 28(3) |
| Confidentiality and security | Are appropriate processor confidentiality/security measures and assistance duties included? | GDPR Art. 28(3) |
| Subprocessors | Does processor require specific/general prior authorization and notification of changes? | GDPR Art. 28(2)-(4) |
| End of service | Are data return/deletion, backups, export format and proof documented? | GDPR Art. 28(3); DORA Art. 30 as applicable |
| Concentration | Could the critical function become dependent on hard-to-replace ICT suppliers? What alternatives exist? | DORA Arts. 28–29, for in-scope entities/functions |
| Critical-function extras | Are stronger quantitative SLAs, resilience tests and enhanced inspection rights addressed where required? | DORA Art. 30(3), **only if critical/important** |

## Specific decisions from the example

- **CLOUD-001:** Contract checklist is open for service locations, critical-function SLAs, incident cooperation, recovery testing and exit rights. No executed contract exists in the case study.
- **PAY-001:** GDPR processor agreement is **not complete**; do not transmit live payroll data. DORA ICT-service status and criticality must be assessed separately.
- **SUP-001:** Incident notification, subprocessor and role-specific data access provisions require negotiation; determine processor role per operation.

## Source cautions

DORA Article 28 addresses overall ICT third-party risk and pre-contract diligence; **Article 29 is specifically on concentration risk for critical or important function dependencies**, not a generic vendor-assessment mandate; Article 30 addresses contractual requirements with additional provisions for critical/important functions. GDPR Article 28 applies when the supplier acts as a **processor** of personal data on the organization's behalf. Contract reviews must not assume every SaaS provider or every vendor receives identical legal treatment.
