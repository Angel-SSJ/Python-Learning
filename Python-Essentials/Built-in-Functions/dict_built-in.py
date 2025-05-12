# BUILT-IN FUNCTION DICT
"""
Different forms of dict() constructors are:
    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)

Note: **kwarg let you take an arbitrary number of keyword arguments
A keyword argument is an argument preceded by an identifier (eg. name=).
Hence, the keyword argument of the form kwarg=value is passed to dict() constructor to create dictionaries.

RETURN VALUES
    dict() doesn't return any value (returns None).

"""
numbers = dict(x=5,y=1)
print(f'numbers= {numbers}')
print(type(numbers))

empty=dict()
print(f'empty= {empty}')
print(type(empty))

# Example 2 : Create Dictionary Using Iterables
    # keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

    # keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

    # zip() creates an iterable in Python 3
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =',numbers3)

# Example 3: Create Dictionary Using Mapping
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)



