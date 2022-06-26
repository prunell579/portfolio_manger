

from typing import List


class Ticker:
    """
    Ticker is an abstract class, that should only be instanciated by Portfolio
    """
    def __init__(self, name, amount, number_of_shares) -> None:
        self.name = name
        self._amount_eur = amount
        self.number_of_shares = number_of_shares

    @property
    def amount_eur(self):
        return self._amount_eur

    @amount_eur.setter
    def amount_eur(self, value_euros):
        self._amount_eur = value_euros

class Portfolio:
    def __init__(self) -> None:
        self._tickers = []

    @property
    def tickers(self) -> List[Ticker]:
        return self._tickers

    def value(self) -> float:
        value = 0
        for ticker in self.tickers:
            value += ticker.amount_eur
        return value

    def ticker_names(self):
        names = []
        for ticker in self.tickers:
            names.append(ticker.name)
        return names

    def get_portfolio_ticker(self, ticker_name) -> Ticker:
        for ticker in self.tickers:
            if ticker_name == ticker.name:
                return ticker
        raise ValueError('The {} ticker does not exist in the portfolio'.format(ticker_name))


    def add_ticker(self, ticker_name, amount_euros, number_of_shares):
        if ticker_name in self.ticker_names():
            ticker = self.get_portfolio_ticker(ticker_name)
            ticker.amount_eur += amount_euros
            ticker.number_of_shares += number_of_shares
            return

        ticker = Ticker(ticker_name, amount_euros, number_of_shares)
        self._tickers.append(ticker)

    def tracker_value(self, ticker_name:str ) -> float:
        return self.get_portfolio_ticker(ticker_name).amount_eur

    def composition(self):
        portfolio_value = 0
        for ticker in self.tickers:
            portfolio_value += ticker.amount_eur

        composition = {}
        for ticker in self.tickers:
            composition[ticker.name] = ticker.amount_eur / portfolio_value

        return composition

    def summary(self):
        summary_format = "{:<10}{:<8}{:<10}\n"
        print(summary_format.format('Ticker', 'EUR', 'NofSH'))
        for ticker in self.tickers:
            print(summary_format.format(ticker.name, ticker.amount_eur,
                                        ticker.number_of_shares))


