# 08 — Evidence calibration: what changed and why

> This record documents a **fictional** assessor's quality-control correction, not a live vendor finding or professional audit.

## Issue discovered in v1.0

The first draft reduced several residual risk scores based on **unverified vendor assertions**, including R-001 privileged admin MFA. Merely having an unverified self-attestation is not the same as demonstrating a control's existence, completeness or efficacy. The original reductions overstated confidence.

## Corrective policy for v1.1

1. Distinguish **claimed control**, **evidence received**, **scope checked**, and **control effectiveness validated**.
2. No numerical risk reduction is given for a claim rated **Low** evidence confidence unless explicit, separately approved assumptions justify it. This fictional case uses **no exceptions**.
3. An absence of evidence **does not prove a control is absent**, but it prevents the assessor from asserting control effectiveness and can stop onboarding.
4. Re-score only when new credible evidence arrives; record the old rating, new rating, rationale, review owner, and impact of contractual approval gates.
5. Treat GDPR processing and DORA contract conditions as **independent gates**, not matters that can always be offset by a lower numerical risk score.

The six risk corrections, their original scores and required verification steps are recorded in [`data/calibration_log.csv`](../data/calibration_log.csv). All suppliers remain **HOLD** on this conservative evidence basis.

## Deep dive: R-001 privileged cloud administrator compromise

**Risk event:** an attacker gains control of a privileged cloud identity and can impact a critical client-facing function.

- **Inherent:** Likelihood 4 (likely given privileged exposure and no credited controls), Impact 5 (severe disruption/compromise possible) = **20, Critical**.
- **Submitted fictional evidence:** `SIM-E01`, a short narrative asserting MFA for the primary administrator group. It omits policy enforcement exports, break-glass account controls, service account handling, exception lists, and complete identity coverage.
- **Current residual:** no independently supported effective controls; **4 × 5 = 20, Critical**. Onboarding: **HOLD**.
- **Action:** ACT-001 requests full inventory, enforced phishing-resistant admin MFA, reviewed exceptions and independent sample validation. Record the outcome, including failures.

### A hypothetical follow-up, **not** the current finding

Suppose a subsequent, credible technical review demonstrates MFA enforcement for **all** relevant privileged human accounts, tested break-glass protections and no uncontrolled exceptions. The assessor may plausibly reconsider the attack likelihood from 4 to **2** while impact stays **5**; **2 × 5 = 10, High**. This is a **teaching scenario**, not an automatically approved numerical effect or assertion of real evidence.

Even at 10 High, high-risk acceptance would need authorized governance action, and critical-service contract/recovery gates remain in scope. A security control may also change impact or not change likelihood by that much; scores are expert judgment requiring written justification.

## Interview explanation

> I caught an optimistic assumption during my quality review: several 'residual' scores credited unverified vendor claims. I changed the methodology so claims are logged but not automatically scored as effective controls. For the cloud admin compromise scenario, the score returned to 20/25 Critical and the vendor stays on hold. I documented what technical evidence would be required to justify a later re-rating and retained an audit trail of the correction.

## Basis and references

- NIST SP 1305 (CSF 2.0 C-SCRM guide): https://csrc.nist.gov/pubs/sp/1305/final
- NIST CSF 2.0 GV.SC-07 (evaluate supplier evidence and monitor risk): https://csrc.nist.gov/Projects/cybersecurity-framework/filters
- NIST SP 1326 (due-diligence quick start; final July 2026): https://csrc.nist.gov/pubs/sp/1326/final
- DORA Articles 28–30 (applicability conditioned on entity and services): https://eur-lex.europa.eu/eli/reg/2022/2554/oj

This is **our conservative scoring policy**, not a quoted universal rule imposed by NIST or DORA.
