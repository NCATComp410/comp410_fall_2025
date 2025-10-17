"""Unit test file for team type_error_titans"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 
class TestTeam_type_error_titans(unittest.TestCase):
    """Test team type_error_titans PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")
    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""
    def test_location(self):
        """Test LOCATION functionality"""
    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""
        prefix = ['943','485','901']
        middle = ['476','777','234']
        suffix = ['591','345','561']
        check = ['9','7','8']

        for i, p in enumerate(prefix):
            m = middle[i]
            s = suffix[i]
            c = check[i]

            nhs_text = f'my uk_nhs is {p}{m}{s}{c}'
            result = analyze_text(nhs_text,['UK_NHS'])
            self.assertEqual(result[0].entity_type,'UK_NHS')

        result = analyze_text('my uk_nhs is hidden',['UK_NHS'])
        self.assertListEqual(result,[])

        print(result)



    def test_uk_nino(self):
        """Test UK_NINO functionality"""
if __name__ == '__main__':
    unittest.main()
