import datetime
from model import portfolio_tracker_model as pt
import random

PEA500 = 'PEA500'
PCEU = 'PCEU'
PAEEM = 'PAEEM'
BTC = 'BTC'

class PorfolioBuilder:
    def build(self, default_mode = False, manual_mode = False) -> pt.Portfolio:
        portfolio = pt.Portfolio()

        if default_mode or manual_mode:
            if default_mode:
                operations = self.operation_generator()
            if manual_mode:
                operations = self.make_current_pf_by_hand()

            for operation in operations:
                    portfolio.add_operation(operation=operation)

        else:
            ticker_names = [PEA500, PCEU]
            for ticker_name in ticker_names:
                for operation_number in range(1,6):
                    portfolio.add_operation(self.random_operation_generator(ticker_name))

        return portfolio


    def random_operation_generator(self, ticker_name):
        quantity = random.randint(1,50)
        gross_amount = random.uniform(15, 75)
        net_amount = random.uniform(0.96, 0.98) * gross_amount
        date = datetime.date(2022, random.randint(1,12), random.randint(1,28))

        return pt.Operation(ticker_name, quantity, gross_amount, net_amount, 
                        date)


    def operation_generator(self):
        """
        This function generates a set of 12 fixed operations
        """
        return [
        pt.Operation('PE500', 21, 786.32, 785.59, datetime.date(2022, 2, 21)),
        pt.Operation('PE500', 25, 1000.32, 998.59, datetime.date(2022, 3, 15)),
        pt.Operation('PE500', 19, 650.34, 640.59, datetime.date(2022, 4, 17)),

        pt.Operation('PCEU', 15, 453.32, 452.59, datetime.date(2022, 2, 21)),
        pt.Operation('PCEU', 18, 500.45, 499.59, datetime.date(2022, 3, 19)),
        pt.Operation('PCEU', 19, 515.45, 514.34, datetime.date(2022, 4, 15)),

        pt.Operation('PAEEM', 22, 320.32, 319.59, datetime.date(2022, 2, 23)),
        pt.Operation('PAEEM', 18, 280.32, 278.59, datetime.date(2022, 3, 23)),
        pt.Operation('PAEEM', 20, 260.32, 259.59, datetime.date(2022, 4, 23)),

        # pt.Operation('BTC', 1, 100.32, 100.00, datetime.date(2022, 5, 10)),
        # pt.Operation('BTC', 1, 102.32, 101.59, datetime.date(2022, 5, 10))
        ]

    def make_current_pf_by_hand(self):
        return [
        pt.Operation('PE500', 230, 7236.03, 7236.03, datetime.date(2022, 2, 21)),
        pt.Operation('PCEU', 171, 3961.215, 3961.215, datetime.date(2022, 2, 21)),
        pt.Operation('PAEEM', 117, 2292.174, 2292.147, datetime.date(2022, 2, 23)),
        ]