import re
# Ejercicio: Detectar si hay un numero de Espa;a en le texto gracias al prefijo +34

text='Mi numero de telefono es +34 86865959 apuntalo chaval'
pattern = r'\+34 \d{8}'

match = re.search(pattern, text)
print(f' He encontrado el siguiente numero: {match.group()}')
