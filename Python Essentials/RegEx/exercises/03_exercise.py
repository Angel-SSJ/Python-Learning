# Ejercicio 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayusculas y minusculas.
import re

text='Este es el curso de Python de Midudev. ¡Suscribite a python si te gusta este contenido! PYTHON'
pattern='python'
matches=re.findall(pattern,text,re.IGNORECASE)
for match in matches:
    print(match)
print(matches)