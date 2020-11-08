# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newProductWindow.ui'
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


class Ui_Form_NewProduct(object):
    def setupUi(self, Form_NewProduct):
        if not Form_NewProduct.objectName():
            Form_NewProduct.setObjectName(u"Form_NewProduct")
        Form_NewProduct.resize(400, 445)
        icon = QIcon()
        icon.addFile(u"main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_NewProduct.setWindowIcon(icon)
        self.comboBox_CategoriesList = QComboBox(Form_NewProduct)
        self.comboBox_CategoriesList.setObjectName(u"comboBox_CategoriesList")
        self.comboBox_CategoriesList.setGeometry(QRect(30, 230, 221, 31))
        font = QFont()
        font.setPointSize(14)
        self.comboBox_CategoriesList.setFont(font)
        self.label_NewProduct = QLabel(Form_NewProduct)
        self.label_NewProduct.setObjectName(u"label_NewProduct")
        self.label_NewProduct.setGeometry(QRect(30, 10, 221, 50))
        font1 = QFont()
        font1.setPointSize(25)
        self.label_NewProduct.setFont(font1)
        self.pushButton_SaveProduct = QPushButton(Form_NewProduct)
        self.pushButton_SaveProduct.setObjectName(u"pushButton_SaveProduct")
        self.pushButton_SaveProduct.setGeometry(QRect(270, 320, 101, 51))
        self.pushButton_SaveProduct.setFont(font)
        self.lineEdit_Name = QLineEdit(Form_NewProduct)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setGeometry(QRect(130, 80, 250, 31))
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Description = QLineEdit(Form_NewProduct)
        self.lineEdit_Description.setObjectName(u"lineEdit_Description")
        self.lineEdit_Description.setGeometry(QRect(129, 120, 251, 31))
        self.lineEdit_Description.setFont(font)
        self.lineEdit_Price = QLineEdit(Form_NewProduct)
        self.lineEdit_Price.setObjectName(u"lineEdit_Price")
        self.lineEdit_Price.setGeometry(QRect(130, 160, 250, 31))
        self.lineEdit_Price.setFont(font)
        self.label_NewProductName = QLabel(Form_NewProduct)
        self.label_NewProductName.setObjectName(u"label_NewProductName")
        self.label_NewProductName.setGeometry(QRect(62, 85, 81, 20))
        self.label_NewProductName.setFont(font)
        self.label_NewProductDescription = QLabel(Form_NewProduct)
        self.label_NewProductDescription.setObjectName(u"label_NewProductDescription")
        self.label_NewProductDescription.setGeometry(QRect(7, 118, 131, 31))
        self.label_NewProductDescription.setFont(font)
        self.label_NewProduct_Price = QLabel(Form_NewProduct)
        self.label_NewProduct_Price.setObjectName(u"label_NewProduct_Price")
        self.label_NewProduct_Price.setGeometry(QRect(71, 163, 71, 20))
        self.label_NewProduct_Price.setFont(font)
        self.listWidget_CategoriesAdded = QListWidget(Form_NewProduct)
        self.listWidget_CategoriesAdded.setObjectName(u"listWidget_CategoriesAdded")
        self.listWidget_CategoriesAdded.setGeometry(QRect(30, 270, 221, 161))
        self.pushButton_AddCategory = QPushButton(Form_NewProduct)
        self.pushButton_AddCategory.setObjectName(u"pushButton_AddCategory")
        self.pushButton_AddCategory.setGeometry(QRect(260, 230, 93, 31))
        self.pushButton_AddCategory.setFont(font)
        self.pushButton_RemoveCategory = QPushButton(Form_NewProduct)
        self.pushButton_RemoveCategory.setObjectName(u"pushButton_RemoveCategory")
        self.pushButton_RemoveCategory.setGeometry(QRect(260, 270, 93, 31))
        self.pushButton_RemoveCategory.setFont(font)
        self.label_NewID = QLabel(Form_NewProduct)
        self.label_NewID.setObjectName(u"label_NewID")
        self.label_NewID.setGeometry(QRect(250, 10, 111, 50))
        self.label_NewID.setFont(font1)
        self.label_NewID.setAlignment(Qt.AlignCenter)
        self.pushButton_CloseProduct = QPushButton(Form_NewProduct)
        self.pushButton_CloseProduct.setObjectName(u"pushButton_CloseProduct")
        self.pushButton_CloseProduct.setGeometry(QRect(270, 380, 101, 51))
        self.pushButton_CloseProduct.setFont(font)
        self.label_NewProduct_Categories = QLabel(Form_NewProduct)
        self.label_NewProduct_Categories.setObjectName(u"label_NewProduct_Categories")
        self.label_NewProduct_Categories.setGeometry(QRect(29, 198, 181, 31))
        self.label_NewProduct_Categories.setFont(font)

        self.retranslateUi(Form_NewProduct)

        QMetaObject.connectSlotsByName(Form_NewProduct)
    # setupUi

    def retranslateUi(self, Form_NewProduct):
        Form_NewProduct.setWindowTitle(QCoreApplication.translate("Form_NewProduct", u"Product", None))
        self.label_NewProduct.setText(QCoreApplication.translate("Form_NewProduct", u"Product ID:", None))
        self.pushButton_SaveProduct.setText(QCoreApplication.translate("Form_NewProduct", u"Save", None))
        self.label_NewProductName.setText(QCoreApplication.translate("Form_NewProduct", u"Name:", None))
        self.label_NewProductDescription.setText(QCoreApplication.translate("Form_NewProduct", u"Description:", None))
        self.label_NewProduct_Price.setText(QCoreApplication.translate("Form_NewProduct", u"Price:", None))
        self.pushButton_AddCategory.setText(QCoreApplication.translate("Form_NewProduct", u"Add ", None))
        self.pushButton_RemoveCategory.setText(QCoreApplication.translate("Form_NewProduct", u"Remove", None))
        self.label_NewID.setText("")
        self.pushButton_CloseProduct.setText(QCoreApplication.translate("Form_NewProduct", u"Close", None))
        self.label_NewProduct_Categories.setText(QCoreApplication.translate("Form_NewProduct", u"Categories:", None))
    # retranslateUi

