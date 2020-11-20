# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(826, 456)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 4, 15, 1)

        self.spinBox_11 = QSpinBox(self.groupBox_2)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_11, 4, 3, 1, 1)

        self.spinBox_13 = QSpinBox(self.groupBox_2)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_13, 1, 3, 1, 1)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 6, 0, 1, 2)

        self.spinBox_16 = QSpinBox(self.groupBox_2)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_16, 2, 3, 1, 1)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 8, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 2)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 7, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 3, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox_2)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_10, 8, 3, 1, 1)

        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 2, 0, 1, 2)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 2)

        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 5, 0, 1, 2)

        self.spinBox_14 = QSpinBox(self.groupBox_2)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_14, 9, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 4, 0, 1, 2)

        self.spinBox_15 = QSpinBox(self.groupBox_2)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_15, 3, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 2)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 9, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox_2)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_9, 7, 3, 1, 1)

        self.ordenar_id_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.gridLayout.addWidget(self.ordenar_id_pushButton, 11, 3, 1, 1)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.gridLayout.addWidget(self.ordenar_distancia_pushButton, 12, 3, 1, 1)

        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.gridLayout.addWidget(self.ordenar_velocidad_pushButton, 13, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 11, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 11, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 13, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 4)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 3, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 2)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_5.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Capturador de part\u00edculas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Color (rgb):", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar ", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
    # retranslateUi

