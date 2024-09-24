from proyect_venv.AppLista.Test.tarea import Tareas

def test_comprobar_si_agrega_una_tarea():
    app = Tareas()
    tarea = "realizar trabajos"
    app.agregar(tarea)

    assert tarea in app.lista_tareas

def test_no_agregar_tarea_existente():
    app = Tareas()
    tarea1 = "tarea 1"
    app.agregar(tarea1)

    assert not app.agregar(tarea1)

def test_tareas_completadas():
    app = Tareas()
    tarea2 = "comprar ferreteria"
    app.agregar(tarea2)

    assert app.completarTareas(tarea2)

def test_eliminar_tareas():
    app = Tareas()
    tarea = "limpiar cuarto"
    app.agregar(tarea)
    app.eliminarTarea(tarea)

    assert tarea not in app.lista_tareas
