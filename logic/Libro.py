class Libro:
    def __init__(self, nombre, autor, estudiante):
        self.nombre = nombre
        self.autor = autor
        self.estudiante = estudiante

    def obtener_estudiante(self):
        return self.estudiante