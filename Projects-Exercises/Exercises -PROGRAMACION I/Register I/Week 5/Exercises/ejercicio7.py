num = int(input("Ingrese un numero positivo: "))

if num < 0:
  print("Ingrese un numero positivo")

for i in range(num, 0, -1):
  print(i)
