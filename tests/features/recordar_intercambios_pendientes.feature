# Created by migue at 18/6/2025
# language: es
Característica: Recordar intercambios pendientes
  Como estudiante
  Quiero recibir recordatorios de los intercambios pendientes
  Para evitar el olvido de los intercambios programados

  Antecedentes:
    Dado que existe un intercambio pendiente programado en una fecha

  Escenario: Recordar intercambio pendiente
    Cuando la fecha del intercambio sea mayor a 24 horas
    Entonces se enviará un recordatorio a los estudiantes involucrados sobre el intercambio pendiente