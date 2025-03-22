import sys

# Apertura de archivo con ruta relativa
# fixed archivo = open("\nose-un-mensaje.txt","r")


# Apertura con ruta absoluta

secuencais = "\n \t \r"
print(sys.prefix)
#with open("C:\\Users\\angel\\OneDrive\\Escritorio\\nose un mensaje.txt", 'r') as archivo:
#   contenido = archivo.read()
#    print(contenido)
#
#with open("..\\Sos un boludo.txt", 'w') as archivo:
#    print('probando')
#    print(contenido)

#with open("..\\Sos un boludo 2.txt", 'w+') as archivo:
#  content = archivo.read()
#   print(content)
#   archivo.write("Estoy probando manejo de archivos con PYTHON.\n")
#   archivo.write("TA LOCA LA VAINA\r")


with open("..\\Sos un boludo 2.txt", 'r+') as archivo:
    content = archivo.read()
    archivo.seek(2)
    print(content)
    print(content[:archivo.tell()])

# Error de encoding(codificación del formato a ocupar)

with open("..\\Sos un boludo 2.txt", 'r+', encoding='utf-8') as archivo:
    content = archivo.read()
    print(content)

with open("..\\Sos un boludo 2.txt", 'r+', encoding='utf-8') as archivo:
    content = archivo.read()
    archivo.seek(1)
    print(content[archivo.tell()])

with open("..\\Sos un boludo 2.txt", 'r+', encoding='utf-8') as archivo:
    content = archivo.read()
    archivo.seek(1)
    archivo.write('esto es una prueba pasmado')
    print(content[archivo.tell()])
