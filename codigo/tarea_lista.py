import sys
from proyect_venv.AppLista.Uic_pruebas.VentanaLista import Ui_ListaTareas
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)

class ListTareas(QMainWindow, Ui_ListaTareas):
    def __init__(self):
        super().__init__()
        self.lista_tareas = []
        self.setupUi(self)
        self.retranslateUi(self)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_marcarcomple.clicked.connect(self.marcarcompletada)
        self.btn_eliminar.clicked.connect(self.eliminar)


    def agregar(self):
        lista_entrada = self.entrada.text()
        self.lista_tareas.append({"Tareas": lista_entrada, "Estado": ""})
        self.actualizar()


    def marcarcompletada(self):
        for i in self.lista_tareas:
            i["Estado"] = "Completado"
        self.actualizar()
        QMessageBox.information(self, "Tarea finalizada", "La tarea ha sido marcada como completada")


    def eliminar(self):
        self.lista_tareas.clear()
        self.actualizar()


    def actualizar(self):
        self.ventanalist.setRowCount(0)
        for i, x in enumerate(self.lista_tareas):
            self.ventanalist.insertRow(i)
            self.ventanalist.setItem(i, 0, QTableWidgetItem(x["Tareas"]))
            self.ventanalist.setItem(i, 1, QTableWidgetItem(x["Estado"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = ListTareas()
    Window.show()
    sys.exit(app.exec())