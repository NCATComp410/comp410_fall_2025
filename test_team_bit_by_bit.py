import unittest
from pii_scan import analyze_text, show_aggie_pride


class TestTeam_bit_by_bit(unittest.TestCase):
    """Test team bit_by_bit PII functions"""

    def test_show_aggie_pride(self):
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        valid_cards = [
            '4111-1111-1111-1111',
            '5500-0000-0000-0004',
            '3400-0000-0000-009',
            '6011-0000-0000-0004',
            '5365-3563-3929-5416',
            '6583-9941-9899-2949',
            '5580-4369-7799-9575',
        ]
        for card in valid_cards:
            text = f"My credit card is {card}"
            result = analyze_text(text, ['CREDIT_CARD'])
            self.assertEqual(result[0].entity_type, 'CREDIT_CARD')

        # Negative test
        result = analyze_text("My credit card is hidden", ['CREDIT_CARD'])
        self.assertEqual(result, [])

    def test_crypto(self):
        pass

    def test_date_time(self):
        valid_dates = [
            'January 1, 2025',
            '2025-10-16',
            '10/16/2025',
            '16 Oct 2025',
            '2025/10/16 14:30',
            'October 16th, 2025 2:30 PM',
            '3:45 PM on October 16, 2025',
            'October 16, 2025 at noon'
        ]
        for date_text in valid_dates:
            text = f"The event is at {date_text}"
            result = analyze_text(text, ['DATE_TIME'])
            self.assertTrue(result)
            self.assertEqual(result[0].entity_type, 'DATE_TIME')

        result = analyze_text("The event happens at", ['DATE_TIME'])
        self.assertEqual(result, [])

    def test_email_address(self):
        pass

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""
        text_with_license = "MD123456"
        text_without_license = "Dr. Jane Doe - Healthcare Professional"

        entities = ["MEDICAL_LICENSE"]

        results_with = analyze_text(text_with_license, entities)
        results_without = analyze_text(text_without_license, entities)

        # Extract detected text using start/end
        texts_with = [text_with_license[e.start:e.end] for e in results_with]
        texts_without = [text_without_license[e.start:e.end] for e in results_without]

        self.assertIn("MD123456", texts_with)
        self.assertNotIn("MD123456", texts_without)


if __name__ == '__main__':
    unittest.main(exit=False)
