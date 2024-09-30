from proyect_venv.applista.Test.tarea import Tareas

def test_comprobar_si_agrega_una_tarea():
    app = Tareas()
    lista = app.listadetareas()
    tarea = "realizar trabajos"
    app.agregartarea(tarea)

    assert tarea in lista

def test_no_agregar_tarea_existente():
    app = Tareas()
    tarea1 = "tarea 1"
    app.agregartarea(tarea1)

    assert not app.agregartarea(tarea1)

def test_tareas_completadas():
    app = Tareas()
    tarea2 = "comprar ferreteria"
    app.agregartarea(tarea2)

    assert app.completartareas(tarea2)

def test_eliminar_tareas():
    app = Tareas()
    lista = app.listadetareas()
    tarea = "limpiar cuarto"
    app.agregartarea(tarea)
    app.eliminarTarea(tarea)

    assert tarea not in lista