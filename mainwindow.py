from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador_particulas import Administrador
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administrador_particulas = Administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_agregar)
        self.ui.pushButton_3.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_4.clicked.connect(self.click_mostrar)
        
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)

    
    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.administrador_particulas))

    @Slot()
    def click_agregar(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

        particula = Particula(id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.administrador_particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )
        
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administrador_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.administrador_particulas:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenx_widget)
                self.ui.tabla.setItem(0, 2, origeny_widget)
                self.ui.tabla.setItem(0, 3, destinox_widget)
                self.ui.tabla.setItem(0, 4, destinoy_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención!",
                f'La particula con id "{id}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.administrador_particulas))

        row = 0
        for particula in self.administrador_particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenx_widget)
            self.ui.tabla.setItem(row, 2, origeny_widget)
            self.ui.tabla.setItem(row, 3, destinox_widget)
            self.ui.tabla.setItem(row, 4, destinoy_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.administrador_particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r, g, b)
            pen.setColor(color)

            origenx = particula.origenx
            origeny = particula.origeny
            destinox = particula.destinox
            destinoy = particula.destinoy

            self.scene.addEllipse(origenx, origeny, 3, 3, pen)
            self.scene.addEllipse(destinox, destinoy, 3, 3, pen)
            self.scene.addLine(origenx+3, origeny+3, destinox, destinoy, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear() 

    @Slot()
    def ordenar_id(self):
        self.administrador_particulas.sort_by_id()
    
    @Slot()
    def ordenar_distancia(self):
        self.administrador_particulas.sort_by_distancia()

    @Slot()
    def ordenar_velocidad(self):
        self.administrador_particulas.sort_by_velocidad()