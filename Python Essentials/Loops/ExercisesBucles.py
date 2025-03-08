## EXERCISE 1 ##
i = 1

while i <= 10:
    print(f"{i}")
    i = i + 1
    break


## EXERCISE 2 ##
for i in range(10,0,-1):
  print(i)

## EXERCISE 3 ##
for i in range(1,11):
  print(f"5 x {i} = {i*5}")


num = int(input('Ingrese el numero del cual quiere ver la tabla de multiplicar:  '))

for i in range(0, 11):
    print(f'{i}x{num} = {i * num}')

## EXERCISE 4 ##
suma = 0
i = 1

while i <= 100:
  suma = suma + i
  i = i + 1

print(f"La suma de los numeros del 1 al 100 es: {suma}")


## EXERCISE 5 ##
producto = 1
for i in range(1,11):
  producto = producto * i

print(producto)


## EXERCISE 6 ##
num = int(input("Ingrese un numero positivo: "))

if num < 0:
  print("Por favor ingresa un numero positivo")
else:
  for i in range(1, num + 1):
    print(i)


## EXERCISE 7 ##
num = int(input("Ingrese un numero positivo: "))

if num < 0:
  print("Ingrese un numero positivo")

for i in range(num, 0, -1):
  print(i)


## EXERCISE 8 ##
for i in range(2,21,2):
  if i % 2 == 0:
    print(i)


## EXERCISE 9 ##
i = 1
while i <= 20:
  if i % 2 != 0:
    print(i)
  i = i + 2


## EXERCISE I0 ##
suma = 0
for i in range(2,51,2):
  if i % 2 == 0:
    suma = suma + i

print(suma)


## EXERCISE I1 ##
num = int(input("Ingrese un numero positivo: "))

if num <= 0:
  print("Por favor ingrese un numero positivo")
divisores = []
divisores2 = [i for i in range(1, num + 1) if num % i == 0]

for i in range(1, num + 1):
  if num % i == 0:
    divisores.append(i)

print(f"Los divisores de {num} son {divisores}")

## EXERCISE I2 ##
num = int(input("Ingrese un numero positivo: "))

if num <= 0:
  print("Por favor ingrese un numero positivo")

divisores = []

for i in range(1, num + 1):
  if num % i == 0:
    divisores.append(i)

es_primo = len(divisores) == 2

if es_primo:
  print(f"El numero {num} es primo.")
else:
  print(f"El numero {num} no es primo.")


## EXERCISE I3 ##
password = "1234"

user_input = ""

while user_input != password:
  user_input = input("Ingrese la contraseña: ")
  if user_input != password:
    print("La contraseña es incorrecta\n")
  else:
    print("La contraseña es correcta\n")

## EXERCISE I4 ##
suma = 0
user_input = 0

while not user_input < 0:
  user_input = int(input("Ingrese un numero positivo para sumar, o uno negativo para salir del bucle: "))
  if user_input >= 0:
    suma = suma + user_input
  else:
    print("Bucle finalizado\n")

print(f"La suma es: {suma}")

## EXERCISE I5 ##
num = int(input("Ingrese un numero: "))

factorial = 1

if num < 0:
  print("Ingrese un numero positivo")
elif num == 0:
  factorial = 1
else:
  for i in range(1,num + 1):
    factorial = factorial * i

print(f"{num}! = {factorial}")

## EXERCISE I6 ##
i,j = 0,1
secuencia_fibonacci = [i,j]
num = int(input("Ingrese un numero positivo: "))

siguiente_fibonacci = 0

if num <= 0:
  print("Ingrese un numero positivo")
else:
  while siguiente_fibonacci < num:
    siguiente_fibonacci = i + j
    i = j
    j = siguiente_fibonacci
    if siguiente_fibonacci < num:
      secuencia_fibonacci.append(siguiente_fibonacci)

print(secuencia_fibonacci)



## EXERCISE I7 ##
usuario = "PepipoElCrack"
contra = "123456"

usuario_input = ""
contra_input = ""

while usuario_input != usuario and contra_input != contra:
    usuario_input = input("Ingrese el usuario: ")
    contra_input = input("Ingrese la contraseña: ")

    if usuario_input != usuario or contra_input != contra:
        print("Usuario o contraseña incorrectos")

print("Login exitoso. Bienvenido!")

## EXERCISE I8 ##
num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
  print("*" * i)


## EXERCISE I9 ##
import random
rand = random.randint(1,100)
num = 0
while num!= rand:
    num = int(input("Ingrese un numero entre el rango 1-100: "))
    if num < rand:
        print("No adivinaste. El numero es mayor pelotudo")
    elif num > rand:
        print("No adivinaste. El numero es menor pelotudo")
print(f'Adivinaste, el numero es {rand}')




