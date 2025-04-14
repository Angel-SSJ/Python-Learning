# Escribir  en un archivo información sobre compras

# Una compra tiene, Nombre producto, Cantidad producto,precio unitario, precio total (Cantidad producto * precio unitario),


archivo_productos = "productos.txt"


def capturar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de producto comprado: "))
    precio = float(input("ingrese el precio unitario del producto: "))

    with open(archivo_productos, mode='a', encoding='utf-8') as archivo:
        archivo.write(f"{nombre},{cantidad},{precio}\n")


def ver_productos_comprados():
    with open(archivo_productos, mode='r', encoding='utf-8') as archivo:
        productos = archivo.readlines()
        for producto in productos:
            informacion_producto = producto.split(",")
            print(
                f"Producto: {informacion_producto[0]} Cantidad: {informacion_producto[1]} Precio: {informacion_producto[2].replace("\n", "")} Total: {float(informacion_producto[1]) * float(informacion_producto[2])}")


def buscar_por_nombre():
    nombre = input("Ingrese el nombre del producto a buscar: ")

    with open(archivo_productos, mode='r', encoding='utf-8') as archivo:
        productos = archivo.readlines()
        for producto in productos:
            if nombre in producto:
                print(producto)


def buscar_por_cantidad():
    cantidad = input("Ingrese la cantidad a buscar en las compras: ")
    with open(archivo_productos, mode='r', encoding='utf-8') as archivo:
        productos = archivo.readlines()
        for producto in productos:
            info_producto = producto.split(",")
            if int(cantidad) == int(info_producto[1]):
                print(producto)


continuar = True

while continuar:
    print(
        "Ingrese una opcion: \n1. Agregar producto\n2. Leer compras\n3.Buscar por nombre producto\n4. Buscar por cantidad producto\n5. Salir")
    opcion = int(input())

    if opcion == 1:
        capturar_producto()
    elif opcion == 2:
        ver_productos_comprados()
    elif opcion == 3:
        buscar_por_nombre()
    elif opcion == 4:
        buscar_por_cantidad()
    elif opcion == 5:
        continuar = False
    else:
        print("Opcion no valida")