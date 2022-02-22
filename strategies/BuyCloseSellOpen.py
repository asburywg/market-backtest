class BuyCloseSellOpen:
    def __init__(self):
        self.cadence = "DAILY"
        self.buy_index = 0
        self.sell_index = 1

    def increment(self):
        self.buy_index += 1
        self.sell_index += 1

    @staticmethod
    def buy_trigger(price):
        return price.close

    @staticmethod
    def sell_trigger(price):
        return price.open
