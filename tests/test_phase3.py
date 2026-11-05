import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_phase3 import validate_phase3, p3_load

class MonitoringTests(unittest.TestCase):
    def test_monitoring_integrity(self):
        validate_phase3()

    def test_conditional_decision_is_revoked(self):
        rows = {r["vendor_id"]: r for r in p3_load("decision_gates.csv")}
        self.assertEqual(rows["PAY-001"]["phase2_decision"], "CONDITIONAL_SIMULATED")
        self.assertEqual(rows["PAY-001"]["phase3_decision"], "HOLD")

    def test_event_affects_only_payroll_access_risk(self):
        rows = p3_load("event_reassessment.csv")
        changed = [r["risk_id"] for r in rows if r["phase2_score"] != r["phase3_score"]]
        self.assertEqual(changed, ["R-003"])
        self.assertEqual(next(r for r in rows if r["risk_id"] == "R-003")["change_evidence"], "P3-E01")
