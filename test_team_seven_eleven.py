"""Unit test file for team seven_eleven"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_seven_eleven(unittest.TestCase):
    """Test team seven_eleven PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

    def test_in_pan(self):
        """Test IN_PAN functionality"""
        beginning = ['ABCDE', 'FFFFF', 'ABABA', 'CDCDC']
        middle = ['1234', '9999', '4343', '9876']
        last = ['A', 'B', 'C', 'D']
        # Positive Test Case
        for b in beginning:
            for m in middle:
                for l in last:
                    in_pan_text = f'My Indian Permanent Account Number is {b}-{m}-{l}'
                    result = analyze_text(in_pan_text, ['IN_PAN'])
                    self.assertEqual(result[0].entity_type, 'IN_PAN')
        # Negative Test Case
        result = analyze_text('My PAN is hidden', ['IN_PAN'])
        self.assertEqual(result, [])

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""
        # Parts of vehicle registration
        state_code = {"MH", "JK", "MZ", "DL"}
        rto_number = {"01", "14", "05", "29"}
        registration_series = {"A", "HK", "GR", "BN"}
        unique_number = {"0345", "4132", "0023", "9026"}

        # Build vehicle registration
        # Positive test cases
        for s in state_code:
            for rto in rto_number:
                for series in registration_series:
                    for num in unique_number:
                        vehicle_registration_text = f'My vehicle registration number is {s}{rto}{series}{num}'
                        result = analyze_text(vehicle_registration_text, ['IN_VEHICLE_REGISTRATION']) 
                        # Check entity_type for IN_VEHICLE_REGISTRATION
                        self.assertEqual(result[0].entity_type, 'IN_VEHICLE_REGISTRATION')

        # Negative test cases
        result = analyze_text('My vehicle registration is hidden ', ['IN_VEHICLE_REGISTRATION'])
        self.assertListEqual(result, [])

        result = analyze_text('My vehicle registration is 111-222-3333 ', ['IN_VEHICLE_REGISTRATION'])
        self.assertListEqual(result, [])

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
