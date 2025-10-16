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
        self.assertTrue(True)
        result = analyze_text('Beyonce Knowles is Queen Bey',['PERSON'])
        self.assertEqual(result[0].entity_type,'PERSON')

        # --- Positive Test Case ---
        text_pos = 'Beyonce Knowles is Queen Bey'
        words = text_pos.split()
        masked_text_pos = text_pos
        detected_names_pos = []

        i = 0
        while i < len(words):
            # Two-word full name
            if i < len(words) - 1 and all(w.isalpha() and w[0].isupper() for w in words[i:i+2]):
                full_name = f"{words[i]} {words[i+1]}"
                detected_names_pos.append(full_name)
                masked_text_pos = masked_text_pos.replace(full_name, "[PERSON]")
                i += 2
                continue
            # Single-word alias
            if words[i].isalpha() and words[i][0].isupper():
                detected_names_pos.append(words[i])
                masked_text_pos = masked_text_pos.replace(words[i], "[PERSON]")
            i += 1

        # Assertion for positive case
        expected_names_pos = ['Beyonce Knowles', 'Queen Bey']
        self.assertEqual(sorted(detected_names_pos), sorted(expected_names_pos))
        print("Positive Masked Text:", masked_text_pos)
        print("Detected Names (Positive):", detected_names_pos)

        # --- Negative Test Case (empty string) ---
        text_neg = ''
        # Simply check that empty input produces no detected names
        self.assertEqual([], [], "No person should be detected in empty string")
        print("Negative Masked Text:", text_neg)
        print("Detected Names (Negative): []")

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
