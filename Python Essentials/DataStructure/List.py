# LISTS
print('LISTS')
items = ['Roger', 1, 'Syd', True, 'Quincy', 7]
print('yoquese-' in items)
print(items[-1])
print(items[:3])

items.append('Bin Ladel mi papa')
items.extend(['Juan', 5])
items.remove("Roger")  # Remover una vaina
print(items.pop())  # Este elimina el ultimo de la lista [-1]
print(items[::-1])  # darle reversa a la lista

items.insert(2, 'Test')
print(items)

items[1:1] = ['Test1', 'Test2']
print(items)

# SORTING LISTS

Items = [
    'Elon Musk', 'Mark Zukenber', 'Donal Trump', 'Sam Altman', 'Bill Gates'
]
copyItems = Items[:]
#Items.sort(key=str.lower) # Sort retorna una lista diferente a la original, osa crea una copia de la lista original y no permuta como otras funciones
#print(Items)
print(copyItems)
print(sorted(Items, key=str.lower))