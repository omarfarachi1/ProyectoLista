class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar(self, texto):
        if texto in self.lista_tareas:
            return False
        else:
            self.lista_tareas.append(texto)
            return True

    def completarTareas(self, texto):
        if texto in self.lista_tareas:
            print("Tarea completada")
            return True
        else:
            return False


    def __listadetareas(self):
        return self.lista_tareas


    def eliminarTarea(self, texto):
        if texto in self.lista_tareas:
            self.lista_tareas.remove(texto)
            return True
        else:
            return False
