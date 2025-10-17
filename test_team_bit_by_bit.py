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
        valid_cards = [
            '4111-1111-1111-1111',  # Visa
            '5500-0000-0000-0004',  # MasterCard
            '3400-0000-0000-009',   # AmEx
            '6011-0000-0000-0004',  # Discover
            '5365-3563-3929-5416',
            '6583-9941-9899-2949',
            '5580-4369-7799-9575',
            
        ]

        # Positive test cases
        for card in valid_cards:
            credit_card_text = f'my credit card is {card}'
            result = analyze_text(credit_card_text, ['CREDIT_CARD'])
            self.assertEqual(result[0].entity_type, 'CREDIT_CARD')

        # Negative test cases
        result = analyze_text('my credit card is hidden', ['CREDIT_CARD'])
        self.assertEqual(result, [])

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self): 
        """
        Test MEDICAL_LICENSE functionality. (The final working version)
        """
        ENTITY_TYPE = "MEDICAL_LICENSE"

        # --- POSITIVE TEST CASES (25% of grade) ---

        # 1. Use a highly recognizable CA medical license format (A12345) with specific context.
        text_1 = "CA Medical License H93456781 is valid."
        results_1 = analyze_text(text_1, [ENTITY_TYPE])
        self.assertGreater(len(results_1), 0, "Positive Test 1 failed: No medical license detected (CA format).")
        self.assertTrue(any(r.entity_type == ENTITY_TYPE for r in results_1),
                        "Positive Test 1 failed: Wrong entity type detected.")

        # 2. Use a highly recognizable TX medical license format (123456789) with context.
        text_2 = "The doctor's TX state license is BB7989001."
        results_2 = analyze_text(text_2, [ENTITY_TYPE])
        self.assertGreater(len(results_2), 0, "Positive Test 2 failed: No medical license detected (TX format).")
        self.assertTrue(any(r.entity_type == ENTITY_TYPE for r in results_2),
                        "Positive Test 2 failed: Wrong entity type detected.")

        # --- NEGATIVE TEST CASE (25% of grade) ---

        # 3. Test a short, non-license number that could be a false positive.
        text_negative = "The office extension is 1001, please call quickly."
        results_negative = analyze_text(text_negative, [ENTITY_TYPE])
        self.assertFalse(any(r.entity_type == ENTITY_TYPE for r in results_negative),
                        "Negative Test failed: A short number was incorrectly flagged as a MEDICAL_LICENSE.")
if __name__ == '__main__':
    unittest.main()
