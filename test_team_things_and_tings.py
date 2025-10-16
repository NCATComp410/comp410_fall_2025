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
        possible = ['11111111111','22222222222','33333333333']
        #possible test cases
        for p in possible:
            license_text = f'my license # is {p}'
            result = analyze_text(license_text,['US_DRIVER_LICENSE'])
            self.assertEqual(result[0].entity_type, 'US_DRIVER_LICENSE')

        # negative test case
        result= analyze_text('my license is hidden', ['US_DRIVER_LICENSE'])
        self.assertListEqual(result,[])
    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
