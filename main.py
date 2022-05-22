from classes.Manager import Manager


def main():
    years_back = 2
    symbols = ["VOO", "GOOGL", "FB", "AAPL", "MSFT"]
    for sym in symbols:
        Manager(sym, years_back).simulate_strategies()

    eth = Manager("ETH-USD", years_back)
    eth.simulate_strategies()
    eth.stock.plot_price_data()


if __name__ == '__main__':
    main()
