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
        """Test MEDICAL_LICENSE functionality"""
    text_with_license = "Dr. Jane Doe - License No: MD123456"
    text_without_license = "Dr. Jane Doe - Healthcare Professional"

    # Run Presidio analyzer on both samples
    results_with = analyze_text(text_with_license)
    results_without = analyze_text(text_without_license)

    # Check that a medical license is detected in the first text
    detected_entities = [r.entity_type for r in results_with]
    self.assertIn("MEDICAL_LICENSE", detected_entities, "Should detect medical license")

    # Check that no medical license is detected in the second text
    detected_entities_without = [r.entity_type for r in results_without]
    self.assertNotIn("MEDICAL_LICENSE", detected_entities_without, "Should not detect medical license")



if __name__ == '__main__':
    unittest.main()
