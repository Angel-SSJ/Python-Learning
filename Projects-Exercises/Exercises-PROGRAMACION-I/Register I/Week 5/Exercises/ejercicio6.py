num = int(input("Ingrese un numero positivo: "))

if num < 0:
  print("Por favor ingresa un numero positivo")
else:
  for i in range(1, num + 1):
    print(i)
