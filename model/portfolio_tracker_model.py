

import datetime
from typing import List


class Ticker:
    """
    Ticker is an abstract class, that should only be instanciated by Portfolio
    """
    def __init__(self, name, amount, number_of_shares, value = None) -> None:
        self.name = name
        self._investment = amount
        self.number_of_shares = number_of_shares
        self._value = None

    @property
    def investment(self):
        return self._investment

    @investment.setter
    def investment(self, value_euros):
        self._investment = value_euros

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_euros):
        self._value = value_euros


    # Methods
    def gain(self, mode='gain'):
        if not self.value:
            return 'NaN'

        gain = self.value - self.investment
        if mode == 'gain':
            return gain
        
        if mode == 'perf':
            return 1e2 * gain / self.investment

        # handle excepciton for non valid params


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
    def __init__(self, operations=None):
        self._tickers = []
        self._operations = []

        if operations:
            for operation in operations:
                self.add_operation(operation=operation)


    @property
    def tickers(self) -> List[Ticker]:
        return self._tickers

    @property
    def operations(self) -> List[Operation]:
        return self._operations

    def investment(self) -> float:
        investment = 0
        for ticker in self.tickers:
            investment += ticker.investment
        return investment

    def value(self) -> float:
        value = 0
        for ticker in self.tickers:
            value += ticker.value
        return value

    def gain(self, mode='gain'):
        # duplicated code!
        if not self.value():
            return 'NaN'

        gain = self.value() - self.investment()
        if mode == 'gain':
            return gain
        
        if mode == 'perf':
            return 1e2 * gain / self.investment()

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
            ticker.investment += amount_euros
            ticker.number_of_shares += number_of_shares
            return

        ticker = Ticker(ticker_name, amount_euros, number_of_shares)
        self._tickers.append(ticker)

    def set_ticker_investment(self, ticker_name: str, investment_value: float):
        self.get_portfolio_ticker(ticker_name).investment = investment_value

    def ticker_investment(self, ticker_name:str ) -> float:
        return self.get_portfolio_ticker(ticker_name)._investment

    def set_ticker_value(self, ticker_name, value):
        self.get_portfolio_ticker(ticker_name)._value = value

    def ticker_value(self, ticker_name: str):
        return self.get_portfolio_ticker(ticker_name).value

    def add_operation(self, ticker_name='', quantity=0, 
                    gross_amount=0.0, net_amount=0.0, 
                    date=datetime.date(2000, 1, 1),
                    operation=None):

        if operation:
            ticker_name = operation.ticker_name
            quantity = operation.quantity
            gross_amount = operation.gross_amount
            net_amount = operation.net_amount
            date = operation.date

        else:
            operation = Operation(ticker_name, quantity, gross_amount, net_amount,
                                date)

        self._operations.append(operation)
        self.add_ticker(ticker_name, net_amount, quantity)

    def composition(self):
        portfolio_value = self.portfolio_investment()

        composition = {}
        for ticker in self.tickers:
            try:
                composition[ticker.name] = ticker.investment / portfolio_value
            except:
                return 'NaN'

        return composition

    def ticker_composition(self, ticker_name):
        portfolio_value = self.portfolio_investment()
        try:
            return self.get_portfolio_ticker(ticker_name).investment / portfolio_value
        except:
            return 'NaN'
        

    # why can't I use the property? 
    def portfolio_investment(self) -> float:
        portfolio_value = 0
        for ticker in self.tickers:
            portfolio_value += ticker.investment

        return portfolio_value

    def ticker_gain(self, ticker_name: str, mode='gain') -> float:
        return self.get_portfolio_ticker(ticker_name).gain(mode)

    def summary(self):
        summary_format = "{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n"
        print(summary_format.format('Ticker', 'VAL', 'INV', 'PERF', 'GAIN',
                                    'QTY', 'COMP'))
        for ticker in self.tickers:

            ticker_comp = self.ticker_composition(ticker.name)
            ticker_gain = self.ticker_gain(ticker.name)
            ticker_perf = self.ticker_gain(ticker.name, mode='perf')
            print(summary_format.format(ticker.name, ticker.value,
                                        '{:.2f}'.format(ticker.investment), 
                                        '{:.2f}'.format(ticker_perf),
                                        '{:.2f}'.format(ticker_gain),
                                        ticker.number_of_shares,
                                        '{:.2f}'.format(ticker_comp)))

        print("-------------------------------------------------------------\n")
        total_value = self.value()
        total_investment = self.investment()
        gain = self.gain()
        perf = self.gain(mode='perf')
        print(summary_format.format('TOTAL',
                                    '{:.2f}'.format(self.value()),
                                    '{:.2f}'.format(self.investment()),
                                    '{:.2f}'.format(self.gain(mode='perf')),
                                    '{:.2f}'.format(self.gain()),
                                    '--',
                                    '{:.2f}'.format(1)))



