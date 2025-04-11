#OBJECTS
#everything is a object in python

age = 8  # now has access to the properties and methods of all int objects
print(age.real)
print(age.bit_length())
print(age.bit_count())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))
#the id global function provided by python lets you inspect the location in memory for a particular object
