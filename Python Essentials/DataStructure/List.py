# LISTS
items = ['Roger', 1, 'Syd', True, 'Quincy', 7]
print('testing' in items)  # envía False ya que 'testing' no esta en items\
print(items[-1])  # envia el objeto que esta en la posición esa(el último)
print(items[:3])



## Comprehension List ##
mylist = [1, 3, -6, -9, -0.2, 2, -1]
bool_list = [True if x > 0 else False for x in mylist]  # list comprehension

for x in mylist:
    print(x)

print(bool_list)  # print a list with boolean values

##AGREGAR ELEMENTOS##
items.append('Bin Ladel')
items.insert(4, 'Socrates')
items.extend(['Juan', 5])

##ElIMINAR OBJETOS##

items.remove("Roger")  # Remover una vaina
print(items.pop())  # Este elimina el ultimo de la lista [-1]

items.insert(2, 'Test')
print(items)

items[1:1] = ['Test1', 'Test2']
print(items)

## OTRAS OPERACIONES ##
Items = ['Elon Musk', 'Mark Zukenber', 'Donal Trump', 'Sam Altman', 'Bill Gates']

# SORTING LISTS

Items.sort(
    key=str.lower)  # Sort retorna una lista diferente a la original, osa crea una copia de la lista original y no permuta como otras funciones
print(Items)
print(sorted(Items, key=str.lower))

# LEN LISTS
print(f'La lista Items tiene la longitud de: {len(Items)}')

#INDEX LIST
element = 'Elon Musk'
Items.index(element)
element2 = 'Donal Trump'
Items.index(element2)

# COUNT LIST
Items.count('Elon Musk')
#Return the number of times the value 9 appears int the list:

# REVERSE LIST
print(items[::-1])  # darle reversa a la lista
print(Items.reverse())

# COPY LIST
print('COPY LIST')
copyItems = Items[:]
print(copyItems)
copy2Items = Items.copy()
print(copy2Items)
copy3Items = list(Items)
print(copy3Items)
