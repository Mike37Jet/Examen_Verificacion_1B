# Created by migue at 18/6/2025
# language: es
Característica: Acordar intercambios entre estudiantes
  Como estudiante
  Quiero confirmar el intercambio de libros con otro estudiante
  Para asegurar el acuerdo del intercambio y evitar malentendidos

  Antecedentes:
    Dado que existe un acuerdo de intercambio de libros
    Y es antes de 24 horas de la fecha de intercambio

  Escenario: Confirmar intercambio de libros
    Cuando el estudiante confirma el intercambio
    Entonces se actualizará el estado del intercambio a "Confirmado"
    Y se notificará al otro estudiante sobre la confirmación del intercambio

  Escenario: No confirmar intercambio de libros
    Cuando el estudiante no confirma el intercambio
    Entonces se actualizará el estado del intercambio a "Cancelado"
    Y se notificará al otro estudiante sobre la cancelación del intercambio