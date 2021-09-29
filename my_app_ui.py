# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app interfacezyWxjq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app_icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 847)
        font = QFont()
        font.setFamily(u"Modern")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(28, 32, 43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(28, 32, 43);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(54, 79, 113);\n"
"")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.header_left_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_icon_button = QPushButton(self.header_left_frame)
        self.menu_icon_button.setObjectName(u"menu_icon_button")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.menu_icon_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_icon_button.setIcon(icon)
        self.menu_icon_button.setIconSize(QSize(32, 32))
        self.menu_icon_button.setFlat(True)

        self.gridLayout_2.addWidget(self.menu_icon_button, 1, 0, 1, 1)

        self.menu_label = QLabel(self.header_left_frame)
        self.menu_label.setObjectName(u"menu_label")

        self.gridLayout_2.addWidget(self.menu_label, 1, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app_title_icon = QLabel(self.header_center_frame)
        self.app_title_icon.setObjectName(u"app_title_icon")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.app_title_icon.setFont(font2)
        self.app_title_icon.setPixmap(QPixmap(u":/icons/icons/activity.svg"))

        self.horizontalLayout_2.addWidget(self.app_title_icon, 0, Qt.AlignRight)

        self.app_name_title = QLabel(self.header_center_frame)
        self.app_name_title.setObjectName(u"app_name_title")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.app_name_title.setFont(font3)

        self.horizontalLayout_2.addWidget(self.app_name_title, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignHCenter)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.header_right_frame)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setEnabled(True)
        self.left_menu_cont_frame.setMinimumSize(QSize(50, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: rgb(54, 79, 113);")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.settings_label = QLabel(self.menu_frame)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setFont(font2)
        self.settings_label.setMargin(5)

        self.gridLayout.addWidget(self.settings_label, 4, 1, 1, 1, Qt.AlignLeft)

        self.about_label = QLabel(self.menu_frame)
        self.about_label.setObjectName(u"about_label")
        self.about_label.setFont(font2)
        self.about_label.setMargin(5)

        self.gridLayout.addWidget(self.about_label, 5, 1, 1, 1, Qt.AlignLeft)

        self.home_label = QLabel(self.menu_frame)
        self.home_label.setObjectName(u"home_label")
        self.home_label.setFont(font2)
        self.home_label.setMargin(5)

        self.gridLayout.addWidget(self.home_label, 0, 1, 1, 1, Qt.AlignLeft)

        self.trade_label = QLabel(self.menu_frame)
        self.trade_label.setObjectName(u"trade_label")
        self.trade_label.setFont(font2)
        self.trade_label.setMargin(5)

        self.gridLayout.addWidget(self.trade_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.trade_icon = QPushButton(self.menu_frame)
        self.trade_icon.setObjectName(u"trade_icon")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trade_icon.setIcon(icon1)
        self.trade_icon.setIconSize(QSize(32, 32))
        self.trade_icon.setFlat(True)

        self.gridLayout.addWidget(self.trade_icon, 3, 0, 1, 1, Qt.AlignLeft)

        self.about_icon = QPushButton(self.menu_frame)
        self.about_icon.setObjectName(u"about_icon")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_icon.setIcon(icon2)
        self.about_icon.setIconSize(QSize(32, 32))
        self.about_icon.setFlat(True)

        self.gridLayout.addWidget(self.about_icon, 5, 0, 1, 1, Qt.AlignLeft)

        self.stock_analysis_label = QLabel(self.menu_frame)
        self.stock_analysis_label.setObjectName(u"stock_analysis_label")
        self.stock_analysis_label.setFont(font2)
        self.stock_analysis_label.setMargin(5)

        self.gridLayout.addWidget(self.stock_analysis_label, 1, 1, 1, 1, Qt.AlignLeft)

        self.stock_analysis_icon = QPushButton(self.menu_frame)
        self.stock_analysis_icon.setObjectName(u"stock_analysis_icon")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stock_analysis_icon.setIcon(icon3)
        self.stock_analysis_icon.setIconSize(QSize(32, 32))
        self.stock_analysis_icon.setFlat(True)

        self.gridLayout.addWidget(self.stock_analysis_icon, 1, 0, 1, 1, Qt.AlignLeft)

        self.learn_label = QLabel(self.menu_frame)
        self.learn_label.setObjectName(u"learn_label")
        self.learn_label.setFont(font2)
        self.learn_label.setMargin(5)

        self.gridLayout.addWidget(self.learn_label, 2, 1, 1, 1, Qt.AlignLeft)

        self.learn_icon = QPushButton(self.menu_frame)
        self.learn_icon.setObjectName(u"learn_icon")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.learn_icon.setIcon(icon4)
        self.learn_icon.setIconSize(QSize(32, 32))
        self.learn_icon.setFlat(True)

        self.gridLayout.addWidget(self.learn_icon, 2, 0, 1, 1, Qt.AlignLeft)

        self.settings_icon = QPushButton(self.menu_frame)
        self.settings_icon.setObjectName(u"settings_icon")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_icon.setIcon(icon5)
        self.settings_icon.setIconSize(QSize(32, 32))
        self.settings_icon.setFlat(True)

        self.gridLayout.addWidget(self.settings_icon, 4, 0, 1, 1, Qt.AlignLeft)

        self.home_icon = QPushButton(self.menu_frame)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_icon.setIcon(icon6)
        self.home_icon.setIconSize(QSize(32, 32))
        self.home_icon.setFlat(True)

        self.gridLayout.addWidget(self.home_icon, 0, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setMaximumSize(QSize(16777215, 16777215))
        self.main_body_contents.setStyleSheet(u"background-color: rgb(32, 36, 48);")
        self.main_body_contents.setFrameShape(QFrame.NoFrame)
        self.main_body_contents.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_menu_pages = QStackedWidget(self.main_body_contents)
        self.stacked_menu_pages.setObjectName(u"stacked_menu_pages")
        self.stacked_menu_pages.setLineWidth(0)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.home_page_scrollArea = QScrollArea(self.home_page)
        self.home_page_scrollArea.setObjectName(u"home_page_scrollArea")
        self.home_page_scrollArea.setFrameShape(QFrame.NoFrame)
        self.home_page_scrollArea.setFrameShadow(QFrame.Plain)
        self.home_page_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.home_page_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.home_page_scrollArea.setWidgetResizable(True)
        self.home_page_frame = QWidget()
        self.home_page_frame.setObjectName(u"home_page_frame")
        self.home_page_frame.setGeometry(QRect(0, 0, 863, 725))
        self.verticalLayout_6 = QVBoxLayout(self.home_page_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.home_page_body = QFrame(self.home_page_frame)
        self.home_page_body.setObjectName(u"home_page_body")
        self.home_page_body.setFrameShape(QFrame.NoFrame)
        self.home_page_body.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.home_page_body)
        self.verticalLayout_8.setSpacing(60)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.home_page_title = QLabel(self.home_page_body)
        self.home_page_title.setObjectName(u"home_page_title")
        self.home_page_title.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.home_page_title, 0, Qt.AlignHCenter)

        self.home_page_content = QLabel(self.home_page_body)
        self.home_page_content.setObjectName(u"home_page_content")
        self.home_page_content.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.home_page_content)


        self.verticalLayout_6.addWidget(self.home_page_body, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.home_page_scrollArea.setWidget(self.home_page_frame)

        self.verticalLayout_5.addWidget(self.home_page_scrollArea)

        self.stacked_menu_pages.addWidget(self.home_page)
        self.stock_analysis = QWidget()
        self.stock_analysis.setObjectName(u"stock_analysis")
        self.verticalLayout_9 = QVBoxLayout(self.stock_analysis)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stock_analysis_scrollArea = QScrollArea(self.stock_analysis)
        self.stock_analysis_scrollArea.setObjectName(u"stock_analysis_scrollArea")
        self.stock_analysis_scrollArea.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stock_analysis_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stock_analysis_scrollArea.setWidgetResizable(True)
        self.stock_analysis_frame = QWidget()
        self.stock_analysis_frame.setObjectName(u"stock_analysis_frame")
        self.stock_analysis_frame.setGeometry(QRect(0, 0, 863, 725))
        self.verticalLayout_10 = QVBoxLayout(self.stock_analysis_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header = QFrame(self.stock_analysis_frame)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stock_analysis_title_frame = QFrame(self.header)
        self.stock_analysis_title_frame.setObjectName(u"stock_analysis_title_frame")
        self.stock_analysis_title_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.stock_analysis_title_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stock_analysis_title = QLabel(self.stock_analysis_title_frame)
        self.stock_analysis_title.setObjectName(u"stock_analysis_title")
        self.stock_analysis_title.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.stock_analysis_title)


        self.horizontalLayout_3.addWidget(self.stock_analysis_title_frame)

        self.search_bar_frame = QFrame(self.header)
        self.search_bar_frame.setObjectName(u"search_bar_frame")
        self.search_bar_frame.setMaximumSize(QSize(200, 16777215))
        self.search_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.search_bar_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.search_bar_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_entry = QLineEdit(self.search_bar_frame)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setMinimumSize(QSize(0, 0))
        self.search_entry.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.search_entry.setFont(font4)
        self.search_entry.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.search_entry, 0, 0, 1, 1)

        self.search_button = QPushButton(self.search_bar_frame)
        self.search_button.setObjectName(u"search_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon7)
        self.search_button.setIconSize(QSize(24, 24))
        self.search_button.setFlat(True)

        self.gridLayout_4.addWidget(self.search_button, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.search_bar_frame)


        self.verticalLayout_10.addWidget(self.header)

        self.stock_analysis_main_body = QFrame(self.stock_analysis_frame)
        self.stock_analysis_main_body.setObjectName(u"stock_analysis_main_body")
        self.stock_analysis_main_body.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.stock_analysis_main_body)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.stock_analysis_options_frame = QFrame(self.stock_analysis_main_body)
        self.stock_analysis_options_frame.setObjectName(u"stock_analysis_options_frame")
        self.stock_analysis_options_frame.setMinimumSize(QSize(0, 0))
        self.stock_analysis_options_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.stock_analysis_options_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stock_anaysis_stock_name_frame = QFrame(self.stock_analysis_options_frame)
        self.stock_anaysis_stock_name_frame.setObjectName(u"stock_anaysis_stock_name_frame")
        self.stock_anaysis_stock_name_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_anaysis_stock_name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.stock_anaysis_stock_name_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.stock_analysis_stock_name = QLabel(self.stock_anaysis_stock_name_frame)
        self.stock_analysis_stock_name.setObjectName(u"stock_analysis_stock_name")
        self.stock_analysis_stock_name.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_34.addWidget(self.stock_analysis_stock_name, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.stock_anaysis_stock_name_frame)


        self.verticalLayout_35.addWidget(self.stock_analysis_options_frame)

        self.stock_analysis_stackedWidget = QStackedWidget(self.stock_analysis_main_body)
        self.stock_analysis_stackedWidget.setObjectName(u"stock_analysis_stackedWidget")
        self.stock_analysis_stackedWidget.setMinimumSize(QSize(0, 0))
        self.stock_analysis_stock_page = QWidget()
        self.stock_analysis_stock_page.setObjectName(u"stock_analysis_stock_page")
        self.verticalLayout_36 = QVBoxLayout(self.stock_analysis_stock_page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.stock_analysis_stock_info_frame = QFrame(self.stock_analysis_stock_page)
        self.stock_analysis_stock_info_frame.setObjectName(u"stock_analysis_stock_info_frame")
        self.stock_analysis_stock_info_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_stock_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.stock_analysis_stock_info_frame)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.stock_analysis_stock_info_content = QLabel(self.stock_analysis_stock_info_frame)
        self.stock_analysis_stock_info_content.setObjectName(u"stock_analysis_stock_info_content")

        self.verticalLayout_39.addWidget(self.stock_analysis_stock_info_content)


        self.verticalLayout_36.addWidget(self.stock_analysis_stock_info_frame)

        self.stock_quote_frame = QFrame(self.stock_analysis_stock_page)
        self.stock_quote_frame.setObjectName(u"stock_quote_frame")
        self.stock_quote_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_quote_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.stock_quote_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ticker_label = QLabel(self.stock_quote_frame)
        self.ticker_label.setObjectName(u"ticker_label")

        self.horizontalLayout_12.addWidget(self.ticker_label)

        self.volume_label = QLabel(self.stock_quote_frame)
        self.volume_label.setObjectName(u"volume_label")

        self.horizontalLayout_12.addWidget(self.volume_label)

        self.price_traded_label = QLabel(self.stock_quote_frame)
        self.price_traded_label.setObjectName(u"price_traded_label")

        self.horizontalLayout_12.addWidget(self.price_traded_label)

        self.change_direction_label = QLabel(self.stock_quote_frame)
        self.change_direction_label.setObjectName(u"change_direction_label")

        self.horizontalLayout_12.addWidget(self.change_direction_label)

        self.change_amount_label = QLabel(self.stock_quote_frame)
        self.change_amount_label.setObjectName(u"change_amount_label")

        self.horizontalLayout_12.addWidget(self.change_amount_label)


        self.verticalLayout_36.addWidget(self.stock_quote_frame)

        self.times_frame = QFrame(self.stock_analysis_stock_page)
        self.times_frame.setObjectName(u"times_frame")
        self.times_frame.setFrameShape(QFrame.StyledPanel)
        self.times_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.times_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.one_week_button = QPushButton(self.times_frame)
        self.one_week_button.setObjectName(u"one_week_button")
        self.one_week_button.setMinimumSize(QSize(60, 30))
        self.one_week_button.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_week_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.one_week_button)

        self.one_month_button = QPushButton(self.times_frame)
        self.one_month_button.setObjectName(u"one_month_button")
        self.one_month_button.setMinimumSize(QSize(60, 30))
        self.one_month_button.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_month_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.one_month_button)

        self.one_year_button = QPushButton(self.times_frame)
        self.one_year_button.setObjectName(u"one_year_button")
        self.one_year_button.setMinimumSize(QSize(60, 30))
        self.one_year_button.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_year_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.one_year_button)

        self.five_year_button = QPushButton(self.times_frame)
        self.five_year_button.setObjectName(u"five_year_button")
        self.five_year_button.setMinimumSize(QSize(60, 30))
        self.five_year_button.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.five_year_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.five_year_button)

        self.max_button = QPushButton(self.times_frame)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMinimumSize(QSize(60, 30))
        self.max_button.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.max_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.max_button)


        self.verticalLayout_36.addWidget(self.times_frame)

        self.charts = QFrame(self.stock_analysis_stock_page)
        self.charts.setObjectName(u"charts")
        self.charts.setFrameShape(QFrame.StyledPanel)
        self.charts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.charts)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stacked_charts = QStackedWidget(self.charts)
        self.stacked_charts.setObjectName(u"stacked_charts")
        self.week_page = QWidget()
        self.week_page.setObjectName(u"week_page")
        self.verticalLayout_13 = QVBoxLayout(self.week_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.week_page_frame = QFrame(self.week_page)
        self.week_page_frame.setObjectName(u"week_page_frame")
        self.week_page_frame.setFrameShape(QFrame.StyledPanel)
        self.week_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.week_page_frame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.week_chart_frame = QFrame(self.week_page_frame)
        self.week_chart_frame.setObjectName(u"week_chart_frame")
        self.week_chart_frame.setFrameShape(QFrame.StyledPanel)
        self.week_chart_frame.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.week_chart_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(190, 40, 101, 31))

        self.verticalLayout_46.addWidget(self.week_chart_frame)

        self.week_info_frame = QFrame(self.week_page_frame)
        self.week_info_frame.setObjectName(u"week_info_frame")
        self.week_info_frame.setFrameShape(QFrame.StyledPanel)
        self.week_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.week_info_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.info_box = QFrame(self.week_info_frame)
        self.info_box.setObjectName(u"info_box")
        self.info_box.setFrameShape(QFrame.StyledPanel)
        self.info_box.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.info_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.week_low = QLabel(self.info_box)
        self.week_low.setObjectName(u"week_low")

        self.gridLayout_3.addWidget(self.week_low, 2, 0, 1, 1)

        self.week_open = QLabel(self.info_box)
        self.week_open.setObjectName(u"week_open")

        self.gridLayout_3.addWidget(self.week_open, 0, 0, 1, 1)

        self.week_high = QLabel(self.info_box)
        self.week_high.setObjectName(u"week_high")

        self.gridLayout_3.addWidget(self.week_high, 1, 0, 1, 1)

        self.week_high_placeholder = QLabel(self.info_box)
        self.week_high_placeholder.setObjectName(u"week_high_placeholder")

        self.gridLayout_3.addWidget(self.week_high_placeholder, 1, 1, 1, 1)

        self.week_open_placeholder = QLabel(self.info_box)
        self.week_open_placeholder.setObjectName(u"week_open_placeholder")

        self.gridLayout_3.addWidget(self.week_open_placeholder, 0, 1, 1, 1)

        self.week_low_placeholder = QLabel(self.info_box)
        self.week_low_placeholder.setObjectName(u"week_low_placeholder")

        self.gridLayout_3.addWidget(self.week_low_placeholder, 2, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.info_box)

        self.size_grip_2 = QFrame(self.week_info_frame)
        self.size_grip_2.setObjectName(u"size_grip_2")
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.size_grip_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.horizontalLayout_14.addWidget(self.size_grip_2)


        self.verticalLayout_46.addWidget(self.week_info_frame)


        self.verticalLayout_13.addWidget(self.week_page_frame)

        self.stacked_charts.addWidget(self.week_page)

        self.verticalLayout_12.addWidget(self.stacked_charts)


        self.verticalLayout_36.addWidget(self.charts)

        self.stock_analysis_stackedWidget.addWidget(self.stock_analysis_stock_page)
        self.stock_analyysis_currency_page = QWidget()
        self.stock_analyysis_currency_page.setObjectName(u"stock_analyysis_currency_page")
        self.verticalLayout_40 = QVBoxLayout(self.stock_analyysis_currency_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.extra_info_about_currency = QLabel(self.stock_analyysis_currency_page)
        self.extra_info_about_currency.setObjectName(u"extra_info_about_currency")

        self.verticalLayout_40.addWidget(self.extra_info_about_currency)

        self.currency_comparison_frame = QFrame(self.stock_analyysis_currency_page)
        self.currency_comparison_frame.setObjectName(u"currency_comparison_frame")
        self.currency_comparison_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_comparison_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.currency_comparison_frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.first_currency_entry = QLineEdit(self.currency_comparison_frame)
        self.first_currency_entry.setObjectName(u"first_currency_entry")
        self.first_currency_entry.setMinimumSize(QSize(100, 0))

        self.gridLayout_10.addWidget(self.first_currency_entry, 1, 0, 1, 1)

        self.second_currency_entry = QLineEdit(self.currency_comparison_frame)
        self.second_currency_entry.setObjectName(u"second_currency_entry")
        self.second_currency_entry.setReadOnly(True)

        self.gridLayout_10.addWidget(self.second_currency_entry, 1, 2, 1, 1)

        self.second_curency_label = QLabel(self.currency_comparison_frame)
        self.second_curency_label.setObjectName(u"second_curency_label")

        self.gridLayout_10.addWidget(self.second_curency_label, 0, 2, 1, 1, Qt.AlignHCenter)

        self.first_currency_label = QLabel(self.currency_comparison_frame)
        self.first_currency_label.setObjectName(u"first_currency_label")

        self.gridLayout_10.addWidget(self.first_currency_label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.comparison_button = QLabel(self.currency_comparison_frame)
        self.comparison_button.setObjectName(u"comparison_button")
        self.comparison_button.setPixmap(QPixmap(u":/icons/icons/chevrons-right.svg"))

        self.gridLayout_10.addWidget(self.comparison_button, 1, 1, 1, 1)


        self.verticalLayout_40.addWidget(self.currency_comparison_frame)

        self.times_frame_2 = QFrame(self.stock_analyysis_currency_page)
        self.times_frame_2.setObjectName(u"times_frame_2")
        self.times_frame_2.setFrameShape(QFrame.StyledPanel)
        self.times_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.times_frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.one_week_button_2 = QPushButton(self.times_frame_2)
        self.one_week_button_2.setObjectName(u"one_week_button_2")
        self.one_week_button_2.setMinimumSize(QSize(60, 30))
        self.one_week_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_week_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_week_button_2)

        self.one_month_button_2 = QPushButton(self.times_frame_2)
        self.one_month_button_2.setObjectName(u"one_month_button_2")
        self.one_month_button_2.setMinimumSize(QSize(60, 30))
        self.one_month_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_month_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_month_button_2)

        self.one_year_button_2 = QPushButton(self.times_frame_2)
        self.one_year_button_2.setObjectName(u"one_year_button_2")
        self.one_year_button_2.setMinimumSize(QSize(60, 30))
        self.one_year_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.one_year_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_year_button_2)

        self.five_year_button_2 = QPushButton(self.times_frame_2)
        self.five_year_button_2.setObjectName(u"five_year_button_2")
        self.five_year_button_2.setMinimumSize(QSize(60, 30))
        self.five_year_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.five_year_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.five_year_button_2)

        self.max_button_2 = QPushButton(self.times_frame_2)
        self.max_button_2.setObjectName(u"max_button_2")
        self.max_button_2.setMinimumSize(QSize(60, 30))
        self.max_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.max_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.max_button_2)


        self.verticalLayout_40.addWidget(self.times_frame_2)

        self.charts_2 = QFrame(self.stock_analyysis_currency_page)
        self.charts_2.setObjectName(u"charts_2")
        self.charts_2.setFrameShape(QFrame.StyledPanel)
        self.charts_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.charts_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.stacked_charts_2 = QStackedWidget(self.charts_2)
        self.stacked_charts_2.setObjectName(u"stacked_charts_2")
        self.week_page_2 = QWidget()
        self.week_page_2.setObjectName(u"week_page_2")
        self.verticalLayout_38 = QVBoxLayout(self.week_page_2)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.chart_frame_2 = QFrame(self.week_page_2)
        self.chart_frame_2.setObjectName(u"chart_frame_2")
        self.chart_frame_2.setFrameShape(QFrame.StyledPanel)
        self.chart_frame_2.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.chart_frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(190, 40, 101, 31))

        self.verticalLayout_38.addWidget(self.chart_frame_2)

        self.info_frame_2 = QFrame(self.week_page_2)
        self.info_frame_2.setObjectName(u"info_frame_2")
        self.info_frame_2.setFrameShape(QFrame.StyledPanel)
        self.info_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.info_frame_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.info_box_2 = QFrame(self.info_frame_2)
        self.info_box_2.setObjectName(u"info_box_2")
        self.info_box_2.setFrameShape(QFrame.StyledPanel)
        self.info_box_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.info_box_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.curency_low = QLabel(self.info_box_2)
        self.curency_low.setObjectName(u"curency_low")

        self.gridLayout_8.addWidget(self.curency_low, 2, 0, 1, 1)

        self.currency_open = QLabel(self.info_box_2)
        self.currency_open.setObjectName(u"currency_open")

        self.gridLayout_8.addWidget(self.currency_open, 0, 0, 1, 1)

        self.currency_high = QLabel(self.info_box_2)
        self.currency_high.setObjectName(u"currency_high")

        self.gridLayout_8.addWidget(self.currency_high, 1, 0, 1, 1)

        self.currency_high_placeholder = QLabel(self.info_box_2)
        self.currency_high_placeholder.setObjectName(u"currency_high_placeholder")

        self.gridLayout_8.addWidget(self.currency_high_placeholder, 1, 1, 1, 1)

        self.currency_open_placeholder = QLabel(self.info_box_2)
        self.currency_open_placeholder.setObjectName(u"currency_open_placeholder")

        self.gridLayout_8.addWidget(self.currency_open_placeholder, 0, 1, 1, 1)

        self.currency_low_placeholder = QLabel(self.info_box_2)
        self.currency_low_placeholder.setObjectName(u"currency_low_placeholder")

        self.gridLayout_8.addWidget(self.currency_low_placeholder, 2, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.info_box_2)

        self.size_grip_3 = QFrame(self.info_frame_2)
        self.size_grip_3.setObjectName(u"size_grip_3")
        self.size_grip_3.setFrameShape(QFrame.StyledPanel)
        self.size_grip_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.size_grip_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.horizontalLayout_20.addWidget(self.size_grip_3)


        self.verticalLayout_38.addWidget(self.info_frame_2)

        self.stacked_charts_2.addWidget(self.week_page_2)

        self.verticalLayout_37.addWidget(self.stacked_charts_2)


        self.verticalLayout_40.addWidget(self.charts_2)

        self.stock_analysis_stackedWidget.addWidget(self.stock_analyysis_currency_page)

        self.verticalLayout_35.addWidget(self.stock_analysis_stackedWidget)


        self.verticalLayout_10.addWidget(self.stock_analysis_main_body)

        self.stock_analysis_scrollArea.setWidget(self.stock_analysis_frame)

        self.verticalLayout_9.addWidget(self.stock_analysis_scrollArea)

        self.stacked_menu_pages.addWidget(self.stock_analysis)
        self.learn = QWidget()
        self.learn.setObjectName(u"learn")
        self.verticalLayout_14 = QVBoxLayout(self.learn)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.learning_pages_stackedWidget = QStackedWidget(self.learn)
        self.learning_pages_stackedWidget.setObjectName(u"learning_pages_stackedWidget")
        font5 = QFont()
        font5.setFamily(u"MS Outlook")
        font5.setBold(False)
        font5.setWeight(50)
        self.learning_pages_stackedWidget.setFont(font5)
        self.learn_start_page = QWidget()
        self.learn_start_page.setObjectName(u"learn_start_page")
        self.verticalLayout_15 = QVBoxLayout(self.learn_start_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.learn_start_page_frame = QFrame(self.learn_start_page)
        self.learn_start_page_frame.setObjectName(u"learn_start_page_frame")
        self.learn_start_page_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.learn_start_page_frame)
        self.verticalLayout_44.setSpacing(235)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.learn_start_page_title_frame = QFrame(self.learn_start_page_frame)
        self.learn_start_page_title_frame.setObjectName(u"learn_start_page_title_frame")
        self.learn_start_page_title_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.learn_start_page_title_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.learn_start_page_title_label = QLabel(self.learn_start_page_title_frame)
        self.learn_start_page_title_label.setObjectName(u"learn_start_page_title_label")
        self.learn_start_page_title_label.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_41.addWidget(self.learn_start_page_title_label)


        self.verticalLayout_44.addWidget(self.learn_start_page_title_frame, 0, Qt.AlignHCenter)

        self.learn_start_page_content_frame_frame = QFrame(self.learn_start_page_frame)
        self.learn_start_page_content_frame_frame.setObjectName(u"learn_start_page_content_frame_frame")
        self.learn_start_page_content_frame_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_content_frame_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.learn_start_page_content_frame_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.learn_start_page_frame_title = QFrame(self.learn_start_page_content_frame_frame)
        self.learn_start_page_frame_title.setObjectName(u"learn_start_page_frame_title")
        self.learn_start_page_frame_title.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.learn_start_page_frame_title)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.what_do_you_wish_to_learn_label = QLabel(self.learn_start_page_frame_title)
        self.what_do_you_wish_to_learn_label.setObjectName(u"what_do_you_wish_to_learn_label")

        self.verticalLayout_17.addWidget(self.what_do_you_wish_to_learn_label, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.learn_start_page_frame_title)

        self.learn_start_page_options_frame = QFrame(self.learn_start_page_content_frame_frame)
        self.learn_start_page_options_frame.setObjectName(u"learn_start_page_options_frame")
        self.learn_start_page_options_frame.setMinimumSize(QSize(400, 0))
        self.learn_start_page_options_frame.setMaximumSize(QSize(25000, 16777215))
        self.learn_start_page_options_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_options_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.learn_start_page_options_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.stocks_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.stocks_button_learn.setObjectName(u"stocks_button_learn")
        self.stocks_button_learn.setMinimumSize(QSize(100, 40))
        self.stocks_button_learn.setMaximumSize(QSize(500, 40))
        self.stocks_button_learn.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.stocks_button_learn.setFlat(False)

        self.horizontalLayout_15.addWidget(self.stocks_button_learn)

        self.forex_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.forex_button_learn.setObjectName(u"forex_button_learn")
        self.forex_button_learn.setMinimumSize(QSize(100, 40))
        self.forex_button_learn.setMaximumSize(QSize(500, 40))
        self.forex_button_learn.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.forex_button_learn.setFlat(False)

        self.horizontalLayout_15.addWidget(self.forex_button_learn)

        self.crypto_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.crypto_button_learn.setObjectName(u"crypto_button_learn")
        self.crypto_button_learn.setMinimumSize(QSize(100, 40))
        self.crypto_button_learn.setMaximumSize(QSize(500, 40))
        self.crypto_button_learn.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.crypto_button_learn.setFlat(False)

        self.horizontalLayout_15.addWidget(self.crypto_button_learn)


        self.verticalLayout_16.addWidget(self.learn_start_page_options_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_44.addWidget(self.learn_start_page_content_frame_frame)


        self.verticalLayout_15.addWidget(self.learn_start_page_frame, 0, Qt.AlignTop)

        self.learning_pages_stackedWidget.addWidget(self.learn_start_page)
        self.stocks_page = QWidget()
        self.stocks_page.setObjectName(u"stocks_page")
        self.verticalLayout_18 = QVBoxLayout(self.stocks_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.stocks_page_scrollArea = QScrollArea(self.stocks_page)
        self.stocks_page_scrollArea.setObjectName(u"stocks_page_scrollArea")
        self.stocks_page_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stocks_page_scrollArea.setFrameShadow(QFrame.Plain)
        self.stocks_page_scrollArea.setWidgetResizable(True)
        self.stocks_page_scrollAreaWidget_frame = QWidget()
        self.stocks_page_scrollAreaWidget_frame.setObjectName(u"stocks_page_scrollAreaWidget_frame")
        self.stocks_page_scrollAreaWidget_frame.setGeometry(QRect(0, 0, 240, 426))
        self.verticalLayout_19 = QVBoxLayout(self.stocks_page_scrollAreaWidget_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.stock_learning_content_header = QLabel(self.stocks_page_scrollAreaWidget_frame)
        self.stock_learning_content_header.setObjectName(u"stock_learning_content_header")

        self.verticalLayout_19.addWidget(self.stock_learning_content_header)

        self.stocks_page_scrollArea.setWidget(self.stocks_page_scrollAreaWidget_frame)

        self.verticalLayout_18.addWidget(self.stocks_page_scrollArea)

        self.learning_pages_stackedWidget.addWidget(self.stocks_page)
        self.cryptocurrency_page = QWidget()
        self.cryptocurrency_page.setObjectName(u"cryptocurrency_page")
        self.verticalLayout_21 = QVBoxLayout(self.cryptocurrency_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.cryptocurrency_page_scrollArea = QScrollArea(self.cryptocurrency_page)
        self.cryptocurrency_page_scrollArea.setObjectName(u"cryptocurrency_page_scrollArea")
        self.cryptocurrency_page_scrollArea.setFrameShape(QFrame.NoFrame)
        self.cryptocurrency_page_scrollArea.setFrameShadow(QFrame.Plain)
        self.cryptocurrency_page_scrollArea.setWidgetResizable(True)
        self.cryptocurrency_scrollAreaWidget_frame = QWidget()
        self.cryptocurrency_scrollAreaWidget_frame.setObjectName(u"cryptocurrency_scrollAreaWidget_frame")
        self.cryptocurrency_scrollAreaWidget_frame.setGeometry(QRect(0, 0, 302, 396))
        self.verticalLayout_20 = QVBoxLayout(self.cryptocurrency_scrollAreaWidget_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.crypto_learning_content_header = QLabel(self.cryptocurrency_scrollAreaWidget_frame)
        self.crypto_learning_content_header.setObjectName(u"crypto_learning_content_header")

        self.verticalLayout_20.addWidget(self.crypto_learning_content_header)

        self.cryptocurrency_page_scrollArea.setWidget(self.cryptocurrency_scrollAreaWidget_frame)

        self.verticalLayout_21.addWidget(self.cryptocurrency_page_scrollArea)

        self.learning_pages_stackedWidget.addWidget(self.cryptocurrency_page)
        self.forex_page = QWidget()
        self.forex_page.setObjectName(u"forex_page")
        self.verticalLayout_23 = QVBoxLayout(self.forex_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.forex_page_scrollArea = QScrollArea(self.forex_page)
        self.forex_page_scrollArea.setObjectName(u"forex_page_scrollArea")
        self.forex_page_scrollArea.setFrameShape(QFrame.NoFrame)
        self.forex_page_scrollArea.setFrameShadow(QFrame.Plain)
        self.forex_page_scrollArea.setWidgetResizable(True)
        self.forex_scrollAreaWidget_frame = QWidget()
        self.forex_scrollAreaWidget_frame.setObjectName(u"forex_scrollAreaWidget_frame")
        self.forex_scrollAreaWidget_frame.setGeometry(QRect(0, 0, 845, 707))
        self.verticalLayout_22 = QVBoxLayout(self.forex_scrollAreaWidget_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.forex_learning_content = QLabel(self.forex_scrollAreaWidget_frame)
        self.forex_learning_content.setObjectName(u"forex_learning_content")

        self.verticalLayout_22.addWidget(self.forex_learning_content, 0, Qt.AlignTop)

        self.forex_page_scrollArea.setWidget(self.forex_scrollAreaWidget_frame)

        self.verticalLayout_23.addWidget(self.forex_page_scrollArea)

        self.learning_pages_stackedWidget.addWidget(self.forex_page)

        self.verticalLayout_14.addWidget(self.learning_pages_stackedWidget)

        self.stacked_menu_pages.addWidget(self.learn)
        self.trade = QWidget()
        self.trade.setObjectName(u"trade")
        self.verticalLayout_24 = QVBoxLayout(self.trade)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.simulator_stacked_widget = QStackedWidget(self.trade)
        self.simulator_stacked_widget.setObjectName(u"simulator_stacked_widget")
        self.simulator_start_page = QWidget()
        self.simulator_start_page.setObjectName(u"simulator_start_page")
        self.verticalLayout_25 = QVBoxLayout(self.simulator_start_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.simulator_start_page_frame = QFrame(self.simulator_start_page)
        self.simulator_start_page_frame.setObjectName(u"simulator_start_page_frame")
        self.simulator_start_page_frame.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.simulator_start_page_frame)
        self.verticalLayout_26.setSpacing(235)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.simulator_start_page_title_frame = QFrame(self.simulator_start_page_frame)
        self.simulator_start_page_title_frame.setObjectName(u"simulator_start_page_title_frame")
        self.simulator_start_page_title_frame.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.simulator_start_page_title_frame)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.simulator_start_page_title_label = QLabel(self.simulator_start_page_title_frame)
        self.simulator_start_page_title_label.setObjectName(u"simulator_start_page_title_label")
        self.simulator_start_page_title_label.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_42.addWidget(self.simulator_start_page_title_label)


        self.verticalLayout_26.addWidget(self.simulator_start_page_title_frame, 0, Qt.AlignHCenter)

        self.simulator_start_page_content_frame = QFrame(self.simulator_start_page_frame)
        self.simulator_start_page_content_frame.setObjectName(u"simulator_start_page_content_frame")
        self.simulator_start_page_content_frame.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.simulator_start_page_content_frame)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.simulator_start_page_title_frame_2 = QFrame(self.simulator_start_page_content_frame)
        self.simulator_start_page_title_frame_2.setObjectName(u"simulator_start_page_title_frame_2")
        self.simulator_start_page_title_frame_2.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_title_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.simulator_start_page_title_frame_2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.simulator_start_page_content_label = QLabel(self.simulator_start_page_title_frame_2)
        self.simulator_start_page_content_label.setObjectName(u"simulator_start_page_content_label")
        self.simulator_start_page_content_label.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.simulator_start_page_content_label, 0, Qt.AlignHCenter)


        self.verticalLayout_45.addWidget(self.simulator_start_page_title_frame_2)

        self.simulator_start_page_options = QFrame(self.simulator_start_page_content_frame)
        self.simulator_start_page_options.setObjectName(u"simulator_start_page_options")
        self.simulator_start_page_options.setMinimumSize(QSize(400, 0))
        self.simulator_start_page_options.setMaximumSize(QSize(25000, 16777215))
        self.simulator_start_page_options.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.simulator_start_page_options)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.stocks_button_2 = QPushButton(self.simulator_start_page_options)
        self.stocks_button_2.setObjectName(u"stocks_button_2")
        self.stocks_button_2.setMinimumSize(QSize(100, 40))
        self.stocks_button_2.setMaximumSize(QSize(500, 40))
        self.stocks_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.stocks_button_2.setFlat(False)

        self.horizontalLayout_21.addWidget(self.stocks_button_2)

        self.forex_button_2 = QPushButton(self.simulator_start_page_options)
        self.forex_button_2.setObjectName(u"forex_button_2")
        self.forex_button_2.setMinimumSize(QSize(100, 40))
        self.forex_button_2.setMaximumSize(QSize(500, 40))
        self.forex_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.forex_button_2.setFlat(False)

        self.horizontalLayout_21.addWidget(self.forex_button_2)

        self.crypto_button_2 = QPushButton(self.simulator_start_page_options)
        self.crypto_button_2.setObjectName(u"crypto_button_2")
        self.crypto_button_2.setMinimumSize(QSize(100, 40))
        self.crypto_button_2.setMaximumSize(QSize(500, 40))
        self.crypto_button_2.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"")
        self.crypto_button_2.setFlat(False)

        self.horizontalLayout_21.addWidget(self.crypto_button_2)


        self.verticalLayout_45.addWidget(self.simulator_start_page_options, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.simulator_start_page_content_frame)


        self.verticalLayout_25.addWidget(self.simulator_start_page_frame, 0, Qt.AlignTop)

        self.simulator_stacked_widget.addWidget(self.simulator_start_page)
        self.stock_simulator_page = QWidget()
        self.stock_simulator_page.setObjectName(u"stock_simulator_page")
        self.verticalLayout_27 = QVBoxLayout(self.stock_simulator_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.stock_simulator_scrollArea = QScrollArea(self.stock_simulator_page)
        self.stock_simulator_scrollArea.setObjectName(u"stock_simulator_scrollArea")
        self.stock_simulator_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stock_simulator_scrollArea.setWidgetResizable(True)
        self.stock_simulator_scroll_area_frame = QWidget()
        self.stock_simulator_scroll_area_frame.setObjectName(u"stock_simulator_scroll_area_frame")
        self.stock_simulator_scroll_area_frame.setGeometry(QRect(0, 0, 845, 707))
        self.stock_simulator_scroll_area_frame.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_28 = QVBoxLayout(self.stock_simulator_scroll_area_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.stock_simulator_header = QFrame(self.stock_simulator_scroll_area_frame)
        self.stock_simulator_header.setObjectName(u"stock_simulator_header")
        self.stock_simulator_header.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.stock_simulator_header)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.stock_simulator_title = QLabel(self.stock_simulator_header)
        self.stock_simulator_title.setObjectName(u"stock_simulator_title")

        self.verticalLayout_29.addWidget(self.stock_simulator_title)

        self.stock_simulator_market_info_label = QLabel(self.stock_simulator_header)
        self.stock_simulator_market_info_label.setObjectName(u"stock_simulator_market_info_label")
        self.stock_simulator_market_info_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_29.addWidget(self.stock_simulator_market_info_label, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.stock_simulator_header, 0, Qt.AlignTop)

        self.stock_simulator_main_body = QFrame(self.stock_simulator_scroll_area_frame)
        self.stock_simulator_main_body.setObjectName(u"stock_simulator_main_body")
        self.stock_simulator_main_body.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.stock_simulator_main_body)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.stock_simulator_order_details_frame = QFrame(self.stock_simulator_main_body)
        self.stock_simulator_order_details_frame.setObjectName(u"stock_simulator_order_details_frame")
        self.stock_simulator_order_details_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_order_details_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.stock_simulator_order_details_frame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.stock_simulator_order_details_title = QLabel(self.stock_simulator_order_details_frame)
        self.stock_simulator_order_details_title.setObjectName(u"stock_simulator_order_details_title")
        self.stock_simulator_order_details_title.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_31.addWidget(self.stock_simulator_order_details_title)

        self.line_2 = QFrame(self.stock_simulator_order_details_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_2)

        self.stock_simulator_order_details_data_frame = QFrame(self.stock_simulator_order_details_frame)
        self.stock_simulator_order_details_data_frame.setObjectName(u"stock_simulator_order_details_data_frame")
        self.stock_simulator_order_details_data_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_order_details_data_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.stock_simulator_order_details_data_frame)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 30)
        self.stock_simulator_stock_ticker_label = QLabel(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_stock_ticker_label.setObjectName(u"stock_simulator_stock_ticker_label")

        self.gridLayout_6.addWidget(self.stock_simulator_stock_ticker_label, 0, 0, 1, 1)

        self.stock_simulator_symbol_lookup_button = QPushButton(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_symbol_lookup_button.setObjectName(u"stock_simulator_symbol_lookup_button")
        self.stock_simulator_symbol_lookup_button.setStyleSheet(u"color:rgb(0, 85, 255)")
        self.stock_simulator_symbol_lookup_button.setFlat(True)

        self.gridLayout_6.addWidget(self.stock_simulator_symbol_lookup_button, 0, 2, 1, 1)

        self.stock_simulator_transaction_label = QLabel(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_transaction_label.setObjectName(u"stock_simulator_transaction_label")

        self.gridLayout_6.addWidget(self.stock_simulator_transaction_label, 1, 0, 1, 1)

        self.stock_simulator_stock_ticker_entry = QLineEdit(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_stock_ticker_entry.setObjectName(u"stock_simulator_stock_ticker_entry")
        self.stock_simulator_stock_ticker_entry.setMaximumSize(QSize(200, 16777215))
        self.stock_simulator_stock_ticker_entry.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);")

        self.gridLayout_6.addWidget(self.stock_simulator_stock_ticker_entry, 0, 1, 1, 1)

        self.stock_simulator_quantity_entry = QLineEdit(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_quantity_entry.setObjectName(u"stock_simulator_quantity_entry")
        self.stock_simulator_quantity_entry.setMaximumSize(QSize(200, 16777215))
        self.stock_simulator_quantity_entry.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);")

        self.gridLayout_6.addWidget(self.stock_simulator_quantity_entry, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.stock_simulator_order_details_data_frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);")

        self.gridLayout_6.addWidget(self.comboBox, 1, 1, 1, 1)

        self.stock_simulator_quantity_label = QLabel(self.stock_simulator_order_details_data_frame)
        self.stock_simulator_quantity_label.setObjectName(u"stock_simulator_quantity_label")

        self.gridLayout_6.addWidget(self.stock_simulator_quantity_label, 2, 0, 1, 1)


        self.verticalLayout_31.addWidget(self.stock_simulator_order_details_data_frame)

        self.stock_simulator_purchase_button = QPushButton(self.stock_simulator_order_details_frame)
        self.stock_simulator_purchase_button.setObjectName(u"stock_simulator_purchase_button")
        self.stock_simulator_purchase_button.setMinimumSize(QSize(300, 30))
        self.stock_simulator_purchase_button.setMaximumSize(QSize(400, 16777215))
        self.stock_simulator_purchase_button.setStyleSheet(u"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(74, 74, 255, 255), stop:0.795455 rgba(0, 255, 233, 255));\n"
"color: rgb(255, 255, 255);")
        self.stock_simulator_purchase_button.setFlat(False)

        self.verticalLayout_31.addWidget(self.stock_simulator_purchase_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.stock_simulator_order_details_frame, 0, Qt.AlignTop)

        self.stock_simulator_middle_line_frame = QFrame(self.stock_simulator_main_body)
        self.stock_simulator_middle_line_frame.setObjectName(u"stock_simulator_middle_line_frame")
        self.stock_simulator_middle_line_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_middle_line_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.stock_simulator_middle_line_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.line = QFrame(self.stock_simulator_middle_line_frame)
        self.line.setObjectName(u"line")
        font6 = QFont()
        font6.setBold(False)
        font6.setWeight(50)
        self.line.setFont(font6)
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_33.addWidget(self.line)


        self.horizontalLayout_16.addWidget(self.stock_simulator_middle_line_frame)

        self.stock_simulator_account_details_frame = QFrame(self.stock_simulator_main_body)
        self.stock_simulator_account_details_frame.setObjectName(u"stock_simulator_account_details_frame")
        self.stock_simulator_account_details_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_account_details_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.stock_simulator_account_details_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stock_simulator_pocket_label = QLabel(self.stock_simulator_account_details_frame)
        self.stock_simulator_pocket_label.setObjectName(u"stock_simulator_pocket_label")
        self.stock_simulator_pocket_label.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_30.addWidget(self.stock_simulator_pocket_label)

        self.line_3 = QFrame(self.stock_simulator_account_details_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_3)

        self.stock_simulator_pocket_data_frame = QFrame(self.stock_simulator_account_details_frame)
        self.stock_simulator_pocket_data_frame.setObjectName(u"stock_simulator_pocket_data_frame")
        self.stock_simulator_pocket_data_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_pocket_data_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.stock_simulator_pocket_data_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stock_simulator_cash_label = QLabel(self.stock_simulator_pocket_data_frame)
        self.stock_simulator_cash_label.setObjectName(u"stock_simulator_cash_label")

        self.horizontalLayout_17.addWidget(self.stock_simulator_cash_label)

        self.stock_simulator_actual_amount_of_cash = QLabel(self.stock_simulator_pocket_data_frame)
        self.stock_simulator_actual_amount_of_cash.setObjectName(u"stock_simulator_actual_amount_of_cash")

        self.horizontalLayout_17.addWidget(self.stock_simulator_actual_amount_of_cash)


        self.verticalLayout_30.addWidget(self.stock_simulator_pocket_data_frame)


        self.horizontalLayout_16.addWidget(self.stock_simulator_account_details_frame, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.stock_simulator_main_body)

        self.stock_simluator_news_content = QFrame(self.stock_simulator_scroll_area_frame)
        self.stock_simluator_news_content.setObjectName(u"stock_simluator_news_content")
        self.stock_simluator_news_content.setFrameShape(QFrame.StyledPanel)
        self.stock_simluator_news_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.stock_simluator_news_content)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame = QFrame(self.stock_simluator_news_content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stock_news_five = QLabel(self.frame)
        self.stock_news_five.setObjectName(u"stock_news_five")

        self.gridLayout_7.addWidget(self.stock_news_five, 5, 0, 1, 1)

        self.stock_news_one = QLabel(self.frame)
        self.stock_news_one.setObjectName(u"stock_news_one")

        self.gridLayout_7.addWidget(self.stock_news_one, 1, 0, 1, 1)

        self.stock_news_two = QLabel(self.frame)
        self.stock_news_two.setObjectName(u"stock_news_two")

        self.gridLayout_7.addWidget(self.stock_news_two, 2, 0, 1, 1)

        self.stock_news_four = QLabel(self.frame)
        self.stock_news_four.setObjectName(u"stock_news_four")

        self.gridLayout_7.addWidget(self.stock_news_four, 4, 0, 1, 1)

        self.stock_news_three = QLabel(self.frame)
        self.stock_news_three.setObjectName(u"stock_news_three")

        self.gridLayout_7.addWidget(self.stock_news_three, 3, 0, 1, 1)

        self.stock_news_stock_label = QLabel(self.frame)
        self.stock_news_stock_label.setObjectName(u"stock_news_stock_label")
        self.stock_news_stock_label.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.stock_news_stock_label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_32.addWidget(self.frame)

        self.stock_simulator_news_index_pointer_frame = QFrame(self.stock_simluator_news_content)
        self.stock_simulator_news_index_pointer_frame.setObjectName(u"stock_simulator_news_index_pointer_frame")
        self.stock_simulator_news_index_pointer_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_news_index_pointer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.stock_simulator_news_index_pointer_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.previous_button = QPushButton(self.stock_simulator_news_index_pointer_frame)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMinimumSize(QSize(0, 30))
        self.previous_button.setMaximumSize(QSize(300, 16777215))
        self.previous_button.setStyleSheet(u"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(74, 74, 255, 255), stop:0.795455 rgba(0, 255, 233, 255));\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.previous_button)

        self.next_button = QPushButton(self.stock_simulator_news_index_pointer_frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(0, 30))
        self.next_button.setMaximumSize(QSize(300, 16777215))
        self.next_button.setStyleSheet(u"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(74, 74, 255, 255), stop:0.795455 rgba(0, 255, 233, 255));\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.next_button)


        self.verticalLayout_32.addWidget(self.stock_simulator_news_index_pointer_frame)


        self.verticalLayout_28.addWidget(self.stock_simluator_news_content)

        self.stock_simulator_scrollArea.setWidget(self.stock_simulator_scroll_area_frame)

        self.verticalLayout_27.addWidget(self.stock_simulator_scrollArea)

        self.simulator_stacked_widget.addWidget(self.stock_simulator_page)

        self.verticalLayout_24.addWidget(self.simulator_stacked_widget)

        self.stacked_menu_pages.addWidget(self.trade)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_7 = QVBoxLayout(self.settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stacked_menu_pages.addWidget(self.settings)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.stacked_menu_pages.addWidget(self.about)

        self.verticalLayout_2.addWidget(self.stacked_menu_pages)


        self.horizontalLayout_7.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setStyleSheet(u"background-color: rgb(54, 79, 113);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.about_extra_content = QFrame(self.right_frame)
        self.about_extra_content.setObjectName(u"about_extra_content")
        font7 = QFont()
        font7.setPointSize(20)
        self.about_extra_content.setFont(font7)
        self.about_extra_content.setFrameShape(QFrame.StyledPanel)
        self.about_extra_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.about_extra_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 10, 0, 0)
        self.about_title = QLabel(self.about_extra_content)
        self.about_title.setObjectName(u"about_title")
        font8 = QFont()
        font8.setPointSize(25)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(True)
        font8.setWeight(75)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.about_title.setFont(font8)

        self.verticalLayout_4.addWidget(self.about_title)

        self.about_extra_content_frame = QFrame(self.about_extra_content)
        self.about_extra_content_frame.setObjectName(u"about_extra_content_frame")
        self.about_extra_content_frame.setFrameShape(QFrame.StyledPanel)
        self.about_extra_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.about_extra_content_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.github_symbol = QLabel(self.about_extra_content_frame)
        self.github_symbol.setObjectName(u"github_symbol")
        font9 = QFont()
        font9.setPointSize(13)
        self.github_symbol.setFont(font9)
        self.github_symbol.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_9.addWidget(self.github_symbol)

        self.github_link = QLabel(self.about_extra_content_frame)
        self.github_link.setObjectName(u"github_link")
        font10 = QFont()
        font10.setPointSize(16)
        self.github_link.setFont(font10)
        self.github_link.setOpenExternalLinks(True)
        self.github_link.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_9.addWidget(self.github_link)


        self.verticalLayout_4.addWidget(self.about_extra_content_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.about_extra_content, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(28, 32, 43);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.developed_by_theo_brown = QLabel(self.footer_left_frame)
        self.developed_by_theo_brown.setObjectName(u"developed_by_theo_brown")
        font11 = QFont()
        font11.setPointSize(12)
        self.developed_by_theo_brown.setFont(font11)
        self.developed_by_theo_brown.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.developed_by_theo_brown)


        self.horizontalLayout_4.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.help_button = QPushButton(self.footer_right_frame)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setFont(font11)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon8)
        self.help_button.setIconSize(QSize(32, 32))
        self.help_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.help_button, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_menu_pages.setCurrentIndex(3)
        self.stock_analysis_stackedWidget.setCurrentIndex(1)
        self.stacked_charts.setCurrentIndex(0)
        self.stacked_charts_2.setCurrentIndex(0)
        self.learning_pages_stackedWidget.setCurrentIndex(3)
        self.simulator_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_icon_button.setText("")
        self.menu_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Menu</span></p></body></html>", None))
        self.app_title_icon.setText("")
        self.app_name_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">INVESTING APP</span></p></body></html>", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_label.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.home_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.trade_label.setText(QCoreApplication.translate("MainWindow", u"Trade", None))
        self.trade_icon.setText("")
        self.about_icon.setText("")
        self.stock_analysis_label.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.stock_analysis_icon.setText("")
        self.learn_label.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.learn_icon.setText("")
        self.settings_icon.setText("")
        self.home_icon.setText("")
        self.home_page_title.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.home_page_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome to the future investor app!</p><p align=\"center\"><br/></p><p align=\"center\">This application is just meant to teach the basics of investing. You will be working with crypto, stocks and forex. </p><p align=\"center\"><br/></p><p align=\"center\">This application is meant for absolute begginers.<br/></p><p align=\"center\">Its features include:</p><p align=\"center\">- Quotes and chart visualization.</p><p align=\"center\">- Teaching on how stock, crypto and forex work.</p><p align=\"center\">- Quizzes to test knowledge.</p><p align=\"center\">- Trading simulator.</p><p align=\"center\">- Next day prediction. (Do not use a s real financial advice)</p></body></html>", None))
        self.stock_analysis_title.setText(QCoreApplication.translate("MainWindow", u"Currency/Stock analysis", None))
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a ticker", None))
        self.search_button.setText("")
        self.stock_analysis_stock_name.setText(QCoreApplication.translate("MainWindow", u"[Insert stock name]", None))
        self.stock_analysis_stock_info_content.setText(QCoreApplication.translate("MainWindow", u"[Info about stock]", None))
        self.ticker_label.setText(QCoreApplication.translate("MainWindow", u"Ticker", None))
        self.volume_label.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.price_traded_label.setText(QCoreApplication.translate("MainWindow", u"Price Traded", None))
        self.change_direction_label.setText(QCoreApplication.translate("MainWindow", u"Change direction", None))
        self.change_amount_label.setText(QCoreApplication.translate("MainWindow", u"Change amount", None))
        self.one_week_button.setText(QCoreApplication.translate("MainWindow", u"1 week", None))
        self.one_month_button.setText(QCoreApplication.translate("MainWindow", u"1 moth", None))
        self.one_year_button.setText(QCoreApplication.translate("MainWindow", u"1 year", None))
        self.five_year_button.setText(QCoreApplication.translate("MainWindow", u"5 year", None))
        self.max_button.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Chart goes here", None))
        self.week_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.week_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.week_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.week_high_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.week_open_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.week_low_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.extra_info_about_currency.setText(QCoreApplication.translate("MainWindow", u"[Extra  info about the currency", None))
        self.second_curency_label.setText(QCoreApplication.translate("MainWindow", u"[second currency]", None))
        self.first_currency_label.setText(QCoreApplication.translate("MainWindow", u"[first currency]", None))
        self.comparison_button.setText("")
        self.one_week_button_2.setText(QCoreApplication.translate("MainWindow", u"1 week", None))
        self.one_month_button_2.setText(QCoreApplication.translate("MainWindow", u"1 moth", None))
        self.one_year_button_2.setText(QCoreApplication.translate("MainWindow", u"1 year", None))
        self.five_year_button_2.setText(QCoreApplication.translate("MainWindow", u"5 year", None))
        self.max_button_2.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Chart goes here", None))
        self.curency_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.currency_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.currency_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.currency_high_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.currency_open_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.currency_low_placeholder.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.learn_start_page_title_label.setText(QCoreApplication.translate("MainWindow", u"LEARN", None))
        self.what_do_you_wish_to_learn_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">What do you wish to learn?</span></p></body></html>", None))
        self.stocks_button_learn.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.forex_button_learn.setText(QCoreApplication.translate("MainWindow", u"Forex", None))
        self.crypto_button_learn.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.stock_learning_content_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">STOCKS</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline; color:#ffffff;\">Table of contents</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">1. What is a stock?</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">2. Investing in stocks</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">3. Stock market capitalization</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">4. Stock Splits</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">5. What are dividends?</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">6. Finding Stocks for your portfolio</span></p><p align=\"center\"><span style=\" font-siz"
                        "e:11pt; color:#ffffff;\">7. Finding a broker</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">8. What affects the price of stock</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">9. Stock terminology</span></p></body></html>", None))
        self.crypto_learning_content_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">CRYPTOCURRENCY</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline; color:#ffffff;\">Table of contents</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">1. What is cryptocurrency?</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">2. Blockchain technology</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">3. Cryptocurrency mining</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">4. Initial coin offering</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">5. Finding a broker</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">6. Chosing the right cryptocurrency</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">7. What affects the price of cryptocu"
                        "rrency</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">8. Cryptocurrency terminology</span></p></body></html>", None))
        self.forex_learning_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">FOREX (FOREIGN EXCHANGE)</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">TABLE OF CONTENTS</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">1. What is Forex trading?</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">2. History of the Forex market</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">3. Major currencies</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">4. Basic Forex terminology</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">5. Where trading happens</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">6. How to connect to the market</span></p></body></html>", None))
        self.simulator_start_page_title_label.setText(QCoreApplication.translate("MainWindow", u"TRADE", None))
        self.simulator_start_page_content_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to the trading simulator! Chose the type below:", None))
        self.stocks_button_2.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.forex_button_2.setText(QCoreApplication.translate("MainWindow", u"Forex", None))
        self.crypto_button_2.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.stock_simulator_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">STOCK SIMULATOR</span></p></body></html>", None))
        self.stock_simulator_market_info_label.setText(QCoreApplication.translate("MainWindow", u"[Market state description]", None))
        self.stock_simulator_order_details_title.setText(QCoreApplication.translate("MainWindow", u"ORDER DETAILS", None))
        self.stock_simulator_stock_ticker_label.setText(QCoreApplication.translate("MainWindow", u"Stock symbol", None))
        self.stock_simulator_symbol_lookup_button.setText(QCoreApplication.translate("MainWindow", u"SYMBOL LOOKUP BUTTON", None))
        self.stock_simulator_transaction_label.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.stock_simulator_quantity_label.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.stock_simulator_purchase_button.setText(QCoreApplication.translate("MainWindow", u"PURCHASE", None))
        self.stock_simulator_pocket_label.setText(QCoreApplication.translate("MainWindow", u"POCKET", None))
        self.stock_simulator_cash_label.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.stock_simulator_actual_amount_of_cash.setText(QCoreApplication.translate("MainWindow", u"(Amount_of_cash)", None))
        self.stock_news_five.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_one.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_two.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_four.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_three.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_stock_label.setText(QCoreApplication.translate("MainWindow", u"[INSERT STOCK] NEWS", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.about_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">About</span></p></body></html>", None))
        self.github_symbol.setText("")
        self.github_link.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/Theo524/\"><span style=\" text-decoration: underline; color:#ffffff;\">Github</span></a></p></body></html>", None))
        self.developed_by_theo_brown.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Developed by Theo Brown</span></p></body></html>", None))
        self.help_button.setText("")
    # retranslateUi

