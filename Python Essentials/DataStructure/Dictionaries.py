# DICTIONARIES
dogs = {'name': 'Roger', 'age': 8, 'color': 'green'}
#dog["name"] = "ElMenso"
#print(dog["name"])
#rint(dog.get("color", 'Esto retorna si no encuentra el valor anterior xd'))
#print(dog.pop("name"))
#print(dog)
#print(
#    dog.popitem())  # its going to retrieve and remove the last key value  pair inserted into teh dictionary
print(dogs.keys())
print(f'{list(dogs.keys()) }   {list(dogs.values())}')
print(list(dogs.items()))

dogs["favorite food"] = "Meat"
del dogs['color']

dogsCopy = dogs.copy()

print(dogs)