# BUILT-IN FUNCTION BOOL()

"""
the bool() method takes a specified argument and returns its boolean value
"""

test=1
print(f'{test} is {bool(test)}')

"""
PARAMETERS
    argument -whose boolean value is returned
RETURN VALUE
    False - if argument is empty,None,0 or False
    True - if argument is any number(besides 0),True or a string
"""
print('------------------------------\n')
test = 254
# bool() with an integer number
print(test, 'is', bool(test))

test1 = 25.14
# bool() with a floating point number
print(test1, 'is', bool(test1))

test2 = 'Python is the best'
# bool() with a string
print(test2, 'is', bool(test2))

test3 = True
# bool() with True
print(test3, 'is', bool(test3))
print('------------------------------\n')
test = []
# bool() with an empty argument
print(test, 'is' ,bool(test))

test1 = 0
# bool() with zero
print(test1, 'is' ,bool(test1))

test2 = None
# bool() with none
print(test2, 'is' ,bool(test2))

test3 = False
# bool() with False
print(test3, 'is' ,bool(test3))
print('------------------------------\n')
print('------------------------------\n')