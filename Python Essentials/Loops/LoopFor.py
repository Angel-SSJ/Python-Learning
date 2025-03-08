
condition = True

items = [1, 2, 3, 4]
for item in items:
  print(item)

for index, item in enumerate(items):
  print(index, item)

for item in range(15):
  print(item)

##FOR BASIC##

for i in range(1, 11):
    i += i
    print(i)

print('testing \n')
print('\n')

for y in range(101, 0, -1): # tu valor es 100, y le vas a restar 1 hasta llegar a 0 uuuu
    print(y)

##SOLO PARES##

for i in range(0,101):
    if i % 2 == 0:
        print(f'Numero par {i}')
    else:
        print(f'Numero impar {i}')


##TABLA DE UN NUMERO##
num = int(input('Ingrese el numero del cual quiere ver la tabla de multiplicar:  '))

for i in range(0, 11, 3):
    print(f'{i}x{num} = {i * num}')



