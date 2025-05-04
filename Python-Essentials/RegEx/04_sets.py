import re

from fontTools.misc.cython import returns

# [:] Coincide con cualquier caracter dentro de los corchetes
username='rub.$ius_69+'
pattern = r'^[\w._%+-]+$'
# con corchetes se pone tipo condicion de lo que puede aparecer ahi ve, y el + qeu una o mas veces :D
# ^: indica el inicio de la cadena y $ el final de la cadena, entonces de principio a fin debe coincidir con lo que hay dentro de los corchetes
match = re.search(pattern, username)
if match:
    print('el usuario es valido :D')
    print(match.group())
else:
    print('el usuario NO es valido CTM :D')


# Buscar todas las vocales de una palabra
text = 'Hola mundo'
pattern = r'[aeiou]'
matches = re.findall(pattern, text)
print(matches)

# Ejercicios - Regex [a-ZA-Z]
# Una Regezx para encontrar las palabras man, fan y ban
# Pero ignora el resto
text = 'Man, ran, ban, man, fan, ban'
pattern = r'[mfb]an'
matches = re.findall(pattern, text)
print(matches)


# Ejercicio: Nos han complicado el asunto, porque ahora hay palabras que encajan pero no eimpiean por esas letras.
# Solo quermeos las palabras man, fan, ban
text = 'omniman fanatico man bandana ban'
pattern =r'\b[.mfb]an\b'
matches = re.findall(pattern, text)
print(matches)

# r'[a-zA-Z]': Coincide con cualquier letra mayuscula o minuscula
# r'[a-zA-Z0-9]': Coincide con cualquier letra mayuscula o minuscula o numero

# [^]: Coincide con cualquier caracter qeu no este dentro de los corchetes
text = 'Hola mundo'
pattern = r'[^aeiou]'
matches = re.findall(pattern, text)
print(matches)