# Phase 2 — Fictional management reassessment

**To:** Asteria Financial Services (fictional) Security / Legal / Risk Committee  
**Scenario date:** 2026-11-19, modeled for portfolio training rather than an actual engagement.

| Supplier | Baseline residual risks | Phase 2 residual risks | Fictional decision |
| --- | --- | --- | --- |
| Atlas Cloud Hosting | 20 Critical, 15 High | **10 High, 15 High** | **HOLD** |
| Helios Payroll SaaS | 12 High, 12 High | **8 Medium, 6 Medium** | **CONDITIONAL (SIMULATION ONLY)** |
| Northstar Support Platform | 16 High, 12 High | **16 High, 12 High** | **HOLD** |

## Cloud — partial progress, still blocked

P2-E01 models 12/12 human admin identities with phishing-resistant MFA and sampled challenges. R-001 likelihood falls 4→2; impact remains 5, resulting **10 High**. P2-E02 covers only a component, not the full critical service: R-002 remains **15 High**. Applicable critical-function contractual and recovery/exit gates remain unresolved; no authorized high-risk exception is assumed. **HOLD.**

## Payroll — conditions supported inside the exercise

P2-E03 models restricted, time-limited supplier access and denied unauthorized requests. R-003 becomes **2×4=8 Medium**. P2-E05 models a 116-minute recovery drill using invented data; R-004 becomes **3×2=6 Medium**.

P2-E04 supplies a **fictional contractual clearance assumption**, not a real signed GDPR processor agreement or legal opinion. For this training scenario alone, the model risk committee records conditional acceptance, with a hypothetical expiry **2026-12-20**, subject to continued access review, contingency rehearsals and change monitoring.

**This does not constitute approval to use any real supplier or employee data.** Real procurement requires actual due diligence, executed applicable agreements, and authorized sign-off.

## Support — insufficient evidence

P2-E06 is a proposed role matrix, not proof it was deployed. R-005 remains **16 High**. P2-E07 is an unsigned, vague notification draft; R-006 remains **12 High**. **HOLD** until evidence of functioning access controls and enforceable incident cooperation is provided.

## Record of decisions

The immutable baseline is `data/risk_register.csv`; Phase 2 values and rationale are in `phase2/data/reassessment.csv`. Review the evidence register, `phase2/data/action_updates.csv`, and independent legal/operational approval gates in `phase2/data/decision_gates.csv`.

This report documents a **simulated independent portfolio exercise** only, not client work, professional audit experience, formal certification, regulatory clearance or an independent assessment of actual products.
