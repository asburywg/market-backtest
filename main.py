import datetime
from dateutil.relativedelta import relativedelta

from classes.Simulate import Simulate
from classes.Stock import Stock
from strategies.BuyAndHold import BuyAndHold
from strategies.BuyCloseSellOpen import BuyCloseSellOpen
from strategies.BuyOpenSellClose import BuyOpenSellClose


def main():
    # load price data
    stock = Stock("VOO")

    end = datetime.date.today()
    start = end - relativedelta(years=5)

    bcso = BuyCloseSellOpen()
    bnh = BuyAndHold()
    bosc = BuyOpenSellClose()

    Simulate(start, end, stock, bnh)
    Simulate(start, end, stock, bcso)
    Simulate(start, end, stock, bosc)


if __name__ == '__main__':
    main()
