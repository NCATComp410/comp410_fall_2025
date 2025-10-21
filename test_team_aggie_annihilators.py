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
        # Positive: valid 9-digit ABA routing numbers (commonly used in docs)
        positives = [
            "Routing number 111000025",
            "ABA: 021000021",
        ]
        for text in positives:
            with self.subTest(text=text):
                res = analyze_text(text, ['ABA_ROUTING_NUMBER'])
                self.assertGreaterEqual(len(res), 1, f"Should detect ABA_ROUTING_NUMBER in: {text}")
                self.assertEqual(res[0].entity_type, 'ABA_ROUTING_NUMBER')

        # Negative: wrong length / unrelated
        negatives = [
            "routing number 11100002",     # 8 digits
            "routing number 1110000250",   # 10 digits
            "credit card 4111 1111 1111 1111",
            "Routing info not provided",
        ]
        for text in negatives:
            with self.subTest(text=text):
                res = analyze_text(text, ['ABA_ROUTING_NUMBER'])
                self.assertEqual(res, [], f"Should NOT detect ABA_ROUTING_NUMBER in: {text}")

    def test_au_abn(self):
        """Test AU_ABN functionality"""
        # Add specific ABN tests later if assigned
        pass

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        # Positive test case - basic format
        acn = 'my australian company number is ACN 010 499 966'
        result = analyze_text(acn, ['AU_ACN'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entity_type, 'AU_ACN')

        # Try without 'ACN' prefix
        acn_no_prefix = 'my australian company number is 010 499 966'
        result = analyze_text(acn_no_prefix, ['AU_ACN'])
        self.assertEqual(len(result), 1)

        # Negative test case
        result = analyze_text('ACN is required', ['AU_ACN'])
        self.assertEqual(result, [])

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""
        # Use numbers that satisfy the AU Medicare checksum (10 digits total).
        positives = [
            "Medicare number: 1234 56788 1",        # 1234567881
            "AU Medicare: 2876543251",              # compact
            "my medicare is 2468 13576 1 please verify"  # 2468135761
        ]
        for text in positives:
            with self.subTest(text=text):
                result = analyze_text(text, ['AU_MEDICARE'])
                self.assertGreaterEqual(len(result), 1, f"Should detect AU_MEDICARE in: {text}")
                self.assertEqual(result[0].entity_type, 'AU_MEDICARE')

        negatives = [
            "Medicare 1234 5678 1",               # too short
            "Medicare 1234 56789 12",             # too long
            "Credit card: 4111 1111 1111 1111",   # unrelated pattern
            "Email: test@example.com",            # unrelated text
            "My number is 123456789"              # wrong length/checks
        ]
        for text in negatives:
            with self.subTest(text=text):
                result = analyze_text(text, ['AU_MEDICARE'])
                self.assertEqual(result, [], f"Should NOT detect AU_MEDICARE in: {text}")

    def test_au_tfn(self):
        """Test AU_TFN functionality"""
        # Add specific TFN tests later if assigned
        pass


if __name__ == '__main__':
    unittest.main()
