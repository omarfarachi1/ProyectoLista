from proyect_venv.AppLista.Test.tarea import tareas

def test_comprobar_si_agrega_una_tarea():
    app = tareas()

    assert app.agregar("realizar trabajos") is True
    assert app.agregar("hacer mates") is True


def test_agregar_tarea_existente():
    app = tareas()
    app.agregar("tarea 1")
    app.agregar("comprar facturas")

    assert app.agregar("tarea 1") is False
    assert app.agregar("comprar facturas") is False


def test_tareas_completadas():
    app = tareas()
    app.agregar("comprar ferreteria")
    app.agregar("ir a rosario")

    assert app.completar_tareas("comprar ferreteria") is True
    assert app.completar_tareas("ir a rosario") is True


def test_eliminar_tareas():
    app = tareas()
    app.agregar("limpiar cuarto")
    app.agregar("lavar auto")

    assert app.eliminar_tarea("limpiar cuarto") is True
    assert "limpiar cuarto" not in app.lista_tareas

    assert app.eliminar_tarea("lavar auto") is True
    assert "lavar auto" not in app.lista_tareas
