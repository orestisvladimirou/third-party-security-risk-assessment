#!/usr/bin/env python3
"""Consistency checks for a fully fictional second-round supplier assessment."""
import csv
from pathlib import Path
from validate_project import ROOT, load, band, validate

P2 = ROOT / "phase2" / "data"

def p2_load(name):
    with (P2 / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))

def validate_phase2():
    validate()
    old = {r["risk_id"]: r for r in load("risk_register.csv")}
    vendors = {v["vendor_id"]: v for v in load("vendors.csv")}
    exhibits = p2_load("evidence_assessments.csv")
    risks = p2_load("reassessment.csv")
    gates = p2_load("decision_gates.csv")
    actions = p2_load("action_updates.csv")
    evidence = {e["evidence_id"]: e for e in exhibits}
    decisions = {g["vendor_id"]: g for g in gates}

    assert len(exhibits) == len(evidence) == 7, "Evidence ID collision or missing exhibit"
    assert len(risks) == len(old) == 6 and {x["risk_id"] for x in risks} == set(old)
    assert len(gates) == len(decisions) == len(vendors) == 3
    assert len(actions) == 6
    assert all(v["decision"] == "HOLD" for v in vendors.values()), "Initial inventory not all HOLD"
    baseline_actions = {a["action_id"]: a for a in load("remediation_tracker.csv")}
    assert {a["action_id"] for a in actions} == set(baseline_actions)

    for e in exhibits:
        assert e["vendor_id"] in vendors
        assert (ROOT / e["artifact_path"]).is_file(), "Missing synthetic exhibit: " + e["evidence_id"]
        assert e["usable_for_scoring"] in ("Yes", "No")
        assert e["gate_use"] in ("Yes", "No")
        for risk_id in e["risk_ids"].split(";"):
            assert risk_id in old and old[risk_id]["vendor_id"] == e["vendor_id"]

    for r in risks:
        base = old[r["risk_id"]]
        assert r["vendor_id"] == base["vendor_id"]
        for k in ("likelihood", "impact", "score"):
            assert int(r["baseline_" + k]) == int(base["residual_" + k]), "Baseline mismatch"
        l, i = int(r["phase2_likelihood"]), int(r["phase2_impact"])
        assert 1 <= l <= 5 and 1 <= i <= 5
        assert int(r["phase2_score"]) == l * i
        assert r["phase2_rating"] == band(l * i)
        scored = [x for x in r["scoring_evidence_ids"].split(";") if x]
        other = [x for x in r["other_evidence_ids"].split(";") if x]
        assert scored or other, "Every reassessment needs an evidence trail"
        for eid in scored:
            assert eid in evidence and evidence[eid]["usable_for_scoring"] == "Yes"
            assert r["risk_id"] in evidence[eid]["risk_ids"].split(";")
        for eid in other:
            assert eid in evidence and r["risk_id"] in evidence[eid]["risk_ids"].split(";")
        if l < int(r["baseline_likelihood"]) or i < int(r["baseline_impact"]):
            assert scored, "Unsubstantiated risk reduction"
        expected = r["change_basis"]
        if expected == "Unchanged":
            assert l == int(r["baseline_likelihood"]) and i == int(r["baseline_impact"])
        elif expected == "Likelihood-only":
            assert l < int(r["baseline_likelihood"]) and i == int(r["baseline_impact"])
        elif expected == "Impact-only":
            assert l == int(r["baseline_likelihood"]) and i < int(r["baseline_impact"])
        else:
            raise AssertionError("Unknown change basis")
        assert r["decision"] == decisions[r["vendor_id"]]["decision"]
        assert r["action_id"] in baseline_actions
        assert base["action_id"] == r["action_id"]

    for vendor_id, d in decisions.items():
        maximum = max(int(r["phase2_score"]) for r in risks if r["vendor_id"] == vendor_id)
        assert int(d["highest_residual_score"]) == maximum
        if maximum >= 10:
            assert d["decision"] == "HOLD", "High risk without exception must remain HOLD"
        if d["decision"] == "CONDITIONAL_SIMULATED":
            assert maximum <= 9 and d["risk_gate"] == "MEDIUM_CONDITIONAL"
            assert d["privacy_gate"] == "PASS_SIMULATED"
            assert d["dora_gate"] == "PASS_SIMULATED_STANDARD_ICT"
            assert d["operational_gate"] == "PASS_SIMULATED"
            assert "2026-12-20" in d["conditions"]
            assert any(e["vendor_id"] == vendor_id and e["gate_use"] == "Yes" for e in exhibits)

    for a in actions:
        assert a["risk_id"] in old
        assert a["vendor_id"] == old[a["risk_id"]]["vendor_id"]
        assert a["action_id"] == old[a["risk_id"]]["action_id"]

    print("PASS Phase 2: seven fictional exhibits; six justified reassessments; six action updates; three gated supplier decisions.")

if __name__ == "__main__":
    validate_phase2()
