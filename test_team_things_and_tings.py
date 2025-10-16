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
        positive_text = "Valid numbers are 9876543210 and 12345678."
        expected_positive_numbers = ['9876543210', '12345678']
        found_results = analyze_text(positive_text, entity_list=["US_BANK_NUMBER"])
        found_positive_numbers = [positive_text[res.start:res.end] for res in found_results]
        self.assertCountEqual(found_positive_numbers, expected_positive_numbers)

        negative_text = "Invalid ones are 1234567 and 123456789012345678."
        expected_negative_numbers = []
        found_negative_numbers = analyze_text(negative_text, entity_list=["US_BANK_NUMBER"])
        self.assertEqual(found_negative_numbers, expected_negative_numbers)


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
        
        #positive test case
        result = analyze_text('123456789', ['US_PASSPORT'])
        self.assertEqual(result[0].entity_type, 'US_PASSPORT')

        #negative test case
        result = analyze_text('My passport numbers are hidden or not found', ['US_PASSPORT'])
        self.assertListEqual(result, [])

if __name__ == '__main__':
    unittest.main()
