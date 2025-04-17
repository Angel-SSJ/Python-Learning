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




#create  a class
class Room:
    # constructor function
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # method to calculate area
    def calculate_area(self, length, breadth):
        return print(f'Area is: {length * breadth} m^2')


instanceTest = Room(10, 20)
instanceTest.calculate_area(10, 20)
'''return
    Area is: 200 ^2'''



'''References
https://www.programiz.com/python-programming/class

'''
