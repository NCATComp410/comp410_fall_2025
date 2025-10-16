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

        # Positive test cases (valid crypto patterns)
        crypto_samples = [
            "My wallet is 0x32Be343B94f860124dC4fEe278FDCBD38C102D88",  # Ethereum
            "Send BTC to 1BoatSLRHtKNngkdXEeobR76b53LETtpyT",           # Bitcoin
            "LTC address: LZ3ZbYdZbYdZbYdZbYdZbYdZbYdZbYdZbY"           # Litecoin-style
        ]

        for sample in crypto_samples:
            result = analyze_text(sample, ['CRYPTO'])
            # Check that we correctly detect crypto
            self.assertGreater(len(result), 0, f"No crypto detected in: {sample}")
            self.assertEqual(result[0].entity_type, 'CRYPTO')

        # Negative test cases (no crypto present)
        negative_samples = [
            "I love using digital money but not real crypto",
            "My account number is 123456789",
            "This is just a random string with numbers 0x123"
        ]

        for sample in negative_samples:
            result = analyze_text(sample, ['CRYPTO'])
            # Ensure nothing is detected
            self.assertListEqual(result, [], f"False positive for: {sample}")


if __name__ == '__main__':
    unittest.main()
