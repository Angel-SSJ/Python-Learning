# BUILT-IN FUNCTION BIN
"""
converts a specified integer number to its binary representation and returns it
"""
number = 15

# convert 15 to its binary equivalent
print('The binary equivalent of 15 is', bin(number))

"""
SYNTAX
    bin(number)
PARAMETERS
    number - an integer whose binary equivalent is calculated
RETURN VALUE
    the binary string equivalent to the given integer
    TypeError for a non-integer argument
"""

print('---------------------------------')
number = 5

# convert 5 to its binary equivalent
print('The binary equivalent of 5 is:', bin(number))
#In the above example, we have used the bin() method to convert the argument 5 to its binary representation i.e. 101.
#Here, the prefix 0b in the output 0b101 represents that the result is a binary string.
print('---------------------------------')


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def testing(self):
        return self.apple + self.orange + self.grapes


#print('The binary equivalent of quantity is:', bin(Quantity()))
print('---------------------------------')
class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))
print('---------------------------------')
print('---------------------------------')