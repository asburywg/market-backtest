class BuyAndHold:
    def __init__(self):
        self.cadence = "LIFETIME"
        self.name = "Buy and Hold"
        self.buy_index = 0
        self.sell_index = -1

    @staticmethod
    def buy_trigger(price):
        return price.close

    @staticmethod
    def sell_trigger(price):
        return price.close
