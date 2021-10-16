import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
import yfinance as yf


class Stock:
    def __init__(self, ticker, **kwargs):
        self.time_range = kwargs['t_range']
        self.time_format = kwargs['t_format']

        # in the format of the y_finance library
        if self.time_format == 'month':
            self.time_period_str = str(self.time_range)+self.time_format[0]+self.time_format[1]
        else:
            self.time_period_str = str(self.time_range)+self.time_format[0]

        self.ticker = ticker

        start_date, end_date = self.calculate_dates(time_range=self.time_range, time_format=self.time_format)

        # Get the company
        tickerData = yf.Ticker(self.ticker)
        # Create historic data dataframe and fetch the data for the dates given.
        self.df = tickerData.history(self.time_period_str)

    @staticmethod
    def calculate_dates(time_range, time_format):
        """Calculates the start date from a given time range"""

        # Today's date
        end_date = date.today()

        if time_format == 'year':
            start_date = end_date - relativedelta(years=time_range)
            return start_date, end_date

        if time_format == 'month':
            start_date = end_date - relativedelta(months=time_range)
            return start_date, end_date

        if time_format == 'day':
            start_date = end_date - relativedelta(days=time_range)
            return start_date, end_date

    def get_column(self, feature):
        """get a specific dataframe"""
        try:

            if feature in ['Low', 'low']:
                return self.df["Low"]

            if feature in ['Close', 'close']:
                return self.df["Close"]

            if feature in ['Open', 'open']:
                return self.df["Open"]

            if feature in ['High', 'high']:
                return self.df["High"]

            if feature in ['Volume', 'volume']:
                return self.df["Volume"]

            if feature in ['Dividends', 'dividends']:
                return self.df["Dividends"]

            if feature in ['Stock Splits', 'Stock splits', 'stock splits']:
                return self.df["Stock Splits"]

        except Exception as e:
            print("Failed to get required data.", e)

    def get_dataframe(self):
        """For operations"""

        # sort data by date
        dataframe = self.df.sort_values('Date')

        # Make a numerical index
        dataframe.reset_index(inplace=True)

        return dataframe

    def view_mid_prices(self):
        """Shows mid prices"""
        plt.plot(range(self.df.shape[0]), (self.df['Low'] + self.df['High']) / 2.0)
        plt.show()
