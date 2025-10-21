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

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""
        # `_etype` returns whichever one is present so tests work across versions.
        def _etype(r):
            return getattr(r, 'entity_type', None) or getattr(r, 'entity', None)

        # --- Positive case: typical Italian passport format ---
        # Italian passports are commonly represented as two letters followed by seven digits (for example, HA1234567)
        # We expect the recognizer to return at least one result with entity type IT_PASSPORT
        text = "My passport number is HA1234567."
        results = analyze_text(text, ['IT_PASSPORT'])
        # Ensure at least one detection for IT_PASSPORT
        self.assertTrue(any(_etype(r) == 'IT_PASSPORT' for r in results),
                        'Should detect IT_PASSPORT in a normal passport string')
        # Find the detection and verify the matched substring equals the number
        match = next(r for r in results if _etype(r) == 'IT_PASSPORT')
        # `match.start` and `match.end` are indices into the original text
        self.assertIn('HA1234567', text[match.start:match.end])

        # --- Case-insensitive and punctuation robustness ---
        # Recognizer should match passport numbers regardless of case and when surrounded by punctuation like parentheses or commas
        text2 = 'Passport: ha1234567'
        results2 = analyze_text(text2, ['IT_PASSPORT'])
        self.assertTrue(any(_etype(r) == 'IT_PASSPORT' for r in results2))

        text3 = 'Document(HA1234567), please check.'
        results3 = analyze_text(text3, ['IT_PASSPORT'])
        self.assertTrue(any(_etype(r) == 'IT_PASSPORT' for r in results3))

        # --- Multiple matches in a single text ---
        # When multiple passport numbers appear, the analyzer should return multiple RecognizerResults. We check we find both expected values
        text4 = 'Passports: HA1234567 and HB7654321'
        results4 = analyze_text(text4, ['IT_PASSPORT'])
        matches = [r for r in results4 if _etype(r) == 'IT_PASSPORT']
        self.assertGreaterEqual(len(matches), 2, 'Should find at least two passport numbers')
        found = {text4[r.start:r.end] for r in matches}
        self.assertTrue('HA1234567' in found and 'HB7654321' in found)

        # --- Negative cases: prevent false positives ---
        # Too-short or malformed strings shouldn't match the IT_PASSPORT recognizer
        text_neg = 'Passport no. A12345'
        results_neg = analyze_text(text_neg, ['IT_PASSPORT'])
        self.assertFalse(any(_etype(r) == 'IT_PASSPORT' for r in results_neg))

       # Numeric-only passport (common in other countries) shouldn't be identified as an Italian passport.
        text_us = 'US passport: 123456789'
        results_us = analyze_text(text_us, ['IT_PASSPORT'])
        self.assertFalse(any(_etype(r) == 'IT_PASSPORT' for r in results_us))

  
        prefix = ['HA', 'HB', 'PC']
        numbers = ['1234567', '7654321', '0000001']

        for p in prefix:
            for n in numbers:
                passport_text = f'my passport is {p}{n}'
                result = analyze_text(passport_text, ['IT_PASSPORT'])
                # expect at least one result and that the first result reports the entity type as IT_PASSPORT
                self.assertTrue(len(result) > 0)
                # Some Presidio versions expose `entity_type`, others expose `entity`
                self.assertEqual(_etype(result[0]), 'IT_PASSPORT')

        # Negative test: when no passport is present, the analyzer should return an empty list (no recognitions).
        result = analyze_text('my passport is hidden', ['IT_PASSPORT'])
        self.assertListEqual(result, [])

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
