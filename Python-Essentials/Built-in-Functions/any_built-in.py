# BUILT-IN FUNCTION ANY()

"""
    The any() function returns True if any element of an iterable is True. If not, it returns False.

"""
boolean_list=['True','False','True']
print(any(boolean_list))

"""
PARAMETERS
the any() function takes an iterable(list,string,dictionary,etc)

RETURN VALUE
    True - if at least one element of an iterable is true
    False - if all elements are false or if an iterable is empty

    Condition                       	        Return Value
        All values are true	                        True
        All values are false	                    False
        One value is true (others are false)	    True
        One value is false (others are true)	    True
        Empty Iterable	                            False
"""


print('----/----/----/----/')
#WORKING WITH LIST
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))

print('----/----/----/----/')
#WORKING WITH STRINGS
# At east one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))

print('----/----/----/----/')
#WORKING WITH DICTIONARIES
# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))