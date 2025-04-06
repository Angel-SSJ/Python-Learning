"""
Arrays
se usa normalmente listas en lugar de arrays, ya que las listas son más flexibles
existe el modulo array que permite trabajar más eficiente en memoria cuando todos los elementos son del mismo tipo
Se usa si necesitas eficiencia en memoria y rendimiento

https://docs.python.org/3/library/array.html
"""



import array
arr = array.array('i', [1, 2, 3,4,5,6,7,8,9,10])

# Acceder a elementos
print(arr[0])

# Agregar elementos
arr.append(6)
print(arr)

# Eliminar elementos
arr.remove(3)
print(arr)



