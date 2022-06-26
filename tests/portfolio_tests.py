import unittest

import sys
import os
sys.path.append('/Users/mariocastillo/portfolio_tracker')
import model.portfolio_builder as pf_builder


"""
Given that I have
500 EUR of PEA500
250 EUR of PECEAU
150 EUR of PCEEAM
100 EUR of BTC

Then my portfolio composition should be:
PEA500 - 50%
PCEU - 25%
PAEEM - 15%
BTC - 10%
"""

PEA500 = 'PEA500'
PCEU = 'PCEU'
PAEEM = 'PAEEM'
BTC = 'BTC'

class PortfolioTests(unittest.TestCase):

    def test_add_ticker(self):
        """
        Given that I don't have a portfolio, I'd like to create one with the 
        following characteristics:

        500 EUR of PEA500
        250 EUR of PECEAU
        150 EUR of PCEEAM
        100 EUR of BTC
        """

        portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)

        tickers = portfolio.tickers

        self.assertEqual(len(tickers), 4)

        ticker_names = []
        for ticker in tickers:
            ticker_names.append(ticker.name)

        self.assertIn(PEA500, ticker_names)
        self.assertIn(PCEU, ticker_names)
        self.assertIn(PAEEM, ticker_names)
        self.assertIn(BTC, ticker_names)

        for ticker in tickers:
            if ticker.name == PEA500:
                self.assertEqual(ticker.amount_eur, 500)
                self.assertEqual(ticker.number_of_shares, 20)
            if ticker.name == PCEU:
                self.assertEqual(ticker.amount_eur, 250)
                self.assertEqual(ticker.number_of_shares, 15)
            if ticker.name == PAEEM:
                self.assertEqual(ticker.amount_eur, 150)
                self.assertEqual(ticker.number_of_shares, 10)
            if ticker.name == BTC:
                self.assertEqual(ticker.amount_eur, 100)
                self.assertEqual(ticker.number_of_shares, 0.23)


    def test_portfolio_composition(self):
        portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)

        composition = portfolio.composition()

        for key, value in composition.items():
            if key == PEA500:
                self.assertEqual(0.5, value)
            if key == PCEU:
                self.assertEqual(0.25, value)
            if key == PAEEM:
                self.assertEqual(0.15, value)
            if key == BTC:
                self.assertEqual(0.1, value)

    def test_add_to_existing_portfolio(self):
        portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)
        portfolio.add_ticker(PEA500, 1000, 50)

        composition = portfolio.composition()

        for key, value in composition.items():
            if key == PEA500:
                self.assertEqual(0.75, value)
            if key == PCEU:
                self.assertEqual(0.125, value)
            if key == PAEEM:
                self.assertEqual(0.075, value)
            if key == BTC:
                self.assertEqual(0.05, value)


    def test_portfolio_value(self):
        portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)

        self.assertEqual(1000, portfolio.value())

        portfolio.add_ticker(PEA500, 222, 10)
        self.assertEqual(1222, portfolio.value())


    def test_tracker_value(self):
        portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)

        self.assertEqual(portfolio.tracker_value(PEA500), 500)
        self.assertEqual(portfolio.tracker_value(PCEU), 250)
        self.assertEqual(portfolio.tracker_value(PAEEM), 150)
        self.assertEqual(portfolio.tracker_value(BTC), 100)

        portfolio.add_ticker(PCEU, 222, 10)
        self.assertEqual(portfolio.tracker_value(PCEU), 472)

        with self.assertRaises(ValueError):
            portfolio.tracker_value('dummy_tracker')

    

if __name__ == '__main__':
    unittest.main()