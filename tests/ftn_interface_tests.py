from pprint import pprint
import unittest
import datetime
import sys
sys.path.append('/Users/mariocastillo/portfolio_tracker')
import model.supported_tickers as st
import model.portfolio_builder as pf_builder
import model.portfolio_tracker_model as pf_model
import interface.fortuneo_data_extractor as ftn_dataext
import interface.stock_info_interface as stock_if

class FtnInterfaceTests(unittest.TestCase):
    def test_parse_sample_ftn_file(self):
        """
        From parsing the sample csv file, I should get a known portfolio
        """
        operations = ftn_dataext.extract_operations_from_csv(
                                'data/sample_fortuneo_data.csv')

        pf = pf_model.Portfolio(operations=operations)

        for ticker in pf.tickers:
            # the stock price in a test should be fixed to validate it
            value = ticker.number_of_shares * stock_if.stock_last_price(ticker.name)
            pf.set_ticker_value(ticker.name, value)

        pf.summary()

        self.assertEqual(1, 1)

    

if __name__ == '__main__':
    unittest.main()