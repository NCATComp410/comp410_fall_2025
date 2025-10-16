"""Unit test file for team code7"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_code7(unittest.TestCase):
    """Test team code7 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        """Test ES_NIE functionality"""

    def test_es_nif(self):
        """Test ES_NIF functionality"""
        letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
        prefix = ['12345678', '65926549']        
        
        for p in prefix:
            suffix = letters[int(p)%23]
            nif_text = f'{p}{suffix}'
            print(nif_text)
            result = analyze_text(nif_text, ['ES_NIF'])
            self.assertEqual(result[0].entity_type, 'ES_NIF')
        
        # negative test case
        result = analyze_text("my nif is hidden",['ES_NIF'])
        self.assertListEqual(result,[])


    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
