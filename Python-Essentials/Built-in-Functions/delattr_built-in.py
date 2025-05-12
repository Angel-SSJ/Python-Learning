# BUILT-IN FUNCTION

"""
SYNTAX
    delattr(object, name)
PARAMETERS
    object - the object from which name attribute is to be removed
    name -  a string which must be the name of the attribute to be removed from the object
RETURN VAlUES
    delattr() doesn't return any value (returns None). It only removes an attribute (if the object allows it).
"""

#Example 1: How delattr() works
class Coordinate:
    x=10
    y=5
    z=0

point= Coordinate()

print(f'x= {point.x}')
print(f'y= {point.y}')
print(f'z= {point.z}')

delattr(Coordinate,'z')

print('--After deleting z attribute--')
print('x = ',point.x)
print('y = ',point.y)

# Raises Error
print('z = ',point.z)

#Example 2: Deleting Attribute Using del Operator
class Coordinate:
  x = 10
  y = -5
  z = 0

point=Coordinate()
print(f'x= {point.x}')
print(f'y= {point.y}')
print(f'z= {point.z}')

del Coordinate.z

print('--After deleting z attribute--')
print('x = ',point.x)
print('y = ',point.y)

# Raises Error
print('z = ',point.z)

#Example 1: How delattr() works