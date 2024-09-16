from proyect_venv.AppLista.Test.tarea import Tareas

def test_comprobar_si_agrega_una_tarea():
    app = Tareas()

    assert app.agregar("realizar trabajos") is True
    assert app.agregar("hacer la cama") is True


def test_agregar_tarea_existente():
    app = Tareas()
    app.agregar("tarea 1")

    assert app.agregar("tarea 1") is False

def test_tareas_completadas():
    app = Tareas()
    app.agregar("comprar ferreteria")
    app.agregar("ir a rosario")

    assert app.completar_tareas("comprar ferreteria") is True
    assert app.completar_tareas("ir a rosario") is True
    assert app.completar_tareas("comprar tomates") is False


def test_eliminar_tareas():
    app = Tareas()
    app.agregar("limpiar cuarto")
    app.agregar("lavar auto")

    assert app.eliminar_tarea("limpiar cuarto") is True
    assert app.eliminar_tarea("lavar auto") is True
