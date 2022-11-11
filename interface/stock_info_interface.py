import model.supported_tickers as st
import datetime as dt
from model.portfolio_tracker_model import Portfolio
import yfinance as yf

def yahoo_stock_ticker(ticker_name):
    if ticker_name == st.PE500 or ticker_name == st.PCEU or ticker_name == st.PAEEM:
        return ticker_name + '.PA' 
    else:
        raise ValueError('Ticker {} not supported'.format(ticker_name))

def stock_close_price(ticker_name, date: dt.datetime):
    ticker_name = yahoo_stock_ticker(ticker_name)

    date = date + dt.timedelta(hours=12)
    end_date = date + dt.timedelta(days=1)
    data = yf.download(ticker_name, start=date, end=end_date)

    return data['Close'][0]

def stock_last_prices(ticker_names: list):
    """Returns a dictionary containing the ticker names as key values and the last stock price as 
    items
    """
    stock_prices = {}
    for ticker_name in ticker_names:
        ticker_yahoo_name = yahoo_stock_ticker(ticker_name)
        data =  yf.download(ticker_yahoo_name, period='1d')
        stock_prices[ticker_name] = data['Close'][0]
    return stock_prices

def portfolio_last_stock_prices(pf: Portfolio):
    return stock_last_prices(pf.ticker_names())

if __name__ == '__main__':
    print(stock_last_prices([st.PE500]))