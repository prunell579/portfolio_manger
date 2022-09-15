
from datetime import date
from pprint import pprint
import sys
# sys.path.append('/Users/mariocastillo/portfolio_tracker')
sys.path.append('/Users/marieljc/Documents/mco_temp')
import model.portfolio_builder as pf_builder
import model.portfolio_tracker_model as pf_model

if __name__ == '__main__':
        # portfolio = pf_builder.PorfolioBuilder().build(default_mode=True)

        # operation_1 = pf_model.Operation('PE500', 21, 786.32, 785.59, date(2022, 2, 21))
        # operation_2 = pf_model.Operation('PCEU', 15, 453.32, 452.59, date(2022, 3, 21))
        # operation_3 = pf_model.Operation('PAAEM', 22, 320.32, 319.59, date(2022, 4, 23))
        # operation_4 = pf_model.Operation('BTC', 1, 200.32, 200.59, date(2022, 5, 10))

        portfolio = pf_model.Portfolio()
        # portfolio.add_operation(operation=operation_1)
        # portfolio.add_operation(operation=operation_2)
        # portfolio.add_operation(operation=operation_3)
        # portfolio.add_operation(operation=operation_4)

        # portfolio.summary()

        # portfolio.set_ticker_value('PE500', 800.23)
        # print(portfolio.ticker_value('PE500'))

        operations = pf_builder.PorfolioBuilder().operation_generator()

        for operation in operations:
                portfolio.add_operation(operation=operation)

        portfolio.set_ticker_value('PE500', 2500.34)
        portfolio.set_ticker_value('PCEU', 1488.52)
        portfolio.set_ticker_value('PAAEM', 888.53)
        portfolio.set_ticker_value('BTC', 120.90)

        portfolio.summary()