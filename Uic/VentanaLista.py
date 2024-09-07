# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaLista.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_ListaTareas(object):
    def setupUi(self, ListaTareas):
        if not ListaTareas.objectName():
            ListaTareas.setObjectName(u"ListaTareas")
        ListaTareas.resize(800, 600)
        self.centralwidget = QWidget(ListaTareas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Btn_Agregar = QPushButton(self.centralwidget)
        self.Btn_Agregar.setObjectName(u"Btn_Agregar")
        self.Btn_Agregar.setGeometry(QRect(310, 130, 75, 24))
        self.Btn_MarcarComple = QPushButton(self.centralwidget)
        self.Btn_MarcarComple.setObjectName(u"Btn_MarcarComple")
        self.Btn_MarcarComple.setGeometry(QRect(270, 180, 171, 24))
        self.Btn_Eliminar = QPushButton(self.centralwidget)
        self.Btn_Eliminar.setObjectName(u"Btn_Eliminar")
        self.Btn_Eliminar.setGeometry(QRect(310, 220, 75, 24))
        self.entrada = QLineEdit(self.centralwidget)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(290, 90, 113, 22))
        self.ventanalist = QTableWidget(self.centralwidget)
        if (self.ventanalist.columnCount() < 2):
            self.ventanalist.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.ventanalist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ventanalist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.ventanalist.setObjectName(u"ventanalist")
        self.ventanalist.setGeometry(QRect(220, 270, 256, 192))
        ListaTareas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ListaTareas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        ListaTareas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ListaTareas)
        self.statusbar.setObjectName(u"statusbar")
        ListaTareas.setStatusBar(self.statusbar)

        self.retranslateUi(ListaTareas)
        self.Btn_Eliminar.clicked.connect(self.entrada.clear)

        QMetaObject.connectSlotsByName(ListaTareas)
    # setupUi

    def retranslateUi(self, ListaTareas):
        ListaTareas.setWindowTitle(QCoreApplication.translate("ListaTareas", u"MainWindow", None))
        self.Btn_Agregar.setText(QCoreApplication.translate("ListaTareas", u"Agregar", None))
        self.Btn_MarcarComple.setText(QCoreApplication.translate("ListaTareas", u"Marcar como completada", None))
        self.Btn_Eliminar.setText(QCoreApplication.translate("ListaTareas", u"Eliminar", None))
        ___qtablewidgetitem = self.ventanalist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListaTareas", u"Tareas", None));
        ___qtablewidgetitem1 = self.ventanalist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListaTareas", u"Estado", None));
    # retranslateUi

