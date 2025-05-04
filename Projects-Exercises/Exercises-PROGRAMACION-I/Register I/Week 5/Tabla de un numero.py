num = int(input('Ingrese el numero del cual quiere ver la tabla de multiplicar:  '))

for i in range(0, 11, 3):
    print(f'{i}x{num} = {i * num}')
