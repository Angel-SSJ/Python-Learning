# MAP, FILTER, REDUCE
# map() is used to run  a function upon each item in an iterable item like a list
from functools import reduce

numbers = [1, 2, 3]

#when the function is a one-liner its common to use a lambda function

result = map(lambda a: a * 2, numbers)
'''def double(a):
  return a * 2


result = map(double, numbers)'''
print(list(result))

numbers = [1, 2, 3]
'''
def isEven(n):
  return n % 2 == 0
'''
result = filter(lambda n: n % 2 == 0, numbers)
print(list(result))

# reduce is used to calcualte a value out of a sequence like a list

expenses = [('Dinner', 45), ('Car repair', 2000)]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
'''for expense in expenses:
  sum += expense[1]
'''
print(sum)