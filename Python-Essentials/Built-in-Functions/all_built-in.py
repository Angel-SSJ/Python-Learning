# BUILT-IN ALL()

"""
the all() function returns True if all elements in the given iterable are truthy. if not, it returns False
"""

boolean_list=['True','True','True']
result = all(boolean_list)
print(result)

"""
PARAMETERS
    iterable - any iterable which contains the elements
RETURN VALUE
    True -if all elements in an iterable are true
    False -if any element in an iterable is false
    
    When                                	    Return Value
        All values are true	                        True
        All values are false	                    False
        One value is true (others are false)	    False
        One value is false (others are true)	    False
        Empty Iterable	                            True
        
    Note: Truthy values include non-zero numbers, non-empty sequences, and True
          Falsy values include 0, None, False and empty sequences.
"""



# WORKING WITH LIST
print('---/---/---/---/')
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

# WORKING WITH STRINGS
print('---/---/---/---/')
s = "This is good"
print(all(s))
# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))


# WORKING WITH DICTIONARIES
print('---/---/---/---/')
s={0:'False',1:'False'}
print(all(s))
s={2:'True',1:'True'}
print(all(s))
s={1:'True',False:0}
print(all(s))


s={}
print(all(s))

# 0 is false
#'0' is True
s={'0':'True'}
print(all(s))





