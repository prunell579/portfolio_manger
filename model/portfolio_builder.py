import portfolio_tracker_model as pt

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

        return portfolio

