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
    prefix = ['111', '222']
    middle = ['222', '333', '444']
    suffix = ['3434', '5454']

    # build sample
    #positive test cases
    for p in prefix:
        for m in middle:
            for s in suffix:
                nhs_text = f'my NHS number is {p}-{m}-{s}'
                print(nhs_text)
                result = analyze_text(nhs_text, ['UK_NHS'])

                # ensure result is not empty before checking
                self.assertTrue(result, f"No entities found in: {nhs_text}")
                self.assertEqual(result[0].entity_type, 'UK_NHS', f"Unexpected entity in: {nhs_text}")

    invalid_inputs = [
        "my NHS number is 123-abc-xyz",
        "no NHS number here",
        "my NHS number is 999-999-9999",
        "NHS? I don't have one.",
        "my NHS number is 12-34-56"
    ]

    for nhs_text in invalid_inputs:
        print(f"Negative test: {nhs_text}")
        result = analyze_text(nhs_text, ['UK_NHS'])

        # ensure result is empty or does not contain UK_NHS
        self.assertFalse(result, f"Unexpected entity detected in: {nhs_text}")
            

            

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
