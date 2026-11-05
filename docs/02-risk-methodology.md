# 02 — Risk methodology and calibration

## Vendor criticality / inherent exposure

Vendor tiers are **not risk scores**. Tiering determines scrutiny and review cadence:

- **Tier 1 / Critical:** directly supports assumed critical business function; loss could stop customer operations; difficult to replace. Review at least annually and after material change.
- **Tier 2 / High:** handles regulated, financial, employee or customer personal data, or significant operational dependency. Review at least annually or following material events.
- **Tier 3 / Standard:** limited sensitive data and readily replaceable. Review every 24 months or on material change.

For AFS, cloud hosting is Tier 1; payroll and support are Tier 2. Final tier is a business judgment supported by `vendors.csv`, not a vendor certification.

## 5-point likelihood scale

| Score | Qualitative guidance |
|---:|---|
| 1 | Rare: strong preventive controls and limited exposure; no known credible pathway in scenario |
| 2 | Unlikely: exposure exists but multiple effective controls limit occurrence |
| 3 | Possible: plausible pathway, partial controls or uncertain effectiveness |
| 4 | Likely: frequent exposure, significant gaps or weakly controlled pathway |
| 5 | Almost certain: ongoing exposure with little/no credible preventive control |

Likelihood is **not** a measured incident probability.

## 5-point impact scale

| Score | Qualitative guidance |
|---:|---|
| 1 | Negligible: small reversible disruption, no meaningful sensitive data impact |
| 2 | Minor: bounded local impact, standard recovery |
| 3 | Moderate: multi-team disruption or limited sensitive-data exposure |
| 4 | Major: material personal-data impact, prolonged service disruption or serious business harm |
| 5 | Severe: sustained disruption of a critical function or extensive compromise with major harm |

## Calculation

`Risk score = Likelihood (1–5) × Impact (1–5)`

| Score | Band |
|---:|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

**Inherent risk** is assessed without the benefit of the existing vendor control set. **Residual risk** is assessed after considering demonstrably effective existing controls. An unverified supplier statement is recorded but is **not credited as an effective control** in this conservative simulation. Planned controls also **do not reduce today's residual score**. Scores are recorded with narrative rationale; the product is a prioritization aid, not a precise or purely mathematical measure.

### Worked example: R-001 (cloud privileged account compromise)

- Inherent **Likelihood 4**, **Impact 5** → `4 × 5 = 20`, **Critical**.
- Synthetic evidence SIM-E01 claims some cloud administrators have MFA, but neither enforcement nor all privileged identities are validated. We record the claim without treating it as effective control evidence.
- Current residual **4 × 5 = 20, Critical**, unchanged from inherent risk. The decision is **Hold**.
- **Hypothetical only:** if independent checks demonstrated complete phishing-resistant privileged MFA, a separate reassessment might justify likelihood **2** and unchanged impact **5**, yielding **10, High**. A reduction is neither guaranteed nor pre-approved.
- ACT-001 defines verification steps and accountable ownership. Only evidence-supported existing controls may justify a revised risk decision.

## Evidence and uncertainty

Record one of: `Synthetic document` (an authored, fictional artefact), `Synthetic self-attestation` (unverified vendor claim), or `Missing` (no material supplied). The fields `evidence_id` and `confidence` prevent an optimistic score from being read as validated fact. An answer of `Yes` is not sufficient by itself. In this dataset, every scored risk has **Low evidence confidence**, so none earns a numerical reduction. This is an explicit conservative assessment convention, not a universal industry requirement. See `data/calibration_log.csv` for the v1-to-v1.1 correction.

## Exception governance

Only a named accountable owner and risk committee may accept high/critical risk. Acceptance must include justification, expiry, compensating controls and review date; absence of approval means `Hold`. No simulated signatures imply actual approval. Treat statutory contract requirements as gates independent of the score.
