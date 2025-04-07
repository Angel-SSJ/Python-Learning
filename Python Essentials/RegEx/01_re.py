##
# 01 -Expresiones regulares
"""Se utiliza pra buscar y manipular cadenas de texto para que coincidan con un patron especifico
-Las expresioens regulares son suna secucnia de carecteres qeu forman un patron de busqueda.
-Se utilizan pra la busqueda de cadenas de texto, validación de datos, etc.


¿Por que aprender Regex?
    -Busquedad avanzada: Encontrar patrones especificos en texto grandes de forma rápida y precisa(un editor de Markdown solo usando Regex)
    -Validación de datos: Validar entradas de usuario, como correos electrónicos, números de teléfono, etc. Sirven para asegurar los datos que ingresa un usuario sean correctos
    -Extraccion de informacion: Extraer, reemplazar y modificar partes de la cadena de texto facilmente
"""

#1- Importar el modulo de expreiones regulares 're'
import re

#2- Crear un patron, que se uan cadena de texto que describe lo que queremos encontrar
pattern = 'Hola'

#3- El texto donde queremos buscar
text = 'Hola mundo'
#4- Buscar el patron en el texto con 're'
result = re.search(pattern, text)  # del tipo match
print(result)
if result:
    print('Patron encontrado')
else:
    print('Patron no encontrado')

# .group() devuelve la cadena que coincide con el pattern
#print(result.group())

#.start() devuelve la posicion de inicio de la coincidencia
#print(result.start())

#.end() devuelve la posicion de fin de la coincidencia
#print(result.end())

### Encontrar todas las coincidencias de un patron
#.findall() devuelve una lista con todas las coincidencias del patron en el texto
text='Me gusta Pyhhon. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python'
pattern='Py.hon'
matches=re.findall(pattern, text) # lista de las veces que encuentra el patron
print(matches)



text = 'Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python'
pattern = 'Python'
matches = re.findall(pattern, text)  # lista de las veces que encuentra el patron
print(matches)
print(len(matches))
#------------------------------

#iter() devuelve un iterador que contiene todos los resultados de la busqueda
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())


