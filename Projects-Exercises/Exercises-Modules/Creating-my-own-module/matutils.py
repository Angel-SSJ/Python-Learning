
def es_primo(n:int):
    if type(n) != int:
        ValueError('n must be an integer')
    else:
        if n<=1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return print(False)
        return print(True)



def factorial(n):
    if type(n) != int:
        ValueError('n must be an integer')
    else:
        if n==0:
            return print(False)
        else:
            a=1
            for i in range(1, n+1):
                a=a*i
            print(f'el numero factorial es: {a}')



def fibonacci(n):
    if type(n) != int:
        ValueError('n must be an integer')
    else:
        a,b=0,1
        for _ in range(n):
            print(a,end=' ')
            a,b=b,a+b

