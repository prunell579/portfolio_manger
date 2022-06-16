
class Ticker:
    """
    Ticker is an abstract class, that should only be instanciated by Portfolio
    """
    def __init__(self, name, amount, number_of_shares) -> None:
        self.name = name
        self.amount_eur = amount
        self.number_of_shares = number_of_shares

class Portfolio:
    def __init__(self) -> None:
        self.value = 0
        self._tickers = []

    @property
    def tickers(self):
        return self._tickers

    def add_ticker(self, ticker_name, amount_euros, number_of_shares):
        ticker = Ticker(ticker_name, amount_euros, number_of_shares)
        self._tickers.append(ticker)

    def composition(self):
        portfolio_value = 0
        for ticker in self._tickers:
            portfolio_value += ticker.amount_eur

        composition = {}
        for ticker in self._tickers:
            composition[ticker.name] = ticker.amount_eur / portfolio_value

        return composition



