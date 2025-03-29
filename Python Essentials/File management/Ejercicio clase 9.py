#crear un script en python que permita:
#Regisrar estudiantes en un archivo(estudiante.txt), guardando su nombre y edad.
#Mostrar la lista de estudiantes registrados
#Buscar estudiantes por nombre
#Usa with open() para manejar los archivos correctamente.

import os
#boceto
almacenEstudiantes = 'estudiantes.txt'


def registerStudents(file):
    name = str(input("student name: "))
    Age = int(input("age: "))

    # metodo un comportamiento
    with open(almacenEstudiantes, 'a', encoding='utf-8') as archivo:
        archivo.write(f'{name}, {Age} años \n')

    with open(almacenEstudiantes, 'r', encoding='utf-8') as archivo:
        content = archivo.read()
        print(content)

    value = str(input("quieres seguir ingresando estudiantes(True/False):  ").upper())
    if value == True:
        registerStudents(almacenEstudiantes)
    elif value==False:
        print('que chingas')
    else:
        print('Sos un pelotudo')



def show_students(file):
    if not os.path.exists(almacenEstudiantes):
        print("No hay estudiantes registrados.")

    with open(almacenEstudiantes, 'r', encoding='utf-8') as archivo:
        estudiantes = archivo.readlines()

    for estudiante in estudiantes:
        informacion = estudiante.split(", ")
        print(f'Nombre del estudiante:{informacion[0]}, Edad del estudiante: {informacion[1]}')


def search_students(file):
    search_student = str(input("ingresa el nombre del estudiante que quieres buscar: "))
    with open(almacenEstudiantes, 'r', 'utf-8') as archivo:
        estudiantes = archivo.readlines()




registerStudents(almacenEstudiantes)
