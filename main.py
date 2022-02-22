import datetime
from dateutil.relativedelta import relativedelta

from classes.Simulate import Simulate
from classes.Stock import Stock
from strategies.BuyCloseSellOpen import BuyCloseSellOpen


def main():
    # load price data
    stock = Stock("VOO")

    end = datetime.date.today()
    start = end - relativedelta(years=1)

    bcso = BuyCloseSellOpen()
    Simulate(start, end, stock, bcso)


if __name__ == '__main__':
    main()
