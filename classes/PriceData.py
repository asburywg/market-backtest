import datetime


def parse_date(date):
    if type(date) == str:
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    return date.date()


class PriceData:
    def __init__(self, date, open, high, low, close, adj_close, volume, moving_averages):
        self.date = parse_date(date)
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.adj_close = float(adj_close)
        self.volume = int(volume)
        self.moving_averages = moving_averages

    def __repr__(self):
        return f"{self.date}: {{ open: ${round(self.open, 2)}, close: ${round(self.close, 2)}, MA: {self.moving_averages} }}"
