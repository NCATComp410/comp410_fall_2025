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
        valid_compact = ["323456789012", "223456789018"]  # pass Verhoeff
        samples = [
            f"My Aadhaar number is {valid_compact[0]}",                  # compact
            f"My Aadhaar number is {valid_compact[1]}",                  # compact
            f"Aadhaar: {valid_compact[0][:4]} {valid_compact[0][4:8]} {valid_compact[0][8:]}",  # spaced
            f"Aadhaar ID {valid_compact[1][:4]}-{valid_compact[1][4:8]}-{valid_compact[1][8:]}",# hyphenated
        ]

        for text in samples:
            result = analyze_text(text, ['IN_AADHAAR'])
            self.assertGreater(len(result), 0, f"No match for: {text}")
            self.assertEqual(result[0].entity_type, 'IN_AADHAAR')

        # Negative
        neg = analyze_text("My Aadhaar is hidden", ['IN_AADHAAR'])
        self.assertListEqual(neg, [])

    # Negative
        result = analyze_text("My Aadhaar is hidden", ['IN_AADHAAR'])
        self.assertListEqual(result, [])
        
    def test_in_pan(self):
        """Test IN_PAN functionality"""

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
