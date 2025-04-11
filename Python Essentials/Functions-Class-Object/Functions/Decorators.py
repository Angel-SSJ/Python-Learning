# DECORATORS
'''they are defined with the at symbol followed by the decorator name just before the functions definition'''


def longtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val

    return wrapper


@longtime
def hello():
    print('Hello')


print(hello())
'''you are  going to often use decorators functions when you want to change the behavior of aa function without modifying the functions itself'''
