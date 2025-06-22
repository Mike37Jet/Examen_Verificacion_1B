from logic import Estado
from datetime import datetime, timedelta


class Intercambio:
    def __init__(self):
        self.estado = None
        self.libro1 = None
        self.libro2 = None
        self.fecha = None

    def acordar_intercambio_libros(self, libro1, libro2, fecha):
        self.libro1 = libro1
        self.libro2 = libro2
        self.fecha = fecha
        self.estado = Estado.Estado.PENDIENTE

    def calcular_fecha_restante(self):
        fecha_actual = datetime.now()
        fecha_intercambio = datetime.strptime(self.fecha, "%Y-%m-%d %H:%M:%S")
        return (fecha_intercambio - fecha_actual).total_seconds() / 3600

    def obtener_estudiantes_involucrados(self):
        return [self.libro1.obtener_estudiante(), self.libro2.obtener_estudiante()]

    def confirmar_intercambio(self):
        if self.estado == Estado.Estado.PENDIENTE:
            self.estado = Estado.Estado.CONFIRMADO
        else:
            raise ValueError("El intercambio no está en estado pendiente para confirmar.")


    def verificar_confirmacion_intercambio(self):
        if self.estado == Estado.Estado.PENDIENTE:
            fecha_actual = datetime.now()
            fecha_intercambio = datetime.strptime(self.fecha, "%Y-%m-%d %H:%M:%S")

            if fecha_actual > fecha_intercambio:
                estudiante1 = self.libro1.obtener_estudiante()
                estudiante2 = self.libro2.obtener_estudiante()

                if not estudiante1.confirmo_intercambio() or not estudiante2.confirmo_intercambio():
                    self.estado = Estado.Estado.CANCELADO
                else:
                    self.estado = Estado.Estado.CONFIRMADO

        return self.estado

    def obtener_estado(self):
        return self.estado

    def actualizar_estado_si_todos_confirmaron(self):
        estudiantes = self.obtener_estudiantes_involucrados()
        if all(estudiante.confirmo_intercambio() for estudiante in estudiantes):
            self.estado = Estado.Estado.CONFIRMADO
        else:
            self.estado = Estado.Estado.PENDIENTE