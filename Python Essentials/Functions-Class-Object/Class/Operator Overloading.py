# OPERATOR OVERLOADING
'''operator overloading is the process of defining special methods for classes that allow them to be used in more complex operations than
is an advanced technique we can use to make  classes comparable and to maek them work with python operators
we can use operator overloading to add a custom way to compare these two objects based on '''


class Dog_2:
  '''the dog class'''

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __gt__(self, other):
    return True if self.age > other.age else False


roger = Dog_2('Roger', 8)
syd = Dog_2('Syd', 7)

print(roger > syd)


'''
__add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv__() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator 
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator


'''