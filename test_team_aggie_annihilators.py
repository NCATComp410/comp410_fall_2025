"""Unit test file for team aggie_annihilators"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 
from presidio_analyzer import AnalyzerEngine
from pii_scan import analyze_text  # assuming your project uses this helper
from au_medicare_recognizer import AuMedicareRecognizer  # your recognizer class


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

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""
        # Initialize analyzer and add recognizer
        analyzer = AnalyzerEngine()
        analyzer.registry.add_recognizer(AuMedicareRecognizer())

        # --- Positive (valid checksum) ---
        valid_numbers = [
            "My Medicare number is 2123 45670 1",
            "Medicare: 3123 45670 2",
            "Medicare card 5234 67890 3",
            "Here’s my medicare number: 4123 45670 1",
            "Medicare number 5123456703",  # no spaces
        ]
        for text in valid_numbers:
            result = analyzer.analyze(text=text, entities=["AU_MEDICARE"], language="en")
            self.assertGreater(len(result), 0, f"Expected AU_MEDICARE detected in: {text}")
            self.assertEqual(result[0].entity_type, "AU_MEDICARE")

        # --- Negative (invalid checksum or format) ---
        invalid_numbers = [
            "Medicare number 2123 45670 9",  # wrong checksum
            "My number is 7123 45670 1",     # invalid prefix (7 not allowed)
            "Medicare 12345678",             # too short
            "Medicare 2123-45670-1",         # dashes (not supported in default patterns)
            "My medicare info is hidden",    # no number
        ]
        for text in invalid_numbers:
            result = analyzer.analyze(text=text, entities=["AU_MEDICARE"], language="en")
            self.assertEqual(result, [], f"Should NOT detect AU_MEDICARE in: {text}")




    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
