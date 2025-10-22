"""Unit test file for team aggie_annihilators"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


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
        # --- Positive (valid checksum) ---
        valid_numbers = [
            "My Medicare number is 2123 45670 1",
            "Medicare number 2123456701",  # no spaces
        ]
        for text in valid_numbers:
            result = analyze_text(text, ["AU_MEDICARE"])
            self.assertGreater(len(result), 0, f"Expected AU_MEDICARE detected in: {text}")
            self.assertEqual(result[0].entity_type, "AU_MEDICARE")

        # --- Negative (invalid checksum or format) ---
        invalid_numbers = [
            "My number is 7123 45670 1",     # invalid prefix (7 not allowed)
            "Medicare 12345678",             # too short
            "Medicare 2123-45670-1",         # dashes (not supported in default patterns)
            "My medicare info is hidden",    # no number
        ]
        for text in invalid_numbers:
            result = analyze_text(text, ["AU_MEDICARE"])
            self.assertEqual(result, [], f"Should NOT detect AU_MEDICARE in: {text}")

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()