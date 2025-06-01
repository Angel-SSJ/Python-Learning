# BUILT-IN FUNCTION

"""
the dir() method returns the list of valid attributes of the passed object.

SYNTAX
    dir(object)
PARAMETERS
    object - can be an empty/filled tuple, list, set, dictionary etc or any user-defined object
RETURN VAlUES
    the list of attributes of the object passed to the method
"""

# EXAMPLE 1: Python dir() with a list

numbers=[1,2,3]
print(dir(numbers))

numbers2=[]
print(dir(numbers2))

# EXAMPLE 2: Python dir() with a Set

numberSet={12,32,43,56}
print(dir(numberSet))

numberSetVoid={}
print(dir(numberSetVoid))

# EXAMPLE 3: Python dir() with a Tupe
numbersTuple=(12,32,54,2)
print(dir(numbersTuple))

numbersTupleVoid=()
print(dir(numbersTupleVoid))


# EXAMPLE 4: dir() with a User-defined Object

class Person:
    def __dir__(self):
        return ['age','name','salary']
teacher=Person()
print(dir(teacher))
print(dir(Person))
