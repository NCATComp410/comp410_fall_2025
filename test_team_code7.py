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

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
