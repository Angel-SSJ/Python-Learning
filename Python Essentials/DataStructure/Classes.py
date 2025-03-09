# CLASSES


# Inheritance
class Animal:

  def walk(self):
    print('Walking...')


class Dog(Animal):  # Inherit
  #Constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    return print('woof!')


roger = Dog('Roger', 8)
print(type(roger))
print(roger.age)
print(roger.name)
print(roger.bark())
print(roger.walk())


