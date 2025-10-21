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

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""
        #Positive test case
        test_code = 'RSSMRA80M15H501K'
        fiscal_code_regex = r"\b[A-Z]{6}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1}\b"
        result = analyze_text(test_code,['IT_FISCAL_CODE'])
        self.assertNotEqual(result, [], "Expected a fiscal code to be detected.")
        self.assertEqual(result[0].entity_type, 'IT_FISCAL_CODE',
                         "The detected entity type is incorrect.")
        #Negative test case
        w_result = analyze_text('Error: No Fiscal Code found',['IT_FISCAL_CODE'])
        self.assertEqual(w_result, [], "Expected no fiscal codes to be detected in this text.")
    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
