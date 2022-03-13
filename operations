import csv 
import datetime
from pprint import pprint

class Operation(object):
    DATE_COLUMN = 3
    QTY_COLUMN = 4
    PRICE_COLUMN = 5
    GROSS_AMOUNT_COLUMN = 6
    COMISSION_COLUMN = 7
    NET_AMOUNT_COLUMN = 8

    PCEEU = 'PCEU'
    PE500 = 'PE500'
    PAEEM = 'PAEEM'


    def __init__(self, row_raw_data=None) -> None:

        if row_raw_data:
            self.ticker = self.ticker_from_raw_data(row_raw_data[0])
            self.date = row_raw_data[self.DATE_COLUMN]
            self.quantity = int(float(row_raw_data[self.QTY_COLUMN]))
            self.ticker_price = float(row_raw_data[self.PRICE_COLUMN])
            self.gross_amount = abs(float(row_raw_data[self.GROSS_AMOUNT_COLUMN]))
            self.comission = abs(float(row_raw_data[self.COMISSION_COLUMN]))
            self.net_amount = abs(float(row_raw_data[self.NET_AMOUNT_COLUMN]))
            self.id = self.generate_operation_id()

        else:
            self.date = None
            self.ticker = None
            self.ticker_price = None
            self.quantity = None
            self.gross_amount = None
            self.net_amount = None
            self.comission = None
            self.id = None

    def ticker_from_raw_data(self, raw_data):
        if 'S&P 500' in raw_data:
            return self.PE500
        if "EUROPE" in raw_data:
            return self.PCEEU
        if 'EMERGING' in raw_data:
            return self.PAEEM
        else:
            raise ValueError('Tracker not compatible with list')

    def generate_operation_id(self):
        return (self.ticker + str(self.date) + str(self.quantity) + 
                str(self.gross_amount))


class Ticker(object):
    """
    Class holding detailed data of a ticker. Should be used within a Portfolio
    object
    """

    def __init__(self, operation=None, ticker_name=None) -> None:
        self.name = ticker_name
        self.value = None
        self.number_of_shares = 0
        self.gross_investment = 0
        self.net_investment = 0
        self.comissions = 0
        self.performance = None
        self.gain = None
        self.operations = []

        if operation:
            self.name = operation.ticker
            self.number_of_shares = operation.quantity
            self.gross_investment = operation.gross_amount
            self.net_investment = operation.net_amount
            self.comissions = operation.comission
            self.operations.append(operation)


    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self, value):
    #     self.name = value

    # @property
    # def operations(self):
    #     return self.operations


    def add_operation(self, operation: Operation):
        self.operations.append(operation)
        self.number_of_shares += operation.quantity
        self.gross_investment += operation.gross_amount
        self.net_investment += operation.net_amount
        self.comissions += operation.comission

class Portfolio(Ticker):

    def __init__(self, operations=None) -> None:
        super().__init__()

        self.ticker_data = {}

        if operations:
            # parse .csv and create ticker objects
            with open(operations, 'r', encoding='ISO-8859-1') as f:
                for row in f.readlines()[1:]:
                    row_data = row.split(sep=';')
                    operation = Operation(row_data)

                    ticker_name = operation.ticker
                    if ticker_name not in self.ticker_data.keys():
                        # initalize ticker and store it in dict
                        self.ticker_data[ticker_name] = Ticker(operation)

                    else:
                        self.get_ticker(ticker_name).add_operation(operation)

            self.update_portfolio()


    def get_ticker(self, ticker_name) -> Ticker:
        try:
            return self.ticker_data[ticker_name]
        except KeyError:
            raise KeyError('{} ticker does not exist in porfolio'.format(ticker_name))

    def ticker_names(self):
        return self.ticker_data.keys()

    def update_net_investment(self):
        for ticker_name in self.ticker_data.keys():
            self.net_investment += self.get_ticker(ticker_name).net_investment

    def update_portfolio(self):
        for ticker_name in self.ticker_data.keys():
            self.number_of_shares += self.get_ticker(ticker_name).net_investment
            self.net_investment += self.get_ticker(ticker_name).net_investment
            self.gross_investment += self.get_ticker(ticker_name).gross_investment
            self.comissions += self.get_ticker(ticker_name).gross_investment


if __name__ == '__main__':
    datafile_path = 'data/HistoriqueOperationsBourse_015207052916_du_01_01_2021_au_01_03_2022.csv'
    portfolio = Portfolio(datafile_path)

    print("net investment of portfolio: {}EUR".format(portfolio.net_investment))

    for ticker_name in portfolio.ticker_names():
        ticker = portfolio.get_ticker(ticker_name)
        print("net investment {}: {}EUR".format(ticker.name, ticker.net_investment))
        # print("gross investment {}: {}EUR".format(portfolio.name, portfolio.gross_investment))
        # print("comissions {}: {}EUR".format(portfolio.name, portfolio.comissions))
        # print("number of shares {}: {}".format(portfolio.name, portfolio.number_of_shares))


        # ideally, what I would want to do is:
        # 1. load portfolio
        # 2. add operations if necessary
        # 3. add the simulator module


