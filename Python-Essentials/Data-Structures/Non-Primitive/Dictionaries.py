# DICTIONARIES

'''
es una colección no ordenada(en versiones anteriores a Python 3.7), mutable que almacena pares de clave-valor
Se accede por medio de claves únicas por objeto.
Características
    No ordenado
    Acceso rápido por clave
    Las claves son únicas


Si se intenta acceder a un clave inexistente en un diccionario normal, se obtiene un error,
para evitar esto podemos usar collections.defaultdict o dict.get()
'''
'''
dogs = {'name': 'Roger', 'age': 8, 'color': 'green'}

print(dogs.keys()) # Tirar las claves
print(f'{list(dogs.keys()) }   {list(dogs.values())}') # Tirar las keys y valores
print(list(dogs.items()))   # its going to retrieve and remove the last key value  pair inserted into teh dictionary

print(f'Este es el estado de dogs: \n{dogs.items()}')
print(f'Se elimino este objeto: {dogs.popitem()}') # Eliminar un elemento
print(f'Y este es el estado despues de popitem: \n {dogs.items()}')

dogs["favorite food"] = "Meat"
del dogs['color']

dogsCopy = dogs.copy()
print(dogsCopy)
print(f'se busca un objeto por la key "c" ...{dogsCopy.get('c', 'No existe esa key pedazo de pobre ')}')
'''



 #DICTIONARIES

#Los diccionarios son coleccione de pare clave-valor.
#Sirven apra almacenar datos relacionados

persona ={
    "nombre":"Angel",
    'edad':18,
    'es_estudiante':True,
    "calificaciones":[10,9,8],
    "socials":{
        'twitter':"@angel",
        'instagram':"@angel",
        'tiktok':"@angel",
    }
}

# acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]['twitter'])

# cambiar valores al acceder
persona['nombre'] = 'Gabriel'
print(persona['nombre'])



# devuelve las claves del diccionario
print(persona.keys())


# elimianar completamente una propiedad
del persona['edad']
print(persona)

es_estudiante = persona.pop('es_estudiante')
print(f'es_estudiante {es_estudiante}')
print(persona)



# sobreecribir un diccionario  con otro diccionario

a = {'name':'Angel', 'age':19}
b = {'name':'Gabriel', 'es_estudiante':True}
# a.update(b) # actualiza el diccionario a con los valores de b
# de derecha a izquierda
a.update(b)
print(a)

# comprobar si existe una propiedad
print('name'in persona) #False
print('nombre'in persona) #True

# obtener todas las claves
print('\nKeys: ')
print(persona.keys())

# obtener todas los valores
print('\nValues: ')
print(persona.values())

#obtener tanto clave como valor
print('\nItems: ')
print(persona.items())


for key, value in persona.items():
    print(f'Key: {key} Value: {value}')

from collections import defaultdict

# Diccionario con valor por defecto 0 para claves inexistentes
mi_dict = defaultdict(int)
mi_dict['x'] += 5
print(mi_dict['x'])
print(mi_dict['x'])

"""
mi_dict = defaultdict(list) # claves inexistentes tendrán una lista vacía
mi_dict['nombre'].append('Juan') 
print(mi_dict) # defaultdict(<class 'list'>, {'nombres': ['Juan']})
"""

"""
SIN OCUPAR DEFAULTDICT
dogsCopy = dogs.copy()
print(dogsCopy)
print(f'se busca un objeto por la key "c" ...{dogsCopy.get('c', 'No existe esa key pedazo de pobre ')}')
"""

