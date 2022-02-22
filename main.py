from classes.Manager import Manager


def main():
    yr = 2
    Manager("VOO", yr).simulate_strategies()
    Manager("GOOGL", yr).simulate_strategies()
    Manager("FB", yr).simulate_strategies()
    Manager("AAPL", yr).simulate_strategies()
    Manager("MSFT", yr).simulate_strategies()


if __name__ == '__main__':
    main()
