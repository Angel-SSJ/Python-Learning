# BUILT-IN FUNCTION ENUMERATE()

"""
the enumerate() function adds a counter to an iterable and returns it as an enumerate object(iterator with index and the value)
SYNTAX
    enumerate(iterable, start=0)
PARAMETERS
    iterable - a sequence, an iterator, or objects that support iteration.
    start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start
RETURN VAlUES
    The enumerate() function adds a counter to an iterable and returns it. The returned object is an enumerate object.
    An enumerate object is an iterator that produces a sequence of tuples, each containing an index and the value from the iterable.
    We can convert enumerate objects to lists and tuples using list() and tuple() functions, respectively.
"""
from pandas.tseries.holiday import next_monday

#Example: Python enumerate()
grocery=['bread','milk','butter']
enumerateGrocery=enumerate(grocery)
print(enumerateGrocery)
print(list(enumerateGrocery))

enumerateGrocery=enumerate(grocery,0)
print(list(enumerateGrocery))

#Example: Loop Over an Enumerate Object
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

for count,string in enumerate(grocery):
    print(count,string)

print()

# change the default counter and loop
for count, item in enumerate(grocery, 100):
  print(count, item)

#Access the Next Element
#In Python, we can use the next() function to access the next element from an enumerated sequence. For example,
grocery = ['bread', 'milk', 'butter']

enumerateGrocery = enumerate(grocery)
next_element=next(enumerateGrocery)
print({next_element})
print(next_element)