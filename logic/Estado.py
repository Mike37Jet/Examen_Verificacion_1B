from enum import Enum

class Estado(Enum):
    PENDIENTE = "Pendiente"
    COMPLETADO = "Completado"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"

    @staticmethod
    def es_valido(estado):
        return estado in (Estado.PENDIENTE, Estado.COMPLETADO, Estado.CANCELADO)