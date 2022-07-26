import datetime
from model import portfolio_tracker_model as pt
import random

PEA500 = 'PEA500'
PCEU = 'PCEU'
PAEEM = 'PAEEM'
BTC = 'BTC'

class PorfolioBuilder:
    def build(self, default_mode = False) -> pt.Portfolio:
        portfolio = pt.Portfolio()

        if default_mode:
            portfolio.add_ticker(PEA500, 500, 20)
            portfolio.add_ticker(PCEU, 250, 15)
            portfolio.add_ticker(PAEEM, 150, 10)
            portfolio.add_ticker(BTC, 100, 0.23)

        else:
            ticker_names = [PEA500, PCEU]
            for ticker_name in ticker_names:
                for operation_number in range(1,6):
                    portfolio.add_operation(self.operation_generator(ticker_name))

        return portfolio


    def operation_generator(self, ticker_name):
        quantity = random.randint(1,50)
        gross_amount = random.uniform(15, 75)
        net_amount = random.uniform(0.96, 0.98) * gross_amount
        date = datetime.date(2022, random.randint(1,12), random.randint(1,28))

        return pt.Operation(ticker_name, quantity, gross_amount, net_amount, 
                        date)

