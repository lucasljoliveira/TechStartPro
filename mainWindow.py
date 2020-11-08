# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 492)
        icon = QIcon()
        icon.addFile(u"main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Title = QLabel(self.centralwidget)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(200, 10, 400, 50))
        font = QFont()
        font.setPointSize(25)
        self.label_Title.setFont(font)
        self.tableWidget_products = QTableWidget(self.centralwidget)
        if (self.tableWidget_products.columnCount() < 4):
            self.tableWidget_products.setColumnCount(4)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"ID");
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        self.tableWidget_products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText(u"Name");
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget_products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"Description");
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget_products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setText(u"Price");
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget_products.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_products.setObjectName(u"tableWidget_products")
        self.tableWidget_products.setGeometry(QRect(30, 130, 741, 271))
        self.pushButton_CreateProduct = QPushButton(self.centralwidget)
        self.pushButton_CreateProduct.setObjectName(u"pushButton_CreateProduct")
        self.pushButton_CreateProduct.setGeometry(QRect(620, 420, 151, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.pushButton_CreateProduct.setFont(font2)
        self.lineEdit_Search = QLineEdit(self.centralwidget)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")
        self.lineEdit_Search.setGeometry(QRect(244, 81, 331, 31))
        self.lineEdit_Search.setFont(font2)
        self.pushButton_Search = QPushButton(self.centralwidget)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(588, 80, 93, 31))
        self.pushButton_Search.setFont(font2)
        self.comboBox_searchType = QComboBox(self.centralwidget)
        self.comboBox_searchType.addItem(u"ID")
        self.comboBox_searchType.addItem(u"Name")
        self.comboBox_searchType.addItem(u"Description")
        self.comboBox_searchType.addItem(u"Price")
        self.comboBox_searchType.addItem(u"Category")
        self.comboBox_searchType.setObjectName(u"comboBox_searchType")
        self.comboBox_searchType.setGeometry(QRect(90, 80, 141, 31))
        self.comboBox_searchType.setFont(font2)
        self.pushButton_ImportCategories = QPushButton(self.centralwidget)
        self.pushButton_ImportCategories.setObjectName(u"pushButton_ImportCategories")
        self.pushButton_ImportCategories.setGeometry(QRect(30, 420, 211, 41))
        self.pushButton_ImportCategories.setFont(font2)
        self.pushButton_UpdateProduct = QPushButton(self.centralwidget)
        self.pushButton_UpdateProduct.setObjectName(u"pushButton_UpdateProduct")
        self.pushButton_UpdateProduct.setGeometry(QRect(540, 420, 71, 41))
        self.pushButton_UpdateProduct.setFont(font2)
        self.pushButton_RemoveProduct = QPushButton(self.centralwidget)
        self.pushButton_RemoveProduct.setObjectName(u"pushButton_RemoveProduct")
        self.pushButton_RemoveProduct.setGeometry(QRect(440, 420, 91, 41))
        self.pushButton_RemoveProduct.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Product Registration", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"Product registration", None))
        self.pushButton_CreateProduct.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.pushButton_Search.setText(QCoreApplication.translate("MainWindow", u"Search", None))

        self.pushButton_ImportCategories.setText(QCoreApplication.translate("MainWindow", u"Import Categories", None))
        self.pushButton_UpdateProduct.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_RemoveProduct.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

