import datetime
from dateutil.relativedelta import relativedelta

from market.Simulate import Simulate
from market.Stock import Stock
from strategies.BuyAndHold import BuyAndHold
from strategies.BuyCloseSellOpen import BuyCloseSellOpen
from strategies.BuyOpenSellClose import BuyOpenSellClose


class Manager:

    def __init__(self, symbol, years_back=5):
        self.stock = Stock(symbol)
        self.end = datetime.date.today()
        self.start = self.end - relativedelta(years=years_back)

    def simulate_strategies(self):
        print(f"********** {self.stock.symbol} **********")
        strategies = [BuyAndHold(), BuyCloseSellOpen(), BuyOpenSellClose()]
        for strat in strategies:
            Simulate(self.start, self.end, self.stock, strat)
