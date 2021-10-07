import sys
#from PySide2 import *
from datetime import date, timedelta
from PySide2 import QtCore
from frontend import *
import yfinance as yf
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
from Custom_Widgets import *

# 43:58
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

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

        # Set left menu buttons
        self.ui.home_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page))
        self.ui.stock_analysis_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.stock_analysis))
        self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)
        self.ui.learn_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.learn))
        self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.learn_start_page)
        self.ui.trade_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.trade))
        self.ui.settings_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.settings))
        self.ui.about_icon.clicked.connect(lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.about))

        # Hide/show menu labels animation
        self.ui.menu_icon_button.clicked.connect(self.show_left_menu)

        # Ticker analysis page search
        self.ui.search_button.clicked.connect(self.search_ticker_in_analysis)

    def show_left_menu(self):
        """Animation for left menu closing"""
        width = self.ui.left_menu_cont_frame.width()

        if width == 50:
            new_width = 160

        else:
            new_width = 50

        # Animate
        animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        animation.setDuration(250)
        animation.setStartValue(width)
        animation.setEndValue(new_width)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        animation.start()

    def search_ticker_in_analysis(self):
        """Searching for a ticker"""

        # ticker name
        ticker = self.ui.search_entry.text()
        # make higher level reference for full access
        self.ticker = ticker
        ticker_obj = yf.Ticker(self.ticker)
        # console
        print(f'User searched for: {ticker}')

        # function verifies if it a stock or crypto
        ticker_type = self.stock_or_currency(ticker)

        if ticker_type == 'stock':
            # Check date of the week
            weekday = date.today()

            # If date is weekend market is closed, else open
            print(weekday)
            if weekday == 6 or weekday == 7:
                market_state = 'Closed'
            else:
                market_state = 'Open'

            if market_state == 'Open':
                # stock info
                stock_info = weekday.strftime(f'%d %B {weekday.year} - Market {market_state}')
                # print all info (temporal)
                # for key, value in ticker_obj.info.items():
                    # print(key, ":", value)

                # day info for stock
                site = ticker_obj.info['website']
                name = ticker_obj.info['longName'].split(',')[0]
                price = ticker_obj.info['currentPrice']
                prev_close = ticker_obj.info['previousClose']
                change_amount = price - prev_close
                change_percentage = change_amount/prev_close * 100
                symbol = '▲' if change_amount > 0 else '▼'

                # connect hyperlink to title(stock name) if there is one available
                if site:
                    self.ui.ticker_label.setOpenExternalLinks(True)
                    self.ui.ticker_label.setText(f"""
                    <html><head/><body><p><a href={site}>
                    <span data-hover={site} style=" font-weight:0; 
                    text-decoration: none; color:#ffffff;">{name.upper()}</span></a></p>
                    </body></html>
                    """)
                    self.ui.ticker_label.setTextFormat(Qt.RichText)

                # set stock header info display
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

        if ticker_type == 'currency':
            pass

    def show_info_data(self, time_period):
        """Shows the line chart and info for a specific timeframe in the gui"""

        # Before anything delete the current chart displayed
        layout = self.ui.stock_analysis_chart_cont
        # check if there is a chart in place
        if layout.count() == 1:
            # if there is, delete it
            layout.removeWidget(self.current_stock_chart)

        if time_period == '1d':
            # reset stock info entries
            self.reset_entries_for_stock_info_display('day')

            # get dataframe for 1d worth of stocks
            df = self.get_data_for_chart(self.ticker, time_period)

            # add line chart
            stock_line_series = QtCharts.QLineSeries()

            for index, row in df.iterrows():
                # stock data values (date, close)
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
            # place new stock data entries
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
        # date
        today = date.today()

        if time_period == '1d':
            # 1 day data for the stock at 5 minute intervals
            data = ticker.history(period='1d', interval='5m')
            return data

        if time_period == '1w':
            # 1 week data for the stock at 15 minute intervals
            week_start = today - timedelta(days=7)
            data = ticker.history(period='1w', interval='15m')
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

    @staticmethod
    def stock_or_currency(ticker):
        """Determine whether the given ticker is a stock or currency"""

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
