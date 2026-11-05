# 13 — Ongoing supplier monitoring standard (fictional)

This is a model control procedure for Asteria Financial Services, not an operating compliance program.

## Monitoring owners and cadence

- **Tier 1 / Critical cloud:** quarterly privileged access and resilience KPI review; at least annual deep assessment; retest after control or service changes.
- **Tier 2 / High payroll:** quarterly subprocessor/change and access review; at least annual full assessment; event-trigger review immediately after material supplier or processing changes.
- **Tier 2 / High support:** quarterly tracking of outstanding controls and notice terms; annual full assessment after the initial HOLD issues have been addressed.

Owners, review frequency, indicators and escalation routes are in `phase3/data/monitoring_plan.csv`.

## Measurable indicators and thresholds (case-study choices)

| Indicator | Trigger | Response |
| --- | --- | --- |
| Critical privileged human account MFA coverage | Below 100% in modeled scope | Security escalation and re-score privileged access risk |
| Critical service recovery exercise | Missed RTO/RPO or a material component excluded | Reopen resilience risk; require broader test |
| Supplier access review | Missing at quarterly checkpoint | Reopen assurance and hold expansion |
| Material subprocessor change | Any proposed new processor or location without reviewed information | Pause conditional approval and open Legal/DPO review |
| Security incident collaboration | Untested or missing contractual notification procedure | Escalate; keep contract gate open |
| Conditional decision expiry | Due or breached without reacceptance | Automatically require renewed accountable decision; do not silently extend |

These are illustrative governance thresholds, not prescribed DORA or NIST numeric requirements.

## Event workflow

1. Capture the date, source and service owner in `monitoring_events.csv`.
2. Check whether evidence invalidates a scored control, privacy analysis, contract term, geographic assumption or criticality tier.
3. Reassess the specific risk with the *same* methodology and record what stayed unchanged.
4. Reopen mandatory gates even if the risk score does not change.
5. Notify accountable risk and service owners; document HOLD, conditional acceptance, approval or rejection through authorized roles.
6. Track proof of remediation and re-review after resolution.

A proposed change does not by itself prove noncompliance or a completed international transfer. GDPR processor authorization and transfer protections require case-specific examination; DORA contractual requirements depend on the regulated entity and ICT service.

No supplier has been contacted for this exercise.
