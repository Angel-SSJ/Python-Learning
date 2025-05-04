# Si el monto total de la compra supera los $100 dolares aplicar un descuento del 3%, si no excede de $50 1% de descuento, de lo contrario no aplica descuento

# monto, descuento a aplicar, el precio final a pagar

monto = float(input("Ingrese el total de la compra: "))
descuentoPorcentaje = 0

if monto >= 100:
    descuentoPorcentaje = 0.03
elif monto <= 50:
    descuentoPorcentaje = 0.01


descuento = monto * descuentoPorcentaje
montoPagar = monto - descuento

print(f"el pago final es {montoPagar}, con el descuento de {descuento} ")
