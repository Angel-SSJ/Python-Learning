
nombre = input('Nombre del persona: ')
edad = input('Introduce tu edad: ')
mensaje = 'Hola, {}. Tienes {} años.'.format(nombre, edad)
print(mensaje)



import sys
def main():
    if len(sys.argv) == 3:
        nombre = sys.argv[1]
        edad =sys.argv[2]
        mensaje = f'Hola, {nombre}. Tienes {edad}  años'
        print(mensaje)
    else:
        nombre = input('Nombre del persona: ')
        edad = input('Introduce tu edad: ')
        mensaje = 'Hola, {}. Tienes {} años.'.format(nombre,edad)
        print(mensaje)

if __name__ == '__main__':
    main()