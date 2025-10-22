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
        aba = 'my aba is 121000358'  # BoA
        result = analyze_text(aba, ['ABA_ROUTING_NUMBER'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entity_type, 'ABA_ROUTING_NUMBER')

        # Try without 'ACN' prefix
        aba_no_prefix = 'My routing number is 121042882'  # Wells Fargo
        result = analyze_text(aba_no_prefix, ['ABA_ROUTING_NUMBER'])
        self.assertEqual(len(result), 1)

        # negative test case
        result = analyze_text('Routing is required', ['ABA_ROUTING_NUMBER'])
        self.assertEqual(result, [])

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        # Positive test case - basic format
        acn = 'my australian company number is ACN 010 499 966'
        result = analyze_text(acn, ['AU_ACN'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entity_type, 'AU_ACN')
        
        # Try without 'ACN' prefix
        acn_no_prefix = 'my australian company number is 010 499 966'
        result = analyze_text(acn_no_prefix, ['AU_ACN'])
        self.assertEqual(len(result), 1)

        # negative test case
        result = analyze_text('ACN is required', ['AU_ACN'])
        self.assertEqual(result, [])

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
