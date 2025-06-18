# Created by migue at 18/6/2025
# language: es
Característica: Recordar intercambios pendientes
  Como estudiante
  Quiero recibir recordatorios de los intercambios pendientes
  Para evitar el olvido de los intercambios programados

  Antecedentes:
    Dado que existen intercambios pendientes programados en una fecha

  Escenario: Recordar intercambio pendiente
    Cuando la fecha del intercambio se mayor a 24 horas
    Entonces se enviará un recordatorio a los estudiantes involucrados sobre el intercambio pendiente