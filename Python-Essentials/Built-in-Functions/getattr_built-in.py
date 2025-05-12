# BUILT-IN FUNCTION GETATTR()
"""
method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function
SYNTAX
    getattr(object, name[, default]) is equivalent to object.name
PARAMETERS
    object - object whose named attribute's value is to be returned
    name - string that contains the attribute's name
    default (Optional) - value that is returned when the named attribute is not found
RETURN VAlUES
    value of the named attribute of the given object
    default, if no named attribute is found
    AttributeError exception, if named attribute is not found and default is not defined
"""

# EXAMPLE 1: How getattr() works in Python?
class Person:
    age=23
    name='Adam'

person=Person()
print('The age is: ',getattr(person, 'age'))
print('The name is: ',getattr(person, 'name'))

# EXAMPLE 2: getattr() when named attribute is not found
class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))