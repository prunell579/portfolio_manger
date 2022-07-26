

import datetime
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

class Operation:
    def __init__(self, ticker_name, quantity, gross_amount, net_amount, 
                date: datetime):
        self.ticker_name = ticker_name
        self.quantity = quantity
        self.gross_amount = gross_amount
        self.net_amount = net_amount
        self.date = date
        # self.id = self.generate_operation_id()


class Portfolio:
    def __init__(self) -> None:
        self._tickers = []
        self._operations = []

    @property
    def tickers(self) -> List[Ticker]:
        return self._tickers

    @property
    def operations(self) -> List[Operation]:
        return self._operations

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

    # should be pvt
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

    def add_operation(self, ticker_name='', quantity=0, 
                    gross_amount=0.0, net_amount=0.0, 
                    date=datetime.date(2000, 1, 1),
                    operation=None):

        if not operation:
            operation = Operation(ticker_name, quantity, gross_amount, net_amount,
                                date)

        self._operations.append(operation)
        self.add_ticker(ticker_name, net_amount, quantity)

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




