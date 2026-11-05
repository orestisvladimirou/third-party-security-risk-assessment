#!/usr/bin/env python3
"""Check simulated ongoing supplier monitoring and event-driven risk changes."""
import csv
from validate_phase2 import ROOT, p2_load, validate_phase2

def p3_load(name):
    with (ROOT / "phase3" / "data" / name).open(encoding="utf-8", newline="") as fp:
        return list(csv.DictReader(fp))

def validate_phase3():
    validate_phase2()
    old = {r["risk_id"]: r for r in p2_load("reassessment.csv")}
    previous = {r["vendor_id"]: r for r in p2_load("decision_gates.csv")}
    current = p3_load("event_reassessment.csv")
    gates = {r["vendor_id"]: r for r in p3_load("decision_gates.csv")}
    plans = p3_load("monitoring_plan.csv")
    events = p3_load("monitoring_events.csv")
    actions = p3_load("new_actions.csv")
    history = p3_load("decision_history.csv")

    assert len(current) == 6
    assert {r["risk_id"] for r in current} == set(old)
    assert len(plans) == 3 and {p["vendor_id"] for p in plans} == set(gates) == set(previous)
    assert len(events) == len(actions) == 1
    event, action = events[0], actions[0]
    assert event["event_id"] == "EV-301" and event["vendor_id"] == "PAY-001"
    assert event["source_evidence_id"] == "P3-E01"
    assert (ROOT / "phase3" / "evidence" / "P3-E01-payroll-change.md").is_file()
    assert action["action_id"] == "ACT-007" and action["event_id"] == event["event_id"]
    assert action["vendor_id"] == "PAY-001" and action["risk_id"] == "R-003"
    assert action["status"] == "OPEN"
    assert len(history) == 9
    assert len({(r["stage"], r["vendor_id"]) for r in history}) == 9
    assert {r["stage"] for r in history} == {"Baseline", "Phase2", "Phase3"}

    for r in current:
        b = old[r["risk_id"]]
        assert r["vendor_id"] == b["vendor_id"]
        for k in ("likelihood", "impact", "score"):
            assert int(r["phase2_" + k]) == int(b["phase2_" + k]), "Phase 2 history was changed"
        l, i = int(r["phase3_likelihood"]), int(r["phase3_impact"])
        assert 1 <= l <= 5 and 1 <= i <= 5
        assert int(r["phase3_score"]) == l * i
        if r["risk_id"] == "R-003":
            assert (l, i) == (3, 4)
            assert r["change_evidence"] == "P3-E01"
        else:
            assert (l, i) == (int(b["phase2_likelihood"]), int(b["phase2_impact"]))
            assert not r["change_evidence"]
        assert r["phase3_decision"] == gates[r["vendor_id"]]["phase3_decision"]

    for vid, d in gates.items():
        maximum = max(int(r["phase3_score"]) for r in current if r["vendor_id"] == vid)
        assert maximum == int(d["highest_score"])
        assert d["phase2_decision"] == previous[vid]["decision"]
        assert d["phase3_decision"] == "HOLD", "High risk requires HOLD in this model"
        stage3 = next(h for h in history if h["stage"] == "Phase3" and h["vendor_id"] == vid)
        assert int(stage3["highest_residual_score"]) == maximum
        assert stage3["decision"] == d["phase3_decision"]
        stage2 = next(h for h in history if h["stage"] == "Phase2" and h["vendor_id"] == vid)
        assert stage2["decision"] == previous[vid]["decision"]
        assert int(stage2["highest_residual_score"]) == int(previous[vid]["highest_residual_score"])
    assert gates["PAY-001"]["privacy_gate"] == "REOPENED_SUBPROCESSOR_REVIEW"
    assert gates["PAY-001"]["phase2_decision"] == "CONDITIONAL_SIMULATED"
    print("PASS Phase 3: three monitoring plans, one scenario event, six linked risks, three HOLD decisions.")

if __name__ == "__main__":
    validate_phase3()
