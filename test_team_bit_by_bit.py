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
        valid_dates = [
            'January 1, 2025', #All possible date_times
            '2025-10-16',
            '10/16/2025', 
            '16 Oct 2025',
            '2025/10/16 14:30',
            'October 16th, 2025 2:30 PM',
            '3:45 PM on October 16, 2025',  # combined date and time
            'October 16, 2025 at noon'
        ]

        # Positive test cases
        for date_text in valid_dates:
            text = f"The event is at {date_text}"
            result = analyze_text(text, ['DATE_TIME'])
            self.assertTrue(result, f"No DATE_TIME entity found for: {date_text}")
            self.assertEqual(result[0].entity_type, 'DATE_TIME', f"Incorrect entity for: {date_text}")

        # Negative test cases
        result = analyze_text("The event happens at", ['DATE_TIME'])
        self.assertEqual(result, [])

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
