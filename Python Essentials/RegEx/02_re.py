import re

### Modificadores
# Los modificadores son opciones que sepueden agregar a un patron para cambiar su comportamiento

#re.IGNORECASE: Ignora las mayusculas y minusculas

print('---------------------------------')
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. Viva la Ia"
pattern = "AI"

found = re.findall(pattern, text, re.IGNORECASE)  # Ignora las mayusculas y minusculas
if found: print(found)

# Reemplazar el texto
# .sub() reemplaza todas las coincidencias del patron de un texto
print('---------------------------------')

text = 'Adios Mundo! Adios pobreza.'
pattern = 'Adios '
replacement = 'Hola '
found_pattern = re.sub(pattern, replacement, text, count=1)  # Podes pasar el numero de veces que queres reemplazar
print(found_pattern)



