# 03 - META CARACTERES ESPECIALES
# Los metacaracteres son simbolos especiales con significado especificos en la expresiones regulares.

import re

#1. El punto(.)
# Coincidir con cualquier caracter excepto una nueva linea

text = 'Hola mundo, H$la de nuevo, H0la otra vez'
pattern='H.la'

found = re.findall(pattern, text)
if (found):
    print(found)
else:
    print('No se encontraron coincidencias chaval')

text = 'casa caasa cosa cisa cesa causa'
pattern = 'c.sa'

matches =re.findall(pattern, text)
print(matches)


#---------------------------------------------------
# r determina que lo siguiente es una expresion regular

text = 'Hola mundo, H$la de nuevo, H0la otra vez'
pattern = r"H.la"

found = re.findall(pattern, text)
if (found):
    print(found)
else:
    print('No se encontraron coincidencias chaval')

text = ('Mi casa es blanca. Y el coche es negro')
'''pattern = '.'
matches =re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())'''
pattern = r'\.' # la \ ayuda a cancelar el significado del punto y toca irlo a buscar jajaj
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())




# BUSCAR UN DIGITO
# \d: coincide con cualqueir digito (0-9)
text = 'El numero de telefono es 123456789'
pattern= r'\d'
found = re.findall(pattern, text)
print(found)

pattern= r'\d{9}'
found = re.findall(pattern, text)
print(found)



# \w: coincide con cualquier caracter alfanumerico(a-z,A-Z, 0-9, _)
text = '@@@el_rubius_69]='
pattern= r'\w{9}'
matches = re.findall(pattern, text)
print(matches)

#Espacios en blanco en Python
# \s: Coincide con cualquier espacio en blanco(espacio, tabulacion, salto de linea)

# \n salto de linea
# \t salto de linea
pattern= r'\s'
text = 'Hola Mundo\n¿Como estas?\t'
matches = re.findall(pattern,text)
print(matches)


# ^: Coincide ceon el principio de cadena.
text = '$085_name'
pattern= r'^\w{3}' # Validar nombre de usuario
valid = re.search(pattern, text)
if valid:
    print('El nombre de usuario es valido')
else:
    print('El nombre de usuario no es valido')


phone = '+34323 123456789'
pattern = r'^\+\d{2,3} '

valid=re.search(pattern, phone)
if valid:
    print('El numero de telefono es valido')
else:
    print('El numero de telefono no es valido')


# Valida el final de la cadena
# $: COincide con el final de la cadena
text = 'Hola mundo'
pattern = r'mundo$'
valid =re.search(pattern, text)
if valid:
    print('El patron coincide con el final de la cadena')
else:
    print('El patron no coincide con el final de la cadena')



# \b: Coincide con el principio o final de una palabra
text = 'casa acasa acasado casado casas cosa casa'
pattern = r'\bc.sa\b'
found = re.findall(pattern, text)
print(found)


# Coincide con opciones
# |: Coincide con alguna opcion u otra
fruits = 'platano, manzana, aguacate,palta, pera, aguacate, aguacate'
pattern = r'palta|aguacate|p..a|\b\w{7}\b'
matches = re.findall(pattern, fruits)
print(matches)