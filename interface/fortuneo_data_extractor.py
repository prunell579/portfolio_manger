import csv
import datetime
from model.portfolio_tracker_model import Operation

TICKER_NAME = 0
OPERATION_DATE = 3
QUANTITY = 4
GROSS_INVESTMENT = 6
NET_INVESTMENT = 8

def extract_operations_from_csv(path_to_csv):

    operations = []
    with open(path_to_csv, encoding='ISO-8859-1') as datafile:
        data_reader = csv.reader(datafile, delimiter=';')
        next(data_reader)
        for row in data_reader:
            ticker_name = row[TICKER_NAME]
            operation_date = row[OPERATION_DATE]
            quantity = row[QUANTITY]
            net_investment = row[NET_INVESTMENT]
            gross_investment = row[GROSS_INVESTMENT]

            # post treatment of raw data
            ticker_name = alias_from_raw_ticker(ticker_name)
            operation_date = datetime.datetime.strptime(operation_date, '%d/%m/%Y')
            quantity = int(float(quantity))
            net_investment = abs(float(net_investment))
            gross_investment = abs(float(gross_investment))

            operations.append(Operation(ticker_name, quantity, gross_investment,
                                        net_investment, operation_date))

    return operations


def alias_from_raw_ticker(raw_ticker_name):
    if raw_ticker_name == 'AMUNDI ETF PEA S&P 500 UCITS ETF - EUR':
        alias = 'PE500'
    elif raw_ticker_name == 'AMUNDI ETF PEA MSCI EUROPE UCITS ETF - EUR':
        alias = 'PCEU'
    elif raw_ticker_name == 'AMUNDI ETF PEA MSCI EMERGING MARKETS UCITS ETF - EUR':
        alias = 'PAEEM'
    else:
        error_string = 'alias for {} not defined'.format(raw_ticker_name)
        raise ValueError(error_string)

    return alias
