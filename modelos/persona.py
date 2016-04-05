class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre+" "+self.apellido+", "+str(self.edad) 

    @property#Ponemos property para que al llamar a mayor_de_edad, este llamando a un atributo
    def mayor_de_edad(self):
        return self.edad > 17