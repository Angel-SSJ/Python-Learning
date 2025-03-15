import array
# se crea un array vacio y un valor para restringuir la inserción de datos
arrayTesting = array.array('i')
value_restringed = 10

'''Se crea esta función que se encargará de ordenar el array, su funcionamiento es el siguiente:
    1. Crea una copia del array entrante
    2. Escanea por primera vez el array, agarrando la primera posición como valor mínimo
    3. Escanea por segunda vez el array, y agarra un valor, en este caso es un valor una
       unidad mayor a i, es decir, j=i+1 en el indice del array
    4. Se evalua si j es menor que i, si esto es correcto, el valor minimo cambia a ser j
    5. Se intercambian valores, el valor indice i toma el valor indice min_value, y el 
       valor de indice min_value toma el valor de indice i
    6. Imprime el array de referencia, el que no ha recibido cambio y se mantiene como al 
       inicio(en este caso es a) y el array que ha sido ordenado(en este caso es arr)  
    '''

def selection_sort(a):
    arr = a[:]
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    print(f'Array original: {a.tolist()}')
    print(f'Array ordenado: {arr.tolist()}')


print('esto es una prueba de un algoritmo de ordenación, por consiguiente, solamente inserte 10  valores entero')
# Se ejecuta un while, con el objetivo de asegurar la inserción correcta de datos y su respectivo limite.
while len(arrayTesting) < value_restringed:
    i = int(input(f'inserte un valor, tiene {value_restringed - len(arrayTesting)} valores restantes a insertar: '))  # Pide un valor al cliente
    arrayTesting.append(i)  # Se añade el valor de i en el array
    print(f'El array se mira así: {arrayTesting.tolist()}')  # Se visualiza el array en vivo
selection_sort(arrayTesting)


