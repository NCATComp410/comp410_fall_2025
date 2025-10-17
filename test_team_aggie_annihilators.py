"""Unit test file for team aggie_annihilators"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa
from presidio_analyzer import Pattern, PatternRecognizer, AnalyzerEngine


class TestTeam_aggie_annihilators(unittest.TestCase):
    """Test team aggie_annihilators PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        # Positive test case - basic format
        acn = 'my australian company number is ACN 010 499 966'
        result = analyze_text(acn, ['AU_ACN'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entity_type, 'AU_ACN')
        
        # Try without 'ACN' prefix
        acn_no_prefix = 'my australian company number is 010 499 966'
        result = analyze_text(acn_no_prefix, ['AU_ACN'])
        self.assertEqual(len(result), 1)

        # negative test case
        result = analyze_text('ACN is required', ['AU_ACN'])
        self.assertEqual(result, [])

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""

        # Create recognizer for AU_TFN (9 digits, optional dashes/spaces)
        pattern = Pattern(name="AU_TFN", regex=r"\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b", score=0.5)
        recognizer = PatternRecognizer(supported_entity="AU_TFN", patterns=[pattern])

        # initialize analyzer and register recognizer
        analyzer = AnalyzerEngine()
        analyzer.registry.add_recognizer(recognizer)

        # --- positive test cases ---
        prefix = ['123', '321']
        middle = ['456', '654']
        suffix = ['782', '987']

        for p in prefix:
            for m in middle:
                for s in suffix:
                    pos_text = f"My TFN is {p}-{m}-{s}"
                    result = analyzer.analyze(text=pos_text, entities=["AU_TFN"], language="en")
                    self.assertGreater(len(result), 0, f"Expected one AU_TFN entity in: {pos_text}")
                    self.assertEqual(result[0].entity_type, "AU_TFN")

        # --- negative test cases ---
        neg_text = "My TFN is hidden"
        result = analyzer.analyze(text=neg_text, entities=["AU_TFN"], language="en")
        self.assertListEqual(result, [])        




if __name__ == '__main__':
    unittest.main()
