#crear un script en python que permita:
#Regisrar estudiantes en un archivo(estudiante.txt), guardando su nombre y edad.
#Mostrar la lista de estudiantes registrados
#Buscar estudiantes por nombre
#Usa with open() para manejar los archivos correctamente.


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
    if value:
        registerStudents(almacenEstudiantes)
    else:
        print('que chingas')


registerStudents(almacenEstudiantes)
