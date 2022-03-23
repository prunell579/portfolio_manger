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
            self.ticker_name = self.ticker_from_raw_data(row_raw_data[0])
            self.date = row_raw_data[self.DATE_COLUMN]
            self.quantity = int(float(row_raw_data[self.QTY_COLUMN]))
            self.ticker_price = float(row_raw_data[self.PRICE_COLUMN])
            self.gross_amount = abs(float(row_raw_data[self.GROSS_AMOUNT_COLUMN]))
            self.comission = abs(float(row_raw_data[self.COMISSION_COLUMN]))
            self.net_amount = abs(float(row_raw_data[self.NET_AMOUNT_COLUMN]))
            self.id = self.generate_operation_id()

        else:
            self.date = None
            self.ticker_name = None
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
        return (self.ticker_name + str(self.date) + str(self.quantity) + 
                str(self.gross_amount))


class Ticker(object):
    """
    Class holding detailed data of a ticker. Should be used within a Portfolio
    object
    """

    def __init__(self, ticker_name=None) -> None:
        self.name = ticker_name
        self.number_of_shares = 0
        self.position = 0

    def add_shares(self, share_number):
        self.number_of_shares += share_number

class Portfolio(object):

    def __init__(self, operations=None) -> None:
        self.value = None
        self.number_of_shares = 0
        self.composition = {}
        self.gross_investment = 0
        self.net_investment = 0
        self.comissions = 0
        self.performance = None
        self.gain = None
        self.operations = []

        self.ticker_data = {}

        if operations:
            """
            Initialize Porfolio instance from data of a .csv file
            """
            # parse .csv and create ticker objects
            with open(operations, 'r', encoding='ISO-8859-1') as f:
                for row in f.readlines()[1:]:
                    row_data = row.split(sep=';')
                    operation = Operation(row_data)

                    ticker_name = operation.ticker_name

                    if ticker_name not in self.ticker_data.keys():
                        self.ticker_data[ticker_name] = Ticker(operation.ticker_name)
                    
                    self.add_operation(operation)


    def add_operation(self, operation: Operation): 
        self.operations.append(operation)
        self.number_of_shares += operation.quantity
        self.gross_investment += operation.gross_amount
        self.net_investment += operation.net_amount
        self.comissions += operation.comission

        self.ticker_data[operation.ticker_name].add_shares(operation.quantity)

    def set_portfolio_value(self, value_summary=None):
        # Fortuneo API to track portfolio value?
        value_pe500 = 4338.906
        value_pceu = 2467.5
        value_paeem = 1632.92

        self.value =  value_paeem + value_pceu + value_pe500

        self.ticker_data[Operation.PE500].position = value_pe500
        self.ticker_data[Operation.PCEEU].position = value_pceu
        self.ticker_data[Operation.PAEEM].position = value_paeem

        self.gain = self.value - self.net_investment
        self.performance = 100 * self.gain / self.value
        self.set_composition()

    def get_ticker(self, ticker_name) -> Ticker:
        try:
            return self.ticker_data[ticker_name]
        except KeyError:
            raise KeyError('{} ticker does not exist in porfolio'.format(ticker_name))

    def ticker_names(self):
        return self.ticker_data.keys()

    def set_composition(self) -> dict:
        self.composition = {}
        for ticker in self.ticker_data.values():
            ticker_percentage = 100 * (ticker.position) / self.value
            self.composition[ticker.name] = ticker_percentage

    def estimate_composition(self, tickers: list, ticker_prices: list, 
                            share_numbers: list, detailed_cost=True):

        provisional_positions = {}
        operation_cost = 0

        for ticker, ticker_price, share_number in zip(tickers, ticker_prices,
                                                    share_numbers):
            try:
                provisional_positions[ticker] = self.ticker_data[ticker].position + ticker_price * share_number
            except KeyError:
                provisional_positions[ticker] = ticker_price * share_number

            operation_cost += ticker_price * share_number

        for ticker in self.ticker_data.keys():
            if ticker not in tickers:
                provisional_positions[ticker] = self.ticker_data[ticker].position

        provisional_composition = {}
        provisional_value = self.value + operation_cost

        for ticker, provisional_position in provisional_positions.items():
            provisional_composition[ticker] = round(100 * provisional_position / provisional_value, 2)

        pprint(provisional_composition)

        if detailed_cost:
            for ticker, ticker_price, share_number in zip(tickers, ticker_prices,
                                                        share_numbers):
                pprint('operation cost for {}: {}'.format(ticker,
                                                          ticker_price * share_number))
        pprint('total operation cost: {}'.format(operation_cost))


if __name__ == '__main__':
    datafile_path = 'data/HistoriqueOperationsBourse_015207052916_du_01_01_2021_au_01_03_2022.csv'
    portfolio = Portfolio(datafile_path)
    portfolio.set_portfolio_value()

    tickers_to_buy = [Operation.PE500, Operation.PCEEU, Operation.PAEEM, 'BTC']
    # API to track stock prices ?
    ticker_prices = [30.37, 23.51, 20.32, 35188.06]
    share_amounts = [16, 13, 10, 0.0085]
    portfolio.estimate_composition(tickers_to_buy, ticker_prices, share_amounts)
    pass

        # interactve session example:
        # start python
        # import the portfolio package
        # load a portfolio file

        # to create a porfolio file
        # start package, import the portfolio package
        # call Portfolio(csv_file)

        # ideally, what I would want to do is:
        # 1. load portfolio
        # 2. add operations if necessary
        # 3. add the simulator module


