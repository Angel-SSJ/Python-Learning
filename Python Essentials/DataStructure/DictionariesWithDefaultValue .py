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

