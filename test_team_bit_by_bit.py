"""Unit test file for team bit_by_bit"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_bit_by_bit(unittest.TestCase):
    """Test team bit_by_bit PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

def test_medical_license(self):
        """
        Test MEDICAL_LICENSE functionality.
        Includes positive tests for numeric and alphanumeric formats,
        and a negative test.
        """
        # Define the entity type locally
        ENTITY_TYPE = "MEDICAL_LICENSE"

        # --- POSITIVE TEST CASES (25% of grade) ---

        # 1. FIX: Use a highly recognizable CA medical license format (A12345) with context
        text_1 = "CA Medical License A12345 is valid."
        # FIX: Passing the entity list as the second positional argument
        results_1 = analyze_text(text_1, [ENTITY_TYPE])
        self.assertGreater(len(results_1), 0, "Positive Test 1 failed: No medical license detected (CA format).")
        self.assertTrue(any(r.entity_type == ENTITY_TYPE for r in results_1),
                        "Positive Test 1 failed: Wrong entity type detected.")

        # 2. FIX: Use a highly recognizable TX medical license format (123456789) with context
        text_2 = "The doctor's TX state license is 123456789."
        # FIX: Passing the entity list as the second positional argument
        results_2 = analyze_text(text_2, [ENTITY_TYPE])
        self.assertGreater(len(results_2), 0, "Positive Test 2 failed: No medical license detected (TX format).")
        self.assertTrue(any(r.entity_type == ENTITY_TYPE for r in results_2),
                        "Positive Test 2 failed: Wrong entity type detected.")

        # --- NEGATIVE TEST CASE (25% of grade) ---

        # 3. Test a short, non-license number
        text_negative = "The office extension is 1001, please call quickly."
        # FIX: Passing the entity list as the second positional argument
        results_negative = analyze_text(text_negative, [ENTITY_TYPE])
        self.assertFalse(any(r.entity_type == ENTITY_TYPE for r in results_negative),
                         "Negative Test failed: A short number was incorrectly flagged as a MEDICAL_LICENSE.")
        
if __name__ == '__main__':
    unittest.main()
