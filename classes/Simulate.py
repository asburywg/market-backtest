import datetime
import classes.Stock as Stock
from classes.Trade import Trade


class Simulate:
    def __init__(self, start: datetime.date, end: datetime.date, stock: Stock, strategy):
        self.data = stock.slice_price_data(start, end)
        self.strategy = strategy
        self.principal = 1000
        self.compound = True
        self.simulate()

    def simulate(self):
        trades = []
        for i in range(len(self.data) - 1):
            buy = self.data[self.strategy.buy_index]
            sell = self.data[self.strategy.sell_index]

            # print(f"BUY {buy}")
            # print(f"SELL {sell}")

            principal = trades[-1].proceeds if len(trades) > 0 else self.principal if self.compound else self.principal
            trade = Trade(principal)
            if buy_price := self.strategy.buy_trigger(buy):
                trade.buy(buy_price, buy)
            if sell_price := self.strategy.sell_trigger(sell):
                trade.sell(sell_price, sell)

            print(f"{sell.date} ${round(trade.proceeds, 2)} ({round((trade.proceeds - self.principal) / self.principal * 100, 2)}%)")
            trades.append(trade)

            self.strategy.increment()
