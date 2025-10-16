"""Unit test file for team things_and_tings"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_things_and_tings(unittest.TestCase):
    """Test team things_and_tings PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""
        prefix = ['901', '912', '987']
        middle = ['70', '85', '99']
        suffix = ['1234', '5678']

        # positive test cases
        for p in prefix:
            for m in middle:
                for s in suffix:
                    itin_text = f'my itin is {p}-{m}-{s}'
                    result = analyze_text(itin_text, ['US_ITIN'])
                    #check entity_type for US_ITIN
                    self.assertTrue(result, f"Failed to detect ITIN in {itin_text}")
                    self.assertEqual(result[0].entity_type, 'US_ITIN')
        
        # negative test cases
        result = analyze_text('my itin is hidden', ['US_ITIN'])
        self.assertListEqual(result, [])

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
