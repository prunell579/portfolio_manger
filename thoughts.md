I have to rethink the code a bit. I already worked on initalizing 
the porfolio and tickers. Now, I have to make it in a way such that
I can:

-> load my portfolio
-> add new operations
-> generate useful insights

Again, I could always initialize the code each time I execute it, but that's not really ok.


# 9/9/22
Last time, I've fixed the fact that VALUE and INVESTMENT are not the same attributes for a Ticker object.

VALUE is actually the only attribute that cannot be fed to a Ticker object through an Operation. Therefore, it must be fed independently. As of today, I can think of two ways of doing this:

Manually set the value
Eat a spreadsheet from fortuneo
Connect to a stock market platform and estimate the value throigh stock price and number of shares.


#End of 9/9 session
The summary is now printed with better details. I have implemented the notion of GAIN and PERF to the portfolio.

I think now could be a good time to write the scripts that eats the CSV and creates the corresponding portfolio. 

Tests are also broken and they need to be fixed.
