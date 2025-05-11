# BUILT-IN FUNCTION ASCII()

"""
the ascii() method replaces a non-printable character with its corresponding ascii value and return it.
"""
text = 'Pythön is interesting'
print(ascii(text))

"""
PARAMETERS
    object -can be a python list,set,tuple,dict,ect
RETURN VALUE
    printable equivalent character for a non-printable character in object
"""

print('----/----/----/----/')
text1 = '√ represents square root'

# replace √ with ascii value
print(ascii(text1))

text2 = 'Thör is coming'

# replace ö with ascii value
print(ascii(text2))
print('----/----/----/----/')
#WORKING WITH LIST
list = ['Python', 'öñ', 5]
print(ascii(list))
print('----/----/----/----/')
#WORKING WITH SET
set = {'Π', 'Φ', 'η'}
print(ascii(set))
print('----/----/----/----/')
#WORKING WITH TUPLE
tuple = ('ö', '√', '¶','Ð','ß' )
print(ascii(tuple))

