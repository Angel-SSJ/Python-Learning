#FUNCTIONS


def hello(name, age):
  print("Hello " + name + ', you are ' + str(age) + ' years old!')


hello('Peruano', 785)


def change(value):
  print(value)
  value['name'] = 'pobre'
  print(value)


val = {'name': 'beau'}
change(val)


def hello(name):
  if not name:
    return
  print(f'Hello {name}!')


hello(False)
hello('beau')

# Variable Scope
#ifyou declare a variable outside of a function, it is global and can be accessed inside of a function
# if you declare a variable inside a function, it is local and can only be accessed inside of that function


def test():
  Age = 8
  print(Age)


#print(Age)
test()

#Nested Functions


def talk(phrase):

  def say(word):
    print(word)

  words = phrase.split(
      ' '
  )  # create a list of words from the phrase spite of there is space between them
  for word in words:
    say(word)


talk("I am going to buy the milk")


def count():
  count = 0

  def increment():
    nonlocal count  # tener acceso a la variable count que esta fuera de la funcion

    count += 1
    print(count)

  increment()


count()


# CLOSURES
# función anidada que hace uso de variables de la función que la contiene y, a su vez, esta función superior o principal retorna la función anidada
def counter():
  count = 0

  def increment():
    nonlocal count
    count += 1
    return count

  return increment


increment = counter()

print(increment())
print(increment())
print(increment())
print(increment())


# BUILT-IN FUNCTIONS
print('BUILT-IN FUNCTIONS')

print(abs(-5.5))  # return teh  absolute value of a number
print(round(5.49, 5))  # round a number to the nearest integer






# LAMBDA FUNCTIONS
lambda num: num * 2
# also called anonymous functions are tiny functions they have no name and only have one expression as their body
# it has to return a value
# can accept more parameters

lambda a, b: a * b
# I can assign this to the variable called multiply
multiply = lambda a, b: a * b

print(multiply(2, 4))






# ANNOTATIONS
'''they are used to specify the type of a variable, function parameter or return
value
'''


def incrementn(n: int) -> int:
    return n + 1


count: int = 0


