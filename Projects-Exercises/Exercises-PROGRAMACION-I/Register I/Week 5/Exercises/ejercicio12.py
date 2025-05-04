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
