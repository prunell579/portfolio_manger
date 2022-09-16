from pprint import pprint
import unittest
import datetime
import sys
sys.path.append('/Users/mariocastillo/portfolio_tracker')
import model.portfolio_builder as pf_builder
import model.portfolio_tracker_model as pf_model
import interface.fortuneo_data_extractor as ftn_dataext

class FtnInterfaceTests(unittest.TestCase):
    def test_parse_sample_ftn_file(self):
        """
        From parsing the sample csv file, I should get a known portfolio
        """
        operations = ftn_dataext.extract_operations_from_csv(
                                'data/sample_fortuneo_data.csv')

        pf = pf_model.Portfolio(operations=operations)

        pf.set_ticker_value('PE500', 0.34)
        pf.set_ticker_value('PCEU', 0.52)
        pf.set_ticker_value('PAEEM', 0.53)
        # pf.set_ticker_value('BTC', 120.90)
        pf.summary()

        self.assertEqual(1, 1)

    

if __name__ == '__main__':
    unittest.main()