# BUILT-IN FUNCTION COMPLEX()


"""
SYNTAX
    complex([real[, imag]])
PARAMETERS
    real - real part. If real is omitted, it defaults to 0.
    imag - imaginary part. If imag is omitted, it defaults to 0.

    If the first parameter passed to this method is a string, it will be interpreted
    as a complex number. In this case, the second parameter shouldn't be passed.
RETURN VALUES
    As suggested by the name, complex() method returns a complex number.
    If the string passed to this method is not a valid complex number, ValueError exception is raised.
    Note: The string passed to complex() should be in the form real+imagj or real+imagJ
"""

#EXAMPLE 1
z = complex(1, -2)
print(z)

z = complex(1)
print(z)

z= complex('1-2j')
print(z)
# Example 2: Create complex numbers without Using complex()
#It's possible to create a complex number without using complex() method. For that, you have to put 'j' or 'J' after a number.
a = 2+3j
print('a =',a)
print('Type of a is',type(a))

b = -2j
print('b =',b)
print('Type of b is',type(a))

c = 0j
print('c =',c)
print('Type of c is',type(c))
