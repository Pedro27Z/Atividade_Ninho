# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 719)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(12)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 25))
        self.btn_pg_cadastro.setMaximumSize(QSize(150, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_pg_cadastro)

        self.btn_pg_import = QPushButton(self.centralwidget)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setMinimumSize(QSize(0, 25))
        self.btn_pg_import.setFont(font)
        self.btn_pg_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_pg_import)

        self.btn_fornecedores = QPushButton(self.centralwidget)
        self.btn_fornecedores.setObjectName(u"btn_fornecedores")
        self.btn_fornecedores.setMinimumSize(QSize(0, 25))
        self.btn_fornecedores.setFont(font)
        self.btn_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fornecedores.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_fornecedores)

        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 25))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.centralwidget)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 25))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pg_fornecedores = QWidget()
        self.pg_fornecedores.setObjectName(u"pg_fornecedores")
        self.verticalLayout_8 = QVBoxLayout(self.pg_fornecedores)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_fornecedores)
        self.tabWidget.setObjectName(u"tabWidget")
        self.pg_fornecedores_2 = QWidget()
        self.pg_fornecedores_2.setObjectName(u"pg_fornecedores_2")
        self.verticalLayout_7 = QVBoxLayout(self.pg_fornecedores_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.pg_fornecedores_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.table_fornec = QTableWidget(self.pg_fornecedores_2)
        if (self.table_fornec.columnCount() < 11):
            self.table_fornec.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_fornec.setObjectName(u"table_fornec")

        self.verticalLayout_5.addWidget(self.table_fornec)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame = QFrame(self.pg_fornecedores_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar_excel = QPushButton(self.frame)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(100, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_gerar_excel.setFont(font2)
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gerar_excel)

        self.btn_alterar_for = QPushButton(self.frame)
        self.btn_alterar_for.setObjectName(u"btn_alterar_for")
        self.btn_alterar_for.setMinimumSize(QSize(100, 25))
        self.btn_alterar_for.setFont(font2)
        self.btn_alterar_for.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_for.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_alterar_for)

        self.btn_excluir_for = QPushButton(self.frame)
        self.btn_excluir_for.setObjectName(u"btn_excluir_for")
        self.btn_excluir_for.setMinimumSize(QSize(100, 25))
        self.btn_excluir_for.setFont(font2)
        self.btn_excluir_for.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_for.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_excluir_for)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.pg_fornecedores_2, "")
        self.pg_cadfornecedores = QWidget()
        self.pg_cadfornecedores.setObjectName(u"pg_cadfornecedores")
        self.verticalLayout_11 = QVBoxLayout(self.pg_cadfornecedores)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_17 = QLabel(self.pg_cadfornecedores)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.label_17)

        self.frame_2 = QFrame(self.pg_cadfornecedores)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_cnpj_contr = QLineEdit(self.frame_2)
        self.txt_cnpj_contr.setObjectName(u"txt_cnpj_contr")
        self.txt_cnpj_contr.setMinimumSize(QSize(0, 25))
        self.txt_cnpj_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cnpj_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj_contr, 4, 0, 1, 1)

        self.txt_nome_contr = QLineEdit(self.frame_2)
        self.txt_nome_contr.setObjectName(u"txt_nome_contr")
        self.txt_nome_contr.setMinimumSize(QSize(0, 25))
        self.txt_nome_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_nome_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome_contr, 4, 1, 1, 2)

        self.txt_logradouro_contr = QLineEdit(self.frame_2)
        self.txt_logradouro_contr.setObjectName(u"txt_logradouro_contr")
        self.txt_logradouro_contr.setMinimumSize(QSize(0, 25))
        self.txt_logradouro_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_logradouro_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro_contr, 5, 0, 1, 3)

        self.txt_num_contr = QLineEdit(self.frame_2)
        self.txt_num_contr.setObjectName(u"txt_num_contr")
        self.txt_num_contr.setMinimumSize(QSize(0, 25))
        self.txt_num_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_num_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_num_contr, 6, 0, 1, 1)

        self.txt_complemento_contr = QLineEdit(self.frame_2)
        self.txt_complemento_contr.setObjectName(u"txt_complemento_contr")
        self.txt_complemento_contr.setMinimumSize(QSize(0, 25))
        self.txt_complemento_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_complemento_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento_contr, 6, 1, 1, 1)

        self.txt_cep_contr = QLineEdit(self.frame_2)
        self.txt_cep_contr.setObjectName(u"txt_cep_contr")
        self.txt_cep_contr.setMinimumSize(QSize(0, 25))
        self.txt_cep_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cep_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep_contr, 7, 2, 1, 1)

        self.txt_telefone_contr = QLineEdit(self.frame_2)
        self.txt_telefone_contr.setObjectName(u"txt_telefone_contr")
        self.txt_telefone_contr.setMinimumSize(QSize(0, 25))
        self.txt_telefone_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_telefone_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone_contr, 9, 0, 1, 1)

        self.txt_bairro_contr = QLineEdit(self.frame_2)
        self.txt_bairro_contr.setObjectName(u"txt_bairro_contr")
        self.txt_bairro_contr.setMinimumSize(QSize(0, 25))
        self.txt_bairro_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.txt_bairro_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro_contr, 6, 2, 1, 1)

        self.txt_municipio_contr = QLineEdit(self.frame_2)
        self.txt_municipio_contr.setObjectName(u"txt_municipio_contr")
        self.txt_municipio_contr.setMinimumSize(QSize(0, 25))
        self.txt_municipio_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_municipio_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio_contr, 7, 0, 1, 1)

        self.txt_uf_contr = QLineEdit(self.frame_2)
        self.txt_uf_contr.setObjectName(u"txt_uf_contr")
        self.txt_uf_contr.setMinimumSize(QSize(0, 25))
        self.txt_uf_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_uf_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf_contr, 7, 1, 1, 1)

        self.txt_email_contr = QLineEdit(self.frame_2)
        self.txt_email_contr.setObjectName(u"txt_email_contr")
        self.txt_email_contr.setMinimumSize(QSize(0, 25))
        self.txt_email_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_email_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email_contr, 9, 1, 1, 2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 27))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.btn_cadforn = QPushButton(self.frame_2)
        self.btn_cadforn.setObjectName(u"btn_cadforn")
        self.btn_cadforn.setMinimumSize(QSize(0, 25))
        self.btn_cadforn.setMaximumSize(QSize(300, 28))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_cadforn.setFont(font3)
        self.btn_cadforn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadforn.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadforn.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.gridLayout.addWidget(self.btn_cadforn, 10, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.tabWidget.addTab(self.pg_cadfornecedores, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_fornecedores)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.verticalLayout.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_cad_produto = QWidget()
        self.pg_cad_produto.setObjectName(u"pg_cad_produto")
        self.verticalLayout_10 = QVBoxLayout(self.pg_cad_produto)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.pg_cad_produto)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_10.addWidget(self.label_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(350, -1, 350, -1)
        self.label_25 = QLabel(self.pg_cad_produto)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_25)

        self.txt_cod = QLineEdit(self.pg_cad_produto)
        self.txt_cod.setObjectName(u"txt_cod")
        self.txt_cod.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setPointSize(10)
        self.txt_cod.setFont(font4)
        self.txt_cod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_11.addWidget(self.txt_cod)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(250, -1, 250, -1)
        self.label_26 = QLabel(self.pg_cad_produto)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_26)

        self.txt_descricao = QLineEdit(self.pg_cad_produto)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setMinimumSize(QSize(0, 25))
        self.txt_descricao.setFont(font4)
        self.txt_descricao.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_12.addWidget(self.txt_descricao)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(300, -1, 250, -1)
        self.label_27 = QLabel(self.pg_cad_produto)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_27)

        self.txt_valor = QLineEdit(self.pg_cad_produto)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setMinimumSize(QSize(0, 25))
        self.txt_valor.setFont(font4)
        self.txt_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_valor.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_13.addWidget(self.txt_valor)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(250, -1, 250, -1)
        self.label_28 = QLabel(self.pg_cad_produto)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_28)

        self.txt_quantidade = QLineEdit(self.pg_cad_produto)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setMinimumSize(QSize(0, 25))
        self.txt_quantidade.setMaximumSize(QSize(16777215, 16777215))
        self.txt_quantidade.setFont(font4)
        self.txt_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_quantidade.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_14.addWidget(self.txt_quantidade)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.cb_categoria = QComboBox(self.pg_cad_produto)
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.setObjectName(u"cb_categoria")
        self.cb_categoria.setMinimumSize(QSize(100, 20))
        self.cb_categoria.setMaximumSize(QSize(150, 25))
        self.cb_categoria.setFont(font1)
        self.cb_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_categoria.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.cb_categoria)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_29 = QLabel(self.pg_cad_produto)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_15.addWidget(self.label_29)

        self.btn_cad_produtos = QPushButton(self.pg_cad_produto)
        self.btn_cad_produtos.setObjectName(u"btn_cad_produtos")
        self.btn_cad_produtos.setMinimumSize(QSize(0, 25))
        self.btn_cad_produtos.setMaximumSize(QSize(150, 30))
        self.btn_cad_produtos.setFont(font2)
        self.btn_cad_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_produtos.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius:15px}\n"
"\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_cad_produtos)

        self.label_30 = QLabel(self.pg_cad_produto)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_15.addWidget(self.label_30)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.Pages.addWidget(self.pg_cad_produto)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, 50, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 25))
        self.txt_nome.setFont(font4)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(0, 25))
        self.txt_usuario.setFont(font4)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setFont(font4)
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, 50, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txt_confirmar = QLineEdit(self.pg_cadastro)
        self.txt_confirmar.setObjectName(u"txt_confirmar")
        self.txt_confirmar.setMinimumSize(QSize(0, 25))
        self.txt_confirmar.setMaximumSize(QSize(16777215, 16777215))
        self.txt_confirmar.setFont(font4)
        self.txt_confirmar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_confirmar.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_confirmar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(750, 0, 50, 0)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setMaximumSize(QSize(50, 100))
        self.label_11.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setMinimumSize(QSize(100, 20))
        self.cb_perfil.setMaximumSize(QSize(150, 25))
        self.cb_perfil.setFont(font1)
        self.cb_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 25))
        self.btn_cadastrar.setMaximumSize(QSize(150, 30))
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius:15px}\n"
"\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_23 = QLabel(self.pg_contato)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_13.addWidget(self.label_23)

        self.label_14 = QLabel(self.pg_contato)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setPointSize(20)
        self.label_14.setFont(font6)

        self.verticalLayout_13.addWidget(self.label_14)

        self.label_19 = QLabel(self.pg_contato)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_13.addWidget(self.label_21)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.pg_sobre)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 200))
        self.label_15.setFont(font6)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_18 = QLabel(self.pg_sobre)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setBold(False)
        self.label_18.setFont(font7)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_22 = QLabel(self.pg_sobre)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_12.addWidget(self.label_22)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.btn_cadforn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"PRODUTOS", None))
        self.btn_fornecedores.setText(QCoreApplication.translate("MainWindow", u"FORNECEDORES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Fornecedores</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_fornec.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.table_fornec.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.table_fornec.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.table_fornec.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.table_fornec.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.table_fornec.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.table_fornec.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.table_fornec.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.table_fornec.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.table_fornec.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.table_fornec.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_for.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_for.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_fornecedores_2), QCoreApplication.translate("MainWindow", u"Lista de Fornecedores", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CADASTRAR FORNECEDOR</span></p></body></html>", None))
        self.txt_cnpj_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.txt_logradouro_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_num_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_complemento_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_cep_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_bairro_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_municipio_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_uf_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_email_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">FORNECEDOR</span></p></body></html>", None))
        self.btn_cadforn.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_cadfornecedores), QCoreApplication.translate("MainWindow", u"Cadastrar Fornecedor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imags/logo_system\"/></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Sistema de Cadastro</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Cadastro de Produto</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Cod:</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Valor:</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Quantidade:</span></p></body></html>", None))
        self.txt_quantidade.setText("")
        self.cb_categoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Informatica", None))
        self.cb_categoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Eletronicos", None))
        self.cb_categoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Alimentos", None))
        self.cb_categoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Moda", None))

        self.label_29.setText("")
        self.btn_cad_produtos.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_30.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Confirmar Senha:</span></p></body></html>", None))
        self.txt_confirmar.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_23.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/18014190591582545595-64.png\"/></p><p align=\"center\">Contatos de Suporte</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/11968623911579738440-32.png\"/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">(85)99999-9999</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/15743770351574338605-32.png\"/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">suportcad@gmail.com</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">O sistema de cadastro \u00e9 uma solu\u00e7\u00e3o pr\u00e1tica e eficiente para empresas que precisam gerenciar seus usu\u00e1rios, cadastrando seus produtos e fornecedores no banco de dados postgresql de forma segura, centralizada e organizada. </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Com a ajuda da API, a integra\u00e7\u00e3o com outras ferramentas e sistemas \u00e9 facilitada, o que pode trazer ainda mais benef\u00edcios para a empresa.</span></p></body></html>", None))
        self.label_22.setText("")
    # retranslateUi

