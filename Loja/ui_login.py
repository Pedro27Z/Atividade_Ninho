# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(403, 416)
        Login.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 190, 271, 141))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(10, 20, 251, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(10, 60, 251, 31))
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(80, 100, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"		\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius:15px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	border-width: 2px;\n"
"	\n"
"}")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 350, 141, 31))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 80, 131, 121))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u"imags/66a1a4a22e271ec3ee3ef35ba0883ca4-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText("")
    # retranslateUi

