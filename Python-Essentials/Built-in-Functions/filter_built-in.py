# BUILT-IN FUNCTION FILTER()

"""
    The filter() function selects elements from an iterable based on the result of a function.
SYNTAX
    filter(function, iterable)
PARAMETERS
    function - a function that runs for each item of an iterable
    iterable - a sequence that needs to be filtered like sets, lists, tuples, etc
RETURN VAlUES
    The filter() function returns an iterator.
"""

# EXAMPLE 1: Example: Filter Vowels From List
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
    vowels=['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False

filtered_vowels=filter(filter_vowels,letters)
vowels=tuple(filtered_vowels)
print(vowels)
"""
    Here's how the above program works:
    each element of letters is passed to the filter_vowels() function
    if flter_vowels() returns True, filter() selects the element
"""

# EXAMPLE 2: USING LAMBA

numbers=[1,2,3,4,5,6,7,8,9]
even_numbers_iterator=filter(lambda x: (x%2==0),numbers)
print(list(even_numbers_iterator))