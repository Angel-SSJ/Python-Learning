# Ejercicio:
# Encuentra las palabras de mas de 4 letas
import re

words= 'ala casa arbol leon cinco murcielado'
pattern =r'\b\w{4,6}\b' # El \b indica que debe desde el inico al final deben haber de 4 a 6 letras jiji
matches = re.findall(pattern, words)
print(matches)

words = ' fantastico jiji ala casa arbol leon cinco murcielado'
pattern = r'\b\w{6,}\b'  # {6,} indica que haye palabras de 6 o mas letras
matches = re.findall(pattern, words)
print(matches)


