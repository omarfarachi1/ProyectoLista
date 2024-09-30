class Tareas:
    def __init__(self):
        self.__lista_tareas = []

    def agregartarea(self, texto):
        if texto in self.__lista_tareas:
            return False
        else:
            self.__lista_tareas.append(texto)
            return True

    def completartareas(self, texto):
        if texto in self.__lista_tareas:
            print("Tarea completada")
            return True
        else:
            return False

    def listadetareas(self):
        return self.__lista_tareas

    def eliminarTarea(self, texto):
        if texto in self.__lista_tareas:
            self.__lista_tareas.remove(texto)
            return True
        else:
            return False