class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar(self, texto):
        if texto not in self.lista_tareas:
            self.lista_tareas.append(texto)
            return True
        return False

    def completar_tareas(self, texto):
        if texto in self.lista_tareas:
            print("Tarea completada")
            return True
        else:
            print("La tarea no existe. Tarea no completada")
            return False

    def __listadetareas(self):
        return self.lista_tareas


    def eliminar_tarea(self, texto):
        if texto in self.lista_tareas:
            self.lista_tareas.remove(texto)
        else:
            return False
        return True