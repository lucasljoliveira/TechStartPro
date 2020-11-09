# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 492)
        icon = QIcon()
        icon.addFile(u"../../../../Desktop/download-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
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
        if (self.tableWidget_products.columnCount() < 5):
            self.tableWidget_products.setColumnCount(5)
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText(u"Categories");
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget_products.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_products.setObjectName(u"tableWidget_products")
        self.tableWidget_products.setGeometry(QRect(30, 140, 741, 271))
        self.pushButton_CreateProduct = QPushButton(self.centralwidget)
        self.pushButton_CreateProduct.setObjectName(u"pushButton_CreateProduct")
        self.pushButton_CreateProduct.setGeometry(QRect(550, 420, 91, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.pushButton_CreateProduct.setFont(font2)
        self.lineEdit_Name = QLineEdit(self.centralwidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setGeometry(QRect(30, 100, 141, 31))
        self.lineEdit_Name.setFont(font2)
        self.pushButton_Search = QPushButton(self.centralwidget)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(670, 100, 101, 31))
        self.pushButton_Search.setFont(font2)
        self.pushButton_ImportCategories = QPushButton(self.centralwidget)
        self.pushButton_ImportCategories.setObjectName(u"pushButton_ImportCategories")
        self.pushButton_ImportCategories.setGeometry(QRect(30, 420, 211, 41))
        self.pushButton_ImportCategories.setFont(font2)
        self.pushButton_UpdateProduct = QPushButton(self.centralwidget)
        self.pushButton_UpdateProduct.setObjectName(u"pushButton_UpdateProduct")
        self.pushButton_UpdateProduct.setGeometry(QRect(450, 420, 91, 41))
        self.pushButton_UpdateProduct.setFont(font2)
        self.pushButton_RemoveProduct = QPushButton(self.centralwidget)
        self.pushButton_RemoveProduct.setObjectName(u"pushButton_RemoveProduct")
        self.pushButton_RemoveProduct.setGeometry(QRect(350, 420, 91, 41))
        self.pushButton_RemoveProduct.setFont(font2)
        self.lineEdit_Description = QLineEdit(self.centralwidget)
        self.lineEdit_Description.setObjectName(u"lineEdit_Description")
        self.lineEdit_Description.setGeometry(QRect(190, 100, 141, 31))
        self.lineEdit_Description.setFont(font2)
        self.lineEdit_Price = QLineEdit(self.centralwidget)
        self.lineEdit_Price.setObjectName(u"lineEdit_Price")
        self.lineEdit_Price.setGeometry(QRect(350, 100, 141, 31))
        self.lineEdit_Price.setFont(font2)
        self.lineEdit_Category = QLineEdit(self.centralwidget)
        self.lineEdit_Category.setObjectName(u"lineEdit_Category")
        self.lineEdit_Category.setGeometry(QRect(510, 100, 141, 31))
        self.lineEdit_Category.setFont(font2)
        self.label_Search_Name = QLabel(self.centralwidget)
        self.label_Search_Name.setObjectName(u"label_Search_Name")
        self.label_Search_Name.setGeometry(QRect(30, 75, 71, 20))
        self.label_Search_Name.setFont(font2)
        self.label_Search_Description = QLabel(self.centralwidget)
        self.label_Search_Description.setObjectName(u"label_Search_Description")
        self.label_Search_Description.setGeometry(QRect(190, 70, 131, 31))
        self.label_Search_Description.setFont(font2)
        self.label_Search_Price = QLabel(self.centralwidget)
        self.label_Search_Price.setObjectName(u"label_Search_Price")
        self.label_Search_Price.setGeometry(QRect(350, 77, 61, 20))
        self.label_Search_Price.setFont(font2)
        self.label_Search_Categories = QLabel(self.centralwidget)
        self.label_Search_Categories.setObjectName(u"label_Search_Categories")
        self.label_Search_Categories.setGeometry(QRect(510, 70, 121, 31))
        self.label_Search_Categories.setFont(font2)
        self.pushButton_Exit = QPushButton(self.centralwidget)
        self.pushButton_Exit.setObjectName(u"pushButton_Exit")
        self.pushButton_Exit.setGeometry(QRect(710, 420, 61, 41))
        self.pushButton_Exit.setFont(font2)
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
        self.pushButton_CreateProduct.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_Search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_ImportCategories.setText(QCoreApplication.translate("MainWindow", u"Import Categories", None))
        self.pushButton_UpdateProduct.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_RemoveProduct.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_Search_Name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_Search_Description.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label_Search_Price.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.label_Search_Categories.setText(QCoreApplication.translate("MainWindow", u"Categories:", None))
        self.pushButton_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

