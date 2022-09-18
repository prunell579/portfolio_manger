import model.supported_tickers as st
import datetime as dt
import model.portfolio_tracker_model as pt
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

def stock_last_price(ticker_name):
    
    ticker_name = yahoo_stock_ticker(ticker_name)

    # on a weekday I think this will give me yesterday's price and todays'
    data =  yf.download(ticker_name, period='1d')
    return data['Close'][0]
