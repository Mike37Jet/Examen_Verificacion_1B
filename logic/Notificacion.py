class Notificacion:
    def __init__(self):
        pass

    def enviar_recordatorio(self, estudiantes):
        for estudiante in estudiantes:
            estudiante.recibir_notificacion("Tiene un intercambio pendiente programado en una fecha próxima.")

    def enviar_confirmacion(self, estudiantes):
        for estudiante in estudiantes:
            estudiante.recibir_notificacion("El intercambio ha sido confirmado por el otro estudiante.")

    def enviar_cancelacion(self, estudiantes):
        for estudiante in estudiantes:
            estudiante.recibir_notificacion("El intercambio ha sido cancelado porque el otro estudiante no confirmó.")
