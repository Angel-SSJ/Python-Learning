# BUILT-IN FUNCTION
"""
The divmode() method takes two numbers are arguments and returns their quotient(cociente) and remainder(resto) in a tuple
SYNTAX
    divmod(number1,number2)
PARAMETERS
    number1 - numerator, can be an integer or a floating point number
    number2 - denominator, can be an integer or a floating point number
RETURN VAlUES
    (quotient, remainder) - a tuple that contains quotient and remainder of the division
    TypeError - for any non-numeric argument
"""

#EXAMPLE 1: Python divmod() with Integer Arguments

print(f'divmod(5,2)={divmod(5,2)}')
print(f'divmod(1,2)={divmod(1,2)}')

#EXAMPLE 2: Python divmod() with Float Arguments

print(f'divmod(5.0, 2)= {divmod(5.0, 2)}')
print(f'divmod(3,8.01)= {divmod(3,8.01)}')
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))


#EXAMPLE 3: Python divmod() with Non-Numeric Arguments
a=divmod('Pobre','Tostado')
print(f'a={a}')

#EXAMPLE 1: Python divmod() with Integer Arguments