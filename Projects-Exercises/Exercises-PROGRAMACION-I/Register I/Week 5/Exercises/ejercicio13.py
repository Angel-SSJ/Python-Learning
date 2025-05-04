password = "1234"

user_input = ""

while user_input != password:
  user_input = input("Ingrese la contraseña: ")
  if user_input != password:
    print("La contraseña es incorrecta\n")
  else:
    print("La contraseña es correcta\n")
