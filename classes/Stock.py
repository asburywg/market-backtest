import csv
from classes.PriceData import PriceData


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_data = self.get_price_data()

    def get_price_data(self):
        price_data = []
        with open(f'data/{self.symbol}.csv') as f:
            reader = csv.reader(f)
            next(reader)  # headers
            for row in reader:
                data = PriceData(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                price_data.append(data)
        return price_data

    def slice_price_data(self, start, end):
        return [x for x in self.price_data if start <= x.date <= end]
