import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QMessageBox)


class ListadodeTareas(QMainWindow):
    def __init__(self, texto):
        super().__init__()
        self.texto = texto
        self.list_Tareas = []


    def Ui(self):
        self.window = QWidget()
        self.setCentralWidget(self.window)

        layout = QVBoxLayout()
        self.window.setLayout(layout)

        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)

        self.botonAgregar = QPushButton("Agregar")
        layout.addWidget(self.botonAgregar)
        self.botonAgregar.clicked.connect(self.Agregar)

        self.botonMarcar = QPushButton("Marcar como completada")
        layout.addWidget(self.botonMarcar)
        self.botonMarcar.clicked.connect(self.MarcarCompletada)

        self.botonEliminar = QPushButton("Eliminar")
        layout.addWidget(self.botonEliminar)
        self.botonEliminar.clicked.connect(self.Eliminar)

        self.widget_tabla = QTableWidget()
        layout.addWidget(self.widget_tabla)
        self.widget_tabla.setColumnCount(2)
        self.widget_tabla.setHorizontalHeaderItem(0, QTableWidgetItem("Tarea"))
        self.widget_tabla.setHorizontalHeaderItem(1, QTableWidgetItem("Estado"))


    def Agregar(self):
        lista_entrada = self.entrada.text()
        self.list_Tareas.append({"Tarea": lista_entrada, "Estado": "pendiente"})
        self.Actualizar()

    def Eliminar(self):
        self.list_Tareas.clear()
        self.Actualizar()


    def MarcarCompletada(self, row):
        for i in self.list_Tareas:
            i["Estado"] = "Completada"
        self.Actualizar()
        QMessageBox.information(self, "Tarea finalizada", "La tarea ha sido marcada como completada")


    def Actualizar(self):
        self.widget_tabla.setRowCount(0)
        for i, x in enumerate(self.list_Tareas):
            self.widget_tabla.insertRow(i)
            self.widget_tabla.setItem(i, 0, QTableWidgetItem(x["Tarea"]))
            self.widget_tabla.setItem(i, 1,  QTableWidgetItem(x["Estado"]))
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = ListadodeTareas("Lista de Tareas")
    Window.Ui()
    Window.setWindowTitle("Lista de Tareas")
    Window.setGeometry(100, 300, 300, 300)
    Window.show()
    sys.exit(app.exec())
