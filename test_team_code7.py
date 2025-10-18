"""Unit test file for team code7"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_code7(unittest.TestCase):
    """Test team code7 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
        prefix = {'X': '0', 'Y': '1', 'Z': '2'}
        middle = ['1234567', '7654321', '3456789']

        for p in prefix:
            for m in middle:
                full = int(prefix[p] + m)
                
                suffix = letters[full % 23]
                nie_text = f'my nie is {p}{m}{suffix}'
                print(nie_text)
                result = analyze_text(nie_text, ['ES_NIE'])
                self.assertEqual(result[0].entity_type, 'ES_NIE')

        # negative test cases
        result = analyze_text('my nie is hidden', ['ES_NIE'])
        self.assertListEqual(result, [])

    def test_es_nif(self):
        """Test ES_NIF functionality"""

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality""" 
        
        correctID = "My FI Personal code is 131052-308T"
        wrongID = "MY FI Personal code 211209+++iwqow"

        correctResult = analyze_text(text = correctID,  entity_list=["FI_PERSONAL_IDENTITY_CODE"])
        failureReseult = analyze_text(text = wrongID,  entity_list=["FI_PERSONAL_IDENTITY_CODE"])

         # positive test case Checks if ID matches the format
        self.assertEqual(correctResult[0].entity_type , "FI_PERSONAL_IDENTITY_CODE")


         # error test case, Returns None because string does not match regex
        self.assertListEqual(failureReseult, [])

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""

        correctIP = "192.158.1.38"
        wrongIP = "192.158.1.372"

        correctResult = analyze_text(text=correctIP, entity_list=["IP_ADDRESS"])
        wrongResult = analyze_text(text=wrongIP, entity_list=["IP_ADDRESS"])

        self.assertEqual(correctResult[0].entity_type, "IP_ADDRESS")
        self.assertEqual(wrongResult, [])


if __name__ == '__main__':
    unittest.main()
