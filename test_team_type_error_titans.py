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
        prefix = ['121', '212', '313']
        middle = ['123', '456', '789']
        suffix = ['2233', '4455', '6677']

        # sample phone number 
        # positive test cases
        for p in prefix:
            for m in middle:
                for s in suffix:
                    number_text = f'my phone number is {p}-{m}-{s}'
                    print(number_text)
                    result = analyze_text(number_text, ['PHONE_NUMBER'])
                    # check entity_type for PHONE_NUMBER
                    #self.assertEqual(result[0].entity_type, 'PHONE_NUMBER')
        result = analyze_text('my phone number is hidden', ['PHONE_NUMBER'])
        self.assertListEqual(result, [])

    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
