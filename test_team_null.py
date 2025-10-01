"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        prefix = ['111', '222']
        middle = ['22', '33', '44']
        suffix = ['3434', '5454']

        # build sample ssn
        # positive test cases
        for p in prefix:
            for m in middle:
                for s in suffix:
                    ssn_text = f'my ssn is {p}-{m}-{s}'
                    result = analyze_text(ssn_text, ['US_SSN'])
                    # check entity_type for US_SSN
                    self.assertEqual(result[0].entity_type, 'US_SSN')

        # negative test case
        result = analyze_text('my ssn is hidden', ['US_SSN'])
        self.assertListEqual(result, [])


if __name__ == '__main__':
    unittest.main()
