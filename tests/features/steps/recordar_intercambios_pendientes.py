from datetime import datetime, timedelta

from behave import *
from logic.Libro import Libro
from logic.Estudiante import Estudiante
from logic.Intercambio import Intercambio
from logic.Estado import Estado
from logic.Notificacion import Notificacion

use_step_matcher("re")


@step("que existe un intercambio pendiente programado en una fecha")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    libro1 = Libro(nombre="Cien años de soledad", autor="Gabriel García Márquez",
                   estudiante=Estudiante(nombre="Miguel"))
    libro2 = Libro(nombre="Orgullo y prejuicio", autor="Jane Austen", estudiante=Estudiante(nombre="Ana"))
    intercambio = Intercambio()

    fecha_futura = (datetime.now() + timedelta(hours=48)).strftime("%Y-%m-%d %H:%M:%S")
    intercambio.acordar_intercambio_libros(libro1, libro2, fecha=fecha_futura)

    context.libro1 = libro1
    context.libro2 = libro2
    context.intercambio = intercambio

    assert intercambio.estado == Estado.PENDIENTE


@step("la fecha del intercambio sea mayor a 24 horas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio
    fecha_restante = intercambio.calcular_fecha_restante()
    assert fecha_restante > float(24)



@step("se enviará un recordatorio a los estudiantes involucrados sobre el intercambio pendiente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio

    notificacion = Notificacion()
    notificacion.enviar_recordatorio_de_intercambio(intercambio.obtener_estudiantes_involucrados(), intercambio)
    estudiantes = intercambio.obtener_estudiantes_involucrados()

    for estudiante in estudiantes:
        assert len(estudiante.notificaciones) > 0

