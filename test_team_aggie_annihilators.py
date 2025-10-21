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
        # Positive test case - basic format
        aba = 'my australian routing number is 123456789'
        result = analyze_text(aba, ['aba_routing_number'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entity_type, 'aba_routing_number')

        # Without prefix
        aba_no_prefix = 'Routing number 123456789'
        result = analyze_text(aba_no_prefix, ['aba_routing_number'])
        self.assertEqual(len(result), 1)

        # Negative test case
        result = analyze_text('Routing info not provided', ['aba_routing_number'])
        self.assertEqual(result, [])

    def test_au_abn(self):
        """Test AU_ABN functionality"""
        # Add tests here later if needed
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
        # Positive test cases (should detect AU_MEDICARE)
        positives = [
            "Medicare number: 1234 56789 1",
            "AU Medicare: 1234567891",
            "my medicare is 2468 13579 1 please verify"
        ]
        for text in positives:
            with self.subTest(text=text):
                result = analyze_text(text, ['AU_MEDICARE'])
                self.assertGreaterEqual(len(result), 1, f"Should detect AU_MEDICARE in: {text}")
                self.assertEqual(result[0].entity_type, 'AU_MEDICARE')

        # Negative test cases (should NOT detect)
        negatives = [
            "Medicare 1234 5678 1",              # too short
            "Medicare 1234 56789 12",            # too long
            "Credit card: 4111 1111 1111 1111",  # unrelated pattern
            "Email: test@example.com",           # unrelated text
            "My number is 123456789"             # invalid format
        ]
        for text in negatives:
            with self.subTest(text=text):
                result = analyze_text(text, ['AU_MEDICARE'])
                self.assertEqual(result, [], f"Should NOT detect AU_MEDICARE in: {text}")

    def test_au_tfn(self):
        """Test AU_TFN functionality"""
        pass


if __name__ == '__main__':
    unittest.main()
