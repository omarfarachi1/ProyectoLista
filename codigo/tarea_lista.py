import sys
from proyect_venv.AppLista.Uic.VentanaLista import Ui_ListaTareas
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)

class ListTareas(QMainWindow, Ui_ListaTareas):
    def __init__(self):
        super().__init__()
        self.lista_tareas = []
        self.setupUi(self)
        self.retranslateUi(self)
        self.Btn_Agregar.clicked.connect(self.Agregar)
        self.Btn_MarcarComple.clicked.connect(self.MarcarCompletada)
        self.Btn_Eliminar.clicked.connect(self.Eliminar)


    def Agregar(self, lista_entrada):
        lista_entrada = self.entrada.text()
        self.lista_tareas.append({"Tareas": lista_entrada, "Estado": ""})
        self.Actualizar()


    def MarcarCompletada(self):
        for i in self.lista_tareas:
            i["Estado"] = "Completado"
        self.Actualizar()
        QMessageBox.information(self, "Tarea finalizada", "La tarea ha sido marcada como completada")


    def Eliminar(self):
        self.lista_tareas.clear()
        self.Actualizar()


    def Actualizar(self):
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