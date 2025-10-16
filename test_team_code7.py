"""Unit test file for team code7"""
import unittest

from presidio_anonymizer import RecognizerResult
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

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

        # Assemble IBAN Codes
        positive_ibans: list[str] = [
            'IE64 IRCE 9205 0112 3456 78',
            'GB82 WEST 1234 5698 7654 32',
            'DE02 2022 0800 0051 0663 66',
            'GB68 TRWI 2314 7094 9392 79',
            'FR14 2004 1010 0505 0001 3M02606'
        ]

        negative_ibans: list[str] = [
            'ZZ91 2100 0418 4502 0005 1332',
            'SA03 8000 0000 6080 1016 7520',
            'PL84 1090 1014 0000 0712 1981 2874',
            'IF64 IRFD 9205 0112 3456 78',
            'DE89 3704 2398 0532 0130 00'
        ]

        # Positive Test Cases
        print('Positive IBAN Test Cases:')

        for iban in positive_ibans:
            iban: str = f'My IBAN is {iban}'
            print(f' ... {iban}')
            result: list[RecognizerResult] = analyze_text(iban, ['IBAN_CODE'])
            self.assertGreater(len(result), 0)
            self.assertEqual(result[0].entity_type, 'IBAN_CODE')

        # Negative Test Cases
        print('\nNegative IBAN Test Cases:')

        for iban in negative_ibans:
            iban: str = f'My IBAN is {iban}'
            print(f' ... {iban}')
            result: list[RecognizerResult] = analyze_text(iban, ['IBAN_CODE'])
            self.assertEqual(len(result), 0)

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
