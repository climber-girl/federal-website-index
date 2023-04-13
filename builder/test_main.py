from main import format_gov_df, format_pulse_df, format_dap_df, format_other_df
import pandas
import unittest


class TestMain(unittest.TestCase):

    def test_format_gov_df(self):
        test_gov_df = pandas.DataFrame({
            'Domain Name': ['AMTRAKOIG.GOV'],
            'Domain Type': ['Federal - Executive'],
            'Agency': ['AMTRAK'],
            'Organization': ['Office of Inspector General'],
            'City': ['Washington'],
            'State': ['DC'],
            'Security Contact Email': ['(blank)']
        })

        expected_gov_df = pandas.DataFrame({
            'target_url': ['amtrakoig.gov', 'www.amtrakoig.gov'],
            'branch': ['Executive', 'Executive'],
            'agency': ['AMTRAK', 'AMTRAK'],
            'bureau': ['Office of Inspector General', 'Office of Inspector General'],
            'base_domain': ['amtrakoig.gov', 'amtrakoig.gov'],
            'source_list_federal_domains': ['TRUE', 'TRUE']
        })

        actual_gov_df = format_gov_df(test_gov_df)

        pandas.testing.assert_frame_equal(
            expected_gov_df.reset_index(drop=True),
            actual_gov_df.reset_index(drop=True)
        )

    def test_format_pulse_df(self):
        test_pulse_df = pandas.DataFrame({
            'Domain': ['18f.gov'],
            'Base Domain': ['18f.gov'],
            'URL': ['https://18f.gov'],
            'Agency': ['General Services Administration'],
            'Sources': ['dotgov'],
            'Compliant with M-15-13 and BOD 18-01': ['Yes'],
            'Enforces HTTPS': ['Yes'],
            'Strict Transport Security (HSTS)': ['Yes'],
            'Free of RC4/3DES and SSLv2/SSLv3': ['Yes'],
            '3DES': ['No'],
            'RC4': ['No'],
            'SSLv2': ['No'],
            'SSLv3': ['No'],
            'Preloaded': ['Yes']
        })

        expected_pulse_df = pandas.DataFrame({
            'target_url': ['18f.gov'],
            'base_domain': ['18f.gov'],
            'source_list_pulse': ['TRUE']
        })

        actual_pulse_df = format_pulse_df(test_pulse_df)

        pandas.testing.assert_frame_equal(
            expected_pulse_df.reset_index(drop=True),
            actual_pulse_df.reset_index(drop=True)
        )

    def test_format_dap_df(self):
        pass

    def test_format_other_df(self):
        pass

if __name__ == '__main__':
    unittest.main()
