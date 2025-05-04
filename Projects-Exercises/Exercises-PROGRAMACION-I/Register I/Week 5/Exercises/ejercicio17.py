usuario = "carlosmoran"
contra = "123456"

usuario_input = ""
contra_input = ""

while usuario_input != usuario and contra_input != contra:
  usuario_input = input("Ingrese el usuario: ")
  contra_input = input("Ingrese la contraseña: ")

  if usuario_input != usuario or contra_input != contra:
    print("Usuario o contraseña incorrectos")
  
print("Login exitoso. Bienvenido!")
