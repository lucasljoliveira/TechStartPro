# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoriesFound.ui'
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


class Ui_Form_CategoriesFound(object):
    def setupUi(self, Form_CategoriesFound):
        if not Form_CategoriesFound.objectName():
            Form_CategoriesFound.setObjectName(u"Form_CategoriesFound")
        Form_CategoriesFound.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_CategoriesFound.setWindowIcon(icon)
        self.label_Categories_found = QLabel(Form_CategoriesFound)
        self.label_Categories_found.setObjectName(u"label_Categories_found")
        self.label_Categories_found.setGeometry(QRect(30, 10, 331, 51))
        font = QFont()
        font.setPointSize(25)
        self.label_Categories_found.setFont(font)
        self.pushButton_SaveCategoriesFound = QPushButton(Form_CategoriesFound)
        self.pushButton_SaveCategoriesFound.setObjectName(u"pushButton_SaveCategoriesFound")
        self.pushButton_SaveCategoriesFound.setGeometry(QRect(150, 250, 101, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_SaveCategoriesFound.setFont(font1)
        self.pushButton_CloseCategoriesFound = QPushButton(Form_CategoriesFound)
        self.pushButton_CloseCategoriesFound.setObjectName(u"pushButton_CloseCategoriesFound")
        self.pushButton_CloseCategoriesFound.setGeometry(QRect(270, 250, 101, 31))
        self.pushButton_CloseCategoriesFound.setFont(font1)
        self.listWidget_CategoriesFound = QListWidget(Form_CategoriesFound)
        self.listWidget_CategoriesFound.setObjectName(u"listWidget_CategoriesFound")
        self.listWidget_CategoriesFound.setGeometry(QRect(30, 70, 341, 161))
        self.pushButton_RemoveCategory = QPushButton(Form_CategoriesFound)
        self.pushButton_RemoveCategory.setObjectName(u"pushButton_RemoveCategory")
        self.pushButton_RemoveCategory.setGeometry(QRect(30, 250, 101, 31))
        self.pushButton_RemoveCategory.setFont(font1)

        self.retranslateUi(Form_CategoriesFound)

        QMetaObject.connectSlotsByName(Form_CategoriesFound)
    # setupUi

    def retranslateUi(self, Form_CategoriesFound):
        Form_CategoriesFound.setWindowTitle(QCoreApplication.translate("Form_CategoriesFound", u"Categories Found", None))
        self.label_Categories_found.setText(QCoreApplication.translate("Form_CategoriesFound", u"Categories found:", None))
        self.pushButton_SaveCategoriesFound.setText(QCoreApplication.translate("Form_CategoriesFound", u"Save All", None))
        self.pushButton_CloseCategoriesFound.setText(QCoreApplication.translate("Form_CategoriesFound", u"Close", None))
        self.pushButton_RemoveCategory.setText(QCoreApplication.translate("Form_CategoriesFound", u"Remove", None))
    # retranslateUi

