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




