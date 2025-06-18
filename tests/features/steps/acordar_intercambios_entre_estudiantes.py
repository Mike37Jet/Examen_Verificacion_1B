from behave import *
from logic.Libro import Libro
from logic.Estudiante import Estudiante
from logic.Intercambio import Intercambio
from logic.Estado import Estado
from datetime import datetime, timedelta
from logic.Notificacion import Notificacion

use_step_matcher("re")


@step("que existe un acuerdo de intercambio de libros")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    libro1 = Libro(nombre="Cien años de soledad", autor="Gabriel García Márquez",
                   estudiante=Estudiante(nombre="Miguel"))
    libro2 = Libro(nombre="Orgullo y prejuicio", autor="Jane Austen", estudiante=Estudiante(nombre="Ana"))
    intercambio = Intercambio()

    fecha_futura = (datetime.now() + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
    intercambio.acordar_intercambio_libros(libro1, libro2, fecha=fecha_futura)

    context.libro1 = libro1
    context.libro2 = libro2
    context.intercambio = intercambio

    assert intercambio.estado == Estado.PENDIENTE


@step("es antes de 24 horas de la fecha de intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio
    fecha_restante = intercambio.calcular_fecha_restante()
    assert fecha_restante <= float(24)


@step("el estudiante confirma el intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio

    intercambio.confirmar_intercambio()

    assert intercambio.estado == Estado.CONFIRMADO


@step("se notificará al otro estudiante sobre la confirmación del intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio

    notificacion = Notificacion()
    notificacion.enviar_confirmacion(intercambio.obtener_estudiantes_involucrados())

    estudiantes = intercambio.obtener_estudiantes_involucrados()

    for estudiante in estudiantes:
        assert len(estudiante.notificaciones) > 0


@step("el estudiante no confirma el intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio

    # Verificar que el intercambio sigue en estado pendiente
    assert intercambio.estado == Estado.PENDIENTE

    # Simular que ha pasado el tiempo y la fecha de intercambio ya ocurrió
    fecha_pasada = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
    intercambio.fecha = fecha_pasada

    # Verificar que la fecha restante es negativa (ya pasó la fecha)
    fecha_restante = intercambio.calcular_fecha_restante()
    assert fecha_restante < 0

    # Opcionalmente, cambiar el estado a cancelado automáticamente
    intercambio.estado = Estado.CANCELADO




@step("se notificará al otro estudiante sobre la cancelación del intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    intercambio = context.intercambio

    notificacion = Notificacion()
    notificacion.enviar_cancelacion(intercambio.obtener_estudiantes_involucrados())

    estudiantes = intercambio.obtener_estudiantes_involucrados()

    for estudiante in estudiantes:
        assert len(estudiante.notificaciones) > 0