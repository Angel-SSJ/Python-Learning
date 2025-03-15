#TUPLES
'''
es similar a una lista, la diferencia recae en su inmutabilidad,
es decir, no puedes modificar sus elementos después de que se han creado.
Características
    Ordeanda: se mantienen en el orden en que fueron creadas
    Inmutable: nos e pueden agregar ni eliminar elmentos
    pueden contener diferentes tipos de datos






'''
# Ayuda a crear grupos de datos inmutables
names = ('Roger', 'Syd')
names[0]
names.index('Roger')

print(len(names))
print("ElSapito" in names)
names[0:2]
print(sorted(names))
newTuple = names + ("Tina", "Quincy")
print(newTuple)


