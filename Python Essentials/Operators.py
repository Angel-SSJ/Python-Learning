# Arithmetic Operators
print('\n')
print('Aritmetic Operators')
print(1 + 1)
print(2 - 1)
print(2 * 2)
print(4 / 2)
print(4 % 3)
print(4**2)
print(4 // 2)
print('Scamp' + 'is a good dog')
age = 8
age += 8
print(age)

#Comparison Operators
print('\n')
print('Comparison Operators')
a, b = 1, 2
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)

#Boolean Operators
condition1 = True
condition2 = False
print('\n')
print('Boolean Operators')
print(not condition1)
print(condition1 and condition2)
print(condition1 or condition2)
print(0 or 1)
print(False or 'hey')#it is returning the second operand since this is a false value, it returns the second value
print('hi' or 'hey')  # the first operand is not a false value it will return the first one
print([] or False)  #
print(False or [])  # The first operand is a false vlue its going to return the second operand /it returns False when the first operand is not a false value

# and and only evaluates teh second argument if the first one is true, otherwise it evaluates the second argument

#Bitwise Operators
print('\n')
print('Bitwise Operators')
print('& performs binary AND')  #bitwise and
print('| performs binary OR')  #bitwise or
print('^ performs binary XOR')  #bitwise xor
print('~ performs binary NOT')  #bitwise not
print('<< performs binary left shift')  #bitwise left shift
print('>> performs binary right shift')  #bitwise right shift

# is and in Operators
print('\n')
print('is and in Operators')
# in is called the membership operator, it checks if a value is contained in a list or sequence
# it is called the identity operator, it checks if two objects have the same identity

#Ternary Operator
print('\n')
print('Ternary Operator')


def is_adult(age):
  if age > 18:
    return True
  else:
    return False


def is_adult2(age):
  return True if age > 18 else False
