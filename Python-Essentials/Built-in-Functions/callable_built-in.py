# BUILT-IN FUNCTION CALLABLE()
"""

"""

"""
SINTAX
    callable(object)
PARAMETERS
    callable() method takes a single argument object.
RETURN VALUES
    True - if the object appears callable
    False - if the object is not callable.
"""

print('------------------------------\n')
x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))
#Here, the object x is not callable. And, the object y appears to be callable (but may not be callable).
print('------------------------------\n')
class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))
print('------------------------------\n')
class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))  # still returns True because Foo is a class (classes are callable)

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()  # error occurs because instances of Foo are not callable
