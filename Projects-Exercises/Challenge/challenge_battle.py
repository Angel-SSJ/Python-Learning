'''
Tienes doslistas de numeros, lista_a y lista_b, ambas de la misma longitud
Cada numero en lista_a "enfrenta" al numero en la misma posicion en lista_b

-si el nuemro en lista_a es mayor, su valor se suam al siguiente numero en lista_a.
-si el numero en lista_b es mayor, su valor se suma al siguiente numero en lista_b
-si son iguales, ambos se eliminana y no afectan al siguiente par.

Debes simular estos enfrentamietnos y devolver le resultado final:
-si al final queda un numero en lista_a, devuelve ese numero seguido de la letra'a (por ejemplo, '5a')
-si al final queda un numero en lista_b, devuelve ese numero seguido de la letra'b (por ejemplo, '5b')
-En caso de empate, devuelve la letra 'x'

lista _a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b) => '2b'


'''
list_a = [4, 2, 2]
list_b = [2, 4, 3]

def battle(lista_a, lista_b):
    for i in range(len(lista_a)):
        if lista_a[i]> lista_b[i]:
            print(f'{lista_a[i]} y {lista_a[i + 1]} se suman')
            lista_a[i] = lista_a[i] + lista_a[i+1]
            print(f'{lista_a[i]} e indice {i+1}')

        elif lista_b[i+1]> lista_a[i]:
            print(f'{lista_b[i]} y {lista_b[i + 1]} se suman')
            lista_b[i] = lista_b[i] + lista_b[i + 1]
            print(f'{lista_b[i]} e indice {i + 1}')



        elif lista_a[i] == lista_b[i]:
            lista_a.pop(i)
            lista_b.pop(i)
            print('x')
        #print(f'lista_a: {lista_a}')


battle(list_a, list_b)


## EN PROCESO AUN JAAJJA