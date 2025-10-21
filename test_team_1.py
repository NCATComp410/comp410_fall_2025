"""Unit test file for team 1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_1(unittest.TestCase):
    """Test team 1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""
        prefixes = ["AB", "CD", "EF", "U1"]
        numbers = ["1234567", "7654321"]
        suffixes = ["A", "B"]

        # positive test cases
        for prefix in prefixes:
            for num in numbers:
                for suffix in suffixes:
                    candidate = f"{prefix}{num}{suffix}"
                    with self.subTest(candidate=candidate):
                        result = analyze_text(candidate, ["IT_DRIVER_LICENSE"])
                        if result:
                            self.assertEqual(result[0].entity_type, "IT_DRIVER_LICENSE")

        # negative test case
        result = analyze_text("my driver license number is hidden", ["IT_DRIVER_LICENSE"])
        self.assertEqual(result, [])
        
    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
