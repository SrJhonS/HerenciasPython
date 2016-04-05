import sys

from modelos.alumno import Alumno
from modelos.persona import Persona


def agregar(numero, bbdd=[]):

    for i in range(numero):
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))
        edad = int(input("Introduce el numero de edad: "))
        asignatura = int(input("Introduce la asignatura: "))

        bbdd.append(Alumno(nombre, apellido, edad, asignatura))

    return bbdd

def mostrar(bbdd):
    for i in bbdd:
        print(i)#Con esto muestra toda la informacion
        #print(i.nombre)#Con esto solo muestra los nombres

def mostrar_adultos(bbdd):
    for i in bbdd:
        if i.mayor_de_edad:
            print(i)

bbdd=[
        Alumno('Jose Luis', 'Rodriguez', 26, 'Matematicas'), 
        Alumno('Gabriel', 'Sanchez', 17, 'Filosofia'), 
        Alumno('Laura', 'de la Torres', 12, 'Educacion Fisica'), 
        Alumno('Virginia', 'Sanz', 25, 'Biologia'),
        Persona('Sara', 'Garrido', 18)
]



try:
    numero = int(input("Introduce el numero de alumnos que va a anadir: "))
except ValueError:
    print("Introduce un numero")
    sys.exit()


bbdd = agregar(numero, bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)