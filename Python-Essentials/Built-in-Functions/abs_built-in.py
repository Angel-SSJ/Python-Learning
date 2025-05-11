# The abs() function returns the absolute value of the given number. If the number is a complex number, abs() return its magnitude.

number=-2
print(abs(number))

# PARAMETERS
'''
abs() method takes a single argument:
    num - a number whose absolute value is to be returned. The number can be enteger, floating number or complex number.
    
Return Value
    for Integers and floating numbers, return absolute value.
    for complex numbers, return magnitude of the number.
'''

integer=-54
print(f'Absolute value is: {abs(integer)}\n')
floating =-3.543
print(f'Absolute value is: {abs(floating)}\n')

complex = (3-4j)
print(f'Magnitude of 3-4j is: {abs(complex)}\n')
print(f'Magnitude of 3-4j is: {abs(complex).imag}\n')

