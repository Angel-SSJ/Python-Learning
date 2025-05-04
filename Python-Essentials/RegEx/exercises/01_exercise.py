import re
#EJERCICIO 01
#Encuentra la primera ocurrencia de la palabra 'IA' en el siguiente texto e indica en que posicion empieza y temina la coincidencia

text ='Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la pruede cagar con las Regex para ir con cuidado'
pattern='ai'

found_ia=re.search(pattern,text)
if found_ia:
    print(f'He encontrado el patron en el texto, inicia en la coordeanda: {found_ia.start()} y termina en la coordenada: {found_ia.end()}')
else:
    print('No he encontrado el patron en el texto CTM')

