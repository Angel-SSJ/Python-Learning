
#Calcula el resultado de la siguiente operación:
resultado = 25 +10 - 5 *2
print(resultado)


#2. Determina el residuo de la división de 23 entre 4
resultado = 25 +10 - 5 *2
print(resultado)

#3. ¿Cuál es el resultado de la división entera entre 55 y 6?
resultado = 55//6
print(resultado)
#4. Evalúa el valor de a después de la operación siguiente
a =7
a = a + 5 * 2
print(a)

#5. Aplica la exponenciación para calcular 4^3
resultado = 4 ** 3
print(resultado)

#6. ¿Cuál es el resultado de la siguiente operación?
resultado = (10 + 2) * 3 - 4 / 2
print(resultado)

#7. Evalúa la operación con prioridad entre división y multiplicación
resultado = 20 / 5 * 2
print(resultado)

#8. Calcula el área de un rectángulo de base 12 y altura 8
base = 12
altura = 8
area = base * altura
print(area)

#9. Convierte 100 grados Celsius a Fahrenheit con la fórmula F = C * 9/5 + 32
C = 100
F = C * 9 / 5 + 32
print(F)

#10. Calcula el perímetro de un triángulo cuyos lados miden 5, 7 y 9.
lado1 = 5
lado2 = 7
lado3 = 9
perimetro = lado1 + lado2 + lado3
print(perimetro)

#Ejercicios de Operadores Lógicos
#Instrucciones: Determina si cada expresión retorna True o False.


#1. ¿El número 10 es mayor que 5 y menor que 20?
if 20 > 10 > 5:
    print(True)
else:
    print(False)

#2. Evalúa si False y True devuelven True o False
resultado = False and True
print(resultado)


#3. Verifica si 15 es múltiplo de 3 o de 4
def multiple(m, n):
    return True if m % n == 0 else False


print(resultado)

#4. ¿El número 8 no es menor que 6?
resultado = not (8 < 6)
print(resultado)

#. Evalúa si 25 es mayor que 10 y 25 no es igual a 30

print(True if 30 > 25 > 10 else False)

#6. ¿La suma de 3 y 5 es igual a 8 y 2 por 4 también es 8?
print(True if 3 + 5 == 8 and 2 * 4 == 8 else False)
print(resultado)

#7. Evalúa si not True or False devuelve True
resultado = not True or False
print(resultado)

#8. ¿El número 20 es mayor que 18 y menor que 25, pero no igual a 22?

print(True if 25 > 20 > 18 and 25 != 22 else False)

#9. ¿El número 9 es par o impar? (Usa or)
n = 9
print('es par' if n%2 ==0 else 'es impar')

#10. ¿La expresión not (10 > 5 and 2 < 3) devuelve False?

print(not (10>5 and 2<3))
