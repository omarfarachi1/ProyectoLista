class tareas:
    def __init__(self):
        self.lista_tareas = []
        self.lista_tareas_completadas = []

    def agregar(self, texto):
        if texto not in self.lista_tareas:
            self.lista_tareas.append(texto)
            return True
        return False

    def completar_tareas(self, texto):
        if texto in self.lista_tareas:
            self.lista_tareas.remove(texto)
            self.lista_tareas_completadas.append(texto)
            return True
        else:
            return False

    def tareas_pendientes(self):
        return self.lista_tareas

    def tareas_completadas(self):
        return self.lista_tareas_completadas

    def eliminar_tarea(self, texto):
        if texto in self.lista_tareas:
            self.lista_tareas.remove(texto)
        elif texto in self.lista_tareas_completadas:
            self.lista_tareas_completadas.remove(texto)
        else:
            return False
        return True