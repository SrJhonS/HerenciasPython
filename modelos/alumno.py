from .persona import Persona#Con el . referenciamos a la carpeta actual

class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad, asignatura):
        super().__init__(nombre, apellidos, edad)
        self.asignatura=asignatura

    def __str__(self):
        return super().__str__()+" Asignatura: "+self.asignatura   
