#Ejercicio 05
import re

# Valida que un correo sea de gmail

text = 'miduga@gmail.com'
#pattern = r'[a-zA-Z0-9_.-]+@gmail\.com$'
pattern = r'@gmail.com$'
# cuantificador del mas = una o mas veces

valid = re.search(pattern, text)
print(valid.group())


