# DICTIONARIES
"""
es una colección no ordenada(en versiones anteriores a Python 3.7), mutable que almacena pares de clave-valor
Se accede por medio de claves únicas por objeto.
Características
    No ordenado
    Acceso rápido por clave
    Las claves son únicas


Si se intenta acceder a un clave inexistente en un diccionario normal, se obtiene un error,
para evitar esto podemos usar collections.defaultdict o dict.get()
"""

dogs = {'name': 'Roger', 'age': 8, 'color': 'green'}

print(dogs.keys()) # Tirar las claves
print(f'{list(dogs.keys()) }   {list(dogs.values())}') # Tirar las keys y valores
print(list(dogs.items()))   # its going to retrieve and remove the last key value  pair inserted into teh dictionary

print(f'Este es el estado de dogs: \n{dogs.items()}')
print(f'Se elimino este objeto: {dogs.popitem()}') # Eliminar un elemento
print(f'Y este es el estado despues de popitem: \n {dogs.items()}')

#dogs["favorite food"] = "Meat"
#del dogs['color']

dogsCopy = dogs.copy()
print(dogsCopy)
print(f'se busca un objeto por la key "c" ...{dogsCopy.get('c', 'No existe esa key pedazo de pobre ')}')
