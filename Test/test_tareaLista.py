from proyect_venv.AppLista.Test.tarea import Tareas

def test_comprobar_si_agrega_una_tarea():
    app = Tareas()

    assert app.agregar("realizar trabajos")
    assert app.agregar("hacer la cama")

def test_no_agregar_tarea_existente():
    app = Tareas()

    assert app.agregar("tarea 1")
    assert app.agregar("tarea 2")

def test_tareas_completadas():
    app = Tareas()
    app.agregar("comprar ferreteria")
    app.agregar("ir a rosario")

    assert app.completarTareas("comprar ferreteria")
    assert app.completarTareas("ir a rosario")
    assert app.completarTareas("comprar tomates") is False


def test_eliminar_tareas():
    app = Tareas()
    app.agregar("limpiar cuarto")

    assert app.eliminarTarea("limpiar cuarto")
    assert app.eliminarTarea("lavar auto") is False
