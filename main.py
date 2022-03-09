"""Change from pyside2 to pyqt5"""

import sys
import os
import re
import datetime
import time
import requests.exceptions
import yfinance as yf
from GoogleNews import GoogleNews
from newspaper import Config
import pandas as pd
import json
import requests
import pyqtgraph
from configparser import ConfigParser
from bs4 import BeautifulSoup

from PyQt5 import QtCore, QtGui
from frontend import *
from PyQt5 import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # ui elements
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.show()

        # ticker in use for higher access
        self.ticker = None
        self.ticker_type = None
        self.ticker_obj = None

        # WINDOW SETTINGS #
        # window border/frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # menu animation
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        # window actions
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        # movement
        self.oldPos = self.pos()
        # resizing
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0);
            border-radius:10px;""")
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)
        # center window
        self.center()
        # shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # SEARCH PAGE #
        # thread objects
        self.thread = None
        self.worker = None
        # graph line
        self.crypto_graph_line = None
        self.stock_graph_line = None
        # graph widgets
        self.crypto_graphWidget = pyqtgraph.PlotWidget()
        self.stock_graphWidget = pyqtgraph.PlotWidget()
        # search error msg for thread
        self.error_msg = None

        # search page buttons
        self.stock_analysis_buttons = {'1d': self.ui.one_day_button, '1w': self.ui.one_week_button,
                                       '1m': self.ui.one_month_button, '1y': self.ui.one_year_button,
                                       '5y': self.ui.five_year_button, 'max': self.ui.max_button}
        self.stock_analysis_crypto_buttons = {'1d': self.ui.one_day_button_2, '1w': self.ui.one_week_button_2,
                                              '1m': self.ui.one_month_button_2, '1y': self.ui.one_year_button_2,
                                              '5y': self.ui.five_year_button_2, 'max': self.ui.max_button_2}

        # stock game(simulator)
        self.stock_game = StockGame()

        # set starting pages
        self.set_starting_widgets()
        self.set_starting_settings()

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

    def center(self):
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtGui.QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.isMaximized():
            # can't drag a maximized window
            return
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def restore_or_maximize_window(self):
        """"Restores or minimizes window size"""

        if self.isMaximized():
            # Maximized, show maximized window icon
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(f'{os.getcwd()}\icons\maximize.svg'))

            # show border radius
            self.ui.header_frame.setStyleSheet(u"background-color: rgb(54, 79, 113);\n"
                                               "border-radius:10px;")

        else:
            # Minimized, show minimized window icon
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(f'{os.getcwd()}\icons\minimize.svg'))

            # hide border radius
            self.ui.header_frame.setStyleSheet(u"background-color: rgb(54, 79, 113);\n"
                                               "border-radius:none;")

    def apply_settings(self):
        """Apply settings to application from setting page"""

        # Confirm user wants to apply settings
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Are you sure you want to apply these settings?")
        msg.setWindowTitle("Settings")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_val = msg.exec_()

        # config file where these settings will be written to
        config = ConfigParser()
        file = 'config.ini'
        config.read(file)
        settings = config["settings"]

        # User clicked no
        if return_val == QMessageBox.No:
            return

        # User clicked yes
        if return_val == QMessageBox.Yes:
            # all headings labels(for first setting)
            headings = (self.ui.home_header, self.ui.analysis_header, self.ui.learning_header,
                        self.ui.simulator_header, self.ui.settings_header)

            # Checkstate 0 represents an unchecked button, Checkstate 2 represents a checked button

            # HIDE/SHOW HEADINGS(FIRST SETTING)
            if self.ui.settings_show_headings_checkBox.checkState() == 0:
                # unchecked
                for header in headings:
                    # Hide all headings
                    header.hide()

                # apply to configfile
                settings["show_headings"] = 'False'

                # home layout adjustment
                self.ui.verticalLayout_8.setContentsMargins(9, 52, 9, 9)

                # settings layout adjustment
                self.ui.verticalLayout_167.setContentsMargins(9, 54, 9, 9)

            elif self.ui.settings_show_headings_checkBox.checkState() == 2:
                # checked
                for header in headings:
                    # Show all headings
                    header.show()

                # home layout adjustments
                self.ui.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
                self.ui.verticalLayout_167.setContentsMargins(9, 0, 9, 9)

                # apply to configfile
                settings["show_headings"] = 'True'

            # SHOW TICKER INFO (SECOND SETTING)
            if self.ui.settings_extra_info_checkBox.checkState() == 0:
                # unchecked
                self.ui.ticker_label_title_analysis.setEnabled(False)

                # apply to configfile
                settings["ticker_info"] = 'False'

            elif self.ui.settings_extra_info_checkBox.checkState() == 2:
                # checked
                self.ui.ticker_label_title_analysis.setEnabled(True)

                # apply to configfile
                settings["ticker_info"] = 'True'

            # SHOW NEWS(THIRD SETTING)
            if self.ui.settings_news_visible_checkBox.checkState() == 0:
                # unchecked
                # hide news frame
                self.ui.stock_analysis_news_frame.hide()
                self.ui.stock_analysis_news_frame_2.hide()

                # apply to configfile
                settings["news_visible"] = 'False'

            elif self.ui.settings_news_visible_checkBox.checkState() == 2:
                # checked
                # show news frame
                self.ui.stock_analysis_news_frame.show()
                self.ui.stock_analysis_news_frame_2.show()

                # apply to configfile
                settings["news_visible"] = 'True'

            # FONTS (FOURTH SETTING)
            font = self.ui.settings_fontComboBox.currentText()
            font_size = self.ui.settings_fontSizeComboBox.text()
            self.ui.stocks_tutorial_main_body.setStyleSheet(f"""
    background-color: rgb(26, 29, 39);
    border-radius:10px;
    color:rgb(255, 255, 255);
    font: {str(font_size)}pt \"{str(font)}\";
    """)

            # apply to configfile
            settings["font"] = str(font)
            settings["font_size"] = str(font_size)

            # changes have been applied to ui, apply them now to config.ini
            # Write changes back to file
            with open('config.ini', 'w') as configfile:
                config.write(configfile)

            # informative feedback
            self.display_feedback(msg_type='information', message='Settings successfully applied', title='Success!')

    def set_starting_settings(self):
        """Read config file and use the values there to set how the application will look like
        """

        # config file
        config = ConfigParser()
        file = 'config.ini'
        config.read(file)
        settings = config["settings"]

        # all headings labels(for first setting)
        headings = (self.ui.home_header, self.ui.analysis_header, self.ui.learning_header,
                    self.ui.simulator_header, self.ui.settings_header)

        # HIDE/SHOW HEADINGS(FIRST SETTING)
        if settings["show_headings"] == 'False':
            # unchecked
            for header in headings:
                # Hide all headings
                header.hide()

            # change ui
            self.ui.settings_show_headings_checkBox.setChecked(False)

            # home layout adjustment
            self.ui.verticalLayout_8.setContentsMargins(9, 52, 9, 9)

            # settings layout adjustment
            self.ui.verticalLayout_167.setContentsMargins(9, 54, 9, 9)

        elif settings["show_headings"] == 'True':
            # checked
            for header in headings:
                # Show all headings
                header.show()

            # home layout adjustments
            self.ui.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
            self.ui.verticalLayout_167.setContentsMargins(9, 0, 9, 9)

            # change ui
            self.ui.settings_show_headings_checkBox.setChecked(True)

        # SHOW TICKER INFO (SECOND SETTING)
        if settings["ticker_info"] == 'False':
            # unchecked
            self.ui.ticker_label_title_analysis.setEnabled(False)

            # change ui
            self.ui.settings_extra_info_checkBox.setChecked(False)

        elif settings["ticker_info"] == 'True':
            # checked
            self.ui.ticker_label_title_analysis.setEnabled(True)

            # change ui
            self.ui.settings_extra_info_checkBox.setChecked(True)

        # SHOW NEWS(THIRD SETTING)
        if settings["news_visible"] == 'False':
            # unchecked
            # hide news frame
            self.ui.stock_analysis_news_frame.hide()
            self.ui.stock_analysis_news_frame_2.hide()

            # change ui
            self.ui.settings_news_visible_checkBox.setChecked(False)

        elif settings["news_visible"] == 'True':
            # checked
            # hide news frame
            self.ui.stock_analysis_news_frame.show()
            self.ui.stock_analysis_news_frame_2.show()

            # change ui
            self.ui.settings_news_visible_checkBox.setChecked(True)

        # FONTS (FOURTH SETTING)
        font = settings["font"]
        font_size = settings["font_size"]
        self.ui.stocks_tutorial_main_body.setStyleSheet(f"""
    background-color: rgb(26, 29, 39);
    border-radius:10px;
    color:rgb(255, 255, 255);
    font: {str(font_size)}pt \"{str(font)}\";
    """)

        font = QFont(font, int(font_size))

        # change ui
        self.ui.settings_fontComboBox.setFont(font)
        self.ui.settings_fontSizeComboBox.setValue(int(font_size))

    def show_left_menu(self):
        """Animation for left menu closing and opening"""

        # left menu frame length
        width = self.ui.left_menu_cont_frame.width()

        # default width is 40
        if width == 40:
            # new width allows enough space for text labels
            new_width = 140
            # set ext
            self.ui.home_icon.setText('  Home')
            self.ui.stock_analysis_icon.setText('  View')
            self.ui.learn_icon.setText('  Learn')
            self.ui.trade_icon.setText('  Trade')
            self.ui.settings_icon.setText('  Settings')
            self.ui.about_icon.setText('  About')

        else:
            new_width = 40
            # set text
            self.ui.home_icon.setText('')
            self.ui.stock_analysis_icon.setText('')
            self.ui.learn_icon.setText('')
            self.ui.trade_icon.setText('')
            self.ui.settings_icon.setText('')
            self.ui.about_icon.setText('')

        # Animation
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        try:
            self.ui.left_menu_cont_frame.set()
        except AttributeError:
            pass

    def set_starting_widgets(self):
        """Set all starting pages/widgets and application events

        A lot of these are necessary because the ui files
        usually end up very messy as in any random widget
        could appear anywhere
        """

        # set app starting page(what the user sees first)
        self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page)

        # TICKER SEARCH PAGE #
        # ticker search button clicked(thread)
        self.ui.search_button.clicked.connect(self.ticker_search_thread)
        # set ticker search starting page
        self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)
        # hide progressbar frame(appears when search is ongoing)
        self.ui.progressbar_frame.hide()
        # button for progress bar widget disabled and command
        self.ui.search_show_data_button.setEnabled(False)
        self.ui.search_show_data_button.clicked.connect(self.display_ticker_search_results)
        # add graphs widgets to the pages
        self.ui.stock_analysis_chart_cont.addWidget(self.stock_graphWidget)
        self.ui.crypto_analysis_chart_cont.addWidget(self.crypto_graphWidget)

        # LEFT MENU #
        # Hide/show left hand side menu animation
        self.ui.menu_icon_button.clicked.connect(self.show_left_menu)
        # Set left menu buttons and the pages they lead to
        self.ui.home_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.home_page))
        self.ui.stock_analysis_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.stock_analysis))
        self.ui.learn_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.learn))
        self.ui.trade_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.trade))
        self.ui.settings_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.settings))
        self.ui.about_icon.clicked.connect(
            lambda: self.ui.stacked_menu_pages.setCurrentWidget(self.ui.about))

        # LEARNING PAGE #
        # set learning page starting page
        self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.learn_start_page)
        # set learning page buttons and the guide they lead to
        self.ui.stocks_button_learn.clicked.connect(
            lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.stocks_page))
        self.ui.crypto_button_learn.clicked.connect(
            lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.cryptocurrency_page))
        self.ui.forex_button_learn.clicked.connect(
            lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.forex_page))
        # return to the previous page buttons
        self.ui.learn_return_to_homepage_button.clicked.connect(
            lambda: self.ui.learning_pages_stackedWidget.setCurrentWidget(self.ui.learn_start_page))

        # SIMULATOR PAGE #
        # simulator page starting page
        self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_start_page)
        # simulator trading tab starting widget
        self.ui.stock_sim_trade_stackedWidget.setCurrentWidget(self.ui.stock_simulator_trade_page_tab)
        # simulator tab widget starting tab
        self.ui.tabWidget.setCurrentIndex(0)
        # simulator page buttons and actions
        self.ui.stock_simulator_start_btn.clicked.connect(
            lambda: self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_login_page))
        self.ui.simulator_create_new_user_btn.clicked.connect(
            lambda: self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_register_page))
        self.ui.simulator_return_to_homepage_button.clicked.connect(
            lambda: self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_start_page))
        self.ui.simulator_return_to_homepage_button_2.clicked.connect(
            lambda: self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_start_page))
        # simulator logout
        self.ui.stock_simulator_logout_btn.clicked.connect(self.simulator_logout)
        # simulator login confirm user button
        self.ui.simulator_continue_to_sim_btn.clicked.connect(self.simulator_login)
        self.ui.simulator_confirm_new_username_entry.clicked.connect(self.simulator_register)
        # simulator entry quantity mask(makes sure the quantity the user can enter for a stock is only int)
        only_int = QIntValidator(1, 10000, self)
        self.ui.stock_simulator_quantity_entry.setValidator(only_int)
        # simulator lookup
        self.ui.stock_simulator_symbol_lookup_button.clicked.connect(self.simulator_stock_lookup)
        # simulator clear entries
        self.ui.stock_simulator_purchase_button_2.clicked.connect(self.simulator_clear_entries)
        # simulator purchase
        self.ui.stock_simulator_purchase_button.clicked.connect(self.preview_order)
        # simulator delete user
        self.ui.stock_simulator_delete_account_btn.clicked.connect(self.simulator_delete_user)
        # simulator user profile btn
        self.ui.simulator_user_icon_btn.clicked.connect(
            lambda: self.ui.tabWidget.setCurrentIndex(3))
        # simulator transaction page disable main window
        self.ui.stock_simulator_confirm_transaction_page.setWindowModality(QtCore.Qt.ApplicationModal)

        # settings page
        self.ui.settings_view_users_btn.clicked.connect(self.update_trading_settings_pg_data)
        self.ui.settings_stackedWidget.setCurrentWidget(self.ui.settings_main)
        self.ui.settings_return_to_homepage_button.clicked.connect(
            lambda: self.ui.settings_stackedWidget.setCurrentWidget(self.ui.settings_main))
        # applying settings button clicked
        self.ui.settings_apply_settings.clicked.connect(self.apply_settings)

    def ticker_search_load(self):
        """Write the search information to files

        writes necessary data for thread to run properly
        """

        # path for the search files
        path = os.getcwd() + '\\temp\\search'

        # ticker
        ticker = self.ui.search_entry.text()
        self.ticker = ticker

        # read config file to see if the news are to be shown
        config_obj = ConfigParser()
        config_obj.read("config.ini")
        news_setting = config_obj["settings"]["news_visible"] # the setting
        show_news = True if news_setting == 'True' else False

        # finally write parameters to file to be read
        dictionary = {
            "ticker": ticker,
            "news": show_news,
            "path": path
        }

        # writing json
        with open(os.getcwd() + '\\temp\\Ticker.json', "w") as outfile:
            json.dump(dictionary, outfile)

    def ticker_search_thread(self):
        """Run thread for ticker search"""
        # write the data the thread will use
        self.ticker_search_load()

        # make progressbar frame visible
        self.ui.progressbar_frame.show()
        # Temporarily disable main search button
        self.ui.search_button.setEnabled(False)

        ###### thread ######
        # Add a QThread object
        self.thread = QThread()
        # Add a worker object
        self.worker = LoadTickerData()
        # Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.thread_is_done.connect(self.thread.requestInterruption)
        self.worker.thread_is_done.connect(self.thread.quit)
        self.worker.thread_is_done.connect(self.thread.wait)
        self.worker.thread_is_done.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # custom signals and slots
        self.worker.progress.connect(self.update_progressBar)
        self.worker.message.connect(self.update_search_message)
        self.worker.thread_is_done.connect(self.search_thread_finished)
        self.worker.error_message.connect(self.thread_error_msg)
        # Start the thread
        self.thread.start()

    def update_progressBar(self, count):
        """Progress bar updating with search thread"""

        self.ui.progressBar.setValue(count)

    def update_search_message(self, msg):
        """Search thread message shown"""

        self.ui.search_show_data_button.setText(msg)

    def thread_error_msg(self, msg):
        """Error message from search thread"""

        self.error_msg = msg

    def search_thread_finished(self, flag):
        """Search thread completed"""

        if flag:
            # Enable frame button
            self.ui.search_show_data_button.setEnabled(True)
            # Enable main search button
            self.ui.search_button.setEnabled(True)

            # display feedback if the user is on a different page
            if self.ui.stacked_menu_pages.currentWidget() != self.ui.stock_analysis:
                self.display_feedback(message='Data loaded', msg_type='information', title='Done')

        if not flag:
            # Set thread to None
            self.thread = None

            # Disable frame button
            self.ui.search_show_data_button.setEnabled(False)
            # Enable main search button
            self.ui.search_button.setEnabled(True)

            # end progress bar
            self.ui.search_show_data_button.setText('Ending...')
            progressbar_val = self.ui.progressBar.value()
            remainder = 100 - progressbar_val
            for i in range(remainder):
                progressbar_val += 2
                time.sleep(.01)
                self.ui.progressBar.setValue(progressbar_val)

            # clear_text
            self.ui.search_entry.clear()
            # hide progressbar frame
            self.ui.progressbar_frame.hide()

            # feedback
            self.display_feedback(message=self.error_msg,
                                  msg_type='error', title='Error')

    def display_ticker_search_results(self):
        """Sets results from ticker search onto search page"""

        # hide progressbar frame again
        self.ui.progressbar_frame.hide()

        # cursor
        QApplication.setOverrideCursor(Qt.WaitCursor)

        # get loaded data
        with open(os.getcwd() + '\\temp\\search\\TickerData.json', 'r') as f:
            data = json.load(f)

        # file contents
        self.ticker_obj = data

        # function verifies if it a stock or crypto, also use it to determine whether user is connected to the internet
        try:
            self.ticker_type = self.stock_or_crypto()
        except requests.exceptions.ConnectionError:

            # restore cursor
            QApplication.restoreOverrideCursor()

            # feedback and and exit function
            self.display_feedback(msg_type='error',
                                  message='You must be connected to a network to search for a ticker...',
                                  title='No connection')

            # clear entry
            self.ui.search_entry.clear()
            return

        # get market data
        market_state = self.check_market_state()

        # stock
        if self.ticker_type == 'stock' and market_state['state'] == 'Open':
            # set chart to stock chart
            self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)

            # stock info label
            stock_info = market_state['stock_info']

            # day information for stock
            name = self.ticker_obj['longName']
            price = self.ticker_obj['currentPrice']
            prev_close = self.ticker_obj['previousClose']
            change_amount = price - prev_close
            change_percentage = change_amount / prev_close * 100
            symbol = '▲' if change_amount > 0 else '▼'
            # set color
            if symbol == '▲':
                self.ui.stock_change_frame.setStyleSheet("""QLabel{
        color:rgb(0, 255, 0);
        }""")
            else:
                self.ui.stock_change_frame.setStyleSheet("""QLabel{
        color:rgb(255, 0, 0);
        }""")

            # connect command to title for extra info (stock name)
            self.ui.ticker_label_title_analysis.clicked.connect(lambda: self.show_ticker_extraInfoWindow('stock'))
            # set stock header info display
            self.ui.ticker_label_title_analysis.setText(name)
            self.ui.stock_analysis_stock_info_content.setText(stock_info)
            self.ui.price_traded_label.setText(str(price))
            self.ui.change_direction_label.setText(symbol)
            self.ui.change_amount_label.setText(str(round(change_amount, 2)))
            self.ui.change_percentage.setText(f'({str(round(change_percentage, 2))})%')

            # add chart for 1 day
            self.set_chart_and_data('1d')

            # timeframe chart buttons
            self.ui.one_day_button.clicked.connect(lambda: self.set_chart_and_data('1d'))
            self.ui.one_week_button.clicked.connect(lambda: self.set_chart_and_data('1w'))
            self.ui.one_month_button.clicked.connect(lambda: self.set_chart_and_data('1m'))
            self.ui.one_year_button.clicked.connect(lambda: self.set_chart_and_data('1y'))
            self.ui.five_year_button.clicked.connect(lambda: self.set_chart_and_data('5y'))
            self.ui.max_button.clicked.connect(lambda: self.set_chart_and_data('max'))

            # load news
            self.set_news()

            # restore cursor
            QApplication.restoreOverrideCursor()

            # enable search button
            self.ui.search_button.setEnabled(True)

        # cryptocurrency
        if self.ticker_type == 'crypto':
            # set chart to crypto chart
            self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_currency_page)

            # stock info
            crypto_info = market_state['stock_info']

            # quote info for crypto
            name = self.ticker_obj['name']
            pair = self.ticker_obj['symbol']
            price = self.ticker_obj['regularMarketPrice']
            currency = self.ticker_obj['currency']

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

            # button for value of currency calculator
            self.ui.crypto_comparison_button.clicked.connect(lambda: self.calc_crypto_worth(price))

            # add chart for 1 day
            self.set_chart_and_data('1d')

            # link timeframe chart buttons
            self.ui.one_day_button_2.clicked.connect(lambda: self.set_chart_and_data('1d'))
            self.ui.one_week_button_2.clicked.connect(lambda: self.set_chart_and_data('1w'))
            self.ui.one_month_button_2.clicked.connect(lambda: self.set_chart_and_data('1m'))
            self.ui.one_year_button_2.clicked.connect(lambda: self.set_chart_and_data('1y'))
            self.ui.five_year_button_2.clicked.connect(lambda: self.set_chart_and_data('5y'))
            self.ui.max_button_2.clicked.connect(lambda: self.set_chart_and_data('max'))

            # load news
            self.set_news()

            # restore cursor
            QApplication.restoreOverrideCursor()

            # enable search button
            self.ui.search_button.setEnabled(True)

        # closed market won't display data
        if self.ticker_type == 'stock' and market_state['state'] == 'Closed':
            # restore cursor
            QApplication.restoreOverrideCursor()

            # feedback
            txt = 'Market is closed right now. You can search cryptocurrencies.'
            title = 'Market closed'
            self.display_feedback(msg_type='information', message=txt, title=title)

            # enable button
            self.ui.search_button.setEnabled(True)

        # not a valid ticker(equity, crypto)
        if not self.ticker_type:
            # restore cursor
            QApplication.restoreOverrideCursor()

            txt = 'The ticker you entered is either incorrect or there is no data on it'
            title = 'Erroneous data'
            self.display_feedback(msg_type='warning', message=txt, title=title)

            # enable search
            self.ui.search_button.setEnabled(True)

        # enable search button
        self.ui.search_button.setEnabled(True)

    def check_market_state(self):
        """Check market is open

        :returns: Dictionary with data regarding market info
        :rtype: dict
        """

        market_status = ''

        # determine if market is open or closed with the help of yahoo finance site
        session = requests.session()
        response = session.get('https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC')
        if response.status_code == 200:
            # html text
            page = response.text
            soup = BeautifulSoup(page, "html.parser")

            # market description
            market = soup.find_all('div', id='quote-market-notice')
            # convert message e.g. 'As of  10:42AM EST. Market open.' To the last sentence
            market_status = 'Market open' if 'open' in market[0].text else 'Market closed'

        # today's date details
        today = datetime.date.today()

        # current time
        time_now = datetime.datetime.now()
        # am or pm
        am_or_pm = 'AM' if time_now.hour < 12 else 'PM'

        # make one digit numbers 2-digit with a zero in front
        h = f'0{time_now.hour}' if len(str(time_now.hour)) == 1 else f'{time_now.hour}'
        m = f'0{time_now.minute}' if len(str(time_now.minute)) == 1 else f'{time_now.minute}'

        # Description about ticker based on what it is
        msg = f"- {market_status}" if self.ticker_type == "stock" else ''
        m_state = 'Open' if market_status == 'Market open' else 'Closed'
        stock_info = today.strftime(f'%A %d %B, {h}:{m} {am_or_pm} {msg}')

        return {'state': m_state, 'stock_info': stock_info}

    def calc_crypto_worth(self, worth_of_one_unit):
        """Calculate the worth of n amount of crypto currency and output

        :param float worth_of_one_unit: Value of a single unit of the crypto currency
        """

        # Quantity
        amount = self.ui.first_currency_entry.text()

        # Total worth
        final_val = int(amount) * worth_of_one_unit

        # set text
        self.ui.second_currency_entry.setText(str(final_val))

    def add_line_to_graph(self, date, close):
        """Add lines to graph"""

        if self.ticker_type == 'stock':
            # range
            self.stock_graphWidget.setYRange(min(close), max(close))
            self.stock_graphWidget.setXRange(min(date), max(date))

            # plot data: x, y values
            axis = pyqtgraph.DateAxisItem()
            self.stock_graphWidget.setAxisItems({'bottom': axis})
            self.stock_graphWidget.enableMouse(False)
            self.stock_graph_line = self.stock_graphWidget.plot(x=date, y=close, symbolBrush=0.2, name='green')

        if self.ticker_type == 'crypto':
            # range
            self.crypto_graphWidget.setYRange(min(close), max(close))
            self.crypto_graphWidget.setXRange(min(date), max(date))

            # plot data: x, y values
            axis = pyqtgraph.DateAxisItem()
            self.crypto_graphWidget.setAxisItems({'bottom': axis})
            self.crypto_graphWidget.enableMouse(False)
            self.crypto_graph_line = self.crypto_graphWidget.plot(x=date, y=close, symbolBrush=0.2, name='green')

    def set_chart_and_data(self, time_period):
        """Shows the line chart and info for a specific timeframe in the gui"""

        # delete previous lines
        if self.crypto_graph_line is not None:
            self.crypto_graph_line.clear()
        if self.stock_graph_line is not None:
            self.stock_graph_line.clear()

        if time_period == '1d':
            if self.ticker_type == 'stock':
                # reset stock info entries, to allocate day entries and also set page to display
                self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_stock_page)
                self.reset_entries_for_stock_info_display('day')

            if self.ticker_type == 'crypto':
                self.ui.stock_analysis_stackedWidget.setCurrentWidget(self.ui.stock_analysis_currency_page)

            # get dataframe for 1d worth of stocks
            df = self.get_data_for_chart(self.ticker, time_period)

            # data lists for plot
            date = []
            close = []

            # add data to lists
            for index, row in df.iterrows():
                date.append(index)
                close.append(row['Close'])

            # convert date timestamps to int(seconds)
            date = [i.timestamp() for i in date]

            # add line to graph with data from lists
            self.add_line_to_graph(date, close)

            # add stock data to labels
            if self.ticker_type == 'stock':
                # add info about stock
                # required info
                volume = self.ticker_obj['volume']
                avg_volume = self.ticker_obj['averageVolume']
                open_price = self.ticker_obj['open']
                high = self.ticker_obj['dayHigh']
                low = self.ticker_obj['dayLow']
                mkt_cap = self.ticker_obj['marketCap']
                fifty_two_week_high = self.ticker_obj['fiftyTwoWeekHigh']
                fifty_two_week_low = self.ticker_obj['fiftyTwoWeekLow']
                # set chart info display
                self.ui.day_open_placeholder.setText(str(open_price))
                self.ui.day_high_placeholder.setText(str(high))
                self.ui.day_low_placeholder.setText(str(low))
                self.ui.volume_placeholder.setText(self.format_money(volume))
                self.ui.avg_volume_placeholder.setText(self.format_money(avg_volume))
                self.ui.market_cap_placeholder.setText(self.format_money(mkt_cap))
                self.ui.fifty_two_week_high_placeholder.setText(str(fifty_two_week_high))
                self.ui.fifty_two_week_low_placeholder.setText(str(fifty_two_week_low))

        else:
            # place new stock data entries for non day entries
            if self.ticker_type == 'stock':
                self.reset_entries_for_stock_info_display('not_day')

            # dataframe for stock
            df = self.get_data_for_chart(self.ticker, time_period)

            if self.ticker_type == 'stock':
                # values from entries
                all_data = list(df['Close'].values)
                highest = max(all_data)
                lowest = min(all_data)
                avg = (highest + lowest) / 2

                # close date
                date = df[df['Close'] == highest].index

                # add info to entries
                self.ui.day_high_placeholder.setText(str(round(highest, 2)))
                self.ui.day_low_placeholder.setText(str(round(lowest, 2)))
                self.ui.day_open_placeholder.setText(str(round(avg, 2)))

            # data for plot
            date = []
            close = []

            # add data to lists
            for index, row in df.iterrows():
                date.append(index)
                close.append(row['Close'])

            # convert date timestamps to int(seconds)
            date = [i.timestamp() for i in date]

            # add line to graph with data from df
            self.add_line_to_graph(date, close)

    @staticmethod
    def get_data_for_chart(ticker, time_period):
        """Get data required for a stock and required time range

        :param str ticker: The ticker to be searched
        :param str time_period: Data time range

        :returns: Data for the ticker, within the provided time range
        :rtype: pandas.core.frame.DataFrame
        """

        # ticker obj
        ticker = yf.Ticker(ticker)

        if time_period == '1d':
            # 1 day data for the stock at 5 minute intervals
            data = ticker.history(period='1d', interval='5m')
            return data

        # // FIX THIS (gives very inaccurate and strange data) ---------------
        if time_period == '1w':
            # 1 week data for the stock at 15 minute interval
            data = ticker.history(period='5d', interval='15m')
            return data
        # //-------------------------------------------------------------------------------------------------------------------

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
        """Organizes the labels shown for a stock in the search section

        :param str new: Determines what type of data labels are shown for the stock charts
        """

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
            self.ui.avg_volume.setText('Avg Volume')
            self.ui.fifty_two_week_high.setText('52wK High')
            self.ui.fifty_two_week_low.setText('52wK Low')
            self.ui.market_cap.setText('Mkt Cap')

    def stock_or_crypto(self):
        """Determine whether the given ticker is a stock or cryptocurrency

        :returns: The type of ticker
        :rtype: str, bool
        """

        try:
            # Anytime a ticker is used it is placed on the 'self.ticker_obj' var.
            # this allows for access and modification through the whole class and specifically its 'info' method
            if self.ticker_obj['quoteType'] == 'EQUITY':
                return 'stock'
            elif self.ticker_obj['quoteType'] == 'CRYPTOCURRENCY':
                return 'crypto'
            elif self.ticker_obj['quoteType'] == 'MUTUALFUND':
                return 'mutual fund'

            else:
                return False
        except KeyError:
            return False

    def show_ticker_extraInfoWindow(self, ticker_type):
        """Window with more info regarding ticker

        :param str ticker_type: Type of ticker being searched
        """

        # This will open a new window in ticker search page regarding the searched ticker
        ticker_window = TickerInfo(self.ticker, ticker_type)

    def set_news(self):
        """Load related news for given ticker, happens in a different thread as it is a long process"""

        # link
        linkTemplate = '<p><a href={0}>{1}</p>'

        # loaded from a different thread
        with open(os.getcwd() + '\\temp\\search\\TickerNews.json', 'r') as f:
            data = json.load(f)

        # file contents
        news = data

        # these just signify where the news boxes are located
        layouts = None
        if self.ticker_type == 'stock':
            # layouts
            layouts = (self.ui.horizontalLayout_23, self.ui.horizontalLayout_24, self.ui.horizontalLayout_25,
                       self.ui.horizontalLayout_27)

        if self.ticker_type == 'crypto':
            # layouts
            layouts = (self.ui.horizontalLayout_28, self.ui.horizontalLayout_29, self.ui.horizontalLayout_30,
                       self.ui.horizontalLayout_31)

        # Here is how this works:
        # 4 rows (as seen in layouts), each row(layout) has three boxes. Each box has a piece of news.
        # Each iteration goes through a row, in this we get the title, body and link frames in each box (3)
        # This is done by traversing the layouts and widgets within until getting to the required ones
        # and thus setting them with the required text
        # The variable counter just helps with getting 3 items from the news dict at according to the loop
        counter = 0
        for layout in layouts:
            try:
                # first_box variables
                title_1 = layout.itemAt(0).widget().layout().itemAt(0).widget().layout().itemAt(0).widget()
                text_1 = layout.itemAt(0).widget().layout().itemAt(1).widget().widget().layout().itemAt(0).widget()
                date_1 = layout.itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(0).widget()
                dot_1 = layout.itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(1).widget()
                source_and_link_1 = layout.itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(2).widget()

                # second box variables
                title_2 = layout.itemAt(1).widget().layout().itemAt(0).widget().layout().itemAt(0).widget()
                text_2 = layout.itemAt(1).widget().layout().itemAt(1).widget().widget().layout().itemAt(0).widget()
                date_2 = layout.itemAt(1).widget().layout().itemAt(2).widget().layout().itemAt(0).widget()
                dot_2 = layout.itemAt(1).widget().layout().itemAt(2).widget().layout().itemAt(1).widget()
                source_and_link_2 = layout.itemAt(1).widget().layout().itemAt(2).widget().layout().itemAt(2).widget()

                # third box variables
                title_3 = layout.itemAt(2).widget().layout().itemAt(0).widget().layout().itemAt(0).widget()
                text_3 = layout.itemAt(2).widget().layout().itemAt(1).widget().widget().layout().itemAt(0).widget()
                date_3 = layout.itemAt(2).widget().layout().itemAt(2).widget().layout().itemAt(0).widget()
                dot_3 = layout.itemAt(2).widget().layout().itemAt(2).widget().layout().itemAt(1).widget()
                source_and_link_3 = layout.itemAt(2).widget().layout().itemAt(2).widget().layout().itemAt(2).widget()

                # set the data(1st)
                title_1.setText(news[counter]['title'])
                text_1.setText(news[counter]['description'])
                date_1.setText(news[counter]['time'])
                dot_1.setText('•')

                hyperlink = linkTemplate.format(news[counter]['link'], news[counter]['source'])
                source_and_link_1.setOpenExternalLinks(True)
                source_and_link_1.setText(hyperlink)

                # set the data(2nd)
                title_2.setText(news[counter + 1]['title'])
                text_2.setText(news[counter + 1]['description'])
                date_2.setText(news[counter + 1]['time'])
                dot_2.setText('•')

                hyperlink = linkTemplate.format(news[counter + 1]['link'], news[counter + 1]['source'])
                source_and_link_2.setOpenExternalLinks(True)
                source_and_link_2.setText(hyperlink)

                # set the data(3rd)
                title_3.setText(news[counter + 2]['title'])
                text_3.setText(news[counter + 2]['description'])
                date_3.setText(news[counter + 2]['time'])
                dot_3.setText('•')

                hyperlink = linkTemplate.format(news[counter + 2]['link'], news[counter + 2]['source'])
                source_and_link_3.setOpenExternalLinks(True)
                source_and_link_3.setText(hyperlink)

                # move to next row (layout)
                counter += 3
            except IndexError:
                break

    def simulator_login(self):
        """Login to trading simulator"""

        # user_name
        user_name = self.ui.simulator_login_to_username_entry.text()

        # use stock game class to verify user exists
        exists = self.stock_game.user_exists(user_name)

        if exists:
            # user exists
            # load user in stock game
            self.stock_game.load_user(user_name)

            # since user found, display informative feedback
            self.display_feedback(message=f'Welcome {user_name}', title="Success", msg_type='information')

            # add user details to stock page
            self.add_user_data_to_simulator_tabs(self.stock_game.current_user)

            # set current page to actual simulator
            self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.stock_simulator_page)

            # End function here
            return

        # if the user was not found
        txt = 'The user is not does not exist. Check the json file to find it.\n ' \
              'You can directly access it or go to setting to see its location.\n' \
              'You can also create a new user if you want to.'
        title = "User not found"

        # feedback
        self.display_feedback(message=txt, msg_type='warning', title=title)

    def simulator_register(self):
        """Create new user for stock simulator"""

        # user
        new_user = self.ui.simulator_new_username_entry.text()

        # if user does exists don't create
        if not self.stock_game.user_exists(new_user):
            # create new user
            self.stock_game.create_user(new_user)

            # display feedback
            self.display_feedback(msg_type='information', msg='User successfully created.', title='Success')

            # return to login
            self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_login_page)

        else:
            # if user exists don't create
            self.display_feedback(msg_type='critical', msg='User already exists. Enter another name', title='Error')

    def add_user_data_to_simulator_tabs(self, user_data):
        """Fill in user tables in simulator

        :param dict user_data: Dictionary representing the user to be used

        user_data dict format
        {
            "user_id": ?,
            "data": {
                "user_name": "?",
                "account_value": ?,
                "cash": ?,
                "portfolio": [
                    {
                        "?": {
                            "purchase_price": ?,
                            "quantity": ?,
                            "total_value": ?
                        }
                    }
                ]
            }
        }

        """

        # account data
        name = user_data['data']['user_name']
        number_of_stocks = len(user_data['data']['portfolio'])
        account_value = user_data['data']['account_value']
        cash = user_data['data']['cash']

        # set account data into user profile labels (Portfolio tab)
        self.ui.stock_simulator_username_label.setText(str(name))
        self.ui.stock_simulator_account_value_label.setText(str(account_value))
        self.ui.stock_simulator_cash_amount_label.setText(str(cash))
        self.ui.stock_simulator_gainloss_label.setText(str(0))

        # More user data(account tab)
        self.ui.stock_simulator_username_label_2.setText(str(name))
        portfolio_length = len(self.stock_game.get_portfolio())
        self.ui.stock_simulator_stocks_owned_label.setText(str(portfolio_length))

        # table widget
        table = self.ui.tableWidget
        num_column = 7
        # remove previous rows if there are any
        for i in reversed(range(table.rowCount())):
            table.removeRow(i)

        # set loading cursor for lengthy process of fetching user data
        QApplication.setOverrideCursor(Qt.WaitCursor)

        try:
            # loop repeats number of rows(stock)
            for i in range(number_of_stocks):

                # Access each stock through its index
                stock = list(user_data['data']['portfolio'][i].keys())[0]

                # More stock data
                ticker = yf.Ticker(stock).info
                stock_symbol = ticker['symbol']
                stock_name = ticker['longName']
                current_price = ticker['regularMarketPrice']
                prev_close = ticker['previousClose']
                change_percentage = (current_price - prev_close) / prev_close * 100
                purchase_price = user_data['data']['portfolio'][i][stock]['initial_purchase_price']
                quantity = user_data['data']['portfolio'][i][stock]['quantity']
                total_value = current_price * quantity

                # insert row into table for the stock
                table.insertRow(i)

                # add data to fields
                table.setItem(i, 0, QTableWidgetItem(str(stock_symbol)))
                table.setItem(i, 1, QTableWidgetItem(str(stock_name)))
                table.setItem(i, 2, QTableWidgetItem(str(current_price)))
                table.setItem(i, 3, QTableWidgetItem(str(change_percentage)))
                table.setItem(i, 4, QTableWidgetItem(str(purchase_price)))
                table.setItem(i, 5, QTableWidgetItem(str(quantity)))
                table.setItem(i, 6, QTableWidgetItem(str(total_value)))

                # set text color and background color for each element in the row
                for column_num in range(num_column):
                    # i - row number, column_num - column number
                    table.item(i, column_num).setForeground(QColor(255, 255, 255))
                    table.item(i, column_num).setBackground(QColor(34, 35, 40))
        except requests.exceptions.ConnectionError:
            # If this exception occurs it means the user is not connected to  a network.
            # Load data again, without using yf

            QApplication.restoreOverrideCursor()
            self.display_feedback(message='You aren\'t connected to a network', msg_type='error', title='No internet')
            QApplication.setOverrideCursor(Qt.WaitCursor)

            for i in range(number_of_stocks):
                # Access each stock through its index
                #stock = list(user_data['data']['portfolio'][i].keys())[0]

                # stock data
                purchase_price = user_data['data']['portfolio'][i][stock]['initial_purchase_price']
                quantity = user_data['data']['portfolio'][i][stock]['quantity']

                # insert row into table for the stock
                table.insertRow(i)
                line = '_'

                # add data to fields
                table.setItem(i, 0, QTableWidgetItem(str(stock)))
                table.setItem(i, 1, QTableWidgetItem(str(line)))
                table.setItem(i, 2, QTableWidgetItem(str(line)))
                table.setItem(i, 3, QTableWidgetItem(str(line)))
                table.setItem(i, 4, QTableWidgetItem(str(purchase_price)))
                table.setItem(i, 5, QTableWidgetItem(str(quantity)))
                table.setItem(i, 6, QTableWidgetItem(str(line)))

                # set text color and background color for each element in the row
                for column_num in range(num_column):
                    # i - row number, column_num - column number
                    table.item(i, column_num).setForeground(QColor(255, 255, 255))
                    table.item(i, column_num).setBackground(QColor(34, 35, 40))

        # close loading cursor as lengthy process of fetching user data is now over
        QApplication.restoreOverrideCursor()

    def simulator_stock_lookup(self):
        """Lookup a ticker whilst in the trading simulator"""

        # change pages
        self.ui.stacked_menu_pages.setCurrentWidget(self.ui.stock_analysis)

        # ticker user searched
        ticker = self.ui.stock_simulator_stock_ticker_entry.text()

        # set ticker
        self.ui.search_entry.setText(str(ticker))

        # run thread
        self.ticker_search_thread()

    def simulator_clear_entries(self):
        """Clear entries used for search in the simulator"""

        self.ui.stock_simulator_stock_ticker_entry.clear()
        self.ui.stock_simulator_quantity_entry.clear()

    def simulator_logout(self):
        """Logout of simulator"""

        # technically speaking this isn't a logout
        # because all it does is change to the frame to the login page
        # but still does the job
        self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_start_page)

    def preview_order(self):
        """Preview order"""

        QApplication.setOverrideCursor(Qt.WaitCursor)

        # entries data
        stock_name = self.ui.stock_simulator_stock_ticker_entry.text().upper()
        transaction_type = self.ui.stock_simulator_transaction_type_combobox.currentText().lower()
        quantity = int(self.ui.stock_simulator_quantity_entry.text())

        # verify stock
        stock_name = stock_name.upper()
        self.ticker = stock_name
        try:
            data = yf.Ticker(self.ticker).info
            self.ticker_obj = data

            ticker_type = self.stock_or_crypto()

            if not ticker_type:
                # random excepetion
                raise ValueError

        except requests.exceptions.ConnectionError:
            QApplication.restoreOverrideCursor()
            self.display_feedback(message='You need to connect to a network', msg_type='error', title='No internet')
            self.simulator_clear_entries()
            return

        except ValueError:
            QApplication.restoreOverrideCursor()
            self.display_feedback(message='You can only sell any equity(stock) you own. You can buy any valid equity.',
                                  msg_type='error', title='Error')
            self.simulator_clear_entries()
            return

        # data about stock
        bid = self.ticker_obj['bid']
        ask = self.ticker_obj['bid']
        full_name = self.ticker_obj['longName']
        total_spread = (ask - bid) * int(quantity)
        total = str(bid * quantity) if transaction_type == 'buy' else str(ask * quantity)

        # ticker
        if ticker_type == 'stock' and int(quantity) > 0:
            # SET TEXT
            self.ui.stock_name.setText(str(full_name))
            self.ui.price_label.setText(str(bid if transaction_type == 'buy' else ask))
            self.ui.quantity_label.setText(str(quantity))
            self.ui.total_spread_label.setText(str(total_spread))
            self.ui.label_11.setText(str(int(bid if transaction_type == 'buy' else ask) * int(quantity)))
            self.ui.label_24.setText(total)
            self.ui.stock_simulator_purchase_confirm_btn.setText('BUY' if transaction_type == 'buy' else 'SELL')

            # valid trade
            self.ui.stock_sim_trade_stackedWidget.setCurrentWidget(self.ui.stock_simulator_confirm_transaction_page)

            # finally update and perform trade on portfolio
            self.ui.stock_simulator_purchase_confirm_btn.clicked.connect(
                lambda: self.perform_stock_trade(stock_name, transaction_type, quantity))

            # cancel order button
            self.ui.stock_simulator_purchase_camcel_btn.clicked.connect(
                lambda: self.ui.stock_sim_trade_stackedWidget.setCurrentWidget(self.ui.stock_simulator_trade_page_tab))
            QApplication.restoreOverrideCursor()

        else:
            QApplication.restoreOverrideCursor()
            txt = 'Missing or invalid entries'
            title = 'Error'
            # msg
            self.display_feedback(title=title, message=txt, msg_type='critical')

    def perform_stock_trade(self, stock_name, transaction_type, quantity):
        """Buy or sell stock

        :param str stock_name: Name of stock to be bought or sold
        :param int quantity: Units of the given stock to be bought or sold
        :param str transaction_type: Type of transaction, can either be buy or sell
        """

        QApplication.setOverrideCursor(Qt.WaitCursor)

        if transaction_type == 'buy':
            # buy stock for user
            self.stock_game.buy(stock_name, quantity)

        if transaction_type == 'sell':
            # sell stock for user
            self.stock_game.sell(stock_name, quantity)

        # update portfolio
        self.stock_game.load_user(self.stock_game.name)
        self.add_user_data_to_simulator_tabs(self.stock_game.current_user)

        QApplication.restoreOverrideCursor()

        # feedback and return to previous page
        self.display_feedback(msg_type='information', title='Success',
                              msg='Stock successfully sold' if transaction_type == 'sell' else \
                                  'Stock successfully bought')

        # return to previous page
        self.ui.stock_sim_trade_stackedWidget.setCurrentWidget(self.ui.stock_simulator_trade_page_tab)

    def simulator_delete_user(self):
        """Delete account from trading simulator"""

        # delete user
        user = self.stock_game.name
        self.stock_game.delete_user(user)

        # message
        self.display_feedback(msg_type='information', msg='User successfully deleted', title='Success')

        # update table data
        self.update_trading_settings_pg_data()

        # return to start
        self.ui.simulator_stacked_widget.setCurrentWidget(self.ui.simulator_start_page)

    def update_trading_settings_pg_data(self):
        """Displays table with stock game users and display original file in settings"""

        QApplication.setOverrideCursor(Qt.WaitCursor)

        # files
        file = os.getcwd() + '\\trading.json'
        file_location_str = f'File Location: {file}'

        with open(file) as f:
            # for original file display
            txt = f.read()

        with open(file) as f:
            # for table display
            file_data = json.load(f)
            users = [user for user in file_data['users']]

        # table display
        table = self.ui.settings_users_table
        # remove previous rows
        for i in reversed(range(table.rowCount())):
            table.removeRow(i)
        num_column = 4
        i = 0
        for user in users:
            # data
            user_id = user['user_id']
            user_name = user['data']['user_name']
            cash = user['data']['cash']
            stocks_owned = len(user['data']['portfolio'])

            # insert row
            table.insertRow(i)

            # add data
            table.setItem(i, 0, QTableWidgetItem(str(user_id)))
            table.setItem(i, 1, QTableWidgetItem(str(user_name)))
            table.setItem(i, 2, QTableWidgetItem(str(cash)))
            table.setItem(i, 3, QTableWidgetItem(str(stocks_owned)))

            # colors
            # set text color and background color for each row
            for column_num in range(num_column):
                try:
                    # i - row number, column_num - column number
                    table.item(i, column_num).setTextColor(QColor(255, 255, 255))
                    table.item(i, column_num).setBackgroundColor(QColor(42, 44, 50))
                except AttributeError:
                    pass

            i += 1

        # original file display
        for _ in txt:
            self.ui.settings_original_file_edit.setPlainText(str(txt))
        # file location sub heading
        self.ui.setting_users_file_location.setText(str(file_location_str))

        QApplication.restoreOverrideCursor()

        # after having set the page, go to the page
        self.go_to_sim_users_pg()

    def go_to_sim_users_pg(self):
        """Go to setting simulator users page"""

        self.ui.settings_stackedWidget.setCurrentWidget(self.ui.settings_sim_users)

    @staticmethod
    def display_feedback(**kwargs):
        """To help with alert messages"""

        # params
        try:
            msg_type = kwargs['msg_type']
            message = kwargs['message']
            title = kwargs['title']
        except KeyError:
            msg_type = 'information'
            message = 'Something happened'
            title = 'Feedback'

        # obj
        msg_obj = QMessageBox()

        # messages
        if msg_type.lower() == 'error':
            msg_obj.setWindowTitle("Error")
            msg_obj.setIcon(QMessageBox.Critical)

        if msg_type.lower() == 'information':
            msg_obj.setWindowTitle("Information")
            msg_obj.setIcon(QMessageBox.Information)

        if msg_type.lower() == 'warning':
            msg_obj.setWindowTitle("Warning")
            msg_obj.setIcon(QMessageBox.Warning)

        if msg_type.lower() == 'critical':
            msg_obj.setWindowTitle("Critical")
            msg_obj.setIcon(QMessageBox.Critical)

        # execute
        msg_obj.setText(message)
        msg_obj.setWindowTitle(title)
        msg_obj.exec_()

    @staticmethod
    def format_money(num, sign=None):
        """Convert long decimal numbers into cleaner format

        :param sign: Sign to be used, optional
        :param float num: The number to be formated

        :returns: Simplified version of the number with signs
        :rtype: str
        """

        # long float number such as 765465.6742356097843416769
        num = float(num)

        # decimal val of the number eg 4564.675 would be '675'
        decimal_value = str(round(num, 2)).split('.')[1]
        # number without decimal part eg 78567.7657 becomes '78567'
        version_no_float = int(round(num, 0))

        # number but with comas eg 1000000 becomes '1,000,000'
        num_with_comas = str("{:,}".format(version_no_float))

        # length of the number(with no decimals)
        length = len(str(version_no_float))
        # true for small numbers, false for abnormal numbers
        normal = True if length <= 6 else False

        # decide prefix
        prefix = 'q'
        if 7 <= length <= 9:
            prefix = 'million'

        elif 10 <= length <= 12:
            prefix = 'billion'

        elif 13 <= length <= 15:
            prefix = 'trillion'

        # get num
        # non decimal part with no comas
        sections = num_with_comas.split(',')
        # take first num eg from ['18','000','000'] it is 18
        first_part = sections[0]

        # for values over 1,000,000
        large_num = '.'.join([first_part, decimal_value]) if decimal_value != '0' else f'{first_part}.{sections[1][:2]}'

        # for values under 1,000,000
        short_num = '.'.join([num_with_comas, decimal_value]) if decimal_value != '0' else num_with_comas
        final_str = f'{large_num} {prefix[0].upper()}' if not normal else short_num

        if sign:
            return f'{sign}{str(final_str)}'

        else:
            return str(final_str)


class TickerInfo(QMainWindow):
    def __init__(self, ticker, ticker_type):
        """Shows extra information for a selected ticker in ticker search page"""
        QMainWindow.__init__(self)

        # gui elements
        self.ui = Ticker_Window()
        self.ui.setupUi(self)
        self.setFixedSize(710, 550)

        # buttons
        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)

        # ticker object
        ticker_obj = yf.Ticker(ticker)

        if ticker_type == 'stock':
            # buttons
            self.ui.stats_btn.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.stock_statistics_page))
            self.ui.profile_btn.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.stock_profile_page))

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

        elif ticker_type == 'crypto':
            # buttons
            # self.ui.stats_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cry))
            self.ui.profile_btn.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.crypto_profile_page))

            summary = ticker_obj.info['description']
            summary = re.sub("(.{64})", "\\1\n", summary, 0, re.DOTALL)
            self.ui.ticker_name.setText(ticker_obj.info['name'])
            self.ui.crypto_summary.setText(f"{summary}")
            self.ui.crypto_market.setText(f"{ticker_obj.info['market']}")

        # show window
        self.show()


class StockGame:
    def __init__(self):
        """
        current user dict format
        {
            "user_id": ?,
            "data": {
                "user_name": "?",
                "account_value": ?,
                "cash": ?,
                "portfolio": [
                    {
                        "?": {
                            "purchase_price": ?,
                            "quantity": ?,
                            "total_value": ?
                        }
                    }
                ]
            }
        }
        """

        # check file exists
        self.file_exists()

        self.name = None
        self.current_user = None

    @staticmethod
    def reset_id_numbers():
        """Reset id numbers in json file"""

        # Writing to trading.json
        with open("trading.json", "r+") as file:
            # load file
            file_data = json.load(file)
            # reset user_ids
            id_count = 1
            for val in file_data['users']:
                val['user_id'] = id_count  # set new id
                # increment id count
                id_count += 1

            # move to file_data to json file
            file.seek(0)
            json.dump(file_data, file, indent=4)

    def create_user(self, name):
        """Create new user"""

        # if the user exists, exit function
        if self.user_exists(name):
            return

        # Writing to trading.json
        with open("trading.json", "r+") as file:
            # load file
            file_data = json.load(file)

            # determine id for new user through file length
            user_id = len(file_data['users']) + 1

            # dict of user
            user_info = {

                "user_id": user_id, "data": {"user_name": name, "account_value": 0, "cash": 100000, "portfolio": []}
            }

            # add new user to json file users
            file_data["users"].append(user_info)

            # move to file_data to json file
            file.seek(0)
            json.dump(file_data, file, indent=4)

    def delete_user(self, name):
        """Delete user from json file"""

        # if the user does not exist, exit function
        if not self.user_exists(name):
            return

        # Writing to trading.json
        with open("trading.json", "r+") as file:
            # load file
            file_data = json.load(file)

            # locate user id
            for val in file_data['users']:
                if name == val['data']['user_name']:
                    # if the id is found, break loop
                    user_id = val['user_id']
                    break

            # rebuild dict
            new_data = {"users": [data for data in file_data['users'] if data['user_id'] != user_id]}

        # move new_data to new json file
        with open("trading.json", "w") as file:
            json.dump(new_data, file, indent=4)

        # reset/match ids
        self.reset_id_numbers()

    def load_user(self, name):
        """Load user from json file to game"""

        # if user does not exist, exit function
        if not self.user_exists(name):
            return

        # open json
        with open("trading.json", 'r+') as file:
            file_data = json.load(file)

            # Loop trough all the users
            for val in file_data['users']:
                # Find the matching name
                if val['data']['user_name'] == name:
                    self.name = name
                    # if the name matches, set StockGame current user to val
                    self.current_user = val
                    return val

    def buy(self, ticker, quantity):
        """Purchase a stock"""

        # check user has been loaded
        if self.current_user is None:
            return

        # user financial data
        cash = self.current_user["data"]["cash"]
        account_value = self.current_user["data"]["account_value"]

        # yfinance stock object
        ticker_obj = yf.Ticker(ticker).info

        # ticker name
        ticker_name = ticker_obj['symbol']
        # current real time price of ticker
        value = ticker_obj['regularMarketPrice']
        total_value = value * quantity

        # purchase/transaction cost
        price = ticker_obj['bid']
        total_cost_of_buy = price * quantity

        # check if user has the stock
        exists, index = self.user_has_stock(ticker.upper())

        # if the stock does not exist in the user portfolio
        # it is a first time purchase
        if not exists:

            # ticker data to add to portfolio
            holding = {ticker_name: {"initial_purchase_price": price, "quantity": quantity, "total_value": total_value}}

            # open json
            with open("trading.json", "r+") as file:
                # load file
                file_data = json.load(file)

                # add user info to list
                for val in file_data['users']:
                    # find the matching user
                    if val["data"]["user_name"] == self.current_user["data"]["user_name"]:
                        # add stock data(holding) to portfolio
                        val["data"]["portfolio"].append(holding)

                        # update cash available
                        cash_left = val["data"]["cash"] - total_cost_of_buy
                        val["data"]["cash"] = cash_left

                        print("---------RECEIPT----------")
                        print(f"Stock: {ticker_name}")
                        print(f"Quantity: {quantity}")
                        print(f"1 share worth: £{price}")
                        print(f"Total cost: £{price * quantity}")
                        print(f"--------PURCHASE---------")
                        print(f"Cash available: £{cash}")
                        print(f"Cash after purchase: £{cash_left}")
                        print("---------------------------")
                        print('\n\n')

                # move to json file
                file.seek(0)
                json.dump(file_data, file, indent=4)

        # if the stock does exist in the user portfolio
        # just need to update the values
        if exists:

            # open json
            with open("trading.json", "r+") as file:
                # load file
                file_data = json.load(file)

                # find user
                for val in file_data['users']:
                    if val["data"]["user_name"] == self.current_user["data"]["user_name"]:
                        # replace user quantity for the stock with new quantity
                        val["data"]["portfolio"][index][ticker_name]["quantity"] = \
                            self.current_user["data"]["portfolio"][index][ticker_name]["quantity"] + quantity

                        # replace user total value for the stock with new total value
                        val["data"]["portfolio"][index][ticker_name]["total_value"] = \
                            self.current_user["data"]["portfolio"][index][ticker_name]["total_value"] + total_value

                        # cash left available
                        cash_left = val["data"]["cash"] - total_cost_of_buy
                        val["data"]["cash"] = cash_left

                file.seek(0)

                # move to json file
                json.dump(file_data, file, indent=4)

        # after each purchase the current user data must also be updated
        self.load_user(self.name)

    def sell(self, ticker, quantity):
        """Sell a stock"""

        # check user has been loaded
        if self.current_user is None:
            return

        # flag to determine whether the stock is to be deleted
        delete_stock = False

        # user financial data
        cash = self.current_user["data"]["cash"]
        account_value = self.current_user["data"]["account_value"]

        # yfinance stock object
        ticker_obj = yf.Ticker(ticker).info

        # ticker name
        ticker_name = ticker_obj['symbol']
        # current real time price of ticker
        value = ticker_obj['regularMarketPrice']
        total_value = value * quantity

        # sell cost
        ask_price = ticker_obj['ask']
        total_cost_of_sell = ask_price * quantity

        # check if user has the stock
        exists, index = self.user_has_stock(ticker)

        if exists:
            # open json
            with open("trading.json", "r+") as file:
                # load file
                file_data = json.load(file)

                # add user info to list
                for val in file_data['users']:
                    # find the matching user
                    if val["data"]["user_name"] == self.current_user["data"]["user_name"]:
                        # add stock data(holding) to portfolio
                        for my_stock in val['data']['portfolio']:
                            # get name for current stock in list
                            stock_symbol = list(my_stock.keys())[0]
                            if stock_symbol == ticker_name:
                                # original quantity
                                original_quantity = self.current_user['data']['portfolio'][index][ticker_name][
                                    'quantity']

                                # new quantity
                                new_quantity = original_quantity - quantity
                                val['data']['portfolio'][index][ticker_name]['quantity'] = new_quantity

                                # total value
                                total_value = new_quantity * value
                                val['data']['portfolio'][index][ticker_name]['total_value'] = total_value

                                # profit
                                val['data']['cash'] = cash + total_cost_of_sell
                                print('HI')

                                if new_quantity <= 0:
                                    # delete the stock if the value is all lost
                                    delete_stock = True
                                    # rebuild dict
                                    new_data = [data for data in val['data']['portfolio'] if
                                                list(data.keys())[0] != ticker_name]

                                    # clear user portfolio
                                    val['data']['portfolio'].clear()

                                    # add all stocks except deleted one
                                    for data in new_data:
                                        val['data']['portfolio'].append(data)

                                    # assign this version to a new variable
                                    deleted_stock_file = file_data

            # rewrite data to new file
            with open('trading.json', 'w') as file:
                if delete_stock:
                    json.dump(deleted_stock_file, file, indent=4)

                elif not delete_stock:
                    json.dump(file_data, file, indent=4)

        if not exists:
            print('The user does not have the stock')

        # after each sell the current user data must also be updated
        self.load_user(self.name)

    @staticmethod
    def user_exists(name):
        """Confirm if a user exists in the json"""

        # Writing to trading.json
        with open("trading.json", "r+") as file:
            # load file
            file_data = json.load(file)

            for val in file_data['users']:
                # find matching name
                if val['data']['user_name'] == name:
                    print('User exists')
                    return True
        return False

    def user_has_stock(self, ticker):
        """Confirm user owns stock

        return bool and index of item in portfolio
        """

        # obj
        ticker_obj = yf.Ticker(ticker).info

        # index
        index = 0
        # loop through the entire portfolio until a match is found
        for stock in self.current_user["data"]["portfolio"]:
            try:
                # name of current stock
                name = list(stock.keys())[0]
                # if exists return true and index
                if name == ticker:
                    return [True, index]
            except KeyError:
                continue

            # index for next item in portfolio list
            index += 1
        return [False, None]

    def get_portfolio(self):
        """Return portfolio"""

        # check user has been loaded
        if self.current_user is None:
            return

        return self.current_user['data']['portfolio']

    @staticmethod
    def file_exists():
        """Ensure trading.json exists"""

        try:
            with open("trading.json", "r") as f:
                pass

        except FileNotFoundError:
            # file doesn't exist
            with open("trading.json", "w") as jsonFile:
                json_obj = {"users": []}
                json.dump(json_obj, jsonFile, indent=4)


class LoadTickerData(QObject):
    thread_is_done = pyqtSignal(bool)
    progress = pyqtSignal(int)
    message = pyqtSignal(str)
    error_message = pyqtSignal(str)

    # the user is on the search page
    search_page = False

    # bar count
    count = 0

    @pyqtSlot()
    def run(self):

        self.show_message(f'Please wait, the time this takes\n relies on your network connection...')

        # bar
        self.increase_progress_bar(5, 'slow')

        # get ticker data
        with open(os.getcwd() + '\\temp\\Ticker.json', 'r') as f:
            data = json.load(f)

        ticker_name = data['ticker']
        show_news = data['news']
        path = data['path']

        if path == os.getcwd() + '\\temp\\search':
            # to handle messages and progress bar
            self.search_page = True
        else:
            self.search_page = False

        # load data to designated files
        try:
            self.load_data(ticker_name, news=show_news, file_path=path)

        except requests.exceptions.ConnectionError:
            self.error_message.emit('You need to connect to a network')
            self.thread_done(False)

    def show_message(self, msg):
        """Display message under progressbar in search page"""

        if self.search_page:
            self.message.emit(msg)

    def increase_progress_bar(self, val, speed):
        """Increase progressbar in search page"""

        if self.search_page:
            for i in range(val):
                self.count += 1
                self.progress.emit(self.count)

                if speed == 'normal':
                    time.sleep(.1)

                if speed == 'slow':
                    time.sleep(.8)

                if speed == 'fast':
                    time.sleep(.001)

    def load_data(self, ticker_name, news, file_path):
        """Write data from the ticker to files"""

        self.show_message(f'Please wait, the time this takes\n relies on your network connection...')
        # bar
        self.increase_progress_bar(5, 'slow')

        self.show_message(f'Fetching data for {ticker_name}\nfrom yfinance...')

        # bar
        self.increase_progress_bar(5, 'normal')

        # get ticker data
        ticker = yf.Ticker(ticker_name)
        obj = ticker.info

        try:
            ticker_type = obj['quoteType']
        except KeyError:
            # if the ticker isn't crypto or stock, exit the thread
            if self.search_page:
                self.error_message.emit('You must enter either an equity or crypto currency.\n'
                                        'For cryptocurrency specify the currency used e.g.: \n'
                                        '- for bitcoin and us dollar write - btc-usd\n'
                                        'For stock write the ticker name e.g.:\n'
                                        '- for amazon write - amzn')
            else:
                self.error_message.emit('You must enter an equity e.g. - AMZN')

            self.thread_done(False)
            return

        # progressbar
        self.increase_progress_bar(len(obj) // 3, 'normal')

        # write data to file
        json_data = json.dumps(obj, indent=4)
        # Writing to data to sample.json
        with open(file_path + "\\TickerData.json", "w") as outfile:
            outfile.write(json_data)

        # do the same for news
        if news:
            self.load_news(ticker_name)

    def load_news(self, ticker):
        """Load news from bing"""

        self.show_message('Retrieving News from bing...')
        # Parameters
        # Data
        url = f'https://www.bing.com/news/search?q={ticker}&FORM=HDRSC6'
        header = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'

        # requesting data from site
        req = requests.get(url=url, headers={'user-agent': header}, timeout=None).text
        html = BeautifulSoup(req, features="lxml")
        news_table = html.find(id='algocore').find_all('div', class_='news-card newsitem cardcommon b_cards2')

        # dict
        news = []

        for row in news_table:
            # progressbar
            self.count += 1
            time.sleep(.2)
            self.progress.emit(self.count)

            try:
                # data
                source = row['data-author']
                title = row['data-title']
                description = row.find(class_='snippet').text
                time_taken = row.find_all('span')[2]['aria-label']
                link = row.find(href=True)['href']

                # save data
                data = {'source': source, 'title': title, 'description': description, 'time': time_taken, 'link': link}
                news.append(data)

            except AttributeError:
                pass

        # write data to file
        json_data = json.dumps(news, indent=4)
        # Writing to data to sample.json
        with open("temp/search/TickerNews.json", "w") as outfile:
            outfile.write(json_data)

        self.thread_done(True)

    def finish_progress_bar(self):
        """End progress left of progressbar"""

        if self.search_page:
            # complete progress bar
            self.show_message('Finishing...')

            # handle the remaining progress bar
            remainder = 100 - self.count
            self.increase_progress_bar(remainder, 'fast')

    def thread_done(self, data_was_loaded):
        # done
        if data_was_loaded:
            # end bar
            self.finish_progress_bar()

            # feedback
            self.show_message('Done!\n'
                              'Click here to see the results!')
            self.thread_is_done.emit(True)
            return

        if not data_was_loaded:
            self.thread_is_done.emit(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
