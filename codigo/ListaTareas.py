import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QMessageBox)

from PySide6.QtCore import Qt, QAbstractTableModel


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

        self.botonEliminar = QPushButton("Eliminar")
        layout.addWidget(self.botonEliminar)
        self.botonEliminar.clicked.connect(self.Eliminar)


    def Agregar(self):
        lista = self.entrada.text()
        self.list_Tareas.append(lista)
        print(self.list_Tareas)

    def Eliminar(self, indice):
        if indice < len(self.list_Tareas):
            del self.list_Tareas[indice]
        QMessageBox.information(self, "Tarea finalizada", "Se eliminaron las tareas")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = ListadodeTareas("Lista de Tareas")
    Window.Ui()
    Window.setWindowTitle("Lista de Tareas")
    Window.setGeometry(100, 300, 300, 300)
    Window.show()
    sys.exit(app.exec())
