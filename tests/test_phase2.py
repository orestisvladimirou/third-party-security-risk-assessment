import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_phase2 import validate_phase2, p2_load

class Phase2Tests(unittest.TestCase):
    def test_integrity(self):
        validate_phase2()

    def test_three_supplier_decisions(self):
        actual = {d["vendor_id"]: d["decision"] for d in p2_load("decision_gates.csv")}
        self.assertEqual(actual, {
            "CLOUD-001": "HOLD",
            "PAY-001": "CONDITIONAL_SIMULATED",
            "SUP-001": "HOLD",
        })

    def test_likelihood_versus_impact(self):
        risks = {r["risk_id"]: r for r in p2_load("reassessment.csv")}
        self.assertEqual((risks["R-001"]["phase2_likelihood"],risks["R-001"]["phase2_impact"]),("2","5"))
        self.assertEqual((risks["R-004"]["phase2_likelihood"],risks["R-004"]["phase2_impact"]),("3","2"))
        for rid in ("R-002","R-005","R-006"):
            self.assertEqual(risks[rid]["phase2_score"], risks[rid]["baseline_score"])

    def test_legal_gate_not_scored(self):
        r = next(x for x in p2_load("reassessment.csv") if x["risk_id"] == "R-003")
        self.assertEqual(r["scoring_evidence_ids"], "P2-E03")
        self.assertEqual(r["other_evidence_ids"], "P2-E04")
