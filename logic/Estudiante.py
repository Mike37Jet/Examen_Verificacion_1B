class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notificaciones = []

    def recibir_notificacion(self, mensaje):
        self.notificaciones.append(mensaje)
        print(f"Notificación para {self.nombre}: {mensaje}")

