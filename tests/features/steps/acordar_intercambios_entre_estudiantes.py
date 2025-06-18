from behave import *

use_step_matcher("re")


@step("que existe un acuerdo de intercambio de libros")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que existe un acuerdo de intercambio de libros')


@step("es antes de 24 horas de la fecha de intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y es antes de 24 horas de la fecha de intercambio')


@step("el estudiante confirma el intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el estudiante confirma el intercambio')


@step('se actualizará el estado del intercambio a "Confirmado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se actualizará el estado del intercambio a "Confirmado"')


@step("se notificará al otro estudiante sobre la confirmación del intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se notificará al otro estudiante sobre la confirmación del intercambio')


@step("el estudiante no confirma el intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el estudiante no confirma el intercambio')


@step("se notificará al otro estudiante sobre la cancelación del intercambio")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se notificará al otro estudiante sobre la cancelación del intercambio')


@step('se actualizará el estado del intercambio a "Cancelado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se actualizará el estado del intercambio a "Cancelado"')