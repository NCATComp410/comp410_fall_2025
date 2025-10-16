"""Unit test file for team aggie_annihilators"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_aggie_annihilators(unittest.TestCase):
    """Test team aggie_annihilators PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
       """Test AU_MEDICARE functionality"""
        prefix = ['1234', '2345']
        middle = ['56789', '67890']
        suffix = ['1', '2']

        # build sample medicare numbers
        # positive test cases
        for p in prefix:
            for m in middle:
                for s in suffix:
                    medicare_text = f"My Medicare number is {p} {m} {s}"
                    result = analyze_text(medicare_text, ['AU_MEDICARE'])

                    # check entity_type for AU_MEDICARE
                    self.assertEqual(result[0].entity_type, 'AU_MEDICARE')

        # negative test case
        result = analyze_text('my medicare number is hidden', ['AU_MEDICARE'])
        self.assertListEqual(result, [])

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
