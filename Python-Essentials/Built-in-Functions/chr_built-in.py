#BUILT-IN FUNCTION CHR()
"""
the chr() method converts an integer to its unicode character and returns it
"""
print(chr(97))
# Output: a

print(chr(98))
#  Output: b
print(chr(1114110))
"""
SYNTAX
    chr(number)
PARAMETERS
number - an integer number in the range 0 to 1,114,111
RETURN VALUE
    a unicode character of the corresponding integer argument (in the range 0 to 1,114,111)
    ValueError - for an out of range integer number
    TypeError - for a non-integer argument
"""


print('------------------------------\n')
print(chr(97))
print(chr(65))
print(chr(1200))
print('------------------------------\n')
print(chr(-1000))
print(chr(1114113))
print('------------------------------\n')
print(chr('Ronald'))
print(chr('Lupin'))
print('------------------------------\n')
print('------------------------------\n')
