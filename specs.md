Objective:

Build an application to visualize and track the performance of my stock porfolio.

Features wanted:
- Track the porfolio composition
- Track de portfolio value
- Track the portfolio performance
- Get the porfolio value, composition, performance over time
- Have a simulator module to compute the next buy operation from composition, 
total amount of money
- Add and stock new operations


----------------------
Code architecture

The model module will only stock information and do calculations as required.
It should interface with external services through another module (adapter)

External services: 
- portfolio information (in form of csv or xls)
- stock price from an API

The information will be shown either on graphs OR xls files

-data
    -*.xls, *.csv
-model
    portfolio_tracker_model
-view
    portfolio_tracker_console_view
-interfaces
    -yahoo_interface
    -xls_parser_interface
main


------------------
Model module

What classes should be defined inside this module? 
Portfolio
Tracker

what does a portfolio have? 
-list of tracker objects

-Methods
composition
value


what does a ticker have?
-name
-amount
-number of shares
-price (?)


The Ticker class can be an abstract class that needs a Portfolio object to be
instantiated. A Ticker object will always belong to a Portfolio.

This is not an abstract class, which is a class that cannot be directly instanciated,
but its children classes can. This results in classes that are not cohesive, but the module itself is cohesive.



