class Notificacion:
    def __init__(self):
        pass

    def enviar_recordatorio_de_intercambio(self, estudiantes, intercambio=None):
                if intercambio:
                    participantes = intercambio.obtener_estudiantes_involucrados()
                    libro1 = intercambio.libro1
                    libro2 = intercambio.libro2
                    fecha = intercambio.fecha

                    for estudiante in estudiantes:
                        otro_estudiante = next(p for p in participantes if p.nombre != estudiante.nombre)

                        if estudiante == libro1.obtener_estudiante():
                            libro_entrega = libro1.nombre
                            libro_recibe = libro2.nombre
                        else:
                            libro_entrega = libro2.nombre
                            libro_recibe = libro1.nombre

                        mensaje = (f"Tiene un intercambio pendiente con {otro_estudiante.nombre} programado para el {fecha}. "
                                  f"Usted entregará '{libro_entrega}' y recibirá '{libro_recibe}'.")

                        estudiante.recibir_notificacion(mensaje)
                else:
                    for estudiante in estudiantes:
                        estudiante.recibir_notificacion("Tiene un intercambio pendiente programado en una fecha próxima.")

    def enviar_confirmacion(self, estudiantes):
        for estudiante in estudiantes:
            estudiante.recibir_notificacion("El intercambio ha sido confirmado por el otro estudiante.")

    def enviar_cancelacion(self, estudiantes, intercambio=None):
                if intercambio:
                    no_confirmados = []
                    for estudiante in intercambio.obtener_estudiantes_involucrados():
                        if not estudiante.confirmo_intercambio():
                            no_confirmados.append(estudiante.nombre)

                    if no_confirmados:
                        nombres = ", ".join(no_confirmados)
                        mensaje = f"El intercambio ha sido cancelado por la falta de confirmación de {nombres}."
                    else:
                        mensaje = "El intercambio ha sido cancelado por falta de confirmación."
                else:
                    mensaje = "El intercambio ha sido cancelado porque el otro estudiante no confirmó."

                for estudiante in estudiantes:
                    estudiante.recibir_notificacion(mensaje)
