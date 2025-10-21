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
        prefix = ['919', '212', '313']
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
                    self.assertEqual(result[0].entity_type, 'PHONE_NUMBER')
        result = analyze_text('my phone number is hidden', ['PHONE_NUMBER'])
        self.assertListEqual(result, [])

    def test_location(self):
        """Test LOCATION functionality"""
        # sample locations
        states = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
            "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
            "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
            "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
            "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
            "New Hampshire", "New Jersey", "New Mexico", "New York", 
            "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
            "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
            "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
            "West Virginia", "Wisconsin", "Wyoming"
        ]
        
        # positive test cases
        for area in states:
            location_text = f'I live in {area}'
            result = analyze_text(location_text, ['LOCATION'])
            # check entity_type for LOCATION
            self.assertEqual(result[0].entity_type, 'LOCATION')

        # negative test case
        result = analyze_text('I live in hidden', ['LOCATION'])
        self.assertListEqual(result, [])

    def test_person(self):
        """Test PERSON functionality"""
        result = analyze_text('Beyonce Knowles is Queen Bey',['PERSON'])
        self.assertEqual(result[0].entity_type,'PERSON')
        self.assertEqual(result[1].entity_type,'PERSON')

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
        text_neg =  "This isn't a name"
        # Simply check that empty input produces no detected names
        result_neg = analyze_text(text_neg, ['PERSON'])
        self.assertListEqual(result_neg, [], "No person should be detected in empty string")


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

    def test_uk_nino(self):
        """Test UK_NINO functionality"""
        prefix = ['AA', 'BB', 'CC']
        middle = ['375629', '837452', '926418']
        suffix = ['A', 'B', 'C', 'D']

        # Build sample nino
        # Positive test cases
        for p in prefix:
            for m in middle:
                for s in suffix:
                    nino_text = f'my nino is {p}{m}{s}'
                    print(nino_text)
                    result = analyze_text(nino_text, ['UK_NINO'])
                    # Check entity_type for UK_NINO
                    self.assertEqual(result[0].entity_type, 'UK_NINO')
        result = analyze_text('my nino is hidden', ['UK_NINO'])
        self.assertListEqual(result, [])

if __name__ == '__main__':
    unittest.main()
