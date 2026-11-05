import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_project import band,load,validate
class ProjectTests(unittest.TestCase):
    def test_bands(self):
        for val,expected in [(1,'Low'),(4,'Low'),(5,'Medium'),(9,'Medium'),(10,'High'),(16,'High'),(17,'Critical'),(25,'Critical')]:
            self.assertEqual(band(val),expected)
    def test_vendor_coverage(self):
        responses=load('vendor_responses.csv')
        self.assertEqual(len(responses),72)
        for vid in ['CLOUD-001','PAY-001','SUP-001']:
            self.assertEqual(sum(row['vendor_id']==vid for row in responses),24)
    def test_evidence_gate(self):
        risks=load('risk_register.csv')
        self.assertEqual(len([r for r in risks if r['residual_rating']=='Critical']),1)
        for r in risks:
            if r['evidence_confidence']=='Low':
                self.assertEqual(r['inherent_score'],r['residual_score'])
                self.assertEqual(r['decision'],'HOLD')
    def test_integrity(self):validate()
if __name__=='__main__':unittest.main()
