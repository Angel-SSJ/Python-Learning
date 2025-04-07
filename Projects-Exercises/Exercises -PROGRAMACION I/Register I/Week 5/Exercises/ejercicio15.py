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
