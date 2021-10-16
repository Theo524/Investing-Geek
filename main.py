import sys
import re
from datetime import date, timedelta, datetime
from PySide2 import QtCore
from frontend import *
import yfinance as yf
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
from PyQt5.QtWidgets import QMessageBox
import requests
from bs4 import BeautifulSoup
import string


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # all ticker names
        all_tickers = AllTickers()

        self.all_stock_ticker_names = all_tickers.stock_dict
        self.all_crypto_ticker_names = all_tickers.crypto_dict

        # gui elements
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # charts reference for stock analysis
        self.current_stock_chart = None
        # charts reference for currency analysis
        self.current_currency_chart = None
        # ticker in use
        self.ticker = None

        # set starting pages
        self.set_starting_widgets()

        # Hide/show menu labels animation
        self.ui.menu_icon_button.clicked.connect(self.show_left_menu)

        # Ticker analysis page search button
        self.ui.search_button.clicked.connect(self.search_ticker_in_analysis)

    def show_left_menu(self):
        """Animation for left menu closing"""
        width = self.ui.left_menu_cont_frame.width()

        if width == 50:
            new_width = 160

        else:
            new_width = 50

        # Animate
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def search_ticker_in_analysis(self):
        """Searching for a ticker"""

        # ticker name
        ticker = self.ui.search_entry.text()
        # make higher level reference for full access
        self.ticker = ticker
        ticker_obj = yf.Ticker(self.ticker)

        # console
        print(f'User searched for: {ticker}')
        try:
            print(f'Which is: {self.all_stock_ticker_names[ticker.upper()]}')
        except KeyError:
            pass

        try:
            print(f'Which is: {self.all_crypto_ticker_names[ticker.upper()]}')
        except KeyError:
            pass

        # function verifies if it a stock or crypto
        ticker_type = self.stock_or_crypto()

        if ticker_type == 'stock':
            self.is_stock = True
            # Check date of the week
            weekday = date.today()

            # If date is weekend market is closed, else open
            if weekday == 6 or weekday == 7:
                market_state = 'Closed'
            else:
                market_state = 'Open'

            if market_state == 'Open':
                time = datetime.now()
                is_am = time.hour < 12
                t = 'AM' if is_am else 'PM'

                # stock info
                stock_info = weekday.strftime(f'%d %B, {time.hour}{time.minute} {t} - Market {market_state}')
                # print all info for ticker(temporal)
                # for key, value in ticker_obj.info.items():
                #    print(key, ":", value)

                # day info for stock
                #name = ticker_obj.info['longName'].split(',')[0]
                price = ticker_obj.info['currentPrice']
                prev_close = ticker_obj.info['previousClose']
                change_amount = price - prev_close
                change_percentage = change_amount/prev_close * 100
                symbol = '▲' if change_amount > 0 else '▼'

                # set stock page
                self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)

                # connect command to title(stock name)
                self.ui.ticker_label_title_analysis.clicked.connect(lambda: self.show_ticker_extraInfoWindow('stock'))

                # set stock header info display
                self.ui.ticker_label_title_analysis.setText(self.all_stock_ticker_names[self.ticker.upper()])
                self.ui.stock_analysis_stock_info_content.setText(stock_info)
                self.ui.price_traded_label.setText(str(price))
                self.ui.change_direction_label.setText(symbol)
                self.ui.change_amount_label.setText(str(round(change_amount, 2)))
                self.ui.change_percentage.setText(f'({str(round(change_percentage, 2))})%')

                # add chart for 1 day
                self.show_info_data('1d')

                # link timeframe chart buttons
                self.ui.one_day_button.clicked.connect(lambda: self.show_info_data('1d'))
                self.ui.one_week_button.clicked.connect(lambda: self.show_info_data('1w'))
                self.ui.one_month_button.clicked.connect(lambda: self.show_info_data('1m'))
                self.ui.one_year_button.clicked.connect(lambda: self.show_info_data('1y'))
                self.ui.five_year_button.clicked.connect(lambda: self.show_info_data('5y'))
                self.ui.max_button.clicked.connect(lambda: self.show_info_data('max'))

        if ticker_type == 'crypto':
            today = date.today()
            time = datetime.now()
            is_am = time.hour < 12
            t = 'AM' if is_am else 'PM'

            # stock info
            crypto_info = today.strftime(f'Last updated - %d %B %Y, {time.hour}:{time.second} {t}')
            # print all info for ticker(temporal)
            # for key, value in ticker_obj.info.items():
            #    print(key, ":", value)

            # quote info for crypto
            name = ticker_obj.info['name']
            pair = ticker_obj.info['symbol']
            price = ticker_obj.info['regularMarketPrice']
            currency = ticker_obj.info['currency']

            # set currency page
            self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_currency_page)

            # connect command to title(stock name)
            self.ui.ticker_label_title_analysis.clicked.connect(lambda: self.show_ticker_extraInfoWindow('crypto'))

            # set crypto header info
            self.ui.ticker_label_title_analysis.setText(f'{str(name)}')
            self.ui.extra_info_about_crypto.setText(str(crypto_info))
            self.ui.crypto_price_label.setText(f'1{str(pair.split("-")[0])}={str(price)}')
            self.ui.crypto_currency_price_label.setText(str(currency))
            self.ui.first_currency_label.setText(str(pair.split('-')[0]))
            self.ui.second_curency_label.setText(str(pair.split('-')[1]))
            self.ui.first_currency_entry.setText('1')
            self.ui.second_currency_entry.setText(str(price))
            # entry mask
            onlyInt = QIntValidator(1, 1000000, self)
            self.ui.first_currency_entry.setValidator(onlyInt)
            self.ui.first_currency_entry.setMaxLength(6)

            # button for value of currency
            worth_of_one_unit = price
            self.ui.crypto_comparison_button.clicked.connect(lambda: self.calc_crypto_worth(worth_of_one_unit))



            # add chart for 1 day
#           self.show_info_data('1d')
#
 #           # link timeframe chart buttons
  #          self.ui.one_day_button.clicked.connect(lambda: self.show_info_data('1d'))
         #   self.ui.one_week_button.clicked.connect(lambda: self.show_info_data('1w'))
   #         self.ui.one_month_button.clicked.connect(lambda: self.show_info_data('1m'))
    #        self.ui.one_year_button.clicked.connect(lambda: self.show_info_data('1y'))
     #       self.ui.five_year_button.clicked.connect(lambda: self.show_info_data('5y'))
      # #     self.ui.max_button.clicked.connect(lambda: self.show_info_data('max'))
       #     pass

        if not ticker_type:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('The ticker you entered is either incorrect or there is no data on it')
            msg.setWindowTitle("Error")
            msg.exec_()

    def calc_crypto_worth(self, worth_of_one_unit):
        """Calculate the worth of n amount of crypto currency"""

        amount = self.ui.first_currency_entry.text()
        final_val = int(amount) * worth_of_one_unit
        self.ui.second_currency_entry.setText(str(final_val))

    def show_info_data(self, time_period):
        """Shows the line chart and info for a specific timeframe in the gui"""

        # Before anything delete the current chart displayed
        layout = self.ui.stock_analysis_chart_cont
        # of course, check if there is a chart in place
        if layout.count() == 1:
            # if there is, delete it
            layout.removeWidget(self.current_stock_chart)

        if time_period == '1d':
            # reset stock info entries, to allocate day data
            self.reset_entries_for_stock_info_display('day')

            # get dataframe for 1d worth of stocks
            df = self.get_data_for_chart(self.ticker, time_period)

            # add line chart
            stock_line_series = QtCharts.QLineSeries()

            for index, row in df.iterrows():
                # add stock data values for chart (date, close)
                stock_line_series.append(float(index.value), float(row['Close']))

            # chart creation
            chart = QtCharts.QChart()
            chart.addSeries(stock_line_series)

            chart_view = QtCharts.QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
            chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)
            chart_view.setRenderHint(QPainter.Antialiasing)

            # add chart to layout
            self.ui.stock_analysis_chart_cont.addWidget(chart_view)
            # keep reference to later delete it
            self.current_stock_chart = chart_view

            # add info about stock
            ticker_obj = yf.Ticker(self.ticker)
            # required info
            volume = ticker_obj.info['volume']
            avg_volume = ticker_obj.info['averageVolume']
            open_price = ticker_obj.info['open']
            high = ticker_obj.info['dayHigh']
            low = ticker_obj.info['dayLow']
            mkt_cap = ticker_obj.info['marketCap']
            fifty_two_week_high = ticker_obj.info['fiftyTwoWeekHigh']
            fifty_two_week_low = ticker_obj.info['fiftyTwoWeekLow']
            # set chart info display
            self.ui.day_open_placeholder.setText(str(open_price))
            self.ui.day_high_placeholder.setText(str(high))
            self.ui.day_low_placeholder.setText(str(low))
            self.ui.volume_placeholder.setText(str(volume))
            self.ui.avg_volume_placeholder.setText(str(avg_volume))
            self.ui.market_cap_placeholder.setText(str(mkt_cap))
            self.ui.fifty_two_week_high_placeholder.setText(str(fifty_two_week_high))
            self.ui.fifty_two_week_low_placeholder.setText(str(fifty_two_week_low))

        else:
            # place new stock data entries for non day entries
            self.reset_entries_for_stock_info_display('not_day')

            # dataframe for stock
            df = self.get_data_for_chart(self.ticker, time_period)

            # values
            highest = max(list(df['High'].values))
            lowest = min(list(df['Low'].values))
            avg = (float(highest) + float(lowest))/2

            # add info to entries
            self.ui.day_high_placeholder.setText(str(round(highest)))
            self.ui.day_low_placeholder.setText(str(round(lowest)))
            self.ui.day_open_placeholder.setText(str(round(avg)))

            # add chart
            stock_line_series = QtCharts.QLineSeries()

            # add data to line chart
            for index, row in df.iterrows():
                # stock data (date, close)
                stock_line_series.append(float(index.value), float(row['Close']))

            # chart creation
            chart = QtCharts.QChart()
            chart.addSeries(stock_line_series)

            chart_view = QtCharts.QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
            chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

            # add chart to layout
            self.ui.stock_analysis_chart_cont.addWidget(chart_view)
            # keep reference for later deletion
            self.current_stock_chart = chart_view

    @staticmethod
    def get_data_for_chart(ticker, time_period):
        """Get data required for a stock and timeframe"""

        # ticker obj
        ticker = yf.Ticker(ticker)

        if time_period == '1d':
            # 1 day data for the stock at 5 minute intervals
            data = ticker.history(period='1d', interval='5m')
            print(data)
            return data

#// FIX THIS (gives very inaccurate and strange data) ----------------------------------------------------------------
        if time_period == '1w':
            # 1 week data for the stock at 15 minute interval
            data = ticker.history(period='5d', interval='15m')
            print(data)
            return data
#//-------------------------------------------------------------------------------------------------------------------

        if time_period == '1m':
            # 1 month data for the stock at a daily interval
            data = ticker.history(period='1mo', interval='1d')
            return data

        if time_period == '1y':
            # 1 month data for the stock at a daily interval
            data = ticker.history(period='1y', interval='1d')
            return data

        if time_period == '5y':
            # 5 year data for the stock at a weekly interval
            data = ticker.history(period='5y', interval='1wk')
            return data

        if time_period == 'max':
            # entire lifetime data for the stock at a monthly interval
            data = ticker.history(period='max', interval='1mo')
            return data

    def reset_entries_for_stock_info_display(self, new='not_day'):
        """Reset display labels for stock info"""

        if new == 'not_day':
            # Non-Day charts only show avg, high and close
            # so reset all entries to show only these
            self.ui.day_open.setText('Avg')
            self.ui.day_open_placeholder.setText(' ')
            self.ui.volume_label.setText('  ')
            self.ui.volume_placeholder.setText(' ')
            self.ui.market_cap.setText(' ')
            self.ui.market_cap_placeholder.setText(' ')
            self.ui.avg_volume.setText(' ')
            self.ui.avg_volume_placeholder.setText(' ')
            self.ui.fifty_two_week_high_placeholder.setText(' ')
            self.ui.fifty_two_week_high.setText(' ')
            self.ui.fifty_two_week_low_placeholder.setText(' ')
            self.ui.fifty_two_week_low.setText(' ')

        else:
            # Day chart info for stocks will show open, high, close, volume, avg volume, mkt cap and 52wk low and high
            # Ensures they appear
            self.ui.day_open.setText('Open')
            self.ui.volume_label.setText('Volume')
            self.ui.avg_volume_placeholder.setText('Avg Volume')
            self.ui.fifty_two_week_high.setText('52wK High')
            self.ui.fifty_two_week_low.setText('52wK Low')
            self.ui.market_cap.setText('Mkt Cap')

    def stock_or_crypto(self):
        """Determine whether the given ticker is a stock or cryptocurrency"""

        if self.ticker.upper() in list(self.all_stock_ticker_names.keys()):
            return 'stock'
        else:
            pair = '-' in self.ticker.lower()
            curr = self.ticker.lower().split('-')
            if pair and curr[0].upper() in list(self.all_crypto_ticker_names.keys()):
                return 'crypto'

            else:
                return False

    def show_ticker_extraInfoWindow(self, ticker_type):
        """Window with more info regarding ticker"""
        ticker_window = TickerInfo(self.ticker, ticker_type)

    def set_starting_widgets(self):
        """Sets all starting pages/widgets"""

        # Set left menu buttons
        self.ui.home_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page))
        self.ui.stock_analysis_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.stock_analysis))
        self.ui.learn_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.learn))
        self.ui.trade_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.trade))
        self.ui.settings_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.settings))
        self.ui.about_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.about))

        # app starting page
        self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page)

        # ticker search starting page (stock)
        self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)

        # learning page
        self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.learn_start_page)

        # learning page buttons
        self.ui.stocks_button_learn.clicked.connect(lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.stocks_page))
        self.ui.crypto_button_learn.clicked.connect(lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.cryptocurrency_page))
        self.ui.forex_button_learn.clicked.connect(lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.forex_page))


class TickerInfo(QMainWindow):
    def __init__(self, ticker):
        QMainWindow.__init__(self, ticker_type='stock')

        # gui elements
        self.ui = Ticker_Window()
        self.ui.setupUi(self)
        self.setFixedSize(710, 550)

        # buttons
        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)
        self.ui.stats_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.statistics_page))
        self.ui.profile_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile_page))

        ticker_obj = yf.Ticker(ticker)
        summary = ticker_obj.info['longBusinessSummary']
        summary = re.sub("(.{64})", "\\1\n", summary, 0, re.DOTALL)
        self.ui.ticker_name.setText(ticker_obj.info['longName'])
        self.ui.sector.setText(f"{ticker_obj.info['sector']}")
        self.ui.employees.setText(f"{ticker_obj.info['fullTimeEmployees']}")
        self.ui.industry.setText(f"{ticker_obj.info['industry']}")
        self.ui.zip.setText(f"{ticker_obj.info['zip']}")
        self.ui.city.setText(f"{ticker_obj.info['city']}")
        self.ui.state.setText(f"{ticker_obj.info['state']}")
        try:
            self.ui.address.setText(f"{ticker_obj.info['address']}")
        except KeyError:
            self.ui.address.setText(f"{ticker_obj.info['address1']}")

        self.ui.phone.setText(f"{ticker_obj.info['phone']}")
        self.ui.country.setText(f"{ticker_obj.info['country']}")
        self.ui.website.setText(f"{ticker_obj.info['website']}")
        self.ui.summary.setText(f"{summary}")

        # show window
        self.show()


class AllTickers:
    """Gets a limited amount of tickers for a ticker type"""

    def __init__(self):

        self.stock_dict = {}
        self.crypto_dict = {}

        # get all stocks
        for char in string.ascii_uppercase:
            self.scrape_symbols(letter=char, val_type='stock')

        # get all crypto
        self.scrape_symbols(letter='', val_type='crypto')

    # Create a function to scrape the data
    def scrape_symbols(self, letter, val_type='stock'):
        """ Create a function to scrape the data"""

        if val_type == 'stock':
            letter = letter.upper()
            exchange = 'nasdaq'
            # website
            URL = f'https://www.advfn.com/{exchange}/{exchange}.asp?companies='+letter

            # convert to soup object
            page = requests.get(URL)
            soup = BeautifulSoup(page.text, "html.parser")

            # iterate all rows '<tr>' tags
            odd_rows = soup.find_all('tr', attrs= {'class':'ts0'})
            even_rows = soup.find_all('tr', attrs= {'class':'ts1'})

            # make dicts with tag content
            for i in odd_rows:
                row = i.find_all('td')
                self.stock_dict[row[1].text.strip()] = row[0].text.strip()

            for i in even_rows:
                row = i.find_all('td')
                self.stock_dict[row[1].text.strip()] = row[0].text.strip()

        if val_type == 'crypto':
            # website
            URL = 'https://crypto.com/price'

            # convert to soup object
            page = requests.get(URL)
            soup = BeautifulSoup(page.text, "html.parser")

            # iterate all rows '<span>' tags
            crypto_names = soup.find_all('span', attrs={'class':'chakra-text css-1mrk1dy'})
            crypto_acr = soup.find_all('span', attrs={'class':'chakra-text css-44ctie'})

            # amount of crypto names
            crypto_length = len(crypto_names)

            # merge into dicts
            for i in range(crypto_length):
                self.crypto_dict[crypto_acr[i].text] = crypto_names[i].text


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())
