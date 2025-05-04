# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
text = '34 65704258'
pattern = r'(\+|00)?34 \d{8}'
found = re.search(pattern, text)
print(found.group())