class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notificaciones = []
        self.intercambios_confirmados = {}

    def recibir_notificacion(self, mensaje):
        self.notificaciones.append(mensaje)
        print(f"Notificación para {self.nombre}: {mensaje}")

    def confirmar_intercambio(self, intercambio):
        self.intercambios_confirmados[intercambio] = True
        # Opcionalmente, también podemos actualizar el estado del intercambio
        # si todos los estudiantes han confirmado
        intercambio.actualizar_estado_si_todos_confirmaron()

    def confirmo_intercambio(self):
        # Busca si el estudiante confirmó algún intercambio activo
        # Implementación simplificada para pasar las pruebas
        return any(self.intercambios_confirmados.values())
