from PySide2 import *
from datetime import date, timedelta
from PySide2 import QtCore
from frontend import *
import yfinance as yf


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ticker = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Set menu buttons
        self.ui.home_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page))
        self.ui.stock_analysis_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.stock_analysis))
        self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)
        self.ui.learn_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.learn))
        self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.learn_start_page)
        self.ui.trade_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.trade))
        self.ui.settings_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.settings))
        self.ui.about_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.about))

        # Hide/show menu labels animation
        self.ui.menu_icon_button.clicked.connect(self.show_left_menu)

        # Stock analysis page search
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
        self.ticker = ticker
        ticker_obj = yf.Ticker(self.ticker)
        print(f'User searched for: {ticker}')

        # function verifies if it a stock or crypto
        ticker_type = self.stock_or_currency(ticker)

        if ticker_type == 'stock':
            # Check date of the week
            #yesterday = date.today() - timedelta(days=1)
            weekday = date.today()

            # If date is weekend market is closed, else open
            print(weekday)
            if weekday == 6 or weekday == 7:
                market_state = 'Closed'
            else:
                market_state = 'Open'

            if market_state == 'Open':
                # yesterday stock info
                stock_info = weekday.strftime(f'%d %B {weekday.year} - Market {market_state}')

                # day info for stock
                price = ticker_obj.info['currentPrice']
                prev_close = ticker_obj.info['previousClose']
                volume = ticker_obj.info['volume']
                avg_volume = ticker_obj.info['averageVolume']
                open_price = ticker_obj.info['open']
                high = ticker_obj.info['dayHigh']
                low = ticker_obj.info['dayLow']
                mkt_cap = ticker_obj.info['marketCap']
                fifty_two_week_high = ticker_obj.info['fiftyTwoWeekHigh']
                fifty_two_week_low = ticker_obj.info['fiftyTwoWeekLow']
                change_amount = price - prev_close
                change_percentage = change_amount/prev_close * 100
                symbol = '▲' if change_amount > 0 else '▼'

                # set display
                self.ui.stock_analysis_stock_info_content.setText(stock_info)
                self.ui.ticker_label.setText(ticker.upper())
                self.ui.volume_placeholder.setText(str(volume))
                self.ui.price_traded_label.setText(str(price))
                self.ui.change_direction_label.setText(symbol)
                self.ui.change_amount_label.setText(str(change_amount))
                self.ui.change_percentage.setText(f'({str(change_percentage)})')

                # set chart info display
                self.ui.day_open_placeholder.setText(str(open_price))
                self.ui.day_high_placeholder.setText(str(high))
                self.ui.day_low_placeholder.setText(str(low))
                self.ui.volume_placeholder.setText(str(volume))
                self.ui.avg_volume_placeholder.setText(str(avg_volume))
                self.ui.market_cap_placeholder.setText(str(mkt_cap))
                self.ui.fifty_two_week_high_placeholder.setText(str(fifty_two_week_high))
                self.ui.fifty_two_week_low_placeholder.setText(str(fifty_two_week_low))

                # chart buttons
                self.ui.one_day_button.clicked.connect(lambda: self.show_info_data('1d'))
                self.ui.one_week_button.clicked.connect(lambda: self.show_info_data('1w'))
                self.ui.one_month_button.clicked.connect(lambda: self.show_info_data('1m'))
                self.ui.one_year_button.clicked.connect(lambda: self.show_info_data('1y'))
                self.ui.five_year_button.clicked.connect(lambda: self.show_info_data('5y'))
                self.ui.max_button.clicked.connect(lambda: self.show_info_data('max'))

        if ticker_type == 'currency':
            pass

    def show_info_data(self, time_period):

        if time_period == '1d':
            self.reset_entries_for_stock_info_display('day')
            pass

        else:
            # get stock data
            self.reset_entries_for_stock_info_display('not_day')

            # dataframe
            df = self.get_data_for_chart(self.ticker, time_period)

            highest = max(list(df['High'].values))
            lowest = min(list(df['Low'].values))
            avg = (float(highest) + float(lowest))/2
            print(type(highest))
            print(lowest)
            print(lowest)

            self.ui.day_high_placeholder.setText(str(highest))
            self.ui.day_low_placeholder.setText(str(lowest))
            self.ui.day_open_placeholder.setText(str(avg))

    @staticmethod
    def get_data_for_chart(ticker, time_period):
        """Get timeframes of data for the stock"""

        ticker = yf.Ticker(ticker)

        today = date.today()

        if time_period == '1d':
            pass

        if time_period == '1w':
            # 1 week data for the stock
            week_start = today - timedelta(days=7)
            data = ticker.history(start=week_start, end=today)
            return data

        if time_period == '1m':
            # 1 month data for the stock
            month_start = today - timedelta(days=31)
            data = ticker.history(start=month_start, end=today)
            return data

        if time_period == '1y':
            # 1 year data for the stock
            year_start = today - timedelta(days=365)
            data = ticker.history(start=year_start, end=today)
            return data

        if time_period == '5y':
            # 5 year data for the stock
            five_year_start = today - timedelta(days=1825)
            data = ticker.history(start=five_year_start, end=today)
            return data

        if time_period == 'max':
            # entire lifetime data for the stock
            data = ticker.history(period='max')
            return data

    def reset_entries_for_stock_info_display(self, new='not_day'):
        """Reset display labels for stock info"""

        if new == 'not_day':
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
            self.ui.day_open.setText('Open')
            #self.ui.day_open_placeholder.setText(' ')

            self.ui.volume_label.setText('Volume')
            #self.ui.volume_placeholder.setText(' ')

            self.ui.avg_volume_placeholder.setText('Avg Volume')
            #self.ui.avg_volume_placeholder.setText(' ')

            #self.ui.fifty_two_week_high_placeholder.setText(' ')
            self.ui.fifty_two_week_high.setText('52wK High')
            #self.ui.fifty_two_week_low_placeholder.setText(' ')
            self.ui.fifty_two_week_low.setText('52wK Low')

            self.ui.market_cap.setText('Mkt Cap')

    @staticmethod
    def stock_or_currency(ticker):
        ticker = yf.Ticker(ticker)
        try:
            if ticker.info['description']:
                return 'currency'

        except KeyError:
            return 'stock'


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())
