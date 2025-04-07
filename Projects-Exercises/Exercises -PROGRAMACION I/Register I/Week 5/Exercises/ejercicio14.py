suma = 0
user_input = 0

while not user_input < 0:
  user_input = int(input("Ingrese un numero positivo para sumar, o uno negativo para salir del bucle: "))
  if user_input >= 0:
    suma = suma + user_input
  else:
    print("Bucle finalizado\n")

print(f"La suma es: {suma}")
