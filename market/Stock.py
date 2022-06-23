import csv
from market.PriceData import PriceData
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


class Stock:
    MOVING_AVERAGES = [50, 100, 200]

    def __init__(self, symbol):
        self.symbol = symbol
        self.price_data_df = self.fetch_price_data()
        self.price_data = self.parse_price_data()

    def moving_averages(self, df, col='Adj Close'):
        col_values = df[col]
        for avg in self.MOVING_AVERAGES:
            df[f"MA{avg}"] = col_values.rolling(window=avg).mean()

    @staticmethod
    def percent_change(df, col='Adj Close'):
        # daily returns
        daily_close = df[[col]]
        daily_pct_change = daily_close.pct_change()
        daily_pct_change.fillna(0, inplace=True)
        df['%Change'] = daily_pct_change
        # daily log returns
        daily_log_returns = np.log(daily_close.pct_change() + 1)
        daily_log_returns.fillna(0, inplace=True)
        df['%ChangeLog'] = daily_log_returns

    def fetch_price_data(self):
        df = yf.download(self.symbol, period="5y", progress=False).reset_index()
        self.moving_averages(df)
        self.percent_change(df)
        return df

    def parse_price_data(self):
        price_data = []
        columns = self.price_data_df.columns
        for idx, row in self.price_data_df.iterrows():
            ma = {}
            if len(columns) > 7:
                for x, y in row[7:].items():
                    if 'MA' in x:
                        ma.update({int(x.replace('MA', '')): y})
            data = PriceData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], ma)
            price_data.append(data)
        return price_data

    def read_static_price_data(self):
        price_data = []
        with open(f'data/{self.symbol}.csv') as f:
            reader = csv.reader(f)
            next(reader)  # headers
            for row in reader:
                data = PriceData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], {})
                price_data.append(data)
        return price_data

    def slice_price_data(self, start, end):
        return [x for x in self.price_data if start <= x.date <= end]

    def plot(self, col):
        self.price_data_df[col].plot(grid=True)
        plt.show()

    def hist(self, col):
        self.price_data_df[col].hist(bins=50)
        plt.show()

    def plot_price_data(self):
        self.plot('Close')
        self.hist('%Change')
        print(self.price_data_df['%Change'].describe())

        ma = [col for col in self.price_data_df.columns.values if "MA" in col]
        ma.append('Adj Close')
        self.plot(ma)
