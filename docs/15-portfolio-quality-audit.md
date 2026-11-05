# 15 — Portfolio quality audit (pre-publication)

**Review date:** 2026-11-05. **Repository remains private.** This review evaluates an independent fictional training exercise, not real vendor assurance.

## Scope reviewed
- Baseline v1.1: three suppliers, 24 questions, 72 synthetic responses, six risks, six remediation actions, evidence calibration.
- Phase 2 v1.2: seven fictional exhibits, six reassessments, three decision gates.
- Phase 3 v1.3: supplier-change notice, six current risk scores, decision history, event-driven HOLD.
- Workbook: historical v1.1 dashboard and newly prepared cross-phase v1.3 review workbook (separate artifact).
- Documentation and automated validation scripts.

## Findings and actions

| ID | Severity | Finding | Resolution / outstanding step |
| --- | --- | --- | --- |
| QA-01 | **Publication blocker** | The original repository workbook's `Vendors!F3` still reads `CONDITIONAL - NO LIVE DATA`. v1.1 CSV and dashboard correctly say HOLD. | A corrected and expanded **v1.3 workbook** has been generated locally. **Replace the outdated binary file in GitHub before publication.** Do not mistake the repository's current workbook for the reviewed file. |
| QA-02 | Medium | Original interview notes describe R-001's initial 20/25 risk without explaining its later 10/25 follow-up. | See `docs/16-interview-preparation.md`; use phase-specific answers. |
| QA-03 | Medium | Original publication demo focuses only on all-three-HOLD baseline and omits Phase 2 and 3. | Updated publication checklist and cross-phase demonstration guide. |
| QA-04 | Low | One-file workbook snapshot can be mistaken for current multi-phase data. | README and `docs/17-workbook-provenance.md` explicitly distinguish the historical original from the reviewed cross-phase workbook. |
| QA-05 | Context limitation | Every control claim, technical check, simulated approval, legal gate, and supplier change is invented. | All are labelled synthetic. Do **not** describe these as genuine supplier audits, external verification, signed contracts, certification, or professional employment. |

## Verified data outcomes

| Supplier | Baseline maximum | Phase 2 maximum | Phase 3 maximum | Latest scenario decision |
| --- | ---: | ---: | ---: | --- |
| CLOUD-001 | 20 Critical | 15 High | 15 High | HOLD |
| PAY-001 | 12 High | 8 Medium | 12 High | HOLD |
| SUP-001 | 16 High | 16 High | 16 High | HOLD |

Six individual risk records persist across the phases. **R-001** moves 20 → 10 → 10, while **R-003** moves 12 → 8 → 12. A conditional payroll decision occurs **only in the fictional Phase 2** and is withdrawn in fictional Phase 3.

## Publication gate — not yet cleared

- [x] Private repository exists; scripts and GitHub Actions exercise data consistency.
- [x] Synthetic case and legal assumptions are documented.
- [x] Initial, follow-up, and monitoring decisions are kept in distinct files.
- [x] Interview guide includes limitations and phase-specific results.
- [ ] **Replace the outdated repository workbook with the reviewed cross-phase v1.3 workbook**; then verify the GitHub file and formulas.
- [ ] Manually inspect the entire public-facing repository and commit history for sensitive details or unintended content.
- [ ] Review wording and prove you can explain each assumption without using interview notes.

**Outcome:** Technically substantial for a graduate portfolio; **not yet publication-ready** because QA-01 needs the GitHub binary corrected. Do not change repository visibility until the owner explicitly approves publication.

## Primary references
- NIST CSF 2.0 GV.SC: https://csrc.nist.gov/Projects/cybersecurity-framework/filters
- EU DORA, Arts. 28–30: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- GDPR processor guidance: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en
