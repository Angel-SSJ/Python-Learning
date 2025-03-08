list = [10,20,30,40,50,60]
print(list[0]) # Primer elemento
print(list[-1]) # Ultimo elemento
print(list[1:4]) # Desde el indice 1 hasta el 3

# secuencia[inicio:fin:paso]

'''
inicio: Indice donde comienza el subarreglo
fin: Indice donde termina el subarreglo(no incluido)
paso: el salto entre elementos 
'''


# LISTAS ANIDADAS(MATRICES 2D)#
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][2]) # Accede al numero 6

cuadrados = [x**2 for x in range(5)]
print(cuadrados)