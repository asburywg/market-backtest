class BuyOpenSellClose:
    def __init__(self):
        self.cadence = "DAILY"
        self.name = "Buy Open, Sell Close"
        self.buy_index = 0
        self.sell_index = 0

    def increment(self):
        self.buy_index += 1
        self.sell_index += 1

    @staticmethod
    def buy_trigger(price):
        return price.open

    @staticmethod
    def sell_trigger(price):
        return price.close
