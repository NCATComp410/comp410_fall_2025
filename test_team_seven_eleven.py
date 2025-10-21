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
        # Voter ID Sample Pattern
        series = ['ABC', 'STU', 'WXY']
        number = ['1234567', '9871236', '0189453' ]

        # Positive Test Case
        for ser in series:
            for numb in number:
                voterID_text = f'My voter id number is {ser}{numb}'
                result = analyze_text(voterID_text , ['IN_VOTER'])
                self.assertEqual(result[0].entity_type, 'IN_VOTER')
        # Negative Test Case
        result = analyze_text('My voter ID is hidden ', ['IN_VOTER'])
        self.assertListEqual(result, [])

        result = analyze_text('My voter ID is wrong 678lolwut', ['IN_VOTER'])
        self.assertListEqual(result, [])






                




if __name__ == '__main__':
    unittest.main()
