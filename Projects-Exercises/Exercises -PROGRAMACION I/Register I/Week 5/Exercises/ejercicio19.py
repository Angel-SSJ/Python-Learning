import random

print("Adivina el numero aleatorio")

rand = random.randint(1,100)
num = 0

while num != rand:
  num = int(input("Ingrese un numero entre 1 y 100: "))
  if num < rand:
    print("No adivinaste. El numero es mayor.\n")
  elif num > rand:
    print("No adivinaste, el numero es menor.\n")

print(f"Adivinaste, el numero es {rand}")
