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
        prefixes = ['john.doe', 'jane_smith', 'user123']
        domains = ['gmail.com', 'outlook.com', 'ncat.edu']

        # Positve test cases
        for p in prefixes:
            for d in domains:
                email_text = f'my email is {p}@{d}'
                result = analyze_text(email_text, ['EMAIL_ADDRESS'])
                self.assertEqual(result[0].entity_type, 'EMAIL_ADDRESS')

        # Negative test cases
        result = analyze_text('my email is hidden', ['EMAIL_ADDRESS'])
        self.assertListEqual(result, [])

        
    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""



if __name__ == '__main__':
    unittest.main()
