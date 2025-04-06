# DOCSTRINGS
'''they are used to document a function, class or module'''


def increment(n):
  '''Increment a number'''
  return n + 1


class Dog:
  '''A class representing a dog'''

  def __init__(self, name, age):
    '''Initialize a new dog'''
    self.name = name
    self.age = age

  def bark(self):
    '''Let the dog bark'''
    print('Woof!')


'''print(help(Dog))'''
