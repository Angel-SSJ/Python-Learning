temperatura = int(input("Ingrese el temperatura ambiente: "))

if 22 > temperatura > 0:
    print("clima frio")
elif 28 > temperatura > 22:
    print("clima caliente ")
elif 40 > temperatura > 29:
    print("Los Team calor son unos enfermos de... ")
else:
    print("I dont know")
