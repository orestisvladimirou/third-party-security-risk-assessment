#!/usr/bin/env python3
"""Standard-library consistency check for this fictional portfolio project."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(filename):
    with (ROOT/'data'/filename).open(newline='',encoding='utf-8') as fp:
        return list(csv.DictReader(fp))
def band(n):
    return 'Low' if n<=4 else 'Medium' if n<=9 else 'High' if n<=16 else 'Critical'
def validate():
    vendors=load('vendors.csv'); questions=load('questionnaire.csv'); responses=load('vendor_responses.csv')
    evidence=load('evidence_register.csv'); risks=load('risk_register.csv'); actions=load('remediation_tracker.csv')
    calibration=load('calibration_log.csv')
    v={x['vendor_id'] for x in vendors}; q={x['question_id'] for x in questions}
    e={x['evidence_id'] for x in evidence}; a={x['action_id'] for x in actions}; r={x['risk_id'] for x in risks}
    assert len(v)==len(vendors)==3, 'Supplier IDs must be distinct'
    assert len(q)==len(questions)==24, 'Question IDs must be distinct'
    assert len(responses)==len(v)*len(q), 'Expected one answer per supplier per question'
    assert len({(x['vendor_id'],x['question_id']) for x in responses})==len(responses), 'Duplicate answers'
    assert len(e)==len(evidence), 'Duplicate evidence IDs'
    assert len(a)==len(actions), 'Duplicate action IDs'
    assert len(r)==len(risks)==6, 'Duplicate or missing risks'
    assert {x['risk_id'] for x in calibration}==r, 'Calibration entries must cover each risk exactly once'
    assert len(calibration)==len(risks), 'Duplicate calibration entry'
    for row in responses:
        assert row['vendor_id'] in v and row['question_id'] in q
        assert row['answer'] in ['Yes','Partial','No','Unknown']
        if row['evidence_id']: assert row['evidence_id'] in e
    for row in evidence:
        assert row['vendor_id'] in v
        if row['file']: assert (ROOT/row['file']).is_file(), f"Missing synthetic evidence file {row['file']}"
        if row['evidence_type']=='Missing': assert not row['file']
    for row in risks:
        assert row['vendor_id'] in v and row['action_id'] in a
        for prefix in ['inherent','residual']:
            l=int(row[f'{prefix}_likelihood']);i=int(row[f'{prefix}_impact'])
            assert 1<=l<=5 and 1<=i<=5
            assert int(row[f'{prefix}_score'])==l*i, f"Invalid {prefix} score {row['risk_id']}"
            assert row[f'{prefix}_rating']==band(l*i), f"Invalid {prefix} rating {row['risk_id']}"
        # Conservative fictional evidence rule: an unverified claim is not credited.
        if row['evidence_confidence']=='Low':
            assert row['residual_likelihood']==row['inherent_likelihood'], f"Unverified likelihood reduction: {row['risk_id']}"
            assert row['residual_impact']==row['inherent_impact'], f"Unverified impact reduction: {row['risk_id']}"
        assert row['decision']=='HOLD', f"Unexpected onboarding decision: {row['risk_id']}"
        for evidence_id in row['evidence_ids'].split(';'):
            if evidence_id: assert evidence_id in e
    for entry in calibration:
        current=next(x for x in risks if x['risk_id']==entry['risk_id'])
        assert entry['revised_residual_score']==current['residual_score'], f"Calibration score mismatch: {entry['risk_id']}"
        assert entry['revised_decision']==current['decision'], f"Calibration decision mismatch: {entry['risk_id']}"
    for row in actions:
        assert row['vendor_id'] in v and row['risk_id'] in r
        assert any(x['risk_id']==row['risk_id'] and x['action_id']==row['action_id'] for x in risks)
    print('PASS: 3 vendors, 24 questions, 72 responses, 8 evidence entries, 6 evidence-calibrated risks, 6 actions and 6 calibration entries.')
if __name__=='__main__':validate()
