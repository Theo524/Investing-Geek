# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app interfacesEyaCf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app_icons
# Main app frontend
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 847)
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
        self.horizontalLayout.setContentsMargins(0, 0, 0, 3)
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
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.menu_icon_button.setFont(font1)
        self.menu_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_icon_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(60, 88, 125);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(71, 105, 149);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_icon_button.setIcon(icon)
        self.menu_icon_button.setIconSize(QSize(32, 32))
        self.menu_icon_button.setFlat(True)

        self.gridLayout_2.addWidget(self.menu_icon_button, 1, 0, 1, 1)

        self.menu_label = QLabel(self.header_left_frame)
        self.menu_label.setObjectName(u"menu_label")

        self.gridLayout_2.addWidget(self.menu_label, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.header_center_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.app_title_icon = QLabel(self.frame_3)
        self.app_title_icon.setObjectName(u"app_title_icon")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.app_title_icon.setFont(font2)
        self.app_title_icon.setPixmap(QPixmap(u":/icons/icons/activity.svg"))

        self.horizontalLayout_20.addWidget(self.app_title_icon)

        self.app_name_title = QLabel(self.frame_3)
        self.app_name_title.setObjectName(u"app_name_title")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.app_name_title.setFont(font3)

        self.horizontalLayout_20.addWidget(self.app_name_title)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.header_center_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(50, 0))
        self.frame_7.setMaximumSize(QSize(100, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignBottom)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(60, 88, 125);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(71, 105, 149);\n"
"}\n"
"")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setFlat(True)

        self.horizontalLayout_22.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setFlat(True)

        self.horizontalLayout_22.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))
        self.close_window_button.setFlat(True)

        self.horizontalLayout_22.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

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
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
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
        self.menu_frame.setMinimumSize(QSize(120, 0))
        self.menu_frame.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(60, 88, 125);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(71, 105, 149);\n"
"}\n"
"")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.trade_icon = QPushButton(self.menu_frame)
        self.trade_icon.setObjectName(u"trade_icon")
        self.trade_icon.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trade_icon.setIcon(icon4)
        self.trade_icon.setIconSize(QSize(32, 32))
        self.trade_icon.setFlat(True)

        self.gridLayout.addWidget(self.trade_icon, 3, 0, 1, 1, Qt.AlignLeft)

        self.stock_analysis_icon = QPushButton(self.menu_frame)
        self.stock_analysis_icon.setObjectName(u"stock_analysis_icon")
        self.stock_analysis_icon.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stock_analysis_icon.setIcon(icon5)
        self.stock_analysis_icon.setIconSize(QSize(32, 32))
        self.stock_analysis_icon.setFlat(True)

        self.gridLayout.addWidget(self.stock_analysis_icon, 1, 0, 1, 1, Qt.AlignLeft)

        self.home_icon = QPushButton(self.menu_frame)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_icon.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_icon.setIcon(icon6)
        self.home_icon.setIconSize(QSize(32, 32))
        self.home_icon.setFlat(True)

        self.gridLayout.addWidget(self.home_icon, 0, 0, 1, 1, Qt.AlignLeft)

        self.settings_icon = QPushButton(self.menu_frame)
        self.settings_icon.setObjectName(u"settings_icon")
        self.settings_icon.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_icon.setIcon(icon7)
        self.settings_icon.setIconSize(QSize(32, 32))
        self.settings_icon.setFlat(True)

        self.gridLayout.addWidget(self.settings_icon, 4, 0, 1, 1, Qt.AlignLeft)

        self.learn_icon = QPushButton(self.menu_frame)
        self.learn_icon.setObjectName(u"learn_icon")
        self.learn_icon.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.learn_icon.setIcon(icon8)
        self.learn_icon.setIconSize(QSize(32, 32))
        self.learn_icon.setFlat(True)

        self.gridLayout.addWidget(self.learn_icon, 2, 0, 1, 1, Qt.AlignLeft)

        self.about_icon = QPushButton(self.menu_frame)
        self.about_icon.setObjectName(u"about_icon")
        self.about_icon.setCursor(QCursor(Qt.ForbiddenCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_icon.setIcon(icon9)
        self.about_icon.setIconSize(QSize(32, 32))
        self.about_icon.setEnabled(False)
        self.about_icon.setFlat(True)

        self.gridLayout.addWidget(self.about_icon, 5, 0, 1, 1, Qt.AlignLeft)


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
        self.stacked_menu_pages.setStyleSheet(u"color: rgb(255, 255, 255);")
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
        self.home_page_frame.setGeometry(QRect(0, 0, 877, 718))
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
"")

        self.verticalLayout_8.addWidget(self.home_page_title, 0, Qt.AlignHCenter)

        self.home_page_content = QLabel(self.home_page_body)
        self.home_page_content.setObjectName(u"home_page_content")
        self.home_page_content.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"")

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
        self.stock_analysis_frame.setGeometry(QRect(0, 0, 860, 2069))
        self.verticalLayout_10 = QVBoxLayout(self.stock_analysis_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header = QFrame(self.stock_analysis_frame)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.header)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.frame_89 = QFrame(self.header)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 30))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_89)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.stock_analysis_title_frame = QFrame(self.frame_89)
        self.stock_analysis_title_frame.setObjectName(u"stock_analysis_title_frame")
        self.stock_analysis_title_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.stock_analysis_title_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stock_analysis_title = QLabel(self.stock_analysis_title_frame)
        self.stock_analysis_title.setObjectName(u"stock_analysis_title")
        self.stock_analysis_title.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.stock_analysis_title, 0, Qt.AlignHCenter)


        self.verticalLayout_137.addWidget(self.stock_analysis_title_frame)


        self.verticalLayout_136.addWidget(self.frame_89)


        self.verticalLayout_10.addWidget(self.header)

        self.stock_analysis_main_body = QFrame(self.stock_analysis_frame)
        self.stock_analysis_main_body.setObjectName(u"stock_analysis_main_body")
        self.stock_analysis_main_body.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.stock_analysis_main_body)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_92 = QFrame(self.stock_analysis_main_body)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(810, 0))
        self.frame_92.setMaximumSize(QSize(16777215, 16777215))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_92)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.frame_90 = QFrame(self.frame_92)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 0))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_entry = QLineEdit(self.frame_90)
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

        self.horizontalLayout_3.addWidget(self.search_entry)

        self.search_button = QPushButton(self.frame_90)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(49, 56, 74);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color:rgb(66, 74, 99);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon10)
        self.search_button.setIconSize(QSize(24, 24))
        self.search_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.search_button)


        self.verticalLayout_138.addWidget(self.frame_90, 0, Qt.AlignRight)


        self.verticalLayout_35.addWidget(self.frame_92, 0, Qt.AlignHCenter)

        self.stock_analysis_options_frame = QFrame(self.stock_analysis_main_body)
        self.stock_analysis_options_frame.setObjectName(u"stock_analysis_options_frame")
        self.stock_analysis_options_frame.setMinimumSize(QSize(0, 0))
        self.stock_analysis_options_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.stock_analysis_options_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ticker_label_title_analysis = QPushButton(self.stock_analysis_options_frame)
        self.ticker_label_title_analysis.setObjectName(u"ticker_label_title_analysis")
        self.ticker_label_title_analysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.ticker_label_title_analysis.setStyleSheet(u"QPushButton{\n"
"	font: 16pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(49, 56, 74);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color:rgb(66, 74, 99);\n"
"}")
        self.ticker_label_title_analysis.setFlat(True)

        self.verticalLayout_11.addWidget(self.ticker_label_title_analysis, 0, Qt.AlignHCenter)


        self.verticalLayout_35.addWidget(self.stock_analysis_options_frame)

        self.stock_analysis_stackedWidget = QStackedWidget(self.stock_analysis_main_body)
        self.stock_analysis_stackedWidget.setObjectName(u"stock_analysis_stackedWidget")
        self.stock_analysis_stackedWidget.setMinimumSize(QSize(0, 0))
        self.stock_analysis_stock_page = QWidget()
        self.stock_analysis_stock_page.setObjectName(u"stock_analysis_stock_page")
        self.verticalLayout_36 = QVBoxLayout(self.stock_analysis_stock_page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.stock_quote_frame = QFrame(self.stock_analysis_stock_page)
        self.stock_quote_frame.setObjectName(u"stock_quote_frame")
        self.stock_quote_frame.setMinimumSize(QSize(750, 0))
        self.stock_quote_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_quote_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.stock_quote_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.stock_change_frame = QFrame(self.stock_quote_frame)
        self.stock_change_frame.setObjectName(u"stock_change_frame")
        self.stock_change_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_change_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.stock_change_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.price_traded_label = QLabel(self.stock_change_frame)
        self.price_traded_label.setObjectName(u"price_traded_label")
        self.price_traded_label.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.price_traded_label)

        self.change_direction_label = QLabel(self.stock_change_frame)
        self.change_direction_label.setObjectName(u"change_direction_label")

        self.horizontalLayout_13.addWidget(self.change_direction_label, 0, Qt.AlignBottom)

        self.change_amount_label = QLabel(self.stock_change_frame)
        self.change_amount_label.setObjectName(u"change_amount_label")

        self.horizontalLayout_13.addWidget(self.change_amount_label, 0, Qt.AlignBottom)

        self.change_percentage = QLabel(self.stock_change_frame)
        self.change_percentage.setObjectName(u"change_percentage")

        self.horizontalLayout_13.addWidget(self.change_percentage, 0, Qt.AlignBottom)


        self.verticalLayout_34.addWidget(self.stock_change_frame, 0, Qt.AlignLeft)

        self.stock_analysis_stock_info_frame = QFrame(self.stock_quote_frame)
        self.stock_analysis_stock_info_frame.setObjectName(u"stock_analysis_stock_info_frame")
        self.stock_analysis_stock_info_frame.setMinimumSize(QSize(750, 0))
        self.stock_analysis_stock_info_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_stock_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.stock_analysis_stock_info_frame)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(9, -1, -1, -1)
        self.stock_analysis_stock_info_content = QLabel(self.stock_analysis_stock_info_frame)
        self.stock_analysis_stock_info_content.setObjectName(u"stock_analysis_stock_info_content")

        self.verticalLayout_39.addWidget(self.stock_analysis_stock_info_content)


        self.verticalLayout_34.addWidget(self.stock_analysis_stock_info_frame)


        self.verticalLayout_36.addWidget(self.stock_quote_frame)

        self.times_frame = QFrame(self.stock_analysis_stock_page)
        self.times_frame.setObjectName(u"times_frame")
        self.times_frame.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")
        self.times_frame.setFrameShape(QFrame.StyledPanel)
        self.times_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.times_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.one_day_button = QPushButton(self.times_frame)
        self.one_day_button.setObjectName(u"one_day_button")
        self.one_day_button.setMinimumSize(QSize(115, 30))
        self.one_day_button.setMaximumSize(QSize(16777215, 16777215))
        self.one_day_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_day_button.setStyleSheet(u"")
        self.one_day_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.one_day_button)

        self.one_week_button = QPushButton(self.times_frame)
        self.one_week_button.setObjectName(u"one_week_button")
        self.one_week_button.setMinimumSize(QSize(115, 30))
        self.one_week_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_week_button.setStyleSheet(u"")
        self.one_week_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.one_week_button)

        self.one_month_button = QPushButton(self.times_frame)
        self.one_month_button.setObjectName(u"one_month_button")
        self.one_month_button.setMinimumSize(QSize(115, 30))
        self.one_month_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_month_button.setStyleSheet(u"")
        self.one_month_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.one_month_button)

        self.one_year_button = QPushButton(self.times_frame)
        self.one_year_button.setObjectName(u"one_year_button")
        self.one_year_button.setMinimumSize(QSize(115, 30))
        self.one_year_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_year_button.setStyleSheet(u"")
        self.one_year_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.one_year_button)

        self.five_year_button = QPushButton(self.times_frame)
        self.five_year_button.setObjectName(u"five_year_button")
        self.five_year_button.setMinimumSize(QSize(115, 30))
        self.five_year_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.five_year_button.setStyleSheet(u"")
        self.five_year_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.five_year_button)

        self.max_button = QPushButton(self.times_frame)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMinimumSize(QSize(115, 30))
        self.max_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.max_button.setStyleSheet(u"")
        self.max_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.max_button)


        self.verticalLayout_36.addWidget(self.times_frame)

        self.charts = QFrame(self.stock_analysis_stock_page)
        self.charts.setObjectName(u"charts")
        self.charts.setFrameShape(QFrame.StyledPanel)
        self.charts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.charts)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.stacked_charts = QStackedWidget(self.charts)
        self.stacked_charts.setObjectName(u"stacked_charts")
        self.day_page = QWidget()
        self.day_page.setObjectName(u"day_page")
        self.verticalLayout_13 = QVBoxLayout(self.day_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.day_page_frame = QFrame(self.day_page)
        self.day_page_frame.setObjectName(u"day_page_frame")
        self.day_page_frame.setFrameShape(QFrame.StyledPanel)
        self.day_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.day_page_frame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.stock_chart = QWidget(self.day_page_frame)
        self.stock_chart.setObjectName(u"stock_chart")
        self.verticalLayout_47 = QVBoxLayout(self.stock_chart)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.stock_analysis_chart_frame = QFrame(self.stock_chart)
        self.stock_analysis_chart_frame.setObjectName(u"stock_analysis_chart_frame")
        self.stock_analysis_chart_frame.setMinimumSize(QSize(700, 400))
        self.stock_analysis_chart_frame.setMaximumSize(QSize(16777215, 16777215))
        self.stock_analysis_chart_frame.setFrameShape(QFrame.Box)
        self.stock_analysis_chart_frame.setFrameShadow(QFrame.Raised)
        self.stock_analysis_chart_cont = QGridLayout(self.stock_analysis_chart_frame)
        self.stock_analysis_chart_cont.setObjectName(u"stock_analysis_chart_cont")

        self.verticalLayout_47.addWidget(self.stock_analysis_chart_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.stock_chart, 0, Qt.AlignHCenter)

        self.line_6 = QFrame(self.day_page_frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(700, 0))
        self.line_6.setMaximumSize(QSize(700, 16777215))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_6, 0, Qt.AlignHCenter)

        self.day_info_frame = QFrame(self.day_page_frame)
        self.day_info_frame.setObjectName(u"day_info_frame")
        self.day_info_frame.setMinimumSize(QSize(700, 0))
        self.day_info_frame.setFrameShape(QFrame.StyledPanel)
        self.day_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.day_info_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.info_box = QFrame(self.day_info_frame)
        self.info_box.setObjectName(u"info_box")
        self.info_box.setFrameShape(QFrame.StyledPanel)
        self.info_box.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.info_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.day_high_placeholder = QLabel(self.info_box)
        self.day_high_placeholder.setObjectName(u"day_high_placeholder")

        self.gridLayout_3.addWidget(self.day_high_placeholder, 1, 1, 1, 1)

        self.day_low = QLabel(self.info_box)
        self.day_low.setObjectName(u"day_low")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.day_low.setFont(font5)

        self.gridLayout_3.addWidget(self.day_low, 2, 0, 1, 1)

        self.day_high = QLabel(self.info_box)
        self.day_high.setObjectName(u"day_high")
        self.day_high.setFont(font5)

        self.gridLayout_3.addWidget(self.day_high, 1, 0, 1, 1)

        self.day_open = QLabel(self.info_box)
        self.day_open.setObjectName(u"day_open")
        self.day_open.setFont(font5)

        self.gridLayout_3.addWidget(self.day_open, 0, 0, 1, 1)

        self.day_open_placeholder = QLabel(self.info_box)
        self.day_open_placeholder.setObjectName(u"day_open_placeholder")

        self.gridLayout_3.addWidget(self.day_open_placeholder, 0, 1, 1, 1)

        self.day_low_placeholder = QLabel(self.info_box)
        self.day_low_placeholder.setObjectName(u"day_low_placeholder")

        self.gridLayout_3.addWidget(self.day_low_placeholder, 2, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.info_box)

        self.line_4 = QFrame(self.day_info_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_4)

        self.size_grip_2 = QFrame(self.day_info_frame)
        self.size_grip_2.setObjectName(u"size_grip_2")
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.size_grip_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.avg_volume_placeholder = QLabel(self.size_grip_2)
        self.avg_volume_placeholder.setObjectName(u"avg_volume_placeholder")

        self.gridLayout_5.addWidget(self.avg_volume_placeholder, 1, 2, 1, 1)

        self.avg_volume = QLabel(self.size_grip_2)
        self.avg_volume.setObjectName(u"avg_volume")
        self.avg_volume.setFont(font5)

        self.gridLayout_5.addWidget(self.avg_volume, 1, 0, 1, 1)

        self.market_cap_placeholder = QLabel(self.size_grip_2)
        self.market_cap_placeholder.setObjectName(u"market_cap_placeholder")

        self.gridLayout_5.addWidget(self.market_cap_placeholder, 2, 2, 1, 1)

        self.volume_placeholder = QLabel(self.size_grip_2)
        self.volume_placeholder.setObjectName(u"volume_placeholder")

        self.gridLayout_5.addWidget(self.volume_placeholder, 0, 2, 1, 1)

        self.volume_label = QLabel(self.size_grip_2)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setFont(font5)

        self.gridLayout_5.addWidget(self.volume_label, 0, 0, 1, 1)

        self.market_cap = QLabel(self.size_grip_2)
        self.market_cap.setObjectName(u"market_cap")
        self.market_cap.setFont(font5)

        self.gridLayout_5.addWidget(self.market_cap, 2, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.size_grip_2)

        self.line_5 = QFrame(self.day_info_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_5)

        self.frame_2 = QFrame(self.day_info_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.fifty_two_week_high = QLabel(self.frame_2)
        self.fifty_two_week_high.setObjectName(u"fifty_two_week_high")
        self.fifty_two_week_high.setFont(font5)

        self.gridLayout_11.addWidget(self.fifty_two_week_high, 0, 0, 1, 1)

        self.fifty_two_week_high_placeholder = QLabel(self.frame_2)
        self.fifty_two_week_high_placeholder.setObjectName(u"fifty_two_week_high_placeholder")

        self.gridLayout_11.addWidget(self.fifty_two_week_high_placeholder, 0, 1, 1, 1)

        self.fifty_two_week_low_placeholder = QLabel(self.frame_2)
        self.fifty_two_week_low_placeholder.setObjectName(u"fifty_two_week_low_placeholder")

        self.gridLayout_11.addWidget(self.fifty_two_week_low_placeholder, 1, 1, 1, 1)

        self.fifty_two_week_low = QLabel(self.frame_2)
        self.fifty_two_week_low.setObjectName(u"fifty_two_week_low")
        self.fifty_two_week_low.setFont(font5)

        self.gridLayout_11.addWidget(self.fifty_two_week_low, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_11.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_2)


        self.verticalLayout_46.addWidget(self.day_info_frame, 0, Qt.AlignHCenter)

        self.line_7 = QFrame(self.day_page_frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(700, 0))
        self.line_7.setMaximumSize(QSize(700, 16777215))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_7, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.day_page_frame)

        self.stacked_charts.addWidget(self.day_page)

        self.verticalLayout_12.addWidget(self.stacked_charts)


        self.verticalLayout_36.addWidget(self.charts)

        self.stock_analysis_news_frame = QFrame(self.stock_analysis_stock_page)
        self.stock_analysis_news_frame.setObjectName(u"stock_analysis_news_frame")
        self.stock_analysis_news_frame.setMinimumSize(QSize(800, 0))
        self.stock_analysis_news_frame.setMaximumSize(QSize(1050, 16777215))
        self.stock_analysis_news_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_news_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.stock_analysis_news_frame)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(-1, 50, -1, -1)
        self.frame_8 = QFrame(self.stock_analysis_news_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_8)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")

        self.verticalLayout_58.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_57.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.stock_analysis_news_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 300))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 100))
        self.frame_12.setMaximumSize(QSize(250, 280))
        self.frame_12.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_12)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.stock_news_title_frame = QFrame(self.frame_12)
        self.stock_news_title_frame.setObjectName(u"stock_news_title_frame")
        self.stock_news_title_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.stock_news_title_frame)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.stock_news_title = QLabel(self.stock_news_title_frame)
        self.stock_news_title.setObjectName(u"stock_news_title")
        self.stock_news_title.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.stock_news_title)


        self.verticalLayout_59.addWidget(self.stock_news_title_frame)

        self.frame_29 = QFrame(self.frame_12)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy1)
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_29)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.stock_news_text = QLabel(self.frame_29)
        self.stock_news_text.setObjectName(u"stock_news_text")
        self.stock_news_text.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text.setWordWrap(True)
        self.stock_news_text.setOpenExternalLinks(False)
        self.stock_news_text.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_80.addWidget(self.stock_news_text)


        self.verticalLayout_59.addWidget(self.frame_29)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.stock_news_media = QLabel(self.frame_21)
        self.stock_news_media.setObjectName(u"stock_news_media")
        self.stock_news_media.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.stock_news_media, 0, Qt.AlignBottom)


        self.verticalLayout_59.addWidget(self.frame_21, 0, Qt.AlignBottom)


        self.horizontalLayout_23.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(100, 100))
        self.frame_14.setMaximumSize(QSize(250, 280))
        self.frame_14.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_14)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.stock_news_title_frame_6 = QFrame(self.frame_14)
        self.stock_news_title_frame_6.setObjectName(u"stock_news_title_frame_6")
        self.stock_news_title_frame_6.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.stock_news_title_frame_6)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.stock_news_title_6 = QLabel(self.stock_news_title_frame_6)
        self.stock_news_title_6.setObjectName(u"stock_news_title_6")
        self.stock_news_title_6.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_6.setWordWrap(True)

        self.verticalLayout_71.addWidget(self.stock_news_title_6)


        self.verticalLayout_70.addWidget(self.stock_news_title_frame_6)

        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.frame_33.setMinimumSize(QSize(0, 0))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_33)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.stock_news_text_6 = QLabel(self.frame_33)
        self.stock_news_text_6.setObjectName(u"stock_news_text_6")
        self.stock_news_text_6.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_6.setWordWrap(True)
        self.stock_news_text_6.setOpenExternalLinks(False)
        self.stock_news_text_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_84.addWidget(self.stock_news_text_6)


        self.verticalLayout_70.addWidget(self.frame_33)

        self.frame_26 = QFrame(self.frame_14)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.stock_news_media_6 = QLabel(self.frame_26)
        self.stock_news_media_6.setObjectName(u"stock_news_media_6")
        self.stock_news_media_6.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_6.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.stock_news_media_6, 0, Qt.AlignBottom)


        self.verticalLayout_70.addWidget(self.frame_26, 0, Qt.AlignBottom)


        self.horizontalLayout_23.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(100, 100))
        self.frame_13.setMaximumSize(QSize(250, 280))
        self.frame_13.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_13)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.stock_news_title_frame_5 = QFrame(self.frame_13)
        self.stock_news_title_frame_5.setObjectName(u"stock_news_title_frame_5")
        self.stock_news_title_frame_5.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.stock_news_title_frame_5)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.stock_news_title_5 = QLabel(self.stock_news_title_frame_5)
        self.stock_news_title_5.setObjectName(u"stock_news_title_5")
        self.stock_news_title_5.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_5.setWordWrap(True)

        self.verticalLayout_69.addWidget(self.stock_news_title_5)


        self.verticalLayout_68.addWidget(self.stock_news_title_frame_5)

        self.frame_32 = QFrame(self.frame_13)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_32)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.stock_news_text_5 = QLabel(self.frame_32)
        self.stock_news_text_5.setObjectName(u"stock_news_text_5")
        self.stock_news_text_5.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_5.setWordWrap(True)
        self.stock_news_text_5.setOpenExternalLinks(False)
        self.stock_news_text_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_83.addWidget(self.stock_news_text_5)


        self.verticalLayout_68.addWidget(self.frame_32)

        self.frame_24 = QFrame(self.frame_13)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.stock_news_media_5 = QLabel(self.frame_24)
        self.stock_news_media_5.setObjectName(u"stock_news_media_5")
        self.stock_news_media_5.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_5.setWordWrap(True)

        self.horizontalLayout_31.addWidget(self.stock_news_media_5, 0, Qt.AlignBottom)


        self.verticalLayout_68.addWidget(self.frame_24, 0, Qt.AlignBottom)


        self.horizontalLayout_23.addWidget(self.frame_13)


        self.verticalLayout_57.addWidget(self.frame_10)

        self.frame_18 = QFrame(self.stock_analysis_news_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(100, 100))
        self.frame_19.setMaximumSize(QSize(250, 280))
        self.frame_19.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_19)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.stock_news_title_frame_10 = QFrame(self.frame_19)
        self.stock_news_title_frame_10.setObjectName(u"stock_news_title_frame_10")
        self.stock_news_title_frame_10.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.stock_news_title_frame_10)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.stock_news_title_10 = QLabel(self.stock_news_title_frame_10)
        self.stock_news_title_10.setObjectName(u"stock_news_title_10")
        self.stock_news_title_10.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_10.setWordWrap(True)

        self.verticalLayout_79.addWidget(self.stock_news_title_10)


        self.verticalLayout_78.addWidget(self.stock_news_title_frame_10)

        self.frame_38 = QFrame(self.frame_19)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.frame_38.setMinimumSize(QSize(0, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_38)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.stock_news_text_10 = QLabel(self.frame_38)
        self.stock_news_text_10.setObjectName(u"stock_news_text_10")
        self.stock_news_text_10.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_10.setWordWrap(True)
        self.stock_news_text_10.setOpenExternalLinks(False)
        self.stock_news_text_10.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_88.addWidget(self.stock_news_text_10)


        self.verticalLayout_78.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_19)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.stock_news_media_10 = QLabel(self.frame_39)
        self.stock_news_media_10.setObjectName(u"stock_news_media_10")
        self.stock_news_media_10.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_10.setWordWrap(True)

        self.horizontalLayout_36.addWidget(self.stock_news_media_10, 0, Qt.AlignBottom)


        self.verticalLayout_78.addWidget(self.frame_39, 0, Qt.AlignBottom)


        self.horizontalLayout_25.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(100, 100))
        self.frame_20.setMaximumSize(QSize(250, 280))
        self.frame_20.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_20.setFrameShape(QFrame.Box)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_20)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.stock_news_title_frame_11 = QFrame(self.frame_20)
        self.stock_news_title_frame_11.setObjectName(u"stock_news_title_frame_11")
        self.stock_news_title_frame_11.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.stock_news_title_frame_11)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.stock_news_title_11 = QLabel(self.stock_news_title_frame_11)
        self.stock_news_title_11.setObjectName(u"stock_news_title_11")
        self.stock_news_title_11.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_11.setWordWrap(True)

        self.verticalLayout_90.addWidget(self.stock_news_title_11)


        self.verticalLayout_89.addWidget(self.stock_news_title_frame_11)

        self.frame_40 = QFrame(self.frame_20)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setMinimumSize(QSize(0, 0))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_40)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.stock_news_text_11 = QLabel(self.frame_40)
        self.stock_news_text_11.setObjectName(u"stock_news_text_11")
        self.stock_news_text_11.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_11.setWordWrap(True)
        self.stock_news_text_11.setOpenExternalLinks(False)
        self.stock_news_text_11.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_91.addWidget(self.stock_news_text_11)


        self.verticalLayout_89.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_20)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.stock_news_media_11 = QLabel(self.frame_41)
        self.stock_news_media_11.setObjectName(u"stock_news_media_11")
        self.stock_news_media_11.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_11.setWordWrap(True)

        self.horizontalLayout_37.addWidget(self.stock_news_media_11, 0, Qt.AlignBottom)


        self.verticalLayout_89.addWidget(self.frame_41, 0, Qt.AlignBottom)


        self.horizontalLayout_25.addWidget(self.frame_20)

        self.frame_42 = QFrame(self.frame_18)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(100, 100))
        self.frame_42.setMaximumSize(QSize(250, 280))
        self.frame_42.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_42.setFrameShape(QFrame.Box)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_42)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.stock_news_title_frame_12 = QFrame(self.frame_42)
        self.stock_news_title_frame_12.setObjectName(u"stock_news_title_frame_12")
        self.stock_news_title_frame_12.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.stock_news_title_frame_12)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.stock_news_title_12 = QLabel(self.stock_news_title_frame_12)
        self.stock_news_title_12.setObjectName(u"stock_news_title_12")
        self.stock_news_title_12.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_12.setWordWrap(True)

        self.verticalLayout_93.addWidget(self.stock_news_title_12)


        self.verticalLayout_92.addWidget(self.stock_news_title_frame_12)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy1.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy1)
        self.frame_43.setMinimumSize(QSize(0, 0))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_43)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.stock_news_text_12 = QLabel(self.frame_43)
        self.stock_news_text_12.setObjectName(u"stock_news_text_12")
        self.stock_news_text_12.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_12.setWordWrap(True)
        self.stock_news_text_12.setOpenExternalLinks(False)
        self.stock_news_text_12.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_94.addWidget(self.stock_news_text_12)


        self.verticalLayout_92.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.stock_news_media_12 = QLabel(self.frame_44)
        self.stock_news_media_12.setObjectName(u"stock_news_media_12")
        self.stock_news_media_12.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_12.setWordWrap(True)

        self.horizontalLayout_38.addWidget(self.stock_news_media_12, 0, Qt.AlignBottom)


        self.verticalLayout_92.addWidget(self.frame_44, 0, Qt.AlignBottom)


        self.horizontalLayout_25.addWidget(self.frame_42)


        self.verticalLayout_57.addWidget(self.frame_18)

        self.frame_11 = QFrame(self.stock_analysis_news_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 300))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(100, 100))
        self.frame_15.setMaximumSize(QSize(250, 280))
        self.frame_15.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_15)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.stock_news_title_frame_7 = QFrame(self.frame_15)
        self.stock_news_title_frame_7.setObjectName(u"stock_news_title_frame_7")
        self.stock_news_title_frame_7.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.stock_news_title_frame_7)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.stock_news_title_7 = QLabel(self.stock_news_title_frame_7)
        self.stock_news_title_7.setObjectName(u"stock_news_title_7")
        self.stock_news_title_7.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_7.setWordWrap(True)

        self.verticalLayout_73.addWidget(self.stock_news_title_7)


        self.verticalLayout_72.addWidget(self.stock_news_title_frame_7)

        self.frame_34 = QFrame(self.frame_15)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy1.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy1)
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_34)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.stock_news_text_7 = QLabel(self.frame_34)
        self.stock_news_text_7.setObjectName(u"stock_news_text_7")
        self.stock_news_text_7.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_7.setWordWrap(True)
        self.stock_news_text_7.setOpenExternalLinks(False)
        self.stock_news_text_7.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_85.addWidget(self.stock_news_text_7)


        self.verticalLayout_72.addWidget(self.frame_34)

        self.frame_27 = QFrame(self.frame_15)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.stock_news_media_7 = QLabel(self.frame_27)
        self.stock_news_media_7.setObjectName(u"stock_news_media_7")
        self.stock_news_media_7.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_7.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.stock_news_media_7, 0, Qt.AlignBottom)


        self.verticalLayout_72.addWidget(self.frame_27, 0, Qt.AlignBottom)


        self.horizontalLayout_24.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(100, 100))
        self.frame_16.setMaximumSize(QSize(250, 280))
        self.frame_16.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_16)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.stock_news_title_frame_8 = QFrame(self.frame_16)
        self.stock_news_title_frame_8.setObjectName(u"stock_news_title_frame_8")
        self.stock_news_title_frame_8.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.stock_news_title_frame_8)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.stock_news_title_8 = QLabel(self.stock_news_title_frame_8)
        self.stock_news_title_8.setObjectName(u"stock_news_title_8")
        self.stock_news_title_8.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_8.setWordWrap(True)

        self.verticalLayout_75.addWidget(self.stock_news_title_8)


        self.verticalLayout_74.addWidget(self.stock_news_title_frame_8)

        self.frame_35 = QFrame(self.frame_16)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy1.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy1)
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_35)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.stock_news_text_8 = QLabel(self.frame_35)
        self.stock_news_text_8.setObjectName(u"stock_news_text_8")
        self.stock_news_text_8.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_8.setWordWrap(True)
        self.stock_news_text_8.setOpenExternalLinks(False)
        self.stock_news_text_8.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_86.addWidget(self.stock_news_text_8)


        self.verticalLayout_74.addWidget(self.frame_35)

        self.frame_28 = QFrame(self.frame_16)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.stock_news_media_8 = QLabel(self.frame_28)
        self.stock_news_media_8.setObjectName(u"stock_news_media_8")
        self.stock_news_media_8.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.stock_news_media_8.setWordWrap(True)

        self.horizontalLayout_34.addWidget(self.stock_news_media_8, 0, Qt.AlignBottom)


        self.verticalLayout_74.addWidget(self.frame_28, 0, Qt.AlignBottom)


        self.horizontalLayout_24.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(100, 100))
        self.frame_17.setMaximumSize(QSize(250, 280))
        self.frame_17.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_17)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.stock_news_title_frame_9 = QFrame(self.frame_17)
        self.stock_news_title_frame_9.setObjectName(u"stock_news_title_frame_9")
        self.stock_news_title_frame_9.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.stock_news_title_frame_9)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.stock_news_title_9 = QLabel(self.stock_news_title_frame_9)
        self.stock_news_title_9.setObjectName(u"stock_news_title_9")
        self.stock_news_title_9.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_9.setWordWrap(True)

        self.verticalLayout_77.addWidget(self.stock_news_title_9)


        self.verticalLayout_76.addWidget(self.stock_news_title_frame_9)

        self.frame_36 = QFrame(self.frame_17)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy1.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy1)
        self.frame_36.setMinimumSize(QSize(0, 0))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_36)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.stock_news_text_9 = QLabel(self.frame_36)
        self.stock_news_text_9.setObjectName(u"stock_news_text_9")
        self.stock_news_text_9.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_9.setWordWrap(True)
        self.stock_news_text_9.setOpenExternalLinks(False)
        self.stock_news_text_9.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_87.addWidget(self.stock_news_text_9)


        self.verticalLayout_76.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_17)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.stock_news_media_9 = QLabel(self.frame_37)
        self.stock_news_media_9.setObjectName(u"stock_news_media_9")
        self.stock_news_media_9.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_9.setWordWrap(True)

        self.horizontalLayout_35.addWidget(self.stock_news_media_9, 0, Qt.AlignBottom)


        self.verticalLayout_76.addWidget(self.frame_37, 0, Qt.AlignBottom)


        self.horizontalLayout_24.addWidget(self.frame_17)


        self.verticalLayout_57.addWidget(self.frame_11)


        self.verticalLayout_36.addWidget(self.stock_analysis_news_frame)

        self.stock_analysis_stackedWidget.addWidget(self.stock_analysis_stock_page)
        self.stock_analysis_currency_page = QWidget()
        self.stock_analysis_currency_page.setObjectName(u"stock_analysis_currency_page")
        self.verticalLayout_40 = QVBoxLayout(self.stock_analysis_currency_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.crypto_quote_frame = QFrame(self.stock_analysis_currency_page)
        self.crypto_quote_frame.setObjectName(u"crypto_quote_frame")
        self.crypto_quote_frame.setMinimumSize(QSize(750, 0))
        self.crypto_quote_frame.setFrameShape(QFrame.StyledPanel)
        self.crypto_quote_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.crypto_quote_frame)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_5 = QFrame(self.crypto_quote_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.crypto_price_label = QLabel(self.frame_5)
        self.crypto_price_label.setObjectName(u"crypto_price_label")

        self.horizontalLayout_12.addWidget(self.crypto_price_label)

        self.crypto_currency_price_label = QLabel(self.frame_5)
        self.crypto_currency_price_label.setObjectName(u"crypto_currency_price_label")

        self.horizontalLayout_12.addWidget(self.crypto_currency_price_label)


        self.verticalLayout_54.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.crypto_quote_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_6)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(-1, 0, -1, -1)
        self.extra_info_about_crypto = QLabel(self.frame_6)
        self.extra_info_about_crypto.setObjectName(u"extra_info_about_crypto")

        self.verticalLayout_55.addWidget(self.extra_info_about_crypto, 0, Qt.AlignTop)


        self.verticalLayout_54.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.currency_comparison_frame = QFrame(self.crypto_quote_frame)
        self.currency_comparison_frame.setObjectName(u"currency_comparison_frame")
        self.currency_comparison_frame.setStyleSheet(u"QLineEdit{\n"
"	border-radius:7px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	color:rgb(0, 0, 0);\n"
"	font: 75 18pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(49, 56, 74);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color:rgb(66, 74, 99);\n"
"}\n"
"")
        self.currency_comparison_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_comparison_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.currency_comparison_frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.second_currency_entry = QLineEdit(self.currency_comparison_frame)
        self.second_currency_entry.setObjectName(u"second_currency_entry")
        self.second_currency_entry.setMinimumSize(QSize(0, 40))
        self.second_currency_entry.setMaximumSize(QSize(250, 40))
        self.second_currency_entry.setStyleSheet(u"")
        self.second_currency_entry.setAlignment(Qt.AlignCenter)
        self.second_currency_entry.setReadOnly(True)

        self.gridLayout_10.addWidget(self.second_currency_entry, 3, 2, 1, 1)

        self.first_currency_entry = QLineEdit(self.currency_comparison_frame)
        self.first_currency_entry.setObjectName(u"first_currency_entry")
        self.first_currency_entry.setMinimumSize(QSize(0, 40))
        self.first_currency_entry.setMaximumSize(QSize(250, 40))
        self.first_currency_entry.setStyleSheet(u"")
        self.first_currency_entry.setAlignment(Qt.AlignCenter)
        self.first_currency_entry.setReadOnly(False)

        self.gridLayout_10.addWidget(self.first_currency_entry, 3, 0, 1, 1)

        self.second_curency_label = QLabel(self.currency_comparison_frame)
        self.second_curency_label.setObjectName(u"second_curency_label")

        self.gridLayout_10.addWidget(self.second_curency_label, 0, 2, 1, 1, Qt.AlignHCenter)

        self.first_currency_label = QLabel(self.currency_comparison_frame)
        self.first_currency_label.setObjectName(u"first_currency_label")

        self.gridLayout_10.addWidget(self.first_currency_label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.crypto_comparison_button = QPushButton(self.currency_comparison_frame)
        self.crypto_comparison_button.setObjectName(u"crypto_comparison_button")
        self.crypto_comparison_button.setMaximumSize(QSize(35, 16777215))
        self.crypto_comparison_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.crypto_comparison_button.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.crypto_comparison_button.setIcon(icon11)
        self.crypto_comparison_button.setIconSize(QSize(32, 32))
        self.crypto_comparison_button.setFlat(True)

        self.gridLayout_10.addWidget(self.crypto_comparison_button, 3, 1, 1, 1)


        self.verticalLayout_54.addWidget(self.currency_comparison_frame)


        self.verticalLayout_40.addWidget(self.crypto_quote_frame)

        self.times_frame_2 = QFrame(self.stock_analysis_currency_page)
        self.times_frame_2.setObjectName(u"times_frame_2")
        self.times_frame_2.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")
        self.times_frame_2.setFrameShape(QFrame.StyledPanel)
        self.times_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.times_frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.one_day_button_2 = QPushButton(self.times_frame_2)
        self.one_day_button_2.setObjectName(u"one_day_button_2")
        self.one_day_button_2.setMinimumSize(QSize(115, 30))
        self.one_day_button_2.setMaximumSize(QSize(16777215, 16777215))
        self.one_day_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_day_button_2.setStyleSheet(u"")
        self.one_day_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_day_button_2)

        self.one_week_button_2 = QPushButton(self.times_frame_2)
        self.one_week_button_2.setObjectName(u"one_week_button_2")
        self.one_week_button_2.setMinimumSize(QSize(115, 30))
        self.one_week_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_week_button_2.setStyleSheet(u"")
        self.one_week_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_week_button_2)

        self.one_month_button_2 = QPushButton(self.times_frame_2)
        self.one_month_button_2.setObjectName(u"one_month_button_2")
        self.one_month_button_2.setMinimumSize(QSize(115, 30))
        self.one_month_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_month_button_2.setStyleSheet(u"")
        self.one_month_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_month_button_2)

        self.one_year_button_2 = QPushButton(self.times_frame_2)
        self.one_year_button_2.setObjectName(u"one_year_button_2")
        self.one_year_button_2.setMinimumSize(QSize(115, 30))
        self.one_year_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_year_button_2.setStyleSheet(u"")
        self.one_year_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.one_year_button_2)

        self.five_year_button_2 = QPushButton(self.times_frame_2)
        self.five_year_button_2.setObjectName(u"five_year_button_2")
        self.five_year_button_2.setMinimumSize(QSize(115, 30))
        self.five_year_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.five_year_button_2.setStyleSheet(u"")
        self.five_year_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.five_year_button_2)

        self.max_button_2 = QPushButton(self.times_frame_2)
        self.max_button_2.setObjectName(u"max_button_2")
        self.max_button_2.setMinimumSize(QSize(115, 30))
        self.max_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.max_button_2.setStyleSheet(u"")
        self.max_button_2.setFlat(False)

        self.horizontalLayout_19.addWidget(self.max_button_2)


        self.verticalLayout_40.addWidget(self.times_frame_2)

        self.charts_2 = QFrame(self.stock_analysis_currency_page)
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
        self.verticalLayout_56 = QVBoxLayout(self.chart_frame_2)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.crypto_analysis_chart_frame = QFrame(self.chart_frame_2)
        self.crypto_analysis_chart_frame.setObjectName(u"crypto_analysis_chart_frame")
        self.crypto_analysis_chart_frame.setMinimumSize(QSize(700, 400))
        self.crypto_analysis_chart_frame.setFrameShape(QFrame.Box)
        self.crypto_analysis_chart_frame.setFrameShadow(QFrame.Raised)
        self.crypto_analysis_chart_cont = QGridLayout(self.crypto_analysis_chart_frame)
        self.crypto_analysis_chart_cont.setObjectName(u"crypto_analysis_chart_cont")

        self.verticalLayout_56.addWidget(self.crypto_analysis_chart_frame)


        self.verticalLayout_38.addWidget(self.chart_frame_2)

        self.stacked_charts_2.addWidget(self.week_page_2)

        self.verticalLayout_37.addWidget(self.stacked_charts_2)


        self.verticalLayout_40.addWidget(self.charts_2)

        self.stock_analysis_news_frame_2 = QFrame(self.stock_analysis_currency_page)
        self.stock_analysis_news_frame_2.setObjectName(u"stock_analysis_news_frame_2")
        self.stock_analysis_news_frame_2.setMinimumSize(QSize(800, 0))
        self.stock_analysis_news_frame_2.setMaximumSize(QSize(1050, 16777215))
        self.stock_analysis_news_frame_2.setFrameShape(QFrame.StyledPanel)
        self.stock_analysis_news_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.stock_analysis_news_frame_2)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(-1, 50, -1, -1)
        self.frame_22 = QFrame(self.stock_analysis_news_frame_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_22)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_2 = QLabel(self.frame_22)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")

        self.verticalLayout_62.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_61.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.stock_analysis_news_frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 300))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(100, 100))
        self.frame_25.setMaximumSize(QSize(250, 280))
        self.frame_25.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_25)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.stock_news_title_frame_2 = QFrame(self.frame_25)
        self.stock_news_title_frame_2.setObjectName(u"stock_news_title_frame_2")
        self.stock_news_title_frame_2.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.stock_news_title_frame_2)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.stock_news_title_2 = QLabel(self.stock_news_title_frame_2)
        self.stock_news_title_2.setObjectName(u"stock_news_title_2")
        self.stock_news_title_2.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_2.setWordWrap(True)

        self.verticalLayout_64.addWidget(self.stock_news_title_2)


        self.verticalLayout_63.addWidget(self.stock_news_title_frame_2)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_30)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.stock_news_text_2 = QLabel(self.frame_30)
        self.stock_news_text_2.setObjectName(u"stock_news_text_2")
        self.stock_news_text_2.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_2.setWordWrap(True)
        self.stock_news_text_2.setOpenExternalLinks(False)
        self.stock_news_text_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_81.addWidget(self.stock_news_text_2)


        self.verticalLayout_63.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.stock_news_media_2 = QLabel(self.frame_31)
        self.stock_news_media_2.setObjectName(u"stock_news_media_2")
        self.stock_news_media_2.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_2.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.stock_news_media_2, 0, Qt.AlignBottom)


        self.verticalLayout_63.addWidget(self.frame_31, 0, Qt.AlignBottom)


        self.horizontalLayout_28.addWidget(self.frame_25)

        self.frame_45 = QFrame(self.frame_23)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(100, 100))
        self.frame_45.setMaximumSize(QSize(250, 280))
        self.frame_45.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_45.setFrameShape(QFrame.Box)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_45)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.stock_news_title_frame_13 = QFrame(self.frame_45)
        self.stock_news_title_frame_13.setObjectName(u"stock_news_title_frame_13")
        self.stock_news_title_frame_13.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.stock_news_title_frame_13)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.stock_news_title_13 = QLabel(self.stock_news_title_frame_13)
        self.stock_news_title_13.setObjectName(u"stock_news_title_13")
        self.stock_news_title_13.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_13.setWordWrap(True)

        self.verticalLayout_95.addWidget(self.stock_news_title_13)


        self.verticalLayout_82.addWidget(self.stock_news_title_frame_13)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy1.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy1)
        self.frame_46.setMinimumSize(QSize(0, 0))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_46)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.stock_news_text_13 = QLabel(self.frame_46)
        self.stock_news_text_13.setObjectName(u"stock_news_text_13")
        self.stock_news_text_13.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_13.setWordWrap(True)
        self.stock_news_text_13.setOpenExternalLinks(False)
        self.stock_news_text_13.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_96.addWidget(self.stock_news_text_13)


        self.verticalLayout_82.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.stock_news_media_13 = QLabel(self.frame_47)
        self.stock_news_media_13.setObjectName(u"stock_news_media_13")
        self.stock_news_media_13.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_13.setWordWrap(True)

        self.horizontalLayout_39.addWidget(self.stock_news_media_13, 0, Qt.AlignBottom)


        self.verticalLayout_82.addWidget(self.frame_47, 0, Qt.AlignBottom)


        self.horizontalLayout_28.addWidget(self.frame_45)

        self.frame_48 = QFrame(self.frame_23)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(100, 100))
        self.frame_48.setMaximumSize(QSize(250, 280))
        self.frame_48.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_48.setFrameShape(QFrame.Box)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_48)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.stock_news_title_frame_14 = QFrame(self.frame_48)
        self.stock_news_title_frame_14.setObjectName(u"stock_news_title_frame_14")
        self.stock_news_title_frame_14.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.stock_news_title_frame_14)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.stock_news_title_14 = QLabel(self.stock_news_title_frame_14)
        self.stock_news_title_14.setObjectName(u"stock_news_title_14")
        self.stock_news_title_14.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_14.setWordWrap(True)

        self.verticalLayout_98.addWidget(self.stock_news_title_14)


        self.verticalLayout_97.addWidget(self.stock_news_title_frame_14)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy1.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy1)
        self.frame_49.setMinimumSize(QSize(0, 0))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_49)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.stock_news_text_14 = QLabel(self.frame_49)
        self.stock_news_text_14.setObjectName(u"stock_news_text_14")
        self.stock_news_text_14.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_14.setWordWrap(True)
        self.stock_news_text_14.setOpenExternalLinks(False)
        self.stock_news_text_14.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_99.addWidget(self.stock_news_text_14)


        self.verticalLayout_97.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.stock_news_media_14 = QLabel(self.frame_50)
        self.stock_news_media_14.setObjectName(u"stock_news_media_14")
        self.stock_news_media_14.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_14.setWordWrap(True)

        self.horizontalLayout_40.addWidget(self.stock_news_media_14, 0, Qt.AlignBottom)


        self.verticalLayout_97.addWidget(self.frame_50, 0, Qt.AlignBottom)


        self.horizontalLayout_28.addWidget(self.frame_48)


        self.verticalLayout_61.addWidget(self.frame_23)

        self.frame_51 = QFrame(self.stock_analysis_news_frame_2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 300))
        self.frame_51.setStyleSheet(u"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(100, 100))
        self.frame_52.setMaximumSize(QSize(250, 280))
        self.frame_52.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_52.setFrameShape(QFrame.Box)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_52)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.stock_news_title_frame_15 = QFrame(self.frame_52)
        self.stock_news_title_frame_15.setObjectName(u"stock_news_title_frame_15")
        self.stock_news_title_frame_15.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.stock_news_title_frame_15)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.stock_news_title_15 = QLabel(self.stock_news_title_frame_15)
        self.stock_news_title_15.setObjectName(u"stock_news_title_15")
        self.stock_news_title_15.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_15.setWordWrap(True)

        self.verticalLayout_101.addWidget(self.stock_news_title_15)


        self.verticalLayout_100.addWidget(self.stock_news_title_frame_15)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy1.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy1)
        self.frame_53.setMinimumSize(QSize(0, 0))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_53)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.stock_news_text_15 = QLabel(self.frame_53)
        self.stock_news_text_15.setObjectName(u"stock_news_text_15")
        self.stock_news_text_15.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_15.setWordWrap(True)
        self.stock_news_text_15.setOpenExternalLinks(False)
        self.stock_news_text_15.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_102.addWidget(self.stock_news_text_15)


        self.verticalLayout_100.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.stock_news_media_15 = QLabel(self.frame_54)
        self.stock_news_media_15.setObjectName(u"stock_news_media_15")
        self.stock_news_media_15.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_15.setWordWrap(True)

        self.horizontalLayout_41.addWidget(self.stock_news_media_15, 0, Qt.AlignBottom)


        self.verticalLayout_100.addWidget(self.frame_54, 0, Qt.AlignBottom)


        self.horizontalLayout_30.addWidget(self.frame_52)

        self.frame_55 = QFrame(self.frame_51)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(100, 100))
        self.frame_55.setMaximumSize(QSize(250, 280))
        self.frame_55.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_55.setFrameShape(QFrame.Box)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_55)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.stock_news_title_frame_16 = QFrame(self.frame_55)
        self.stock_news_title_frame_16.setObjectName(u"stock_news_title_frame_16")
        self.stock_news_title_frame_16.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.stock_news_title_frame_16)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.stock_news_title_16 = QLabel(self.stock_news_title_frame_16)
        self.stock_news_title_16.setObjectName(u"stock_news_title_16")
        self.stock_news_title_16.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_16.setWordWrap(True)

        self.verticalLayout_104.addWidget(self.stock_news_title_16)


        self.verticalLayout_103.addWidget(self.stock_news_title_frame_16)

        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy1.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy1)
        self.frame_56.setMinimumSize(QSize(0, 0))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_56)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.stock_news_text_16 = QLabel(self.frame_56)
        self.stock_news_text_16.setObjectName(u"stock_news_text_16")
        self.stock_news_text_16.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_16.setWordWrap(True)
        self.stock_news_text_16.setOpenExternalLinks(False)
        self.stock_news_text_16.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_105.addWidget(self.stock_news_text_16)


        self.verticalLayout_103.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.stock_news_media_16 = QLabel(self.frame_57)
        self.stock_news_media_16.setObjectName(u"stock_news_media_16")
        self.stock_news_media_16.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_16.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.stock_news_media_16, 0, Qt.AlignBottom)


        self.verticalLayout_103.addWidget(self.frame_57, 0, Qt.AlignBottom)


        self.horizontalLayout_30.addWidget(self.frame_55)

        self.frame_58 = QFrame(self.frame_51)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(100, 100))
        self.frame_58.setMaximumSize(QSize(250, 280))
        self.frame_58.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_58.setFrameShape(QFrame.Box)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_58)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.stock_news_title_frame_17 = QFrame(self.frame_58)
        self.stock_news_title_frame_17.setObjectName(u"stock_news_title_frame_17")
        self.stock_news_title_frame_17.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.stock_news_title_frame_17)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.stock_news_title_17 = QLabel(self.stock_news_title_frame_17)
        self.stock_news_title_17.setObjectName(u"stock_news_title_17")
        self.stock_news_title_17.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_17.setWordWrap(True)

        self.verticalLayout_107.addWidget(self.stock_news_title_17)


        self.verticalLayout_106.addWidget(self.stock_news_title_frame_17)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy1.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy1)
        self.frame_59.setMinimumSize(QSize(0, 0))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_59)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.stock_news_text_17 = QLabel(self.frame_59)
        self.stock_news_text_17.setObjectName(u"stock_news_text_17")
        self.stock_news_text_17.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_17.setWordWrap(True)
        self.stock_news_text_17.setOpenExternalLinks(False)
        self.stock_news_text_17.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_108.addWidget(self.stock_news_text_17)


        self.verticalLayout_106.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.stock_news_media_17 = QLabel(self.frame_60)
        self.stock_news_media_17.setObjectName(u"stock_news_media_17")
        self.stock_news_media_17.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_17.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.stock_news_media_17, 0, Qt.AlignBottom)


        self.verticalLayout_106.addWidget(self.frame_60, 0, Qt.AlignBottom)


        self.horizontalLayout_30.addWidget(self.frame_58)


        self.verticalLayout_61.addWidget(self.frame_51)

        self.frame_61 = QFrame(self.stock_analysis_news_frame_2)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 300))
        self.frame_61.setStyleSheet(u"")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(100, 100))
        self.frame_62.setMaximumSize(QSize(250, 280))
        self.frame_62.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_62.setFrameShape(QFrame.Box)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_62)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.stock_news_title_frame_18 = QFrame(self.frame_62)
        self.stock_news_title_frame_18.setObjectName(u"stock_news_title_frame_18")
        self.stock_news_title_frame_18.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.stock_news_title_frame_18)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.stock_news_title_18 = QLabel(self.stock_news_title_frame_18)
        self.stock_news_title_18.setObjectName(u"stock_news_title_18")
        self.stock_news_title_18.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_18.setWordWrap(True)

        self.verticalLayout_110.addWidget(self.stock_news_title_18)


        self.verticalLayout_109.addWidget(self.stock_news_title_frame_18)

        self.frame_63 = QFrame(self.frame_62)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy1.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy1)
        self.frame_63.setMinimumSize(QSize(0, 0))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_63)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.stock_news_text_18 = QLabel(self.frame_63)
        self.stock_news_text_18.setObjectName(u"stock_news_text_18")
        self.stock_news_text_18.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_18.setWordWrap(True)
        self.stock_news_text_18.setOpenExternalLinks(False)
        self.stock_news_text_18.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_111.addWidget(self.stock_news_text_18)


        self.verticalLayout_109.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_62)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.stock_news_media_18 = QLabel(self.frame_64)
        self.stock_news_media_18.setObjectName(u"stock_news_media_18")
        self.stock_news_media_18.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_18.setWordWrap(True)

        self.horizontalLayout_45.addWidget(self.stock_news_media_18, 0, Qt.AlignBottom)


        self.verticalLayout_109.addWidget(self.frame_64, 0, Qt.AlignBottom)


        self.horizontalLayout_44.addWidget(self.frame_62)

        self.frame_65 = QFrame(self.frame_61)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(100, 100))
        self.frame_65.setMaximumSize(QSize(250, 280))
        self.frame_65.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_65.setFrameShape(QFrame.Box)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_65)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.stock_news_title_frame_19 = QFrame(self.frame_65)
        self.stock_news_title_frame_19.setObjectName(u"stock_news_title_frame_19")
        self.stock_news_title_frame_19.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.stock_news_title_frame_19)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.stock_news_title_19 = QLabel(self.stock_news_title_frame_19)
        self.stock_news_title_19.setObjectName(u"stock_news_title_19")
        self.stock_news_title_19.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_19.setWordWrap(True)

        self.verticalLayout_113.addWidget(self.stock_news_title_19)


        self.verticalLayout_112.addWidget(self.stock_news_title_frame_19)

        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy1.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy1)
        self.frame_66.setMinimumSize(QSize(0, 0))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_66)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.stock_news_text_19 = QLabel(self.frame_66)
        self.stock_news_text_19.setObjectName(u"stock_news_text_19")
        self.stock_news_text_19.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_19.setWordWrap(True)
        self.stock_news_text_19.setOpenExternalLinks(False)
        self.stock_news_text_19.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_114.addWidget(self.stock_news_text_19)


        self.verticalLayout_112.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.stock_news_media_19 = QLabel(self.frame_67)
        self.stock_news_media_19.setObjectName(u"stock_news_media_19")
        self.stock_news_media_19.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.stock_news_media_19.setWordWrap(True)

        self.horizontalLayout_46.addWidget(self.stock_news_media_19, 0, Qt.AlignBottom)


        self.verticalLayout_112.addWidget(self.frame_67, 0, Qt.AlignBottom)


        self.horizontalLayout_44.addWidget(self.frame_65)

        self.frame_68 = QFrame(self.frame_61)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(100, 100))
        self.frame_68.setMaximumSize(QSize(250, 280))
        self.frame_68.setStyleSheet(u"background-color: rgb(45, 50, 67);\n"
"")
        self.frame_68.setFrameShape(QFrame.Box)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_68)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.stock_news_title_frame_20 = QFrame(self.frame_68)
        self.stock_news_title_frame_20.setObjectName(u"stock_news_title_frame_20")
        self.stock_news_title_frame_20.setFrameShape(QFrame.StyledPanel)
        self.stock_news_title_frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.stock_news_title_frame_20)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.stock_news_title_20 = QLabel(self.stock_news_title_frame_20)
        self.stock_news_title_20.setObjectName(u"stock_news_title_20")
        self.stock_news_title_20.setStyleSheet(u"color:rgb(234, 234, 234);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.stock_news_title_20.setWordWrap(True)

        self.verticalLayout_116.addWidget(self.stock_news_title_20)


        self.verticalLayout_115.addWidget(self.stock_news_title_frame_20)

        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        sizePolicy1.setHeightForWidth(self.frame_69.sizePolicy().hasHeightForWidth())
        self.frame_69.setSizePolicy(sizePolicy1)
        self.frame_69.setMinimumSize(QSize(0, 0))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_69)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.stock_news_text_20 = QLabel(self.frame_69)
        self.stock_news_text_20.setObjectName(u"stock_news_text_20")
        self.stock_news_text_20.setStyleSheet(u"color:rgb(209, 209, 209);")
        self.stock_news_text_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stock_news_text_20.setWordWrap(True)
        self.stock_news_text_20.setOpenExternalLinks(False)
        self.stock_news_text_20.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_117.addWidget(self.stock_news_text_20)


        self.verticalLayout_115.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.stock_news_media_20 = QLabel(self.frame_70)
        self.stock_news_media_20.setObjectName(u"stock_news_media_20")
        self.stock_news_media_20.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.stock_news_media_20.setWordWrap(True)

        self.horizontalLayout_47.addWidget(self.stock_news_media_20, 0, Qt.AlignBottom)


        self.verticalLayout_115.addWidget(self.frame_70, 0, Qt.AlignBottom)


        self.horizontalLayout_44.addWidget(self.frame_68)


        self.verticalLayout_61.addWidget(self.frame_61)

        self.frame_71 = QFrame(self.stock_analysis_news_frame_2)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.pushButton_3 = QPushButton(self.frame_71)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.ForbiddenCursor))

        self.horizontalLayout_48.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.frame_71)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.ForbiddenCursor))

        self.horizontalLayout_48.addWidget(self.pushButton_4, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_71)


        self.verticalLayout_40.addWidget(self.stock_analysis_news_frame_2, 0, Qt.AlignHCenter)

        self.stock_analysis_stackedWidget.addWidget(self.stock_analysis_currency_page)

        self.verticalLayout_35.addWidget(self.stock_analysis_stackedWidget, 0, Qt.AlignHCenter)


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
        font6 = QFont()
        font6.setFamily(u"MS Outlook")
        font6.setBold(False)
        font6.setWeight(50)
        self.learning_pages_stackedWidget.setFont(font6)
        self.learn_start_page = QWidget()
        self.learn_start_page.setObjectName(u"learn_start_page")
        self.verticalLayout_15 = QVBoxLayout(self.learn_start_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.learn_start_page_frame = QFrame(self.learn_start_page)
        self.learn_start_page_frame.setObjectName(u"learn_start_page_frame")
        self.learn_start_page_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.learn_start_page_frame)
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
"")

        self.verticalLayout_41.addWidget(self.learn_start_page_title_label, 0, Qt.AlignHCenter)


        self.verticalLayout_44.addWidget(self.learn_start_page_title_frame)

        self.learn_start_page_content_frame_frame = QFrame(self.learn_start_page_frame)
        self.learn_start_page_content_frame_frame.setObjectName(u"learn_start_page_content_frame_frame")
        self.learn_start_page_content_frame_frame.setStyleSheet(u"")
        self.learn_start_page_content_frame_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_content_frame_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.learn_start_page_content_frame_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 250, -1, -1)
        self.learn_start_page_frame_title = QFrame(self.learn_start_page_content_frame_frame)
        self.learn_start_page_frame_title.setObjectName(u"learn_start_page_frame_title")
        self.learn_start_page_frame_title.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.learn_start_page_frame_title)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.what_do_you_wish_to_learn_label = QLabel(self.learn_start_page_frame_title)
        self.what_do_you_wish_to_learn_label.setObjectName(u"what_do_you_wish_to_learn_label")
        self.what_do_you_wish_to_learn_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_17.addWidget(self.what_do_you_wish_to_learn_label, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.learn_start_page_frame_title)

        self.learn_start_page_options_frame = QFrame(self.learn_start_page_content_frame_frame)
        self.learn_start_page_options_frame.setObjectName(u"learn_start_page_options_frame")
        self.learn_start_page_options_frame.setMinimumSize(QSize(400, 0))
        self.learn_start_page_options_frame.setMaximumSize(QSize(25000, 16777215))
        self.learn_start_page_options_frame.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")
        self.learn_start_page_options_frame.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_options_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.learn_start_page_options_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.stocks_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.stocks_button_learn.setObjectName(u"stocks_button_learn")
        self.stocks_button_learn.setMinimumSize(QSize(100, 40))
        self.stocks_button_learn.setMaximumSize(QSize(500, 40))
        self.stocks_button_learn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stocks_button_learn.setStyleSheet(u"")
        self.stocks_button_learn.setFlat(False)

        self.horizontalLayout_15.addWidget(self.stocks_button_learn)

        self.forex_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.forex_button_learn.setObjectName(u"forex_button_learn")
        self.forex_button_learn.setMinimumSize(QSize(100, 40))
        self.forex_button_learn.setMaximumSize(QSize(500, 40))
        self.forex_button_learn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forex_button_learn.setStyleSheet(u"")
        self.forex_button_learn.setFlat(False)

        self.horizontalLayout_15.addWidget(self.forex_button_learn)

        self.crypto_button_learn = QPushButton(self.learn_start_page_options_frame)
        self.crypto_button_learn.setObjectName(u"crypto_button_learn")
        self.crypto_button_learn.setMinimumSize(QSize(100, 40))
        self.crypto_button_learn.setMaximumSize(QSize(500, 40))
        self.crypto_button_learn.setCursor(QCursor(Qt.PointingHandCursor))
        self.crypto_button_learn.setStyleSheet(u"")
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
        self.stocks_page_scrollAreaWidget_frame.setGeometry(QRect(0, 0, 842, 3805))
        self.verticalLayout_19 = QVBoxLayout(self.stocks_page_scrollAreaWidget_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.stock_tutorial_all = QFrame(self.stocks_page_scrollAreaWidget_frame)
        self.stock_tutorial_all.setObjectName(u"stock_tutorial_all")
        self.stock_tutorial_all.setMinimumSize(QSize(0, 0))
        self.stock_tutorial_all.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stock_tutorial_all.setFrameShape(QFrame.StyledPanel)
        self.stock_tutorial_all.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.stock_tutorial_all)
        self.verticalLayout_51.setSpacing(17)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_74 = QFrame(self.stock_tutorial_all)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_74)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.learn_return_to_homepage_button = QPushButton(self.frame_74)
        self.learn_return_to_homepage_button.setObjectName(u"learn_return_to_homepage_button")
        self.learn_return_to_homepage_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.learn_return_to_homepage_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(39, 44, 59);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(43, 49, 65);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.learn_return_to_homepage_button.setIcon(icon12)
        self.learn_return_to_homepage_button.setIconSize(QSize(32, 32))
        self.learn_return_to_homepage_button.setFlat(True)

        self.verticalLayout_118.addWidget(self.learn_return_to_homepage_button, 0, Qt.AlignLeft)


        self.verticalLayout_51.addWidget(self.frame_74)

        self.label_22 = QLabel(self.stock_tutorial_all)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_51.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.stock_tutorial_all)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(745, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_4)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_78 = QFrame(self.frame_4)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"QPushButton{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.frame_78.setFrameShape(QFrame.Box)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_78)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.frame_80 = QFrame(self.frame_78)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_80)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(-1, -1, -1, 16)
        self.label_20 = QLabel(self.frame_80)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"")

        self.verticalLayout_158.addWidget(self.label_20)


        self.verticalLayout_149.addWidget(self.frame_80)

        self.pushButton_12 = QPushButton(self.frame_78)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton_12)

        self.pushButton = QPushButton(self.frame_78)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton)

        self.pushButton_11 = QPushButton(self.frame_78)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_78)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_78)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_78)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFlat(True)

        self.verticalLayout_149.addWidget(self.pushButton_8)


        self.verticalLayout_50.addWidget(self.frame_78, 0, Qt.AlignLeft)


        self.verticalLayout_51.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.stocks_tutorial_main_body = QFrame(self.stock_tutorial_all)
        self.stocks_tutorial_main_body.setObjectName(u"stocks_tutorial_main_body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stocks_tutorial_main_body.sizePolicy().hasHeightForWidth())
        self.stocks_tutorial_main_body.setSizePolicy(sizePolicy2)
        self.stocks_tutorial_main_body.setMinimumSize(QSize(750, 0))
        self.stocks_tutorial_main_body.setMaximumSize(QSize(16777215, 16777215))
        self.stocks_tutorial_main_body.setStyleSheet(u"background-color: rgb(26, 29, 39);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.stocks_tutorial_main_body.setFrameShape(QFrame.StyledPanel)
        self.stocks_tutorial_main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.stocks_tutorial_main_body)
        self.verticalLayout_48.setSpacing(50)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.wha_is_a_stock = QFrame(self.stocks_tutorial_main_body)
        self.wha_is_a_stock.setObjectName(u"wha_is_a_stock")
        self.wha_is_a_stock.setMinimumSize(QSize(0, 0))
        self.wha_is_a_stock.setFrameShape(QFrame.StyledPanel)
        self.wha_is_a_stock.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.wha_is_a_stock)
        self.verticalLayout_52.setSpacing(6)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, 9, -1, -1)
        self.label_3 = QLabel(self.wha_is_a_stock)
        self.label_3.setObjectName(u"label_3")
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(18)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(9)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_52.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.plainTextEdit = QPlainTextEdit(self.wha_is_a_stock)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(500, 464))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setTabStopWidth(80)
        self.plainTextEdit.setCursorWidth(1)
        self.plainTextEdit.setMaximumBlockCount(0)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_52.addWidget(self.plainTextEdit)


        self.verticalLayout_48.addWidget(self.wha_is_a_stock, 0, Qt.AlignHCenter)

        self.understanding_stocks = QFrame(self.stocks_tutorial_main_body)
        self.understanding_stocks.setObjectName(u"understanding_stocks")
        self.understanding_stocks.setFrameShape(QFrame.StyledPanel)
        self.understanding_stocks.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.understanding_stocks)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_6 = QLabel(self.understanding_stocks)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)
        self.label_6.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_49.addWidget(self.label_6)

        self.plainTextEdit_2 = QPlainTextEdit(self.understanding_stocks)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(500, 325))

        self.verticalLayout_49.addWidget(self.plainTextEdit_2)


        self.verticalLayout_48.addWidget(self.understanding_stocks, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.why_do_people_buy_stocks = QFrame(self.stocks_tutorial_main_body)
        self.why_do_people_buy_stocks.setObjectName(u"why_do_people_buy_stocks")
        self.why_do_people_buy_stocks.setMinimumSize(QSize(0, 0))
        self.why_do_people_buy_stocks.setFrameShape(QFrame.Box)
        self.why_do_people_buy_stocks.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.why_do_people_buy_stocks)
        self.verticalLayout_65.setSpacing(9)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(-1, 9, -1, -1)
        self.label_11 = QLabel(self.why_do_people_buy_stocks)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_65.addWidget(self.label_11)

        self.plainTextEdit_3 = QPlainTextEdit(self.why_do_people_buy_stocks)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(500, 650))

        self.verticalLayout_65.addWidget(self.plainTextEdit_3)


        self.verticalLayout_48.addWidget(self.why_do_people_buy_stocks, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.why_do_companies_issue_stocks = QFrame(self.stocks_tutorial_main_body)
        self.why_do_companies_issue_stocks.setObjectName(u"why_do_companies_issue_stocks")
        self.why_do_companies_issue_stocks.setFrameShape(QFrame.StyledPanel)
        self.why_do_companies_issue_stocks.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.why_do_companies_issue_stocks)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_14 = QLabel(self.why_do_companies_issue_stocks)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_66.addWidget(self.label_14)

        self.plainTextEdit_4 = QPlainTextEdit(self.why_do_companies_issue_stocks)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMinimumSize(QSize(500, 175))

        self.verticalLayout_66.addWidget(self.plainTextEdit_4)


        self.verticalLayout_48.addWidget(self.why_do_companies_issue_stocks, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.types_of_stock = QFrame(self.stocks_tutorial_main_body)
        self.types_of_stock.setObjectName(u"types_of_stock")
        self.types_of_stock.setFrameShape(QFrame.StyledPanel)
        self.types_of_stock.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.types_of_stock)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.label_9 = QLabel(self.types_of_stock)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_161.addWidget(self.label_9)

        self.plainTextEdit_5 = QPlainTextEdit(self.types_of_stock)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(500, 378))

        self.verticalLayout_161.addWidget(self.plainTextEdit_5)


        self.verticalLayout_48.addWidget(self.types_of_stock, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.market_capitalization = QFrame(self.stocks_tutorial_main_body)
        self.market_capitalization.setObjectName(u"market_capitalization")
        self.market_capitalization.setMinimumSize(QSize(0, 0))
        self.market_capitalization.setFrameShape(QFrame.StyledPanel)
        self.market_capitalization.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.market_capitalization)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(-1, 9, -1, -1)
        self.label_15 = QLabel(self.market_capitalization)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 75 18pt;")

        self.verticalLayout_67.addWidget(self.label_15)

        self.plainTextEdit_6 = QPlainTextEdit(self.market_capitalization)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setMinimumSize(QSize(500, 750))

        self.verticalLayout_67.addWidget(self.plainTextEdit_6)


        self.verticalLayout_48.addWidget(self.market_capitalization, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_51.addWidget(self.stocks_tutorial_main_body, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.stock_tutorial_all)

        self.stocks_tutorial_credits_frame = QFrame(self.stocks_page_scrollAreaWidget_frame)
        self.stocks_tutorial_credits_frame.setObjectName(u"stocks_tutorial_credits_frame")
        self.stocks_tutorial_credits_frame.setFrameShape(QFrame.StyledPanel)
        self.stocks_tutorial_credits_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.stocks_tutorial_credits_frame)

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
        self.forex_scrollAreaWidget_frame.setGeometry(QRect(0, 0, 302, 340))
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
"")

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
        self.simulator_start_page_title_frame_2.setStyleSheet(u"")
        self.simulator_start_page_title_frame_2.setFrameShape(QFrame.StyledPanel)
        self.simulator_start_page_title_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.simulator_start_page_title_frame_2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.simulator_start_page_content_label = QLabel(self.simulator_start_page_title_frame_2)
        self.simulator_start_page_content_label.setObjectName(u"simulator_start_page_content_label")
        self.simulator_start_page_content_label.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_43.addWidget(self.simulator_start_page_content_label, 0, Qt.AlignHCenter)


        self.verticalLayout_45.addWidget(self.simulator_start_page_title_frame_2)

        self.learn_start_page_options_frame_2 = QFrame(self.simulator_start_page_content_frame)
        self.learn_start_page_options_frame_2.setObjectName(u"learn_start_page_options_frame_2")
        self.learn_start_page_options_frame_2.setMinimumSize(QSize(400, 0))
        self.learn_start_page_options_frame_2.setMaximumSize(QSize(25000, 16777215))
        self.learn_start_page_options_frame_2.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")
        self.learn_start_page_options_frame_2.setFrameShape(QFrame.StyledPanel)
        self.learn_start_page_options_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.learn_start_page_options_frame_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stock_simulator_start_btn = QPushButton(self.learn_start_page_options_frame_2)
        self.stock_simulator_start_btn.setObjectName(u"stock_simulator_start_btn")
        self.stock_simulator_start_btn.setMinimumSize(QSize(100, 40))
        self.stock_simulator_start_btn.setMaximumSize(QSize(200, 40))
        self.stock_simulator_start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_start_btn.setStyleSheet(u"")
        self.stock_simulator_start_btn.setFlat(False)

        self.horizontalLayout_17.addWidget(self.stock_simulator_start_btn)


        self.verticalLayout_45.addWidget(self.learn_start_page_options_frame_2)


        self.verticalLayout_26.addWidget(self.simulator_start_page_content_frame)


        self.verticalLayout_25.addWidget(self.simulator_start_page_frame, 0, Qt.AlignTop)

        self.simulator_stacked_widget.addWidget(self.simulator_start_page)
        self.simulator_login_page = QWidget()
        self.simulator_login_page.setObjectName(u"simulator_login_page")
        self.verticalLayout_125 = QVBoxLayout(self.simulator_login_page)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.simulator_return_to_homepage_button = QPushButton(self.simulator_login_page)
        self.simulator_return_to_homepage_button.setObjectName(u"simulator_return_to_homepage_button")
        self.simulator_return_to_homepage_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulator_return_to_homepage_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(39, 44, 59);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(43, 49, 65);\n"
"}")
        self.simulator_return_to_homepage_button.setIcon(icon12)
        self.simulator_return_to_homepage_button.setIconSize(QSize(32, 32))
        self.simulator_return_to_homepage_button.setFlat(True)

        self.verticalLayout_125.addWidget(self.simulator_return_to_homepage_button, 0, Qt.AlignLeft)

        self.frame_81 = QFrame(self.simulator_login_page)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_81)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_82)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.pushButton_5 = QPushButton(self.frame_82)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon13)
        self.pushButton_5.setIconSize(QSize(64, 64))
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setFlat(True)

        self.verticalLayout_127.addWidget(self.pushButton_5)

        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_85)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 3, 0, 6)
        self.simulator_login_to_username_entry = QLineEdit(self.frame_85)
        self.simulator_login_to_username_entry.setObjectName(u"simulator_login_to_username_entry")
        self.simulator_login_to_username_entry.setMinimumSize(QSize(170, 0))
        self.simulator_login_to_username_entry.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.simulator_login_to_username_entry.setMaxLength(20)
        self.simulator_login_to_username_entry.setAlignment(Qt.AlignCenter)

        self.verticalLayout_128.addWidget(self.simulator_login_to_username_entry, 0, Qt.AlignHCenter)


        self.verticalLayout_127.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_82)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_86)
        self.verticalLayout_129.setSpacing(13)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 16, 0, 0)
        self.simulator_continue_to_sim_btn = QPushButton(self.frame_86)
        self.simulator_continue_to_sim_btn.setObjectName(u"simulator_continue_to_sim_btn")
        sizePolicy2.setHeightForWidth(self.simulator_continue_to_sim_btn.sizePolicy().hasHeightForWidth())
        self.simulator_continue_to_sim_btn.setSizePolicy(sizePolicy2)
        self.simulator_continue_to_sim_btn.setMinimumSize(QSize(115, 30))
        self.simulator_continue_to_sim_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulator_continue_to_sim_btn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")

        self.verticalLayout_129.addWidget(self.simulator_continue_to_sim_btn, 0, Qt.AlignHCenter)

        self.simulator_create_new_user_btn = QPushButton(self.frame_86)
        self.simulator_create_new_user_btn.setObjectName(u"simulator_create_new_user_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.simulator_create_new_user_btn.sizePolicy().hasHeightForWidth())
        self.simulator_create_new_user_btn.setSizePolicy(sizePolicy3)
        self.simulator_create_new_user_btn.setMinimumSize(QSize(230, 20))
        self.simulator_create_new_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulator_create_new_user_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover {\n"
"	border-radius:10px;\n"
"	background-color: rgb(41, 47, 62);\n"
"\n"
"}\n"
"QPushButton::pressed {\n"
"	border-radius:10px;\n"
"	background-color: rgb(53, 59, 79);	\n"
"}\n"
"")
        self.simulator_create_new_user_btn.setFlat(True)

        self.verticalLayout_129.addWidget(self.simulator_create_new_user_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_127.addWidget(self.frame_86)


        self.verticalLayout_123.addWidget(self.frame_82, 0, Qt.AlignHCenter)


        self.verticalLayout_125.addWidget(self.frame_81, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.simulator_stacked_widget.addWidget(self.simulator_login_page)
        self.simulator_register_page = QWidget()
        self.simulator_register_page.setObjectName(u"simulator_register_page")
        self.verticalLayout_126 = QVBoxLayout(self.simulator_register_page)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.simulator_return_to_homepage_button_2 = QPushButton(self.simulator_register_page)
        self.simulator_return_to_homepage_button_2.setObjectName(u"simulator_return_to_homepage_button_2")
        self.simulator_return_to_homepage_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulator_return_to_homepage_button_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(39, 44, 59);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(43, 49, 65);\n"
"}")
        self.simulator_return_to_homepage_button_2.setIcon(icon12)
        self.simulator_return_to_homepage_button_2.setIconSize(QSize(32, 32))
        self.simulator_return_to_homepage_button_2.setFlat(True)

        self.verticalLayout_126.addWidget(self.simulator_return_to_homepage_button_2, 0, Qt.AlignLeft)

        self.frame_83 = QFrame(self.simulator_register_page)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_83)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_84)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.frame_87 = QFrame(self.frame_84)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_87)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 3, 0, 6)
        self.simulator_new_username_entry = QLineEdit(self.frame_87)
        self.simulator_new_username_entry.setObjectName(u"simulator_new_username_entry")
        self.simulator_new_username_entry.setMinimumSize(QSize(170, 0))
        self.simulator_new_username_entry.setStyleSheet(u"background-color: rgb(0, 0, 0, 0 );\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 115, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.simulator_new_username_entry.setMaxLength(20)
        self.simulator_new_username_entry.setAlignment(Qt.AlignCenter)

        self.verticalLayout_131.addWidget(self.simulator_new_username_entry, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_87, 0, Qt.AlignBottom)

        self.frame_88 = QFrame(self.frame_84)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_88)
        self.verticalLayout_132.setSpacing(13)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 16, 0, 0)
        self.simulator_confirm_new_username_entry = QPushButton(self.frame_88)
        self.simulator_confirm_new_username_entry.setObjectName(u"simulator_confirm_new_username_entry")
        self.simulator_confirm_new_username_entry.setMinimumSize(QSize(115, 30))
        self.simulator_confirm_new_username_entry.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulator_confirm_new_username_entry.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(32, 36, 48);\n"
"}")

        self.verticalLayout_132.addWidget(self.simulator_confirm_new_username_entry, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_88, 0, Qt.AlignTop)


        self.verticalLayout_124.addWidget(self.frame_84)


        self.verticalLayout_126.addWidget(self.frame_83, 0, Qt.AlignHCenter)

        self.simulator_stacked_widget.addWidget(self.simulator_register_page)
        self.stock_simulator_page = QWidget()
        self.stock_simulator_page.setObjectName(u"stock_simulator_page")
        self.verticalLayout_27 = QVBoxLayout(self.stock_simulator_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.stock_simulator_scrollArea = QScrollArea(self.stock_simulator_page)
        self.stock_simulator_scrollArea.setObjectName(u"stock_simulator_scrollArea")
        sizePolicy.setHeightForWidth(self.stock_simulator_scrollArea.sizePolicy().hasHeightForWidth())
        self.stock_simulator_scrollArea.setSizePolicy(sizePolicy)
        self.stock_simulator_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stock_simulator_scrollArea.setWidgetResizable(True)
        self.stock_simulator_scroll_area_frame = QWidget()
        self.stock_simulator_scroll_area_frame.setObjectName(u"stock_simulator_scroll_area_frame")
        self.stock_simulator_scroll_area_frame.setGeometry(QRect(0, 0, 859, 700))
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

        self.verticalLayout_29.addWidget(self.stock_simulator_title, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.stock_simulator_header)

        self.stock_simulator_main_body = QFrame(self.stock_simulator_scroll_area_frame)
        self.stock_simulator_main_body.setObjectName(u"stock_simulator_main_body")
        sizePolicy2.setHeightForWidth(self.stock_simulator_main_body.sizePolicy().hasHeightForWidth())
        self.stock_simulator_main_body.setSizePolicy(sizePolicy2)
        self.stock_simulator_main_body.setMinimumSize(QSize(0, 0))
        self.stock_simulator_main_body.setMaximumSize(QSize(2020, 16777215))
        self.stock_simulator_main_body.setLayoutDirection(Qt.LeftToRight)
        self.stock_simulator_main_body.setAutoFillBackground(False)
        self.stock_simulator_main_body.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.stock_simulator_main_body)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.tabWidget = QTabWidget(self.stock_simulator_main_body)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(1430, 16777215))
        self.tabWidget.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(42, 44, 50);\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.Portfolio = QWidget()
        self.Portfolio.setObjectName(u"Portfolio")
        self.verticalLayout_32 = QVBoxLayout(self.Portfolio)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.scrollArea = QScrollArea(self.Portfolio)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(42, 44, 50);\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 797, 553))
        self.verticalLayout_121 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_9)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_156.addWidget(self.label_18)


        self.verticalLayout_121.addWidget(self.frame_9)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font8 = QFont()
        font8.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setFamily(u"MS Shell Dlg 2")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.tableWidget.setFont(font9)
        self.tableWidget.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(42, 44, 50);\n"
"\n"
"\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_26.addWidget(self.tableWidget)

        self.frame_75 = QFrame(self.frame)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"background-color: rgb(42, 44, 50);\n"
"")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_75)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(-1, 0, -1, -1)
        self.frame_79 = QFrame(self.frame_75)
        self.frame_79.setObjectName(u"frame_79")
        sizePolicy2.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy2)
        self.frame_79.setStyleSheet(u"background-color: rgb(42, 44, 50);\n"
"")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_79)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(9, 0, 9, -1)
        self.frame_77 = QFrame(self.frame_79)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"background-color: rgb(37, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.frame_77.setFrameShape(QFrame.Box)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_77)
        self.verticalLayout_119.setSpacing(3)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(10, 5, 10, 5)
        self.simulator_user_icon_btn = QPushButton(self.frame_77)
        self.simulator_user_icon_btn.setObjectName(u"simulator_user_icon_btn")
        self.simulator_user_icon_btn.setIcon(icon13)
        self.simulator_user_icon_btn.setIconSize(QSize(64, 64))
        self.simulator_user_icon_btn.setAutoDefault(True)
        self.simulator_user_icon_btn.setFlat(True)

        self.verticalLayout_119.addWidget(self.simulator_user_icon_btn)

        self.stock_simulator_username_label = QLabel(self.frame_77)
        self.stock_simulator_username_label.setObjectName(u"stock_simulator_username_label")
        self.stock_simulator_username_label.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_119.addWidget(self.stock_simulator_username_label, 0, Qt.AlignHCenter)


        self.verticalLayout_157.addWidget(self.frame_77, 0, Qt.AlignTop)


        self.verticalLayout_122.addWidget(self.frame_79)

        self.frame_110 = QFrame(self.frame_75)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setStyleSheet(u"background-color: rgb(37, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.frame_110.setFrameShape(QFrame.Box)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.frame_110)
        self.verticalLayout_151.setSpacing(14)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.frame_115 = QFrame(self.frame_110)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(53, 56, 63);")
        self.frame_115.setFrameShape(QFrame.Box)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_115)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_27 = QLabel(self.frame_115)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout_12.addWidget(self.label_27, 0, 0, 1, 1, Qt.AlignHCenter)

        self.stock_simulator_account_value_label = QLabel(self.frame_115)
        self.stock_simulator_account_value_label.setObjectName(u"stock_simulator_account_value_label")
        self.stock_simulator_account_value_label.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout_12.addWidget(self.stock_simulator_account_value_label, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_151.addWidget(self.frame_115)

        self.frame_116 = QFrame(self.frame_110)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(53, 56, 63);")
        self.frame_116.setFrameShape(QFrame.Box)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_116)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_33 = QLabel(self.frame_116)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout_13.addWidget(self.label_33, 0, 0, 1, 1, Qt.AlignHCenter)

        self.stock_simulator_cash_amount_label = QLabel(self.frame_116)
        self.stock_simulator_cash_amount_label.setObjectName(u"stock_simulator_cash_amount_label")
        self.stock_simulator_cash_amount_label.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout_13.addWidget(self.stock_simulator_cash_amount_label, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_151.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_110)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(53, 56, 63);")
        self.frame_117.setFrameShape(QFrame.Box)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_117)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.label_34 = QLabel(self.frame_117)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_154.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.stock_simulator_gainloss_label = QLabel(self.frame_117)
        self.stock_simulator_gainloss_label.setObjectName(u"stock_simulator_gainloss_label")
        self.stock_simulator_gainloss_label.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_154.addWidget(self.stock_simulator_gainloss_label, 0, Qt.AlignHCenter)


        self.verticalLayout_151.addWidget(self.frame_117)


        self.verticalLayout_122.addWidget(self.frame_110)

        self.frame_118 = QFrame(self.frame_75)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setStyleSheet(u"#stock_simulator_logout_btn{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font:14pt \"MS Shell Dlg 2\";\n"
"}\n"
"#stock_simulator_logout_btn::hover{\n"
"	background-color: rgb(59, 62, 70);\n"
"}\n"
"#stock_simulator_logout_btn::pressed{\n"
"	border:2px solid rgb(42, 44, 50);\n"
"	background-color: rgb(70, 73, 83);\n"
"}")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_118)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.stock_simulator_logout_btn = QPushButton(self.frame_118)
        self.stock_simulator_logout_btn.setObjectName(u"stock_simulator_logout_btn")
        self.stock_simulator_logout_btn.setMinimumSize(QSize(130, 41))
        self.stock_simulator_logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stock_simulator_logout_btn.setIcon(icon14)
        self.stock_simulator_logout_btn.setIconSize(QSize(32, 32))
        self.stock_simulator_logout_btn.setFlat(True)

        self.verticalLayout_155.addWidget(self.stock_simulator_logout_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_122.addWidget(self.frame_118)


        self.horizontalLayout_26.addWidget(self.frame_75, 0, Qt.AlignTop)


        self.verticalLayout_121.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_32.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.Portfolio, "")
        self.Trade = QWidget()
        self.Trade.setObjectName(u"Trade")
        self.verticalLayout_133 = QVBoxLayout(self.Trade)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.stock_sim_trade_stackedWidget = QStackedWidget(self.Trade)
        self.stock_sim_trade_stackedWidget.setObjectName(u"stock_sim_trade_stackedWidget")
        self.stock_simulator_trade_page_tab = QWidget()
        self.stock_simulator_trade_page_tab.setObjectName(u"stock_simulator_trade_page_tab")
        self.verticalLayout_31 = QVBoxLayout(self.stock_simulator_trade_page_tab)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_91 = QFrame(self.stock_simulator_trade_page_tab)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_91)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.stock_simulator_order_details_title = QLabel(self.frame_91)
        self.stock_simulator_order_details_title.setObjectName(u"stock_simulator_order_details_title")
        self.stock_simulator_order_details_title.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";")

        self.verticalLayout_120.addWidget(self.stock_simulator_order_details_title)


        self.verticalLayout_31.addWidget(self.frame_91)

        self.line = QFrame(self.stock_simulator_trade_page_tab)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(750, 0))
        self.line.setMaximumSize(QSize(16777215, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line, 0, Qt.AlignLeft)

        self.frame_97 = QFrame(self.stock_simulator_trade_page_tab)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(0, 0))
        self.frame_97.setSizeIncrement(QSize(0, 0))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 10, -1, -1)
        self.stock_simulator_order_details_data_frame = QFrame(self.frame_97)
        self.stock_simulator_order_details_data_frame.setObjectName(u"stock_simulator_order_details_data_frame")
        self.stock_simulator_order_details_data_frame.setStyleSheet(u"QLabel{\n"
"	font: 18pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(64, 67, 76);\n"
"border:none;\n"
"border-radius:5px;\n"
"border:2px solid rgba(105, 115, 132, 255);\n"
"color: rgb(201, 210, 238);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(64, 67, 76);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:5px;\n"
"border:2px solid rgba(105, 115, 132, 255);\n"
"color: rgb(201, 210, 238);\n"
"}\n"
"")
        self.stock_simulator_order_details_data_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_simulator_order_details_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.stock_simulator_order_details_data_frame)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.frame_94 = QFrame(self.stock_simulator_order_details_data_frame)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_94)
        self.verticalLayout_135.setSpacing(12)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(-1, -1, 9, -1)
        self.stock_simulator_stock_ticker_label = QLabel(self.frame_94)
        self.stock_simulator_stock_ticker_label.setObjectName(u"stock_simulator_stock_ticker_label")

        self.verticalLayout_135.addWidget(self.stock_simulator_stock_ticker_label)

        self.stock_simulator_stock_ticker_entry = QLineEdit(self.frame_94)
        self.stock_simulator_stock_ticker_entry.setObjectName(u"stock_simulator_stock_ticker_entry")
        self.stock_simulator_stock_ticker_entry.setMinimumSize(QSize(500, 30))
        self.stock_simulator_stock_ticker_entry.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_stock_ticker_entry.setStyleSheet(u"")

        self.verticalLayout_135.addWidget(self.stock_simulator_stock_ticker_entry)


        self.verticalLayout_134.addWidget(self.frame_94)

        self.frame_93 = QFrame(self.stock_simulator_order_details_data_frame)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_93)
        self.verticalLayout_140.setSpacing(12)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.stock_simulator_transaction_label = QLabel(self.frame_93)
        self.stock_simulator_transaction_label.setObjectName(u"stock_simulator_transaction_label")

        self.verticalLayout_140.addWidget(self.stock_simulator_transaction_label)

        self.stock_simulator_transaction_type_combobox = QComboBox(self.frame_93)
        self.stock_simulator_transaction_type_combobox.addItem("")
        self.stock_simulator_transaction_type_combobox.addItem("")
        self.stock_simulator_transaction_type_combobox.setObjectName(u"stock_simulator_transaction_type_combobox")
        self.stock_simulator_transaction_type_combobox.setMinimumSize(QSize(500, 30))
        self.stock_simulator_transaction_type_combobox.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_transaction_type_combobox.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.stock_simulator_transaction_type_combobox)


        self.verticalLayout_134.addWidget(self.frame_93)

        self.frame_96 = QFrame(self.stock_simulator_order_details_data_frame)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_96)
        self.verticalLayout_141.setSpacing(12)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.stock_simulator_quantity_label = QLabel(self.frame_96)
        self.stock_simulator_quantity_label.setObjectName(u"stock_simulator_quantity_label")

        self.verticalLayout_141.addWidget(self.stock_simulator_quantity_label)

        self.stock_simulator_quantity_entry = QLineEdit(self.frame_96)
        self.stock_simulator_quantity_entry.setObjectName(u"stock_simulator_quantity_entry")
        self.stock_simulator_quantity_entry.setMinimumSize(QSize(500, 30))
        self.stock_simulator_quantity_entry.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_quantity_entry.setStyleSheet(u"")

        self.verticalLayout_141.addWidget(self.stock_simulator_quantity_entry)


        self.verticalLayout_134.addWidget(self.frame_96)


        self.horizontalLayout_21.addWidget(self.stock_simulator_order_details_data_frame)

        self.frame_95 = QFrame(self.frame_97)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(0, 0))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_95)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(-1, 57, -1, -1)
        self.stock_simulator_symbol_lookup_button = QPushButton(self.frame_95)
        self.stock_simulator_symbol_lookup_button.setObjectName(u"stock_simulator_symbol_lookup_button")
        sizePolicy2.setHeightForWidth(self.stock_simulator_symbol_lookup_button.sizePolicy().hasHeightForWidth())
        self.stock_simulator_symbol_lookup_button.setSizePolicy(sizePolicy2)
        self.stock_simulator_symbol_lookup_button.setMinimumSize(QSize(150, 35))
        self.stock_simulator_symbol_lookup_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_symbol_lookup_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover {\n"
"	border-radius:4px;\n"
"	background-color: rgb(55, 58, 66);\n"
"}\n"
"QPushButton::pressed {\n"
"	border-radius:4px;\n"
"	background-color: rgb(65, 68, 77);\n"
"}")
        self.stock_simulator_symbol_lookup_button.setIcon(icon10)
        self.stock_simulator_symbol_lookup_button.setFlat(True)

        self.verticalLayout_139.addWidget(self.stock_simulator_symbol_lookup_button)


        self.horizontalLayout_21.addWidget(self.frame_95, 0, Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.frame_97, 0, Qt.AlignLeft)

        self.line_2 = QFrame(self.stock_simulator_trade_page_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(750, 0))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_2, 0, Qt.AlignLeft)

        self.frame_76 = QFrame(self.stock_simulator_trade_page_tab)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(42, 44, 50);\n"
"}")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_16.setSpacing(115)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(27, 17, -1, -1)
        self.stock_simulator_purchase_button_2 = QPushButton(self.frame_76)
        self.stock_simulator_purchase_button_2.setObjectName(u"stock_simulator_purchase_button_2")
        self.stock_simulator_purchase_button_2.setMinimumSize(QSize(200, 30))
        self.stock_simulator_purchase_button_2.setMaximumSize(QSize(400, 16777215))
        self.stock_simulator_purchase_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_purchase_button_2.setStyleSheet(u"")
        self.stock_simulator_purchase_button_2.setFlat(False)

        self.horizontalLayout_16.addWidget(self.stock_simulator_purchase_button_2)

        self.stock_simulator_purchase_button = QPushButton(self.frame_76)
        self.stock_simulator_purchase_button.setObjectName(u"stock_simulator_purchase_button")
        self.stock_simulator_purchase_button.setMinimumSize(QSize(200, 30))
        self.stock_simulator_purchase_button.setMaximumSize(QSize(400, 16777215))
        self.stock_simulator_purchase_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_purchase_button.setStyleSheet(u"")
        self.stock_simulator_purchase_button.setFlat(False)

        self.horizontalLayout_16.addWidget(self.stock_simulator_purchase_button)


        self.verticalLayout_31.addWidget(self.frame_76, 0, Qt.AlignLeft)

        self.stock_sim_trade_stackedWidget.addWidget(self.stock_simulator_trade_page_tab)
        self.stock_simulator_confirm_transaction_page = QWidget()
        self.stock_simulator_confirm_transaction_page.setObjectName(u"stock_simulator_confirm_transaction_page")
        self.verticalLayout_145 = QVBoxLayout(self.stock_simulator_confirm_transaction_page)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.frame_107 = QFrame(self.stock_simulator_confirm_transaction_page)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_107)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.frame_98 = QFrame(self.frame_107)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMaximumSize(QSize(470, 16777215))
        self.frame_98.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 85, 97);\n"
"border-radius:10px;\n"
"")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_98)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_17 = QLabel(self.frame_99)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_49.addWidget(self.label_17)

        self.header_right_frame_2 = QFrame(self.frame_99)
        self.header_right_frame_2.setObjectName(u"header_right_frame_2")
        self.header_right_frame_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(60, 88, 125);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(71, 105, 149);\n"
"}\n"
"")
        self.header_right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.header_right_frame_2)
        self.horizontalLayout_50.setSpacing(10)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_49.addWidget(self.header_right_frame_2, 0, Qt.AlignRight)


        self.verticalLayout_142.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_100)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.stock_name = QLabel(self.frame_100)
        self.stock_name.setObjectName(u"stock_name")
        self.stock_name.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_143.addWidget(self.stock_name, 0, Qt.AlignHCenter)


        self.verticalLayout_142.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_98)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_101)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.frame_102 = QFrame(self.frame_101)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_19 = QLabel(self.frame_102)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_51.addWidget(self.label_19)

        self.price_label = QLabel(self.frame_102)
        self.price_label.setObjectName(u"price_label")

        self.horizontalLayout_51.addWidget(self.price_label)


        self.verticalLayout_144.addWidget(self.frame_102)

        self.line_3 = QFrame(self.frame_101)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_144.addWidget(self.line_3)

        self.frame_103 = QFrame(self.frame_101)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_21 = QLabel(self.frame_103)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_52.addWidget(self.label_21)

        self.quantity_label = QLabel(self.frame_103)
        self.quantity_label.setObjectName(u"quantity_label")

        self.horizontalLayout_52.addWidget(self.quantity_label)


        self.verticalLayout_144.addWidget(self.frame_103)

        self.line_8 = QFrame(self.frame_101)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_144.addWidget(self.line_8)

        self.frame_104 = QFrame(self.frame_101)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_23 = QLabel(self.frame_104)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_53.addWidget(self.label_23)

        self.total_spread_label = QLabel(self.frame_104)
        self.total_spread_label.setObjectName(u"total_spread_label")

        self.horizontalLayout_53.addWidget(self.total_spread_label)


        self.verticalLayout_144.addWidget(self.frame_104)

        self.line_9 = QFrame(self.frame_101)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_144.addWidget(self.line_9)

        self.line_10 = QFrame(self.frame_101)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_144.addWidget(self.line_10)

        self.frame_105 = QFrame(self.frame_101)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.total_cost_label = QLabel(self.frame_105)
        self.total_cost_label.setObjectName(u"total_cost_label")

        self.horizontalLayout_54.addWidget(self.total_cost_label)

        self.label_24 = QLabel(self.frame_105)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_54.addWidget(self.label_24)


        self.verticalLayout_144.addWidget(self.frame_105)


        self.verticalLayout_142.addWidget(self.frame_101)

        self.frame_106 = QFrame(self.frame_98)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(106, 156, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(80, 119, 167);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(47, 71, 99);\n"
"	border:2px solid rgb(42, 44, 50);\n"
"}")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_55.setSpacing(115)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(27, 17, -1, -1)
        self.stock_simulator_purchase_camcel_btn = QPushButton(self.frame_106)
        self.stock_simulator_purchase_camcel_btn.setObjectName(u"stock_simulator_purchase_camcel_btn")
        self.stock_simulator_purchase_camcel_btn.setMinimumSize(QSize(150, 30))
        self.stock_simulator_purchase_camcel_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_purchase_camcel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_purchase_camcel_btn.setStyleSheet(u"")
        self.stock_simulator_purchase_camcel_btn.setFlat(False)

        self.horizontalLayout_55.addWidget(self.stock_simulator_purchase_camcel_btn)

        self.stock_simulator_purchase_confirm_btn = QPushButton(self.frame_106)
        self.stock_simulator_purchase_confirm_btn.setObjectName(u"stock_simulator_purchase_confirm_btn")
        self.stock_simulator_purchase_confirm_btn.setMinimumSize(QSize(150, 30))
        self.stock_simulator_purchase_confirm_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_purchase_confirm_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_purchase_confirm_btn.setStyleSheet(u"")
        self.stock_simulator_purchase_confirm_btn.setFlat(False)

        self.horizontalLayout_55.addWidget(self.stock_simulator_purchase_confirm_btn)


        self.verticalLayout_142.addWidget(self.frame_106, 0, Qt.AlignHCenter)


        self.verticalLayout_146.addWidget(self.frame_98, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_145.addWidget(self.frame_107)

        self.stock_sim_trade_stackedWidget.addWidget(self.stock_simulator_confirm_transaction_page)

        self.verticalLayout_133.addWidget(self.stock_sim_trade_stackedWidget, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.Trade, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_147 = QVBoxLayout(self.tab)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.frame_108 = QFrame(self.tab)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_108)
        self.verticalLayout_148.setSpacing(31)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.frame_109 = QFrame(self.frame_108)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(600, 0))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_109)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.label_26 = QLabel(self.frame_109)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.verticalLayout_152.addWidget(self.label_26)

        self.line_11 = QFrame(self.frame_109)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_152.addWidget(self.line_11)

        self.frame_111 = QFrame(self.frame_109)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_111)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(115)
        self.gridLayout_4.setVerticalSpacing(40)
        self.gridLayout_4.setContentsMargins(-1, 30, -1, 30)
        self.stock_simulator_stocks_owned_label = QLabel(self.frame_111)
        self.stock_simulator_stocks_owned_label.setObjectName(u"stock_simulator_stocks_owned_label")

        self.gridLayout_4.addWidget(self.stock_simulator_stocks_owned_label, 1, 1, 1, 1)

        self.stock_simulator_username_label_2 = QLabel(self.frame_111)
        self.stock_simulator_username_label_2.setObjectName(u"stock_simulator_username_label_2")

        self.gridLayout_4.addWidget(self.stock_simulator_username_label_2, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_111)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_28 = QLabel(self.frame_111)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 0, 0, 1, 1)


        self.verticalLayout_152.addWidget(self.frame_111)


        self.verticalLayout_148.addWidget(self.frame_109)

        self.frame_112 = QFrame(self.frame_108)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(345, 0))
        self.frame_112.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"font:14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#stock_simulator_delete_account_btn::hover{\n"
"background-color: rgb(203, 0, 0);\n"
"}\n"
"#stock_simulator_delete_account_btn::pressed{\n"
"	border:2px solid rgb(42, 44, 50);\n"
"	background-color: rgb(158, 0, 0);\n"
"}\n"
"\n"
"#stock_simulator_logout_btn::hover{\n"
"	background-color: rgb(59, 62, 70);\n"
"}\n"
"#stock_simulator_logout_btn::pressed{\n"
"	border:2px solid rgb(42, 44, 50);\n"
"	background-color: rgb(70, 73, 83);\n"
"}")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_112)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.label_32 = QLabel(self.frame_112)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.verticalLayout_153.addWidget(self.label_32)

        self.line_12 = QFrame(self.frame_112)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_153.addWidget(self.line_12)

        self.frame_113 = QFrame(self.frame_112)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setStyleSheet(u"")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_113)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.stock_simulator_delete_account_btn = QPushButton(self.frame_113)
        self.stock_simulator_delete_account_btn.setObjectName(u"stock_simulator_delete_account_btn")
        self.stock_simulator_delete_account_btn.setMinimumSize(QSize(225, 40))
        self.stock_simulator_delete_account_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stock_simulator_delete_account_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stock_simulator_delete_account_btn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/user-x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stock_simulator_delete_account_btn.setIcon(icon15)
        self.stock_simulator_delete_account_btn.setIconSize(QSize(32, 32))
        self.stock_simulator_delete_account_btn.setFlat(True)

        self.verticalLayout_150.addWidget(self.stock_simulator_delete_account_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_153.addWidget(self.frame_113)


        self.verticalLayout_148.addWidget(self.frame_112)


        self.verticalLayout_147.addWidget(self.frame_108, 0, Qt.AlignLeft|Qt.AlignTop)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_30.addWidget(self.tabWidget)


        self.verticalLayout_28.addWidget(self.stock_simulator_main_body)

        self.stock_simulator_scrollArea.setWidget(self.stock_simulator_scroll_area_frame)

        self.verticalLayout_27.addWidget(self.stock_simulator_scrollArea)

        self.simulator_stacked_widget.addWidget(self.stock_simulator_page)

        self.verticalLayout_24.addWidget(self.simulator_stacked_widget)

        self.stacked_menu_pages.addWidget(self.trade)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_7 = QVBoxLayout(self.settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_114 = QFrame(self.settings)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_114)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.scrollArea_2 = QScrollArea(self.frame_114)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 857, 698))
        self.verticalLayout_159 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.settings_stackedWidget = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.settings_stackedWidget.setObjectName(u"settings_stackedWidget")
        self.settings_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.settings_main = QWidget()
        self.settings_main.setObjectName(u"settings_main")
        self.verticalLayout_53 = QVBoxLayout(self.settings_main)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_131 = QFrame(self.settings_main)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"\n"
"QLineEdit{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(64, 67, 76);\n"
"border:none;\n"
"border-radius:5px;\n"
"border:2px solid rgba(105, 115, 132, 255);\n"
"color: rgb(201, 210, 238);\n"
"}\n"
"\n"
"QSpinBox{\n"
"background-color: rgb(64, 67, 76);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:5px;\n"
"border:2px solid rgba(105, 115, 132, 255);\n"
"color: rgb(201, 210, 238);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(64, 67, 76);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:5px;\n"
"border:2px solid rgba(105, 115, 132, 255);\n"
"color: rgb(201, 210, 238);\n"
"}\n"
"")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_131)
        self.verticalLayout_167.setSpacing(0)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.frame_131)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(0, 0))
        self.frame_128.setMaximumSize(QSize(16777215, 16777215))
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 28)
        self.label_31 = QLabel(self.frame_128)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"")

        self.horizontalLayout_18.addWidget(self.label_31, 0, Qt.AlignHCenter)


        self.verticalLayout_167.addWidget(self.frame_128)

        self.frame_120 = QFrame(self.frame_131)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_120)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(-1, 28, -1, -1)
        self.frame_124 = QFrame(self.frame_120)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMaximumSize(QSize(16777215, 50))
        self.frame_124.setSizeIncrement(QSize(0, 0))
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(15, 9, 13, 8)
        self.label_40 = QLabel(self.frame_124)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(35, 16777215))
        self.label_40.setPixmap(QPixmap(u":/icons/icons/activity.svg"))

        self.horizontalLayout_57.addWidget(self.label_40)

        self.label_37 = QLabel(self.frame_124)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 50))
        self.label_37.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_57.addWidget(self.label_37)


        self.verticalLayout_162.addWidget(self.frame_124)

        self.line_14 = QFrame(self.frame_120)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_162.addWidget(self.line_14)

        self.frame_125 = QFrame(self.frame_120)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_125)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(36)
        self.gridLayout_7.setVerticalSpacing(24)
        self.label_38 = QLabel(self.frame_125)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setToolTipDuration(0)
        self.label_38.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.frame_125)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_7.addWidget(self.label_39, 1, 0, 1, 1)

        self.settings_news_visible_checkBox = QCheckBox(self.frame_125)
        self.settings_news_visible_checkBox.setObjectName(u"settings_news_visible_checkBox")
        self.settings_news_visible_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_news_visible_checkBox.setCheckable(True)
        self.settings_news_visible_checkBox.setChecked(True)
        self.settings_news_visible_checkBox.setTristate(False)

        self.gridLayout_7.addWidget(self.settings_news_visible_checkBox, 1, 1, 1, 1)

        self.settings_extra_info_checkBox = QCheckBox(self.frame_125)
        self.settings_extra_info_checkBox.setObjectName(u"settings_extra_info_checkBox")
        self.settings_extra_info_checkBox.setChecked(True)

        self.gridLayout_7.addWidget(self.settings_extra_info_checkBox, 0, 1, 1, 1)


        self.verticalLayout_162.addWidget(self.frame_125, 0, Qt.AlignLeft)

        self.line_16 = QFrame(self.frame_120)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_162.addWidget(self.line_16)


        self.verticalLayout_167.addWidget(self.frame_120)

        self.frame_119 = QFrame(self.frame_131)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_119)
        self.verticalLayout_160.setSpacing(3)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(-1, 9, -1, -1)
        self.frame_122 = QFrame(self.frame_119)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMaximumSize(QSize(16777215, 50))
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(9, 9, 9, 9)
        self.label_41 = QLabel(self.frame_122)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(35, 16777215))
        self.label_41.setPixmap(QPixmap(u":/icons/icons/book.svg"))

        self.horizontalLayout_58.addWidget(self.label_41)

        self.label_29 = QLabel(self.frame_122)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_58.addWidget(self.label_29)


        self.verticalLayout_160.addWidget(self.frame_122)

        self.line_13 = QFrame(self.frame_119)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_160.addWidget(self.line_13)

        self.frame_123 = QFrame(self.frame_119)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_123)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(25)
        self.gridLayout_6.setVerticalSpacing(20)
        self.settings_fontComboBox = QFontComboBox(self.frame_123)
        self.settings_fontComboBox.setObjectName(u"settings_fontComboBox")
        self.settings_fontComboBox.setEditable(False)

        self.gridLayout_6.addWidget(self.settings_fontComboBox, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_35 = QLabel(self.frame_123)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_25 = QLabel(self.frame_123)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)

        self.settings_fontSizeComboBox = QSpinBox(self.frame_123)
        self.settings_fontSizeComboBox.setObjectName(u"settings_fontSizeComboBox")
        self.settings_fontSizeComboBox.setMinimumSize(QSize(0, 0))
        self.settings_fontSizeComboBox.setStyleSheet(u"")
        self.settings_fontSizeComboBox.setMinimum(8)
        self.settings_fontSizeComboBox.setMaximum(14)
        self.settings_fontSizeComboBox.setValue(12)

        self.gridLayout_6.addWidget(self.settings_fontSizeComboBox, 2, 1, 1, 1, Qt.AlignLeft)


        self.verticalLayout_160.addWidget(self.frame_123, 0, Qt.AlignLeft)

        self.line_17 = QFrame(self.frame_119)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_160.addWidget(self.line_17)


        self.verticalLayout_167.addWidget(self.frame_119)

        self.frame_121 = QFrame(self.frame_131)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_121)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(-1, 9, -1, -1)
        self.frame_126 = QFrame(self.frame_121)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMaximumSize(QSize(16777215, 50))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_42 = QLabel(self.frame_126)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(35, 16777215))
        self.label_42.setPixmap(QPixmap(u":/icons/icons/briefcase.svg"))

        self.horizontalLayout_59.addWidget(self.label_42)

        self.label_36 = QLabel(self.frame_126)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_59.addWidget(self.label_36)


        self.verticalLayout_164.addWidget(self.frame_126)

        self.line_15 = QFrame(self.frame_121)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_164.addWidget(self.line_15)

        self.frame_127 = QFrame(self.frame_121)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setStyleSheet(u"QPushButton{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(43, 49, 65);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(50, 56, 75);\n"
"}\n"
"")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_127)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.settings_view_users_btn = QPushButton(self.frame_127)
        self.settings_view_users_btn.setObjectName(u"settings_view_users_btn")
        self.settings_view_users_btn.setMinimumSize(QSize(120, 25))
        self.settings_view_users_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_view_users_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_view_users_btn.setFlat(True)

        self.verticalLayout_166.addWidget(self.settings_view_users_btn)


        self.verticalLayout_164.addWidget(self.frame_127, 0, Qt.AlignHCenter)


        self.verticalLayout_167.addWidget(self.frame_121)

        self.settings_apply_settings = QPushButton(self.frame_131)
        self.settings_apply_settings.setObjectName(u"settings_apply_settings")
        self.settings_apply_settings.setMinimumSize(QSize(100, 25))
        self.settings_apply_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_apply_settings.setStyleSheet(u"QPushButton{\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius:4px;\n"
"background-color: rgb(83, 94, 125);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(92, 105, 139);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(111, 126, 168);\n"
"}\n"
"")

        self.verticalLayout_167.addWidget(self.settings_apply_settings, 0, Qt.AlignRight)


        self.verticalLayout_53.addWidget(self.frame_131, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.settings_stackedWidget.addWidget(self.settings_main)
        self.settings_sim_users = QWidget()
        self.settings_sim_users.setObjectName(u"settings_sim_users")
        self.verticalLayout_168 = QVBoxLayout(self.settings_sim_users)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.settings_return_to_homepage_button = QPushButton(self.settings_sim_users)
        self.settings_return_to_homepage_button.setObjectName(u"settings_return_to_homepage_button")
        self.settings_return_to_homepage_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border:none;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border-radius:7px;\n"
"	background-color: rgb(60, 88, 125);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border-radius:7px;\n"
"	background-color: rgb(71, 105, 149);\n"
"}\n"
"")
        self.settings_return_to_homepage_button.setIcon(icon12)
        self.settings_return_to_homepage_button.setIconSize(QSize(32, 32))
        self.settings_return_to_homepage_button.setFlat(True)

        self.verticalLayout_168.addWidget(self.settings_return_to_homepage_button, 0, Qt.AlignLeft)

        self.frame_129 = QFrame(self.settings_sim_users)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_129)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.frame_72 = QFrame(self.frame_129)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_72)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.label_8 = QLabel(self.frame_72)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_165.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.frame_130 = QFrame(self.frame_72)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(423, 0))
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_130)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.settings_users_table = QTableWidget(self.frame_130)
        if (self.settings_users_table.columnCount() < 4):
            self.settings_users_table.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.settings_users_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.settings_users_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.settings_users_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.settings_users_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.settings_users_table.setObjectName(u"settings_users_table")
        self.settings_users_table.setMaximumSize(QSize(410, 16777215))
        self.settings_users_table.setToolTipDuration(3)
        self.settings_users_table.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(182, 182, 182);")

        self.verticalLayout_170.addWidget(self.settings_users_table)


        self.verticalLayout_165.addWidget(self.frame_130, 0, Qt.AlignHCenter)


        self.verticalLayout_169.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_129)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_73)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.label_5 = QLabel(self.frame_73)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")

        self.verticalLayout_163.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.settings_original_file_edit = QPlainTextEdit(self.frame_73)
        self.settings_original_file_edit.setObjectName(u"settings_original_file_edit")
        self.settings_original_file_edit.setMinimumSize(QSize(700, 0))
        self.settings_original_file_edit.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(40, 40, 40);")
        self.settings_original_file_edit.setReadOnly(True)

        self.verticalLayout_163.addWidget(self.settings_original_file_edit)

        self.setting_users_file_location = QLabel(self.frame_73)
        self.setting_users_file_location.setObjectName(u"setting_users_file_location")

        self.verticalLayout_163.addWidget(self.setting_users_file_location)


        self.verticalLayout_169.addWidget(self.frame_73)


        self.verticalLayout_168.addWidget(self.frame_129, 0, Qt.AlignHCenter)

        self.settings_stackedWidget.addWidget(self.settings_sim_users)

        self.verticalLayout_159.addWidget(self.settings_stackedWidget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_33.addWidget(self.scrollArea_2)


        self.verticalLayout_7.addWidget(self.frame_114)

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
        font10 = QFont()
        font10.setPointSize(20)
        self.about_extra_content.setFont(font10)
        self.about_extra_content.setFrameShape(QFrame.StyledPanel)
        self.about_extra_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.about_extra_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 10, 0, 0)
        self.about_title = QLabel(self.about_extra_content)
        self.about_title.setObjectName(u"about_title")
        font11 = QFont()
        font11.setPointSize(25)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setUnderline(True)
        font11.setWeight(75)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        self.about_title.setFont(font11)

        self.verticalLayout_4.addWidget(self.about_title)

        self.about_extra_content_frame = QFrame(self.about_extra_content)
        self.about_extra_content_frame.setObjectName(u"about_extra_content_frame")
        self.about_extra_content_frame.setFrameShape(QFrame.StyledPanel)
        self.about_extra_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.about_extra_content_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.github_symbol = QLabel(self.about_extra_content_frame)
        self.github_symbol.setObjectName(u"github_symbol")
        font12 = QFont()
        font12.setPointSize(13)
        self.github_symbol.setFont(font12)
        self.github_symbol.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_9.addWidget(self.github_symbol)

        self.github_link = QLabel(self.about_extra_content_frame)
        self.github_link.setObjectName(u"github_link")
        font13 = QFont()
        font13.setPointSize(16)
        self.github_link.setFont(font13)
        self.github_link.setCursor(QCursor(Qt.PointingHandCursor))
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
        font14 = QFont()
        font14.setPointSize(12)
        self.developed_by_theo_brown.setFont(font14)
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
        self.help_button.setFont(font14)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon16)
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

        self.stacked_menu_pages.setCurrentIndex(4)
        self.ticker_label_title_analysis.setDefault(False)
        self.stock_analysis_stackedWidget.setCurrentIndex(0)
        self.stacked_charts.setCurrentIndex(0)
        self.stacked_charts_2.setCurrentIndex(0)
        self.learning_pages_stackedWidget.setCurrentIndex(0)
        self.simulator_stacked_widget.setCurrentIndex(0)
        self.pushButton_5.setDefault(False)
        self.tabWidget.setCurrentIndex(0)
        self.simulator_user_icon_btn.setDefault(False)
        self.stock_sim_trade_stackedWidget.setCurrentIndex(0)
        self.settings_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_icon_button.setText("")
        self.menu_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Menu</span></p></body></html>", None))
        self.app_title_icon.setText("")
        self.app_name_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">INVESTING APP</span></p></body></html>", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.trade_icon.setText("")
        self.stock_analysis_icon.setText("")
        self.home_icon.setText("")
        self.settings_icon.setText("")
        self.learn_icon.setText("")
        self.about_icon.setText("")
        self.home_page_title.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.home_page_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome to the future investor app!</p><p align=\"center\"><br/></p><p align=\"center\">This application is just meant to teach the basics of investing. You will be working with crypto, stocks and forex. </p><p align=\"center\"><br/></p><p align=\"center\">This application is meant for absolute begginers.<br/></p><p align=\"center\">Its features include:</p><p align=\"center\">- Quotes and chart visualization.</p><p align=\"center\">- Teaching on how stock, crypto and forex work.</p><p align=\"center\">- Quizzes to test knowledge.</p><p align=\"center\">- Trading simulator.</p><p align=\"center\">- Next day prediction. (Do not use a s real financial advice)</p></body></html>", None))
        self.stock_analysis_title.setText(QCoreApplication.translate("MainWindow", u"Currency/Stock analysis", None))
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a ticker", None))
        self.search_button.setText("")
        self.ticker_label_title_analysis.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.price_traded_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.change_direction_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.change_amount_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.change_percentage.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_analysis_stock_info_content.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.one_day_button.setText(QCoreApplication.translate("MainWindow", u"1 day", None))
        self.one_week_button.setText(QCoreApplication.translate("MainWindow", u"1 week", None))
        self.one_month_button.setText(QCoreApplication.translate("MainWindow", u"1 moth", None))
        self.one_year_button.setText(QCoreApplication.translate("MainWindow", u"1 year", None))
        self.five_year_button.setText(QCoreApplication.translate("MainWindow", u"5 year", None))
        self.max_button.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.day_high_placeholder.setText("")
        self.day_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.day_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.day_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.day_open_placeholder.setText("")
        self.day_low_placeholder.setText("")
        self.avg_volume_placeholder.setText("")
        self.avg_volume.setText(QCoreApplication.translate("MainWindow", u"Avg Volume", None))
        self.market_cap_placeholder.setText("")
        self.volume_placeholder.setText("")
        self.volume_label.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.market_cap.setText(QCoreApplication.translate("MainWindow", u"Mkt Cap", None))
        self.fifty_two_week_high.setText(QCoreApplication.translate("MainWindow", u"52wK High", None))
        self.fifty_two_week_high_placeholder.setText("")
        self.fifty_two_week_low_placeholder.setText("")
        self.fifty_two_week_low.setText(QCoreApplication.translate("MainWindow", u"52wK Low", None))
        self.label_7.setText("")
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_title.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_6.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_6.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_6.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_5.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_5.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_5.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_10.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_10.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_10.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_11.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_11.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_11.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_12.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_12.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_12.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_7.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_7.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_7.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_8.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_8.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_8.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_9.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_9.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_9.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.crypto_price_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.crypto_currency_price_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.extra_info_about_crypto.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.first_currency_entry.setText("")
        self.second_curency_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.first_currency_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.crypto_comparison_button.setText("")
        self.one_day_button_2.setText(QCoreApplication.translate("MainWindow", u"1 day", None))
        self.one_week_button_2.setText(QCoreApplication.translate("MainWindow", u"1 week", None))
        self.one_month_button_2.setText(QCoreApplication.translate("MainWindow", u"1 moth", None))
        self.one_year_button_2.setText(QCoreApplication.translate("MainWindow", u"1 year", None))
        self.five_year_button_2.setText(QCoreApplication.translate("MainWindow", u"5 year", None))
        self.max_button_2.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.stock_news_title_2.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_2.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_2.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_13.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_13.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_13.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_14.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_14.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_14.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_15.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_15.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_15.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_16.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_16.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_16.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_17.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_17.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_17.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_18.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_18.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_18.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_19.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_19.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_19.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_title_20.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_text_20.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_news_media_20.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.learn_start_page_title_label.setText(QCoreApplication.translate("MainWindow", u"LEARN", None))
        self.what_do_you_wish_to_learn_label.setText(QCoreApplication.translate("MainWindow", u"What do you wish to learn?", None))
        self.stocks_button_learn.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.forex_button_learn.setText(QCoreApplication.translate("MainWindow", u"Forex", None))
        self.crypto_button_learn.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.learn_return_to_homepage_button.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"STOCKS", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Table of contents", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"1. What is a stock?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"2. Investing in stocks", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"3. Why do people invest in stocks?", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"4. Why do companies issue stocks", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"5. Types of stock", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"6. Stock market capitalization", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1. What is a stock", None))
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation (e.g. Apple, Netflix, Amazon).\\n\\nThis entitles the owner of the stock to a proportion of the corporation's assets and profits equal to how much stock they own.\\n\\nUnits of stock are called \"shares.\"\\n\\n\\nStocks are bought and sold predominantly on stock exchanges, though there can be private sales as well, and are the foundation of many individual investors' portfolios.\\n\\nThese transactions have to conform to government regulations which are meant to protect investors from fraudulent practices.\\n\\n\\nWhen you own stock in a company, you are called a shareholder because you share in the company's profits.\\n\\nPublic companies sell their stock through a stock market exchange, like the Nasdaq or the New York Stock Exchange.\\n\\nInvestors can then buy and sell these shares among themselves through stockbrokers.\\n\\nThe stock exchanges track the supply and demand of each company's stock, which"
                        " directly affects the stock's price.\\n\\n\\nStock prices fluctuate throughout the day, but investors who own stock hope that over time, the stock will increase in value.\\n\\nHowever, not every company or stock does so, companies can lose value or go out of business completely.\\n\\nWhen that happens, stock investors may lose all or part of their investment.\\n\\nThat's why it's important for investors to spread their money around, buying stock in many different companies rather than focusing on just one.\\n\\nThis is also called a portfolio.\\n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2. Understanding stocks", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Corporations issue (sell) stock to raise funds to operate their businesses.\\n\\nThe holder of stock (a shareholder) has now bought a piece of the corporation and, depending on the type of shares held, may have a claim to a part of its assets and earnings.\\n\\nIn other words, a shareholder is now an owner of the issuing company.\\n\\nOwnership is determined by the number of shares a person owns relative to the number of outstanding shares. For example, if a company has 1,000 shares of stock outstanding and one person owns 100 shares, that person would own and have claim to 10% of the company's assets and earnings.\\n\\nStock holders do not own corporations; they own shares issued by corporations. But corporations are a special type of organization because the law treats them as legal persons. \\n\\nIn other words, corporations file taxes, can borrow, can own property, can be sued, etc.\\n\\nThe idea that a corporation is a \u201cperson\u201d means that the corporation owns its own assets. A corporate office f"
                        "ull of chairs and tables belongs to the corporation, and not to the shareholders.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3. Why do people buy stocks", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"The primary reason that people buy shares of companies is to make money. The idea is to buy low and sell high. \\nFor instance, if you buy 100 shares of Company B stock valued at $25 each, you will have made an initial investment totaling $2,500. Say the value of the share increases to 50$. Your profit will be of $2,500. \\nHowever there is more to why people buy stocks, here are some other reasons:\\n\\n\\n - Investing in stocks is an excellent way to grow wealth. For long-term investors, stocks are a good investment even during periods of market volatility\\n\\n \\n - You can get rich with stocks, you just need to take the risk. You can grow wealth by putting your money into the stock market over a long timeframe.\\n\\n\\n - It Doesn't Cost Much to Get Started\\n\\n\\n - Protect. Taxes and inflation can impact your wealth.\\n\\n\\n - Stocks Are Designed To Go Up In Price, the larger indexes including the Dow Jones and the S&P 500 are updated periodically. Companies that are not performing are pulled out of t"
                        "he indexes and are replaced by companies that are being traded more frequently\u2014among other factors. This ensures that the major indexes are always populated by companies that are earning money, and being traded frequently.\\n\\n\\n - You Don't Have to Be a Genius. While an experienced investor may be able to grow their money faster than you\u2014that doesn't mean you can't buy stocks! And you don't need to be a Chartered Financial Analyst, portfolio manager or the next Warren Buffett to invest in stocks. Also, buying stocks and making money with them is clearly much easier than building a successful business from scratch! To invest in a company's stock you must read their annual report (which you can easily find online), set some money aside and understand basic math.\\n\\n\\n - Another reason why people buy stocks is to support a company they like.\\nIt is funny to think of investing for sentimental reasons, but if you\u2019re the type of person who likes a product or a company and you wish to help ensur"
                        "e that it stays successful within the market, then this reason for stock investment describes you. Some people also want the power to help in making company decisions and this will happen when you become a shareholder. Shareholders can attend meetings that help the company they invest in make decisions that affect its income.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"4. Why do Companies issue stocks", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"Corporations issue stock to raise money for growth and expansion. To raise money, corporations will issue stock by selling off a percentage of profits in a company.\\nThere are many reasons that a company would issue stock to raise money. Some of the common reasons include:\\n\\n\\n - The development of new products\\n \\n - To purchase equipment\\n \\n - To buy new buildings\\n \\n - To increase inventory\\n \\n - To expand and grow staff\\n \\n - To reduce debt\\n \\n - To prepare for a merger or acquisition\\n \\n - To improve the value of a company\\n \\n - To provide for greater flexibility", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"5. Types of Stock", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"There are two main kinds of stocks, common stock and preferred stock.\\n\\nCommon stock entitles owners to vote at shareholder meetings and receive dividends. They represent the majority of stock held by the public.\\nOwners of common stock have voting rights and the right to dividend payouts, but there is one major drawback: If a company is forced to liquidate or go bankrupt, common shareholders are last in line when it comes to payouts.\\nPreferred shareholders and bondholders must be paid out in full before common shareholders can begin receiving payments.\\n\\nPreferred stockholders usually don\u2019t have voting rights but they receive dividend payments before common stockholders do, and have priority over common stockholders if the company goes bankrupt and its assets are liquidated. Preferred stockholders have fewer rights than common stockholders, except when it comes to dividends.\\nCompanies that issue preferred stocks usually pay consistent dividends, and preferred stockholders have priority on divi"
                        "dends over common stockholders.  Investors buy preferred stock for its current income from dividends, so look for companies that make big profits to use preferred stock to return some of those profits via dividends.", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"6. Market capitalization", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"A way to categorize stocks is by the size of the company, as shown in its market capitalization. \\nThere are large-cap, mid-cap, and small-cap stocks. Shares in very small companies are sometimes called \u201cmicrocap\u201d stocks.\\nThe very lowest priced stocks are known as \u201cpenny stocks.\u201d These companies may have little or no earnings. Penny stocks do not pay dividends and are highly speculative.\\n\\nMarket cap\u2014or market capitalization\u2014refers to the total value of all a company's shares of stock.\\nIt is calculated by multiplying the price of a stock by its total number of outstanding shares. For example, a company with 200 million shares selling at $50 a share would have a market cap of $10 billion.\\n\\nThis value allows investors to understand the relative size of one company versus another. \\nMarket cap measures what a company is worth on the open market, as well as the market's perception of its future prospects, because it reflects what investors are willing to pay for its stock"
                        ".\\nBelow are the descriptions for 3 market cap sizes:\\n\\n - Large-cap companies are typically firms with a market value of $10 billion or more. Large-cap firms often have a reputation for producing quality goods and services, a history of consistent dividend payments, and steady growth. They are often dominant players within established industries, and their brand names may be familiar to a national consumer audience.\\n\\n - Mid-cap companies are typically businesses with a market value between $2 billion and $10 billion. Typically, these are established companies in industries experiencing or expected to experience rapid growth. These medium-sized companies may be in the process of increasing market share and improving overall competitiveness. This stage of growth is likely to determine whether a company eventually lives up to its full potential. Mid-cap stocks generally fall between large caps and small caps on the risk/return spectrum. Mid-caps may offer more growth potential than large caps, and possib"
                        "ly less risk than small caps.\\n\\n - Small-cap companies are typically those with a market value of $300 million to $2 billion. Generally, these are young companies that serve niche markets or emerging industries. Small caps are considered the most aggressive and risky of the 3 categories. The relatively limited resources of small companies can potentially make them more susceptible to a business or economic downturn. They may also be vulnerable to the intense competition and uncertainties characteristic of untried, burgeoning markets. On the other hand, small-cap stocks may offer significant growth potential to long-term investors who can tolerate volatile stock price swings in the short term.", None))
        self.crypto_learning_content_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">CRYPTOCURRENCY</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline; color:#ffffff;\">Table of contents</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">1. What is cryptocurrency?</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">2. Blockchain technology</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">3. Cryptocurrency mining</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">4. Initial coin offering</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">5. Finding a broker</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">6. Chosing the right cryptocurrency</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">7. What affects the price of cryptocu"
                        "rrency</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">8. Cryptocurrency terminology</span></p></body></html>", None))
        self.forex_learning_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">FOREX (FOREIGN EXCHANGE)</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">TABLE OF CONTENTS</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">1. What is Forex trading?</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">2. History of the Forex market</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">3. Major currencies</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">4. Basic Forex terminology</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">5. Where trading happens</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">6. How to connect to the market</span></p></body></html>", None))
        self.simulator_start_page_title_label.setText(QCoreApplication.translate("MainWindow", u"TRADE", None))
        self.simulator_start_page_content_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to the trading simulator! Click the button below to start:", None))
        self.stock_simulator_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.simulator_return_to_homepage_button.setText("")
        self.pushButton_5.setText("")
        self.simulator_login_to_username_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your username", None))
        self.simulator_continue_to_sim_btn.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.simulator_create_new_user_btn.setText(QCoreApplication.translate("MainWindow", u"Don't have one? Click here to create one", None))
        self.simulator_return_to_homepage_button_2.setText("")
        self.simulator_new_username_entry.setText("")
        self.simulator_new_username_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter new username", None))
        self.simulator_confirm_new_username_entry.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
#if QT_CONFIG(tooltip)
        self.stock_simulator_title.setToolTip(QCoreApplication.translate("MainWindow", u"hee", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.stock_simulator_title.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.stock_simulator_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">STOCK SIMULATOR</span></p></body></html>", None))
        self.label_18.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Current price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Today's change", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Purchase price", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total value", None));
        self.simulator_user_icon_btn.setText("")
        self.stock_simulator_username_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Account value", None))
        self.stock_simulator_account_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.stock_simulator_cash_amount_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Total Gain/Loss", None))
        self.stock_simulator_gainloss_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.stock_simulator_logout_btn.setText(QCoreApplication.translate("MainWindow", u"  Logout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Portfolio), QCoreApplication.translate("MainWindow", u"Portfolio", None))
        self.stock_simulator_order_details_title.setText(QCoreApplication.translate("MainWindow", u"ORDER DETAILS", None))
        self.stock_simulator_stock_ticker_label.setText(QCoreApplication.translate("MainWindow", u"Stock symbol", None))
        self.stock_simulator_transaction_label.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.stock_simulator_transaction_type_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Buy", None))
        self.stock_simulator_transaction_type_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sell", None))

        self.stock_simulator_quantity_label.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.stock_simulator_quantity_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.stock_simulator_symbol_lookup_button.setText(QCoreApplication.translate("MainWindow", u"View stock...", None))
        self.stock_simulator_purchase_button_2.setText(QCoreApplication.translate("MainWindow", u"CLEAR ALL", None))
        self.stock_simulator_purchase_button.setText(QCoreApplication.translate("MainWindow", u"PREVIEW ORDER", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Preview order", None))
        self.stock_name.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.quantity_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total Spread", None))
        self.total_spread_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.total_cost_label.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_simulator_purchase_camcel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL ORDER", None))
        self.stock_simulator_purchase_confirm_btn.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Trade), QCoreApplication.translate("MainWindow", u"Trade", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT DETAILS", None))
        self.stock_simulator_stocks_owned_label.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.stock_simulator_username_label_2.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Stocks owned", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT ACTIONS", None))
        self.stock_simulator_delete_account_btn.setText(QCoreApplication.translate("MainWindow", u"  Delete account", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_40.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Stocks Page", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Ticker Extra Info", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"News visible", None))
        self.settings_news_visible_checkBox.setText("")
        self.settings_extra_info_checkBox.setText("")
        self.label_41.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Learning Section", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.label_42.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Trading Simulator", None))
        self.settings_view_users_btn.setText(QCoreApplication.translate("MainWindow", u"View users", None))
        self.settings_apply_settings.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.settings_return_to_homepage_button.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        ___qtablewidgetitem7 = self.settings_users_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem8 = self.settings_users_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.settings_users_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Cash", None));
        ___qtablewidgetitem10 = self.settings_users_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Stocks owned", None));
#if QT_CONFIG(tooltip)
        self.settings_users_table.setToolTip(QCoreApplication.translate("MainWindow", u"double click on a user to delete", u"lllll"))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.settings_users_table.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.settings_users_table.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.settings_users_table.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Original File", None))
        self.settings_original_file_edit.setPlainText("")
        self.setting_users_file_location.setText(QCoreApplication.translate("MainWindow", u"File Location: _", None))
        self.about_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">About</span></p></body></html>", None))
        self.github_symbol.setText("")
        self.github_link.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/Theo524/\"><span style=\" text-decoration: underline; color:#ffffff;\">Github</span></a></p></body></html>", None))
        self.developed_by_theo_brown.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Developed by Theo Brown</span></p></body></html>", None))
        self.help_button.setText("")
    # retranslateUi


# Ticker extra info frontend
class Ticker_Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 551)
        MainWindow.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(32, 36, 48);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ticker_name = QLabel(self.frame)
        self.ticker_name.setObjectName(u"ticker_name")
        self.ticker_name.setStyleSheet(u"font: 75 24pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.ticker_name, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	border-radius:10px;\n"
"	background-color:rgb(85, 170, 255);\n"
"}\n"
"QPushButton::hover {\n"
"	border-radius:10px;\n"
"    background-color:rgb(63, 126, 189);\n"
"}\n"
"QPushButton::pressed {\n"
"	border-radius:10px;	\n"
"    background-color:rgb(37, 75, 112);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profile_btn = QPushButton(self.frame_3)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setMinimumSize(QSize(0, 20))
        self.profile_btn.setMaximumSize(QSize(100, 16777215))
        self.profile_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.profile_btn)

        self.stats_btn = QPushButton(self.frame_3)
        self.stats_btn.setObjectName(u"stats_btn")
        self.stats_btn.setMinimumSize(QSize(0, 20))
        self.stats_btn.setMaximumSize(QSize(100, 16777215))
        self.stats_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.stats_btn)


        self.verticalLayout.addWidget(self.frame_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stock_profile_page = QWidget()
        self.stock_profile_page.setObjectName(u"stock_profile_page")
        self.verticalLayout_3 = QVBoxLayout(self.stock_profile_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_4 = QFrame(self.stock_profile_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.scrollArea = QScrollArea(self.stock_profile_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 657, 402))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 13, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.website = QLabel(self.frame_6)
        self.website.setObjectName(u"website")

        self.gridLayout_5.addWidget(self.website, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 14, 0, 1, 1, Qt.AlignTop)

        self.summary_frame = QFrame(self.scrollAreaWidgetContents)
        self.summary_frame.setObjectName(u"summary_frame")
        self.summary_frame.setFrameShape(QFrame.StyledPanel)
        self.summary_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.summary_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.summary = QLabel(self.summary_frame)
        self.summary.setObjectName(u"summary")
        self.summary.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.summary, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.summary_frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sector = QLabel(self.frame_2)
        self.sector.setObjectName(u"sector")

        self.gridLayout_2.addWidget(self.sector, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.industry = QLabel(self.frame_2)
        self.industry.setObjectName(u"industry")

        self.gridLayout_2.addWidget(self.industry, 1, 1, 1, 1)

        self.employees = QLabel(self.frame_2)
        self.employees.setObjectName(u"employees")

        self.gridLayout_2.addWidget(self.employees, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 5, 0, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.country = QLabel(self.frame_4)
        self.country.setObjectName(u"country")

        self.gridLayout_3.addWidget(self.country, 1, 0, 1, 1)

        self.zip = QLabel(self.frame_4)
        self.zip.setObjectName(u"zip")

        self.gridLayout_3.addWidget(self.zip, 9, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.city = QLabel(self.frame_4)
        self.city.setObjectName(u"city")

        self.gridLayout_3.addWidget(self.city, 5, 0, 1, 1)

        self.phone = QLabel(self.frame_4)
        self.phone.setObjectName(u"phone")

        self.gridLayout_3.addWidget(self.phone, 7, 0, 1, 1)

        self.state = QLabel(self.frame_4)
        self.state.setObjectName(u"state")

        self.gridLayout_3.addWidget(self.state, 3, 0, 1, 1)

        self.address = QLabel(self.frame_4)
        self.address.setObjectName(u"address")

        self.gridLayout_3.addWidget(self.address, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 9, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.stock_profile_page)
        self.crypto_profile_page = QWidget()
        self.crypto_profile_page.setObjectName(u"crypto_profile_page")
        self.verticalLayout_4 = QVBoxLayout(self.crypto_profile_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.crypto_profile_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 674, 312))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_7, 8, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_9.addWidget(self.label_4, 1, 0, 1, 1)

        self.crypto_market = QLabel(self.frame_5)
        self.crypto_market.setObjectName(u"crypto_market")

        self.gridLayout_9.addWidget(self.crypto_market, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_7, 3, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_5, 5, 0, 1, 1)

        self.summary_frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.summary_frame_2.setObjectName(u"summary_frame_2")
        self.summary_frame_2.setFrameShape(QFrame.StyledPanel)
        self.summary_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.summary_frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.crypto_summary = QLabel(self.summary_frame_2)
        self.crypto_summary.setObjectName(u"crypto_summary")
        self.crypto_summary.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_8.addWidget(self.crypto_summary, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.summary_frame_2, 0, 0, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 4, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.crypto_profile_page)
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.stackedWidget.addWidget(self.start_page)
        self.stock_statistics_page = QWidget()
        self.stock_statistics_page.setObjectName(u"stock_statistics_page")
        self.stackedWidget.addWidget(self.stock_statistics_page)
        self.crypto_statistics_page = QWidget()
        self.crypto_statistics_page.setObjectName(u"crypto_statistics_page")
        self.stackedWidget.addWidget(self.crypto_statistics_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ticker_name.setText(QCoreApplication.translate("MainWindow", u"Ticker name", None))
        self.profile_btn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.stats_btn.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.website.setText(QCoreApplication.translate("MainWindow", u"website", None))
        self.summary.setText(QCoreApplication.translate("MainWindow", u"summary", None))
        self.sector.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Time Employees", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Industry", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sector", None))
        self.industry.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.employees.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.country.setText(QCoreApplication.translate("MainWindow", u"country", None))
        self.zip.setText(QCoreApplication.translate("MainWindow", u"zip", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Personal info", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"city", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.state.setText(QCoreApplication.translate("MainWindow", u"state", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"address", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Market", None))
        self.crypto_market.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.crypto_summary.setText(QCoreApplication.translate("MainWindow", u"summary", None))
    # retranslateUi
