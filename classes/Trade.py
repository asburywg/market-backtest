class Trade:
    def __init__(self, principal):
        self.principal = principal
        self.proceeds = None
        self.shares = None
        self.buy_price = None
        self.buy_data = None
        self.sell_price = None
        self.sell_data = None
        self.profit_loss = None
        self.percent = None

    def buy(self, price, data):
        self.buy_price = price
        self.shares = self.principal / price
        self.buy_data = data

    def sell(self, price, data):
        self.sell_price = price
        self.proceeds = price * self.shares
        self.sell_data = data
        self.profit_loss_calc()

    def profit_loss_calc(self):
        self.profit_loss = self.proceeds - self.principal
        self.percent = self.profit_loss / self.principal

    def __repr__(self):
        return f"Principal: ${round(self.principal, 2)} Proceeds: ${round(self.proceeds, 2)} // ${round(self.profit_loss, 2)} ({round(self.percent * 100, 2)}%)"
